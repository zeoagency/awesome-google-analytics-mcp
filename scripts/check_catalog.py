#!/usr/bin/env python3
"""Validate reviewed records, task placement, generated pages and local navigation."""

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

from build_catalog import ROOT, anchor, load_records, render, slug


def check_schema(schema, label, errors, root=None):
    root = schema if root is None else root
    if isinstance(schema, bool):
        return
    if not isinstance(schema, dict):
        errors.append(f'{label}: schema must be an object or boolean.')
        return
    if '$ref' in schema:
        ref = schema['$ref']
        if not ref.startswith('#/'):
            errors.append(f'{label}: expected a local schema reference: {ref}')
        else:
            value = root
            try:
                for part in ref[2:].split('/'):
                    value = value[part.replace('~1', '/').replace('~0', '~')]
            except (KeyError, TypeError):
                errors.append(f'{label}: unresolved reference: {ref}')
    properties = schema.get('properties', {})
    required = schema.get('required', [])
    if not isinstance(required, list) or len(required) != len(set(required)) or ('properties' in schema and not set(required) <= properties.keys()):
        errors.append(f'{label}: required fields do not match properties.')
    for key in ('properties', '$defs', 'definitions', 'patternProperties', 'dependentSchemas'):
        for name, child in schema.get(key, {}).items():
            check_schema(child, f'{label}/{key}/{name}', errors, root)
    for key in ('items', 'additionalProperties', 'not', 'contains', 'if', 'then', 'else', 'propertyNames'):
        if key in schema:
            children = schema[key] if isinstance(schema[key], list) else [schema[key]]
            for child in children:
                check_schema(child, f'{label}/{key}', errors, root)
    for key in ('anyOf', 'oneOf', 'allOf', 'prefixItems'):
        for child in schema.get(key, []):
            check_schema(child, f'{label}/{key}', errors, root)


def validate_records(records, catalog, clients):
    errors = []
    repos = [r['repo'] for r in records]
    if not repos or len(repos) != len(set(repos)):
        errors.append('MCP records must be nonempty and unique.')
    for record in records:
        repo = record['repo']
        if record.get('status') != 'included' or not record.get('review', {}).get('method'):
            errors.append(f'{repo}: missing independent inclusion review.')
        if not re.fullmatch(r'[0-9a-f]{40}', record.get('revision', '')):
            errors.append(f'{repo}: missing pinned revision.')
        tools = record['tools']
        names = [t['name'] for t in tools]
        if record['tool_count'] != len(tools) or len(names) != len(set(names)) or not tools:
            errors.append(f'{repo}: tool count, uniqueness or inventory is invalid.')
        if not any(t['scope'] == 'ga4' for t in tools):
            errors.append(f'{repo}: no implemented GA4 tool.')
        for tool in tools:
            label = f'{repo}/{tool["name"]}'
            if not re.fullmatch(r'[A-Za-z0-9_.-]+', tool['name']):
                errors.append(f'{label}: unsupported tool name.')
            if not isinstance(tool.get('description'), str) or not tool.get('behavior') or not tool.get('schema_origin'):
                errors.append(f'{label}: missing description, implementation or schema provenance.')
            if tool['scope'] not in {'ga4', 'adjacent', 'support'} or tool['effect'] not in {'read', 'write', 'mixed', 'local'}:
                errors.append(f'{label}: invalid scope/effect.')
            if tool['inputSchema'].get('type') != 'object':
                errors.append(f'{label}: input schema must describe an object.')
            check_schema(tool['inputSchema'], label, errors)
            if not tool.get('sources'):
                errors.append(f'{label}: missing pinned source evidence.')
            for source in tool.get('sources', []):
                path = Path(source['path'])
                if path.is_absolute() or '..' in path.parts or not 1 <= source['start_line'] <= source['end_line']:
                    errors.append(f'{label}: invalid source path or lines.')
    placement = []
    by_repo = {r['repo']: r for r in records}
    for group in catalog['groups']:
        if not group['servers'] or not group['description']:
            errors.append(f'{group["title"]}: empty group.')
        for item in group['servers']:
            placement.append(item['repo'])
            if item['repo'] not in by_repo:
                errors.append(f'Unknown grouped server: {item["repo"]}')
                continue
            names = {t['name'] for t in by_repo[item['repo']]['tools'] if t['scope'] == 'ga4'}
            if not item['summary'] or not item['featured_tools'] or not set(item['featured_tools']) <= names:
                errors.append(f'{item["repo"]}: featured tools must be implemented GA4 tools.')
    if sorted(placement) != sorted(repos):
        errors.append('Every MCP must appear in exactly one primary task group.')
    for key in ('label', 'url'):
        values = [c[key].rstrip('/').casefold() for c in clients]
        if len(values) != len(set(values)):
            errors.append(f'Duplicate CLI/SDK {key}.')
    if any(c['category'] not in {'CLI tools', 'SDKs'} for c in clients):
        errors.append('Invalid client category.')
    return errors


def without_fences(content):
    lines = []
    marker = None
    for line in content.splitlines():
        match = re.match(r'^\s*(`{3,}|~{3,})', line)
        if marker:
            if match and match[1][0] == marker[0] and len(match[1]) >= len(marker):
                marker = None
        elif match:
            marker = match[1]
        else:
            lines.append(line)
    return '\n'.join(lines)


def check_links(root):
    errors = []
    content = {p: without_fences(p.read_text()) for p in root.rglob('*.md') if not set(p.parts) & {'.git', 'node_modules'}}
    for document, text in content.items():
        for target in re.findall(r'(?<!!)\[[^\]\n]+\]\(([^\s)]+)\)', text):
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc:
                continue
            destination = (document.parent / unquote(parsed.path)).resolve() if parsed.path else document
            if not destination.is_file() and not (destination.is_dir() and not parsed.fragment):
                errors.append(f'{document.relative_to(root)}: missing local target {target}')
                continue
            if parsed.fragment:
                headings = re.findall(r'^#{1,6} (.+)$', content.get(destination, ''), re.M)
                if unquote(parsed.fragment) not in {anchor(h) for h in headings}:
                    errors.append(f'{document.relative_to(root)}: missing heading {target}')
    return errors


def check():
    records = load_records()
    catalog = json.loads((ROOT / 'data/catalog.json').read_text())
    clients = json.loads((ROOT / 'data/clients.json').read_text())
    errors = validate_records(records, catalog, clients)
    for record in records:
        path = ROOT / f'data/mcps/{slug(record["repo"])}.json'
        if not path.is_file():
            errors.append(f'{record["repo"]}: record filename differs from its repository slug.')
    evidence = (ROOT / 'docs/verification.md').read_text()
    decisions = {}
    for block in re.split(r'^### ', evidence, flags=re.M)[1:]:
        heading, _, body = block.partition('\n')
        match = re.fullmatch(r'`(.+?)` — (Retained|Added|Removed|Excluded)', heading)
        if match:
            if match[1] in decisions:
                errors.append(f'Duplicate verification decision: {match[1]}')
            decisions[match[1]] = (match[2], body)
    expected = {r['repo'] for r in records} | {c['label'] for c in clients}
    actual = {name for name, (status, _) in decisions.items() if status in {'Retained', 'Added'}}
    if expected != actual:
        errors.append('Verification decisions and current catalog entries differ.')
    for name in expected:
        body = decisions.get(name, ('', ''))[1]
        if not re.search(r'Revision: `[0-9a-f]{40}`', body) or not re.search(r'https://github.com/[^\s)]+/(?:blob|tree)/[0-9a-f]{40}/', body):
            errors.append(f'{name}: missing pinned verification evidence.')
    for record in records:
        if f'Revision: `{record["revision"]}`' not in decisions.get(record['repo'], ('', ''))[1]:
            errors.append(f'{record["repo"]}: tool inventory and verification revisions differ.')
    outputs = render()
    for path, expected_content in outputs.items():
        if not path.is_file() or path.read_text() != expected_content:
            errors.append(f'{path.relative_to(ROOT)}: generated page is stale.')
    orphaned = set((ROOT / 'docs/mcps').glob('*.md')) - set(outputs)
    errors.extend(f'{p.relative_to(ROOT)}: orphaned MCP page.' for p in sorted(orphaned))
    errors += check_links(ROOT)
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        return 1
    count = sum(len(r['tools']) for r in records)
    print(f'Catalog OK: {len(records)} MCPs, {count} tool registrations, {len(clients)} CLI/SDK entries; schemas, placement, evidence and links match.')
    return 0


if __name__ == '__main__':
    sys.exit(check())

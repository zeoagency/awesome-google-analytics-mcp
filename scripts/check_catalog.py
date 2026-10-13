#!/usr/bin/env python3
"""Check catalog counts, duplicate links, navigation, and verification coverage."""

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / 'README.md'


def check():
    text = README.read_text()
    errors = []
    sections = list(re.finditer(r'^## ([123])\. (MCP servers|CLI tools|SDKs) \((\d+)\)$', text, re.M))
    if [(s[1], s[2]) for s in sections] != [('1', 'MCP servers'), ('2', 'CLI tools'), ('3', 'SDKs')]:
        errors.append('Expected the three numbered MCP, CLI, and SDK sections.')

    catalog = []
    for index, section in enumerate(sections):
        next_heading = re.search(r'^## ', text[section.end():], re.M)
        end = section.end() + next_heading.start() if next_heading else len(text)
        body = text[section.end():end]
        entries = re.findall(r'^\| \[\*\*(.+?)\*\*\]\((https://[^\s)]+)\) \| (.+) \|$', body, re.M)
        rows = [line for line in body.splitlines() if line.startswith('|') and line != '| Project | What it does |' and not re.fullmatch(r'\|[\s:|\-]+\|', line)]
        if len(rows) != len(entries):
            errors.append(f'{section[2]}: malformed project row.')
        if len(entries) != int(section[3]):
            errors.append(f'{section[2]}: heading says {section[3]}, found {len(entries)} entries.')
        heading = section.group()[3:]
        anchor = re.sub(r'[^\w\- ]', '', heading.lower()).replace(' ', '-')
        toc = f'[{section[2]} ({section[3]})](#{anchor})'
        if toc not in text[:sections[0].start()]:
            errors.append(f'{section[2]}: contents count or anchor differs from the heading.')
        catalog.extend(entries)

    labels = [entry[0].casefold() for entry in catalog]
    urls = [entry[1].rstrip('/').casefold() for entry in catalog]
    if len(labels) != len(set(labels)):
        errors.append('Duplicate catalog entry names.')
    if len(urls) != len(set(urls)):
        errors.append('Duplicate catalog URLs.')

    evidence_path = ROOT / 'docs/verification.md'
    evidence = evidence_path.read_text() if evidence_path.is_file() else ''
    records = {}
    for block in re.split(r'^### ', evidence, flags=re.M)[1:]:
        heading, _, body = block.partition('\n')
        match = re.fullmatch(r'`(.+?)` — (Retained|Added|Removed|Excluded)', heading)
        if match:
            if match[1] in records:
                errors.append(f'Duplicate verification record: {match[1]}')
            records[match[1]] = (match[2], body)
    for label, _, _ in catalog:
        status, body = records.get(label, ('', ''))
        if status not in {'Retained', 'Added'}:
            errors.append(f'Missing inclusion decision: {label}')
        if not re.search(r'Revision: `[0-9a-f]{40}`', body):
            errors.append(f'Missing inspected revision: {label}')
        if not re.search(r'https://github.com/[^\s)]+/(?:blob|tree)/[0-9a-f]{40}/', body):
            errors.append(f'Missing pinned source evidence: {label}')
    included = {label for label, (status, _) in records.items() if status in {'Retained', 'Added'}}
    if included != {entry[0] for entry in catalog}:
        errors.append('Verification inclusion decisions and catalog entries differ.')

    for document in ROOT.rglob('*.md'):
        if any(part in {'node_modules', '.git', '.tmp', 'scratch'} for part in document.parts):
            continue
        content = document.read_text()
        for target in re.findall(r'(?<!!)\[[^\]\n]+\]\(([^\s)]+)\)', content):
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc:
                continue
            destination = document.parent / unquote(parsed.path) if parsed.path else document
            if not destination.is_file():
                errors.append(f'{document.relative_to(ROOT)}: missing local target {target}')
                continue
            if parsed.fragment:
                headings = re.findall(r'^#{1,6} (.+)$', destination.read_text(), re.M)
                anchors = {re.sub(r'[^\w\- ]', '', h.lower()).replace(' ', '-') for h in headings}
                if unquote(parsed.fragment) not in anchors:
                    errors.append(f'{document.relative_to(ROOT)}: missing heading {target}')

    if errors:
        print('\n'.join(errors), file=sys.stderr)
        return 1
    print(f'Catalog OK: {len(catalog)} entries; counts, links, and verification coverage match.')
    return 0


if __name__ == '__main__':
    sys.exit(check())

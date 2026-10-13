#!/usr/bin/env python3
"""Render the catalog, tool index and server pages from reviewed source records."""

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_records():
    return [json.loads(p.read_text()) for p in sorted((ROOT / 'data/mcps').glob('*.json'))]


def slug(repo):
    return repo.replace('/', '--').lower()


def anchor(name):
    return re.sub(r'[^\w\- ]', '', name.lower()).replace(' ', '-')


def cell(value):
    return str(value).replace('|', '&#124;').replace('\n', ' ').strip()


def prose(value):
    """Autolink bare URLs without changing existing Markdown links or code spans."""
    parts = re.split(r'(`[^`]*`|\[[^\]]*\]\([^)]*\)|<https?://[^>]*>)', value)
    for i in range(0, len(parts), 2):
        parts[i] = re.sub(r'https?://[^\s<>]+', lambda m: '<' + m[0].rstrip('.,;') + '>' + m[0][len(m[0].rstrip('.,;')):], parts[i])
    return ''.join(parts)


def fence(value, language=''):
    length = max([3] + [len(m[0]) + 1 for m in re.finditer(r'`{3,}', value)])
    marker = '`' * length
    # JSON records preserve source whitespace; presentation strips trailing spaces.
    displayed = '\n'.join(line.rstrip() for line in value.rstrip().splitlines())
    return f'{marker}{language}\n{displayed}\n{marker}\n'


def source_link(record, source):
    path = source['path']
    target = f'https://github.com/{record["repo"]}/blob/{record["revision"]}/{path}'
    target += f'#L{source["start_line"]}-L{source["end_line"]}'
    return f'[{cell(path)}:{source["start_line"]}]({target})'


def schema_type(schema):
    if isinstance(schema, bool):
        return 'any' if schema else 'never'
    if '$ref' in schema:
        return schema['$ref'].rsplit('/', 1)[-1]
    for keyword in ('anyOf', 'oneOf'):
        if keyword in schema:
            return ' or '.join(dict.fromkeys(schema_type(s) for s in schema[keyword]))
    value = schema.get('type', 'any')
    if isinstance(value, list):
        return ' or '.join(value)
    if value == 'array':
        return f'array of {schema_type(schema.get("items", {}))}'
    return value


def server_page(record):
    tools = record['tools']
    repo = record['repo']
    page = f'# {repo}\n\n[Catalog](../../README.md) · [All tool names](../tool-index.md) · [Upstream](https://github.com/{repo}) · [JSON](../../data/mcps/{slug(repo)}.json)\n\n'
    ga = sum(t['scope'] == 'ga4' for t in tools)
    page += f'**{len(tools)} tools:** {ga} GA4, {len(tools) - ga} other-service or server-support tools. Reviewed source: [`{record["revision"][:12]}`](https://github.com/{repo}/tree/{record["revision"]}).\n\n'
    page += 'Descriptions and parameter schemas come from the registered source definitions. Generated schemas are reconstructed from annotations or validators; live `tools/list` and authenticated API calls were not run. Loose objects remain loose.\n\n'
    if record.get('notes'):
        page += '<details>\n<summary>Exposure and compatibility notes</summary>\n\n'
        for note in record['notes']:
            page += f'- {prose(cell(note))}\n'
        page += '\n</details>\n\n'
    page += '## Tools\n\n| Tool | Scope | Effect |\n| --- | --- | --- |\n'
    scopes = {'ga4': 'GA4', 'adjacent': 'Other service', 'support': 'Server support'}
    for tool in tools:
        page += f'| [`{tool["name"]}`](#{anchor(tool["name"])}) | {scopes[tool["scope"]]} | {tool["effect"]} |\n'
    for tool in tools:
        page += f'\n## {tool["name"]}\n\n{prose(tool["behavior"])}\n\n'
        if tool['description']:
            page += '<details>\n<summary>Full registered description</summary>\n\n'
            page += fence(tool['description'], 'text') + '\n</details>\n\n'
        else:
            page += 'The registration does not provide a tool description.\n\n'
        schema = tool['inputSchema']
        properties = schema.get('properties', {})
        required = set(schema.get('required', []))
        if properties:
            page += '| Parameter | Required by schema | Type | Default |\n| --- | --- | --- | --- |\n'
            for name, prop in properties.items():
                default = json.dumps(prop['default'], ensure_ascii=False) if 'default' in prop else 'Not declared'
                page += f'| `{cell(name)}` | {"Yes" if name in required else "No"} | {cell(schema_type(prop))} | {cell(default)} |\n'
            page += '\n'
        else:
            page += 'No named input parameters are declared.\n\n'
        page += '<details>\n<summary>Full input schema: nested fields, descriptions and constraints</summary>\n\n'
        page += fence(json.dumps(schema, ensure_ascii=False, indent=2), 'json') + '\n</details>\n\n'
        if tool.get('signature'):
            page += 'Handler signature (including defaults not emitted by a generated schema):\n\n'
            page += fence(tool['signature'], 'python') + '\n'
        if tool['notes']:
            for note in tool['notes']:
                page += f'- {prose(cell(note))}\n'
            page += '\n'
        page += 'Source: ' + ' · '.join(source_link(record, s) for s in tool['sources']) + '.\n'
    return page


def tool_index(records):
    providers = defaultdict(list)
    for record in records:
        for tool in record['tools']:
            providers[tool['name']].append((record, tool))
    total = sum(len(r['tools']) for r in records)
    page = '# Tool index\n\n[Catalog](../README.md)\n\n'
    page += f'**{len(providers)} distinct tool names · {total} tool registrations · {len(records)} MCP servers.** Use your browser’s Find command to search this alphabetical index. Each provider link opens that tool’s description and complete parameters.\n\n'
    page += 'Lists every registered tool, including other services and server support inside multi-service MCPs. Identical names can have different parameters and behavior; inspect the provider’s page.\n\n| Tool name | Providers |\n| --- | --- |\n'
    for name in sorted(providers, key=str.casefold):
        links = []
        for record, tool in sorted(providers[name], key=lambda pair: pair[0]['repo'].casefold()):
            target = f'mcps/{slug(record["repo"])}.md#{anchor(name)}'
            tag = f' ({tool["scope"]}, {tool["effect"]})'
            links.append(f'[{record["repo"]}]({target}){tag}')
        page += f'| `{cell(name)}` | ' + ' · '.join(links) + ' |\n'
    return page


def main_page(records, catalog, clients):
    included = {r['repo']: r for r in records}
    total = sum(len(r['tools']) for r in records)
    page = '# Awesome Google Analytics MCP [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)\n\n'
    page += '> Discover what Google Analytics 4 MCP tools actually do, with complete tool references.\n\n'
    ga = sum(t['scope'] == 'ga4' for r in records for t in r['tools'])
    page += f'**{len(records)} MCP servers · {ga} GA4 tool registrations.** [Find a tool by name](docs/tool-index.md) or browse the tasks below. Server pages include every tool, full descriptions and complete input schemas.\n\n'
    page += f'Grouped by implemented GA4 behavior, with one primary placement per server. The [tool index](docs/tool-index.md) covers all {total} registrations, including other services, server support and optional tools. Counts describe reviewed source, not live availability. [Source review and decisions](docs/verification.md).\n\n## Contents\n\n'
    groups = catalog['groups']
    for i, group in enumerate(groups, 1):
        count = len(group['servers'])
        heading = f'{i}. {group["title"]}'
        page += f'{i}. [{group["title"]} ({count})](#{anchor(heading)})\n'
    for offset, category in enumerate(('CLI tools', 'SDKs'), len(groups) + 1):
        count = sum(c['category'] == category for c in clients)
        page += f'{offset}. [{category} ({count})](#{anchor(f"{offset}. {category}")})\n'
    for i, group in enumerate(groups, 1):
        count = len(group['servers'])
        page += f'\n## {i}. {group["title"]}\n\n*{count} {"server" if count == 1 else "servers"}. {group["description"]}*\n\n'
        page += '| MCP server | What its tools do | Tool reference |\n| --- | --- | --- |\n'
        for item in group['servers']:
            record = included[item['repo']]
            path = f'docs/mcps/{slug(item["repo"])}.md'
            examples = ', '.join(f'[`{name}`]({path}#{anchor(name)})' for name in item['featured_tools'])
            ga_count = sum(t['scope'] == 'ga4' for t in record['tools'])
            count_label = f'{ga_count} GA4 / {len(record["tools"])} total' if ga_count != len(record['tools']) else f'{ga_count} {"tool" if ga_count == 1 else "tools"}'
            page += f'| [**{item["repo"]}**](https://github.com/{item["repo"]}) | {cell(item["summary"])} {examples}. | [{count_label}]({path}) |\n'
    for offset, category in enumerate(('CLI tools', 'SDKs'), len(groups) + 1):
        page += f'\n## {offset}. {category}\n\n| Project | What it does |\n| --- | --- |\n'
        for item in clients:
            if item['category'] == category:
                page += f'| [**{item["label"]}**]({item["url"]}) | {item["description"]} |\n'
    return page


def render():
    records = load_records()
    if not records or any(r.get('status') != 'included' or not r.get('review', {}).get('method') for r in records):
        raise ValueError('Only included records with an independent review can be rendered.')
    catalog = json.loads((ROOT / 'data/catalog.json').read_text())
    clients = json.loads((ROOT / 'data/clients.json').read_text())
    outputs = {
        ROOT / 'README.md': main_page(records, catalog, clients),
        ROOT / 'docs/tool-index.md': tool_index(records),
    }
    for record in records:
        outputs[ROOT / f'docs/mcps/{slug(record["repo"])}.md'] = server_page(record)
    return outputs


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Fail if rendered pages differ from tracked data.')
    args = parser.parse_args()
    outputs = render()
    stale = []
    for path, content in outputs.items():
        if args.check:
            if not path.is_file() or path.read_text() != content:
                stale.append(str(path.relative_to(ROOT)))
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content)
    expected = {path for path in outputs if path.parent == ROOT / 'docs/mcps'}
    unexpected = set((ROOT / 'docs/mcps').glob('*.md')) - expected
    if unexpected:
        stale += [str(p.relative_to(ROOT)) for p in sorted(unexpected)]
    if stale:
        parser.exit(1, 'Generated pages differ: ' + ', '.join(stale) + '\n')
    print(f'{"Checked" if args.check else "Rendered"} {len(outputs)} catalog pages.')


if __name__ == '__main__':
    main()

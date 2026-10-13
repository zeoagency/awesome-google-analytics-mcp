"""Regression checks for coverage, schema references and source text rendering."""

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from build_catalog import ROOT, load_records, server_page, tool_index
from check_catalog import check_links, check_schema, validate_records


class CatalogTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.records = load_records()
        cls.catalog = json.loads((ROOT / 'data/catalog.json').read_text())
        cls.clients = json.loads((ROOT / 'data/clients.json').read_text())

    def test_duplicate_placement_is_rejected(self):
        catalog = copy.deepcopy(self.catalog)
        catalog['groups'][1]['servers'].append(catalog['groups'][0]['servers'][0])
        self.assertIn('Every MCP must appear in exactly one primary task group.', validate_records(self.records, catalog, self.clients))

    def test_unreviewed_record_is_rejected(self):
        records = copy.deepcopy(self.records)
        records[0].pop('review')
        self.assertTrue(any('missing independent inclusion review' in e for e in validate_records(records, self.catalog, self.clients)))

    def test_featured_other_service_tool_is_rejected(self):
        catalog = copy.deepcopy(self.catalog)
        item = catalog['groups'][2]['servers'][1]
        record = next(r for r in self.records if r['repo'] == item['repo'])
        item['featured_tools'] = [next(t['name'] for t in record['tools'] if t['scope'] == 'adjacent')]
        self.assertTrue(any('featured tools must be implemented GA4' in e for e in validate_records(self.records, catalog, self.clients)))

    def test_nested_unresolved_reference_is_rejected(self):
        schema = {'type': 'object', 'properties': {'reports': {'type': 'array', 'items': {'$ref': '#/$defs/missing'}}}}
        errors = []
        check_schema(schema, 'report', errors)
        self.assertEqual(len(errors), 1)
        self.assertIn('unresolved reference', errors[0])

    def test_composition_required_selector_is_valid(self):
        schema = {'type': 'object', 'properties': {'a': {}, 'b': {}}, 'anyOf': [{'required': ['a']}, {'required': ['b']}]}
        errors = []
        check_schema(schema, 'selector', errors)
        self.assertEqual(errors, [])

    def test_shared_name_links_to_every_provider(self):
        records = [r for r in self.records if any(t['name'] == 'run_report' for t in r['tools'])]
        index = tool_index(records)
        row = next(line for line in index.splitlines() if line.startswith('| `run_report` |'))
        self.assertGreater(len(records), 1)
        for record in records:
            self.assertIn(f'[{record["repo"]}]', row)

    def test_source_examples_are_fenced_and_schema_is_complete(self):
        record = copy.deepcopy(self.records[0])
        tool = record['tools'][0]
        tool['description'] = '## Example heading\n[example](nonexistent.md)\n```json\n{}\n```'
        page = server_page(record)
        self.assertIn('````text\n' + tool['description'], page)
        self.assertIn(json.dumps(tool['inputSchema'], ensure_ascii=False, indent=2), page)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'example.md').write_text('# Example\n\n```text\n[upstream example](missing.md)\n```\n')
            self.assertEqual(check_links(root), [])
            (root / 'example.md').write_text('# Example\n\n[broken](missing.md)\n')
            self.assertEqual(len(check_links(root)), 1)


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/env python3
"""
Test suite verifying repository integrity, mathematical count parity,
anchor resolution, matrix geometry, and description uniqueness.
"""

import json
import re
from pathlib import Path
import pytest

ROOT = Path(__file__).resolve().parent.parent
README_PATH = ROOT / "README.md"
REGISTRY_PATH = ROOT / "data" / "normalized_project_registry.json"
TAXONOMY_PATH = ROOT / "specs" / "04-taxonomy-blueprint.json"
DESCRIPTIONS_PATH = ROOT / "data" / "differentiated_descriptions.json"
COUNTS_PATH = ROOT / "data" / "taxonomy_counts.json"

@pytest.fixture(scope="module")
def readme_text():
    with open(README_PATH, "r", encoding="utf-8") as f:
        return f.read()

@pytest.fixture(scope="module")
def registry():
    with open(REGISTRY_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

@pytest.fixture(scope="module")
def taxonomy():
    with open(TAXONOMY_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

@pytest.fixture(scope="module")
def descriptions():
    with open(DESCRIPTIONS_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

@pytest.fixture(scope="module")
def counts():
    with open(COUNTS_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def test_project_count_parity(readme_text, registry, taxonomy, counts):
    """Verify exactly 63 tools across all sources with zero drift."""
    assert len(registry) == 63, f"Registry has {len(registry)} projects, expected 63"
    assert counts["total_index_projects"] == 63, f"Counts total is {counts['total_index_projects']}, expected 63"
    assert taxonomy["total_projects"] == 63

    # Count table rows in README.md (excluding comparison matrix)
    # Project rows start with | <a id="..."
    catalog_rows = re.findall(r'^\|\s*<a id="[^"]+"></a>\[\*\*', readme_text, re.MULTILINE)
    assert len(catalog_rows) == 63, f"README has {len(catalog_rows)} catalog entries, expected 63"


def test_category_and_subcategory_counts(readme_text, taxonomy, counts):
    """Verify category banners and subcategory counts match mathematical ground truth."""
    for cat in taxonomy["categories"]:
        cat_id = cat["id"]
        cat_count = cat["count"]
        # Check H2 banner: *N projects...*
        banner_pattern = rf"## {cat_id}\. [^\n]+\n\n\*{cat_count} projects\."
        assert re.search(banner_pattern, readme_text), f"Missing or mismatched count banner for category {cat_id}"

        for sub in cat["subcategories"]:
            sub_name = re.escape(sub["name"])
            sub_count = len(sub["projects"])
            proj_word = "project" if sub_count == 1 else "projects"
            sub_banner_pattern = rf"### {sub_name}\n\n\*{sub_count} {proj_word}\."
            assert re.search(sub_banner_pattern, readme_text), f"Missing or mismatched subcategory banner for {sub['name']}"


def test_comparison_matrix_geometry(readme_text):
    """Verify the comparison matrix conforms to column <= 20 and row <= 200 bounds."""
    # Find Developer Comparison Matrix table
    match = re.search(r"## Developer Comparison Matrix\s*\n\n\*.*?\*\s*\n\n(\|.*?\n\|[-:\s|]+\n(?:\|.*?\n)+)", readme_text)
    assert match, "Developer Comparison Matrix table not found in README.md"
    table_text = match.group(1).strip()
    table_lines = table_text.splitlines()

    headers = [col.strip() for col in table_lines[0].split("|")[1:-1]]
    num_columns = len(headers)
    assert num_columns <= 20, f"Comparison matrix has {num_columns} columns, expected <= 20"
    assert num_columns == 16, f"Expected 16 columns, got {num_columns}"

    data_rows = table_lines[2:]
    num_rows = len(data_rows)
    assert num_rows == 63, f"Expected 63 data rows in comparison matrix, got {num_rows}"
    assert num_rows <= 200, f"Comparison matrix exceeds 200 rows limit ({num_rows})"


def test_two_stage_linking_and_anchors(readme_text, registry):
    """Verify that every link in the comparison matrix resolves to an anchor in the catalog."""
    # Extract comparison table links: [**owner/repo**](#anchor)
    matrix_links = re.findall(r'\|\s*\[\*\*([^\]]+)\*\*\]\(#([^)]+)\)', readme_text)
    assert len(matrix_links) == 63, f"Expected 63 comparison matrix links, found {len(matrix_links)}"

    # Extract all HTML anchors: <a id="anchor"></a>
    anchors = set(re.findall(r'<a id="([^"]+)"></a>', readme_text))
    assert len(anchors) == 63, f"Expected 63 unique HTML anchors, found {len(anchors)}"

    for repo_display, anchor in matrix_links:
        assert anchor in anchors, f"Comparison matrix link #{anchor} does not resolve to any <a id=\"{anchor}\">"


def test_description_uniqueness_and_quality(descriptions):
    """Verify that descriptions are unique, concise, verb-led, and devoid of marketing fluff."""
    assert len(descriptions) == 63
    seen_texts = set()
    banned_phrases = ["great tool", "amazing", "powerful mcp", "best in class", "super fast", "extremely"]

    for slug, entry in descriptions.items():
        desc = entry["description"].strip()
        assert desc not in seen_texts, f"Duplicate description found for {slug}"
        seen_texts.add(desc)

        words = desc.split()
        assert 10 <= len(words) <= 45, f"Description for {slug} has {len(words)} words, expected 10-45"

        lower = desc.lower()
        for phrase in banned_phrases:
            assert phrase not in lower, f"Banned marketing phrase '{phrase}' found in {slug}: {desc}"


def test_no_catch_all_categories(taxonomy):
    """Verify that no category uses forbidden catch-all labels."""
    forbidden = ["misc", "miscellaneous", "other", "others", "general", "various"]
    for cat in taxonomy["categories"]:
        cat_lower = cat["name"].lower()
        for f in forbidden:
            assert f != cat_lower, f"Forbidden catch-all category name: {cat['name']}"
        for sub in cat["subcategories"]:
            sub_lower = sub["name"].lower()
            for f in forbidden:
                assert f != sub_lower, f"Forbidden catch-all subcategory name: {sub['name']}"

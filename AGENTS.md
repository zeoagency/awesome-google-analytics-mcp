# AGENTS.md

This document provides operational instructions, architectural invariants, and verification protocols for AI coding and research agents working in `awesome-google-analytics-mcp`.

---

## 1. Information Architecture & Structural Invariants

1. **Information Architecture Derived from `awesome-herdr`**:
   - Title + Awesome badge banner.
   - One-sentence positioning blockquote.
   - Official links line separated by middle dots (` · `).
   - Horizontal rule `---`.
   - `## Contents` with numbered top-level categories and parenthesized counts `(N)`, followed by nested unnumbered subcategory jump links with parenthesized counts `(M)`.
   - Developer Comparison Table ($\le 20$ columns, $\le 200$ rows) with two-stage linking.
   - Numbered top-level category sections (`## 1. <Category Name>`) with italicized project counts and scope description (`*N projects. Explanation.*`).
   - Subcategory sections (`### <Subcategory Name>`) with italicized subcategory counts and scope description (`*M projects. Explanation.*`).
   - Compact Markdown tables: `| Project | What it does |`.
   - Bold repository links: `[**owner/repo**](url)`.
   - Terminal sections: `## Resources` and `## Reference`.

2. **Root Minimalism**:
   - Zero tutorial sprawl in the root catalog.
   - Jump links must allow 1-click navigation from Contents to any category, subcategory, or comparison row.

3. **Mathematical Count Reconciliation**:
   - Contents count == Section intro count == Sum of subcategory counts == Sum of table rows.
   - Counts are managed programmatically via `scripts/sync_counts.py`. Never edit counts manually.

4. **Two-Stage Linking Model**:
   - Developer Comparison Table cells link internally to section anchors in the README (`#owner--repo`).
   - Detailed project table links point externally to upstream GitHub repositories.

5. **Markdownlint Rules**:
   - Adhere to `.markdownlint.yml` (`MD013` line length disabled for tables, `MD033` inline HTML enabled for anchors).

---

## 2. Evidence Grounding & Bounding Rules

- Every claim regarding API coverage (Data API, Admin API, Realtime, Measurement Protocol write-back), local storage (DuckDB/SQLite), and authentication (OAuth PKCE, Service Account, Firestore) must trace directly to verified source code in `data/normalized_project_registry.json`.
- Generic, unverified claims or marketing boilerplate are strictly prohibited.

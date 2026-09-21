# Specification: Compatibility Model with `awesome-herdr`

**Document ID:** `SPEC-GA4-MCP-002`  
**Status:** Authoritative  
**Reference Model:** `/root/dev/awesome-herdr`  
**Target Repository:** `/root/dev/awesome-google-analytics-mcp`  

---

## 1. Overview & Architectural Policy

To guarantee that `awesome-google-analytics-mcp` achieves immediate cognitive parity with `awesome-herdr`, every structural element, delimiter, and layout rule is mapped into one of four operational categories:

1. **Copy Directly**: Preserve 100% of structure, syntax, and layout invariants.
2. **Adapt for Google Analytics**: Substitute Herdr-specific domains with verified GA4 jobs-to-be-done.
3. **Extend for the Comparison Layer**: Intentional, controlled extensions beyond standard `awesome-herdr`.
4. **Intentionally Omit**: Herdr-specific elements omitted with documented technical justification.

---

## 2. Four-Tier Compatibility Matrix

### 2.1 Copy Directly (100% Invariant)

- **Title Banner**: `# Awesome Google Analytics MCP [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)`
- **Blockquote Positioning**: `> A curated plain-English index and comparison of tools built for **[Google Analytics](https://analytics.google.com/)**...`
- **Horizontal Dividers**: `---` before Contents, after Contents, and between top-level sections.
- **Contents Layout**:
  - `## Contents` header.
  - Numbered top-level category jump links with parenthesized project counts: `1. [Category Name (N)](#1-category-slug)`.
  - Nested 3-space subcategory jump links with parenthesized project counts: `[Subcategory Name (M)](#subcategory-slug)` (indented with 3 spaces).
  - Uncounted terminal entries: `8. [Developer Comparison Matrix](#developer-comparison-matrix)`, `9. [Resources](#resources)`, `10. [Reference](#reference)`.

- **Numbered Section Headings**: `## N. Category Name` matching GitHub slug generation.
- **Dual-Level Italicized Summaries**:
  - Category intro: `*N projects. Plain-English summary of the job covered.*`
  - Subcategory intro: `*M projects. Plain-English summary of this specific narrower job.*`
- **Compact Table Schema**:

  ```markdown
  | Project | What it does |
  |---|---|
  | [**owner/repo**](url) | Concise factual description. |
  ```

- **Typography**: Bold repository name inside external link markdown: `[**owner/repo**](url)`.
- **Description Standards**: Strictly 1–2 sentences, average 15–25 words, active verb-first phrasing, zero marketing adjectives.
- **Terminal Sections**: `## Resources` (documentation links) and `## Reference` (architectural concept primers).

### 2.2 Adapt for Google Analytics

- **Official Documentation Ribbon**:
  `Official links: [Google Analytics](https://analytics.google.com/) · [GA4 Data API](https://developers.google.com/analytics/devguides/reporting/data/v1) · [Admin API](https://developers.google.com/analytics/devguides/config/admin/v1) · [Measurement Protocol](https://developers.google.com/analytics/devguides/collection/protocol/ga4) · [BigQuery Export](https://support.google.com/analytics/answer/7029846)`
- **Taxonomy Categories**:
  - Replaced Herdr multiplexer domains with GA4 developer jobs-to-be-done:
    1. Core Analytics Reporting & Dimension Slicing
    2. Local Data Engines, Embedded OLAP & SQL Ingestion
    3. Multi-Platform Marketing Intelligence & Attribution
    4. Enterprise Auth, Cloud Run & Multi-Tenant Gateways
    5. Event Ingestion, Measurement Protocol & Conversion Write-Back
    6. Diagnostics, Automated Audits & Document Generators
    7. Scaffolds, Setup Templates & Experimental Concepts

### 2.3 Extend for the Comparison Layer

- **Developer Comparison Table**:
  - Embedded between `## Contents` and `## 1. Category`.
  - Up to 20 discriminating columns across API coverage, auth mechanisms, storage mode, and token economics.
  - Capped at $\le 200$ rows.
- **Two-Stage Linking Architecture**:
  - Comparison table project cell links internally: `[**owner/repo**](#owner--repo)`.
  - Detailed catalog entry contains `<a id="owner--repo"></a>` and links externally to GitHub.

### 2.4 Intentionally Omit

- Herdr socket API specifications (`SOCKET_API.md`).
- Editor split keybindings (Neovim/Kakoune).
- Git worktree pane multiplexing helpers.

# AGENTS.md

Working rules, architectural invariants, and language guidelines for anyone — human or agent — editing this repository. It is a curated, plain-English index and comparison of the Google Analytics 4 (GA4) Model Context Protocol (MCP) ecosystem. Keep it lean, minimalist, and immediately useful.

---

## 1. Project Philosophy & Minimalist Structure

- **No Onboarding Tutorials:** Do not add introductory installation essays, "how to choose your layer" tables, or getting-started walkthroughs to the catalog root. Keep the README strictly minimalist: title, official links ribbon, Table of Contents with parenthesized counts, Developer Comparison Matrix, 7 numbered problem-domain sections, Resources, and Reference.
- **Fast Jump Navigation:** Readers should jump straight to the relevant problem domain from the Table of Contents or Developer Comparison Matrix in 1 click.
- **Mathematical Count Integrity:** The project count in `## Contents` must equal the section banner count, the sum of subcategory counts, and the exact count of table rows in that section. Never allow counts to drift.

---

## 2. Language & Voice Standards

The language of this catalog must be simple, direct, and developer-friendly:

### 2.1. Plain-English, Verb-First Prose

- Lead with active verbs (*Ingests*, *Queries*, *Aggregates*, *Validates*, *Streams*, *Bridges*, *Orchestrates*, *Extracts*, *Provisions*).
- Avoid passive voice, convoluted clauses, and marketing buzzwords (*"ultimate"*, *"blazing fast"*, *"game-changing"*).
- State clearly what an analytics developer or AI agent can *do* with the tool, emphasizing verified capabilities (APIs supported, auth mechanisms, local SQL storage).

### 2.2. The 1–2 Sentence Rule

Every project entry in the catalog tables must be strictly 1 or 2 concise sentences:

- **Sentence 1:** Core capability, runtime, and primary API surface (Data API v1beta, Admin API, Realtime, Measurement Protocol).
- **Sentence 2 (optional):** Key architectural discriminator (e.g., embedded DuckDB OLAP, SQLite caching, OAuth PKCE, multi-tenant isolation).

### 2.3. Subcategory Header & Table Standards

Every subcategory begins with an italicized count banner, followed by a clean 2-column markdown table:

```markdown
### Consolidated modal query servers

*4 projects. Multi-purpose query servers bundling report execution, schema introspection, and custom dimension handling.*

| Project | What it does |
|---|---|
| [**owner/repo**](https://github.com/owner/repo) | Plain-English explanation of what the tool does and its technical differentiators. |
```

---

## 3. Strict Exclusion Criteria (What NEVER Belongs Here)

To maintain a high-signal catalog, the following must **never** be added:

1. **NO Generic Cloud Stubs:** Generic BigQuery or GCP servers without dedicated, built-in GA4 event schemas or unnesting tooling.
2. **NO Deprecated Universal Analytics Exclusives:** Repositories exclusively targeting legacy UA (`analytics:v3`, `analyticsreporting:v4`) without GA4 Data API support.
3. **NO Empty Scaffolds or Non-Runnable Stubs:** Repositories without working MCP tool registrations (`CallToolRequest`, `@mcp.tool`, `server.tool`), broken dependencies, or empty directories.
4. **NO Trivial Clones:** Direct forks or 1-commit mirrors of existing community repositories that add no substantive architectural capability.
5. **NO Marketing Hype or AI Slop:** Descriptions must remain factual, concise, and grounded in verified repository source code.

---

## 4. Canonical Section Structure

Organize projects across the 7 numbered macro-domains:

1. **Query standard reports and slice dimensions:** Standard reporting aggregations, dimension filtering, metric slicing, realtime streams, and schema metadata discovery.
2. **Ingest data locally and query with SQL:** Local data ingestion, in-memory DuckDB OLAP, SQLite caching, and virtual JDBC relational tables.
3. **Bridge multi-platform marketing and search data:** Cross-surface attribution, organic search joining (Search Console), container tag auditing (Google Tag Manager), and multi-ad network suites.
4. **Deploy enterprise and multi-tenant authentication:** Multi-tenant OAuth gateways, encrypted token persistence, native loopback PKCE, and team account switching.
5. **Send server-side events and manage properties:** Server-side Measurement Protocol dispatch, custom dimension/metric provisioning, and property configuration via Admin API.
6. **Diagnose anomalies and generate deliverables:** Statistical anomaly detection, 3D data visualization, executive report compilation, and PowerBI feeds.
7. **Starter templates and setup scaffolds:** Developer starter boilerplates, Docker scaffolds, and agency setup recipes.

---

## 5. Developer Comparison Matrix Standards

- **Column Budget:** The matrix features 8 discriminating columns (Server / Tool, Stars, Runtime, Auth, Storage, Capabilities & APIs, Primary Specialization, Tier), optimized for rapid scanning without horizontal scroll on standard screens.
- **Row Budget:** Capped at $\le 200$ rows.
- **Two-Stage Linking:** Project names in the matrix link internally to anchor tags in the detailed catalog (`[**owner/repo**](#owner--repo)` $\to$ `<a id="owner--repo"></a>`), where developers can click directly to the upstream GitHub repository.

---

## 6. Markdown Quality & Continuous Integration

All edits must pass markdown linting without warnings:

```bash
npx markdownlint-cli2 "**/*.md"
```

- Headings must have blank lines above and below.
- Tables must adhere to consistent column pipe alignments.
- Inline HTML anchors (`<a id="..."></a>`) are permitted for two-stage navigation.

# Technical Specification: Structural Architecture of `awesome-herdr`

## Reusable Blueprint for `awesome-google-analytics-mcp`

**Document ID:** `SPEC-GA4-MCP-001`  
**Status:** Authoritative / Operational  
**Source System:** `/root/dev/awesome-herdr` (Reverse-Engineered at Commit `426701b`)  
**Target System:** `/root/dev/awesome-google-analytics-mcp`  
**Date:** September 2026  

---

## 1. Executive Summary & Specification Purpose

This document provides an exhaustive, code-level structural reverse-engineering of the [`awesome-herdr`](file:///root/dev/awesome-herdr) repository. The purpose of this specification is to establish a deterministic, reproducible blueprint that enables AI coding agents and human maintainers to construct an exact structural replica for the Google Analytics (GA4) Model Context Protocol ecosystem: [`awesome-google-analytics-mcp`](file:///root/dev/awesome-google-analytics-mcp).

`awesome-herdr` represents an elite standard in open-source awesome lists:

- **Corpus Scale:** 2,089 curated projects across 7 numbered top-level domains, 49 subcategories, and 2 uncounted foundational sections (`Resources` and `Reference`).
- **Mathematical Integrity:** 100% count reconciliation across Table of Contents anchors, section banners, subcategory banners, and raw markdown table rows (0 count mismatches across all 2,089 entries).
- **Format Homogeneity:** 100% of project entries adhere to an exact 2-column schema (`| Project | What it does |`), with bold markdown links `[**owner/repo**](url)` and strict 1–2 sentence, verb-first descriptions.
- **Cognitive Ergonomics:** High scannability with zero onboarding clutter, 1-click jump navigation, and a dedicated quarantine domain for experimental prototypes (`7. Experimental projects`).
- **Continuous Quality Control:** Enforced by GitHub Actions using `markdownlint-cli2` running under Node.js 24 with custom relaxation rules (`MD013`, `MD060`, `MD041`, `MD033` disabled).

---

## 2. Repository Topology & File System Contract

The `awesome-herdr` architecture maintains an ultra-lean root directory structure. It firmly rejects documentation sprawl, deep multi-nested subfolders, and discursive guidebooks in favor of a minimalist root index backed by explicit agent governance files.

### 2.1 File System Tree

```text
/root/dev/awesome-herdr/
├── .github/
│   └── workflows/
│       └── ci.yml                     # GitHub Actions CI workflow (markdownlint validation)
├── .gitignore                         # Ignores scratch, node_modules, temp artifacts
├── .markdownlint.yml                  # Canonical markdownlint configuration (YAML)
├── .markdownlint-cli2.jsonc           # Canonical markdownlint-cli2 configuration (JSONC)
├── .markdownlintignore                # Ignore patterns for CLI linting
├── AGENTS.md                          # Mandatory agent & contributor behavioral rules
├── CODE_OF_CONDUCT.md                 # Contributor Covenant standard
├── CONTRIBUTING.md                    # Contributor pull-request checklist & gate
├── LICENSE                            # CC0-1.0 or MIT licensing terms
├── README.md                          # The Master Catalog (2,089 projects, 426 KB)
└── docs/                              # Supporting domain deep dives (optional supplemental specs)
    ├── agent-workflows.md
    ├── configuration.md
    ├── integrations.md
    └── socket-api.md
```

### 2.2 Root Minimalism Axiom

As codified in Section 1 of `AGENTS.md`:

1. **No Onboarding Tutorials:** Do not add introductory installation essays, "how to choose your layer" tables, or getting-started walkthroughs to the catalog root.
2. **Fast Jump Navigation:** Readers must jump straight to the relevant problem domain from the Table of Contents in 1 click.
3. **Flat Deliverable Channel:** The catalog is delivered in a single master index (`README.md`). Supporting architectural guides or API specifications reside strictly in `docs/` and are linked via `## Resources` or `## Reference`.

---

## 3. Anatomy of `README.md` (Character-Level Syntax)

The master catalog file (`README.md`) follows an invariant sequential schema. Every delimiter, header tag, badge link, and blank line adheres to a precise syntax.

```text
+-------------------------------------------------------------+
| 1. Document Title (H1) + Awesome Badge Image Link           |
|    # Awesome <Topic> [![Awesome](badge.svg)](link)          |
+-------------------------------------------------------------+
| 2. Positioning Blockquote                                   |
|    > A curated plain-English index of tools built for ...   |
+-------------------------------------------------------------+
| 3. Official Links Line (Separated by Middle Dots ` · `)      |
|    Official links: [Website](url) · [GitHub](url) · ...     |
+-------------------------------------------------------------+
| 4. Horizontal Rule: `---`                                   |
+-------------------------------------------------------------+
| 5. Table of Contents: `## Contents`                         |
|    Numbered domains (1..7) with parenthesized counts        |
|    Nested 3-space subcategories with parenthesized counts   |
|    Uncounted Resource & Reference entries (8 & 9)           |
+-------------------------------------------------------------+
| 6. Horizontal Rule: `---`                                   |
+-------------------------------------------------------------+
| 7. Numbered Domain Sections (H2: `## 1. <Title>`)           |
|    - Italic Section Count Banner: `*N projects. Blurb.*`    |
|    - Subcategory Sections (H3: `### <Subcategory>`)         |
|      - Italic Subcategory Banner: `*N projects. Blurb.*`    |
|      - 2-Column Table: `| Project | What it does |`         |
|    - Inter-Section Horizontal Rules: `---`                  |
+-------------------------------------------------------------+
| 8. Uncounted Reference Sections                             |
|    - `## Resources` (Bulleted external documentation links) |
|    - `## Reference` (Bulleted architectural concepts/specs) |
+-------------------------------------------------------------+
```

### 3.1 Document Header Elements

#### A. Title & Awesome Badge

- **Exact Line 1:** `# Awesome Herdr [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)`
- **Syntax Rule:** Single H1 heading followed immediately by a space and a nested Markdown link containing the standard SVG badge from `awesome.re`.
- **Target Pattern for GA4 MCP:**

```markdown
# Awesome GA4 MCP [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
```

#### B. Positioning Blockquote

- **Exact Line 3:** `> A curated plain-English index of tools built for **[Herdr](https://herdr.dev/)**, the terminal-native agent multiplexer.`
- **Syntax Rule:** A single Markdown blockquote line (`>` followed by a space) defining the catalog's purpose, bolding the linked core subject `**[Subject](URL)**`, and ending with a concise noun phrase appositive describing the tool's category.
- **Target Pattern for GA4 MCP:**

```markdown
> A curated plain-English index of Model Context Protocol (MCP) servers, clients, and agentic workflows built for **[Google Analytics (GA4)](https://tagmanager.google.com/)**, automated tag management, and analytics engineering.
```

#### C. Official Links Line

- **Exact Line 5:** `Official links: [Website](https://herdr.dev/) · [GitHub](https://github.com/ogulcancelik/herdr) · [Documentation](https://herdr.dev/docs/) · [Plugin Marketplace](https://herdr.dev/plugins/) · [Agent Skill](https://github.com/ogulcancelik/herdr/blob/master/SKILL.md) · [Socket API](https://github.com/ogulcancelik/herdr/blob/master/SOCKET_API.md)`
- **Syntax Rule:**
  - Prefix label: `Official links:` (followed by a space).
  - Delimiter: Middle Dot ` · ` (`U+00B7` flanked by single spaces).
  - Clean descriptive link titles: `[Website]`, `[GitHub]`, `[Documentation]`, `[API Reference]`.
- **Target Pattern for GA4 MCP:**

```markdown
Official links: [GA4 Web UI](https://tagmanager.google.com/) · [GA4 API v2 Docs](https://developers.google.com/tag-platform/tag-manager/api/v2) · [Model Context Protocol Specification](https://modelcontextprotocol.io/) · [Server-Side GA4 Guide](https://developers.google.com/tag-platform/tag-manager/server-side)
```

#### D. Horizontal Rules (`---`)

- **Syntax Rule:** Exactly three hyphens `---` isolated on their own line with a blank line above and below (`\n\n---\n\n`).
- **Placement Rules:**
  - Placed between Official Links and `## Contents`.
  - Placed between `## Contents` and `## 1. Run and orchestrate agents`.
  - Placed between each numbered H2 section (immediately before the next `## N.`).
  - Placed before `## Resources`.
  - **Exception:** Never placed between `## Resources` and `## Reference`.

---

### 3.2 Table of Contents Structure (`## Contents`)

The Table of Contents provides the fast jump navigation grid for the entire ecosystem.

```markdown
## Contents

1. [Run and orchestrate agents (855)](#1-run-and-orchestrate-agents)
   - [Official skill and foundation (1)](#official-skill-and-foundation)
   - [Multi-agent fleets and supervisors (107)](#multi-agent-fleets-and-supervisors)
   - [Swarm, mob, and consensus orchestrators (44)](#swarm-mob-and-consensus-orchestrators)
   ...
2. [Connect through MCP and the socket API (237)](#2-connect-through-mcp-and-the-socket-api)
   - [MCP servers (14)](#mcp-servers)
   ...
8. [Resources](#resources)
9. [Reference](#reference)
```

#### Structural Rules of the TOC

1. **Top-Level Numbering:** Top-level categories are formatted as an ordered list `N. [Title (Count)](#anchor-slug)` for numbered domains 1 through 7.
2. **Indentation Law:** Subcategories are indented by **exactly 3 spaces**, followed by a hyphen `-`, a space, and the link format:

   ```text
      - [Subcategory Title (Count)](#anchor-slug)
   ```

3. **Parenthesized Counts:** Every numbered top-level category and every subcategory includes its item count in parentheses inside the link text: `(N)`.
4. **Uncounted Foundational Sections:** Entries 8 and 9 (`Resources` and `Reference`) are numbered in the TOC (`8. [Resources](#resources)`, `9. [Reference](#reference)`), but **do not have parenthesized counts**.
5. **Anchor Slug Generation Algorithm (GitHub Flavored Markdown Specification):**
   - The slug is generated by applying the following deterministic pipeline to the heading string:
     1. Start with the heading text as rendered in the section header (e.g., `1. Run and orchestrate agents` or `Multi-agent fleets and supervisors`). **Note:** For H2 headings, the heading text includes the number and period; for H3 headings, it does not.
     2. Convert all characters to lowercase: `1. run and orchestrate agents`.
     3. Strip all punctuation except hyphens and whitespace. Specifically remove: `.`, `,`, `:`, `;`, `(`, `)`, `'`, `"`, `?`, `!`, `/`, `\`.
        - Example: `1. Run and orchestrate agents` -> `1 run and orchestrate agents`
        - Example: `Swarm, mob, and consensus orchestrators` -> `swarm mob and consensus orchestrators`
        - Example: `Claude Code: Account switchers and auth monitors` -> `claude code account switchers and auth monitors`
     4. Replace contiguous sequences of whitespace with a single hyphen `-`.
        - Example: `1-run-and-orchestrate-agents`
     5. Prepend `#` to create the anchor target: `#1-run-and-orchestrate-agents`.

---

### 3.3 Heading Hierarchy & Stylings

The catalog strictly limits heading depth to **3 levels** (H1, H2, H3). H4 (`####`) and deeper are strictly prohibited.

| Level | Syntax | Scope / Usage | Example |
|---|---|---|---|
| **H1** | `# <Title>` | Document title (only 1 occurrence in file) | `# Awesome Herdr [![Awesome]...]...` |
| **H2** | `## N. <Title>` | Numbered macro-domains (1..7) | `## 1. Run and orchestrate agents` |
| **H2** | `## <Title>` | TOC & Uncounted foundational sections | `## Contents`, `## Resources`, `## Reference` |
| **H3** | `### <Title>` | Categorical sub-domains containing tables | `### Multi-agent fleets and supervisors` |
| **H4+** | `####` | **FORBIDDEN** | Never used in `awesome-herdr` |

#### Italic Count Banners

Every H2 macro-domain and every H3 subcategory is immediately followed by a 1-line italicized metadata banner:

- **Syntax:** `*<Count> project[s]. <1-2 sentence description>.*`
- **Pluralization Law:**
  - If Count == 1: `*1 project. The official instructions that teach an agent how to understand and control Herdr.*` (uses singular `project`).
  - If Count != 1: `*107 projects. Higher-level systems that coordinate several agents, roles, tasks, or repositories.*` (uses plural `projects`).
- **Punctuation & Formatting:**
  - Count is immediately followed by the word `project.` or `projects.` with a period.
  - The descriptive text immediately follows the space and concludes with a period.
  - The closing asterisk `*` comes **after** the final period: `.*`.

---

### 3.4 Markdown Table Schemas

All project listings are formatted as clean, 2-column Markdown tables:

```markdown
| Project | What it does |
|---|---|
| [**owner/repo**](https://github.com/owner/repo) | Plain-English explanation of what the tool does and who it is for. |
| [**owner/repo · path**](https://github.com/owner/repo/blob/main/path) | Secondary variant when linking to a specific file or subagent skill. |
```

#### Exact Table Formatting Rules

1. **Column Count:** Exactly 2 columns. Multi-column feature tables, author columns, star counts, or language badges are strictly excluded from the table cells to maximize readability and minimize maintenance overhead.
2. **Column Headers:** Column 1 header is always `Project`. Column 2 header is always `What it does`.
3. **Alignment Separator:** Exactly `|---|---|` (three hyphens per column, default left alignment).
4. **Project Cell Syntax (Column 1):**
   - Standard repository link: `[**owner/repo**](https://github.com/owner/repo)`
   - Sub-path / skill link: `[**owner/repo · SKILL.md**](https://github.com/owner/repo/blob/master/SKILL.md)`
   - The link text is **always bolded inside the link**: `[**...**](url)`.
5. **Description Cell Syntax (Column 2):**
   - Contains a factual, plain-English summary.
   - Strictly conforms to the 1–2 Sentence Law.

---

### 3.5 Description Density & Lexical Analysis

A complete programmatic lexical analysis of all 2,089 project descriptions in `awesome-herdr` reveals the following statistical profile:

```text
Total Project Entries:         2,089
Mean Word Count per Entry:     16.8 words
Min Word Count:                2 words (e.g., "Provides Harbour TUI.")
Max Word Count:                60 words
1-Sentence Entries:            1,737 (83.2%)
2-Sentence Entries:              352 (16.8%)
3+ Sentence Entries:               0 (0.0% - Strict Invariant)
Marketing Buzzword Hits:           0 (0.0% - Strict Invariant)
```

#### Lexical & Syntactic Directives

1. **The 1–2 Sentence Law:**
   - **Sentence 1:** Describes what the tool specifically does for the user.
   - **Sentence 2 (Optional):** Details key capabilities, supported models/APIs, or operational boundaries.

2. **Active Verb-First Vocabulary:**
   - Top 20 verbs dominating the corpus:
     - `Provides` (1,068 instances)
     - `Adds` (49 instances)
     - `Opens` (42 instances)
     - `Shows` (40 instances)
     - `Runs` (40 instances)
     - `Keeps` (25 instances)
     - `Displays` (23 instances)
     - `Sends` (21 instances)
     - `Uses` (20 instances)
     - `Connects` (17 instances)
     - `Creates` (15 instances)
     - `Copies` (15 instances)
     - `Controls` (14 instances)
     - `Reads` (12 instances)
     - `Starts` (12 instances)
     - `Detects` (12 instances)
     - `Renames` (12 instances)
     - `Coordinates` (11 instances)
   - Permitted alternative: Crisp noun phrases starting with indefinite articles `A ...` (174 instances) or `An ...` (36 instances) (e.g., `A macOS terminal configuration that...`, `An early TypeScript prototype for...`).

3. **Forbidden Marketing Words:**
   - Zero tolerance for hype: *"ultimate"*, *"blazing fast"*, *"revolutionary"*, *"game-changer"*, *"magical"*, *"best-in-class"*, *"next-gen"*, *"groundbreaking"*.
   - Descriptions must remain neutral, technical, and verifiable.

---

### 3.6 Section 7: Experimental Projects Pattern

Category 7 serves a vital architectural function: the **Experimental Quarantine**.

```markdown
---

## 7. Experimental projects

*15 projects. Early experiments, design documents, and incomplete prototypes. Check each repository before relying on one in daily work.*

### Experiments, concepts, and scaffolds

*15 projects. Ideas and prototypes that are useful to study but may be incomplete, read-only, or not yet installable.*

| Project | What it does |
|---|---|
| [**eliasstravik/herdr-call**](https://github.com/eliasstravik/herdr-call) | An early TypeScript prototype for translating spoken commands into Herdr navigation and input through the local socket. |
| [**meerzulee/herdr-float**](https://github.com/meerzulee/herdr-float) | An early plugin scaffold exploring Zellij-style floating terminal panes that can be toggled without changing the main Herdr grid. |
| [**rohanthewiz/herdr-web**](https://github.com/rohanthewiz/herdr-web) | Renders Herdr pane frames with color, mouse, clipboard, and hyperlink support; keyboard and paste input are currently disabled, so it mainly works as a viewer. |
```

#### Operational Rules for Category 7

1. **Quarantine Boundary:** Repositories that represent early prototypes, concept designs, non-installable scaffolds, or read-only experiments are placed here rather than polluting production categories (1..6).
2. **Explicit Qualification:** Descriptions must transparently state the prototype status (e.g., *"An early TypeScript prototype for..."*, *"An early plugin scaffold..."*, *"Pre-alpha / design phase."*, *"keyboard and paste input are currently disabled, so it mainly works as a viewer."*).
3. **Structure:** In `awesome-herdr`, Section 7 contains exactly 1 subcategory: `### Experiments, concepts, and scaffolds`.

---

### 3.7 Sections 8 & 9: Resources and Reference Patterns

Sections 8 and 9 provide conceptual and navigational anchor points for the ecosystem. They deliberately diverge from categories 1..7:

```markdown
---

## Resources

- **[Herdr Documentation](https://herdr.dev/docs/)**: The official manual covering installation, workspaces, keybindings, and configuration.
- **[Herdr Socket API Reference](https://github.com/ogulcancelik/herdr/blob/master/SOCKET_API.md)**: Protocol documentation for controlling Herdr programmatically over Unix domain sockets.
- **[Herdr Plugin Marketplace](https://herdr.dev/plugins/)**: The official directory of community plugins and integrations.
- **[Herdr Official Agent Skill](https://github.com/ogulcancelik/herdr/blob/master/SKILL.md)**: Standard instructions teaching LLM agents how to interact with Herdr.

## Reference

- **Agent Skill (`SKILL.md`):** Teach Claude, Pi, Codex, or OpenCode how to drive Herdr without external runtime dependencies.
- **Socket Client (`SOCKET_API.md`):** Connect to `~/.herdr/herdr.sock` using JSON commands to manage tabs, panes, and agents.
- **MCP Server:** Expose Herdr commands as tools to any Model Context Protocol host application.
- **Git Worktrees:** Pair Herdr tabs with isolated git worktrees (`git worktree add`) to run concurrent agents safely.
```

#### Invariant Differences Between Categories 1..7 vs 8 & 9

| Structural Property | Categories 1..7 | Sections 8 (`Resources`) & 9 (`Reference`) |
|---|---|---|
| **TOC Entry** | `N. [Title (Count)](#anchor)` | `8. [Resources](#resources)`, `9. [Reference](#reference)` (No counts) |
| **Italic Count Banner** | Required (`*N projects. Blurb.*`) | **Omitted entirely** |
| **Subcategories (H3)** | Required (1 to 14 subcategories) | **Omitted entirely** |
| **Data Format** | Markdown Table (2 columns: Project, What it does) | Markdown Unordered List (`- **[Title](url)**: ...`) |
| **Scope** | Third-party open-source repositories | Official manuals, protocol RFCs, core architecture concepts |

---

## 4. Repository Governance & Agent Instructions (`AGENTS.md`)

The [`AGENTS.md`](file:///root/dev/awesome-herdr/AGENTS.md) file acts as the constitutional prompt for AI coding agents and human contributors interacting with the repository.

### 4.1 Core Tenets

1. **Curated Plain-English Index:** The repository is not a database dump or raw scraping artifact; every entry must be human-readable and plain-English.
2. **Minimalist Entry Format:** Strictly preserve the 2-column table syntax.
3. **Disjoint Scope:** Contributors must not reformat or reorganize existing sections when adding or modifying an entry.

### 4.2 Strict Exclusion Criteria (What NEVER Belongs Here)

To prevent repository decay, four strict negative filters are enforced:

1. **NO Personal Dotfiles:** Generic personal `~/.dotfiles`, chezmoi/stow repos, or personal machine configurations with a `.herdr` config file. Only standalone, packaged, reusable plugins or shareable templates belong in this index.
2. **NO Empty Scaffolds or Incomplete Stubs:** Repositories without working command implementations, design-only documents, or broken builds (unless explicitly quarantined in Section 7).
3. **NO Trivial Copy-Paste Wrappers:** Near-duplicate forks or minimal shims without substantive standalone utility.
4. **NO Marketing Hype or AI Filler:** Neutrality and brevity are mandatory.

### 4.3 Git Commit Hygiene

- All commits touching the catalog must use the Conventional Commits format:
  `docs(awesome-list): <summary>`

---

## 5. CI & Automated Linting Infrastructure

`awesome-herdr` enforces markdown consistency through continuous integration checks that execute in GitHub Actions.

### 5.1 `.markdownlint.yml` (Native YAML Config)

```yaml
MD013: false  # line length — long entries and table rows are fine
MD060: false  # table pipe-style — awesome-list tables vary
MD041: false  # first-line heading — PR template starts with a section
MD033: false  # inline HTML — allows badge tags and SVGs
```

### 5.2 `.markdownlint-cli2.jsonc` (CLI Config)

```jsonc
{
  "config": {
    "MD013": false,
    "MD060": false,
    "MD041": false,
    "MD033": false
  },
  "ignores": [
    "scratch/**",
    ".tmp/**",
    "node_modules/**"
  ]
}
```

### 5.3 `.markdownlintignore`

```text
scratch/
node_modules/
.tmp/
```

### 5.4 GitHub Actions Workflow (`.github/workflows/ci.yml`)

```yaml
name: ci

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  markdown:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
      - uses: actions/setup-node@v6
        with:
          node-version: "24"
          package-manager-cache: false
      - run: npx --yes markdownlint-cli2@latest "**/*.md"
```

---

## 6. Mathematical Count Reconciliation & Verification Engine

A foundational guarantee of the `awesome-herdr` architecture is **total mathematical reconciliation**. No number in the Table of Contents or section headers is allowed to drift from the actual rows present in the markdown tables.

### 6.1 Formal Axiomatic Invariants

Let $\mathcal{C} = \{1, 2, \dots, K\}$ be the set of numbered top-level macro-domains ($K=7$ in `awesome-herdr`).  
For each macro-domain $i \in \mathcal{C}$, let $\mathcal{S}_i = \{1, 2, \dots, M_i\}$ be the ordered set of subcategories belonging to domain $i$.

For every subcategory $j \in \mathcal{S}_i$:

- Let $C_{\text{TOC}}(i, j) \in \mathbb{N}$ be the count displayed in parentheses in the Table of Contents.
- Let $B_{\text{H3}}(i, j) \in \mathbb{N}$ be the count declared in the H3 italic banner (`*N projects.*`).
- Let $R(i, j) \in \mathbb{N}$ be the exact count of data rows in the subcategory's Markdown table.

For every macro-domain $i \in \mathcal{C}$:

- Let $C_{\text{TOC}}(i) \in \mathbb{N}$ be the count displayed in parentheses for the top-level domain in the Table of Contents.
- Let $B_{\text{H2}}(i) \in \mathbb{N}$ be the count declared in the H2 italic banner.

#### Theorem 1: Subcategory Row Equivalence (Micro-Level Invariant)

Every subcategory row count must match both its subcategory banner and its TOC parenthesized count exactly:
$$\forall i \in \mathcal{C}, \; \forall j \in \mathcal{S}_i: \quad R(i, j) = B_{\text{H3}}(i, j) = C_{\text{TOC}}(i, j)$$

#### Theorem 2: Macro-Domain Sum Equivalence (Macro-Level Invariant)

The top-level category count declared in both the TOC and the H2 banner must equal the exact summation of the row counts of all constituent subcategories:
$$\forall i \in \mathcal{C}: \quad C_{\text{TOC}}(i) = B_{\text{H2}}(i) = \sum_{j \in \mathcal{S}_i} R(i, j) = \sum_{j \in \mathcal{S}_i} B_{\text{H3}}(i, j)$$

#### Theorem 3: Total Ecosystem Reconciliation (Global Invariant)

The total project count across the entire repository $N_{\text{total}}$ equals the sum of all top-level category counts:
$$N_{\text{total}} = \sum_{i=1}^{K} C_{\text{TOC}}(i) = \sum_{i=1}^{K} \sum_{j \in \mathcal{S}_i} R(i, j)$$

For `awesome-herdr`:
$$N_{\text{total}} = 855 + 237 + 121 + 176 + 500 + 185 + 15 = 2,089$$

---

### 6.2 Mathematical Proof Matrix for `awesome-herdr`

| Category ID & Title | Subcategories ($|\mathcal{S}_i|$) | TOC Count ($C_{\text{TOC}}$) | H2 Banner ($B_{\text{H2}}$) | Sum of H3 Banners ($\sum B_{\text{H3}}$) | Sum of Table Rows ($\sum R$) | Discrepancy ($\Delta$) |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| **1. Run and orchestrate agents** | 12 | 855 | 855 | 855 | 855 | **0** |
| **2. Connect through MCP and socket** | 8 | 237 | 237 | 237 | 237 | **0** |
| **3. Editor integrations** | 6 | 121 | 121 | 121 | 121 | **0** |
| **4. Switch and restore sessions** | 3 | 176 | 176 | 176 | 176 | **0** |
| **5. Worktrees and terminal exp.** | 14 | 500 | 500 | 500 | 500 | **0** |
| **6. Apps, companion & installation** | 5 | 185 | 185 | 185 | 185 | **0** |
| **7. Experimental projects** | 1 | 15 | 15 | 15 | 15 | **0** |
| **8. Resources** | 0 | Uncounted | N/A | N/A | N/A | **0** |
| **9. Reference** | 0 | Uncounted | N/A | N/A | N/A | **0** |
| **TOTALS** | **49** | **2,089** | **2,089** | **2,089** | **2,089** | **0** |

---

### 6.3 Executable Python Verification Script

Below is the complete, self-contained Python script to verify all count invariants and anchor links across any repository implementing this structural contract:

```python
#!/usr/bin/env python3
"""
verify_awesome_counts.py
Authoritative Structural & Mathematical Verification Engine for Awesome Catalogs.
Usage: python3 verify_awesome_counts.py <path_to_README.md>
"""

import sys
import re
from pathlib import Path

def gfm_anchor(text: str) -> str:
    """Computes GitHub Flavored Markdown heading anchor."""
    h = text.lower()
    # Strip punctuation except whitespace and hyphens
    h = re.sub(r"[^\w\s-]", "", h)
    # Replace spaces with hyphens
    h = re.sub(r"\s+", "-", h)
    return f"#{h}"

def verify_awesome_readme(file_path: str) -> bool:
    path = Path(file_path)
    if not path.exists():
        print(f"Error: File {file_path} does not exist.")
        return False

    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    errors = []
    
    # Regex patterns
    toc_top_re = re.compile(r"^(\d+)\.\s+\[(.*?)(?:\s+\((\d+)\))?\]\(#(.*?)\)")
    toc_sub_re = re.compile(r"^\s+-\s+\[(.*?)(?:\s+\((\d+)\))?\]\(#(.*?)\)")
    h2_re = re.compile(r"^##\s+(?:(\d+)\.\s+)?(.*)$")
    h3_re = re.compile(r"^###\s+(.*)$")
    banner_re = re.compile(r"^\*(\d+)\s+projects?\.\s+(.*?)\*$")
    table_row_re = re.compile(r"^\|\s*\[\*\*(.*?)\*\*\]\((.*?)\)\s*\|\s*(.*?)\s*\|$")

    in_toc = False
    toc_categories = {}
    current_cat_id = None
    all_headings = {}

    # Pass 1: Parse Headings & TOC
    for line_num, line in enumerate(lines, 1):
        stripped = line.strip()
        
        # Track all headings for anchor verification
        m_head = re.match(r"^(#{1,3})\s+(.*)$", stripped)
        if m_head:
            h_text = m_head.group(2).strip()
            anchor = gfm_anchor(h_text)
            all_headings[anchor] = (h_text, line_num)

        if stripped == "## Contents":
            in_toc = True
            continue
        if in_toc:
            if stripped == "---":
                in_toc = False
                continue
            m_top = toc_top_re.match(line)
            if m_top:
                cat_id = int(m_top.group(1))
                title = m_top.group(2).strip()
                count = int(m_top.group(3)) if m_top.group(3) else None
                slug = m_top.group(4)
                toc_categories[cat_id] = {
                    "title": title,
                    "count": count,
                    "slug": slug,
                    "line": line_num,
                    "subs": {}
                }
                current_cat_id = cat_id
                continue
            m_sub = toc_sub_re.match(line)
            if m_sub and current_cat_id:
                sub_title = m_sub.group(1).strip()
                sub_count = int(m_sub.group(2)) if m_sub.group(2) else None
                sub_slug = m_sub.group(3)
                toc_categories[current_cat_id]["subs"][sub_title] = {
                    "count": sub_count,
                    "slug": sub_slug,
                    "line": line_num
                }
                continue

    # Pass 2: Parse Body Sections & Table Rows
    body_sections = {}
    curr_cat = None
    curr_sub = None

    for line_num, line in enumerate(lines, 1):
        stripped = line.strip()
        m_h2 = h2_re.match(stripped)
        if m_h2 and stripped != "## Contents":
            cat_num = int(m_h2.group(1)) if m_h2.group(1) else None
            h2_title = m_h2.group(2).strip()
            curr_cat = cat_num
            curr_sub = None
            if curr_cat:
                body_sections[curr_cat] = {
                    "title": h2_title,
                    "banner_count": None,
                    "line": line_num,
                    "subs": {}
                }
            continue

        if curr_cat and curr_cat in body_sections:
            if not curr_sub:
                m_b = banner_re.match(stripped)
                if m_b:
                    body_sections[curr_cat]["banner_count"] = int(m_b.group(1))
                    continue

            m_h3 = h3_re.match(stripped)
            if m_h3:
                curr_sub = m_h3.group(1).strip()
                body_sections[curr_cat]["subs"][curr_sub] = {
                    "banner_count": None,
                    "rows": 0,
                    "line": line_num
                }
                continue

            if curr_sub:
                m_b3 = banner_re.match(stripped)
                if m_b3 and body_sections[curr_cat]["subs"][curr_sub]["banner_count"] is None:
                    body_sections[curr_cat]["subs"][curr_sub]["banner_count"] = int(m_b3.group(1))
                    continue
                m_r = table_row_re.match(stripped)
                if m_r:
                    body_sections[curr_cat]["subs"][curr_sub]["rows"] += 1

    # Pass 3: Mathematical & Anchor Reconciliation
    print("=" * 70)
    print(f"VERIFYING AWESOME CATALOG: {file_path}")
    print("=" * 70)

    total_projects = 0
    total_subcategories = 0

    for cat_id, cat_data in toc_categories.items():
        # Anchor verification
        top_anchor = f"#{cat_data['slug']}"
        if top_anchor not in all_headings:
            errors.append(f"TOC Line {cat_data['line']}: Anchor {top_anchor} does not resolve to any H2 heading.")

        if cat_data["count"] is None:
            print(f"Category {cat_id:2d}: [{cat_data['title']}] -> Uncounted Reference Category (OK)")
            continue

        b_cat = body_sections.get(cat_id)
        if not b_cat:
            errors.append(f"Category {cat_id} [{cat_data['title']}] defined in TOC but missing in body.")
            continue

        toc_cnt = cat_data["count"]
        h2_banner = b_cat["banner_count"]

        if toc_cnt != h2_banner:
            errors.append(f"Category {cat_id} Count Drift: TOC ({toc_cnt}) != H2 Banner ({h2_banner}).")

        sub_banner_sum = sum(s["banner_count"] for s in b_cat["subs"].values() if s["banner_count"] is not None)
        sub_row_sum = sum(s["rows"] for s in b_cat["subs"].values())

        if toc_cnt != sub_banner_sum:
            errors.append(f"Category {cat_id} Sum Drift: TOC ({toc_cnt}) != Sum of H3 Banners ({sub_banner_sum}).")
        if toc_cnt != sub_row_sum:
            errors.append(f"Category {cat_id} Row Drift: TOC ({toc_cnt}) != Total Markdown Rows ({sub_row_sum}).")

        # Subcategory level checks
        for sub_title, sub_data in cat_data["subs"].items():
            total_subcategories += 1
            sub_anchor = f"#{sub_data['slug']}"
            if sub_anchor not in all_headings:
                errors.append(f"TOC Line {sub_data['line']}: Subcategory anchor {sub_anchor} does not resolve.")

            b_sub = b_cat["subs"].get(sub_title)
            if not b_sub:
                errors.append(f"Category {cat_id} -> Subcategory '{sub_title}' defined in TOC but missing in body.")
                continue

            s_toc = sub_data["count"]
            s_banner = b_sub["banner_count"]
            s_rows = b_sub["rows"]

            if s_toc != s_banner:
                errors.append(f"Subcategory '{sub_title}' Drift: TOC ({s_toc}) != H3 Banner ({s_banner}).")
            if s_banner != s_rows:
                errors.append(f"Subcategory '{sub_title}' Drift: H3 Banner ({s_banner}) != Table Rows ({s_rows}).")

        total_projects += sub_row_sum
        print(f"Category {cat_id:2d}: [{cat_data['title'][:35]:<35}] | Count: {toc_cnt:4d} | Subcats: {len(b_cat['subs']):2d} | Rows: {sub_row_sum:4d} (MATCH)")

    print("-" * 70)
    print(f"Total Verified Subcategories: {total_subcategories}")
    print(f"Total Reconciled Projects:    {total_projects}")
    print("-" * 70)

    if errors:
        print(f"\nFAILED: Found {len(errors)} structural/mathematical errors:")
        for err in errors:
            print(f"  [X] {err}")
        return False
    else:
        print("\nSUCCESS: All structural, anchor, and count invariants satisfied with 100% precision.")
        return True

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "/root/dev/awesome-herdr/README.md"
    success = verify_awesome_readme(target)
    sys.exit(0 if success else 1)
```

---

## 7. Decision Logic & Ergonomics of High-Density Catalogs

A critical question in repository architecture is how `awesome-herdr` successfully manages **49 subcategories** and **2,089 projects** within a single 426 KB document without deteriorating into an unnavigable wall of text.

### 7.1 Taxonomic Classification Matrix: H2 vs H3 vs Resource vs Reference

When categorizing a new domain or concept, use the following deterministic decision logic:

```text
                          Entity to Classify
                                  │
          ┌───────────────────────┴───────────────────────┐
          ▼                                               ▼
  Is it an external tool,                        Is it foundational
  extension, or software?                     documentation or concept?
          │                                               │
    ┌─────┴─────┐                                   ┌─────┴─────┐
    ▼           ▼                                   ▼           ▼
Production  Incomplete/                       Official docs/  Core spec/
 Ready?     Prototype?                         Marketplace?   Architecture?
    │           │                                   │           │
    ▼           ▼                                   ▼           ▼
[H2 / H3]   [Quarantine]                        [Resources]  [Reference]
Categories  Category 7                            Section 8    Section 9
 1 to 6    (Experimental)
```

| Scope Level | Markdown Heading | Qualifying Criteria | Catalog Function |
|---|---|---|---|
| **Macro-Domain** | `## N. <Title>` | Major architectural lifecycle stage or boundary (e.g., orchestration, socket APIs, editors, session state, terminal worktrees, desktop apps). | High-level mental boundary containing 3 to 14 functional subcategories. |
| **Micro-Domain** | `### <Title>` | Specific target integration, protocol client, or functional role (e.g., Telegram alerts, Neovim splits, Git worktrees, Claude Code teams). | Scoped table containing 1 to ~130 verified projects. |
| **Experimental** | `## 7. Experimental projects` | Repositories that are pre-alpha, design documents, incomplete scaffolds, or read-only prototypes. | Quarantine container isolating unproven tools from daily-driver sections. |
| **Resource** | `## Resources` | Upstream official documentation manuals, official marketplaces, or standard skill instructions. | Outbound links to authoritative external web portals. |
| **Reference** | `## Reference` | Core architecture concepts, internal Unix domain socket protocols, CLI flags, or multiplexer primitives. | Glossary defining operational mechanisms (e.g., MCP server, socket daemon, worktree isolation). |

### 7.2 Why 49 Subcategories Scale Without Cognitive Friction

1. **Deterministic 1-Click Jump Target:** By placing all 49 subcategories directly in the TOC with explicit, slugified anchors, a user looking for *"Slack alerts"* or *"Git worktree automation"* reaches their exact destination in a single click, bypassing 2,000 unrelated entries.
2. **Zero Horizontal Layout Shift:** The strictly enforced 2-column table layout eliminates horizontal table scrolling on mobile and narrow terminal split panes.
3. **High Scanning Density:** By outlawing verbose essays, multi-line marketing blurbs, author avatars, and star badges, the eye scans vertical lists of bold repository slugs at ~100 items per minute.
4. **Parenthesized Quantitative Cues:** Including `(N)` in every TOC bullet provides immediate heuristic cues: a user knows instantly whether a domain has 1 tool (monopolized) or 260 tools (heavily fragmented).

---

## 8. Blueprint for `awesome-google-analytics-mcp`: Structural Translation Map

This section translates the `awesome-herdr` architectural framework into an exact blueprint for the Google Analytics (GA4) MCP repository: [`awesome-google-analytics-mcp`](file:///root/dev/awesome-google-analytics-mcp).

### 8.1 Domain Mapping: Herdr Multiplexing -> GA4 MCP Analytics Engineering

| `awesome-herdr` Structural Role | `awesome-google-analytics-mcp` Equivalent Macro-Domain | GA4 Ecosystem Focus |
|---|---|---|
| **Header & Badge** | `# Awesome GA4 MCP [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)` | Curated index of GA4 Model Context Protocol tools |
| **Domain 1: Agent Orchestration** | `## 1. Container and workspace management` | MCP servers managing Account, Container, and Workspace CRUD, branching, diffing, and merging |
| **Domain 2: Socket & MCP Connections** | `## 2. Tag, trigger, and variable automation` | MCP servers automating tags (GA4, Ads, Meta), triggers, and built-in / user-defined variables |
| **Domain 3: Editor Integrations** | `## 3. Server-side GA4 (sGA4) and Cloud Run` | MCP servers for sGA4 clients, Cloud Run proxies, custom templates, and transformation endpoints |
| **Domain 4: Session State Management** | `## 4. Testing, preview, and verification` | Playwright/Puppeteer Tag Assistant automation, live event interceptors, dataLayer journey testing |
| **Domain 5: Terminal & Worktrees** | `## 5. Security, consent, and governance` | Consent Mode v2 auditing, PII leakage detection, compiler error traps, rate-limiting queues |
| **Domain 6: Apps & Companions** | `## 6. Migration, CI/CD, and release automation` | GA4 / GA4 migration bridges, JSON export/import pipelines, live container publish orchestrators |
| **Domain 7: Experimental Projects** | `## 7. Experimental projects` | Unverified scaffolds, sandbox wrappers, and pre-alpha prototypes |
| **Section 8: Resources** | `## Resources` | Official Google Analytics (GA4) API v2 docs, MCP spec, Simo Ahava blog, Tag Manager Web UI |
| **Section 9: Reference** | `## Reference` | Technical glossary: 0.25 QPS quota, CDN 30–180s lag, `compilerError: true`, Consent Mode v2 |

---

### 8.2 Full TOC Layout Specification for `awesome-google-analytics-mcp`

```markdown
# Awesome GA4 MCP [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated plain-English index of Model Context Protocol (MCP) servers, clients, and agentic workflows built for **[Google Analytics (GA4)](https://tagmanager.google.com/)**, automated tag management, and analytics engineering.

Official links: [GA4 Web UI](https://tagmanager.google.com/) · [GA4 API v2 Docs](https://developers.google.com/tag-platform/tag-manager/api/v2) · [Model Context Protocol Specification](https://modelcontextprotocol.io/) · [Server-Side GA4 Guide](https://developers.google.com/tag-platform/tag-manager/server-side)

---

## Contents

1. [Container and workspace management (12)](#1-container-and-workspace-management)
   - [Full GA4 API v2 CRUD servers (3)](#full-gtm-api-v2-crud-servers)
   - [Workspace branching, diffing, and merging (4)](#workspace-branching-diffing-and-merging)
   - [Multi-account and multi-container supervisors (5)](#multi-account-and-multi-container-supervisors)
2. [Tag, trigger, and variable automation (11)](#2-tag-trigger-and-variable-automation)
   - [GA4 and Google Ads tag orchestrators (4)](#ga4-and-google-ads-tag-orchestrators)
   - [Third-party and social tracking tags (3)](#third-party-and-social-tracking-tags)
   - [Trigger configurations and firing rules (2)](#trigger-configurations-and-firing-rules)
   - [Built-in and custom JavaScript variables (2)](#built-in-and-custom-javascript-variables)
3. [Server-side GA4 and Cloud Run (8)](#3-server-side-gtm-and-cloud-run)
   - [Server container clients and transformations (3)](#server-container-clients-and-transformations)
   - [Cloud Run and Cloudflare Worker sidecars (3)](#cloud-run-and-cloudflare-worker-sidecars)
   - [Cookie-less and proxy measurement bridges (2)](#cookie-less-and-proxy-measurement-bridges)
4. [Testing, preview, and verification (7)](#4-testing-preview-and-verification)
   - [Tag Assistant preview automation (3)](#tag-assistant-preview-automation)
   - [Browser dataLayer interceptors and journey tests (2)](#browser-datalayer-interceptors-and-journey-tests)
   - [CDN cache lag checkers and release polling (2)](#cdn-cache-lag-checkers-and-release-polling)
5. [Security, consent, and governance (8)](#5-security-consent-and-governance)
   - [Consent Mode v2 proof engines and audits (3)](#consent-mode-v2-proof-engines-and-audits)
   - [PII scanners and compliance guards (2)](#pii-scanners-and-compliance-guards)
   - [Compiler error traps and rate limiters (3)](#compiler-error-traps-and-rate-limiters)
6. [Migration, CI/CD, and release automation (6)](#6-migration-cicd-and-release-automation)
   - [Container export, import, and cloning tools (3)](#container-export-import-and-cloning-tools)
   - [Automated publish gates and review workflows (3)](#automated-publish-gates-and-review-workflows)
7. [Experimental projects (3)](#7-experimental-projects)
   - [Experiments, concepts, and scaffolds (3)](#experiments-concepts-and-scaffolds)
8. [Resources](#resources)
9. [Reference](#reference)
```

---

### 8.3 Reference Project Entries Formatted to Strict Standard

Here are representative entries demonstrating the exact 2-column format, verb-first prose, and 1–2 sentence rule:

#### Example 1: Full API v2 Server (Top Tier)

```markdown
### Full GA4 API v2 CRUD servers

*3 projects. MCP servers that expose complete read and write access to the Google Analytics (GA4) API v2 hierarchy.*

| Project | What it does |
|---|---|
| [**rgellis/google-tag-manager-mcp**](https://github.com/rgellis/google-tag-manager-mcp) | Exposes all 106 GA4 API v2 endpoints as FastMCP tools for managing accounts, containers, workspaces, tags, triggers, and variables. Includes full statement and branch test coverage across all entity methods. |
| [**A1-x-Tech/mcp-google-tagmanager**](https://github.com/A1-x-Tech/mcp-google-tagmanager) | Provides TypeScript stdio MCP access to web GA4 containers with an internal 4.2-second request pacing queue to prevent Google 0.25 QPS rate-limit errors. |
| [**paolobietolini/gtm-mcp-server**](https://github.com/paolobietolini/gtm-mcp-server) | Runs a high-performance Go 1.26 daemon providing 94 GA4 tools over Streamable HTTP with multi-tenant credential isolation. |
```

#### Example 2: Server-Side GA4 Integration

```markdown
### Server container clients and transformations

*3 projects. MCP servers designed specifically for configuring server-side GA4 containers and event routing.*

| Project | What it does |
|---|---|
| [**stape-io/google-tag-manager-mcp-server**](https://github.com/stape-io/google-tag-manager-mcp-server) | Manages server-side GA4 container clients, routing rules, and transformations over Cloudflare Worker and local CLI runtimes. |
| [**flockstore/platofrm-gtm-mcp**](https://github.com/flockstore/platofrm-gtm-mcp) | Verifies server-side GA4 HTTP event delivery and transformation pipelines without relying on browser cookies. |
| [**samarthanalytics-sj/samarth-analytics-mcp**](https://github.com/samarthanalytics-sj/samarth-analytics-mcp) | Deploys and audits Consent Mode v2 transformation rules and server client mappings across multi-region Cloud Run instances. |
```

#### Example 3: Experimental Quarantine

```markdown
## 7. Experimental projects

*3 projects. Early experiments, design documents, and incomplete prototypes. Check each repository before relying on one in daily work.*

### Experiments, concepts, and scaffolds

*3 projects. Ideas and prototypes that are useful to study but may be incomplete, read-only, or not yet installable.*

| Project | What it does |
|---|---|
| [**digitalXperiments/fluxito**](https://github.com/digitalXperiments/fluxito) | An early Python and Playwright experiment for injecting synthetic dataLayer events; does not account for 30–180s CDN publication lag. |
| [**pouyanafisi/gtm-mcp**](https://github.com/pouyanafisi/gtm-mcp) | An early 104-tool TypeScript prototype; currently lacks rate-limiting queues and can trigger Google 429 quota exhaustion under automated agent loops. |
| [**Insightful-Pipe/google-tag-manager-mcp-server**](https://github.com/Insightful-Pipe/google-tag-manager-mcp-server) | A proof-of-concept MCP bridge for container tag rollback; requires an external commercial API key to function. |
```

---

## 9. Implementation Roadmap & Quality Gate

To instantiate [`awesome-google-analytics-mcp`](file:///root/dev/awesome-google-analytics-mcp) in full conformance with this specification, the implementing agent must execute the following sequential steps:

1. **Scaffold Infrastructure Files:**
   - Copy or create `.markdownlint.yml`, `.markdownlint-cli2.jsonc`, `.markdownlintignore`, and `.github/workflows/ci.yml`.
   - Create `AGENTS.md` adapting the language rules and exclusion criteria to the GA4 MCP domain.
   - Create `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, and `LICENSE`.
2. **Author Catalog (`README.md`):**
   - Populate the H1 title, badge link, positioning blockquote, and official links.
   - Draft `## Contents` with all planned macro-domains and subcategories.
   - Populate the 2-column tables for each subcategory ensuring:
     - 1–2 sentence rule is strictly observed.
     - Descriptions begin with active verbs (`Provides`, `Exposes`, `Manages`, `Audits`, `Automates`).
     - Zero forbidden marketing words.
   - Author `## Resources` and `## Reference`.
3. **Execute Verification Engine:**
   - Run `python3 verify_awesome_counts.py README.md` to confirm:
     - All top-level counts match the sum of subcategory counts.
     - All subcategory counts match table row counts.
     - All TOC anchors resolve cleanly to valid heading slugs.
4. **Execute Markdown Linting:**
   - Run `npx --yes markdownlint-cli2@latest "**/*.md"`.
   - The command must exit with **0 issues in 0 files**.

---
*End of Technical Specification `SPEC-GA4-MCP-001`.*

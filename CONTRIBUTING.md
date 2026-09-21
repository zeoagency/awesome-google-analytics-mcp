# Contributing to Awesome Google Analytics MCP

Thank you for helping maintain this curated index and comparison of Google Analytics Model Context Protocol (MCP) tooling.

## Submission Guidelines

Before opening a pull request to add or modify a project, ensure your entry adheres to the following criteria:

1. **Google Analytics Focus**: The tool must interface directly with Google Analytics APIs (GA4 Data API v1beta, Admin API v1beta, Realtime API, Measurement Protocol v2) or query direct GA4 BigQuery export tables. Generic Google Cloud MCPs or general BI tools without dedicated GA4 tooling are strictly out of scope.
2. **Model Context Protocol Integration**: The tool must implement an MCP server (stdio, SSE, or Streamable HTTP), MCP client, or programmatic agent automation bridge.
3. **Working Implementation**: The repository must contain functional, runnable code or published packages (PyPI, npm, Docker, uvx), not empty stubs or unverified concept docs.
4. **Description Standards**:
   - Strictly 1 to 2 sentences (average 15–25 words, maximum 3 sentences / 45 words).
   - Lead with an active verb (*Extracts*, *Aggregates*, *Ingests*, *Validates*, *Streams*, *Sandboxes*).
   - State concrete, decision-relevant differentiation (API surface covered, write capability, local SQL engine, auth type). Avoid generic filler ("fast and lightweight").
5. **Exact Table Format**: Add your entry in alphabetical order using the format:

   ```markdown
   | [**owner/repo**](https://github.com/owner/repo) | Concise factual description of what it actually does. |
   ```

6. **Count Synchronization**: If adding a new entry, run `python3 scripts/sync_counts.py` to automatically update all parenthesized counts in `## Contents`, category section intros, and subcategory headers.
7. **Local Verification**: Run `npx markdownlint-cli2 "**/*.md"` and `pytest tests/` before submitting.

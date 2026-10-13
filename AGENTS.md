# Catalog maintenance

This repository catalogs implemented Google Analytics 4 MCP servers, CLI tools and SDKs. Keep reader-facing text concise and in English.

## Scope

Include GA4 Data API reporting, Admin API management, Measurement Protocol events or GA4 collection SDKs. Multi-service servers qualify through their implemented GA4 tools; show their GA4 and total tool counts separately. Exclude unrelated utilities, Universal Analytics-only tools, empty scaffolds, documentation-only projects, standalone apps without an MCP/CLI/SDK interface, trivial mirrors and installations with incompatible dependencies and no usable documented lockfile path.

## Review and update

1. Inventory existing records and inspect the upstream revision, registration modules, handlers and package entrypoints. Trace every MCP tool into its implementation; enumerate imported and optional tools as well as default tools. For CLI/SDK entries, trace commands or client methods into GA4 behavior.
2. For each MCP, preserve exact names, full registered descriptions and complete exposed input schemas in `data/mcps/<owner>--<repo>.json`. Include shared/nested models, local references, defaults, required fields, enums and constraints. Preserve loose native objects. Distinguish declared schema restrictions from handler checks and upstream API restrictions.
3. Review extracted data against source independently before setting `review`. Record actual behavior, GA4/other-service/support scope, read/write/local effects, exposure conditions and material defects. Record the pinned revision and inclusion/removal decision in `docs/verification.md`. Static source inspection does not establish successful installation or live API behavior.
4. Place each MCP once in `data/catalog.json`, using its implemented GA4 tools to choose its primary task. Featured tools must exist and have GA4 scope. Keep `data/clients.json` for CLI/SDK entries. Omit popularity rankings, frozen stars, authentication/language tiers and unsupported claims.
5. Run `python3 scripts/build_catalog.py`, then the checks in `.github/workflows/ci.yml`. Review the generated main page, tool index and affected server pages. Completion requires every tool and provider to be linked, every schema reference to resolve, and every inclusion decision and revision to match.

## Data and generated pages

`README.md`, `docs/tool-index.md` and `docs/mcps/*.md` are generated from reviewed JSON. Edit the records and renderer, then regenerate; direct page edits fail the drift check. Server pages show concise behavior with full descriptions and schemas in expandable blocks. Keep upstream descriptions verbatim even when they overstate functionality; explain the actual behavior and limitation separately.

The main page groups MCPs by tasks, followed by CLI tools and SDKs. Each server appears once; its reference page and the alphabetical index expose secondary capabilities. Scope labels distinguish unrelated tools inside a qualifying multi-service server. Count SDK packages separately when they expose different APIs or languages.

# Contributing

Help developers discover what Google Analytics 4 tools actually do. Read [AGENTS.md](AGENTS.md) for scope and the source-review process.

## Pull request checklist

- [ ] The project implements GA4 functionality as an MCP server, CLI or SDK and is not a duplicate or trivial wrapper.
- [ ] Its upstream revision, implementation evidence and inclusion decision are recorded in [the verification log](docs/verification.md).
- [ ] An MCP record includes every registered tool, exact names, full descriptions, complete nested input schemas and pinned source links.
- [ ] The extraction was independently reviewed; optional exposure, write effects and material limitations are documented.
- [ ] Its primary task and featured tools follow actual GA4 handlers. Multi-service totals clearly separate GA4 from other tools.
- [ ] Reviewed JSON is updated and `python3 scripts/build_catalog.py` regenerates the main page, server references and searchable index.
- [ ] `python3 -m unittest discover -s tests`, `python3 scripts/build_catalog.py --check`, `python3 scripts/check_catalog.py` and `npx --yes markdownlint-cli2 "**/*.md"` pass.

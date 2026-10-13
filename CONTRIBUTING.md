# Contributing

Help developers discover Google Analytics 4 MCP servers, CLI tools, and SDKs. Read [AGENTS.md](AGENTS.md) for the scope, evidence requirements, and entry format.

## Pull request checklist

- [ ] The project implements GA4 functionality and belongs to one of the three tool categories.
- [ ] The implementation is publicly inspectable; the description is supported by upstream source or official SDK documentation.
- [ ] The entry is not a duplicate, trivial clone, or wrapper around another listed implementation.
- [ ] The description covers the Google Analytics functionality in one or two concise English sentences.
- [ ] The inspected revision, source links, and decision are recorded in [the verification log](docs/verification.md).
- [ ] Category counts and links are correct.
- [ ] `python3 scripts/check_catalog.py` and `npx --yes markdownlint-cli2 "**/*.md"` pass.

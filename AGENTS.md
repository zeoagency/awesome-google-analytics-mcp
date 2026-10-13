# Catalog maintenance

This repository lists Google Analytics 4 (GA4) MCP servers, command-line tools, and SDKs. The README is an English catalog; keep entries concise and factual.

## Scope

Include tools with an implemented GA4 integration: Data API reporting, Admin API management, Measurement Protocol events, or GA4 event collection SDKs. Multi-service tools qualify when their GA4 integration is implemented; describe that integration.

Exclude Universal Analytics-only tools, generic cloud/database/MCP utilities, standalone dashboards or agents without an MCP server, CLI, or SDK, empty scaffolds, documentation-only projects, and projects whose documented installation resolves incompatible dependencies without a usable locked installation path. List the original implementation instead of a trivial fork, mirror, or launcher. A fork qualifies when its GA4 implementation adds a substantive capability.

## Review process

1. Inventory every existing entry and supporting file before editing.
2. Inspect the upstream source and package metadata. For an MCP server, trace tool registration to a GA4 API handler; for a CLI, trace a command to its GA4 implementation; for an SDK, inspect its GA4 client or collection API.
3. Record the inspected revision, source links, and inclusion/removal reason in `docs/verification.md`. Distinguish source inspection from runtime testing. If the implementation cannot be verified, leave the candidate out and record why.
4. Correct retained descriptions and add verified missing tools. Use current canonical upstream links. Check copied implementations before listing them separately.
5. Update category counts, run `python3 scripts/check_catalog.py` and `npx --yes markdownlint-cli2 "**/*.md"`, then review the full diff.

Use upstream code, official package repositories, and publisher documentation as evidence. Stars, marketing claims, and commit age alone do not establish functionality or quality. Archived projects may be useful; label their status when included. Never imply a live API test was performed unless it was.

## README format

Use three numbered sections: MCP servers, CLI tools, and SDKs. The contents and section headings carry matching entry counts. Each tool appears once, in its primary category; mention additional interfaces in its description. Count SDK packages separately when they expose different APIs or languages.

Use a two-column table (`Project | What it does`). Each description is one or two sentences, starts with a verb, and states the implemented GA4 capability and relevant language or interface. For SDKs, identify whether the publisher is Google or a community maintainer. Prefer substantive differences over exact tool counts, frozen star counts, or subjective tiers.

Keep the catalog focused on tools. Put verification evidence and maintenance instructions in supporting documents rather than adding general tutorials or unrelated resource lists to the README.

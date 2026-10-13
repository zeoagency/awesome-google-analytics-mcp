# Verification log

Reviewed on 2026-10-13. All 47 original entries were inspected against upstream source, along with the added tools and SDK packages. This is a static source review: upstream code was not installed or run, and authenticated Google Analytics API behavior was not tested. Revisions below identify the inspected source; README links follow the upstream project for future updates.

The catalog contains 56 entries: 35 mcp servers, 5 cli tools, 16 sdks. Fourteen original entries were removed or excluded, including six with incompatible documented Python installations. One existing entry moved from MCP to CLI. Added three MCP servers, four CLI tools and sixteen SDK packages.

## Review method

Trace MCP tool registration, CLI command dispatch or SDK client code to an implemented GA4 API. Inspect package metadata and documented installation paths, compare derivative implementations, and describe only supported GA4 behavior. Multi-service tools qualify on their GA4 implementation; stars and commit age are not inclusion criteria. Source-less hosted-service documentation cannot establish executable capabilities for this source-reviewed catalog.

Remove unrelated database/host setup links, subjective tiers, frozen star counts and unsupported performance claims. Keep one catalog entry per implementation; count language/API SDK packages separately. [AGENTS.md](../AGENTS.md) documents the repeatable process and [CONTRIBUTING.md](../CONTRIBUTING.md) provides the checklist.

## Tool reference audit

All 35 retained MCPs were reviewed again, one source inventory per server, using separate GPT 6.1 Sol subagents on low reasoning in batches of at most three. The coordinating reviewer independently checked registrations, descriptions, parameters and handlers before accepting each record. The reviewed revisions match the entry decisions below. All 35 still implement GA4 operations; no additional removal was justified by this pass.

The [tool index](tool-index.md) contains 480 distinct names across 649 registrations: 423 GA4 operations and 226 other-service or server-support operations. Multi-service totals include every registered tool; only their implemented GA4 capabilities determine the main-page placement. Counts include optional tools, not just default exposure. A name shared by several servers is indexed once with links to every provider.

The [per-server references](../README.md) preserve full registered descriptions and complete exposed input schemas. Explicit JSON schemas were compared against source literals; annotation and Zod schemas were reconstructed and checked against signatures, shared models, enums, constraints and defaults. Sednalabs provides a committed schema snapshot, independently matched to all 35 registrations and request structs. Generated schema cosmetics may vary with unbounded dependencies. Loose native objects remain loose; descriptions and handler-only checks do not become invented schema restrictions.

Each [machine-readable record](../data/mcps/) contains its pinned registration/handler sources, independent review method, observed behavior, scope, effects and limitations. Records distinguish native funnels from independent event counts, historical reporting from realtime calls, and advertised tools from permission-gated availability. No live `tools/list`, upstream server execution or authenticated GA4 calls were performed.

The main page now groups servers by six implemented tasks rather than popularity, language, authentication style or marketing. The CLI and SDK entries retain their previous review. Generated-page checks enforce full tool/provider coverage; catalog checks enforce reviewed inclusion decisions, schema references, task placement and navigation.

## Dependency compatibility evidence

MCP Python SDK 2 removes the legacy FastMCP module and lowlevel decorator APIs used by six excluded entries. See the [removed FastMCP module](https://github.com/modelcontextprotocol/python-sdk/blob/754254c08fe1c3eda18b69da3d336106fe8d72d6/src/mcp/server/fastmcp.py), [lowlevel server](https://github.com/modelcontextprotocol/python-sdk/blob/754254c08fe1c3eda18b69da3d336106fe8d72d6/src/mcp/server/lowlevel/server.py), and [published package metadata](https://pypi.org/pypi/mcp/json). At review, PyPI stable was 2.3.0. Those entries provide neither an MCP <2 constraint nor a usable documented lockfile. This concerns fresh documented installations; existing environments using MCP 1 may still work. Reconsider after an upstream dependency fix.

Retained Python implementations either pin compatible MCP versions, use the newer API, use the separate FastMCP package, implement HTTP handling directly, or provide a committed lockfile for their documented installation. HappyMonkeyAI is retained using its documented locked `uv sync` path. Buyte is retained for its source MCP and Workers entrypoints; its compiled Node start path is defective, as recorded below.

Official SDK package locations were checked against Google's [Data client library index](https://developers.google.com/analytics/devguides/reporting/data/v1/client-libraries) and [Admin client library index](https://developers.google.com/analytics/devguides/config/admin/v1/client-libraries). Links use the active package directories instead of relocated standalone repositories.

## Entry decisions

### `googleanalytics/google-analytics-mcp` — Retained

Revision: `75c0e1be8322e5eaa5c2e3ef7e79cf4760060f9a`.

coordinator, credentials, funnel. Nine registered tools, including annotations and conversion reports; actual Data v1beta/v1alpha and Admin v1beta/v1alpha clients. ADC, not built-in browser PKCE. The previous catalog incorrectly listed five tools.

Sources: [coordinator](https://github.com/googleanalytics/google-analytics-mcp/blob/75c0e1be8322e5eaa5c2e3ef7e79cf4760060f9a/analytics_mcp/coordinator.py) · [credentials](https://github.com/googleanalytics/google-analytics-mcp/blob/75c0e1be8322e5eaa5c2e3ef7e79cf4760060f9a/analytics_mcp/tools/client.py) · [funnel](https://github.com/googleanalytics/google-analytics-mcp/blob/75c0e1be8322e5eaa5c2e3ef7e79cf4760060f9a/analytics_mcp/tools/reporting/funnel.py).

### `surendranb/google-analytics-mcp` — Retained

Revision: `d6a321257ae7f5c2a721554602792bf69d796891`.

reporting, metadata, setup, server. Actual Data API reporting, live metadata/schema discovery and schema cache; setup/recovery via MCP elicitation. Credential-file flow accepts service account or user ADC, so SA-only label is too narrow. No realtime/funnel handler found in registered reporting tool.

Sources: [reporting](https://github.com/surendranb/google-analytics-mcp/blob/d6a321257ae7f5c2a721554602792bf69d796891/ga4_mcp/tools/reporting.py) · [metadata](https://github.com/surendranb/google-analytics-mcp/blob/d6a321257ae7f5c2a721554602792bf69d796891/ga4_mcp/tools/metadata.py) · [setup](https://github.com/surendranb/google-analytics-mcp/blob/d6a321257ae7f5c2a721554602792bf69d796891/ga4_mcp/setup_flow.py) · [server](https://github.com/surendranb/google-analytics-mcp/blob/d6a321257ae7f5c2a721554602792bf69d796891/ga4_mcp/server.py).

### `eiiot/ga4-mcp` — Excluded

Revision: `5a18b86d7c0594ca37d86b835761d5eab219226f`.

documented install resolves unbounded `mcp` into 2.x, while this source uses removed v1 APIs. No dependency lockfile or documented `<2` override found. Requires an upstream MCP v1 upper bound or v2 migration before presenting the published install as runnable. See Dependency compatibility evidence above. hosted implementation, credential provider. Copies official reporting foundation but adds substantial multi-user Streamable HTTP OAuth implementation with encrypted Google refresh tokens and SQLite/PostgreSQL grant stores. Not a trivial clone. Five tools/stateless storage characterization is false.

Sources: [hosted implementation](https://github.com/eiiot/ga4-mcp/blob/5a18b86d7c0594ca37d86b835761d5eab219226f/analytics_mcp/hosted.py) · [credential provider](https://github.com/eiiot/ga4-mcp/blob/5a18b86d7c0594ca37d86b835761d5eab219226f/analytics_mcp/tools/client.py) · [dependencies](https://github.com/eiiot/ga4-mcp/blob/5a18b86d7c0594ca37d86b835761d5eab219226f/pyproject.toml).

### `CUTolu2021/ga4-mcp-server` — Retained

Revision: `02b6e355b412dbd303daf1cdd1f17679bb449046`.

source. TypeScript, not plain JavaScript. Six tool schemas: listProperties, runReport, getPageViews, getActiveUsers, getEvents, getUserBehavior. All report execution uses runReport, including activeUsers; no runRealtimeReport. Auth requires GOOGLE_CLIENT_EMAIL/GOOGLE_PRIVATE_KEY, no session-token extraction. Admin property discovery uses TTL cache; compact output supports pagination and quota details.

Sources: [source](https://github.com/CUTolu2021/ga4-mcp-server/blob/02b6e355b412dbd303daf1cdd1f17679bb449046/src/index.ts).

### `mharnett/mcp-ga4` — Retained

Revision: `e44f8b02cb84e7b1f7c56b5b25ea7e0590c330a5`.

tool schemas, handlers, OAuth CLI, write gate. Nine schemas, includes feedback tools; standard/realtime queries, custom dimensions/metrics and streams; actual custom dimension creation; service account or user OAuth and PKCE helper. Working-directory client context is real.

Sources: [tool schemas](https://github.com/mharnett/mcp-ga4/blob/e44f8b02cb84e7b1f7c56b5b25ea7e0590c330a5/src/tools.ts) · [handlers](https://github.com/mharnett/mcp-ga4/blob/e44f8b02cb84e7b1f7c56b5b25ea7e0590c330a5/src/index.ts) · [OAuth CLI](https://github.com/mharnett/mcp-ga4/blob/e44f8b02cb84e7b1f7c56b5b25ea7e0590c330a5/src/authCli.ts) · [write gate](https://github.com/mharnett/mcp-ga4/blob/e44f8b02cb84e7b1f7c56b5b25ea7e0590c330a5/src/writeGate.ts).

### `fujii-yuji/GA4-MCP-Remote` — Excluded

Revision: `7d0f48cb485aac95dda1956e012146e0af7b0b1e`.

documented install resolves unbounded `mcp` into 2.x, while this source uses removed v1 APIs. No dependency lockfile or documented `<2` override found. Requires an upstream MCP v1 upper bound or v2 migration before presenting the published install as runnable. See Dependency compatibility evidence above. transport, policy settings, credentials, reports. Streamable HTTP, bearer access gating, ADC to Google, property allowlists, row/date limits and concurrency. SSE transport and Google PKCE labels inaccurate. GA realtime requests are snapshots, not telemetry subscriptions.

Sources: [transport](https://github.com/fujii-yuji/GA4-MCP-Remote/blob/7d0f48cb485aac95dda1956e012146e0af7b0b1e/src/ga4_remote_mcp/transport/app.py) · [policy settings](https://github.com/fujii-yuji/GA4-MCP-Remote/blob/7d0f48cb485aac95dda1956e012146e0af7b0b1e/src/ga4_remote_mcp/config/settings.py) · [credentials](https://github.com/fujii-yuji/GA4-MCP-Remote/blob/7d0f48cb485aac95dda1956e012146e0af7b0b1e/src/ga4_remote_mcp/ga/tools/utils.py) · [reports](https://github.com/fujii-yuji/GA4-MCP-Remote/blob/7d0f48cb485aac95dda1956e012146e0af7b0b1e/src/ga4_remote_mcp/ga/tools/reporting/core.py) · [dependencies](https://github.com/fujii-yuji/GA4-MCP-Remote/blob/7d0f48cb485aac95dda1956e012146e0af7b0b1e/pyproject.toml).

### `Newsstate/ga4-mcp` — Retained

Revision: `54ba34d170438ad186f78cf412b0aaefd6ebe6c0`.

live route, GA4 client, Search Console, OAuth. Actual GA4 reporting/realtime and Admin discovery plus GSC sites/query/page/date tools. No dynamic GA4 schema introspection implemented; classification false. TypeScript Next.js with browser OAuth/bearer tokens; generic OAuth2 != proof of Google PKCE.

Sources: [live route](https://github.com/Newsstate/ga4-mcp/blob/54ba34d170438ad186f78cf412b0aaefd6ebe6c0/app/api/mcp/route.ts) · [GA4 client](https://github.com/Newsstate/ga4-mcp/blob/54ba34d170438ad186f78cf412b0aaefd6ebe6c0/lib/ga4.ts) · [Search Console](https://github.com/Newsstate/ga4-mcp/blob/54ba34d170438ad186f78cf412b0aaefd6ebe6c0/lib/searchconsole.ts) · [OAuth](https://github.com/Newsstate/ga4-mcp/blob/54ba34d170438ad186f78cf412b0aaefd6ebe6c0/app/authorize/route.ts).

### `gviollaz/iita-ga4-mcp` — Retained

Revision: `9d5fae652689754a8e8aa64039f7d887c1018fd6`.

GA4 tools, server, MCP OAuth. Seven GA4 tools implemented via FastMCP and Starlette HTTP wrapper; Google API access uses configured Google refresh token. Separate MCP OAuth2.1/PKCE authentication exists, not Google browser OAuth. Catalog FastAPI description wrong.

Sources: [GA4 tools](https://github.com/gviollaz/iita-ga4-mcp/blob/9d5fae652689754a8e8aa64039f7d887c1018fd6/main.py) · [server](https://github.com/gviollaz/iita-ga4-mcp/blob/9d5fae652689754a8e8aa64039f7d887c1018fd6/server.py) · [MCP OAuth](https://github.com/gviollaz/iita-ga4-mcp/blob/9d5fae652689754a8e8aa64039f7d887c1018fd6/oauth.py).

### `paulsign-lab/ga4-mcp` — Removed

Revision: `fc18ec6925385e18c39bdf44c3a0745a59f965c6`.

server. Actual JavaScript MCP is explicitly Google Sheets, uses spreadsheets scope and ten spreadsheet CRUD/format tools. GA4 content is agency documentation and skills, not GA4 MCP handlers. Claimed Python/batch reports/realtime is fabricated for this source.

Sources: [server](https://github.com/paulsign-lab/ga4-mcp/blob/fc18ec6925385e18c39bdf44c3a0745a59f965c6/mcp-server/index.js).

### `Leanpicazoo/ga4-mcp` — Removed

Revision: `beca989a34f3d4434cbb58035ba8cd3ad46631db`.

shim, extension manifest. Claude Desktop extension invokes `pipx run analytics-mcp`; Python shim explicitly says actual server is Google's official package and execs it. No independent query implementation. Could be ancillary packaging resource, but no distinct server capability.

Sources: [shim](https://github.com/Leanpicazoo/ga4-mcp/blob/beca989a34f3d4434cbb58035ba8cd3ad46631db/server/main.py) · [extension manifest](https://github.com/Leanpicazoo/ga4-mcp/blob/beca989a34f3d4434cbb58035ba8cd3ad46631db/manifest.json).

### `mamaladze22/ga4-mcp` — Removed

Revision: `553e3bac2f66bc2e05d6edc022c2ed6baccaae67`.

README, .claude settings. Tracked files are README, CLAUDE.md, .gitignore, settings JSON. Documents installing official analytics-mcp; contains no TypeScript source, package manifest, independent handlers, or JSON-reporting implementation.

Sources: [README](https://github.com/mamaladze22/ga4-mcp/blob/553e3bac2f66bc2e05d6edc022c2ed6baccaae67/README.md) · [.claude settings](https://github.com/mamaladze22/ga4-mcp/blob/553e3bac2f66bc2e05d6edc022c2ed6baccaae67/.claude/settings.json).

### `scalably-io/ga4-mcp` — Retained

Revision: `90b8c28b4e62844fe1f1b765e3b95ce08367285b`.

complete implementation. Seventeen registered tools, real Data v1beta/v1alpha and Admin v1beta/v1alpha calls including pivot, batch, funnel, compatibility, annotations, access report and stream inspection. Supports explicit SA file or ADC; no built-in PKCE. Read-only operations, no Admin provisioning implied.

Sources: [complete implementation](https://github.com/scalably-io/ga4-mcp/blob/90b8c28b4e62844fe1f1b765e3b95ce08367285b/src/scalably_ga4_mcp/server.py).

### `luminarylane/ga4-mcp` — Retained

Revision: `90e80869b6ad043956e8fb2d551332d5dec5312a`.

source. Seven tools and actual Data/Admin calls. Auth is service_account.Credentials.from_service_account_file; OAuth mentioned as phase 2 in docstring, not implemented. Implements rate limiting/retry, top pages, sources, conversions, realtime, date comparisons; demographics claim not supported by a dedicated tool.

Sources: [source](https://github.com/luminarylane/ga4-mcp/blob/90e80869b6ad043956e8fb2d551332d5dec5312a/ga4_server.py).

### `thesyedyahya/ga4-mcp` — Excluded

Revision: `3bb3d5d00e645b7f16b8aa04534d15e0116216da`.

documented install resolves unbounded `mcp` into 2.x, while this source uses removed v1 APIs. No dependency lockfile or documented `<2` override found. Requires an upstream MCP v1 upper bound or v2 migration before presenting the published install as runnable. See Dependency compatibility evidence above. server, coordinator, credentials. Seven official-derived reporting/Admin tools including annotations. Substantive extension: stdio, SSE and Streamable HTTP, token gate, CORS and deployment health endpoint. ADC, not SA-exclusive. Do not frame ordinary upstream annotation tool as architectural innovation.

Sources: [server](https://github.com/thesyedyahya/ga4-mcp/blob/3bb3d5d00e645b7f16b8aa04534d15e0116216da/analytics_mcp/server.py) · [coordinator](https://github.com/thesyedyahya/ga4-mcp/blob/3bb3d5d00e645b7f16b8aa04534d15e0116216da/analytics_mcp/coordinator.py) · [credentials](https://github.com/thesyedyahya/ga4-mcp/blob/3bb3d5d00e645b7f16b8aa04534d15e0116216da/analytics_mcp/tools/utils.py) · [dependencies](https://github.com/thesyedyahya/ga4-mcp/blob/3bb3d5d00e645b7f16b8aa04534d15e0116216da/pyproject.toml).

### `yusofansari/google-analytics-mcp` — Excluded

Revision: `ad78c3d9a3c7e076b1083587cfad4778b3ff099e`.

documented install resolves unbounded `mcp` into 2.x, while this source uses removed v1 APIs. No dependency lockfile or documented `<2` override found. Requires an upstream MCP v1 upper bound or v2 migration before presenting the published install as runnable. See Dependency compatibility evidence above. tools, user credentials, OAuth provider. Actual per-user OAuth reporting, pivot/cohort/funnel/batch/realtime/metadata and Admin property listing. Stronger than catalog's minimal bridge. Many convenience wrappers omit required property_id when calling run_report, so do not advertise them as verified working. Core parameterized handlers do pass property ID.

Sources: [tools](https://github.com/yusofansari/google-analytics-mcp/blob/ad78c3d9a3c7e076b1083587cfad4778b3ff099e/ga4/server.py) · [user credentials](https://github.com/yusofansari/google-analytics-mcp/blob/ad78c3d9a3c7e076b1083587cfad4778b3ff099e/shared/user_creds.py) · [OAuth provider](https://github.com/yusofansari/google-analytics-mcp/blob/ad78c3d9a3c7e076b1083587cfad4778b3ff099e/shared/google_oauth_provider.py) · [dependencies](https://github.com/yusofansari/google-analytics-mcp/blob/ad78c3d9a3c7e076b1083587cfad4778b3ff099e/requirements.txt).

### `CamilaBarbareschi/cafedelirante-ga4-mcp` — Removed

Revision: `52f7f212f7aac8863713549c97bf160186459ee5`.

app, analytics TODO, auth TODO. FastAPI root/health only. Says next step add OAuth/GA4/MCP endpoints. No GA client or MCP handlers. E-commerce reporting and PKCE claims false.

Sources: [app](https://github.com/CamilaBarbareschi/cafedelirante-ga4-mcp/blob/52f7f212f7aac8863713549c97bf160186459ee5/app/main.py) · [analytics TODO](https://github.com/CamilaBarbareschi/cafedelirante-ga4-mcp/blob/52f7f212f7aac8863713549c97bf160186459ee5/app/analytics.py) · [auth TODO](https://github.com/CamilaBarbareschi/cafedelirante-ga4-mcp/blob/52f7f212f7aac8863713549c97bf160186459ee5/app/auth.py).

### `K41R0N/ga4-mcp` — Retained

Revision: `aa90b1568a0800eb4dfdc96700e6c10ef1d36ecd`.

MCP route, OAuth callback. Two real tools: list_properties and run_report; Google user refresh tokens in Upstash Redis. MCP bearer token gating. No realtime handler and no service account authentication. Storage isn't stateless.

Sources: [MCP route](https://github.com/K41R0N/ga4-mcp/blob/aa90b1568a0800eb4dfdc96700e6c10ef1d36ecd/app/api/mcp/route.ts) · [OAuth callback](https://github.com/K41R0N/ga4-mcp/blob/aa90b1568a0800eb4dfdc96700e6c10ef1d36ecd/app/api/auth/google/callback/route.ts).

### `Hasim-cim/ga4-mcp` — Retained

Revision: `80a2c6ffc267106c7a854bc2bac67f5f8a07339d`.

CLI, dependencies. Explicit standalone script, no MCP dependency. argparse presets realtime/top-pages/traffic-sources/demographics/property/custom call real GA4 Data/Admin APIs with ADC. Has default organization-specific property ID overridable via GA4_PROPERTY_ID; no --property flag. Fits authorized CLI scope.

Sources: [CLI](https://github.com/Hasim-cim/ga4-mcp/blob/80a2c6ffc267106c7a854bc2bac67f5f8a07339d/ga4.py) · [dependencies](https://github.com/Hasim-cim/ga4-mcp/blob/80a2c6ffc267106c7a854bc2bac67f5f8a07339d/pyproject.toml).

### `aline-delmain/delmain-ga4-mcp` — Excluded

Revision: `0d5fe109ead9362eed61e9a361a8b71cd273c1ae`.

documented install resolves unbounded `mcp` into 2.x, while this source uses removed v1 APIs. No dependency lockfile or documented `<2` override found. Requires an upstream MCP v1 upper bound or v2 migration before presenting the published install as runnable. See Dependency compatibility evidence above. tools, GA4 implementation, setup CLI. Four tools: property list/details and standard/realtime reports. Per-user browser OAuth token setup. No agency report presets implemented; actual arbitrary dimensions/metrics.

Sources: [tools](https://github.com/aline-delmain/delmain-ga4-mcp/blob/0d5fe109ead9362eed61e9a361a8b71cd273c1ae/src/delmain_ga4_mcp/server.py) · [GA4 implementation](https://github.com/aline-delmain/delmain-ga4-mcp/blob/0d5fe109ead9362eed61e9a361a8b71cd273c1ae/src/delmain_ga4_mcp/ga4.py) · [setup CLI](https://github.com/aline-delmain/delmain-ga4-mcp/blob/0d5fe109ead9362eed61e9a361a8b71cd273c1ae/src/delmain_ga4_mcp/setup_cli.py) · [dependencies](https://github.com/aline-delmain/delmain-ga4-mcp/blob/0d5fe109ead9362eed61e9a361a8b71cd273c1ae/pyproject.toml).

### `devli13/mcp-ga4` — Retained

Revision: `30727d04fe681872700ba5bce5c9e06b876218a7`.

source. Six schemas, five real Data API handlers; ga4_list_properties merely echoes configured default and instructions, not Admin API. Service account file/inline/base64 credentials. General report, realtime, top events, daily users, first-session date report implemented. No Admin client; no dedicated conversion rate calculation. propertyName executes before try and before list handler, another functional limitation.

Sources: [source](https://github.com/devli13/mcp-ga4/blob/30727d04fe681872700ba5bce5c9e06b876218a7/server.js).

### `administrator-prog/ga4-mcp` — Retained

Revision: `5a2453257e66c2c53dc961611fd2bb55c729e0f5`.

source. Eleven registered tools, real Data v1beta reports and Admin property listing, Streamable HTTP/Express. Google OAuth refresh token, not service account. No realtime API calls. Organic/landing/device/event/internal-search reports and date comparisons actual; conversion drop tool returns report comparisons, not statistical anomaly classifier.

Sources: [source](https://github.com/administrator-prog/ga4-mcp/blob/5a2453257e66c2c53dc961611fd2bb55c729e0f5/src/index.ts).

### `sednalabs/ga4-mcp` — Retained

Revision: `847406e7ce36360216ba5bd0a71b218619b0fa8e`.

rmcp tool_router and #[tool] registrations call real GA Data/Admin REST methods. scratchpad_ingest_report and scratchpad_ingest_realtime_report implement DuckDB ingestion; remove unsupported sub-millisecond performance claim.

Sources: [src/tools.rs](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs) · [src/ga_client.rs](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/ga_client.rs) · [src/server.rs](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/server.rs) · [Cargo.toml](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/Cargo.toml).

### `fenjo26/OpenGSC` — Retained

Revision: `3805be32a8d3a33d32e38724928b92946ce6c2a4`.

get_analytics handler calls analyticsdata v1beta properties.runReport with current and previous periods. HTTP route implements tools/list and tools/call and invokes registered handlers. GA4 data here is LIVE, not ingested into SQLite for arbitrary SQL. Remove 68-tool/storage specialization claim.

Sources: [src/lib/mcp/toolsData.ts](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsData.ts) · [src/lib/mcp/tools.ts](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/tools.ts) · [src/app/api/mcp/route.ts](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/app/api/mcp/route.ts) · [src/lib/ga4.ts](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/ga4.ts).

### `rablab-mtl/mcp-ga4-gsc` — Retained

Revision: `2fff5e4a0de1174116c6cb51f0061e388d03155b`.

Numerous server.tool registrations execute GA4 Data v1beta and Admin requests through callGoogle. OAuth/Workers remote architecture is distinct; no service-account support demonstrated.

Sources: [src/index.ts](https://github.com/rablab-mtl/mcp-ga4-gsc/blob/2fff5e4a0de1174116c6cb51f0061e388d03155b/src/index.ts) · [src/google-handler.ts](https://github.com/rablab-mtl/mcp-ga4-gsc/blob/2fff5e4a0de1174116c6cb51f0061e388d03155b/src/google-handler.ts) · [src/workers-oauth-utils.ts](https://github.com/rablab-mtl/mcp-ga4-gsc/blob/2fff5e4a0de1174116c6cb51f0061e388d03155b/src/workers-oauth-utils.ts).

### `delaren47/gsc-ga4-mcp` — Retained

Revision: `b21d75c0baa66e4a9f992aa864ef6aaa5196794f`.

server.tool registers GA4/GSC and combined analysis tools. compareGscGa4Pages actually joins landingPagePlusQueryString sessions/engagedSessions/engagementRate with GSC page clicks. No claim that it merges GA4 conversion events is justified by this combined handler.

Sources: [src/index.ts](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/index.ts) · [src/google.ts](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/google.ts) · [src/analysis.ts](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/analysis.ts) · [src/auth.ts](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/auth.ts).

### `CreativeMetrics/gtm-ga4-mcp` — Retained

Revision: `2f274468eaf7dcf3fbb9d29e1d997a83bd88b302`.

ListToolsRequestSchema/CallToolRequestSchema register and dispatch actual handlers; src/ga4.js calls google.analyticsdata(v1beta) and analyticsadmin(v1beta). Distinct GTM audit implementation, not a stub.

Sources: [index.js](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js) · [src/ga4.js](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/ga4.js) · [src/gtm-health.js](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm-health.js) · [src/auth.js](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/auth.js).

### `kb223/gtm-ga4-mcp` — Retained

Revision: `40862b6e92d0b70e04b543a6f7ec854258e392cd`.

build_server iterates ToolSpecs and applies mcp.tool to executable functions. ga4_run_report uses google discovery analyticsdata/v1beta; realtime and metadata implemented. SDK dependency mcp>=2,<3 verified against PyPI current release 2.3.0; server uses new MCPServer API. Auth uses google-auth default credentials, not necessarily interactive OAuth PKCE.

Sources: [src/gtm_ga4_mcp/server.py](https://github.com/kb223/gtm-ga4-mcp/blob/40862b6e92d0b70e04b543a6f7ec854258e392cd/src/gtm_ga4_mcp/server.py) · [src/gtm_ga4_mcp/tools/ga4_data.py](https://github.com/kb223/gtm-ga4-mcp/blob/40862b6e92d0b70e04b543a6f7ec854258e392cd/src/gtm_ga4_mcp/tools/ga4_data.py) · [src/gtm_ga4_mcp/tools/ga4_write.py](https://github.com/kb223/gtm-ga4-mcp/blob/40862b6e92d0b70e04b543a6f7ec854258e392cd/src/gtm_ga4_mcp/tools/ga4_write.py) · [src/gtm_ga4_mcp/config.py](https://github.com/kb223/gtm-ga4-mcp/blob/40862b6e92d0b70e04b543a6f7ec854258e392cd/src/gtm_ga4_mcp/config.py).

### `irinabuht12-oss/google-meta-ads-ga4-mcp` — Removed

Revision: `029dd696d0f46d4ee0bfc0ae3f335a3841d6af99`.

Tracked files contain docs, images, configurations and remote MCP descriptor only. server.json points to `https://connector.get-ryze.ai/mcp` and another repository spelling. No runtime source, dependencies, GA4 implementation or executable MCP registrations to verify. The previous catalog’s TypeScript, tool-count and API claims were unsupported. Removal means unverifiable implementation, not proof the hosted service lacks GA4.

Sources: [server.json](https://github.com/irinabuht12-oss/google-meta-ads-ga4-mcp/blob/029dd696d0f46d4ee0bfc0ae3f335a3841d6af99/server.json) · [google-analytics-mcp/README.md](https://github.com/irinabuht12-oss/google-meta-ads-ga4-mcp/blob/029dd696d0f46d4ee0bfc0ae3f335a3841d6af99/google-analytics-mcp/README.md).

### `freema/mcp-google-marketing` — Retained

Revision: `adda0be8151627308d903820b7b9a914face1ca8`.

allTools/allHandlers registered through MCP request schemas; GA4 client is BetaAnalyticsDataClient and runReport handler calls API. Admin lifecycle operations implemented. Actual adjacent platform is AdSense, not Google Ads bidding.

Sources: [src/index.ts](https://github.com/freema/mcp-google-marketing/blob/adda0be8151627308d903820b7b9a914face1ca8/src/index.ts) · [src/tools/analytics/index.ts](https://github.com/freema/mcp-google-marketing/blob/adda0be8151627308d903820b7b9a914face1ca8/src/tools/analytics/index.ts) · [src/tools/analytics/run-report.ts](https://github.com/freema/mcp-google-marketing/blob/adda0be8151627308d903820b7b9a914face1ca8/src/tools/analytics/run-report.ts) · [src/utils/google-auth.ts](https://github.com/freema/mcp-google-marketing/blob/adda0be8151627308d903820b7b9a914face1ca8/src/utils/google-auth.ts).

### `stufently/google-webtools-mcp` — Retained

Revision: `2d18361dffddb441b92abc79667a11df1b19ac42`.

server.tool registrations in GA4 modules call Ga4ApiClient real Data and Admin methods. No Google Tag Manager implementation; remove GTM claim and fixed inflated counts.

Sources: [src/server.ts](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/server.ts) · [src/tools/ga4-reporting/index.ts](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/ga4-reporting/index.ts) · [src/tools/ga4-admin/index.ts](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/ga4-admin/index.ts) · [src/api/ga4-client.ts](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/ga4-client.ts).

### `dhawalshah/google-analytics-mcp` — Retained

Revision: `ef0a3415025f891d06354be3379a3c7c1f3bd1f7`.

Ten @mcp.tool registrations; runFunnelReport uses Data v1alpha, report/realtime Data v1beta. Shares substantial original report wrappers with gomarble-ai but substantive added funnel/realtime/schema tools and remote Firestore OAuth architecture justify retaining. No organizational isolation implementation demonstrated; per-user isolation is evidenced.

Sources: [server.py](https://github.com/dhawalshah/google-analytics-mcp/blob/ef0a3415025f891d06354be3379a3c7c1f3bd1f7/server.py) · [main.py](https://github.com/dhawalshah/google-analytics-mcp/blob/ef0a3415025f891d06354be3379a3c7c1f3bd1f7/main.py) · [oauth/google_auth.py](https://github.com/dhawalshah/google-analytics-mcp/blob/ef0a3415025f891d06354be3379a3c7c1f3bd1f7/oauth/google_auth.py) · [oauth/token_store.py](https://github.com/dhawalshah/google-analytics-mcp/blob/ef0a3415025f891d06354be3379a3c7c1f3bd1f7/oauth/token_store.py).

### `ESGEE-0562/google-analytics-mcp` — Retained

Revision: `7e1e0873dde071e23d416c09942573b74f199368`.

Manual JSON-RPC tools/list/tools/call dispatches seven executable GA4 tools. ga_tools.py ports official SDK report/admin handlers but OAuth HTTP architecture is substantive. Fernet encrypts OAuth state and MCP token payload (includes refresh token); local JSON save_token stores credentials unencrypted, so encrypted persistence claim must be removed.

Sources: [server.py](https://github.com/ESGEE-0562/google-analytics-mcp/blob/7e1e0873dde071e23d416c09942573b74f199368/server.py) · [src/ga_tools.py](https://github.com/ESGEE-0562/google-analytics-mcp/blob/7e1e0873dde071e23d416c09942573b74f199368/src/ga_tools.py) · [src/auth.py](https://github.com/ESGEE-0562/google-analytics-mcp/blob/7e1e0873dde071e23d416c09942573b74f199368/src/auth.py) · [src/storage.py](https://github.com/ESGEE-0562/google-analytics-mcp/blob/7e1e0873dde071e23d416c09942573b74f199368/src/storage.py).

### `codeChap/mcp-server-google-analytics` — Retained

Revision: `b003d8ade81adc672fd338bc50a0d5287e10d890`.

15 #[tool] handlers via rmcp tool_router; real Data v1beta/Admin calls. login.rs performs loopback authorization code flow with state but no code_challenge/verifier, so PKCE claim false. Cargo.toml lists numerous dependencies: zero-dependency claim false.

Sources: [src/server.rs](https://github.com/codeChap/mcp-server-google-analytics/blob/b003d8ade81adc672fd338bc50a0d5287e10d890/src/server.rs) · [src/api.rs](https://github.com/codeChap/mcp-server-google-analytics/blob/b003d8ade81adc672fd338bc50a0d5287e10d890/src/api.rs) · [src/auth.rs](https://github.com/codeChap/mcp-server-google-analytics/blob/b003d8ade81adc672fd338bc50a0d5287e10d890/src/auth.rs) · [src/login.rs](https://github.com/codeChap/mcp-server-google-analytics/blob/b003d8ade81adc672fd338bc50a0d5287e10d890/src/login.rs).

### `minholi/google-analytics-mcp` — Retained

Revision: `21a816a16df6cb5d45783c1479ea72b585ab849b`.

Eight @mcp.tool handlers use actual Data v1beta REST client. Remote HTTP GoogleProvider path and local stdio path implemented; no Admin API or centralized team property switcher tool.

Sources: [src/server.py](https://github.com/minholi/google-analytics-mcp/blob/21a816a16df6cb5d45783c1479ea72b585ab849b/src/server.py) · [src/client.py](https://github.com/minholi/google-analytics-mcp/blob/21a816a16df6cb5d45783c1479ea72b585ab849b/src/client.py) · [src/auth.py](https://github.com/minholi/google-analytics-mcp/blob/21a816a16df6cb5d45783c1479ea72b585ab849b/src/auth.py) · [main.py](https://github.com/minholi/google-analytics-mcp/blob/21a816a16df6cb5d45783c1479ea72b585ab849b/main.py).

### `gomarble-ai/google-analytics-mcp-server` — Retained

Revision: `42b4fa21874c66d3b3bb0c5d47d0a8f0541cbc33`.

Seven @mcp.tool registrations with GA4 runReport calls and account summaries. Original implementation underlying dhawalshah derivative; distinct original retained. No explicit team-account switching framework.

Sources: [server.py](https://github.com/gomarble-ai/google-analytics-mcp-server/blob/42b4fa21874c66d3b3bb0c5d47d0a8f0541cbc33/server.py) · [oauth/google_auth.py](https://github.com/gomarble-ai/google-analytics-mcp-server/blob/42b4fa21874c66d3b3bb0c5d47d0a8f0541cbc33/oauth/google_auth.py).

### `ankhangonline/mcp-ga4-team-server` — Retained

Revision: `f7c3a3bc89610f3cf261d7aa9f637d488506d73c`.

ListToolsRequestSchema and CallToolRequestSchema expose exactly one get_team_ga4_report handler calling Data v1beta runReport. Auth reads request Authorization header, not shared service account; no realtime/permission guardrail claims supported. Implementation is simple but real; global singleton SSE transport limits concurrent sessions. Do not market as hardened team access.

Sources: [index.js](https://github.com/ankhangonline/mcp-ga4-team-server/blob/f7c3a3bc89610f3cf261d7aa9f637d488506d73c/index.js) · [package.json](https://github.com/ankhangonline/mcp-ga4-team-server/blob/f7c3a3bc89610f3cf261d7aa9f637d488506d73c/package.json).

### `mnsmasum62786/was-ga4-mcp` — Retained

Revision: `74d3244754dde0d3cd3142de4d2e513796d38dca`.

MCP request schemas register allTools and dispatch tool.handler; Data module implements real GA4 REST calls. server.js connects StdioServerTransport, so remote session-proxy label false. Local credential/token handling does not establish PKCE.

Sources: [server.js](https://github.com/mnsmasum62786/was-ga4-mcp/blob/74d3244754dde0d3cd3142de4d2e513796d38dca/server.js) · [tools/registry.js](https://github.com/mnsmasum62786/was-ga4-mcp/blob/74d3244754dde0d3cd3142de4d2e513796d38dca/tools/registry.js) · [tools/data.js](https://github.com/mnsmasum62786/was-ga4-mcp/blob/74d3244754dde0d3cd3142de4d2e513796d38dca/tools/data.js) · [tools/admin.js](https://github.com/mnsmasum62786/was-ga4-mcp/blob/74d3244754dde0d3cd3142de4d2e513796d38dca/tools/admin.js).

### `leonardosepulvedat/mcp-google-analytics` — Retained

Revision: `97731c9bcf801297b0c8f0cd34cdde903730f2a2`.

26 registerTool definitions route into GADataClient REST Data v1beta/v1alpha and Admin v1beta plus MeasurementProtocolClient. Admin is read-only, not custom-definition provisioning. Per-tool property override is implemented.

Sources: [src/index.ts](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/index.ts).

### `Insightful-Pipe/google-analytics-mcp-server` — Removed

Revision: `3b64f49171166bb88b280fcde14e7ea21756dbe4`.

Repository contains README, license, example data and image only: no implementation, manifest or registered tool handlers. TypeScript, PKCE, event sending and actual 62-tool registration cannot be verified. This is documentation for an external commercial service, not an executable source project. Can be placed in separately identified hosted-services resources only if scope later includes such services.

Sources: [README.md](https://github.com/Insightful-Pipe/google-analytics-mcp-server/blob/3b64f49171166bb88b280fcde14e7ea21756dbe4/README.md).

### `HappyMonkeyAI/ai-google-analytics-mcp` — Retained

Revision: `170ca6d97a076393f5ef530c8cc39f3ffb50951f`.

18 @mcp.tool handlers; admin.py uses AnalyticsAdminServiceClient, create_property/create_data_stream. No Data client dependency; reporting explicitly delegated to official analytics-mcp. The previous catalog description claiming Reports and property metadata synchronization is false. Documented uv sync uses the committed lockfile with MCP 1.28.1.

Sources: [src/ga4_provision_mcp/server.py](https://github.com/HappyMonkeyAI/ai-google-analytics-mcp/blob/170ca6d97a076393f5ef530c8cc39f3ffb50951f/src/ga4_provision_mcp/server.py).

### `mario-hernandez/google-analytics-mcp-claude-code` — Excluded

Revision: `8877be0828a5b93cd1ce16360ada63c76cd0aa72`.

Superseded by the unified google-seo-mcp-claude-code repository. Both implementations import the removed mcp.server.fastmcp API with an unbounded mcp dependency and no lockfile; their documented fresh installations are incompatible with MCP 2. 14 _register calls use mcp.tool(name=...)(fn), plus two direct tools = 16. auth.py uses official Data/Admin clients. Funnel/cohort tools derive analyses from aggregated run_report data; do not claim native runFunnelReport support. gsc_to_ga4_journey accepts supplied GSC rows; no independently authenticated Search Console integration.

Sources: [src/ga4_seo_mcp/server.py](https://github.com/mario-hernandez/google-analytics-mcp-claude-code/blob/8877be0828a5b93cd1ce16360ada63c76cd0aa72/src/ga4_seo_mcp/server.py) · [dependencies](https://github.com/mario-hernandez/google-analytics-mcp-claude-code/blob/8877be0828a5b93cd1ce16360ada63c76cd0aa72/pyproject.toml).

### `onionst/ga4-toolkit` — Retained

Revision: `1fbfe9e929dbdb055e556318b152be675e60071c`.

8 @mcp.tool handlers and pyproject commands ga4, ga4-mcp. client.py uses AuthorizedSession against Data/Admin v1beta; CLI has auth/properties/use and report presets. No anomaly or historical-baseline detection in source. Admin access is discovery, not writes.

Sources: [src/ga4_toolkit/mcp_server.py](https://github.com/onionst/ga4-toolkit/blob/1fbfe9e929dbdb055e556318b152be675e60071c/src/ga4_toolkit/mcp_server.py).

### `TheTechBasket/GA4-Dashboard-MCP` — Retained

Revision: `349560e7ba0221dccb152e0a87fd573d8974c785`.

11 server.registerTool definitions. Tools call official Data/Admin clients; optional PageSpeed and Google Indexing tools. mcp-server/lib/auth.js delegates to lib/credentials.js with service-account environment credentials, no OAuth/PKCE. Three.js visualization is dashboard UI, not 11 visualization-generating tools.

Sources: [mcp-server/index.js](https://github.com/TheTechBasket/GA4-Dashboard-MCP/blob/349560e7ba0221dccb152e0a87fd573d8974c785/mcp-server/index.js).

### `inakigorostiza/ga4-mcp-dashboard` — Removed

Revision: `18427a747021ce200e441e15808f8c53b3bc86ca`.

server.js imports Client and StdioClientTransport, spawns command analytics-mcp and calls get_account_summaries/run_report. No McpServer, tool registration, CLI analytics command or reusable SDK. No realtime event stream or HTML-generation MCP tool. Actual MCP CLIENT, outside narrowed scope.

Sources: [server.js](https://github.com/inakigorostiza/ga4-mcp-dashboard/blob/18427a747021ce200e441e15808f8c53b3bc86ca/server.js).

### `arcbaslow/google-analytics-agent` — Retained

Revision: `305af22aa78797e3348e045d46e61814fb6b45a3`.

47 @mcp.tool handlers call substantive adapters. pyproject includes ga4-mcp; source scripts use argparse for actual CLIs. ga4_data/ga4_admin use Google client libraries, ga4_utils stores identity-scoped JSON caching: matrix stateless is wrong. Optional PDF requires extra; benchmark bands are repository estimates, not live industry data.

Sources: [scripts/ga4_mcp.py](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_mcp.py).

### `analyticsdatajg2025-cmd/ga4-mcp-powerbi` — Removed

Revision: `07126edf5104a9e69e6110727489b3700b537ba7`.

server.js only registers POST /api/ask and GET /health, uses axios runReport and Anthropic API. package.json has express/cors/dotenv/googleapis/axios and no MCP dependency. No MCP registration, analytics CLI or SDK; no PowerBI tabular feeds or realtime support. Name alone does not confer MCP.

Sources: [server.js](https://github.com/analyticsdatajg2025-cmd/ga4-mcp-powerbi/blob/07126edf5104a9e69e6110727489b3700b537ba7/server.js).

### `burhan29ee/ga4-mcp-server` — Retained

Revision: `e8bd5db77475e8b7e5dd312ea3ab91f6ea4355c3`.

19 @mcp.tool handlers with Data beta and Admin beta/alpha clients, urllib MP event POST. No OAuth/PKCE. This is a working read/write server, not starter scaffolding, and current 13-tool count is wrong.

Sources: [src/ga4_mcp_server/server.py](https://github.com/burhan29ee/ga4-mcp-server/blob/e8bd5db77475e8b7e5dd312ea3ab91f6ea4355c3/src/ga4_mcp_server/server.py).

### `get-mcp-ads/google-analytics-mcp-server` — Added

Revision: `f59104fd0edd96807944df94657e337e17c989be`.

CLI creates McpServer, registers GA4 tools/resources, then connects StdioServerTransport. server.tool registrations call real Data v1beta report/realtime/pivot/batch and v1alpha runFunnelReport endpoints plus Admin reads. Dedicated query planner, compatibility catalogs and diagnostic implementations show substantive authored implementation; GitHub fork:false. Build entries match dist/cli.js bin and dist/index.js exports; direct SDK/zod dependencies and tsup build configuration coherent by inspection. Requires Node >=22.12 and configured client ID, secret, refresh token. No obvious static blocker. Do not call funnel fallback a sequenced funnel: source explicitly reports independent counts.

Sources: [src/cli.ts](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/cli.ts) · [src/server.ts](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/server.ts) · [src/platforms/ga4/tools.ts](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/tools.ts) · [src/platforms/ga4/surface-tools.ts](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/surface-tools.ts).

### `buyte-io/GA4-MCP-Server` — Added

Revision: `0c828761972759a32432c36ed4b32e6af7677acd`.

Four registerTool calls list accounts/properties, retrieve metadata and run reports. Node service uses official Data/Admin SDK clients; Workers service uses actual REST clients and custom MCP HTTP transport. Dedicated HTTP transport/service split/cache implementation is substantive; GitHub fork:false. npm run mcp invokes tsx src/mcp/cli-entry.ts, which can resolve tsconfig aliases and imports; declared SDK/zod/tsx dependencies match source. Static caveat: npm start points at dist/index.js but rootDir:. emits dist/src/index.js. Plain tsc also preserves @config/@features aliases and extensionless imports, so plain Node compiled start is broken without bundling/alias handling. This does not erase the documented tsx MCP entrypoint or Wrangler-bundled path. Debug logs use stdout and should be disabled for stdio. Describe as source-verified implementation, never fully runtime-tested.

Sources: [src/mcp/server.ts](https://github.com/buyte-io/GA4-MCP-Server/blob/0c828761972759a32432c36ed4b32e6af7677acd/src/mcp/server.ts) · [src/mcp/cli-entry.ts](https://github.com/buyte-io/GA4-MCP-Server/blob/0c828761972759a32432c36ed4b32e6af7677acd/src/mcp/cli-entry.ts) · [src/mcp/cli.ts](https://github.com/buyte-io/GA4-MCP-Server/blob/0c828761972759a32432c36ed4b32e6af7677acd/src/mcp/cli.ts) · [src/mcp/worker-http.ts](https://github.com/buyte-io/GA4-MCP-Server/blob/0c828761972759a32432c36ed4b32e6af7677acd/src/mcp/worker-http.ts).

### `Callince/ga4-mcp-server` — Added

Revision: `4b0eeba11a24aaf1b20fdee12209db5d4d795371`.

Four ListToolsRequestSchema definitions dispatch via CallToolRequestSchema to executable listProperties/runReport/runRealtimeReport/getMetadata handlers. Official Data/Admin clients use GoogleAuth wrapping OAuth2Client; --login dynamically imports @google-cloud/local-auth and stores user token. All source imports have matching dependency declarations; package main server/index.js exists and needs no compilation. Straightforward OAuth reporting implementation, not a scaffold; GitHub fork:false and no substantive byte-for-byte match to group2 servers found. Local-auth differentiates this from service-account-only servers. Node >=18 declared. No obvious static dependency/entrypoint blocker. No evidence of PKCE in this source; do not claim it.

Sources: [server/index.js](https://github.com/Callince/ga4-mcp-server/blob/4b0eeba11a24aaf1b20fdee12209db5d4d795371/server/index.js) · [package.json](https://github.com/Callince/ga4-mcp-server/blob/4b0eeba11a24aaf1b20fdee12209db5d4d795371/package.json) · [package-lock.json](https://github.com/Callince/ga4-mcp-server/blob/4b0eeba11a24aaf1b20fdee12209db5d4d795371/package-lock.json).

### `sulimanbenhalim/ga-cli` — Added

Revision: `929b3dc1a03c53df742bb6c133f8eccf065c1a4a`.

ga_cli/cli.py registers Click accounts/properties/datastreams/config; auth.py constructs AnalyticsAdminServiceClient; setup.py installs ga-cli from PyPI ga4-cli. No Data reporting: Admin-only GA4 is within scope.

Sources: [ga_cli/cli.py](https://github.com/sulimanbenhalim/ga-cli/blob/929b3dc1a03c53df742bb6c133f8eccf065c1a4a/ga_cli/cli.py) · [auth.py](https://github.com/sulimanbenhalim/ga-cli/blob/929b3dc1a03c53df742bb6c133f8eccf065c1a4a/ga_cli/auth.py).

### `Bin-Huang/google-analytics-cli` — Added

Revision: `b22395084426e6530d84a9ba3d040240c89a9d42`.

src/commands/reporting.ts calls runReport, runPivotReport, batchRunReports, runRealtimeReport, createAudienceExport; admin.ts reads Admin v1beta/v1alpha; package bin google-analytics-cli. Do not infer property CRUD from broad README phrase “manage”: commands inspect configuration, and createAudienceExport is Data export.

Sources: [src/commands/reporting.ts](https://github.com/Bin-Huang/google-analytics-cli/blob/b22395084426e6530d84a9ba3d040240c89a9d42/src/commands/reporting.ts) · [admin.ts](https://github.com/Bin-Huang/google-analytics-cli/blob/b22395084426e6530d84a9ba3d040240c89a9d42/src/commands/admin.ts).

### `kasdimg/analytics-cli` — Added

Revision: `3886e7781faa53dd3b19fe960e65ef424b8e1de3`.

lib/ga4.js creates google.analyticsdata v1beta and calls properties.runReport; cli.js dispatches GA4 and Search Console commands; package.json bin analytics-cli. Multiproduct with actual GA4 allowed.

Sources: [lib/ga4.js](https://github.com/kasdimg/analytics-cli/blob/3886e7781faa53dd3b19fe960e65ef424b8e1de3/lib/ga4.js).

### `nyosegawa/gacli` — Added

Revision: `84e6cb41dcea70096f3987c5c8f14eeb5cbc0dd4`.

gacli/client.py uses BetaAnalyticsDataClient run_report/run_realtime_report; cli.py registers Click commands; oauth.py uses InstalledAppFlow; pyproject.toml installs gacli.

Sources: [gacli/client.py](https://github.com/nyosegawa/gacli/blob/84e6cb41dcea70096f3987c5c8f14eeb5cbc0dd4/gacli/client.py).

### `MarkEdmondson1234/googleAnalyticsR` — Added

Revision: `ae113f2f52c3c121fd763890c24c3a061683b44d`.

R/ga_data.R constructs analyticsdata.googleapis.com runReport and runRealtimeReport URLs. GA4 implementation is substantial despite retained legacy UA functions; multiproduct/GA4-inclusive allowed.

Sources: [R/ga_data.R](https://github.com/MarkEdmondson1234/googleAnalyticsR/blob/ae113f2f52c3c121fd763890c24c3a061683b44d/R/ga_data.R).

### `adswerve/GA4-Measurement-Protocol-Python` — Added

Revision: `4663738f8f9575c0dbc8c47b9b95455483c6e5e3`.

ga4mp/ga4mp.py implements mp/collect and debug/mp/collect using urllib HTTP POST; GtagMP and FirebaseMP subclasses set platform-specific identity fields. Actual SDK ga4mp; not UA-only.

Sources: [ga4mp/ga4mp.py](https://github.com/adswerve/GA4-Measurement-Protocol-Python/blob/4663738f8f9575c0dbc8c47b9b95455483c6e5e3/ga4mp/ga4mp.py).

### `Python — google-analytics-data` — Added

Revision: `69a8c4941737877d95d58067d0f94ac8c91f940f`.

Google-published Data API package for Python; inspected dedicated package documentation or generated client source.

Sources: [packages/google-analytics-data/README.rst](https://github.com/googleapis/google-cloud-python/blob/69a8c4941737877d95d58067d0f94ac8c91f940f/packages/google-analytics-data/README.rst).

### `Python — google-analytics-admin` — Added

Revision: `69a8c4941737877d95d58067d0f94ac8c91f940f`.

Google-published Admin API package for Python; inspected dedicated package documentation or generated client source.

Sources: [packages/google-analytics-admin/README.rst](https://github.com/googleapis/google-cloud-python/blob/69a8c4941737877d95d58067d0f94ac8c91f940f/packages/google-analytics-admin/README.rst).

### `Node.js — @google-analytics/data` — Added

Revision: `dd43d94a4cde1de6f7573434a377e358fee3b931`.

Google-published Data API package for Node.js; inspected dedicated package documentation or generated client source.

Sources: [packages/google-analytics-data/README.md](https://github.com/googleapis/google-cloud-node/blob/dd43d94a4cde1de6f7573434a377e358fee3b931/packages/google-analytics-data/README.md).

### `Node.js — @google-analytics/admin` — Added

Revision: `dd43d94a4cde1de6f7573434a377e358fee3b931`.

Google-published Admin API package for Node.js; inspected dedicated package documentation or generated client source.

Sources: [packages/google-analytics-admin/README.md](https://github.com/googleapis/google-cloud-node/blob/dd43d94a4cde1de6f7573434a377e358fee3b931/packages/google-analytics-admin/README.md).

### `Java — google-analytics-data` — Added

Revision: `3b02a442725d216d9b1fa6f2b97b02a82f5c8ad8`.

Google-published Data API package for Java; inspected dedicated package documentation or generated client source.

Sources: [java-analytics-data/README.md](https://github.com/googleapis/google-cloud-java/blob/3b02a442725d216d9b1fa6f2b97b02a82f5c8ad8/java-analytics-data/README.md).

### `Java — google-analytics-admin` — Added

Revision: `3b02a442725d216d9b1fa6f2b97b02a82f5c8ad8`.

Google-published Admin API package for Java; inspected dedicated package documentation or generated client source.

Sources: [java-analytics-admin/README.md](https://github.com/googleapis/google-cloud-java/blob/3b02a442725d216d9b1fa6f2b97b02a82f5c8ad8/java-analytics-admin/README.md).

### `Go — analytics/data/v1beta` — Added

Revision: `4341edf3f941fd7107b74ea255025675ef98730e`.

Google-published Data API package for Go; inspected dedicated package documentation or generated client source.

Sources: [googleapis/analytics/data/v1beta/analytics_data_api.pb.go](https://github.com/googleapis/go-genproto/blob/4341edf3f941fd7107b74ea255025675ef98730e/googleapis/analytics/data/v1beta/analytics_data_api.pb.go).

### `Go — analytics/admin/v1beta` — Added

Revision: `4341edf3f941fd7107b74ea255025675ef98730e`.

Google-published Admin API package for Go; inspected dedicated package documentation or generated client source.

Sources: [googleapis/analytics/admin/v1beta/analytics_admin.pb.go](https://github.com/googleapis/go-genproto/blob/4341edf3f941fd7107b74ea255025675ef98730e/googleapis/analytics/admin/v1beta/analytics_admin.pb.go).

### `.NET — Google.Analytics.Data.V1Beta` — Added

Revision: `1ed2a211cd575f4c836403d05229dd22b35e5170`.

Google-published Data API package for .NET; inspected dedicated package documentation or generated client source.

Sources: [apis/Google.Analytics.Data.V1Beta/Google.Analytics.Data.V1Beta/BetaAnalyticsDataClient.g.cs](https://github.com/googleapis/google-cloud-dotnet/blob/1ed2a211cd575f4c836403d05229dd22b35e5170/apis/Google.Analytics.Data.V1Beta/Google.Analytics.Data.V1Beta/BetaAnalyticsDataClient.g.cs).

### `.NET — Google.Analytics.Admin.V1Beta` — Added

Revision: `1ed2a211cd575f4c836403d05229dd22b35e5170`.

Google-published Admin API package for .NET; inspected dedicated package documentation or generated client source.

Sources: [apis/Google.Analytics.Admin.V1Beta/Google.Analytics.Admin.V1Beta/AnalyticsAdminServiceClient.g.cs](https://github.com/googleapis/google-cloud-dotnet/blob/1ed2a211cd575f4c836403d05229dd22b35e5170/apis/Google.Analytics.Admin.V1Beta/Google.Analytics.Admin.V1Beta/AnalyticsAdminServiceClient.g.cs).

### `PHP — google/analytics-data` — Added

Revision: `a92130574ea4a08034c996a6e0bb14d9ba479f92`.

Google-published Data API package for PHP; inspected dedicated package documentation or generated client source.

Sources: [AnalyticsData/README.md](https://github.com/googleapis/google-cloud-php/blob/a92130574ea4a08034c996a6e0bb14d9ba479f92/AnalyticsData/README.md).

### `PHP — google/analytics-admin` — Added

Revision: `a92130574ea4a08034c996a6e0bb14d9ba479f92`.

Google-published Admin API package for PHP; inspected dedicated package documentation or generated client source.

Sources: [AnalyticsAdmin/README.md](https://github.com/googleapis/google-cloud-php/blob/a92130574ea4a08034c996a6e0bb14d9ba479f92/AnalyticsAdmin/README.md).

### `Ruby — google-analytics-data-v1beta` — Added

Revision: `ba23ea0eb5944b870d6616dd163c717ce4b173d8`.

Google-published Data API package for Ruby; inspected dedicated package documentation or generated client source.

Sources: [google-analytics-data-v1beta/README.md](https://github.com/googleapis/google-cloud-ruby/blob/ba23ea0eb5944b870d6616dd163c717ce4b173d8/google-analytics-data-v1beta/README.md).

### `Ruby — google-analytics-admin-v1alpha` — Added

Revision: `ba23ea0eb5944b870d6616dd163c717ce4b173d8`.

Google-published Admin API package for Ruby; inspected dedicated package documentation or generated client source.

Sources: [google-analytics-admin-v1alpha/README.md](https://github.com/googleapis/google-cloud-ruby/blob/ba23ea0eb5944b870d6616dd163c717ce4b173d8/google-analytics-admin-v1alpha/README.md).

### `mario-hernandez/google-seo-mcp-claude-code` — Excluded

Revision: `b0e9deeadd00aa4401f75d77680174735e48eac2`.

Implements GA4 and Search Console MCP tools, but imports mcp.server.fastmcp with an unbounded mcp>=1.2 dependency and no lockfile. The documented fresh pipx installation resolves incompatible MCP 2.x APIs.

Sources: [server.py](https://github.com/mario-hernandez/google-seo-mcp-claude-code/blob/b0e9deeadd00aa4401f75d77680174735e48eac2/src/google_seo_mcp/server.py) · [ga4/data.py](https://github.com/mario-hernandez/google-seo-mcp-claude-code/blob/b0e9deeadd00aa4401f75d77680174735e48eac2/src/google_seo_mcp/ga4/data.py) · [gsc/analytics.py](https://github.com/mario-hernandez/google-seo-mcp-claude-code/blob/b0e9deeadd00aa4401f75d77680174735e48eac2/src/google_seo_mcp/gsc/analytics.py) · [pyproject.toml](https://github.com/mario-hernandez/google-seo-mcp-claude-code/blob/b0e9deeadd00aa4401f75d77680174735e48eac2/pyproject.toml) · [dependencies](https://github.com/mario-hernandez/google-seo-mcp-claude-code/blob/b0e9deeadd00aa4401f75d77680174735e48eac2/pyproject.toml).

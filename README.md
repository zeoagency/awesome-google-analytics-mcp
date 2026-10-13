# Awesome Google Analytics MCP [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of Google Analytics 4 (GA4) MCP servers, CLI tools, and SDKs.

Includes multi-service tools with an implemented GA4 integration. Projects are listed once; MCP servers with CLI commands are identified in their descriptions. SDK counts refer to individual packages.

Source review: 2026-10-13. See the [verification log](docs/verification.md) for inspected revisions, corrections, exclusions, and known limitations. Live Google Analytics requests were not tested.

## Contents

1. [MCP servers (35)](#1-mcp-servers-35)
2. [CLI tools (5)](#2-cli-tools-5)
3. [SDKs (16)](#3-sdks-16)

## 1. MCP servers (35)

| Project | What it does |
| --- | --- |
| [**googleanalytics/google-analytics-mcp**](https://github.com/googleanalytics/google-analytics-mcp) | Queries GA4 reports, realtime data, funnels, conversions, and property metadata through Google's official Python MCP server. Uses Application Default Credentials for Google API access. |
| [**administrator-prog/ga4-mcp**](https://github.com/administrator-prog/ga4-mcp) | Queries GA4 traffic, landing pages, acquisition channels, devices, events, and internal search through a TypeScript MCP server. Serves tools over Streamable HTTP with Google OAuth and date-range comparison reports. |
| [**ankhangonline/mcp-ga4-team-server**](https://github.com/ankhangonline/mcp-ga4-team-server) | Runs filtered GA4 reports and date-range comparisons from a JavaScript MCP server over SSE. Passes the caller’s Google OAuth bearer token to the Data API. |
| [**arcbaslow/google-analytics-agent**](https://github.com/arcbaslow/google-analytics-agent) | Audits GA4 data quality, reports, funnels and property configuration through Python CLI commands and an MCP server. Generates Markdown or HTML reports and prepares Admin writes for terminal approval. |
| [**burhan29ee/ga4-mcp-server**](https://github.com/burhan29ee/ga4-mcp-server) | Queries GA4 reports and realtime data with a Python MCP server using a service account. Manages custom definitions, key events, audiences and Measurement Protocol secrets, and sends server-side events. |
| [**buyte-io/GA4-MCP-Server**](https://github.com/buyte-io/GA4-MCP-Server) | Queries GA4 reports and metadata and lists accounts and properties from a TypeScript MCP server. Runs via the source stdio entrypoint or Cloudflare Workers; the compiled Node entrypoint has a known build-path issue. |
| [**Callince/ga4-mcp-server**](https://github.com/Callince/ga4-mcp-server) | Queries GA4 standard and realtime reports, discovers metadata and lists accessible properties from a JavaScript stdio MCP server. Signs in through a local browser OAuth flow and stores a refresh token for subsequent queries. |
| [**codeChap/mcp-server-google-analytics**](https://github.com/codeChap/mcp-server-google-analytics) | Queries GA4 reports, realtime data and property metadata and manages custom dimensions, key events and annotations from a Rust MCP server. Supports multiple configured accounts, service-account credentials and loopback OAuth login. |
| [**CreativeMetrics/gtm-ga4-mcp**](https://github.com/CreativeMetrics/gtm-ga4-mcp) | Queries GA4 reports and manages property definitions from a JavaScript MCP server alongside Tag Manager and Search Console tools. Checks measurement data while auditing Tag Manager configuration. |
| [**CUTolu2021/ga4-mcp-server**](https://github.com/CUTolu2021/ga4-mcp-server) | Queries GA4 reports and discovers accessible properties through a TypeScript MCP server using service account credentials. Returns compact rows with pagination, optional quota metadata, and cached property lookup. |
| [**delaren47/gsc-ga4-mcp**](https://github.com/delaren47/gsc-ga4-mcp) | Queries GA4 reports and realtime activity alongside Search Console data from a TypeScript MCP server. Joins landing-page engagement with search clicks and impressions using OAuth or service-account credentials. |
| [**devli13/mcp-ga4**](https://github.com/devli13/mcp-ga4) | Queries GA4 reports and realtime data through a JavaScript stdio MCP server. Provides event, daily-user, and first-session report presets with service account credentials supplied by file or environment variables. |
| [**dhawalshah/google-analytics-mcp**](https://github.com/dhawalshah/google-analytics-mcp) | Queries GA4 standard, realtime and funnel reports plus account metadata from a Python MCP server. Adds remote OAuth authorization and per-user token storage in Firestore to the GoMarble reporting implementation. |
| [**ESGEE-0562/google-analytics-mcp**](https://github.com/ESGEE-0562/google-analytics-mcp) | Queries GA4 standard and realtime reports plus account and property metadata from a Python HTTP MCP server. Implements OAuth authorization with encrypted state and MCP bearer tokens, while caching Google credentials in local JSON files. |
| [**fenjo26/OpenGSC**](https://github.com/fenjo26/OpenGSC) | Compares GA4 sessions, engagement, key events and revenue across periods through a TypeScript HTTP MCP endpoint within a Search Console and SEO application. Uses each connected Google account’s OAuth credentials. |
| [**freema/mcp-google-marketing**](https://github.com/freema/mcp-google-marketing) | Queries GA4 reports, pivots and realtime activity and manages properties, data streams and custom definitions from a TypeScript MCP server. Also exposes Search Console and AdSense tools with shared OAuth credentials. |
| [**get-mcp-ads/google-analytics-mcp-server**](https://github.com/get-mcp-ads/google-analytics-mcp-server) | Queries GA4 reports, realtime activity, funnels and property configuration from a read-only TypeScript MCP server. Adds query validation and diagnostic checks with OAuth refresh-token credentials. |
| [**gomarble-ai/google-analytics-mcp-server**](https://github.com/gomarble-ai/google-analytics-mcp-server) | Queries GA4 traffic, campaigns, devices, geography and ecommerce reports from a Python MCP server. Lists accessible properties through the Admin API and authenticates with Google OAuth. |
| [**gviollaz/iita-ga4-mcp**](https://github.com/gviollaz/iita-ga4-mcp) | Queries GA4 reports and realtime data through a Python MCP server with presets for traffic sources, top pages, landing pages, and daily trends. Serves the tools over Streamable HTTP with optional MCP OAuth authentication. |
| [**HappyMonkeyAI/ai-google-analytics-mcp**](https://github.com/HappyMonkeyAI/ai-google-analytics-mcp) | Creates GA4 properties and web streams with a Python MCP server using the Admin API. Generates or inserts gtag and Next.js tracking code and records local project configuration. |
| [**K41R0N/ga4-mcp**](https://github.com/K41R0N/ga4-mcp) | Lists accessible GA4 properties and runs reports through a Next.js MCP endpoint. Stores per-user Google OAuth refresh tokens in Redis and requires a bearer token for MCP access. |
| [**kb223/gtm-ga4-mcp**](https://github.com/kb223/gtm-ga4-mcp) | Queries GA4 reports, realtime data and metadata from a Python MCP server alongside Tag Manager tools. Enables Admin and Tag Manager writes through configurable read, write and destructive permission tiers. |
| [**leonardosepulvedat/mcp-google-analytics**](https://github.com/leonardosepulvedat/mcp-google-analytics) | Queries GA4 reports, realtime data and funnels through a TypeScript MCP server, and reads account and property configuration. Sends and validates Measurement Protocol events, including ecommerce events. |
| [**luminarylane/ga4-mcp**](https://github.com/luminarylane/ga4-mcp) | Queries GA4 reports, realtime users, top pages, traffic sources, conversions, and period comparisons using a Python MCP server. Uses service account credentials with request throttling and retries. |
| [**mharnett/mcp-ga4**](https://github.com/mharnett/mcp-ga4) | Queries GA4 reports and realtime data through a TypeScript MCP server using client context selected from the working directory. Reads custom definitions and data streams, with gated custom-dimension creation and service account or user OAuth authentication. |
| [**minholi/google-analytics-mcp**](https://github.com/minholi/google-analytics-mcp) | Queries GA4 overview, traffic, pages, geography, audience, events, conversions and realtime activity from a Python MCP server. Runs locally with refresh-token credentials or remotely with per-user Google OAuth. |
| [**mnsmasum62786/was-ga4-mcp**](https://github.com/mnsmasum62786/was-ga4-mcp) | Queries GA4 standard, realtime, batch and pivot reports and manages properties through a JavaScript stdio MCP server. Stores OAuth credentials locally and exposes Data and Admin API tools. |
| [**Newsstate/ga4-mcp**](https://github.com/Newsstate/ga4-mcp) | Queries GA4 reports, realtime metrics, and Search Console search performance through a Next.js MCP endpoint. Uses Google user OAuth and provides page, acquisition, audience, and event report presets. |
| [**onionst/ga4-toolkit**](https://github.com/onionst/ga4-toolkit) | Queries GA4 reports, realtime data and metadata through a Python CLI and MCP server. Provides overview, page, acquisition and event presets with service-account or user ADC credentials. |
| [**rablab-mtl/mcp-ga4-gsc**](https://github.com/rablab-mtl/mcp-ga4-gsc) | Queries GA4 reports, realtime activity, pivots and schema metadata alongside Search Console data from a TypeScript server on Cloudflare Workers. Uses per-user Google OAuth authorization. |
| [**scalably-io/ga4-mcp**](https://github.com/scalably-io/ga4-mcp) | Queries GA4 standard, batch, pivot, realtime, and funnel reports through a Python MCP server and checks dimension compatibility. Reads property configuration, custom definitions, annotations, audiences, and access reports using service account credentials or ADC. |
| [**sednalabs/ga4-mcp**](https://github.com/sednalabs/ga4-mcp) | Queries GA4 reports, realtime data, funnels and property metadata from a Rust MCP server. Imports report rows into an in-memory DuckDB scratchpad for local SQL queries. |
| [**stufently/google-webtools-mcp**](https://github.com/stufently/google-webtools-mcp) | Queries GA4 reports, realtime activity and metadata and manages properties from a TypeScript MCP server alongside Search Console and site-verification tools. Supports OAuth and service-account credentials. |
| [**surendranb/google-analytics-mcp**](https://github.com/surendranb/google-analytics-mcp) | Queries GA4 reports through a Python MCP server with live dimension and metric discovery, schema validation, and cached property metadata. Guides credential setup and recovery through MCP elicitation. |
| [**TheTechBasket/GA4-Dashboard-MCP**](https://github.com/TheTechBasket/GA4-Dashboard-MCP) | Queries GA4 reports, realtime data, funnels and property settings through a JavaScript MCP server. Includes cached reads, request limits and a web dashboard with a Three.js globe. |

## 2. CLI tools (5)

| Project | What it does |
| --- | --- |
| [**Bin-Huang/google-analytics-cli**](https://github.com/Bin-Huang/google-analytics-cli) | Runs GA4 standard, pivot, batch and realtime reports from a TypeScript CLI using the Data API. Reads Admin configuration and exports audiences with JSON output and named credential profiles. |
| [**Hasim-cim/ga4-mcp**](https://github.com/Hasim-cim/ga4-mcp) | Runs GA4 reports, realtime queries, and property inspection from a Python command-line tool. Provides page, acquisition, demographic, and custom-report presets using Application Default Credentials. |
| [**kasdimg/analytics-cli**](https://github.com/kasdimg/analytics-cli) | Queries GA4 reports and Search Console analytics through a JavaScript CLI. Returns summary, page, device and custom-query results using shared service-account credentials. |
| [**nyosegawa/gacli**](https://github.com/nyosegawa/gacli) | Queries GA4 summaries, pages, realtime activity and custom reports through a Python CLI. Stores separate OAuth profiles and supports filtered queries with selectable output formats. |
| [**sulimanbenhalim/ga-cli**](https://github.com/sulimanbenhalim/ga-cli) | Creates, updates and deletes GA4 properties and data streams through a Python CLI using the Admin API. Lists accounts and supports local credential configuration. |

## 3. SDKs (16)

| Project | What it does |
| --- | --- |
| [**.NET — Google.Analytics.Admin.V1Beta**](https://github.com/googleapis/google-cloud-dotnet/tree/main/apis/Google.Analytics.Admin.V1Beta) | Manages GA4 accounts, properties, data streams and custom definitions with Google's official .NET Admin API client. |
| [**.NET — Google.Analytics.Data.V1Beta**](https://github.com/googleapis/google-cloud-dotnet/tree/main/apis/Google.Analytics.Data.V1Beta) | Queries GA4 reports and realtime activity with Google's official .NET Data API client. |
| [**adswerve/GA4-Measurement-Protocol-Python**](https://github.com/adswerve/GA4-Measurement-Protocol-Python) | Sends and validates GA4 Measurement Protocol events from Python for web and Firebase app streams. Provides a community SDK with queued events and persistent client state. |
| [**Go — analytics/admin/v1beta**](https://github.com/googleapis/go-genproto/tree/main/googleapis/analytics/admin/v1beta) | Calls the GA4 Admin API with Google's generated Go gRPC client and protobuf request types. Requires an authenticated gRPC connection supplied by the application. |
| [**Go — analytics/data/v1beta**](https://github.com/googleapis/go-genproto/tree/main/googleapis/analytics/data/v1beta) | Calls the GA4 Data API with Google's generated Go gRPC client and protobuf request types. Requires an authenticated gRPC connection supplied by the application. |
| [**Java — google-analytics-admin**](https://github.com/googleapis/google-cloud-java/tree/main/java-analytics-admin) | Manages GA4 accounts, properties, data streams and custom definitions with Google's official Java Admin API client. |
| [**Java — google-analytics-data**](https://github.com/googleapis/google-cloud-java/tree/main/java-analytics-data) | Queries GA4 reports and realtime activity with Google's official Java Data API client. |
| [**MarkEdmondson1234/googleAnalyticsR**](https://github.com/MarkEdmondson1234/googleAnalyticsR) | Queries GA4 reports and realtime data from R with dimension filters and metric expressions. Provides a community SDK with data-frame results and Admin API helpers. |
| [**Node.js — @google-analytics/admin**](https://github.com/googleapis/google-cloud-node/tree/main/packages/google-analytics-admin) | Manages GA4 accounts, properties, data streams and custom definitions with Google's official Node.js Admin API client. |
| [**Node.js — @google-analytics/data**](https://github.com/googleapis/google-cloud-node/tree/main/packages/google-analytics-data) | Queries GA4 reports and realtime activity with Google's official Node.js Data API client. |
| [**PHP — google/analytics-admin**](https://github.com/googleapis/google-cloud-php/tree/main/AnalyticsAdmin) | Manages GA4 accounts, properties, data streams and custom definitions with Google's official PHP Admin API client. |
| [**PHP — google/analytics-data**](https://github.com/googleapis/google-cloud-php/tree/main/AnalyticsData) | Queries GA4 reports and realtime activity with Google's official PHP Data API client. |
| [**Python — google-analytics-admin**](https://github.com/googleapis/google-cloud-python/tree/main/packages/google-analytics-admin) | Manages GA4 accounts, properties, data streams and custom definitions with Google's official Python Admin API client. |
| [**Python — google-analytics-data**](https://github.com/googleapis/google-cloud-python/tree/main/packages/google-analytics-data) | Queries GA4 reports and realtime activity with Google's official Python Data API client. |
| [**Ruby — google-analytics-admin-v1alpha**](https://github.com/googleapis/google-cloud-ruby/tree/main/google-analytics-admin-v1alpha) | Manages GA4 accounts, properties, data streams and custom definitions with Google's official Ruby Admin API client. |
| [**Ruby — google-analytics-data-v1beta**](https://github.com/googleapis/google-cloud-ruby/tree/main/google-analytics-data-v1beta) | Queries GA4 reports and realtime activity with Google's official Ruby Data API client. |

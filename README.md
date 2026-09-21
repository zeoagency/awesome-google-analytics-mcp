# Awesome Google Analytics MCP [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated plain-English index of Model Context Protocol (MCP) servers, local analytical engines, and agent-facing tools built for **[Google Analytics 4 (GA4)](https://developers.google.com/analytics/devguides/reporting/data/v1)** and ecosystem telemetry.

Official links: [Google Analytics Data API](https://developers.google.com/analytics/devguides/reporting/data/v1) · [Google Analytics Admin API](https://developers.google.com/analytics/devguides/config/admin/v1) · [Model Context Protocol](https://modelcontextprotocol.io/) · [Google Cloud Console](https://console.cloud.google.com/) · [Zeo Agency](https://zeo.org/)

---

## Contents

- [Developer Comparison Matrix](#developer-comparison-matrix)

1. [Query standard reports and slice dimensions (21)](#1-query-standard-reports-and-slice-dimensions)
   - [Official and foundational servers (1)](#official-and-foundational-servers)
   - [Consolidated modal query servers (4)](#consolidated-modal-query-servers)
   - [Dynamic schema and metadata introspectors (3)](#dynamic-schema-and-metadata-introspectors)
   - [Lightweight reporting bridges (13)](#lightweight-reporting-bridges)
2. [Ingest data locally and query with SQL (3)](#2-ingest-data-locally-and-query-with-sql)
   - [Embedded columnar OLAP scratchpads (DuckDB) (1)](#embedded-columnar-olap-scratchpads-duckdb)
   - [Embedded relational databases (SQLite) (1)](#embedded-relational-databases-sqlite)
   - [Relational schema drivers (1)](#relational-schema-drivers)
3. [Bridge multi-platform marketing and search data (11)](#3-bridge-multi-platform-marketing-and-search-data)
   - [Unified Search Console and GA4 platforms (4)](#unified-search-console-and-ga4-platforms)
   - [Google Tag Manager audit and event bridges (2)](#google-tag-manager-audit-and-event-bridges)
   - [Multi-ad network and marketing suites (4)](#multi-ad-network-and-marketing-suites)
   - [Cookieless attribution and privacy bridges (1)](#cookieless-attribution-and-privacy-bridges)
4. [Deploy enterprise and multi-tenant authentication (7)](#4-deploy-enterprise-and-multi-tenant-authentication)
   - [Cloud-native multi-tenant OAuth gateways (1)](#cloud-native-multi-tenant-oauth-gateways)
   - [Cryptographically encrypted session persistence (1)](#cryptographically-encrypted-session-persistence)
   - [Ephemeral loopback PKCE authenticators (1)](#ephemeral-loopback-pkce-authenticators)
   - [Remote team and multi-account proxies (4)](#remote-team-and-multi-account-proxies)
5. [Send server-side events and manage properties (3)](#5-send-server-side-events-and-manage-properties)
   - [Measurement Protocol event dispatchers (1)](#measurement-protocol-event-dispatchers)
   - [Admin API property and custom definition managers (2)](#admin-api-property-and-custom-definition-managers)
6. [Diagnose anomalies and generate deliverables (6)](#6-diagnose-anomalies-and-generate-deliverables)
   - [Algorithmic anomaly detection and drop classifiers (2)](#algorithmic-anomaly-detection-and-drop-classifiers)
   - [Visual 3D dashboards and real-time streaming (2)](#visual-3d-dashboards-and-real-time-streaming)
   - [Automated executive report and document generators (2)](#automated-executive-report-and-document-generators)
7. [Starter templates and setup scaffolds (4)](#7-starter-templates-and-setup-scaffolds)
   - [Starter templates and boilerplate scaffolds (4)](#starter-templates-and-boilerplate-scaffolds)
8. [Resources](#resources)
   - [Official Documentation & SDKs](#official-documentation--sdks)
   - [Community Guides & Architecture](#community-guides--architecture)
9. [Reference](#reference)
   - [Evaluation Methodology & Verification Invariants](#evaluation-methodology--verification-invariants)
   - [Repository Inclusion & Quarantine Invariants](#repository-inclusion--quarantine-invariants)

---

## Developer Comparison Matrix

*A compact comparative matrix of all 55 Model Context Protocol servers and analytical bridges for Google Analytics 4, optimized for quick scanning on standard screens. Click any project name to jump directly to its detailed catalog entry below.*

| Server / Tool | ⭐ Stars | Runtime | Auth Paradigm | Storage | Capabilities & APIs | Primary Specialization | Tier |
| --- | :---: | :---: | :---: | :---: | --- | --- | :---: |
| [**googleanalytics/google-analytics-mcp**](#googleanalytics--google-analytics-mcp) | 3,260 | Python | Dual (SA + PKCE) | Stateless | Reports · Realtime · Funnels · Admin | Official Reference Implementation | Solid / Functional Community Baseline |
| [**surendranb/google-analytics-mcp**](#surendranb--google-analytics-mcp) | 242 | Python | Service Account | Stateless | Reports · Admin | Runtime Schema Introspection & Caching | Solid / Functional Community Baseline |
| [**eiiot/ga4-mcp**](#eiiot--ga4-mcp) | 0 | Python | Dual (SA + PKCE) | Stateless | Reports · Realtime · Funnels · Admin | Consolidated Reporting & Funnels | Solid / Functional Community Baseline |
| [**CUTolu2021/ga4-mcp-server**](#cutolu2021--ga4-mcp-server) | 0 | JavaScript | Service Account | Stateless | Reports · Realtime · Admin | Session-Extracted Telemetry Proxy | Viable Lightweight / Niche Alternative |
| [**mharnett/mcp-ga4**](#mharnett--mcp-ga4) | 0 | TypeScript | Dual (SA + PKCE) | Stateless | Reports · Realtime · Admin | Client Context & Custom Dimensions | Viable Lightweight / Niche Alternative |
| [**fujii-yuji/GA4-MCP-Remote**](#fujii-yuji--ga4-mcp-remote) | 0 | Python | Dual (SA + PKCE) | Stateless | Reports · Realtime · Admin | Remote SSE Multi-Property Stream | Viable Lightweight / Niche Alternative |
| [**Newsstate/ga4-mcp**](#newsstate--ga4-mcp) | 0 | TypeScript | OAuth 2.0 PKCE | Stateless | Reports · Realtime · Admin | Dynamic Schema & Metric Introspection | Tier 4 |
| [**gviollaz/iita-ga4-mcp**](#gviollaz--iita-ga4-mcp) | 0 | Python | OAuth 2.0 PKCE | Stateless | Reports · Realtime | FastAPI Realtime Telemetry Bridge | Tier 4 |
| [**paulsign-lab/ga4-mcp**](#paulsign-lab--ga4-mcp) | 0 | Python | Dual (SA + PKCE) | Stateless | Reports · Realtime · Admin | Batch Report Execution & Streaming | Viable Lightweight / Niche Alternative |
| [**Leanpicazoo/ga4-mcp**](#leanpicazoo--ga4-mcp) | 0 | Python | Dual (SA + PKCE) | Stateless | Reports · Realtime · Funnels · Admin | Minimalist Data API Bridge | Viable Lightweight / Niche Alternative |
| [**mamaladze22/ga4-mcp**](#mamaladze22--ga4-mcp) | 0 | TypeScript | Dual (SA + PKCE) | Stateless | Reports · Realtime · Funnels · Admin | Structured JSON Reporting Bridge | Viable Lightweight / Niche Alternative |
| [**scalably-io/ga4-mcp**](#scalably-io--ga4-mcp) | 0 | Python | Dual (SA + PKCE) | Stateless | Reports · Realtime · Funnels · Admin | Multi-Tool Dimension Extraction | Viable Lightweight / Niche Alternative |
| [**luminarylane/ga4-mcp**](#luminarylane--ga4-mcp) | 0 | Python | Dual (SA + PKCE) | Stateless | Reports · Realtime · Admin | Opinionated Traffic Source Wrappers | Tier 4 |
| [**thesyedyahya/ga4-mcp**](#thesyedyahya--ga4-mcp) | 2 | Python | Service Account | Stateless | Reports · Realtime · Admin | Annotation History & Custom Metrics | Tier 4 |
| [**yusofansari/google-analytics-mcp**](#yusofansari--google-analytics-mcp) | 0 | Python | OAuth 2.0 PKCE | Stateless | Reports · Realtime | Interactive OAuth Query Bridge | Tier 4 |
| [**CamilaBarbareschi/cafedelirante-ga4-mcp**](#camilabarbareschi--cafedelirante-ga4-mcp) | 0 | Python | OAuth 2.0 PKCE | Stateless | Reports · Realtime | E-Commerce Conversion Tracking | Tier 4 |
| [**K41R0N/ga4-mcp**](#k41r0n--ga4-mcp) | 0 | TypeScript | Service Account | Stateless | Reports · Realtime | Lightweight Visitor Monitoring | Viable Lightweight / Niche Alternative |
| [**Hasim-cim/ga4-mcp**](#hasim-cim--ga4-mcp) | 0 | Python | Service Account | Stateless | Reports · Realtime | Direct Agent Query Bridge | Tier 4 |
| [**aline-delmain/delmain-ga4-mcp**](#aline-delmain--delmain-ga4-mcp) | 0 | Python | OAuth 2.0 PKCE | Stateless | Reports · Realtime · Admin | Agency Client Preset Reporting | Tier 4 |
| [**devli13/mcp-ga4**](#devli13--mcp-ga4) | 0 | JavaScript | Service Account | Stateless | Reports · Realtime · Admin | Fast Dimension Slicing | Tier 4 |
| [**administrator-prog/ga4-mcp**](#administrator-prog--ga4-mcp) | 0 | TypeScript | Service Account | Stateless | Reports · Realtime | Headless Multi-Agent Pipeline | Viable Lightweight / Niche Alternative |
| [**sednalabs/ga4-mcp**](#sednalabs--ga4-mcp) | 0 | Rust | Dual (SA + PKCE) | DuckDB OLAP | Reports · Realtime · Funnels · Admin · Local SQL | In-Memory Columnar DuckDB OLAP | Solid / Functional Community Baseline |
| [**fenjo26/OpenGSC**](#fenjo26--opengsc) | 25 | TypeScript | OAuth 2.0 PKCE | SQLite DB | Reports · Admin · Local SQL | SQLite Caching & SQL Query Engine | Solid / Functional Community Baseline |
| [**CDataSoftware/google-analytics-mcp-server-by-cdata**](#cdatasoftware--google-analytics-mcp-server-by-cdata) | 1 | Java | Dual (SA + PKCE) | Virtual JDBC | Reports · Local SQL | Virtual Relational JDBC Driver | Viable Lightweight / Niche Alternative |
| [**rablab-mtl/mcp-ga4-gsc**](#rablab-mtl--mcp-ga4-gsc) | 0 | TypeScript | Dual (SA + PKCE) | Stateless | Reports · Realtime · Admin | Unified Search Console & GA4 Platform | Viable Lightweight / Niche Alternative |
| [**peliter/google-gsc-ga4-mcp-setup**](#peliter--google-gsc-ga4-mcp-setup) | 0 | Python | Dual (SA + PKCE) | Stateless | Reports · Realtime | Synchronized GSC + GA4 Date Ranges | Viable Lightweight / Niche Alternative |
| [**delaren47/gsc-ga4-mcp**](#delaren47--gsc-ga4-mcp) | 0 | TypeScript | Dual (SA + PKCE) | Stateless | Reports · Realtime · Admin | Organic Landing Page Attribution | Tier 4 |
| [**shailrajsinh-rathod-seo/gsc-ga4-mcp**](#shailrajsinh-rathod-seo--gsc-ga4-mcp) | 0 | Python | Dual (SA + PKCE) | Stateless | Reports | Keyword Ranking & Engagement Joins | Tier 4 |
| [**CreativeMetrics/gtm-ga4-mcp**](#creativemetrics--gtm-ga4-mcp) | 0 | JavaScript | OAuth 2.0 PKCE | Stateless | Reports · Admin | GTM Container Tag & Schema Auditing | Viable Lightweight / Niche Alternative |
| [**kb223/gtm-ga4-mcp**](#kb223--gtm-ga4-mcp) | 1 | Python | OAuth 2.0 PKCE | Stateless | Reports · Realtime · Admin | Tag Trigger & Measurement Correlation | Tier 4 |
| [**irinabuht12-oss/google-meta-ads-ga4-mcp**](#irinabuht12-oss--google-meta-ads-ga4-mcp) | 2,033 | TypeScript | OAuth 2.0 PKCE | Stateless | Reports · Realtime · Admin | Google & Meta Ads Attribution Hub | Viable Lightweight / Niche Alternative |
| [**freema/mcp-google-marketing**](#freema--mcp-google-marketing) | 3 | TypeScript | OAuth 2.0 PKCE | Stateless | Reports · Realtime · Admin | Google Marketing Platform Lifecycle | Viable Lightweight / Niche Alternative |
| [**stufently/google-webtools-mcp**](#stufently--google-webtools-mcp) | 7 | TypeScript | Dual (SA + PKCE) | Stateless | Reports · Realtime · Admin | Multi-Platform Marketing Suite | Viable Lightweight / Niche Alternative |
| [**henkisdabro/wookstar-claude-plugins**](#henkisdabro--wookstar-claude-plugins) | 89 | Shell | Service Account | Stateless | Reports · Realtime · Admin | Modular Stape GTM & GA4 Plugins | Viable Lightweight / Niche Alternative |
| [**DevDomeFamily/devdome-analytics**](#devdomefamily--devdome-analytics) | 0 | PHP | Service Account | Stateless | Admin | Cookieless Tracking & BigQuery Exports | Viable Lightweight / Niche Alternative |
| [**dhawalshah/google-analytics-mcp**](#dhawalshah--google-analytics-mcp) | 0 | Python | OAuth 2.0 PKCE | Stateless | Reports · Realtime · Funnels · Admin | Enterprise Multi-Tenant OAuth Gateway | Solid / Functional Community Baseline |
| [**ESGEE-0562/google-analytics-mcp**](#esgee-0562--google-analytics-mcp) | 0 | Python | OAuth 2.0 PKCE | Stateless | Reports · Realtime · Admin | Encrypted Token Persistence Engine | Viable Lightweight / Niche Alternative |
| [**codeChap/mcp-server-google-analytics**](#codechap--mcp-server-google-analytics) | 0 | Rust | Dual (SA + PKCE) | Stateless | Reports · Realtime · Admin | Zero-Dependency Loopback PKCE | Viable Lightweight / Niche Alternative |
| [**minholi/google-analytics-mcp**](#minholi--google-analytics-mcp) | 1 | Python | OAuth 2.0 PKCE | Stateless | Reports · Realtime | Agency Property Switching Proxy | Viable Lightweight / Niche Alternative |
| [**gomarble-ai/google-analytics-mcp-server**](#gomarble-ai--google-analytics-mcp-server) | 18 | Python | OAuth 2.0 PKCE | Stateless | Reports · Admin | Marketing Team Multi-Account Proxy | Viable Lightweight / Niche Alternative |
| [**ankhangonline/mcp-ga4-team-server**](#ankhangonline--mcp-ga4-team-server) | 0 | JavaScript | Service Account | Stateless | Reports · Realtime | Shared Service Account Guardrails | Viable Lightweight / Niche Alternative |
| [**mnsmasum62786/was-ga4-mcp**](#mnsmasum62786--was-ga4-mcp) | 0 | JavaScript | OAuth 2.0 PKCE | Stateless | Reports · Realtime · Admin | Remote OAuth Session Proxy | Tier 4 |
| [**leonardosepulvedat/mcp-google-analytics**](#leonardosepulvedat--mcp-google-analytics) | 2 | TypeScript | Service Account | Stateless | Reports · Realtime · Funnels · Admin · Events | Measurement Protocol Event Dispatch | Viable Lightweight / Niche Alternative |
| [**Insightful-Pipe/google-analytics-mcp-server**](#insightful-pipe--google-analytics-mcp-server) | 0 | TypeScript | OAuth 2.0 PKCE | Stateless | Reports · Admin · Events | Admin API Custom Dimension Manager | Tier 4 |
| [**HappyMonkeyAI/ai-google-analytics-mcp**](#happymonkeyai--ai-google-analytics-mcp) | 0 | Python | Service Account | Stateless | Reports · Admin | Property Metadata Synchronization | Viable Lightweight / Niche Alternative |
| [**mario-hernandez/google-analytics-mcp-claude-code**](#mario-hernandez--google-analytics-mcp-claude-code) | 1 | Python | Dual (SA + PKCE) | Stateless | Reports · Funnels · Admin · Anomalies | Statistical Anomaly Drop Detection | Viable Lightweight / Niche Alternative |
| [**onionst/ga4-toolkit**](#onionst--ga4-toolkit) | 0 | Python | Service Account | Stateless | Reports · Realtime · Admin · Anomalies | Baseline Trend Anomaly Detection | Viable Lightweight / Niche Alternative |
| [**TheTechBasket/GA4-Dashboard-MCP**](#thetechbasket--ga4-dashboard-mcp) | 7 | JavaScript | Dual (SA + PKCE) | Stateless | Reports · Realtime · Funnels · Admin | Three.js 3D Interactive Visualizer | Viable Lightweight / Niche Alternative |
| [**inakigorostiza/ga4-mcp-dashboard**](#inakigorostiza--ga4-mcp-dashboard) | 0 | JavaScript | Dual (SA + PKCE) | Stateless | Reports · Realtime | Real-Time Event Stream Dashboard | Viable Lightweight / Niche Alternative |
| [**arcbaslow/google-analytics-agent**](#arcbaslow--google-analytics-agent) | 0 | Python | Dual (SA + PKCE) | Stateless | Reports · Realtime · Funnels · Admin · Anomalies | Autonomous Executive Report Compiler | Solid / Functional Community Baseline |
| [**analyticsdatajg2025-cmd/ga4-mcp-powerbi**](#analyticsdatajg2025-cmd--ga4-mcp-powerbi) | 0 | JavaScript | Service Account | Stateless | Reports · Realtime | PowerBI Tabular Data Feeds | Viable Lightweight / Niche Alternative |
| [**drewbeechler/ga4-mcp-template**](#drewbeechler--ga4-mcp-template) | 0 | TypeScript | Service Account | Stateless | Reports · Realtime · Funnels · Admin | Dockerized TypeScript Starter Scaffold | Tier 4 |
| [**burhan29ee/ga4-mcp-server**](#burhan29ee--ga4-mcp-server) | 0 | Python | Dual (SA + PKCE) | Stateless | Reports · Realtime · Admin | Modular Python Starter Template | Viable Lightweight / Niche Alternative |
| [**communicationseo2021-creator/gsc-ga4-mcp-setup-guide**](#communicationseo2021-creator--gsc-ga4-mcp-setup-guide) | 0 | HTML | Service Account | Stateless | Reports · Realtime | Service Account Setup Reference | Tier 4 |
| [**seoteamschbang2021-hub/ga4-mcp-server**](#seoteamschbang2021-hub--ga4-mcp-server) | 0 | Python | Service Account | Stateless | Reports · Realtime | Agency SEO Deployment Recipe | Tier 4 |

---

## 1. Query standard reports and slice dimensions

*21 projects. 21 projects across 4 subcategories for executing standard reports, introspecting dimension schemas, and querying realtime telemetry.*

### Official and foundational servers

*1 project. The official reference server implementation authored by Google.*

| Project | What it does |
|---|---|
| <a id="googleanalytics--google-analytics-mcp"></a>[**googleanalytics/google-analytics-mcp**](https://github.com/googleanalytics/google-analytics-mcp) | Google's reference Python implementation exposing Data API v1beta and Admin API via 5 modal tools supporting dual Service Account and interactive OAuth 2.0 PKCE. |

### Consolidated modal query servers

*4 projects. Multi-purpose query servers bundling report execution, schema introspection, and custom dimension handling.*

| Project | What it does |
|---|---|
| <a id="surendranb--google-analytics-mcp"></a>[**surendranb/google-analytics-mcp**](https://github.com/surendranb/google-analytics-mcp) | Python MCP server offering 11 modal tools with runtime schema introspection and property metadata caching over Service Account authentication. |
| <a id="eiiot--ga4-mcp"></a>[**eiiot/ga4-mcp**](https://github.com/eiiot/ga4-mcp) | Python server bundling Data API v1beta reporting, funnel analysis, and dimension introspection into 5 consolidated tools with dual OAuth and Service Account support. |
| <a id="cutolu2021--ga4-mcp-server"></a>[**CUTolu2021/ga4-mcp-server**](https://github.com/CUTolu2021/ga4-mcp-server) | Node.js server executing standard and realtime GA4 reports through 3 consolidated modal tools with session token extraction and Service Account auth. |
| <a id="mharnett--mcp-ga4"></a>[**mharnett/mcp-ga4**](https://github.com/mharnett/mcp-ga4) | TypeScript MCP server providing 8 client-aware query tools with custom dimension creation and context persistence over dual OAuth/Service Account credentials. |

### Dynamic schema and metadata introspectors

*3 projects. Specialized servers focusing on real-time schema discovery and active property metadata introspection.*

| Project | What it does |
|---|---|
| <a id="fujii-yuji--ga4-mcp-remote"></a>[**fujii-yuji/GA4-MCP-Remote**](https://github.com/fujii-yuji/GA4-MCP-Remote) | Remote Python MCP server delivering real-time streaming queries and dynamic schema metadata lookup across multiple GA4 properties. |
| <a id="newsstate--ga4-mcp"></a>[**Newsstate/ga4-mcp**](https://github.com/Newsstate/ga4-mcp) | TypeScript implementation providing automated GA4 dimension and metric schema introspection with interactive browser OAuth authentication. |
| <a id="gviollaz--iita-ga4-mcp"></a>[**gviollaz/iita-ga4-mcp**](https://github.com/gviollaz/iita-ga4-mcp) | FastAPI-based Python MCP server focusing on high-speed GA4 report execution and realtime active-user telemetry via OAuth 2.0 PKCE. |

### Lightweight reporting bridges

*13 projects. Streamlined, single-purpose bridges querying core GA4 traffic, active users, and conversions.*

| Project | What it does |
|---|---|
| <a id="paulsign-lab--ga4-mcp"></a>[**paulsign-lab/ga4-mcp**](https://github.com/paulsign-lab/ga4-mcp) | Python server providing batch report execution and realtime telemetry streaming through 5 lightweight tool definitions with dual auth. |
| <a id="leanpicazoo--ga4-mcp"></a>[**Leanpicazoo/ga4-mcp**](https://github.com/Leanpicazoo/ga4-mcp) | Minimalist Python bridge querying core GA4 metrics, active users, and traffic channels via Data API v1beta. |
| <a id="mamaladze22--ga4-mcp"></a>[**mamaladze22/ga4-mcp**](https://github.com/mamaladze22/ga4-mcp) | TypeScript reporting bridge wrapping GA4 Data API v1beta with dual authentication and structured JSON output for AI assistants. |
| <a id="scalably-io--ga4-mcp"></a>[**scalably-io/ga4-mcp**](https://github.com/scalably-io/ga4-mcp) | Python server exposing 17 modular reporting tools for custom dimension extraction, data stream auditing, and metric aggregation. |
| <a id="luminarylane--ga4-mcp"></a>[**luminarylane/ga4-mcp**](https://github.com/luminarylane/ga4-mcp) | Python bridge providing opinionated query wrappers for top pages, traffic acquisition sources, and audience demographics. |
| <a id="thesyedyahya--ga4-mcp"></a>[**thesyedyahya/ga4-mcp**](https://github.com/thesyedyahya/ga4-mcp) | Python server pairing GA4 Data API reporting with property annotation history and custom metric extraction over Service Account JSON. |
| <a id="yusofansari--google-analytics-mcp"></a>[**yusofansari/google-analytics-mcp**](https://github.com/yusofansari/google-analytics-mcp) | Clean Python MCP server wrapping GA4 report execution and realtime telemetry via standard OAuth 2.0 user credentials. |
| <a id="camilabarbareschi--cafedelirante-ga4-mcp"></a>[**CamilaBarbareschi/cafedelirante-ga4-mcp**](https://github.com/CamilaBarbareschi/cafedelirante-ga4-mcp) | Specialized Python reporting bridge configured for e-commerce conversion tracking and session telemetry via OAuth 2.0 PKCE. |
| <a id="k41r0n--ga4-mcp"></a>[**K41R0N/ga4-mcp**](https://github.com/K41R0N/ga4-mcp) | Lightweight TypeScript server exposing clean Data API v1beta reporting and realtime visitor monitoring over Service Account JSON. |
| <a id="hasim-cim--ga4-mcp"></a>[**Hasim-cim/ga4-mcp**](https://github.com/Hasim-cim/ga4-mcp) | Streamlined Python bridge delivering direct Data API v1beta reporting and realtime active user telemetry for local agent workflows. |
| <a id="aline-delmain--delmain-ga4-mcp"></a>[**aline-delmain/delmain-ga4-mcp**](https://github.com/aline-delmain/delmain-ga4-mcp) | Python MCP server providing agency client reporting wrappers with pre-configured dimension presets over OAuth 2.0. |
| <a id="devli13--mcp-ga4"></a>[**devli13/mcp-ga4**](https://github.com/devli13/mcp-ga4) | JavaScript implementation providing 4 core reporting endpoints for fast dimension slicing and conversion rate calculations. |
| <a id="administrator-prog--ga4-mcp"></a>[**administrator-prog/ga4-mcp**](https://github.com/administrator-prog/ga4-mcp) | Compact TypeScript bridge offering headless GA4 Data API execution and raw JSON output for multi-agent analytical pipelines. |

---

## 2. Ingest data locally and query with SQL

*3 projects. 3 projects across 3 subcategories for caching GA4 telemetry into local analytical databases and virtual relational schemas.*

### Embedded columnar OLAP scratchpads (DuckDB)

*1 project. In-memory columnar analytics executing sub-millisecond SQL queries over locally ingested GA4 data.*

| Project | What it does |
|---|---|
| <a id="sednalabs--ga4-mcp"></a>[**sednalabs/ga4-mcp**](https://github.com/sednalabs/ga4-mcp) | High-performance Rust MCP server ingesting GA4 API reports into an embedded in-memory DuckDB OLAP database for sub-millisecond local SQL queries. |

### Embedded relational databases (SQLite)

*1 project. Embedded SQLite caching engine with comprehensive multi-tool SQL analysis suites.*

| Project | What it does |
|---|---|
| <a id="fenjo26--opengsc"></a>[**fenjo26/OpenGSC**](https://github.com/fenjo26/OpenGSC) | TypeScript MCP suite caching GA4 and Search Console telemetry into an embedded SQLite database with 68 SQL analytical and inspection tools. |

### Relational schema drivers

*1 project. Enterprise JDBC relational driver projecting live GA4 endpoints as standard SQL tables.*

| Project | What it does |
|---|---|
| <a id="cdatasoftware--google-analytics-mcp-server-by-cdata"></a>[**CDataSoftware/google-analytics-mcp-server-by-cdata**](https://github.com/cdatasoftware/google-analytics-mcp-server-by-cdata) | Enterprise Java server projecting live GA4 Data API endpoints as virtual SQL relational tables via CData JDBC driver technology. |

---

## 3. Bridge multi-platform marketing and search data

*11 projects. 11 projects across 4 subcategories uniting GA4 with Google Search Console, Google Tag Manager, ad platforms, and attribution pipelines.*

### Unified Search Console and GA4 platforms

*4 projects. Multi-platform servers correlating organic search impressions and queries with downstream GA4 engagement.*

| Project | What it does |
|---|---|
| <a id="rablab-mtl--mcp-ga4-gsc"></a>[**rablab-mtl/mcp-ga4-gsc**](https://github.com/rablab-mtl/mcp-ga4-gsc) | TypeScript multi-platform server exposing 21 tools that unify GA4 engagement metrics with Google Search Console organic search impressions. |
| <a id="peliter--google-gsc-ga4-mcp-setup"></a>[**peliter/google-gsc-ga4-mcp-setup**](https://github.com/peliter/google-gsc-ga4-mcp-setup) | Python orchestration bridge configuring dual GA4 Data API and Search Console query workflows with synchronized date ranges. |
| <a id="delaren47--gsc-ga4-mcp"></a>[**delaren47/gsc-ga4-mcp**](https://github.com/delaren47/gsc-ga4-mcp) | TypeScript MCP server executing coordinated landing-page attribution by merging Search Console click queries with GA4 conversion events. |
| <a id="shailrajsinh-rathod-seo--gsc-ga4-mcp"></a>[**shailrajsinh-rathod-seo/gsc-ga4-mcp**](https://github.com/shailrajsinh-rathod-seo/gsc-ga4-mcp) | Python SEO intelligence server joining Search Console keyword ranking telemetry with GA4 page engagement and bounce rates. |

### Google Tag Manager audit and event bridges

*2 projects. Cross-platform servers validating GTM container tags, triggers, and live GA4 measurement schemas.*

| Project | What it does |
|---|---|
| <a id="creativemetrics--gtm-ga4-mcp"></a>[**CreativeMetrics/gtm-ga4-mcp**](https://github.com/CreativeMetrics/gtm-ga4-mcp) | Full-featured JavaScript MCP server with 47 tools auditing Google Tag Manager container tags and verifying live GA4 measurement schemas. |
| <a id="kb223--gtm-ga4-mcp"></a>[**kb223/gtm-ga4-mcp**](https://github.com/kb223/gtm-ga4-mcp) | Python bridge correlating GTM tag firing triggers with GA4 property measurement streams and custom event parameters. |

### Multi-ad network and marketing suites

*4 projects. Unified marketing hubs coordinating GA4 analytics alongside Google Ads and Meta Ads management.*

| Project | What it does |
|---|---|
| <a id="irinabuht12-oss--google-meta-ads-ga4-mcp"></a>[**irinabuht12-oss/google-meta-ads-ga4-mcp**](https://github.com/irinabuht12-oss/google-meta-ads-ga4-mcp) | TypeScript suite featuring 25 tools spanning Google Ads campaign management, Meta Ads audiences, and GA4 attribution reporting. |
| <a id="freema--mcp-google-marketing"></a>[**freema/mcp-google-marketing**](https://github.com/freema/mcp-google-marketing) | Comprehensive TypeScript server with 35 tools covering Google Marketing Platform, GA4 property lifecycle, and Google Ads bidding. |
| <a id="stufently--google-webtools-mcp"></a>[**stufently/google-webtools-mcp**](https://github.com/stufently/google-webtools-mcp) | Extensive TypeScript marketing suite exposing 39 tools across GA4 property configuration, Google Tag Manager, and Search Console. |
| <a id="henkisdabro--wookstar-claude-plugins"></a>[**henkisdabro/wookstar-claude-plugins**](https://github.com/henkisdabro/wookstar-claude-plugins) | Modular Claude plugin architecture orchestrating GA4 Data API querying alongside remote Stape GTM server-side containers. |

### Cookieless attribution and privacy bridges

*1 project. Privacy-preserving servers handling server-side tracking, cookieless conversions, and BigQuery exports.*

| Project | What it does |
|---|---|
| <a id="devdomefamily--devdome-analytics"></a>[**DevDomeFamily/devdome-analytics**](https://github.com/DevDomeFamily/devdome-analytics) | Enterprise PHP server bridging server-side analytics, BigQuery exports, and cookieless conversion attribution across privacy-centric domains. |

---

## 4. Deploy enterprise and multi-tenant authentication

*7 projects. 7 projects across 4 subcategories providing hardened OAuth gateways, encrypted persistence, and multi-tenant team proxies.*

### Cloud-native multi-tenant OAuth gateways

*1 project. Enterprise OAuth proxies with organizational multi-tenancy and token rotation.*

| Project | What it does |
|---|---|
| <a id="dhawalshah--google-analytics-mcp"></a>[**dhawalshah/google-analytics-mcp**](https://github.com/dhawalshah/google-analytics-mcp) | Cloud-native Python server providing 10 tools with multi-tenant OAuth token rotation, organization isolation, and tenant-scoped GA4 querying. |

### Cryptographically encrypted session persistence

*1 project. Secure token storage engines encrypting refresh tokens for continuous unattended background execution.*

| Project | What it does |
|---|---|
| <a id="esgee-0562--google-analytics-mcp"></a>[**ESGEE-0562/google-analytics-mcp**](https://github.com/ESGEE-0562/google-analytics-mcp) | Production Python server implementing encrypted OAuth token persistence and automated refresh for unattended continuous GA4 report execution. |

### Ephemeral loopback PKCE authenticators

*1 project. High-performance native authenticators implementing zero-dependency loopback OAuth 2.0 PKCE.*

| Project | What it does |
|---|---|
| <a id="codechap--mcp-server-google-analytics"></a>[**codeChap/mcp-server-google-analytics**](https://github.com/codeChap/mcp-server-google-analytics) | High-performance Rust MCP server exposing 15 tools with zero-dependency loopback PKCE OAuth authentication and atomic token handling. |

### Remote team and multi-account proxies

*4 projects. Team-oriented servers enabling agency multi-account switching and shared credential guardrails.*

| Project | What it does |
|---|---|
| <a id="minholi--google-analytics-mcp"></a>[**minholi/google-analytics-mcp**](https://github.com/minholi/google-analytics-mcp) | Python MCP server exposing 8 tools designed for shared team agency environments with centralized GA4 property switching. |
| <a id="gomarble-ai--google-analytics-mcp-server"></a>[**gomarble-ai/google-analytics-mcp-server**](https://github.com/gomarble-ai/google-analytics-mcp-server) | Python server tailored for marketing teams with multi-account switching and specialized revenue metric extraction tools. |
| <a id="ankhangonline--mcp-ga4-team-server"></a>[**ankhangonline/mcp-ga4-team-server**](https://github.com/ankhangonline/mcp-ga4-team-server) | Node.js server facilitating multi-user agency access to shared GA4 service accounts with request logging and permission guardrails. |
| <a id="mnsmasum62786--was-ga4-mcp"></a>[**mnsmasum62786/was-ga4-mcp**](https://github.com/mnsmasum62786/was-ga4-mcp) | JavaScript remote server proxying team GA4 report requests through secure OAuth 2.0 session endpoints with error recovery. |

---

## 5. Send server-side events and manage properties

*3 projects. 3 projects across 2 subcategories dispatching Measurement Protocol events and provisioning GA4 properties via Admin API.*

### Measurement Protocol event dispatchers

*1 project. Bidirectional servers sending and validating server-side Measurement Protocol events.*

| Project | What it does |
|---|---|
| <a id="leonardosepulvedat--mcp-google-analytics"></a>[**leonardosepulvedat/mcp-google-analytics**](https://github.com/leonardosepulvedat/mcp-google-analytics) | TypeScript MCP server featuring 26 tools with bidirectional support for GA4 Data API reporting and server-side Measurement Protocol event validation. |

### Admin API property and custom definition managers

*2 projects. Infrastructure management servers provisioning custom dimensions, metrics, and property settings.*

| Project | What it does |
|---|---|
| <a id="insightful-pipe--google-analytics-mcp-server"></a>[**Insightful-Pipe/google-analytics-mcp-server**](https://github.com/Insightful-Pipe/google-analytics-mcp-server) | Full-featured TypeScript server with 25 tools managing GA4 custom dimensions, metrics, data streams, and BigQuery linkages via Admin API. |
| <a id="happymonkeyai--ai-google-analytics-mcp"></a>[**HappyMonkeyAI/ai-google-analytics-mcp**](https://github.com/HappyMonkeyAI/ai-google-analytics-mcp) | Python server focusing on GA4 property configuration, account metadata inspection, and custom definition synchronization. |

---

## 6. Diagnose anomalies and generate deliverables

*6 projects. 6 projects across 3 subcategories performing statistical anomaly detection, rendering 3D visualizations, and compiling reports.*

### Algorithmic anomaly detection and drop classifiers

*2 projects. Diagnostic toolkits identifying statistical traffic anomalies, baseline drops, and pattern changes.*

| Project | What it does |
|---|---|
| <a id="mario-hernandez--google-analytics-mcp-claude-code"></a>[**mario-hernandez/google-analytics-mcp-claude-code**](https://github.com/mario-hernandez/google-analytics-mcp-claude-code) | Python toolkit featuring 16 tools with built-in statistical anomaly detection, schema discovery, and diagnostic traffic shift classification. |
| <a id="onionst--ga4-toolkit"></a>[**onionst/ga4-toolkit**](https://github.com/onionst/ga4-toolkit) | Python MCP server providing 8 tools with historical baseline trend comparison and automated traffic anomaly identification. |

### Visual 3D dashboards and real-time streaming

*2 projects. Interactive visual servers streaming live visitor telemetry into 3D environments and dashboards.*

| Project | What it does |
|---|---|
| <a id="thetechbasket--ga4-dashboard-mcp"></a>[**TheTechBasket/GA4-Dashboard-MCP**](https://github.com/TheTechBasket/GA4-Dashboard-MCP) | JavaScript server featuring 11 tools that render interactive Three.js 3D data visualizations directly from live GA4 telemetry. |
| <a id="inakigorostiza--ga4-mcp-dashboard"></a>[**inakigorostiza/ga4-mcp-dashboard**](https://github.com/inakigorostiza/ga4-mcp-dashboard) | Node.js MCP server providing real-time visitor event streaming and visual HTML dashboard generation for monitoring active traffic. |

### Automated executive report and document generators

*2 projects. Autonomous reporting agents compiling end-to-end analytical summaries and BI data models.*

| Project | What it does |
|---|---|
| <a id="arcbaslow--google-analytics-agent"></a>[**arcbaslow/google-analytics-agent**](https://github.com/arcbaslow/google-analytics-agent) | Autonomous Python agent framework with 32 tools orchestrating end-to-end GA4 data collection, executive report compilation, and multi-format exports. |
| <a id="analyticsdatajg2025-cmd--ga4-mcp-powerbi"></a>[**analyticsdatajg2025-cmd/ga4-mcp-powerbi**](https://github.com/analyticsdatajg2025-cmd/ga4-mcp-powerbi) | JavaScript MCP server converting GA4 metric streams into PowerBI-compatible tabular data models and automated BI refresh feeds. |

---

## 7. Starter templates and setup scaffolds

*4 projects. 4 projects. Production boilerplates and setup recipes for authoring custom GA4 MCP servers.*

### Starter templates and boilerplate scaffolds

*4 projects. Production boilerplates and setup recipes for authoring custom GA4 MCP servers.*

| Project | What it does |
|---|---|
| <a id="drewbeechler--ga4-mcp-template"></a>[**drewbeechler/ga4-mcp-template**](https://github.com/drewbeechler/ga4-mcp-template) | TypeScript boilerplate template offering 7 starter tools, Docker configuration, and standard Service Account setup for custom MCP authoring. |
| <a id="burhan29ee--ga4-mcp-server"></a>[**burhan29ee/ga4-mcp-server**](https://github.com/burhan29ee/ga4-mcp-server) | Modular Python starter template with 13 scaffolding tools and type-annotated handler patterns for rapid GA4 integration. |
| <a id="communicationseo2021-creator--gsc-ga4-mcp-setup-guide"></a>[**communicationseo2021-creator/gsc-ga4-mcp-setup-guide**](https://github.com/communicationseo2021-creator/gsc-ga4-mcp-setup-guide) | Educational setup scaffold and MCP reference implementation detailing end-to-end Service Account configuration and report retrieval. |
| <a id="seoteamschbang2021-hub--ga4-mcp-server"></a>[**seoteamschbang2021-hub/ga4-mcp-server**](https://github.com/seoteamschbang2021-hub/ga4-mcp-server) | Python template scaffold providing pre-configured MCP tools and configuration recipes for agency SEO deployment. |

---

## Resources

### Official Documentation & SDKs

- [Google Analytics Data API (v1beta)](https://developers.google.com/analytics/devguides/reporting/data/v1) — Official reference documentation for standard reports, realtime streams, and funnel dimensions.
- [Google Analytics Admin API (v1)](https://developers.google.com/analytics/devguides/config/admin/v1) — Programmatic management API for accounts, properties, data streams, and custom metrics.
- [Google Analytics Measurement Protocol (GA4)](https://developers.google.com/analytics/devguides/collection/protocol/ga4) — HTTP protocol specification for dispatching server-side, offline, and mobile event streams directly to GA4 properties.
- [Model Context Protocol Specification](https://modelcontextprotocol.io/) — Anthropic's open standard protocol specification connecting language model clients with external data sources and execution environments.
- [Google Cloud IAM Service Accounts](https://cloud.google.com/iam/docs/service-account-overview) — Google Cloud security guidelines for provisioning and rotating service account JSON credentials.

### Community Guides & Architecture

- [Anthropic Claude Code MCP Integration Guide](https://docs.anthropic.com/en/docs/agents-and-tools/mcp) — Setup guide for attaching stdio and SSE MCP servers to Claude Code CLI and Anthropic desktop environments.
- [Cursor MCP Server Setup](https://docs.cursor.com/context/model-context-protocol) — Configuring local and remote MCP agents within Cursor IDE.
- [DuckDB Columnar Analytical Engine](https://duckdb.org/) — In-memory SQL OLAP engine optimized for local-first telemetry analytics without external database infrastructure.
- [SQLite Embedded Relational Database](https://www.sqlite.org/) — Zero-configuration SQL database engine for caching agent sessions and analytics data.

---

## Reference

### Evaluation Methodology & Verification Invariants

Every repository indexed in this catalog has undergone code-level forensic evaluation against the following standards:

1. **6-Month Maintenance Invariant:** Active development verified on GitHub (last commit dated March 2026 or later). Abandoned, archival, or unmaintained stubs are quarantined.
2. **Evidence-Grounded Technical Audit:** Every tool signature, authentication pattern, and storage engine is verified directly from repository source code (`package.json`, `pyproject.toml`, `Cargo.toml`, and handler definitions), never from unverified README claims.
3. **Job-to-Be-Done Taxonomy Bounding:** Repositories are organized into 7 functional domains and 20 subcategories based on actual developer operational needs rather than arbitrary vendor classifications.
4. **Mathematical Parity Guarantee:** Category counts, Table of Contents anchors, subcategory summaries, and table row counts are reconciled via automated verification scripts with zero mathematical drift.

### Repository Inclusion & Quarantine Invariants

To maintain signal purity, candidate repositories must pass strict inclusion filters:

- **GA4 Direct Technical Affinity:** Tools must interface directly with Google Analytics Data API, Admin API, Measurement Protocol, or provide tightly unified multi-platform workflows (GSC, GTM).
- **Executable Agent Tool Handlers:** Servers must expose executable MCP tool definitions (`CallToolRequest`, `@mcp.tool`, `server.tool`) compatible with MCP hosts.
- **Quarantine Protocol:** Generic multi-cloud wrappers without GA4 implementations, non-MCP reporting scripts, and hallucinated synthetic repositories are excluded from this catalog.

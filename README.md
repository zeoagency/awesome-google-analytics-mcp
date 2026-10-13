# Awesome Google Analytics MCP [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> Discover what Google Analytics 4 MCP tools actually do, with complete tool references.

**35 MCP servers · 423 GA4 tool registrations.** [Find a tool by name](docs/tool-index.md) or browse the tasks below. Server pages include every tool, full descriptions and complete input schemas.

Grouped by implemented GA4 behavior, with one primary placement per server. The [tool index](docs/tool-index.md) covers all 649 registrations, including other services, server support and optional tools. Counts describe reviewed source, not live availability. [Source review and decisions](docs/verification.md).

## Contents

1. [Audit measurement and reporting (3)](#1-audit-measurement-and-reporting)
2. [Configure properties and send events (9)](#2-configure-properties-and-send-events)
3. [Connect GA4 with search data (4)](#3-connect-ga4-with-search-data)
4. [Build funnels and multidimensional reports (4)](#4-build-funnels-and-multidimensional-reports)
5. [Analyze GA4 reports with SQL (1)](#5-analyze-ga4-reports-with-sql)
6. [Query traffic and realtime reports (14)](#6-query-traffic-and-realtime-reports)
7. [CLI tools (5)](#7-cli-tools)
8. [SDKs (16)](#8-sdks)

## 1. Audit measurement and reporting

*3 servers. Investigate event health, ecommerce coverage, configuration and cross-property differences.*

| MCP server | What its tools do | Tool reference |
| --- | --- | --- |
| [**arcbaslow/google-analytics-agent**](https://github.com/arcbaslow/google-analytics-agent) | Audit measurement, inspect consent signals and event coverage, and compare reporting periods. [`audit`](docs/mcps/arcbaslow--google-analytics-agent.md#audit), [`consent_diagnostics`](docs/mcps/arcbaslow--google-analytics-agent.md#consent_diagnostics), [`funnel`](docs/mcps/arcbaslow--google-analytics-agent.md#funnel). | [44 GA4 / 47 total](docs/mcps/arcbaslow--google-analytics-agent.md) |
| [**CreativeMetrics/gtm-ga4-mcp**](https://github.com/CreativeMetrics/gtm-ga4-mcp) | Check tag health against GA4 event counts, compare properties and duplicate custom dimensions. [`gtm_check_tag_health`](docs/mcps/creativemetrics--gtm-ga4-mcp.md#gtm_check_tag_health), [`ga4_compare_properties`](docs/mcps/creativemetrics--gtm-ga4-mcp.md#ga4_compare_properties), [`ga4_duplicate_custom_dimensions`](docs/mcps/creativemetrics--gtm-ga4-mcp.md#ga4_duplicate_custom_dimensions). | [14 GA4 / 47 total](docs/mcps/creativemetrics--gtm-ga4-mcp.md) |
| [**get-mcp-ads/google-analytics-mcp-server**](https://github.com/get-mcp-ads/google-analytics-mcp-server) | Inspect ecommerce, audiences and export configuration; validate queries and inspect quota state. [`ga4_get_ecommerce_diagnostics`](docs/mcps/get-mcp-ads--google-analytics-mcp-server.md#ga4_get_ecommerce_diagnostics), [`ga4_get_bigquery_export_diagnostics`](docs/mcps/get-mcp-ads--google-analytics-mcp-server.md#ga4_get_bigquery_export_diagnostics), [`ga4_validate_query`](docs/mcps/get-mcp-ads--google-analytics-mcp-server.md#ga4_validate_query). | [27 tools](docs/mcps/get-mcp-ads--google-analytics-mcp-server.md) |

## 2. Configure properties and send events

*9 servers. Create or change GA4 configuration, install collection code, or send Measurement Protocol events.*

| MCP server | What its tools do | Tool reference |
| --- | --- | --- |
| [**burhan29ee/ga4-mcp-server**](https://github.com/burhan29ee/ga4-mcp-server) | Create definitions, key events and audiences; manage Measurement Protocol secrets and send events. [`create_event_audience`](docs/mcps/burhan29ee--ga4-mcp-server.md#create_event_audience), [`create_measurement_protocol_secret`](docs/mcps/burhan29ee--ga4-mcp-server.md#create_measurement_protocol_secret), [`send_ga4_event`](docs/mcps/burhan29ee--ga4-mcp-server.md#send_ga4_event). | [19 tools](docs/mcps/burhan29ee--ga4-mcp-server.md) |
| [**codeChap/mcp-server-google-analytics**](https://github.com/codeChap/mcp-server-google-analytics) | Manage custom dimensions and key events, and add dated property annotations. [`create_custom_dimension`](docs/mcps/codechap--mcp-server-google-analytics.md#create_custom_dimension), [`create_key_event`](docs/mcps/codechap--mcp-server-google-analytics.md#create_key_event), [`create_property_annotation`](docs/mcps/codechap--mcp-server-google-analytics.md#create_property_annotation). | [14 GA4 / 15 total](docs/mcps/codechap--mcp-server-google-analytics.md) |
| [**freema/mcp-google-marketing**](https://github.com/freema/mcp-google-marketing) | Create and update properties and streams, manage conversion events, and query reports. [`ga4_create_property`](docs/mcps/freema--mcp-google-marketing.md#ga4_create_property), [`ga4_create_web_stream`](docs/mcps/freema--mcp-google-marketing.md#ga4_create_web_stream), [`ga4_create_custom_metric`](docs/mcps/freema--mcp-google-marketing.md#ga4_create_custom_metric). | [22 GA4 / 35 total](docs/mcps/freema--mcp-google-marketing.md) |
| [**HappyMonkeyAI/ai-google-analytics-mcp**](https://github.com/HappyMonkeyAI/ai-google-analytics-mcp) | Provision properties and web streams, then install gtag or scaffold Next.js tracking in local projects. [`provision_project_ga4_setup`](docs/mcps/happymonkeyai--ai-google-analytics-mcp.md#provision_project_ga4_setup), [`scaffold_ga4_nextjs_tracking`](docs/mcps/happymonkeyai--ai-google-analytics-mcp.md#scaffold_ga4_nextjs_tracking). | [12 GA4 / 18 total](docs/mcps/happymonkeyai--ai-google-analytics-mcp.md) |
| [**kb223/gtm-ga4-mcp**](https://github.com/kb223/gtm-ga4-mcp) | Create, update and delete GA4 entities through permission tiers, dry-run previews and confirmation tokens. [`ga4_admin_create`](docs/mcps/kb223--gtm-ga4-mcp.md#ga4_admin_create), [`ga4_admin_update`](docs/mcps/kb223--gtm-ga4-mcp.md#ga4_admin_update), [`ga4_admin_delete`](docs/mcps/kb223--gtm-ga4-mcp.md#ga4_admin_delete). | [9 GA4 / 16 total](docs/mcps/kb223--gtm-ga4-mcp.md) |
| [**leonardosepulvedat/mcp-google-analytics**](https://github.com/leonardosepulvedat/mcp-google-analytics) | Send and debug-validate custom or ecommerce events; also run reporting and native funnel queries. [`ga_send_purchase`](docs/mcps/leonardosepulvedat--mcp-google-analytics.md#ga_send_purchase), [`ga_send_refund`](docs/mcps/leonardosepulvedat--mcp-google-analytics.md#ga_send_refund), [`ga_validate_event`](docs/mcps/leonardosepulvedat--mcp-google-analytics.md#ga_validate_event). | [26 tools](docs/mcps/leonardosepulvedat--mcp-google-analytics.md) |
| [**mharnett/mcp-ga4**](https://github.com/mharnett/mcp-ga4) | Register custom dimensions when writes are enabled; inspect definitions and streams and run reports. [`ga4_create_custom_dimension`](docs/mcps/mharnett--mcp-ga4.md#ga4_create_custom_dimension), [`ga4_list_custom_metrics`](docs/mcps/mharnett--mcp-ga4.md#ga4_list_custom_metrics). | [6 GA4 / 9 total](docs/mcps/mharnett--mcp-ga4.md) |
| [**mnsmasum62786/was-ga4-mcp**](https://github.com/mnsmasum62786/was-ga4-mcp) | Update properties, create definitions and BigQuery links, or call native GA4 endpoints with an explicit method. [`ga4_create_bigquery_link`](docs/mcps/mnsmasum62786--was-ga4-mcp.md#ga4_create_bigquery_link), [`ga4_update_property`](docs/mcps/mnsmasum62786--was-ga4-mcp.md#ga4_update_property), [`ga4_universal_call`](docs/mcps/mnsmasum62786--was-ga4-mcp.md#ga4_universal_call). | [31 tools](docs/mcps/mnsmasum62786--was-ga4-mcp.md) |
| [**stufently/google-webtools-mcp**](https://github.com/stufently/google-webtools-mcp) | Provision GA4 properties and web streams, retrieve measurement IDs and query historical or realtime reports. [`ga4_create_property`](docs/mcps/stufently--google-webtools-mcp.md#ga4_create_property), [`ga4_create_data_stream`](docs/mcps/stufently--google-webtools-mcp.md#ga4_create_data_stream). | [10 GA4 / 39 total](docs/mcps/stufently--google-webtools-mcp.md) |

## 3. Connect GA4 with search data

*4 servers. Read GA4 alongside Search Console, or explicitly join landing-page acquisition and engagement.*

| MCP server | What its tools do | Tool reference |
| --- | --- | --- |
| [**delaren47/gsc-ga4-mcp**](https://github.com/delaren47/gsc-ga4-mcp) | Join Search Console clicks with GA4 landing-page engagement and identify content refresh opportunities. [`compare_gsc_ga4_pages`](docs/mcps/delaren47--gsc-ga4-mcp.md#compare_gsc_ga4_pages), [`content_refresh_candidates`](docs/mcps/delaren47--gsc-ga4-mcp.md#content_refresh_candidates), [`find_pages_with_clicks_but_low_engagement`](docs/mcps/delaren47--gsc-ga4-mcp.md#find_pages_with_clicks_but_low_engagement). | [11 GA4 / 20 total](docs/mcps/delaren47--gsc-ga4-mcp.md) |
| [**fenjo26/OpenGSC**](https://github.com/fenjo26/OpenGSC) | Compare sessions, engagement, key events and revenue for a linked GA4 property; one GA4 tool within a larger search toolkit. [`get_analytics`](docs/mcps/fenjo26--opengsc.md#get_analytics). | [1 GA4 / 95 total](docs/mcps/fenjo26--opengsc.md) |
| [**Newsstate/ga4-mcp**](https://github.com/Newsstate/ga4-mcp) | Query GA4 traffic, audiences and events alongside separate Search Console query and page reports. [`get_traffic_sources`](docs/mcps/newsstate--ga4-mcp.md#get_traffic_sources), [`get_audience_overview`](docs/mcps/newsstate--ga4-mcp.md#get_audience_overview). | [7 GA4 / 11 total](docs/mcps/newsstate--ga4-mcp.md) |
| [**rablab-mtl/mcp-ga4-gsc**](https://github.com/rablab-mtl/mcp-ga4-gsc) | Run GA4 reports, pivots and batches alongside separate Search Console and URL inspection tools. [`ga4_run_pivot_report`](docs/mcps/rablab-mtl--mcp-ga4-gsc.md#ga4_run_pivot_report), [`ga4_batch_run_reports`](docs/mcps/rablab-mtl--mcp-ga4-gsc.md#ga4_batch_run_reports). | [17 GA4 / 22 total](docs/mcps/rablab-mtl--mcp-ga4-gsc.md) |

## 4. Build funnels and multidimensional reports

*4 servers. Use native funnel APIs, pivot tables, batches or conversion-specific reports.*

| MCP server | What its tools do | Tool reference |
| --- | --- | --- |
| [**googleanalytics/google-analytics-mcp**](https://github.com/googleanalytics/google-analytics-mcp) | Run native funnels, conversion reports and realtime queries; inspect custom definitions and annotations. [`run_funnel_report`](docs/mcps/googleanalytics--google-analytics-mcp.md#run_funnel_report), [`run_conversions_report`](docs/mcps/googleanalytics--google-analytics-mcp.md#run_conversions_report). | [9 tools](docs/mcps/googleanalytics--google-analytics-mcp.md) |
| [**dhawalshah/google-analytics-mcp**](https://github.com/dhawalshah/google-analytics-mcp) | Build native event funnels, inspect realtime country/device activity and run custom reports. [`run_funnel_report`](docs/mcps/dhawalshah--google-analytics-mcp.md#run_funnel_report), [`get_realtime_users`](docs/mcps/dhawalshah--google-analytics-mcp.md#get_realtime_users). | [10 tools](docs/mcps/dhawalshah--google-analytics-mcp.md) |
| [**scalably-io/ga4-mcp**](https://github.com/scalably-io/ga4-mcp) | Run native funnels, pivot and batch reports, preflight compatibility and inspect access reports. [`ga4_run_funnel_report`](docs/mcps/scalably-io--ga4-mcp.md#ga4_run_funnel_report), [`ga4_run_pivot_report`](docs/mcps/scalably-io--ga4-mcp.md#ga4_run_pivot_report), [`ga4_run_access_report`](docs/mcps/scalably-io--ga4-mcp.md#ga4_run_access_report). | [17 tools](docs/mcps/scalably-io--ga4-mcp.md) |
| [**TheTechBasket/GA4-Dashboard-MCP**](https://github.com/TheTechBasket/GA4-Dashboard-MCP) | Run native funnels and filtered reports with quota guards and caching; query realtime activity. [`run_funnel_report`](docs/mcps/thetechbasket--ga4-dashboard-mcp.md#run_funnel_report), [`run_report`](docs/mcps/thetechbasket--ga4-dashboard-mcp.md#run_report). | [7 GA4 / 11 total](docs/mcps/thetechbasket--ga4-dashboard-mcp.md) |

## 5. Analyze GA4 reports with SQL

*1 server. Materialize GA4 reports locally and investigate changes across imported tables.*

| MCP server | What its tools do | Tool reference |
| --- | --- | --- |
| [**sednalabs/ga4-mcp**](https://github.com/sednalabs/ga4-mcp) | Ingest reports into DuckDB, query them with SQL and investigate release regressions or landing-parameter shifts; scratchpad profile required. [`scratchpad_ingest_report`](docs/mcps/sednalabs--ga4-mcp.md#scratchpad_ingest_report), [`scratchpad_query`](docs/mcps/sednalabs--ga4-mcp.md#scratchpad_query), [`scratchpad_release_regression_report`](docs/mcps/sednalabs--ga4-mcp.md#scratchpad_release_regression_report). | [25 GA4 / 35 total](docs/mcps/sednalabs--ga4-mcp.md) |

## 6. Query traffic and realtime reports

*14 servers. Discover fields and properties, explore traffic, compare periods or query active users.*

| MCP server | What its tools do | Tool reference |
| --- | --- | --- |
| [**administrator-prog/ga4-mcp**](https://github.com/administrator-prog/ga4-mcp) | Compare periods and investigate organic traffic, landing pages, device changes, events and site searches. [`analyse_conversion_drop`](docs/mcps/administrator-prog--ga4-mcp.md#analyse_conversion_drop), [`analyse_events_by_page`](docs/mcps/administrator-prog--ga4-mcp.md#analyse_events_by_page), [`analyse_site_search`](docs/mcps/administrator-prog--ga4-mcp.md#analyse_site_search). | [11 tools](docs/mcps/administrator-prog--ga4-mcp.md) |
| [**ankhangonline/mcp-ga4-team-server**](https://github.com/ankhangonline/mcp-ga4-team-server) | Run one configurable historical report with filters, ordering, pagination and a team-specific property mapping. [`get_team_ga4_report`](docs/mcps/ankhangonline--mcp-ga4-team-server.md#get_team_ga4_report). | [1 tool](docs/mcps/ankhangonline--mcp-ga4-team-server.md) |
| [**buyte-io/GA4-MCP-Server**](https://github.com/buyte-io/GA4-MCP-Server) | Discover accounts, properties and metadata, then run filtered historical reports through the source entrypoints. [`ga4_getMetadata`](docs/mcps/buyte-io--ga4-mcp-server.md#ga4_getmetadata), [`ga4_runReport`](docs/mcps/buyte-io--ga4-mcp-server.md#ga4_runreport). | [4 tools](docs/mcps/buyte-io--ga4-mcp-server.md) |
| [**Callince/ga4-mcp-server**](https://github.com/Callince/ga4-mcp-server) | Discover properties and metadata and run custom historical or realtime reports. [`run_report`](docs/mcps/callince--ga4-mcp-server.md#run_report), [`run_realtime_report`](docs/mcps/callince--ga4-mcp-server.md#run_realtime_report). | [4 tools](docs/mcps/callince--ga4-mcp-server.md) |
| [**CUTolu2021/ga4-mcp-server**](https://github.com/CUTolu2021/ga4-mcp-server) | Query page views, events and user behavior with historical report presets and paginated custom reports. [`getUserBehavior`](docs/mcps/cutolu2021--ga4-mcp-server.md#getuserbehavior), [`getEvents`](docs/mcps/cutolu2021--ga4-mcp-server.md#getevents). | [6 tools](docs/mcps/cutolu2021--ga4-mcp-server.md) |
| [**devli13/mcp-ga4**](https://github.com/devli13/mcp-ga4) | Query daily users, top events, cohort retention and realtime data for a configured property. [`ga4_retention`](docs/mcps/devli13--mcp-ga4.md#ga4_retention), [`ga4_daily_users`](docs/mcps/devli13--mcp-ga4.md#ga4_daily_users). | [5 GA4 / 6 total](docs/mcps/devli13--mcp-ga4.md) |
| [**ESGEE-0562/google-analytics-mcp**](https://github.com/ESGEE-0562/google-analytics-mcp) | Read account/property metadata, annotations and custom definitions, then query historical or realtime reports. [`run_report`](docs/mcps/esgee-0562--google-analytics-mcp.md#run_report), [`run_realtime_report`](docs/mcps/esgee-0562--google-analytics-mcp.md#run_realtime_report). | [7 tools](docs/mcps/esgee-0562--google-analytics-mcp.md) |
| [**gomarble-ai/google-analytics-mcp-server**](https://github.com/gomarble-ai/google-analytics-mcp-server) | Query page views, active users, events, traffic sources and devices, or supply a custom filtered report. [`get_device_metrics`](docs/mcps/gomarble-ai--google-analytics-mcp-server.md#get_device_metrics), [`run_report`](docs/mcps/gomarble-ai--google-analytics-mcp-server.md#run_report). | [7 tools](docs/mcps/gomarble-ai--google-analytics-mcp-server.md) |
| [**gviollaz/iita-ga4-mcp**](https://github.com/gviollaz/iita-ga4-mcp) | Query traffic sources, top and landing pages, daily trends and device/geography breakdowns; also request realtime reports. [`ga4_daily_trend`](docs/mcps/gviollaz--iita-ga4-mcp.md#ga4_daily_trend), [`ga4_device_geo`](docs/mcps/gviollaz--iita-ga4-mcp.md#ga4_device_geo). | [7 tools](docs/mcps/gviollaz--iita-ga4-mcp.md) |
| [**K41R0N/ga4-mcp**](https://github.com/K41R0N/ga4-mcp) | Discover properties and run historical reports using the specified teammate’s Google credentials. [`list_properties`](docs/mcps/k41r0n--ga4-mcp.md#list_properties), [`run_report`](docs/mcps/k41r0n--ga4-mcp.md#run_report). | [2 tools](docs/mcps/k41r0n--ga4-mcp.md) |
| [**luminarylane/ga4-mcp**](https://github.com/luminarylane/ga4-mcp) | Query top pages, traffic sources, conversion events and realtime activity, or compare two reporting periods. [`ga4_compare_periods`](docs/mcps/luminarylane--ga4-mcp.md#ga4_compare_periods), [`ga4_get_realtime`](docs/mcps/luminarylane--ga4-mcp.md#ga4_get_realtime). | [7 tools](docs/mcps/luminarylane--ga4-mcp.md) |
| [**minholi/google-analytics-mcp**](https://github.com/minholi/google-analytics-mcp) | Explore traffic, geography, devices, events and conversion presets with nested options and JSON or Markdown output. [`google_analytics_get_geographic_performance`](docs/mcps/minholi--google-analytics-mcp.md#google_analytics_get_geographic_performance), [`google_analytics_get_conversions`](docs/mcps/minholi--google-analytics-mcp.md#google_analytics_get_conversions). | [8 tools](docs/mcps/minholi--google-analytics-mcp.md) |
| [**onionst/ga4-toolkit**](https://github.com/onionst/ga4-toolkit) | Query acquisition, page and event presets, or request custom historical and realtime reports with quota metadata. [`ga4_acquisition`](docs/mcps/onionst--ga4-toolkit.md#ga4_acquisition), [`ga4_realtime`](docs/mcps/onionst--ga4-toolkit.md#ga4_realtime). | [8 tools](docs/mcps/onionst--ga4-toolkit.md) |
| [**surendranb/google-analytics-mcp**](https://github.com/surendranb/google-analytics-mcp) | Search the configured property’s cached dimension/metric schema, then query filtered historical data with volume checks. [`search_schema`](docs/mcps/surendranb--google-analytics-mcp.md#search_schema), [`get_ga4_data`](docs/mcps/surendranb--google-analytics-mcp.md#get_ga4_data). | [8 GA4 / 12 total](docs/mcps/surendranb--google-analytics-mcp.md) |

## 7. CLI tools

| Project | What it does |
| --- | --- |
| [**Bin-Huang/google-analytics-cli**](https://github.com/Bin-Huang/google-analytics-cli) | Runs GA4 standard, pivot, batch and realtime reports from a TypeScript CLI using the Data API. Reads Admin configuration and exports audiences with JSON output and named credential profiles. |
| [**Hasim-cim/ga4-mcp**](https://github.com/Hasim-cim/ga4-mcp) | Runs GA4 reports, realtime queries, and property inspection from a Python command-line tool. Provides page, acquisition, demographic, and custom-report presets using Application Default Credentials. |
| [**kasdimg/analytics-cli**](https://github.com/kasdimg/analytics-cli) | Queries GA4 reports and Search Console analytics through a JavaScript CLI. Returns summary, page, device and custom-query results using shared service-account credentials. |
| [**nyosegawa/gacli**](https://github.com/nyosegawa/gacli) | Queries GA4 summaries, pages, realtime activity and custom reports through a Python CLI. Stores separate OAuth profiles and supports filtered queries with selectable output formats. |
| [**sulimanbenhalim/ga-cli**](https://github.com/sulimanbenhalim/ga-cli) | Creates, updates and deletes GA4 properties and data streams through a Python CLI using the Admin API. Lists accounts and supports local credential configuration. |

## 8. SDKs

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

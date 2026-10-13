# fenjo26/OpenGSC

[Catalog](../../README.md) · [All tool names](../tool-index.md) · [Upstream](https://github.com/fenjo26/OpenGSC) · [JSON](../../data/mcps/fenjo26--opengsc.json)

**95 tools:** 1 GA4, 94 other-service or server-support tools. Reviewed source: [`3805be32a8d3`](https://github.com/fenjo26/OpenGSC/tree/3805be32a8d3a33d32e38724928b92946ce6c2a4).

Descriptions and parameter schemas come from the registered source definitions. Generated schemas are reconstructed from annotations or validators; live `tools/list` and authenticated API calls were not run. Loose objects remain loose.

<details>
<summary>Exposure and compatibility notes</summary>

- Source review only; no tools/list or live requests and no upstream code executed. Git HEAD matches supplied revision.
- All 95 tools are advertised unconditionally; tools/call enforces role permissions according to paid cost or explicit readOnly:false. Tokens resolve to workspace-owner data.
- GA4 analytics is live; most GSC performance and other dataset tools read the local SQLite/Prisma cache. Live GSC query and URL Inspection are separate quota tools.
- Imported contour arrays are populated at this revision despite stale comments describing them as empty stubs.
- Existing Google OAuth account, linked GA4 property and Analytics read scope/access are needed for get_analytics; application database/migrations and provider credentials are needed for respective surfaces. No installation or authentication was tested.
- Several registrations default to read-only annotations while performing writes, and fit_meta paid mode is still labeled local. Schemas are advertised verbatim; prose constraints are not synthesized into schema constraints.

</details>

## Tools

| Tool | Scope | Effect |
| --- | --- | --- |
| [`list_sites`](#list_sites) | Server support | read |
| [`get_search_performance`](#get_search_performance) | Other service | read |
| [`get_striking_distance`](#get_striking_distance) | Other service | read |
| [`get_cannibalization`](#get_cannibalization) | Other service | read |
| [`get_rank_tracker`](#get_rank_tracker) | Other service | read |
| [`get_aeo_visibility`](#get_aeo_visibility) | Other service | read |
| [`get_backlinks`](#get_backlinks) | Other service | read |
| [`get_link_mentions`](#get_link_mentions) | Other service | read |
| [`get_site_health`](#get_site_health) | Other service | read |
| [`get_indexing_status`](#get_indexing_status) | Other service | read |
| [`get_site_audit`](#get_site_audit) | Other service | read |
| [`compare_periods`](#compare_periods) | Other service | read |
| [`query_gsc_live`](#query_gsc_live) | Other service | read |
| [`inspect_url`](#inspect_url) | Other service | mixed |
| [`get_capabilities`](#get_capabilities) | Server support | read |
| [`execute_sql_query`](#execute_sql_query) | Server support | read |
| [`get_content_decay`](#get_content_decay) | Other service | read |
| [`get_ctr_benchmark`](#get_ctr_benchmark) | Other service | read |
| [`get_content_groups`](#get_content_groups) | Other service | read |
| [`get_rank_history`](#get_rank_history) | Other service | read |
| [`get_geo_audits`](#get_geo_audits) | Other service | read |
| [`get_generations`](#get_generations) | Other service | read |
| [`get_engine_performance`](#get_engine_performance) | Other service | read |
| [`get_analytics`](#get_analytics) | GA4 | read |
| [`get_clarity`](#get_clarity) | Other service | read |
| [`get_indexer_stats`](#get_indexer_stats) | Other service | read |
| [`get_digests`](#get_digests) | Other service | read |
| [`get_alerts`](#get_alerts) | Other service | read |
| [`get_keyword_metrics`](#get_keyword_metrics) | Other service | read |
| [`get_domain_metrics`](#get_domain_metrics) | Other service | read |
| [`get_yandex_ai_answers`](#get_yandex_ai_answers) | Other service | read |
| [`get_backlink_profile`](#get_backlink_profile) | Other service | read |
| [`get_competitor_gap`](#get_competitor_gap) | Other service | read |
| [`get_domain_traffic`](#get_domain_traffic) | Other service | read |
| [`get_ads_intel`](#get_ads_intel) | Other service | read |
| [`get_keyword_demand`](#get_keyword_demand) | Other service | read |
| [`research_keywords`](#research_keywords) | Other service | mixed |
| [`get_optimization_brief`](#get_optimization_brief) | Other service | read |
| [`fetch_page_content`](#fetch_page_content) | Other service | read |
| [`analyze_text`](#analyze_text) | Other service | local |
| [`start_rewrite_job`](#start_rewrite_job) | Other service | mixed |
| [`start_generation_job`](#start_generation_job) | Other service | mixed |
| [`get_generation_job`](#get_generation_job) | Other service | write |
| [`list_outreach_prospects`](#list_outreach_prospects) | Other service | read |
| [`save_outreach_prospect`](#save_outreach_prospect) | Other service | write |
| [`update_outreach_prospect`](#update_outreach_prospect) | Other service | write |
| [`create_outreach_campaign`](#create_outreach_campaign) | Other service | write |
| [`get_source_audit`](#get_source_audit) | Other service | read |
| [`drops_list`](#drops_list) | Other service | read |
| [`drops_ingest`](#drops_ingest) | Other service | write |
| [`drops_prefilter`](#drops_prefilter) | Other service | mixed |
| [`drops_check`](#drops_check) | Other service | mixed |
| [`drops_enrich_wayback`](#drops_enrich_wayback) | Other service | mixed |
| [`drops_enrich_dr`](#drops_enrich_dr) | Other service | mixed |
| [`drops_enrich_refdomains`](#drops_enrich_refdomains) | Other service | mixed |
| [`drops_enrich_tf`](#drops_enrich_tf) | Other service | mixed |
| [`drops_groups`](#drops_groups) | Other service | write |
| [`drops_dr_history`](#drops_dr_history) | Other service | mixed |
| [`drops_history_ai`](#drops_history_ai) | Other service | mixed |
| [`drops_toxicity`](#drops_toxicity) | Other service | mixed |
| [`glue_plan`](#glue_plan) | Other service | local |
| [`glue_check`](#glue_check) | Other service | read |
| [`drops_watch`](#drops_watch) | Other service | write |
| [`serpmon_projects`](#serpmon_projects) | Other service | read |
| [`serpmon_market`](#serpmon_market) | Other service | read |
| [`serpmon_keyword_history`](#serpmon_keyword_history) | Other service | read |
| [`serpmon_storms`](#serpmon_storms) | Other service | read |
| [`serpmon_domains`](#serpmon_domains) | Other service | read |
| [`serpmon_run`](#serpmon_run) | Other service | mixed |
| [`fit_meta`](#fit_meta) | Other service | local |
| [`get_uptime`](#get_uptime) | Other service | read |
| [`get_index_coverage`](#get_index_coverage) | Other service | read |
| [`get_brand_mentions`](#get_brand_mentions) | Other service | read |
| [`get_ai_share_of_voice`](#get_ai_share_of_voice) | Other service | read |
| [`get_footprints`](#get_footprints) | Other service | read |
| [`get_backlink_toxicity`](#get_backlink_toxicity) | Other service | read |
| [`get_disavow_file`](#get_disavow_file) | Other service | read |
| [`get_local_profile`](#get_local_profile) | Other service | read |
| [`check_nap`](#check_nap) | Other service | read |
| [`local_grid_scans`](#local_grid_scans) | Other service | read |
| [`local_grid_scan_run`](#local_grid_scan_run) | Other service | mixed |
| [`local_grid_presets`](#local_grid_presets) | Other service | read |
| [`local_grid_preset_create`](#local_grid_preset_create) | Other service | write |
| [`local_grid_preset_delete`](#local_grid_preset_delete) | Other service | write |
| [`local_grid_preset_run`](#local_grid_preset_run) | Other service | mixed |
| [`get_trends`](#get_trends) | Other service | read |
| [`check_plagiarism`](#check_plagiarism) | Other service | mixed |
| [`serp_index_check`](#serp_index_check) | Other service | mixed |
| [`list_reports`](#list_reports) | Other service | read |
| [`list_leads`](#list_leads) | Other service | read |
| [`get_site_context`](#get_site_context) | Server support | read |
| [`update_site_context`](#update_site_context) | Server support | write |
| [`publish_list_connections`](#publish_list_connections) | Other service | read |
| [`publish_post`](#publish_post) | Other service | mixed |
| [`publish_list_posts`](#publish_list_posts) | Other service | read |

## list_sites

Read the owner’s connected Site rows with identifiers, tags and sync metadata.

<details>
<summary>Full registered description</summary>

```text
List every site connected to this OpenGSC instance (all Google accounts), with tags and last-sync info. Call this first to discover what data is available and to get exact site identifiers for the other tools.
```

</details>

No named input parameters are declared.

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {}
}
```

</details>

Source: [src/lib/mcp/tools.ts:77](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/tools.ts#L77-L94) · [src/lib/mcp/shared.ts:1](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/shared.ts#L1-L373).

## get_search_performance

Aggregate locally synced GSC DailyMetric rows by the requested grouping and period.

<details>
<summary>Full registered description</summary>

```text
Google Search Console performance for one site from the local metrics store: totals (clicks, impressions, CTR, avg position) plus the top rows grouped by query or page over a date window. Use dimension=query for keyword analysis, dimension=page to find top/weak pages. Pass `page` to see which queries drive traffic to ONE specific page.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `site` | Yes | string | Not declared |
| `days` | No | number | Not declared |
| `dimension` | No | string | Not declared |
| `page` | No | string | Not declared |
| `limit` | No | number | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "site": {
      "type": "string",
      "description": "The site — a domain (example.com), GSC property (sc-domain:example.com), or a site id from list_sites"
    },
    "days": {
      "type": "number",
      "description": "Lookback window in days (default 28, max 480)"
    },
    "dimension": {
      "type": "string",
      "enum": [
        "query",
        "page"
      ],
      "description": "Group rows by search query (default) or by page URL"
    },
    "page": {
      "type": "string",
      "description": "Optional: restrict to one page — full URL or path substring (e.g. /pricing). Combine with dimension=query to see that page's queries."
    },
    "limit": {
      "type": "number",
      "description": "Max rows to return (default 50, max 500)"
    }
  },
  "required": [
    "site"
  ]
}
```

</details>

Source: [src/lib/mcp/tools.ts:96](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/tools.ts#L96-L152) · [src/lib/mcp/shared.ts:1](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/shared.ts#L1-L373).

## get_striking_distance

Resolve one site or the portfolio and run findStriking over locally synced search performance.

<details>
<summary>Full registered description</summary>

```text
Striking-distance keywords: query + page pairs ranking just off the top (default positions 4–20) with real impression volume — the fastest ranking wins. Covers one site or the whole portfolio (site="all"); every pair of every site is considered. Sorted by estGainClicks: the extra clicks the pair would get at position 3 with today's impressions (benchmark CTR) — for ordering, not a forecast. Data is the 90-day query+page total from the last Search Console sync; `window` gives its dates (there is no shorter period to choose).
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `site` | No | string | Not declared |
| `positionFrom` | No | number | Not declared |
| `positionTo` | No | number | Not declared |
| `minImpressions` | No | number | Not declared |
| `sort` | No | string | Not declared |
| `limit` | No | number | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "site": {
      "type": "string",
      "description": "The site — a domain, GSC property, or site id from list_sites. Pass \"all\" for the whole portfolio."
    },
    "positionFrom": {
      "type": "number",
      "description": "Lower bound of the position band (default 4)"
    },
    "positionTo": {
      "type": "number",
      "description": "Upper bound of the position band, inclusive of the whole position (default 20 = up to 20.9)"
    },
    "minImpressions": {
      "type": "number",
      "description": "Minimum impressions over the 90 days (default 10)"
    },
    "sort": {
      "type": "string",
      "enum": [
        "gain",
        "impressions"
      ],
      "description": "gain (default) or impressions"
    },
    "limit": {
      "type": "number",
      "description": "Max rows (default 50, max 500)"
    }
  }
}
```

</details>

Source: [src/lib/mcp/tools.ts:154](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/tools.ts#L154-L202) · [src/lib/mcp/shared.ts:1](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/shared.ts#L1-L373).

## get_cannibalization

Resolve sites and run findCannibalization or findRelatedIntent over stored search query/page data.

<details>
<summary>Full registered description</summary>

```text
Cannibalization for one site or the portfolio (site="all"). mode=exact (default) returns queries where two or more of a site's URLs each take ≥10% of the impressions within 20 positions of each other (branded queries skipped); isTrue marks pairs whose pages' own top queries overlap. mode=related deterministically finds different query wordings with similar intent and conflicting ranking URLs, with confidence, page roles, winner changes (flipFlops, from per-day data of the last 28 days — see dailyWindow; null until the instance has synced it) and review-only recommendations. Local: no LLM, live SERP or paid call, never changes pages/canonicals/redirects. Volumes are the 90-day query+page total from the last sync; `window` gives the dates.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `site` | No | string | Not declared |
| `mode` | No | string | Not declared |
| `minImpressions` | No | number | Not declared |
| `limit` | No | number | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "site": {
      "type": "string",
      "description": "The site — a domain, GSC property, or site id from list_sites. Pass \"all\" for the whole portfolio."
    },
    "mode": {
      "type": "string",
      "enum": [
        "exact",
        "related"
      ],
      "description": "exact (default) or related intent conflicts"
    },
    "minImpressions": {
      "type": "number",
      "description": "Minimum impressions per query across its competing pages (default 30)"
    },
    "limit": {
      "type": "number",
      "description": "Max queries / conflicts (default 30, max 200)"
    }
  }
}
```

</details>

Source: [src/lib/mcp/tools.ts:204](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/tools.ts#L204-L258) · [src/lib/mcp/shared.ts:1](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/shared.ts#L1-L373).

## get_rank_tracker

Read tracked keywords and their saved rank-check results.

<details>
<summary>Full registered description</summary>

```text
Tracked keyword rankings (Rank Tracker): every tracked keyword for a site with its latest SERP position check and the previous one for direction, plus country/device. Position 0/null means not found in the checked depth.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `site` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "site": {
      "type": "string",
      "description": "The site — a domain (example.com), GSC property (sc-domain:example.com), or a site id from list_sites"
    }
  },
  "required": [
    "site"
  ]
}
```

</details>

Source: [src/lib/mcp/tools.ts:260](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/tools.ts#L260-L284) · [src/lib/mcp/shared.ts:1](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/shared.ts#L1-L373).

## get_aeo_visibility

Read tracked questions and stored AI-answer visibility results.

<details>
<summary>Full registered description</summary>

```text
AI answer-engine visibility (AEO Tracker): tracked real-user questions and whether this site gets cited/mentioned when they are asked to ChatGPT, Perplexity, Claude, and Grok — latest result per engine per question. Use to assess AI-search presence and find questions where the site is invisible.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `site` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "site": {
      "type": "string",
      "description": "The site — a domain (example.com), GSC property (sc-domain:example.com), or a site id from list_sites"
    }
  },
  "required": [
    "site"
  ]
}
```

</details>

Source: [src/lib/mcp/tools.ts:286](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/tools.ts#L286-L304) · [src/lib/mcp/shared.ts:1](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/shared.ts#L1-L373).

## get_backlinks

Read saved backlink rows for the resolved site.

<details>
<summary>Full registered description</summary>

```text
The site's curated backlink inventory (Backlinks Checker): each tracked backlink with liveness (is the link still present) and indexed status, plus summary counts. This is the user's own link list — for competitor backlinks use get_link_mentions.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `site` | Yes | string | Not declared |
| `limit` | No | number | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "site": {
      "type": "string",
      "description": "The site — a domain (example.com), GSC property (sc-domain:example.com), or a site id from list_sites"
    },
    "limit": {
      "type": "number",
      "description": "Max rows (default 100, max 500)"
    }
  },
  "required": [
    "site"
  ]
}
```

</details>

Source: [src/lib/mcp/tools.ts:306](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/tools.ts#L306-L330) · [src/lib/mcp/shared.ts:1](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/shared.ts#L1-L373).

## get_link_mentions

Query stored LinkMention rows and related summaries using raw SQL.

<details>
<summary>Full registered description</summary>

```text
Link Monitor data: fresh quality backlinks recently earned by the WATCHED COMPETITOR BRANDS (pulled from Ahrefs; in-content, DR-filtered), plus multi-linker domains — sites that link to 2+ watched brands and are therefore prime outreach targets. Use for link prospecting and digital-PR ideas.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `brand` | No | string | Not declared |
| `limit` | No | number | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "brand": {
      "type": "string",
      "description": "Optional: filter to one watched brand domain"
    },
    "limit": {
      "type": "number",
      "description": "Max mention rows (default 100, max 500)"
    }
  }
}
```

</details>

Source: [src/lib/mcp/tools.ts:332](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/tools.ts#L332-L370) · [src/lib/mcp/shared.ts:1](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/shared.ts#L1-L373).

## get_site_health

Read the saved SiteHealth record.

<details>
<summary>Full registered description</summary>

```text
Site health snapshot: SSL certificate status/expiry, Google Safe Browsing verdict, VirusTotal reputation, and Core Web Vitals (PageSpeed, mobile) — as last checked by the app.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `site` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "site": {
      "type": "string",
      "description": "The site — a domain (example.com), GSC property (sc-domain:example.com), or a site id from list_sites"
    }
  },
  "required": [
    "site"
  ]
}
```

</details>

Source: [src/lib/mcp/tools.ts:372](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/tools.ts#L372-L392) · [src/lib/mcp/shared.ts:1](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/shared.ts#L1-L373).

## get_indexing_status

Group stored sitemap URLs and read saved URL inspection records.

<details>
<summary>Full registered description</summary>

```text
Indexing overview for a site: sitemap URL counts grouped by known Google index status, and the most recent URL Inspection results. Large 'unknown/not inspected' counts mean inspection coverage is thin, not that pages are deindexed.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `site` | Yes | string | Not declared |
| `limit` | No | number | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "site": {
      "type": "string",
      "description": "The site — a domain (example.com), GSC property (sc-domain:example.com), or a site id from list_sites"
    },
    "limit": {
      "type": "number",
      "description": "Max recent inspections to include (default 25, max 100)"
    }
  },
  "required": [
    "site"
  ]
}
```

</details>

Source: [src/lib/mcp/tools.ts:394](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/tools.ts#L394-L420) · [src/lib/mcp/shared.ts:1](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/shared.ts#L1-L373).

## get_site_audit

Read the latest saved audit and its page findings.

<details>
<summary>Full registered description</summary>

```text
Latest technical Site Audit from OpenGSC's built-in crawler: health score and issue counts across HTTP/redirects, metadata, canonicals/robots, HTML structure, JSON-LD/social metadata, links, mixed content, security headers and response time, plus affected URLs for one issue. This is the runtime Site Audit only; it does not combine AI Visibility or SEO Tools → GEO data. If no audit exists, tell the user to run one in the site's Audit tab.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `site` | Yes | string | Not declared |
| `issue` | No | string | Not declared |
| `limit` | No | number | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "site": {
      "type": "string",
      "description": "The site — a domain (example.com), GSC property (sc-domain:example.com), or a site id from list_sites"
    },
    "issue": {
      "type": "string",
      "description": "Optional issue code to list affected pages for (e.g. broken_links, title_missing, description_too_short, thin_content)"
    },
    "limit": {
      "type": "number",
      "description": "Max affected pages to return (default 30, max 200)"
    }
  },
  "required": [
    "site"
  ]
}
```

</details>

Source: [src/lib/mcp/tools.ts:421](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/tools.ts#L421-L467) · [src/lib/mcp/shared.ts:1](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/shared.ts#L1-L373).

## compare_periods

Aggregate stored DailyMetric rows for two date windows and compute changes.

<details>
<summary>Full registered description</summary>

```text
Period-over-period comparison from the local metrics store: current window vs the equally-sized previous window, grouped by query or page. Returns overall deltas plus the biggest winners, losers, new entries, and lost entries — answers "which queries improved/declined vs last month?" without any external API call.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `site` | Yes | string | Not declared |
| `days` | No | number | Not declared |
| `dimension` | No | string | Not declared |
| `limit` | No | number | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "site": {
      "type": "string",
      "description": "The site — a domain (example.com), GSC property (sc-domain:example.com), or a site id from list_sites"
    },
    "days": {
      "type": "number",
      "description": "Window length in days; compares the last N days vs the N days before that (default 28, max 240)"
    },
    "dimension": {
      "type": "string",
      "enum": [
        "query",
        "page"
      ],
      "description": "Compare by search query (default) or by page URL"
    },
    "limit": {
      "type": "number",
      "description": "Max rows per list — winners/losers/new/lost (default 15, max 50)"
    }
  },
  "required": [
    "site"
  ]
}
```

</details>

Source: [src/lib/mcp/tools.ts:468](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/tools.ts#L468-L533) · [src/lib/mcp/shared.ts:1](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/shared.ts#L1-L373).

## query_gsc_live

Resolve a site and try connected Google OAuth accounts through queryGsc, returning live Search Console search analytics.

<details>
<summary>Full registered description</summary>

```text
LIVE Google Search Console query (calls Google's Search Analytics API through the user's own OAuth token — free, but uses Google's daily quota; prefer get_search_performance for query/page data that's already synced). Use this when you need dimensions the local store doesn't have: country, device, date, or their combinations.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `site` | Yes | string | Not declared |
| `days` | No | number | Not declared |
| `dimensions` | No | array of string | Not declared |
| `limit` | No | number | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "site": {
      "type": "string",
      "description": "The site — a domain (example.com), GSC property (sc-domain:example.com), or a site id from list_sites"
    },
    "days": {
      "type": "number",
      "description": "Lookback window in days (default 28, max 480)"
    },
    "dimensions": {
      "type": "array",
      "items": {
        "type": "string",
        "enum": [
          "query",
          "page",
          "country",
          "device",
          "date"
        ]
      },
      "description": "GSC dimensions to group by, e.g. [\"country\"] or [\"query\",\"device\"] (default [\"country\"])"
    },
    "limit": {
      "type": "number",
      "description": "Max rows (default 50, max 250)"
    }
  },
  "required": [
    "site"
  ]
}
```

</details>

Source: [src/lib/mcp/tools.ts:535](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/tools.ts#L535-L575) · [src/lib/mcp/shared.ts:1](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/shared.ts#L1-L373) · [src/lib/gscQuery.ts:1](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/gscQuery.ts#L1-L114).

## inspect_url

Call Google Search Console URL Inspection using linked OAuth accounts, then upsert the inspection result and local quota counter.

<details>
<summary>Full registered description</summary>

```text
LIVE Google URL Inspection for up to 10 URLs (calls Google's URL Inspection API through the user's own OAuth token — free, but Google caps inspections per day; results are also cached into the app's Indexing tab). Returns index verdict, coverage state, last crawl, Google-selected canonical, and robots state per URL.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `site` | Yes | string | Not declared |
| `urls` | Yes | array of string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "site": {
      "type": "string",
      "description": "The site — a domain (example.com), GSC property (sc-domain:example.com), or a site id from list_sites"
    },
    "urls": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "1–10 absolute URLs on this site to inspect"
    }
  },
  "required": [
    "site",
    "urls"
  ]
}
```

</details>

- Actual handler can mutate local state, but dispatcher defaults this non-paid registration to readOnlyHint:true and read permission.

Source: [src/lib/mcp/tools.ts:577](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/tools.ts#L577-L660) · [src/lib/mcp/shared.ts:1](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/shared.ts#L1-L373).

## get_capabilities

Count local module records and group the complete tool registry by cost; report configured capabilities without exposing credentials.

<details>
<summary>Full registered description</summary>

```text
Instance overview — call this first if unsure what's available: server version, connected sites count, how fresh the synced GSC data is, which optional modules (rank tracker, AEO, Link Monitor, audits, GEO, indexer, GA4, Clarity, Bing/Yandex) actually contain data, and every tool grouped by what it costs to call. Saves you from calling tools that will come back empty, and from calling a paid one by accident.
```

</details>

No named input parameters are declared.

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {}
}
```

</details>

Source: [src/lib/mcp/tools.ts:662](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/tools.ts#L662-L731) · [src/lib/mcp/shared.ts:1](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/shared.ts#L1-L373).

## execute_sql_query

Execute a guarded read-only SQL statement against the local database, block credential tables and filter returned userId/siteId columns; return at most 500 rows.

<details>
<summary>Full registered description</summary>

```text
Run a custom read-only SELECT (or WITH…SELECT) query over the local database — for cohorts, cross-table joins, and aggregations the standard tools don't cover. Available tables: Site, DailyMetric, TrackedKeyword, RankCheck, TrackedQuestion, AeoCheck, Backlink, SitemapUrl, PageInspection, PageInspectionHistory, SiteHealth, SiteAudit, SiteAuditPage, LinkWatchBrand, LinkMention, DrCache, AlertEvent, Digest, ContentGroup, TopicCluster; sqlite_master (SQLite) or information_schema (MySQL) for schema discovery. Credential tables (User, Account, Session) are blocked, the connection is read-only, and results are capped at 500 rows.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `sql` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "sql": {
      "type": "string",
      "description": "The SELECT SQL query to execute (single statement)"
    }
  },
  "required": [
    "sql"
  ]
}
```

</details>

- Tenant filtering only checks userId/siteId columns present in the returned rows; arbitrary SELECT results without those columns are not fully tenant-isolated.

Source: [src/lib/mcp/tools.ts:732](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/tools.ts#L732-L824) · [src/lib/mcp/shared.ts:1](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/shared.ts#L1-L373).

## get_content_decay

Run findDecayingPages against stored search performance for the selected sites.

<details>
<summary>Full registered description</summary>

```text
Content Decay: every page whose traffic fell, compared over two equal, complete windows ending at the site's latest synced day (period=month: 56 days vs the 56 before; week: 14 vs 14; the newest 2 provisional days are left out). Status: Lost = had traffic, none in the last 14 days (deindexed, broken or migrated away — check it first); Critical = down 25%+; Warning = down 5%+. Pages below min_previous in the earlier window are ignored as noise. Sorted by absolute loss. yoyPct compares the current window with the same 52 weeks earlier, when history reaches that far. This is the primary way to find pages that need refreshing — feed a decaying URL straight into get_optimization_brief.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `site` | No | string | Not declared |
| `metric` | No | string | Not declared |
| `period` | No | string | Not declared |
| `min_previous` | No | number | Not declared |
| `status` | No | string | Not declared |
| `limit` | No | number | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "site": {
      "type": "string",
      "description": "The site — a domain, GSC property, or site id from list_sites. Pass \"all\" for the whole portfolio."
    },
    "metric": {
      "type": "string",
      "enum": [
        "clicks",
        "impressions"
      ],
      "description": "Which metric decays (default clicks)"
    },
    "period": {
      "type": "string",
      "enum": [
        "month",
        "week"
      ],
      "description": "Window length per side: month = 56 days, week = 14 (default month)"
    },
    "min_previous": {
      "type": "number",
      "description": "Ignore pages with less than this in the earlier window (default 5 clicks / 100 impressions)"
    },
    "status": {
      "type": "string",
      "enum": [
        "Lost",
        "Critical",
        "Warning"
      ],
      "description": "Only this status"
    },
    "limit": {
      "type": "number",
      "description": "How many pages to return, worst first (default 50, max 500)"
    }
  }
}
```

</details>

Source: [src/lib/mcp/toolsData.ts:42](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsData.ts#L42-L97) · [src/lib/mcp/shared.ts:1](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/shared.ts#L1-L373).

## get_ctr_benchmark

Group saved DailyMetric rows and compare CTR against positional benchmarks.

<details>
<summary>Full registered description</summary>

```text
CTR Benchmark: for queries already ranking in the top 10, the page's real CTR against the industry-standard CTR for that position (Backlinko 2023). A large negative `diff` means the ranking is fine but the search snippet is not — a title/meta rewrite, not a content rewrite. Sorted worst-first by default.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `site` | Yes | string | Not declared |
| `days` | No | number | Not declared |
| `minImpressions` | No | number | Not declared |
| `underperformingOnly` | No | boolean | Not declared |
| `limit` | No | number | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "site": {
      "type": "string",
      "description": "The site — a domain (example.com), GSC property (sc-domain:example.com), or a site id from list_sites"
    },
    "days": {
      "type": "number",
      "description": "Lookback window in days (default 90, max 365)"
    },
    "minImpressions": {
      "type": "number",
      "description": "Minimum summed impressions per query/page pair (default 10)"
    },
    "underperformingOnly": {
      "type": "boolean",
      "description": "Only rows below their benchmark (default true)"
    },
    "limit": {
      "type": "number",
      "description": "Max rows (default 50, max 500)"
    }
  },
  "required": [
    "site"
  ]
}
```

</details>

Source: [src/lib/mcp/toolsData.ts:98](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsData.ts#L98-L153) · [src/lib/mcp/shared.ts:1](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/shared.ts#L1-L373).

## get_content_groups

Read saved content groups/clusters and match their rules against stored URLs and queries.

<details>
<summary>Full registered description</summary>

```text
The site's Content Groups and Topic Clusters — the user's own URL/query groupings — with aggregate clicks, impressions and average position per group over a window. Use to answer "which section of the site is growing" without guessing at URL patterns.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `site` | Yes | string | Not declared |
| `days` | No | number | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "site": {
      "type": "string",
      "description": "The site — a domain (example.com), GSC property (sc-domain:example.com), or a site id from list_sites"
    },
    "days": {
      "type": "number",
      "description": "Lookback window in days (default 28)"
    }
  },
  "required": [
    "site"
  ]
}
```

</details>

Source: [src/lib/mcp/toolsData.ts:155](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsData.ts#L155-L215) · [src/lib/mcp/shared.ts:1](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/shared.ts#L1-L373).

## get_rank_history

Read tracked keywords and RankCheck history.

<details>
<summary>Full registered description</summary>

```text
Full SERP position history for tracked keywords (Rank Tracker), not just the latest check — every RankCheck point with its date and ranking URL. get_rank_tracker gives the current standing; this gives the trend, so you can tell a one-off SERP wobble from a sustained slide.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `site` | Yes | string | Not declared |
| `keyword` | No | string | Not declared |
| `days` | No | number | Not declared |
| `limit` | No | number | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "site": {
      "type": "string",
      "description": "The site — a domain (example.com), GSC property (sc-domain:example.com), or a site id from list_sites"
    },
    "keyword": {
      "type": "string",
      "description": "Optional: one keyword (exact or substring). Omit for every tracked keyword."
    },
    "days": {
      "type": "number",
      "description": "Lookback window in days (default 90, max 480)"
    },
    "limit": {
      "type": "number",
      "description": "Max history points per keyword (default 60, max 300)"
    }
  },
  "required": [
    "site"
  ]
}
```

</details>

Source: [src/lib/mcp/toolsData.ts:217](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsData.ts#L217-L261) · [src/lib/mcp/shared.ts:1](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/shared.ts#L1-L373).

## get_geo_audits

Read saved GeoAudit summaries or a selected detailed audit.

<details>
<summary>Full registered description</summary>

```text
GEO audits (Generative Engine Optimization): stored reports on how AI search engines answer a target query — which brands and sources they cite, and where this site stands. Pass an id for the full report, omit it for the list. Unlike AEO Tracker (tracked questions over time) these are one-off deep audits.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `id` | No | string | Not declared |
| `query` | No | string | Not declared |
| `limit` | No | number | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "id": {
      "type": "string",
      "description": "Optional: a specific audit id from the list, to get its full report"
    },
    "query": {
      "type": "string",
      "description": "Optional: filter the list by audited query (substring)"
    },
    "limit": {
      "type": "number",
      "description": "Max audits to list (default 20, max 100)"
    }
  }
}
```

</details>

Source: [src/lib/mcp/toolsData.ts:263](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsData.ts#L263-L296) · [src/lib/mcp/shared.ts:1](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/shared.ts#L1-L373).

## get_generations

Query saved SEO generation history; no generation is started.

<details>
<summary>Full registered description</summary>

```text
The SEO Tools generation history: outlines, articles, analyses and landing pages this instance has produced, newest first. Call before writing anything new — it shows what already exists for a keyword, so you extend the existing piece instead of producing a near-duplicate that will cannibalize it. Pass an id to read one in full.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `id` | No | string | Not declared |
| `type` | No | string | Not declared |
| `keyword` | No | string | Not declared |
| `limit` | No | number | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "id": {
      "type": "string",
      "description": "Optional: one record id, to get its full content"
    },
    "type": {
      "type": "string",
      "description": "Optional filter: outline | text | analysis | landing | cluster"
    },
    "keyword": {
      "type": "string",
      "description": "Optional: filter by keyword (substring)"
    },
    "limit": {
      "type": "number",
      "description": "Max records to list (default 25, max 100)"
    }
  }
}
```

</details>

Source: [src/lib/mcp/toolsData.ts:298](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsData.ts#L298-L341) · [src/lib/mcp/shared.ts:1](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/shared.ts#L1-L373).

## get_engine_performance

Read EnginePortfolioCache for Bing or Yandex and the requested period; return empty data with configuration/migration guidance when absent. No engine API call occurs.

<details>
<summary>Full registered description</summary>

```text
Bing and Yandex portfolio performance from the server-side snapshot (EnginePortfolioCache) — per-site clicks, impressions, CTR and average position across every connected Bing/Yandex Webmaster account, plus period-over-period deltas. Google data comes from the local store via get_search_performance instead. Returns the cached snapshot; if it is empty the user needs to press Sync on the dashboard.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `engine` | No | string | Not declared |
| `period` | No | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "engine": {
      "type": "string",
      "enum": [
        "bing",
        "yandex"
      ],
      "description": "Which engine (default bing)"
    },
    "period": {
      "type": "string",
      "description": "Cached period key as used by the dashboard, e.g. 28d / 3m (default 28d)"
    }
  }
}
```

</details>

Source: [src/lib/mcp/toolsData.ts:343](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsData.ts#L343-L377) · [src/lib/mcp/shared.ts:1](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/shared.ts#L1-L373).

## get_analytics

Resolve the site’s ga4PropertyId and try linked Google OAuth accounts. Call Google Analytics Data API v1beta properties.runReport with current and previous date ranges and sessions, engagementRate, keyEvents and totalRevenue; return normalized metrics and percentage changes. Return linked:false if no GA4 property is attached.

<details>
<summary>Full registered description</summary>

```text
LIVE Google Analytics 4 for a site (calls GA4 through the user's own OAuth — free, but uses Google's quota): sessions, engagement rate, key events and revenue for a period, with the previous-period comparison. GSC tells you how people arrive; this tells you what they did next. Returns linked:false when the site has no GA4 property attached.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `site` | Yes | string | Not declared |
| `period` | No | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "site": {
      "type": "string",
      "description": "The site — a domain (example.com), GSC property (sc-domain:example.com), or a site id from list_sites"
    },
    "period": {
      "type": "string",
      "description": "Period key: 7d, 28d, 3m, 6m, 12m (default 28d)"
    }
  },
  "required": [
    "site"
  ]
}
```

</details>

- period has no exposed enum/default despite descriptive examples; handler defaults to 28d and dateWindows determines the supported periods.
- Only four fixed metrics and two aggregate date ranges are requested; this is not an arbitrary GA4 report tool.

Source: [src/lib/mcp/toolsData.ts:379](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsData.ts#L379-L446) · [src/lib/mcp/shared.ts:1](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/shared.ts#L1-L373) · [src/lib/ga4.ts:1](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/ga4.ts#L1-L96).

## get_clarity

Read saved ClaritySnapshot rows, not the live Clarity API.

<details>
<summary>Full registered description</summary>

```text
Microsoft Clarity behaviour data for a site from the stored snapshots: sessions, dead clicks, rage clicks, scroll depth and the worst-performing pages over the last 30 days. Rage and dead clicks on a page that ranks well are a UX problem, not an SEO one — worth separating before recommending a content rewrite.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `site` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "site": {
      "type": "string",
      "description": "The site — a domain (example.com), GSC property (sc-domain:example.com), or a site id from list_sites"
    }
  },
  "required": [
    "site"
  ]
}
```

</details>

Source: [src/lib/mcp/toolsData.ts:448](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsData.ts#L448-L473) · [src/lib/mcp/shared.ts:1](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/shared.ts#L1-L373).

## get_indexer_stats

Read saved indexer domains and daily statistics.

<details>
<summary>Full registered description</summary>

```text
Private Indexer Network status: every doorway domain with its template, money-site target and allowed crawlers, plus verified bot hits over the last 30 days broken down by engine (Google/Bing/Yandex/Mail.ru/AI) and the redirect count for non-bot visitors. A domain with zero Google hits is not being crawled and its deployed script needs checking.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `domain` | No | string | Not declared |
| `days` | No | number | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "domain": {
      "type": "string",
      "description": "Optional: one doorway domain to detail"
    },
    "days": {
      "type": "number",
      "description": "Lookback window for the hit counts (default 30, max 180)"
    }
  }
}
```

</details>

Source: [src/lib/mcp/toolsData.ts:475](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsData.ts#L475-L538) · [src/lib/mcp/shared.ts:1](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/shared.ts#L1-L373).

## get_digests

Query stored digest history, not generate or send a digest.

<details>
<summary>Full registered description</summary>

```text
Previously generated portfolio digests (the Telegram/Slack reports): rendered Markdown per run, with the tag filter and window each covered. Useful for "what did we report last week" and for continuity — so a new report picks up where the last one left off instead of restating it.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `id` | No | string | Not declared |
| `limit` | No | number | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "id": {
      "type": "string",
      "description": "Optional: one digest id, to get its full Markdown"
    },
    "limit": {
      "type": "number",
      "description": "Max digests to list (default 10, max 50)"
    }
  }
}
```

</details>

Source: [src/lib/mcp/toolsData.ts:540](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsData.ts#L540-L574) · [src/lib/mcp/shared.ts:1](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/shared.ts#L1-L373).

## get_alerts

Query saved alert records for one site or the workspace.

<details>
<summary>Full registered description</summary>

```text
Alerts that have actually fired (alert-cron, hourly): rank drops, week-over-week click drops, SSL expiry and low audit scores, newest first. Each is deduplicated per occurrence, so this is a clean incident list rather than a repeating notification stream. Start a triage here — it is the app's own view of what already went wrong.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `site` | No | string | Not declared |
| `type` | No | string | Not declared |
| `days` | No | number | Not declared |
| `limit` | No | number | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "site": {
      "type": "string",
      "description": "Optional: restrict to one site (domain or id)"
    },
    "type": {
      "type": "string",
      "description": "Optional: rank_drop | traffic_drop | ssl_expiry | audit_score"
    },
    "days": {
      "type": "number",
      "description": "Lookback window in days (default 30, max 365)"
    },
    "limit": {
      "type": "number",
      "description": "Max alerts (default 50, max 200)"
    }
  }
}
```

</details>

Source: [src/lib/mcp/toolsData.ts:576](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsData.ts#L576-L617) · [src/lib/mcp/shared.ts:1](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/shared.ts#L1-L373).

## get_keyword_metrics

ReadKeywordCache for requested keywords; no provider request.

<details>
<summary>Full registered description</summary>

```text
Search volume, keyword difficulty and CPC for specific keywords, from the local metric cache. The cache is filled by the 'load weights' button or by importing an Ahrefs/Semrush export — this tool never calls a provider and never spends credits. A keyword missing from the response has not been loaded yet; that is not evidence of zero search volume. Pair with get_striking_distance to rank opportunities by real demand.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `keywords` | Yes | array of string | Not declared |
| `country` | No | string | Not declared |
| `provider` | No | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "keywords": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Keywords to look up (max 200)"
    },
    "country": {
      "type": "string",
      "description": "Market the volumes belong to, 2-letter code. Default us"
    },
    "provider": {
      "type": "string",
      "description": "ahrefs (default) or semrush"
    }
  },
  "required": [
    "keywords"
  ]
}
```

</details>

Source: [src/lib/mcp/toolsMetrics.ts:28](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsMetrics.ts#L28-L69) · [src/lib/mcp/shared.ts:1](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/shared.ts#L1-L373).

## get_domain_metrics

ReadDomainCache for requested domains; no provider request.

<details>
<summary>Full registered description</summary>

```text
Referring domains, backlink count, estimated organic traffic and traffic value for one or more domains, from the local cache. Read-only and free. Domain Rating is NOT here — it comes from a separate free endpoint and is available for every site without any of this. Empty means not loaded, not zero. Provider chooses whose rows to read: ahrefs (default), semrush, majestic (no traffic figures), or keysso — Keys.so, the Yandex/Runet index: its `dr` is Keys.so's own DR (not comparable with Ahrefs DR), organic traffic fields stay null, and Yandex visibility/top-50/AI-answer counts ride in `payload` (vis, it50, dashboard); or dataforseo — its `dr` is DataForSEO rank on a 0–100 scale (not Ahrefs DR), traffic fields stay null, and the backlink spam score, broken-backlink count and referring main domains ride in `payload`.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `domains` | Yes | array of string | Not declared |
| `provider` | No | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "domains": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Domains to look up (max 100)"
    },
    "provider": {
      "type": "string",
      "description": "ahrefs (default), semrush, majestic, keysso (Yandex/Runet), or dataforseo"
    }
  },
  "required": [
    "domains"
  ]
}
```

</details>

Source: [src/lib/mcp/toolsMetrics.ts:71](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsMetrics.ts#L71-L102) · [src/lib/mcp/shared.ts:1](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/shared.ts#L1-L373).

## get_yandex_ai_answers

Resolve a site and read cached Yandex AI-answer domain metrics.

<details>
<summary>Full registered description</summary>

```text
Yandex AI-answer visibility for a site, from Keys.so (Yandex/Runet index, Moscow base): the queries whose Yandex AI answer already cites the site (top 100 by exact Wordstat frequency `wsk`), the site's cited URL and its 1-based `rank` among the answer's source domains, the other `sources`, and the ten domains most often cited beside it (`shared` = queries citing both). `total` is every query Keys.so has with the site in an AI answer. Read-only from the stored report the human refreshed in Visibility → Yandex AI (2 Keys.so credits); null `report` means not loaded yet, not 'never cited'.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `site` | Yes | string | Not declared |
| `limit` | No | number | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "site": {
      "type": "string",
      "description": "The site — a domain (example.com), GSC property (sc-domain:example.com), or a site id from list_sites"
    },
    "limit": {
      "type": "number",
      "description": "Max queries to return (default 50, max 100)"
    }
  },
  "required": [
    "site"
  ]
}
```

</details>

Source: [src/lib/mcp/toolsMetrics.ts:104](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsMetrics.ts#L104-L146) · [src/lib/mcp/shared.ts:1](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/shared.ts#L1-L373).

## get_backlink_profile

Read stored referring-domain rows and backlink snapshots.

<details>
<summary>Full registered description</summary>

```text
A site's referring domains — live and lost — plus the stored history of referring-domain and backlink counts. Read-only from the local cache, filled by the Backlink profile panel or a referring-domains import. Lost domains are derived by diffing pulls, so a site with one pull has no lost rows yet regardless of reality.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `site` | Yes | string | Not declared |
| `includeLost` | No | boolean | Not declared |
| `provider` | No | string | Not declared |
| `minDr` | No | number | Not declared |
| `limit` | No | number | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "site": {
      "type": "string",
      "description": "The site — a domain (example.com), GSC property (sc-domain:example.com), or a site id from list_sites"
    },
    "includeLost": {
      "type": "boolean",
      "description": "Include referring domains recorded as lost. Default true"
    },
    "provider": {
      "type": "string",
      "description": "Whose stored rows to read: ahrefs (default), semrush, majestic (dr = Trust Flow), keysso (dr = Keys.so DR, Yandex/Runet index), dataforseo (dr = DataForSEO rank 0–100), or all"
    },
    "minDr": {
      "type": "number",
      "description": "Only return referring domains at or above this rating (in the chosen provider's own scale)"
    },
    "limit": {
      "type": "number",
      "description": "Max referring domains to return (default 100, max 500)"
    }
  },
  "required": [
    "site"
  ]
}
```

</details>

Source: [src/lib/mcp/toolsMetrics.ts:148](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsMetrics.ts#L148-L192) · [src/lib/mcp/shared.ts:1](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/shared.ts#L1-L373).

## get_competitor_gap

Read stored competitor-gap data and own Yandex/GSC queries to classify gaps.

<details>
<summary>Full registered description</summary>

```text
Keywords competitors rank for, joined against this site's own Search Console data. Each row says whether you already rank (and where), whether you get impressions but no ranking page, or whether you are absent entirely — which is the difference between a rewrite, an intent fix, and net-new content. Read-only: competitor keywords must first be pulled in the Competitors screen.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `site` | Yes | string | Not declared |
| `country` | No | string | Not declared |
| `bucket` | No | string | Not declared |
| `limit` | No | number | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "site": {
      "type": "string",
      "description": "The site — a domain (example.com), GSC property (sc-domain:example.com), or a site id from list_sites"
    },
    "country": {
      "type": "string",
      "description": "Market, 2-letter code. Default us. \"yandex\" = the Yandex market from Keys.so (Moscow; other regions \"yandex_<code>\", e.g. yandex_spb) — both sides are Yandex positions (ours from the site's own stored Yandex keywords), volume is Wordstat exact frequency, no KD"
    },
    "bucket": {
      "type": "string",
      "description": "Filter: close (we rank in top 30) | weak (impressions only) | missing (absent)"
    },
    "limit": {
      "type": "number",
      "description": "Max rows (default 100, max 500)"
    }
  },
  "required": [
    "site"
  ]
}
```

</details>

Source: [src/lib/mcp/toolsMetrics.ts:194](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsMetrics.ts#L194-L291) · [src/lib/mcp/shared.ts:1](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/shared.ts#L1-L373).

## get_domain_traffic

Query stored domain traffic cache rows.

<details>
<summary>Full registered description</summary>

```text
Estimated monthly visits, engagement (bounce rate, time on site, pages per visit), global and country rank, the 3-month visit trend, traffic-source shares INCLUDING the GenAI channel, top countries and top keywords for any domain — including competitors, since this does not need Search Console access. Read-only from the local cache, filled when a human presses Traffic on a site page; this tool never calls the provider and never spends credits. Empty means nobody has checked that domain yet, not that it has no traffic. Pair the GenAI share with get_aeo_visibility: citations in AI answers only matter if they send sessions.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `domains` | Yes | array of string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "domains": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Domains to look up (max 50)"
    }
  },
  "required": [
    "domains"
  ]
}
```

</details>

Source: [src/lib/mcp/toolsMetrics.ts:293](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsMetrics.ts#L293-L345) · [src/lib/mcp/shared.ts:1](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/shared.ts#L1-L373).

## get_ads_intel

Query cached advertising intelligence rows.

<details>
<summary>Full registered description</summary>

```text
Ad intelligence for a domain, from the local cache. Google Ads Transparency: which advertisers run ads for it (with creative ID counts), the ad titles with their run windows, weekly ad-count activity per advertiser and country, and image creatives. Read-only and free — the cache is filled when a human presses Load on the site's Ads tab. Sections not loaded yet come back in notLoaded; an empty section means the provider answered and found nothing, not that nobody looked. Section `yandex_direct` (when loaded via Keys.so on the same tab; the region last loaded wins here) holds Yandex Direct: top ads with landing URL and query reach, and the queries the domain's ads show on with Wordstat exact frequency.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `domain` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "domain": {
      "type": "string",
      "description": "Domain to inspect (normalized; www stripped)"
    }
  },
  "required": [
    "domain"
  ]
}
```

</details>

Source: [src/lib/mcp/toolsMetrics.ts:347](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsMetrics.ts#L347-L403) · [src/lib/mcp/shared.ts:1](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/shared.ts#L1-L373).

## get_keyword_demand

Read stored demand searches/results, optionally join the site’s saved Yandex/GSC queries and compute verdicts.

<details>
<summary>Full registered description</summary>

```text
Keyword research already stored on this instance, joined against a site's own Search Console positions. Free and instant. Call this BEFORE research_keywords: a seed researched in the last 14 days is answered here at no cost. Each row carries a verdict — reach (you rank top 30, improve the page), wrong_page (impressions but nothing winning), none (write it). With no seed, lists the searches that have been run. An empty result means nobody has researched this seed yet; it is not evidence that the market is empty.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `seed` | No | string | Not declared |
| `site` | No | string | Not declared |
| `country` | No | string | Not declared |
| `verdict` | No | string | Not declared |
| `limit` | No | number | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "seed": {
      "type": "string",
      "description": "Seed keyword to look up. Omit to list stored searches instead."
    },
    "site": {
      "type": "string",
      "description": "The site — a domain (example.com), GSC property (sc-domain:example.com), or a site id from list_sites Optional — without it, rows carry market data but no verdict."
    },
    "country": {
      "type": "string",
      "description": "Market, 2-letter code. Default us. \"yandex\" = the Yandex market, Moscow (Keys.so, Wordstat volumes; verdicts against the site's own Yandex positions); other Yandex regions are \"yandex_<code>\", e.g. yandex_spb"
    },
    "verdict": {
      "type": "string",
      "description": "Filter rows: reach | wrong_page | none"
    },
    "limit": {
      "type": "number",
      "description": "Max rows (default 100, max 500)"
    }
  }
}
```

</details>

Source: [src/lib/mcp/toolsDemand.ts:210](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsDemand.ts#L210-L299) · [src/lib/mcp/shared.ts:1](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/shared.ts#L1-L373).

## research_keywords

Resolve configured keyword source, expand keywords using the provider, record usage, upsert demand cache and optionally update shared site context.

<details>
<summary>Full registered description</summary>

```text
PAID — spends the owner's own DataForSEO credits. Discovers what a market searches for from one seed keyword, then joins it against a site's Search Console history so every row says whether you already rank (reach), appear without ranking (wrong_page), or are absent (none). Call get_keyword_demand first: a seed researched in the last 14 days comes back from cache for free, and get_striking_distance already covers queries the site ranks for without spending anything. Roughly $0.03 per call at the default 150 rows. Results are stored before this returns, so a client timeout costs nothing — the same call replays from cache.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `seed` | Yes | string | Not declared |
| `site` | No | string | Not declared |
| `country` | No | string | Not declared |
| `language` | No | string | Not declared |
| `mode` | No | string | Not declared |
| `limit` | No | number | Not declared |
| `clickstream` | No | boolean | Not declared |
| `confirm` | Yes | boolean | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "seed": {
      "type": "string",
      "description": "The seed keyword to research"
    },
    "site": {
      "type": "string",
      "description": "The site — a domain (example.com), GSC property (sc-domain:example.com), or a site id from list_sites Optional — without it there is no Search Console half and no verdicts."
    },
    "country": {
      "type": "string",
      "description": "Market, 2-letter code. Default us"
    },
    "language": {
      "type": "string",
      "description": "Language code. Default en"
    },
    "mode": {
      "type": "string",
      "description": "auto (default) walks related → suggestions → ideas and stops at the first source with enough terms. related = semantic neighbours, suggestions = long tail containing the seed, ideas = same meaning, different words. Auto is one billed call, not three."
    },
    "limit": {
      "type": "number",
      "description": "Rows to request (default 150, max 1000). Billed per row returned."
    },
    "clickstream": {
      "type": "boolean",
      "description": "Clickstream-refined volumes. DOUBLES the cost and changes nothing else. Default false."
    },
    "confirm": {
      "type": "boolean",
      "description": "Must be true. PAID: this spends the instance owner's own DataForSEO credits — get their permission before setting it."
    }
  },
  "required": [
    "seed",
    "confirm"
  ]
}
```

</details>

- Registry cost is paid; dispatcher requires workspace spend permission. Handler confirmation/estimate/cache paths determine whether this call actually spends credits.

Source: [src/lib/mcp/toolsDemand.ts:301](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsDemand.ts#L301-L456) · [src/lib/mcp/shared.ts:1](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/shared.ts#L1-L373).

## get_optimization_brief

Combine saved query/audit data with a live scrapePage result into an optimization brief.

<details>
<summary>Full registered description</summary>

```text
FREE, and the entry point for optimizing a page: everything this instance knows about one URL, assembled in a single call — the queries it ranks for, its striking-distance keywords, where its CTR falls short of the benchmark for its position, its traffic trend over recent months, cannibalization conflicts with the site's other pages, its technical audit issues, and (unless disabled) its live title, meta description, headings and body Markdown. Use this to write the rewrite yourself. Only reach for the PAID start_rewrite_job when the user explicitly wants the app's own pipeline.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `site` | Yes | string | Not declared |
| `url` | Yes | string | Not declared |
| `days` | No | number | Not declared |
| `includeContent` | No | boolean | Not declared |
| `limit` | No | number | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "site": {
      "type": "string",
      "description": "The site — a domain (example.com), GSC property (sc-domain:example.com), or a site id from list_sites"
    },
    "url": {
      "type": "string",
      "description": "The page to optimize — full URL or path (e.g. /pricing)"
    },
    "days": {
      "type": "number",
      "description": "Lookback window for the performance data (default 90)"
    },
    "includeContent": {
      "type": "boolean",
      "description": "Fetch the live page for title/meta/headings/body (default true). Set false to stay entirely offline."
    },
    "limit": {
      "type": "number",
      "description": "Max query rows per section (default 30, max 200)"
    }
  },
  "required": [
    "site",
    "url"
  ]
}
```

</details>

Source: [src/lib/mcp/toolsOptimize.ts:103](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsOptimize.ts#L103-L258) · [src/lib/mcp/shared.ts:1](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/shared.ts#L1-L373).

## fetch_page_content

Fetch and extract a page through scrapePage.

<details>
<summary>Full registered description</summary>

```text
FREE: fetch any URL — your own or a competitor's — and return it as clean article Markdown with title, meta description, headings and word count. Boilerplate (menus, footers, sidebars) is stripped by the same readability pass the SEO Tools use, so what comes back is the article rather than the chrome. `boilerplateOnly: true` means no article was found and the result must not be treated as content.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `url` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "url": {
      "type": "string",
      "description": "Absolute URL to fetch"
    }
  },
  "required": [
    "url"
  ]
}
```

</details>

Source: [src/lib/mcp/toolsOptimize.ts:260](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsOptimize.ts#L260-L283) · [src/lib/mcp/shared.ts:1](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/shared.ts#L1-L373).

## analyze_text

Run deterministic local text metrics and similarity analysis on supplied text; no AI call.

<details>
<summary>Full registered description</summary>

```text
FREE and deterministic — no model is called, so this costs nothing and returns the same answer every time. Given a draft and the source it replaces, reports: uniqueness (1 − word-trigram overlap), fact drift (numbers and identifiers that were INVENTED or dropped — invented is the dangerous direction, since a wrong price ships), heading-structure match, word count, and a count of common machine tells (em dashes, "furthermore", "it is important to note"). Run it on every rewrite you produce before handing it to the user.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `text` | Yes | string | Not declared |
| `source` | No | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "text": {
      "type": "string",
      "description": "The draft to analyze"
    },
    "source": {
      "type": "string",
      "description": "The original text it is meant to replace. Omit to get word count and machine tells only — drift and uniqueness need something to compare against."
    }
  },
  "required": [
    "text"
  ]
}
```

</details>

Source: [src/lib/mcp/toolsOptimize.ts:285](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsOptimize.ts#L285-L341) · [src/lib/mcp/shared.ts:1](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/shared.ts#L1-L373).

## start_rewrite_job

Require confirmation, resolve owner AI credentials/policy, queue a rewrite job and return its id.

<details>
<summary>Full registered description</summary>

```text
PAID — spends the instance owner's own AI credits and needs confirm: true. Rewrites up to 20 pages with OpenGSC's Content Rewriter, in the BACKGROUND: returns a jobId immediately, then poll get_generation_job. One page takes minutes (fetch, a model call on a length-scaled token budget, a repair pass when the value audit fails, then a publication gate and an independent QA judge that rejects non-articles instead of saving them as completed). MCP clients cut a tool call off at 30–60s, which is far shorter than the run — so this never returns the text directly. Each page is saved the moment it finishes, so a timeout, a closed client or a server restart costs at most the page in flight and never the ones already paid for. Prefer get_optimization_brief + your own writing + analyze_text, which costs the owner nothing; use this when they want the app's own pipeline, editorial policy, banned-word list or a per-job `custom` instruction applied.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `confirm` | Yes | boolean | Not declared |
| `urls` | No | array of string | Not declared |
| `text` | No | string | Not declared |
| `language` | No | string | Not declared |
| `tone` | No | string | Not declared |
| `forbiddenBrands` | No | array of string | Not declared |
| `custom` | No | string | Not declared |
| `maskAI` | No | boolean | Not declared |
| `marksScrub` | No | boolean | Not declared |
| `bannedWords` | No | array of string | Not declared |
| `temperature` | No | number | Not declared |
| `snippet` | No | boolean | Not declared |
| `judge` | No | boolean | Not declared |
| `policyName` | No | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "confirm": {
      "type": "boolean",
      "description": "Must be true. PAID: this call spends the instance owner's own AI credits — get their permission before setting it."
    },
    "urls": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "1–20 page URLs to rewrite, processed one after another"
    },
    "text": {
      "type": "string",
      "description": "Literal text to rewrite instead of URLs (single item)"
    },
    "language": {
      "type": "string",
      "description": "Target language NAME, e.g. \"Greek\". Omit to keep each page's own language."
    },
    "tone": {
      "type": "string",
      "description": "Optional tone hint"
    },
    "forbiddenBrands": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Names that must not appear in the rewritten body. Checked deterministically after each page and reported per page as `mechanics`; never fails a page."
    },
    "custom": {
      "type": "string",
      "description": "Free-text instruction applied to every page in this job — what the rewrite must not mention, placeholders it must keep verbatim, links it must add. Use this for one-off rules; a standing house style belongs in the editorial policy instead."
    },
    "maskAI": {
      "type": "boolean",
      "description": "Strip common machine tells from the output (default true)"
    },
    "marksScrub": {
      "type": "boolean",
      "description": "Strip invisible Unicode marks from the output — zero-width spaces, bidi controls, soft hyphens, exotic spaces (default true). Set false only to reproduce the raw model output."
    },
    "bannedWords": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Words the model must not use — the AI-Fingerprint Lab's marker export goes here"
    },
    "temperature": {
      "type": "number",
      "description": "Sampling temperature; omit for the provider default"
    },
    "snippet": {
      "type": "boolean",
      "description": "Also propose a refreshed title + meta description per page"
    },
    "judge": {
      "type": "boolean",
      "description": "Independent QA pass (default true): after the deterministic gate, a fresh-context model call checks the draft is a complete publishable article — rejects planning notes, truncated stubs and copied page furniture instead of saving them as completed pages"
    },
    "policyName": {
      "type": "string",
      "description": "Editorial policy to write under, by name. Omit to use the instance's active policy."
    }
  },
  "required": [
    "confirm"
  ]
}
```

</details>

- Registry cost is paid; dispatcher requires workspace spend permission. Handler confirmation/estimate/cache paths determine whether this call actually spends credits.

Source: [src/lib/mcp/toolsOptimize.ts:343](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsOptimize.ts#L343-L449) · [src/lib/mcp/shared.ts:1](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/shared.ts#L1-L373).

## start_generation_job

Require confirmation, resolve generation type, owner AI/SERP credentials, policy and optional keyword grounding; launch a background generation job and persist history.

<details>
<summary>Full registered description</summary>

```text
PAID — spends the instance owner's own AI credits and needs confirm: true. Starts a background SEO Tools generation job and returns its id immediately; the pipeline runs for minutes (competitor scrape, MAP/REDUCE fact grounding, fact-scrub, chunked writing, volume guard), far longer than a tool call can wait. Poll get_generation_job for the result. Types: outline, outline_auto (SERP→scrape→outline in one unattended step), text (writes the article FROM an outline), analysis, landing, cluster. type=landing ships the outline TOGETHER with the landing wireframe (blocks) and the scraped top-page skeletons (competitors) — the wireframe is the deliverable, the outline is its grounding. Completed results are saved to SEO Tools → History, so finished outlines appear in the UI Text generator's structure picker and in get_generations. HOW TO WRITE AN ARTICLE (same clicks as the UI): 1) start_generation_job type=outline with the keyword, country, language and keywordIdeas:{} — that last one is the UI's 'load keywords' button: real ideas with volumes from the user's Ahrefs/Semrush/DataForSEO key, billed against the same monthly cap; 2) poll get_generation_job until completed; 3) start_generation_job type=text with outlineId set to that jobId — the server loads the outline itself, with its facts bank, keyword and language. The text step's form fields (language, tone, sourceMode, promptType+custom, includeToc, targetWordCount, temperature, bannedWords) are top-level arguments with the UI's defaults; anything else the /seo-tools pages post (competitors, gl/hl, generate) goes in payload. For a straightforward rewrite, get_optimization_brief and your own writing is free.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `confirm` | Yes | boolean | Not declared |
| `type` | Yes | string | Not declared |
| `keyword` | No | string | Not declared |
| `outlineId` | No | string | Not declared |
| `keywordIdeas` | No | object | Not declared |
| `language` | No | string | Not declared |
| `country` | No | string | Not declared |
| `tone` | No | string | Not declared |
| `promptType` | No | string | Not declared |
| `custom` | No | string | Not declared |
| `sourceMode` | No | string | Not declared |
| `includeToc` | No | boolean | Not declared |
| `targetWordCount` | No | number | Not declared |
| `temperature` | No | number | Not declared |
| `bannedWords` | No | array of string | Not declared |
| `chunkSections` | No | number | Not declared |
| `forbiddenBrands` | No | array of string | Not declared |
| `judge` | No | boolean | Not declared |
| `marksScrub` | No | boolean | Not declared |
| `payload` | No | object | Not declared |
| `policyName` | No | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "confirm": {
      "type": "boolean",
      "description": "Must be true. PAID: this call spends the instance owner's own AI credits — get their permission before setting it."
    },
    "type": {
      "type": "string",
      "enum": [
        "outline",
        "outline_auto",
        "text",
        "analysis",
        "landing",
        "cluster"
      ],
      "description": "Which pipeline to run"
    },
    "keyword": {
      "type": "string",
      "description": "The target keyword — top-level, exactly like the UI's keyword field (required for outline/outline_auto/analysis/cluster; for text it defaults to the outline's own keyword)"
    },
    "outlineId": {
      "type": "string",
      "description": "type=text: the structure to write from — the jobId of a finished outline/outline_auto job, or an id from get_generations. This is the server-side equivalent of the UI's structure picker; use it instead of passing the outline object around."
    },
    "keywordIdeas": {
      "type": "object",
      "description": "outline/outline_auto/landing only — the UI's 'load keywords' step: fetch real keyword ideas with volumes from the instance's configured provider (Ahrefs/Semrush/DataForSEO, official or reseller) and ground the outline on them. Spends provider units against the same monthly cap as the UI button. Pass {} for the Settings defaults, or { limit: 50-200, withDifficulty: boolean, mode: 'matching'|'related' }. Requires country — the market is never guessed.",
      "properties": {
        "limit": {
          "type": "number",
          "description": "Max ideas to request — the ceiling on what this can cost (50–200, default from Settings)"
        },
        "withDifficulty": {
          "type": "boolean",
          "description": "Also fetch keyword difficulty (costs more units on Ahrefs)"
        },
        "mode": {
          "type": "string",
          "enum": [
            "matching",
            "related"
          ],
          "description": "matching = keywords containing the seed; related = semantic neighbours (default matching)"
        }
      }
    },
    "language": {
      "type": "string",
      "description": "Language code, e.g. en, ru, el, fr. Outline jobs default to en; text jobs inherit the outline's own language when omitted."
    },
    "country": {
      "type": "string",
      "description": "Two-letter market code for outline/landing/cluster (default us) — drives SERP geo and the outline's country meta."
    },
    "tone": {
      "type": "string",
      "description": "Free-text tone hint, e.g. 'expert, friendly, no hype' (the UI maps its tone dropdown to the same kind of string)."
    },
    "promptType": {
      "type": "string",
      "enum": [
        "service",
        "custom"
      ],
      "description": "Service prompt (default) or a fully custom writing prompt — same radio as the UI Text generator."
    },
    "custom": {
      "type": "string",
      "description": "The author's instruction. With promptType=custom it IS the writing prompt; with service (default) it is an additional instruction that outranks the section briefs where they conflict. It reaches every call that writes prose — each chunk of the chunked writer and the FAQ pass — and, on outline jobs, the structure and section-enrichment passes too, so a rule like 'never name a competitor' or 'no separate section for the reverse route' is enforced at both steps. A text job inherits the instruction its outline was planned under when this is omitted."
    },
    "sourceMode": {
      "type": "string",
      "enum": [
        "off",
        "facts",
        "cited"
      ],
      "description": "Competitor sourcing for the article (UI default off). off still grounds the text on the facts bank the outline was built on; facts/cited additionally scrape live SERP competitors — slower."
    },
    "includeToc": {
      "type": "boolean",
      "description": "Insert a table-of-contents block after H1 (default false)."
    },
    "targetWordCount": {
      "type": "number",
      "description": "Target article length in words — sets outline section budgets and drives the volume guard."
    },
    "temperature": {
      "type": "number",
      "description": "Sampling temperature; omit for the provider default. The outline phase caps it at 0.8 (JSON reliability)."
    },
    "bannedWords": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Words the model must not use — the AI-Fingerprint Lab's marker export goes here."
    },
    "chunkSections": {
      "type": "number",
      "description": "type=text: how many sections one writing call covers (2–5, default 5). Lower it only when a page keeps losing a rule the instruction demonstrably carries — each step down adds provider calls, which is what a rate limit counts."
    },
    "forbiddenBrands": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "type=text: names that must not appear in the body. Checked deterministically after writing and repaired in one scoped pass; with sourceMode=facts the source domains are used automatically and this only adds to them."
    },
    "judge": {
      "type": "boolean",
      "description": "Independent QA pass on the finished result (default true): a fresh-context model call — on the per-task 'judge' slot, which can be a DIFFERENT model than the writer — checks a finished article is complete and publishable (rejects truncated stubs, planning notes, wrong language) and an outline actually covers the keyword, before anything is saved as completed."
    },
    "marksScrub": {
      "type": "boolean",
      "description": "type=text: strip invisible Unicode marks from the finished article — zero-width spaces, bidi controls, soft hyphens, exotic spaces (default true). Reported in the result as `marksScrub` when anything was found."
    },
    "payload": {
      "type": "object",
      "description": "Pipeline payload, the same shape the /seo-tools UI posts — e.g. { competitors, paa, related } for outline, { gl, hl, keywords } for cluster, { generate } for landing. The common knobs above are top-level arguments; payload wins when both are given."
    },
    "policyName": {
      "type": "string",
      "description": "Editorial policy to write under, by name. Omit to use the instance's active policy — it is applied either way."
    }
  },
  "required": [
    "confirm",
    "type"
  ]
}
```

</details>

- Registry cost is paid; dispatcher requires workspace spend permission. Handler confirmation/estimate/cache paths determine whether this call actually spends credits.

Source: [src/lib/mcp/toolsOptimize.ts:451](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsOptimize.ts#L451-L679) · [src/lib/mcp/shared.ts:1](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/shared.ts#L1-L373).

## get_generation_job

Mark stale jobs failed and read the selected generation job/status/result.

<details>
<summary>Full registered description</summary>

```text
FREE: check a background job started by start_generation_job or start_rewrite_job — status, progress, and the result. A finished text job also reports `needsAttention`: page-mechanics defects found deterministically after writing and NOT fixable automatically (a competitor named on a page told not to name one, a dropped [[PLACEHOLDER]], a missing internal link, a price in the wrong currency). Read it before publishing — the prose being good says nothing about these. Rewrite batches report per-page progress and return finished pages as they complete, so polling early gives partial work rather than nothing; pass includeContent to get the rewritten text itself. Jobs silent for over 20 minutes are reported as timed out (the process restarted mid-run). On error, the message carries the provider's own reason, including content-policy rejections.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `jobId` | No | string | Not declared |
| `includeContent` | No | boolean | Not declared |
| `page` | No | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "jobId": {
      "type": "string",
      "description": "The id returned by start_generation_job / start_rewrite_job. Omit to list recent jobs."
    },
    "includeContent": {
      "type": "boolean",
      "description": "For rewrite batches: include each page's full rewritten text (default false — the summary alone is usually what you want, and 20 articles is a lot to read at once)"
    },
    "page": {
      "type": "string",
      "description": "For rewrite batches: return just this one page's full result (URL or substring)"
    }
  }
}
```

</details>

- Actual handler can mutate local state, but dispatcher defaults this non-paid registration to readOnlyHint:true and read permission.

Source: [src/lib/mcp/toolsOptimize.ts:681](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsOptimize.ts#L681-L790) · [src/lib/mcp/shared.ts:1](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/shared.ts#L1-L373).

## list_outreach_prospects

Read saved outreach prospects and pipeline statistics through listOutreach.

<details>
<summary>Full registered description</summary>

```text
List the owner's Outreach Workspace campaigns, prospects, evidence snapshots, stages, follow-up dates and won-link state. LOCAL/READ-ONLY: no network request and no message is sent.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `stage` | No | string | Not declared |
| `campaignId` | No | string | Not declared |
| `limit` | No | number | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "stage": {
      "type": "string",
      "enum": [
        "discovered",
        "qualified",
        "ready",
        "contacted",
        "replied",
        "negotiating",
        "won",
        "lost"
      ],
      "description": "Optional pipeline-stage filter"
    },
    "campaignId": {
      "type": "string",
      "description": "Optional Outreach campaign id. Use list_outreach_prospects to discover ids."
    },
    "limit": {
      "type": "number",
      "description": "Maximum prospects returned (default 100, max 500)"
    }
  }
}
```

</details>

Source: [src/lib/mcp/toolsOutreach.ts:20](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsOutreach.ts#L20-L41) · [src/lib/outreach/types.ts:1](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/outreach/types.ts#L1-L37).

## save_outreach_prospect

Save an outreach prospect in the local store.

<details>
<summary>Full registered description</summary>

```text
Save one publisher domain or Link Monitor source URL as an Outreach prospect. Existing evidence is snapshotted and saving the same domain again returns the existing row. LOCAL WRITE ONLY: never fetches the web, spends credits or sends a message.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `domain` | No | string | Not declared |
| `sourceUrl` | No | string | Not declared |
| `campaignId` | No | string | Not declared |
| `targetAsset` | No | string | Not declared |
| `pitchAngle` | No | string | Not declared |
| `notes` | No | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "domain": {
      "type": "string",
      "description": "Publisher domain, for example publisher.com"
    },
    "sourceUrl": {
      "type": "string",
      "description": "Optional existing Link Monitor evidence URL (http/https)"
    },
    "campaignId": {
      "type": "string",
      "description": "Optional Outreach campaign id. Use list_outreach_prospects to discover ids."
    },
    "targetAsset": {
      "type": "string",
      "description": "Page or asset you may pitch"
    },
    "pitchAngle": {
      "type": "string",
      "description": "Internal value proposition; not sent automatically"
    },
    "notes": {
      "type": "string",
      "description": "Private operator notes"
    }
  },
  "anyOf": [
    {
      "required": [
        "domain"
      ]
    },
    {
      "required": [
        "sourceUrl"
      ]
    }
  ]
}
```

</details>

Source: [src/lib/mcp/toolsOutreach.ts:42](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsOutreach.ts#L42-L62).

## update_outreach_prospect

Update the prospect’s local pipeline fields through updateOutreachProspect.

<details>
<summary>Full registered description</summary>

```text
Update an existing Outreach prospect's stage, contact research, follow-up, campaign, pitch notes or won backlink. Stage changes are recorded in local history. LOCAL WRITE ONLY: does not contact the publisher or run an audit.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `id` | Yes | string | Not declared |
| `stage` | No | string | Not declared |
| `campaignId` | No | string | Not declared |
| `contactName` | No | string | Not declared |
| `contactEmail` | No | string | Not declared |
| `contactUrl` | No | string | Not declared |
| `contactSource` | No | string | Not declared |
| `targetAsset` | No | string | Not declared |
| `pitchAngle` | No | string | Not declared |
| `notes` | No | string | Not declared |
| `nextFollowUpAt` | No | string or null | Not declared |
| `lastContactAt` | No | string or null | Not declared |
| `backlinkId` | No | string or null | Not declared |
| `wonBacklinkUrl` | No | string | Not declared |
| `stageNote` | No | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "id": {
      "type": "string",
      "description": "Prospect id from list_outreach_prospects"
    },
    "stage": {
      "type": "string",
      "enum": [
        "discovered",
        "qualified",
        "ready",
        "contacted",
        "replied",
        "negotiating",
        "won",
        "lost"
      ]
    },
    "campaignId": {
      "type": "string",
      "description": "Campaign id, or null to remove the prospect from a campaign"
    },
    "contactName": {
      "type": "string"
    },
    "contactEmail": {
      "type": "string"
    },
    "contactUrl": {
      "type": "string"
    },
    "contactSource": {
      "type": "string"
    },
    "targetAsset": {
      "type": "string"
    },
    "pitchAngle": {
      "type": "string"
    },
    "notes": {
      "type": "string"
    },
    "nextFollowUpAt": {
      "type": [
        "string",
        "null"
      ],
      "description": "ISO date/time, or null to clear"
    },
    "lastContactAt": {
      "type": [
        "string",
        "null"
      ],
      "description": "ISO date/time, or null to clear"
    },
    "backlinkId": {
      "type": [
        "string",
        "null"
      ],
      "description": "Optional Backlink row owned by this user"
    },
    "wonBacklinkUrl": {
      "type": "string",
      "description": "Optional verified/manual won backlink URL"
    },
    "stageNote": {
      "type": "string",
      "description": "Optional note stored with a stage transition"
    }
  },
  "required": [
    "id"
  ]
}
```

</details>

Source: [src/lib/mcp/toolsOutreach.ts:63](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsOutreach.ts#L63-L96) · [src/lib/outreach/types.ts:1](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/outreach/types.ts#L1-L37).

## create_outreach_campaign

Create a local outreach campaign.

<details>
<summary>Full registered description</summary>

```text
Create a local Outreach campaign for grouping prospects and measuring won links. This only stores workspace data; it never launches or sends a campaign.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `name` | Yes | string | Not declared |
| `targetAsset` | No | string | Not declared |
| `notes` | No | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string",
      "description": "Unique campaign name"
    },
    "targetAsset": {
      "type": "string",
      "description": "Page or asset this campaign promotes"
    },
    "notes": {
      "type": "string",
      "description": "Private operator notes"
    }
  },
  "required": [
    "name"
  ]
}
```

</details>

Source: [src/lib/mcp/toolsOutreach.ts:97](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsOutreach.ts#L97-L114).

## get_source_audit

Read saved source audit runs and optionally filter findings by severity.

<details>
<summary>Full registered description</summary>

```text
Read stored Source Audit runs: score, severity counters, per-finding rule id, file path, line, evidence and confidence, plus whether the snapshot was truncated. LOCAL/READ-ONLY: reads this instance's database only — it does not contact GitHub, start an audit, or modify code. Site Audit, AI Visibility and GEO are separate tools with their own data.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `repositoryId` | No | string | Not declared |
| `runId` | No | string | Not declared |
| `severity` | No | string | Not declared |
| `limit` | No | number | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "repositoryId": {
      "type": "string",
      "description": "Optional Content Operations repository id"
    },
    "runId": {
      "type": "string",
      "description": "Optional specific run id; defaults to the most recent runs"
    },
    "severity": {
      "type": "string",
      "enum": [
        "error",
        "warning",
        "info"
      ],
      "description": "Optional severity filter applied to findings"
    },
    "limit": {
      "type": "number",
      "description": "Maximum runs returned (default 5, max 20)"
    }
  }
}
```

</details>

Source: [src/lib/mcp/toolsSourceAudit.ts:12](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsSourceAudit.ts#L12-L45).

## drops_list

Read candidate-domain catalogue rows and stage counts.

<details>
<summary>Full registered description</summary>

```text
List the expired-domain catalogue (/drops): candidates with stage, DR, refdomains, Majestic TF/CF, group, Wayback snapshots, score, hard veto (spam_history | idle_over_2y | dr_drop | pbn_profile — a veto caps the score at 0 and means 'do not buy') and AI history verdict. Filters: runId, stage, tld, q (domain substring), starred, watched, groupId / ungrouped, minScore, noVeto (the buyable cut — only rows where nothing fired), and inclusive numeric ranges — drMin/drMax (drNull=true for rows never rated — a different thing from DR 0), refMin/refMax on the displayed refdomain count, tfMin/tfMax on Majestic Trust Flow; sorted page. Returns the funnel stage counts alongside, so one call answers 'what does the catalogue look like'.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `stage` | No | string | Not declared |
| `runId` | No | string | Not declared |
| `tld` | No | string | Not declared |
| `q` | No | string | Not declared |
| `starred` | No | boolean | Not declared |
| `watched` | No | boolean | Not declared |
| `minScore` | No | number | Not declared |
| `drMin` | No | number | Not declared |
| `drMax` | No | number | Not declared |
| `drNull` | No | boolean | Not declared |
| `refMin` | No | number | Not declared |
| `refMax` | No | number | Not declared |
| `tfMin` | No | number | Not declared |
| `tfMax` | No | number | Not declared |
| `noVeto` | No | boolean | Not declared |
| `history` | No | string | Not declared |
| `groupId` | No | string | Not declared |
| `ungrouped` | No | boolean | Not declared |
| `limit` | No | number | Not declared |
| `offset` | No | number | Not declared |
| `orderBy` | No | string | Not declared |
| `order` | No | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "stage": {
      "type": "string",
      "description": "funnel stage, one of: ingested, dns_checked, no_registry, resolved_taken, checking, available, taken, confirmed, rejected, acquired"
    },
    "runId": {
      "type": "string",
      "description": "restrict to one import run"
    },
    "tld": {
      "type": "string",
      "description": "zone without the dot, e.g. gr"
    },
    "q": {
      "type": "string",
      "description": "domain substring"
    },
    "starred": {
      "type": "boolean"
    },
    "watched": {
      "type": "boolean",
      "description": "only rows the watch loop is polling"
    },
    "minScore": {
      "type": "number"
    },
    "drMin": {
      "type": "number",
      "description": "minimum DR, inclusive — e.g. 10 for 'DR ≥ 10'"
    },
    "drMax": {
      "type": "number",
      "description": "maximum DR, inclusive — e.g. 5 for the garbage band 0–5"
    },
    "drNull": {
      "type": "boolean",
      "description": "true = only rows with no DR yet (never enriched, or Ahrefs has no rating); independent of drMin/drMax"
    },
    "refMin": {
      "type": "number",
      "description": "minimum referring domains, inclusive (dofollow when known, total otherwise)"
    },
    "refMax": {
      "type": "number",
      "description": "maximum referring domains, inclusive"
    },
    "tfMin": {
      "type": "number",
      "description": "minimum Majestic Trust Flow, inclusive"
    },
    "tfMax": {
      "type": "number",
      "description": "maximum Majestic Trust Flow, inclusive"
    },
    "noVeto": {
      "type": "boolean",
      "description": "true = only rows with no hard veto (the buyable cut); veto values: spam_history, idle_over_2y, dr_drop (DR fell ≥5 in the monthly series), pbn_profile (TF far below DR)"
    },
    "history": {
      "type": "string",
      "description": "history verdict filter: clean | empty | suspicious | toxic (the free classifier) or none (never classified). historyScore in the row is parsed from the note"
    },
    "groupId": {
      "type": "string",
      "description": "only rows in this curated group (see drops_groups)"
    },
    "ungrouped": {
      "type": "boolean",
      "description": "true = only rows in no group"
    },
    "limit": {
      "type": "number",
      "description": "rows per page, default 50, max 200"
    },
    "offset": {
      "type": "number"
    },
    "orderBy": {
      "type": "string",
      "description": "one of: score, createdAt, domain, dr, refdomains, snapshots, checkedAt, tf, history (default score)"
    },
    "order": {
      "type": "string",
      "description": "asc | desc (default desc)"
    }
  }
}
```

</details>

Source: [src/lib/mcp/toolsDrops.ts:99](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsDrops.ts#L99-L169).

## drops_ingest

Create a drop-domain ingestion run from supplied source rows.

<details>
<summary>Full registered description</summary>

```text
Import a list of domains into the drops catalogue as a new run. `raw` is pasted text or CSV — URLs, www.-prefixed hosts, IPs and junk rows are normalised or rejected with a per-reason report (rows reduce to their registrable apex). Returns accepted/inserted/duplicated counts.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `raw` | Yes | string | Not declared |
| `label` | No | string | Not declared |
| `source` | No | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "required": [
    "raw"
  ],
  "properties": {
    "raw": {
      "type": "string",
      "description": "the list itself: one domain per line or a CSV (the first domain-like column wins)"
    },
    "label": {
      "type": "string",
      "description": "human label for the run"
    },
    "source": {
      "type": "string",
      "description": "one of: csv, ahrefs_refdomains, ahrefs_broken, crawler, zone_diff (default csv)"
    }
  }
}
```

</details>

- Actual handler can mutate local state, but dispatcher defaults this non-paid registration to readOnlyHint:true and read permission.

Source: [src/lib/mcp/toolsDrops.ts:171](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsDrops.ts#L171-L196).

## drops_prefilter

DNS-check pending candidates in batches and persist DNS results.

<details>
<summary>Full registered description</summary>

```text
Run one bounded slice of the DNS pre-filter on ingested rows: resolves NS records and retires every delegated (alive) domain for free, advancing the rest to the registry stage. Returns { checked, retired, advanced, remaining, done } — call repeatedly while remaining > 0 and done is false. The free stage that should always run first.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `runId` | No | string | Not declared |
| `batch` | No | number | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "runId": {
      "type": "string"
    },
    "batch": {
      "type": "number",
      "description": "rows this slice, default 200, max 1000"
    }
  }
}
```

</details>

- Actual handler can mutate local state, but dispatcher defaults this non-paid registration to readOnlyHint:true and read permission.

Source: [src/lib/mcp/toolsDrops.ts:198](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsDrops.ts#L198-L227).

## drops_check

Perform registry/availability checks for pending candidates and persist availability results.

<details>
<summary>Full registered description</summary>

```text
Run one bounded slice of the registry availability check (RDAP then WHOIS, throttled per zone, ~35s wall-clock budget). Returns { checked, available, taken, deferred, uncheckable, remaining, done }: call repeatedly while remaining > 0 and done is false. `uncheckable` counts rows whose zone has no public registry (e.g. .gr) — those need a registrar API and are parked for a week. An `available` verdict must be corroborated=true before it is treated as free.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `runId` | No | string | Not declared |
| `batch` | No | number | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "runId": {
      "type": "string"
    },
    "batch": {
      "type": "number",
      "description": "rows per slice, default 40, max 200"
    }
  }
}
```

</details>

- Actual handler can mutate local state, but dispatcher defaults this non-paid registration to readOnlyHint:true and read permission.

Source: [src/lib/mcp/toolsDrops.ts:229](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsDrops.ts#L229-L270).

## drops_enrich_wayback

Fetch Wayback profiles for candidate domains and persist snapshot/history summaries.

<details>
<summary>Full registered description</summary>

```text
Fetch Wayback Machine snapshots for up to 12 domains: months archived, first/last seen, days since death. Free and keyless. Writes into the catalogue and updates the score (stale domains get vetoed down).
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `domains` | Yes | array of string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "required": [
    "domains"
  ],
  "properties": {
    "domains": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "up to 12 domains"
    }
  }
}
```

</details>

- Actual handler can mutate local state, but dispatcher defaults this non-paid registration to readOnlyHint:true and read permission.

Source: [src/lib/mcp/toolsDrops.ts:272](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsDrops.ts#L272-L305).

## drops_enrich_dr

Fetch configured DR enrichment and write metrics/snapshots to local candidate history.

<details>
<summary>Full registered description</summary>

```text
Fetch Ahrefs Domain Rating for up to 60 domains through the free public endpoint (needs the free Ahrefs DR key in Settings → SEO Metrics, or falls back to the paid Ahrefs key; 7-day server cache). Every fresh rating also lands in the panel's own monthly DR history (DrSnapshot), and the response carries each domain's accumulated series with a penalty flag (a fall of ≥5 points across the window reads as a Google filter, not lost links). Attribution required when displayed: 'Domain Rating by Ahrefs'.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `domains` | Yes | array of string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "required": [
    "domains"
  ],
  "properties": {
    "domains": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "up to 60 domains"
    }
  }
}
```

</details>

- Actual handler can mutate local state, but dispatcher defaults this non-paid registration to readOnlyHint:true and read permission.

Source: [src/lib/mcp/toolsDrops.ts:307](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsDrops.ts#L307-L337).

## drops_enrich_refdomains

Require confirmation and provider settings/capacity, fetch domain metrics, record usage and persist candidate metrics.

<details>
<summary>Full registered description</summary>

```text
PAID: fetch Ahrefs refdomains/backlink counts for up to 25 domains through the configured metrics provider — spends the owner's Ahrefs units (~100 units per domain, the 50-unit floor doubled). Do not run for the whole catalogue; run for shortlisted rows. Needs confirm: true.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `domains` | Yes | array of string | Not declared |
| `confirm` | Yes | boolean | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "required": [
    "domains",
    "confirm"
  ],
  "properties": {
    "domains": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "up to 25 shortlisted domains"
    },
    "confirm": {
      "type": "boolean",
      "description": "must be true — this spends Ahrefs units"
    }
  }
}
```

</details>

- Registry cost is paid; dispatcher requires workspace spend permission. Handler confirmation/estimate/cache paths determine whether this call actually spends credits.

Source: [src/lib/mcp/toolsDrops.ts:339](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsDrops.ts#L339-L391).

## drops_enrich_tf

Require confirmation, call Majestic item statistics, record usage and persist trust/citation-flow metrics.

<details>
<summary>Full registered description</summary>

```text
PAID: fetch Majestic Trust Flow / Citation Flow for up to 100 domains in one batched GetIndexItemInfo call — the cheapest meaningful enrichment (1 Majestic unit per domain, i.e. well under a cent each) and the read a DR number cannot replace: TF catches a PBN-heavy profile DR is happy with. Writes majesticTf/majesticCf onto the rows; drops_list can then filter and sort by TF. Needs confirm: true.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `domains` | Yes | array of string | Not declared |
| `confirm` | Yes | boolean | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "required": [
    "domains",
    "confirm"
  ],
  "properties": {
    "domains": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "up to 100 domains — the call is batched, so this is cheap even at the ceiling"
    },
    "confirm": {
      "type": "boolean",
      "description": "must be true — this spends Majestic units"
    }
  }
}
```

</details>

- Registry cost is paid; dispatcher requires workspace spend permission. Handler confirmation/estimate/cache paths determine whether this call actually spends credits.

Source: [src/lib/mcp/toolsDrops.ts:393](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsDrops.ts#L393-L441).

## drops_groups

List/create/rename/delete local drop groups or assign candidate domains to a group according to action.

<details>
<summary>Full registered description</summary>

```text
Curated groups over the drops catalogue — name a batch of domains once ('buy in October', 'defer'), then work with it as a unit; the /drops table renders them as collapsible sections. Actions: list (default — groups with row counts), create {name}, rename {groupId, name}, delete {groupId} (rows stay in the catalogue, ungrouped), assign {groupId, ids | filter}, unassign {ids | filter}. ids are row ids from drops_list; filter is the same filter dict drops_list takes (stage, runId, tld, q, drMin/drMax/drNull, refMin/refMax, tfMin/tfMax, groupId, ungrouped, watched, starred) — so 'put everything with DR < 10 into a group' is one call.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `action` | No | string | Not declared |
| `name` | No | string | Not declared |
| `groupId` | No | string | Not declared |
| `ids` | No | array of string | Not declared |
| `filter` | No | object | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "action": {
      "type": "string",
      "description": "list (default) | create | rename | delete | assign | unassign"
    },
    "name": {
      "type": "string",
      "description": "group name (create/rename)"
    },
    "groupId": {
      "type": "string",
      "description": "target group (rename/delete/assign)"
    },
    "ids": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "row ids (assign/unassign), max 500"
    },
    "filter": {
      "type": "object",
      "description": "drops_list-shaped filter (assign/unassign) — bulk over the whole filtered set"
    }
  }
}
```

</details>

- Actual handler can mutate local state, but dispatcher defaults this non-paid registration to readOnlyHint:true and read permission.

Source: [src/lib/mcp/toolsDrops.ts:443](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsDrops.ts#L443-L494).

## drops_dr_history

Read stored DR history; optionally fetch paid provider history with confirmation and persist snapshots.

<details>
<summary>Full registered description</summary>

```text
Domain Rating history for one domain — the DR series by month, not the snapshot. Free first: when the panel has accumulated a local series (DrSnapshot, 2+ months — filled automatically by every fresh DR check and by the watch loop once a month), it is returned at no cost with source:'local', no key and no confirm needed. Otherwise it fetches via GoAnyAPI at 2 credits per returned month (includeDr=false = free preview of which months exist) and stores the fetched months locally, so the series never costs twice. A DR series is a veto signal a single number cannot be: 22→24→12→11→8 is not lost links, it is a hit — read a drop of ≥5 points as a spam/penalty flag before acquiring. Pass vendor:true to force the GoAnyAPI window even when a local series exists. Needs confirm: true for the paid variant.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `domain` | Yes | string | Not declared |
| `vendor` | No | boolean | Not declared |
| `confirm` | No | boolean | Not declared |
| `includeDr` | No | boolean | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "required": [
    "domain"
  ],
  "properties": {
    "domain": {
      "type": "string",
      "description": "One domain to inspect"
    },
    "vendor": {
      "type": "boolean",
      "description": "Skip the free local series and fetch the full GoAnyAPI window (2 credits/month)"
    },
    "confirm": {
      "type": "boolean",
      "description": "must be true for the paid GoAnyAPI fetch; the local series needs neither key nor confirm"
    },
    "includeDr": {
      "type": "boolean",
      "description": "Fetch DR values (default: follows confirm)"
    }
  }
}
```

</details>

- Registry cost is paid; dispatcher requires workspace spend permission. Handler confirmation/estimate/cache paths determine whether this call actually spends credits.

Source: [src/lib/mcp/toolsDrops.ts:496](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsDrops.ts#L496-L573).

## drops_history_ai

Require confirmation, obtain Wayback timestamps and use configured AI to analyze domain history; save verdicts.

<details>
<summary>Full registered description</summary>

```text
PAID: run the AI history pass over hand-picked domains (up to 25 per call) — fetches three Wayback snapshots across the domain's life and asks the configured LLM what the site was about, whether the topic shifted and whether a spam period shows. Writes historyVerdict (clean | topic_shift | spam_period | unknown) + a factual note, and re-scores the row (spam_period vetoes). Domains run sequentially, several seconds each — a full list takes minutes. Uses the dedicated drops-history AI slot (Settings → per-task AI) and falls back to the main AI provider; an explicit aiProvider/aiApiKey argument wins over both. Needs confirm: true — it spends LLM credits. Still a vetting tool for shortlists, not a bulk sweep over whole runs.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `domains` | Yes | array of string | Not declared |
| `confirm` | Yes | boolean | Not declared |
| `aiProvider` | No | string | Not declared |
| `aiApiKey` | No | string | Not declared |
| `model` | No | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "required": [
    "domains",
    "confirm"
  ],
  "properties": {
    "domains": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "up to 25 hand-picked domains"
    },
    "confirm": {
      "type": "boolean",
      "description": "must be true — this spends LLM credits"
    },
    "aiProvider": {
      "type": "string",
      "description": "override the AI provider for this call"
    },
    "aiApiKey": {
      "type": "string",
      "description": "override the AI key for this call"
    },
    "model": {
      "type": "string",
      "description": "override the model for this call"
    }
  }
}
```

</details>

- Registry cost is paid; dispatcher requires workspace spend permission. Handler confirmation/estimate/cache paths determine whether this call actually spends credits.

Source: [src/lib/mcp/toolsDrops.ts:575](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsDrops.ts#L575-L633).

## drops_toxicity

Run a network-fetching toxicity slice and save resulting candidate classification.

<details>
<summary>Full registered description</summary>

```text
Run one bounded slice of the FREE toxicity classifier over the catalogue — the same slice the /drops button runs (historyVerdict: clean | empty | suspicious | toxic written in shadow mode; score and veto untouched unless the arm flag is on). Sources in order: topAnchors already on the row (anchorsOnly: true = the whole catalogue with ZERO network requests), then a Wayback walk (CDX + up to N snapshots per domain through the proxy pool's web.archive.org zone). 429/503 from the archive is never a verdict — the row sits out 6h and is listed in skipped. Returns { checked, toxic, suspicious, clean, empty, remaining, done, skipped } — call repeatedly while remaining > 0.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `domains` | No | array of string | Not declared |
| `filter` | No | object | Not declared |
| `snapshots` | No | number | Not declared |
| `anchorsOnly` | No | boolean | Not declared |
| `runId` | No | string | Not declared |
| `batch` | No | number | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "domains": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "up to 25 explicit domains"
    },
    "filter": {
      "type": "object",
      "description": "drops_list-shaped filter, alternative to domains"
    },
    "snapshots": {
      "type": "number",
      "description": "snapshots per domain, 1..5, default 3"
    },
    "anchorsOnly": {
      "type": "boolean",
      "description": "true = classify by topAnchors + name scan only, no network at all"
    },
    "runId": {
      "type": "string"
    },
    "batch": {
      "type": "number",
      "description": "rows this slice, default 8 (25 with anchorsOnly)"
    }
  }
}
```

</details>

- Actual handler can mutate local state, but dispatcher defaults this non-paid registration to readOnlyHint:true and read permission.

Source: [src/lib/mcp/toolsDrops.ts:635](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsDrops.ts#L635-L666).

## glue_plan

Build a deterministic local domain-to-target glue plan from supplied data.

<details>
<summary>Full registered description</summary>

```text
Build the hreflang/canonical annotation blocks that glue a dropped domain to a money site — the generator behind the «Склейка» card on /drops?tab=activation. One cluster, one mode: 'cluster' (mutual, each page canonical to itself — nothing merges, nothing falls off) or 'funnel' (every canonical points at the drop — signals merge into it, and the drop's owner controls your rankings; that trade-off is the scheme's whole point). Returns per-page <html lang>, canonical, the shared alternate set (self-reference included — without it Google drops the group) and a ready-to-paste <head> block. Notes (locale_fixed, locale_duplicate, url_not_absolute, …) come back verbatim: they say exactly what was corrected in the input.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `mode` | Yes | string | Not declared |
| `dropUrl` | Yes | string | Not declared |
| `alternates` | Yes | array of object | Not declared |
| `xDefault` | No | string | Not declared |
| `dropHtmlLang` | No | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "required": [
    "mode",
    "dropUrl",
    "alternates"
  ],
  "properties": {
    "mode": {
      "type": "string",
      "description": "cluster | funnel"
    },
    "dropUrl": {
      "type": "string",
      "description": "the drop, absolute URL"
    },
    "alternates": {
      "type": "array",
      "items": {
        "type": "object"
      },
      "description": "[{ hreflang, url }] — locales and their money-page URLs"
    },
    "xDefault": {
      "type": "string",
      "description": "x-default target, defaults to the drop"
    },
    "dropHtmlLang": {
      "type": "string",
      "description": "<html lang> for the drop page, defaults to the first locale's language"
    }
  }
}
```

</details>

Source: [src/lib/mcp/toolsDrops.ts:668](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsDrops.ts#L668-L700).

## glue_check

Fetch source/target cluster pages and compute the glue-check report.

<details>
<summary>Full registered description</summary>

```text
Check a LIVE glue cluster: fetches every page (safeFetch, manual redirects, ≤5 hops), parses canonical/alternate/noindex from the final response and runs the validator — reciprocity, self-reference, x-default, dead or noindex targets, and with a plan also a live-vs-plan diff (a swapped canonical on your money page). ua: 'both' adds the Googlebot pass and flags cloaked_annotations when browser and bot see different annotations. LIMITATION you must carry into any conclusion: the UA diff only catches User-Agent-based cloaking. Serious setups cloak by IP with reverse-DNS verification — a Googlebot-UA request from a foreign address gets the plain page, so an EMPTY cloaked_annotations finding does NOT prove the absence of cloaking.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `mode` | Yes | string | Not declared |
| `urls` | Yes | array of string | Not declared |
| `plan` | No | object | Not declared |
| `ua` | No | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "required": [
    "mode",
    "urls"
  ],
  "properties": {
    "mode": {
      "type": "string",
      "description": "cluster | funnel (in funnel, hreflang→non-canonical is info, not a blocker — that IS the mechanism)"
    },
    "urls": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "up to 10 absolute URLs, both sides of the cluster"
    },
    "plan": {
      "type": "object",
      "description": "the glue_plan output — when present, live pages are also diffed against it"
    },
    "ua": {
      "type": "string",
      "description": "browser (default) | googlebot | both"
    }
  }
}
```

</details>

Source: [src/lib/mcp/toolsDrops.ts:702](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsDrops.ts#L702-L742).

## drops_watch

Read the watchlist or toggle watched state for selected candidate domains; scheduler performs subsequent checks.

<details>
<summary>Full registered description</summary>

```text
Watch taken (registered) domains from the catalogue and get told when one becomes free. Watched rows are re-checked by the in-app scheduler (default daily; 15 min once the registry reports pendingDelete, 60 min on redemptionPeriod); a corroborated free verdict sends ONE Telegram/Slack notification (Settings → Notifications) and ends that watch — an uncorroborated one is silently re-checked within the hour instead. Rows must have passed the funnel's DNS + registry stages to be watched meaningfully. `watch: true` makes rows due immediately; without `watch`, returns the current watchlist with the count.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `watch` | No | boolean | Not declared |
| `domains` | No | array of string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "watch": {
      "type": "boolean",
      "description": "true = start watching, false = stop watching; omit to list"
    },
    "domains": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "domains to (un)watch, max 200"
    }
  }
}
```

</details>

- Actual handler can mutate local state, but dispatcher defaults this non-paid registration to readOnlyHint:true and read permission.

Source: [src/lib/mcp/toolsDrops.ts:744](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsDrops.ts#L744-L776).

## serpmon_projects

Read SERP-monitor projects, counts and recent run summaries.

<details>
<summary>Full registered description</summary>

```text
List SERP Monitor projects (/serp-monitor). A project is one market — engine, country, language, device — plus a keyword set; every run snapshots the whole top-100 per keyword and diffs are computed per host. Each row carries the keyword count, last/next run, the latest run's summary (including its storm verdict) and the volatility series of the last 30 runs, so one call answers 'which markets are quiet and which are shaking'.
```

</details>

No named input parameters are declared.

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {}
}
```

</details>

Source: [src/lib/mcp/toolsSerpMon.ts:27](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsSerpMon.ts#L27-L37).

## serpmon_market

Read stored project market rows with host-level changes and volatility.

<details>
<summary>Full registered description</summary>

```text
The market table of one SERP Monitor project: per keyword the current leaders (`leaders` skips platform and ignored hosts, `leadersAll` keeps them), the changes since its last comparable snapshot, RBO volatility and the project's own position. Two facts hold everywhere in this module: changes are HOST-level (a host has one best position and one change — `urls` is a side count, not one entry per URL), and a `failed` snapshot never enters a comparison — a burned proxy cannot fake mass exits. Comparison always runs against the previous snapshot with status ok or partial, within their common depth. Filters: q (keyword substring), host, group, changed_only, sort (keyword | volatility | changes), page, limit ≤ 200.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `project_id` | Yes | string | Not declared |
| `q` | No | string | Not declared |
| `host` | No | string | Not declared |
| `group` | No | string | Not declared |
| `changed_only` | No | boolean | Not declared |
| `sort` | No | string | Not declared |
| `page` | No | number | Not declared |
| `limit` | No | number | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "required": [
    "project_id"
  ],
  "properties": {
    "project_id": {
      "type": "string",
      "description": "project id from serpmon_projects"
    },
    "q": {
      "type": "string",
      "description": "keyword substring filter"
    },
    "host": {
      "type": "string",
      "description": "only keywords whose latest snapshot contains this host"
    },
    "group": {
      "type": "string",
      "description": "only keywords in this import group"
    },
    "changed_only": {
      "type": "boolean",
      "description": "only keywords whose latest comparison had visible host changes"
    },
    "sort": {
      "type": "string",
      "description": "one of: keyword, volatility, changes (default keyword)"
    },
    "page": {
      "type": "number",
      "description": "1-based page"
    },
    "limit": {
      "type": "number",
      "description": "rows per page, default 50, max 200"
    }
  }
}
```

</details>

Source: [src/lib/mcp/toolsSerpMon.ts:39](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsSerpMon.ts#L39-L73).

## serpmon_keyword_history

Read saved keyword SERP snapshots and host-position history.

<details>
<summary>Full registered description</summary>

```text
Full SERP history of one keyword inside a SERP Monitor project: every snapshot with its status (ok | partial | failed), problem code, depth, rows fetched, volatility and change count, plus the position series of the ≤ 10 hosts with the most presence aligned to those snapshots. Failed snapshots are kept in the history (with their problem) but sit outside every comparison. Get keyword ids from serpmon_market.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `keyword_id` | Yes | string | Not declared |
| `limit` | No | number | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "required": [
    "keyword_id"
  ],
  "properties": {
    "keyword_id": {
      "type": "string",
      "description": "keywordId from serpmon_market rows"
    },
    "limit": {
      "type": "number",
      "description": "snapshots to return, newest first, default 30, max 200"
    }
  }
}
```

</details>

Source: [src/lib/mcp/toolsSerpMon.ts:75](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsSerpMon.ts#L75-L95).

## serpmon_storms

Read project runs and stored storm/calibration verdicts.

<details>
<summary>Full registered description</summary>

```text
Recent runs of one SERP Monitor project with their storm verdicts: per run the ok/partial/failed counters, how many keywords were compared, median volatility, share of keywords above their own usual churn, and the storm verdict — a robust z-score of this run's volatility against the project's OWN baseline (a gambling market runs hotter than a boring one; nothing is absolute), storm=true from z ≥ 3 plus ≥ 30% of keywords above their own p90. The first runs (< 7 done runs) are calibration: no verdict is given yet, 'calibrating' — not 'no storms'. Storm detection is a property of a finished run; failed snapshots inside it never produce exits. Also the way to follow a run started with serpmon_run, which is asynchronous.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `project_id` | Yes | string | Not declared |
| `limit` | No | number | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "required": [
    "project_id"
  ],
  "properties": {
    "project_id": {
      "type": "string",
      "description": "project id from serpmon_projects"
    },
    "limit": {
      "type": "number",
      "description": "runs to return, newest first, default 30, max 200"
    }
  }
}
```

</details>

Source: [src/lib/mcp/toolsSerpMon.ts:97](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsSerpMon.ts#L97-L121).

## serpmon_domains

Read stored domain catalogue/filter results for a SERP-monitor project.

<details>
<summary>Full registered description</summary>

```text
The domain catalogue of one SERP Monitor project: who holds how many keywords and at what best/average position, who is rising or falling run-over-run, who is new (first seen after the project's first run), young (registered < N months ago), bounced (entered and exited within 7 runs), platform or the project's own domain — with registration age and DR where the enrichment has run. Presets like the UI: all, new, young, rising, falling, bounced. Counts are per host, the same host-level convention as every SERP Monitor surface.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `project_id` | Yes | string | Not declared |
| `preset` | No | string | Not declared |
| `q` | No | string | Not declared |
| `max_age_months` | No | number | Not declared |
| `include_platforms` | No | boolean | Not declared |
| `sort` | No | string | Not declared |
| `page` | No | number | Not declared |
| `limit` | No | number | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "required": [
    "project_id"
  ],
  "properties": {
    "project_id": {
      "type": "string",
      "description": "project id from serpmon_projects"
    },
    "preset": {
      "type": "string",
      "description": "one of: all, new, young, rising, falling, bounced (default all)"
    },
    "q": {
      "type": "string",
      "description": "host substring filter"
    },
    "max_age_months": {
      "type": "number",
      "description": "young cutoff in months (default 6)"
    },
    "include_platforms": {
      "type": "boolean",
      "description": "include social networks / app stores / wikipedia (hidden by default)"
    },
    "sort": {
      "type": "string",
      "description": "one of: keywords, top10, bestPos, firstSeen, age, dr (default keywords)"
    },
    "page": {
      "type": "number",
      "description": "1-based page"
    },
    "limit": {
      "type": "number",
      "description": "rows per page, default 50, max 200"
    }
  }
}
```

</details>

Source: [src/lib/mcp/toolsSerpMon.ts:123](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsSerpMon.ts#L123-L159).

## serpmon_run

Start an asynchronous SERP-monitor run using the owner’s configured A-Parser/proxies and return runId.

<details>
<summary>Full registered description</summary>

```text
Start a SERP Monitor check now (manual trigger): every active keyword of the project is re-collected top-N through the instance owner's self-hosted A-Parser (SE::Google) over the user's own proxies. No per-request cost — but the fetch leaves the server, hence cost: net. ASYNCHRONOUS: returns the new runId immediately and snapshots appear per keyword while it runs; check progress and the storm verdict with serpmon_storms. Error codes: cooldown (checked within the last 10 minutes — pass force: true to run anyway), already_running, no_creds (A-Parser not configured), no_keywords, not_found.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `project_id` | Yes | string | Not declared |
| `force` | No | boolean | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "required": [
    "project_id"
  ],
  "properties": {
    "project_id": {
      "type": "string",
      "description": "project id from serpmon_projects"
    },
    "force": {
      "type": "boolean",
      "description": "true = ignore the 10-minute manual-run cooldown"
    }
  }
}
```

</details>

- Actual handler can mutate local state, but dispatcher defaults this non-paid registration to readOnlyHint:true and read permission.

Source: [src/lib/mcp/toolsSerpMon.ts:161](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsSerpMon.ts#L161-L184).

## fit_meta

Sanitize up to 50 items and run deterministic fitMeta; allow_llm:true requires confirmation and owner AI credentials and permits repair calls. Return per-field methods and flagged warnings.

<details>
<summary>Full registered description</summary>

```text
FREE (local): fit page meta tags inside the audit band — Title 50–60 and Meta Description 150–160 characters, counted in Unicode code points by CODE, not by the model. Give it the current values plus any alternative options the generator produced; it deterministically picks an in-band option, trims a trailing clause (keeping the main keyword, never leaving a dangling separator or preposition), and reports method per field (kept | picked | trimmed | unfixable). Set allow_llm: true (PAID — spends the instance owner's own AI credits, needs confirm: true) to let it make up to 2 repair calls per item when nothing fits deterministically, and to force a word-boundary cut as the last resort (reported as forced_cut, review those). Lengths only ever change toward the band: a too-short value is never padded.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `items` | Yes | array of object | Not declared |
| `allow_llm` | No | boolean | Not declared |
| `confirm` | No | boolean | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "items": {
      "type": "array",
      "description": "Up to 50 items: { keyword (required — kept at the start of the title), language (ISO-639-1), title?, description?, titleOptions?, descriptionOptions?, brand? (dropped first when over the limit) }",
      "items": {
        "type": "object"
      }
    },
    "allow_llm": {
      "type": "boolean",
      "description": "PAID when true: up to 2 AI repair calls per item on the owner's key, for values no deterministic trim can fit. Requires confirm: true."
    },
    "confirm": {
      "type": "boolean",
      "description": "Must be true when allow_llm is set. PAID: this call spends the instance owner's own AI credits — get their permission before setting it."
    }
  },
  "required": [
    "items"
  ]
}
```

</details>

- items.items is intentionally an open object schema; item fields and 50-item maximum are enforced only by the handler.
- allow_llm:true is paid despite cost:local; dispatcher uses read permission, while handler independently requires confirm:true.

Source: [src/lib/mcp/toolsMeta.ts:24](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsMeta.ts#L24-L96).

## get_uptime

Read a selected site’s uptime summary or all workspace uptime badges.

<details>
<summary>Full registered description</summary>

```text
Uptime monitor: without `site`, the status of every monitored site of the workspace (status up | degraded | down | unknown | paused | checker_offline, current since, last latency ms, 24 h uptime %, last error — plus the site domain). With `site` (Site id, GSC property, or domain), the full summary of one monitor: settings, uptime % over 24 h / 7 / 30 / 90 days, 30-day latency series and the last 20 incidents with causes. checker_offline means the OpenGSC server itself could not reach the network on its last pass — the sites are not known to be down.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `site` | No | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "site": {
      "type": "string",
      "description": "one site: Site row id, GSC property (sc-domain:example.com or URL), or bare domain"
    }
  }
}
```

</details>

Source: [src/lib/mcp/toolsUptime.ts:31](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsUptime.ts#L31-L61).

## get_index_coverage

Read indexAutoStatus: saved settings, queue, inspection-quota and coverage data.

<details>
<summary>Full registered description</summary>

```text
Automatic index-check status for one site: settings, today's Google URL Inspection quota usage (2,000/day per property, resets at midnight Pacific), priority queue counts (never checked / changed / not-indexed recheck / indexed recheck), 90-day index coverage by day, why-not-indexed reason breakdown, and pages with traffic that recently dropped out of the index. Local read of data the scheduler collects inside Google's free quota — to inspect URLs live, use inspect_url.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `site` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "site": {
      "type": "string",
      "description": "The site — a domain (example.com), GSC property (sc-domain:example.com), or a site id from list_sites"
    }
  },
  "required": [
    "site"
  ]
}
```

</details>

Source: [src/lib/mcp/toolsIndex.ts:7](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsIndex.ts#L7-L37) · [src/lib/mcp/shared.ts:1](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/shared.ts#L1-L373).

## get_brand_mentions

Read stored mentions with supplied filters; no live collection.

<details>
<summary>Full registered description</summary>

```text
Brand mentions feed for one site: where the brand was mentioned in Google News, Wikipedia and Wikidata. LOCAL/READ-ONLY — returns rows already stored; it does not fetch. Mentions are collected by the daily watcher (or the Mentions panel's check-now). linkStatus 'unlinked' marks an unlinked mention — the cheapest link-building target.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `site` | Yes | string | Not declared |
| `source` | No | string | Not declared |
| `state` | No | string | Not declared |
| `linkStatus` | No | string | Not declared |
| `q` | No | string | Not declared |
| `limit` | No | number | Not declared |
| `offset` | No | number | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "site": {
      "type": "string",
      "description": "The site — a domain (example.com), GSC property (sc-domain:example.com), or a site id from list_sites"
    },
    "source": {
      "type": "string",
      "enum": [
        "news",
        "wikipedia",
        "wikidata",
        "all"
      ],
      "description": "Filter by source (default all)"
    },
    "state": {
      "type": "string",
      "enum": [
        "new",
        "reviewed",
        "dismissed",
        "all"
      ],
      "description": "new = not yet reviewed (default all)"
    },
    "linkStatus": {
      "type": "string",
      "enum": [
        "unchecked",
        "linked",
        "unlinked",
        "unreachable",
        "all"
      ],
      "description": "Filter by link status (default all)"
    },
    "q": {
      "type": "string",
      "description": "Substring filter over title, snippet and publisher"
    },
    "limit": {
      "type": "number",
      "description": "Max rows (default 50, max 200)"
    },
    "offset": {
      "type": "number",
      "description": "Pagination offset"
    }
  },
  "required": [
    "site"
  ]
}
```

</details>

Source: [src/lib/mcp/toolsMentions.ts:19](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsMentions.ts#L19-L58) · [src/lib/mcp/shared.ts:1](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/shared.ts#L1-L373).

## get_ai_share_of_voice

Compute sovForSite from saved AEO answers and deterministic host categories.

<details>
<summary>Full registered description</summary>

```text
AI share of voice vs the site's named competitors (brand mentions and citation share, per engine, weekly trend) plus the domains AI engines cite for its tracked questions. The cited domains carry a heuristic DETERMINISTIC category (brand/competitor/forum/social/video/developer/ecommerce/reviews/reference/institutional/editorial — host rules, no AI), and `categoryCounts` + `reddit` aggregate those categories over the window (the Reddit cut lists the subreddits); `otherShare` (0..1) is the share the classifier could not name — high values mean the instance's domain lists should be extended (categories are configurable per instance via the aeo_domain_lists setting; a Greek starter set is built in). Aggregated from stored AEO answers — LOCAL/READ-ONLY: no AI call runs, adding a competitor never costs anything.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `site` | Yes | string | Not declared |
| `days` | No | number | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "site": {
      "type": "string",
      "description": "The site — a domain (example.com), GSC property (sc-domain:example.com), or a site id from list_sites"
    },
    "days": {
      "type": "number",
      "description": "Window: 7, 30 (default) or 90 days"
    }
  },
  "required": [
    "site"
  ]
}
```

</details>

Source: [src/lib/mcp/toolsVisibility.ts:7](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsVisibility.ts#L7-L31) · [src/lib/mcp/shared.ts:1](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/shared.ts#L1-L373).

## get_footprints

Run footprintReport on saved portfolio audits and generation history.

<details>
<summary>Full registered description</summary>

```text
Network footprint report: title/description/H1 templates repeated across several sites of the portfolio (the same construction with only the entity swapped — a linkable footprint for a site network). LOCAL and free: reads the last completed audit of every live site plus 180 days of outline/text generation history. Returns exact groups (skeleton, site count, page count, source, one example per site) and a separate similar-templates section (Jaccard >= 0.85). A skeleton with noEntity=true matched even WITHOUT the site name — the stronger footprint.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `kind` | No | string | Not declared |
| `min_sites` | No | number | Not declared |
| `include_ignored` | No | boolean | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "kind": {
      "type": "string",
      "enum": [
        "title",
        "description",
        "h1"
      ],
      "description": "Which meta field to inspect (default title; h1 covers generated outlines/articles only — the audit stores h1Count, not the text)"
    },
    "min_sites": {
      "type": "number",
      "description": "Distinct sites a template needs to qualify (default 2, min 2, max 50)"
    },
    "include_ignored": {
      "type": "boolean",
      "description": "Also return skeletons the operator marked fine (default false)"
    }
  }
}
```

</details>

Source: [src/lib/mcp/toolsFootprint.ts:11](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsFootprint.ts#L11-L43).

## get_backlink_toxicity

Read stored backlink donor classifications and overview; return migration guidance when unavailable.

<details>
<summary>Full registered description</summary>

```text
Toxicity of the site's own backlink profile, judged for THE SITE'S NICHE: Site.backlinkNiche names marker groups that are NOT toxic here (a casino anchor on a gambling site is a normal topical link; pharma/adult/hack stay toxic). Returns the niche, the donor distribution (clean/suspicious/toxic/unknown), the worst donors with their signal codes (marker groups from the drops vocabulary plus sitewide_low_dr / out_of_content / donor_parked), and the over-optimisation share of exact commercial anchors. LOCAL/READ-ONLY — it reads the last classification run; recalculating is the UI button or the hourly scheduler.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `site` | Yes | string | Not declared |
| `limit` | No | number | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "site": {
      "type": "string",
      "description": "The site — a domain (example.com), GSC property (sc-domain:example.com), or a site id from list_sites"
    },
    "limit": {
      "type": "number",
      "description": "Max donor rows (default 100, max 500)"
    }
  },
  "required": [
    "site"
  ]
}
```

</details>

Source: [src/lib/mcp/toolsBacklinkTox.ts:15](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsBacklinkTox.ts#L15-L48) · [src/lib/mcp/shared.ts:1](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/shared.ts#L1-L373).

## get_disavow_file

Build disavow file text from operator-marked local backlink rows; no upload.

<details>
<summary>Full registered description</summary>

```text
The Google disavow file for the links the OPERATOR marked (PATCH /api/backlinks/disavow — nothing is ever marked automatically). Returns the file text verbatim: header, one comment line per donor with the reason (operator note or tox signals) and the link count, then `domain:` lines for donors whose every link is marked — per-URL lines for partially marked donors, or everywhere in urls mode. Upload target: https://search.google.com/search-console/disavow-links. LOCAL/READ-ONLY.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `site` | Yes | string | Not declared |
| `mode` | No | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "site": {
      "type": "string",
      "description": "The site — a domain (example.com), GSC property (sc-domain:example.com), or a site id from list_sites"
    },
    "mode": {
      "type": "string",
      "enum": [
        "domain",
        "urls"
      ],
      "description": "domain = domain: lines where the whole donor is marked (default); urls = individual URLs everywhere"
    }
  },
  "required": [
    "site"
  ]
}
```

</details>

Source: [src/lib/mcp/toolsBacklinkTox.ts:49](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsBacklinkTox.ts#L49-L81) · [src/lib/mcp/shared.ts:1](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/shared.ts#L1-L373).

## get_local_profile

Read saved business profile and derived validation/JSON-LD.

<details>
<summary>Full registered description</summary>

```text
Local SEO business card of one site: name, schema.org business type, NAP (address, phone in E.164, e-mail), coordinates, opening hours, price range, sameAs profiles, service areas, and the selected Google Business Profile account/location. Includes the generated LocalBusiness JSON-LD and Google-requirements validation (required fields, recommended-field warnings). Returns { profile: null } when the site has no card yet — nothing is guessed from the domain.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `site` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "site": {
      "type": "string",
      "description": "Site row id, GSC property (sc-domain:example.com or URL), or bare domain"
    }
  },
  "required": [
    "site"
  ]
}
```

</details>

Source: [src/lib/mcp/toolsLocal.ts:16](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsLocal.ts#L16-L45).

## check_nap

Read business profile and run live homepage/contact-page NAP consistency checks; do not save report.

<details>
<summary>Full registered description</summary>

```text
NAP consistency check of one site against its business card: fetches the homepage and up to 10 contact-ish pages (free, one request each), extracts name/phones/address (JSON-LD first, then microdata, then text) and reports every field as match | differs | missing with the expected and found values. Requires a profile (create it in Local → Business profile first). The report is returned live and never stored.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `site` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "site": {
      "type": "string",
      "description": "Site row id, GSC property, or bare domain"
    }
  },
  "required": [
    "site"
  ]
}
```

</details>

Source: [src/lib/mcp/toolsLocal.ts:46](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsLocal.ts#L46-L72).

## local_grid_scans

Read saved grid scans and point summaries.

<details>
<summary>Full registered description</summary>

```text
Geo-grid scan history of one site (Local Falcon-style): every stored scan with status (queued/running/done/error), keyword, grid size, radius, provider, and a per-scan point summary — average rank, in-map-pack share, errored/not-found counts. Running scans show partial results (points persist as they are answered); re-call to follow progress. Free read of this instance's database.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `site` | Yes | string | Not declared |
| `limit` | No | number | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "site": {
      "type": "string",
      "description": "Site row id, GSC property, or bare domain"
    },
    "limit": {
      "type": "number",
      "description": "Max scans to return (default 20, max 50)"
    }
  },
  "required": [
    "site"
  ]
}
```

</details>

Source: [src/lib/mcp/toolsLocal.ts:73](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsLocal.ts#L73-L106).

## local_grid_scan_run

Create/start a background coordinate-grid SERP rank scan.

<details>
<summary>Full registered description</summary>

```text
Start a geo-grid rank scan (Local Falcon-style) for one keyword: the keyword is checked at gridSize² coordinate points spread over a square around the business, each point geolocated to its own lat,lng, so the result shows where the map pack actually reaches. COST: gridSize² SERP queries on the workspace's configured Rank Tracker provider (9 for 3×3, 25 for 5×5, 49 for 7×7) — free on a personal A-Parser instance, metered on Serper/DataForSEO. The scan runs in the background; poll local_grid_scans for its points. Defaults: centre = the business profile's coordinates (profile_no_coords when neither the profile nor explicit centerLat/centerLng state any — never a guessed city), gridSize 5, radiusKm 2 (0.1–100).
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `site` | Yes | string | Not declared |
| `keyword` | Yes | string | Not declared |
| `gridSize` | No | number | Not declared |
| `radiusKm` | No | number | Not declared |
| `centerLat` | No | number | Not declared |
| `centerLng` | No | number | Not declared |
| `hl` | No | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "site": {
      "type": "string",
      "description": "Site row id, GSC property, or bare domain"
    },
    "keyword": {
      "type": "string",
      "description": "The keyword to check at every grid point"
    },
    "gridSize": {
      "type": "number",
      "description": "Grid edge: 3, 5 or 7 (default 5). The scan costs gridSize² queries."
    },
    "radiusKm": {
      "type": "number",
      "description": "Centre → outer edge in km, 0.1–100 (default 2)"
    },
    "centerLat": {
      "type": "number",
      "description": "Scan centre override; pass with centerLng to skip the business profile location"
    },
    "centerLng": {
      "type": "number",
      "description": "Scan centre override; pass with centerLat"
    },
    "hl": {
      "type": "string",
      "description": "Answer language override: \"\" (default — language of the profile country) or a 2-letter code like \"en\", \"ru\", \"de\" for tourist markets"
    }
  },
  "required": [
    "site",
    "keyword"
  ]
}
```

</details>

- Registry cost is paid; dispatcher requires workspace spend permission. Handler confirmation/estimate/cache paths determine whether this call actually spends credits.
- No confirm input or handler confirmation gate is exposed; spend permission is the MCP dispatcher gate.

Source: [src/lib/mcp/toolsLocal.ts:107](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsLocal.ts#L107-L151).

## local_grid_presets

Read saved grid presets and summarized scan history.

<details>
<summary>Full registered description</summary>

```text
Saved geo-grid presets of one site — the REPEATABLE scans (R+ wave G): each preset is a named point + radius + grid + answer language + optional cron schedule, e.g. "SKG airport" or "Thessaloniki centre". Returns every preset with its schedule (5-field cron, "" = manual only), lastFireAt (the scheduler's high-water mark), and its scan history summarized — per scan: date, hl, avg rank, in-map-pack share — which IS the dynamics series across that preset's scans. Free read of this instance's database.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `site` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "site": {
      "type": "string",
      "description": "Site row id, GSC property, or bare domain"
    }
  },
  "required": [
    "site"
  ]
}
```

</details>

Source: [src/lib/mcp/toolsLocal.ts:152](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsLocal.ts#L152-L191).

## local_grid_preset_create

Save a grid preset including coordinates and optional recurring cron schedule.

<details>
<summary>Full registered description</summary>

```text
Save a geo-grid preset (a repeatable scan): name, keyword, centre (an ARBITRARY point — SKG airport, a Halkidiki resort zone — not just the business profile), gridSize 3|5|7, radiusKm 0.1–100, hl ("" = language of the profile country; "en"/"ru"/"de" for tourist markets — the SERP language changes the result as much as geography does), and schedule. schedule is "" (manual — fire with local_grid_preset_run) or a 5-field cron expression (minute hour day-of-month month day-of-week, UTC) evaluated by the in-house matcher; the scheduler fires it with a 15-minute tick, never back-fills missed windows, and its first sighting of a preset only records the marker without firing. COST PER FIRE: gridSize² SERP queries (9/25/49) on the workspace's Rank Tracker provider — free on a personal A-Parser, metered elsewhere; the preset keeps no caps, the operator owns the schedule.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `site` | Yes | string | Not declared |
| `name` | Yes | string | Not declared |
| `keyword` | Yes | string | Not declared |
| `centerLat` | Yes | number | Not declared |
| `centerLng` | Yes | number | Not declared |
| `gridSize` | No | number | Not declared |
| `radiusKm` | No | number | Not declared |
| `hl` | No | string | Not declared |
| `schedule` | No | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "site": {
      "type": "string",
      "description": "Site row id, GSC property, or bare domain"
    },
    "name": {
      "type": "string",
      "description": "Preset label, e.g. \"SKG airport\""
    },
    "keyword": {
      "type": "string",
      "description": "The keyword the preset checks at every grid point"
    },
    "centerLat": {
      "type": "number",
      "description": "Grid centre latitude (-90…90)"
    },
    "centerLng": {
      "type": "number",
      "description": "Grid centre longitude (-180…180)"
    },
    "gridSize": {
      "type": "number",
      "description": "Grid edge: 3, 5 or 7 (default 5). Each fire costs gridSize² queries."
    },
    "radiusKm": {
      "type": "number",
      "description": "Centre → outer edge in km, 0.1–100 (default 2)"
    },
    "hl": {
      "type": "string",
      "description": "Answer language: \"\" (default — language of the profile country) or a 2-letter code (\"en\", \"ru\", \"de\"…)"
    },
    "schedule": {
      "type": "string",
      "description": "5-field cron (UTC), e.g. \"0 6 * * 1\" = Mondays 06:00 UTC; \"\" = manual only. The UI compiles \"weekly at HH:MM\" into this — free-text cron never reaches users, but the field is the contract."
    }
  },
  "required": [
    "site",
    "name",
    "keyword",
    "centerLat",
    "centerLng"
  ]
}
```

</details>

- Actual handler can mutate local state, but dispatcher defaults this non-paid registration to readOnlyHint:true and read permission.

Source: [src/lib/mcp/toolsLocal.ts:192](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsLocal.ts#L192-L238).

## local_grid_preset_delete

Delete a saved grid preset while retaining its past scans.

<details>
<summary>Full registered description</summary>

```text
Delete a saved geo-grid preset by id (see local_grid_presets for ids). The preset's past scans SURVIVE (they stay in local_grid_scans, unchained) — history is a fact, not part of the configuration. Free.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `site` | Yes | string | Not declared |
| `id` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "site": {
      "type": "string",
      "description": "Site row id, GSC property, or bare domain"
    },
    "id": {
      "type": "string",
      "description": "Preset id from local_grid_presets"
    }
  },
  "required": [
    "site",
    "id"
  ]
}
```

</details>

- Actual handler can mutate local state, but dispatcher defaults this non-paid registration to readOnlyHint:true and read permission.

Source: [src/lib/mcp/toolsLocal.ts:239](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsLocal.ts#L239-L265).

## local_grid_preset_run

Start a background grid scan from a saved preset.

<details>
<summary>Full registered description</summary>

```text
Fire a saved geo-grid preset NOW (run-now button's path): creates one GridScan chained to the preset — the preset's own point, radius, grid and hl — and runs it in the background; the scan joins the preset's dynamics series. COST: gridSize² SERP queries (9 for 3×3, 25 for 5×5, 49 for 7×7) on the workspace's configured Rank Tracker provider — free on a personal A-Parser instance, metered on Serper/DataForSEO. Poll local_grid_scans (or local_grid_presets for the series) for points as they are answered. This is a manual fire: scheduled fires happen on their own and need no agent.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `site` | Yes | string | Not declared |
| `id` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "site": {
      "type": "string",
      "description": "Site row id, GSC property, or bare domain"
    },
    "id": {
      "type": "string",
      "description": "Preset id from local_grid_presets"
    }
  },
  "required": [
    "site",
    "id"
  ]
}
```

</details>

- Registry cost is paid; dispatcher requires workspace spend permission. Handler confirmation/estimate/cache paths determine whether this call actually spends credits.
- No confirm input or handler confirmation gate is exposed; spend permission is the MCP dispatcher gate.

Source: [src/lib/mcp/toolsLocal.ts:266](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsLocal.ts#L266-L295).

## get_trends

Read watcher-collected stored trend rows; no refresh or live autocomplete fetch.

<details>
<summary>Full registered description</summary>

```text
Trend radar for one site: queries rising in its Search Console (7 data days vs the previous 28), queries new to it (≥10 impressions, absent for 60 days), and new Google-suggest discoveries for the operator's seeds. Rows are collected by the daily watcher or the Demand page's Refresh — LOCAL/READ-ONLY, this call fetches nothing. Each row's score is source-specific hotness (higher = hotter); impressions are null for suggest rows because autocomplete has no volume.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `site` | Yes | string | Not declared |
| `source` | No | string | Not declared |
| `limit` | No | number | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "site": {
      "type": "string",
      "description": "The site — a domain (example.com), GSC property (sc-domain:example.com), or a site id from list_sites"
    },
    "source": {
      "type": "string",
      "enum": [
        "gsc_rising",
        "gsc_new",
        "suggest"
      ],
      "description": "Filter by source (default all three)"
    },
    "limit": {
      "type": "number",
      "description": "Max rows (default 50, max 200)"
    }
  },
  "required": [
    "site"
  ]
}
```

</details>

Source: [src/lib/mcp/toolsTrends.ts:14](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsTrends.ts#L14-L54) · [src/lib/mcp/shared.ts:1](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/shared.ts#L1-L373) · [src/lib/trends/types.ts:1](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/trends/types.ts#L1-L54).

## check_plagiarism

Estimate or execute fragment SERP searches and shingle matching through configured providers; reuse cached text-hash results.

<details>
<summary>Full registered description</summary>

```text
PAID · Search the web for exact fragments of a text and report where it was copied from. Samples up to 10 rare sentences, runs one quoted SERP query per fragment through the configured SERP provider (Serper / DataForSEO / ScrapingRobot / A-Parser), matches results by 4-word shingles and repeated URLs, and returns the share of sampled fragments found elsewhere plus the sources. An ESTIMATE, not a verdict: quotes, syndication and the site's own pages light up too (own-site matches are marked as such and never counted). Results are cached by text hash for 7 days — re-checking the same text costs nothing. Pass `text`, or `historyId` of a generated article.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `text` | No | string | Not declared |
| `historyId` | No | string | Not declared |
| `siteId` | No | string | Not declared |
| `confirm` | Yes | boolean | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "text": {
      "type": "string",
      "description": "The text to check (markdown or plain). Required unless historyId is given."
    },
    "historyId": {
      "type": "string",
      "description": "SeoHistory id of a generated article to check instead of pasted text."
    },
    "siteId": {
      "type": "string",
      "description": "Optional site id: pages on this site's domain are marked as own-site matches, not plagiarism."
    },
    "confirm": {
      "type": "boolean",
      "description": "Must be true. PAID: each sampled fragment is one billed SERP query (≤ 10) on the instance owner's key — get their permission first."
    }
  },
  "required": [
    "confirm"
  ]
}
```

</details>

- Registry cost is paid; dispatcher requires workspace spend permission. Handler confirmation/estimate/cache paths determine whether this call actually spends credits.
- confirm:true is required even for a free cache hit; unconfirmed calls throw a cost estimate error.

Source: [src/lib/mcp/toolsPlagiarism.ts:29](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsPlagiarism.ts#L29-L89) · [src/lib/plagiarism/index.ts:1](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/plagiarism/index.ts#L1-L351).

## serp_index_check

Estimate or execute site: SERP checks through configured providers, and save SERP index verdicts for workspace-owned sitemap URLs.

<details>
<summary>Full registered description</summary>

```text
PAID · Estimate whether URLs are in Google's index via a `site:` SERP query — for URLs the URL Inspection API cannot reach (drops, other people's sites, domains without a verified Search Console property). One query per URL. A captcha or provider failure returns `error`, never `not_indexed`. Verdicts are written into the site: index columns (SitemapUrl.serpIndex*) when the URL belongs to a site of this workspace; foreign URLs are checked and returned only. This is an estimate read off the public SERP, not Google's own verdict.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `urls` | Yes | array of string | Not declared |
| `confirm` | Yes | boolean | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "urls": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Absolute URLs to check (homepage or pages), at most 200."
    },
    "confirm": {
      "type": "boolean",
      "description": "Must be true. PAID: each URL is one billed SERP query on the instance owner's key — get their permission first."
    }
  },
  "required": [
    "urls",
    "confirm"
  ]
}
```

</details>

- Registry cost is paid; dispatcher requires workspace spend permission. Handler confirmation/estimate/cache paths determine whether this call actually spends credits.

Source: [src/lib/mcp/toolsPlagiarism.ts:90](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsPlagiarism.ts#L90-L154) · [src/lib/indexing/serpIndex.ts:1](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/indexing/serpIndex.ts#L1-L340).

## list_reports

Read report configurations and saved sent snapshots; no rendering/sending.

<details>
<summary>Full registered description</summary>

```text
Client reports (white-label snapshots): every report of the workspace with site, template, sections, period, schedule (off | weekly | monthly, send day), recipients, client-link state, last/next send, and the last sent snapshots (period, date, whether a PDF exists, sent-to, error state). Local database state only — no report is rendered or sent by this call.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `includeRuns` | No | boolean | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "includeRuns": {
      "type": "boolean",
      "description": "kept for forward compatibility; the latest 10 snapshots are always included"
    }
  }
}
```

</details>

Source: [src/lib/mcp/toolsReports.ts:10](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsReports.ts#L10-L55).

## list_leads

Read locally stored audit-widget leads with pipeline filters.

<details>
<summary>Full registered description</summary>

```text
List incoming leads from the embeddable audit widget: domain, contact e-mail, audit score, the top issues found, source page and pipeline status. LOCAL/READ-ONLY: touches nothing but this instance's database.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `status` | No | string | Not declared |
| `q` | No | string | Not declared |
| `limit` | No | number | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "status": {
      "type": "string",
      "enum": [
        "new",
        "contacted",
        "won",
        "lost",
        "client"
      ],
      "description": "Optional pipeline-stage filter: new | contacted | won | lost | client"
    },
    "q": {
      "type": "string",
      "description": "Optional substring filter over domain, e-mail and name"
    },
    "limit": {
      "type": "number",
      "description": "Maximum leads returned (default 50, max 200)"
    }
  }
}
```

</details>

Source: [src/lib/mcp/toolsLeads.ts:9](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsLeads.ts#L9-L47) · [src/lib/leads/types.ts:1](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/leads/types.ts#L1-L157).

## get_site_context

Read shared context and research log; for empty context return bootstrap suggestions from saved GSC/competitor data.

<details>
<summary>Full registered description</summary>

```text
The site's shared AI context (Project Memory): business overview, current goal, positioning, writing preferences, custom sections, the competitor list (same as AI share of voice), key pages (money/hub/spoke) and the research log. Call this FIRST for any site work — it grounds every workflow and its missingSections list tells you what to fill instead of re-interviewing the user. The research log's rule: if the same research ran within the last 30 days, reuse that result and say so — do not re-buy it. On an EMPTY context the response carries `bootstrap`: key pages suggested from the site's own top GSC pages, competitors from stored gap scans, the sitemap size — proposals to confirm with the operator and write via update_site_context, never to write unreviewed. Free, local; empty (not an error) before the context tables are migrated.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `site` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "site": {
      "type": "string",
      "description": "Site — id, exact URL, or domain substring"
    }
  },
  "required": [
    "site"
  ]
}
```

</details>

Source: [src/lib/mcp/toolsContext.ts:25](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsContext.ts#L25-L55).

## update_site_context

Apply context patch operations, skipping invalid operations and reporting reasons.

<details>
<summary>Full registered description</summary>

```text
Write back to the site's shared AI context (Project Memory) — the same store get_site_context reads and the Context card in the site's settings tab edits. Use it for durable learnings (positioning the user explained, competitors worth tracking, pages that matter, writing preferences) and to append a research-log entry whenever a session spent paid units. One bad op skips itself with a reason in `skipped`; the rest of the batch still applies.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `site` | Yes | string | Not declared |
| `updates` | Yes | array of object | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "site": {
      "type": "string",
      "description": "Site — id, exact URL, or domain substring"
    },
    "updates": {
      "type": "array",
      "description": "updates: an array of patch ops —\n{ section, content, title? } — set a typed section (business_overview | current_goal | positioning | writing_preferences) or a custom one (key \"custom:<slug>\"; empty content deletes it)\n{ deleteCustomSection: \"custom:<slug>\" }\n{ addCompetitors: [{ name, domain?, notes?, terms? }] } — upsert by domain (or name when no site); same list AI share of voice uses\n{ removeCompetitors: [domainOrName] }\n{ addKeyPages: [{ url, role?: money|hub|spoke|other, topic?, notes? }] } — upsert by url; a curated shortlist, not a sitemap inventory\n{ removeKeyPages: [url] }\n{ appendResearchLog: { summary } } — \"<what>: <inputs>. Verdict: <conclusion>\"; the server stamps the date and prunes past 90 days\n{ removeResearchLog: [id] }",
      "items": {
        "type": "object"
      }
    }
  },
  "required": [
    "site",
    "updates"
  ]
}
```

</details>

Source: [src/lib/mcp/toolsContext.ts:56](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsContext.ts#L56-L79).

## publish_list_connections

Read site publishing connections with masked credential previews.

<details>
<summary>Full registered description</summary>

```text
The site's publishing connections (P1: WordPress) with platform, connectionType (own_satellite | money_site | external_platform — respin is allowed ONLY for external_platform), label, site URL, verification status (unverified | ok | error with the real lastError), lastVerifiedAt and a MASKED credential preview (first 3 chars). Full credentials are never returned. Free local read.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `site` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "site": {
      "type": "string",
      "description": "The site — a domain (example.com), GSC property (sc-domain:example.com), or a site id from list_sites"
    }
  },
  "required": [
    "site"
  ]
}
```

</details>

Source: [src/lib/mcp/toolsPublish.ts:22](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsPublish.ts#L22-L40) · [src/lib/mcp/shared.ts:1](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/shared.ts#L1-L373).

## publish_post

Resolve saved or literal sources and call runPublish to create/schedule WordPress posts; optional confirmed AI respin. Store outcomes, enforce uniqueness at send time and feed successful posts into backlink records.

<details>
<summary>Full registered description</summary>

```text
Publish a post to the site's blog connections (P1: WordPress). Source is a SeoHistory record (historyId — text/landing types carry the body; find ids with get_generations) or literal title + markdown; for own-satellite networks pass items[] and give EACH connectionId its own source (own historyId or title+markdown) so every satellite carries its own post. Publishes to every connection, sequentially; each connection is independent — one failure does not abort the rest. Respin (respin: true, needs confirm) adapts the text with one cheap AI call per platform and is allowed ONLY for external_platform connections — for anything else the post is refused with respin_not_allowed_for_own_satellite. At SEND time every post passes a uniqueness gate: its text is compared (analyze_text's trigram-Jaccard engine) against every published post of the WHOLE instance (latest 300); maxSimilarity ≥ 0.3 → the post is created with status "blocked" and an error naming the twin post (no bypass exists — publish a genuinely different text); 0.15–0.3 → it publishes with the score surfaced. uniquenessScore (1 − maxSimilarity) is stored on every sent post. windowHours or windowDays (never both) defers the batch instead: posts are created as "scheduled" with a random offset inside the window (the scheduler sends them later through the same gated path — for a deferred respin the AI call happens at send time). The response carries per-post status/scores, an anchorSummary (money-site anchor distribution across this batch, repeated exact anchors flagged) and honest footprint warnings (shared title skeletons, repeated anchors, clustered schedule times). Failed or blocked posts can be re-sent via the /publishing Retry — the gate re-runs. Every successful publish feeds the existing backlink loop: a SiteBacklink row with source "self" pointing the new post's URL at the money-site link it contains.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `site` | Yes | string | Not declared |
| `historyId` | No | string | Not declared |
| `title` | No | string | Not declared |
| `markdown` | No | string | Not declared |
| `connectionIds` | No | array of string | Not declared |
| `items` | No | array of object | Not declared |
| `respin` | No | boolean | Not declared |
| `windowHours` | No | number | Not declared |
| `windowDays` | No | number | Not declared |
| `targetUrl` | No | string | Not declared |
| `confirm` | No | boolean | Not declared |
| `aiProvider` | No | string | Not declared |
| `aiApiKey` | No | string | Not declared |
| `model` | No | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "site": {
      "type": "string",
      "description": "The site — a domain (example.com), GSC property (sc-domain:example.com), or a site id from list_sites"
    },
    "historyId": {
      "type": "string",
      "description": "SeoHistory id to publish (type text or landing) — flat form, one source for every connection"
    },
    "title": {
      "type": "string",
      "description": "Literal title when no historyId is given (or as a fallback body source)"
    },
    "markdown": {
      "type": "string",
      "description": "Literal markdown body when no historyId is given"
    },
    "connectionIds": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Connections to publish to (flat form), from publish_list_connections"
    },
    "items": {
      "type": "array",
      "description": "Per-connection sources (own-satellite form): [{connectionId, historyId | title + markdown}] — each connection publishes its own post. Takes precedence over the flat form.",
      "items": {
        "type": "object",
        "properties": {
          "connectionId": {
            "type": "string"
          },
          "historyId": {
            "type": "string"
          },
          "title": {
            "type": "string"
          },
          "markdown": {
            "type": "string"
          }
        },
        "required": [
          "connectionId"
        ]
      }
    },
    "respin": {
      "type": "boolean",
      "description": "AI-adapt per external_platform connection first (one cheap call each; needs confirm; refused for own_satellite/money_site connections)"
    },
    "windowHours": {
      "type": "number",
      "description": "Defer the batch with a random offset within N hours (posts created as \"scheduled\"; sent later, gated at send time). Mutually exclusive with windowDays"
    },
    "windowDays": {
      "type": "number",
      "description": "Same as windowHours, in days"
    },
    "targetUrl": {
      "type": "string",
      "description": "Optional urlTo for the backlink row; defaults to the first money-site link in the post, else the site root"
    },
    "confirm": {
      "type": "boolean",
      "description": "Must be true when respin is on — it spends the owner's AI credits."
    },
    "aiProvider": {
      "type": "string",
      "description": "Override the respin AI provider for this call"
    },
    "aiApiKey": {
      "type": "string",
      "description": "Override the respin AI key for this call"
    },
    "model": {
      "type": "string",
      "description": "Override the respin model for this call"
    }
  },
  "required": [
    "site"
  ]
}
```

</details>

- Registry cost is paid; dispatcher requires workspace spend permission. Handler confirmation/estimate/cache paths determine whether this call actually spends credits.
- Cost remains paid even when respin:false; spend role is still required. Confirmation is required only for respin.

Source: [src/lib/mcp/toolsPublish.ts:41](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsPublish.ts#L41-L126) · [src/lib/mcp/shared.ts:1](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/shared.ts#L1-L373).

## publish_list_posts

Read site publishing post rows and status/remote/uniqueness/scheduling fields.

<details>
<summary>Full registered description</summary>

```text
Published posts of a site: title, connection, status (draft | scheduled | publishing | published | failed | blocked with the gate's twin-naming error), remoteUrl, remoteId, whether a respin was used (for scheduled posts: planned, runs at send time), scheduledAt (due time of a deferred post), uniquenessScore (1 − max similarity vs the instance's published set at send time; null = not yet sent through the gate), timestamps. Free local read.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `site` | Yes | string | Not declared |
| `page` | No | number | Not declared |
| `pageSize` | No | number | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "site": {
      "type": "string",
      "description": "The site — a domain (example.com), GSC property (sc-domain:example.com), or a site id from list_sites"
    },
    "page": {
      "type": "number",
      "description": "1-based page (default 1)"
    },
    "pageSize": {
      "type": "number",
      "description": "rows per page, default 50, max 100"
    }
  },
  "required": [
    "site"
  ]
}
```

</details>

Source: [src/lib/mcp/toolsPublish.ts:127](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/toolsPublish.ts#L127-L146) · [src/lib/mcp/shared.ts:1](https://github.com/fenjo26/OpenGSC/blob/3805be32a8d3a33d32e38724928b92946ce6c2a4/src/lib/mcp/shared.ts#L1-L373).

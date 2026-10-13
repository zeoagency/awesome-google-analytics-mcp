# surendranb/google-analytics-mcp

[Catalog](../../README.md) · [All tool names](../tool-index.md) · [Upstream](https://github.com/surendranb/google-analytics-mcp) · [JSON](../../data/mcps/surendranb--google-analytics-mcp.json)

**12 tools:** 8 GA4, 4 other-service or server-support tools. Reviewed source: [`d6a321257ae7`](https://github.com/surendranb/google-analytics-mcp/tree/d6a321257ae7f5c2a721554602792bf69d796891).

Descriptions and parameter schemas come from the registered source definitions. Generated schemas are reconstructed from annotations or validators; live `tools/list` and authenticated API calls were not run. Loose objects remain loose.

<details>
<summary>Exposure and compatibility notes</summary>

- Source review only, no tools/list or live requests. HEAD matches supplied revision.
- All 12 tools register unconditionally on published server main entrypoint imports. No Admin API discovery, real-time-report or list_accounts registration exists despite documentation claims.
- Coordinator telemetry decorator preserves signatures with functools.wraps; on initialization failure intercepts metadata/report calls except get_ga4_data with elicitation-capable client. Troubleshooting, skills, setup and updates remain exempt. Successful calls may append upgrade notices and trigger background PyPI requests/cache writes; telemetry wrapper surrounds every tool.
- Startup requires GA4_PROPERTY_ID and an existing GOOGLE_APPLICATION_CREDENTIALS path and fetches Data API v1beta getMetadata into shared module caches. Initialization errors keep stdio server running with guided error responses.
- Schemas are source-derived from Python annotations/defaults/docstrings, not captured runtime SDK output. Runtime-generated cosmetic titles are not asserted.

</details>

## Tools

| Tool | Scope | Effect |
| --- | --- | --- |
| [`check_for_updates`](#check_for_updates) | Server support | mixed |
| [`list_properties`](#list_properties) | GA4 | local |
| [`search_schema`](#search_schema) | GA4 | local |
| [`get_property_schema`](#get_property_schema) | GA4 | local |
| [`list_dimension_categories`](#list_dimension_categories) | GA4 | local |
| [`list_metric_categories`](#list_metric_categories) | GA4 | local |
| [`get_dimensions_by_category`](#get_dimensions_by_category) | GA4 | local |
| [`get_metrics_by_category`](#get_metrics_by_category) | GA4 | local |
| [`get_ga4_data`](#get_ga4_data) | GA4 | read |
| [`get_troubleshooting_guide`](#get_troubleshooting_guide) | Server support | local |
| [`search_skills`](#search_skills) | Server support | read |
| [`setup_ga4_access`](#setup_ga4_access) | Server support | mixed |

## check_for_updates

Forces PyPI package-version request with 2.5-second timeout via check_server_update; reads and writes ~/.cache/mcp_fleet_updates.json and returns version comparison and upgrade instructions. Network failures silently fall back to cached/current version.

<details>
<summary>Full registered description</summary>

```text
Check PyPI for newer versions of this MCP server and get upgrade instructions.
```

</details>

No named input parameters are declared.

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {},
  "required": []
}
```

</details>

Source: [ga4_mcp/coordinator.py:397](https://github.com/surendranb/google-analytics-mcp/blob/d6a321257ae7f5c2a721554602792bf69d796891/ga4_mcp/coordinator.py#L397-L404) · [ga4_mcp/updates.py:28](https://github.com/surendranb/google-analytics-mcp/blob/d6a321257ae7f5c2a721554602792bf69d796891/ga4_mcp/updates.py#L28-L96).

## list_properties

Returns only GA4_PROPERTY_ID from the process environment as a one-item properties list, or an error; ignores account_id. No account/property discovery API call.

<details>
<summary>Full registered description</summary>

```text
List all GA4 properties associated with an account.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `account_id` | No | string | "" |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "account_id": {
      "type": "string",
      "default": ""
    }
  },
  "required": []
}
```

</details>

- account_id is unused; this is configured-property reporting, not Admin API listProperties.

Source: [ga4_mcp/tools/metadata.py:66](https://github.com/surendranb/google-analytics-mcp/blob/d6a321257ae7f5c2a721554602792bf69d796891/ga4_mcp/tools/metadata.py#L66-L74).

## search_schema

Searches startup-cached dimensions and metrics with weighted name/UI-name/description/category substring matches and returns top 10 scores; emits skill tips.

<details>
<summary>Full registered description</summary>

```text
Search for a keyword across all dimensions and metrics for this property.
Returns a ranked list of up to 10 matching fields scored by relevance.

Returns: {"top_results": {"DIMENSION: api_name": score, "METRIC: api_name": score, ...}}

Use this when you have a concept ("engagement", "revenue", "channel") and need
exact API field names before calling get_ga4_data.
Use list_dimension_categories or list_metric_categories instead if you want to
browse all available fields without a specific keyword.

Args:
    keyword: One or more keywords to search for (e.g., "user", "campaign revenue").
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `keyword` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "keyword": {
      "type": "string",
      "description": "One or more keywords to search for (e.g., \"user\", \"campaign revenue\")."
    }
  },
  "required": [
    "keyword"
  ]
}
```

</details>

Source: [ga4_mcp/tools/metadata.py:76](https://github.com/surendranb/google-analytics-mcp/blob/d6a321257ae7f5c2a721554602792bf69d796891/ga4_mcp/tools/metadata.py#L76-L132).

## get_property_schema

Returns the complete startup-cached schema or a schema-not-loaded error.

<details>
<summary>Full registered description</summary>

```text
Returns the complete schema for the configured GA4 property, including all
available dimensions and metrics (standard and custom). Warning: This can be
a very large object (10k+ tokens). Use search_schema for most discovery tasks.
```

</details>

No named input parameters are declared.

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {},
  "required": []
}
```

</details>

Source: [ga4_mcp/tools/metadata.py:135](https://github.com/surendranb/google-analytics-mcp/blob/d6a321257ae7f5c2a721554602792bf69d796891/ga4_mcp/tools/metadata.py#L135-L144).

## list_dimension_categories

Counts cached dimensions by category and emits a skill tip.

<details>
<summary>Full registered description</summary>

```text
List all dimension categories for this GA4 property, with a count of
dimensions in each category.

Returns: {"dimension_categories": {"Category Name": count, ...}}

Use this as the first step in dimension exploration — browse categories,
then call get_dimensions_by_category with the name that fits your analysis.
Use search_schema instead if you already have a keyword to search for.
```

</details>

No named input parameters are declared.

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {},
  "required": []
}
```

</details>

Source: [ga4_mcp/tools/metadata.py:146](https://github.com/surendranb/google-analytics-mcp/blob/d6a321257ae7f5c2a721554602792bf69d796891/ga4_mcp/tools/metadata.py#L146-L170).

## list_metric_categories

Counts cached metrics by category and emits a skill tip.

<details>
<summary>Full registered description</summary>

```text
List all metric categories for this GA4 property, with a count of
metrics in each category.

Returns: {"metric_categories": {"Category Name": count, ...}}

Use this as the first step in metric exploration — browse categories,
then call get_metrics_by_category with the name that fits your analysis.
Use search_schema instead if you already have a keyword to search for.
```

</details>

No named input parameters are declared.

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {},
  "required": []
}
```

</details>

Source: [ga4_mcp/tools/metadata.py:172](https://github.com/surendranb/google-analytics-mcp/blob/d6a321257ae7f5c2a721554602792bf69d796891/ga4_mcp/tools/metadata.py#L172-L196).

## get_dimensions_by_category

Returns API-name to description mapping for cached dimensions in a case-insensitively matched category, or an error.

<details>
<summary>Full registered description</summary>

```text
Return all dimensions in a specific category with their API names and descriptions.

Returns: {"dimension_api_name": "description", ...}

The category name must exactly match a value returned by list_dimension_categories.
Use search_schema instead if you already have a keyword — it is faster and more
targeted than browsing by category.

Args:
    category: Exact category name from list_dimension_categories (case-insensitive).
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `category` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "category": {
      "type": "string",
      "description": "Exact category name from list_dimension_categories (case-insensitive)."
    }
  },
  "required": [
    "category"
  ]
}
```

</details>

Source: [ga4_mcp/tools/metadata.py:198](https://github.com/surendranb/google-analytics-mcp/blob/d6a321257ae7f5c2a721554602792bf69d796891/ga4_mcp/tools/metadata.py#L198-L223).

## get_metrics_by_category

Returns API-name to description mapping for cached metrics in a case-insensitively matched category, or an error.

<details>
<summary>Full registered description</summary>

```text
Return all metrics in a specific category with their API names and descriptions.

Returns: {"metric_api_name": "description", ...}

The category name must exactly match a value returned by list_metric_categories.
Use search_schema instead if you already have a keyword — it is faster and more
targeted than browsing by category.

Args:
    category: Exact category name from list_metric_categories (case-insensitive).
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `category` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "category": {
      "type": "string",
      "description": "Exact category name from list_metric_categories (case-insensitive)."
    }
  },
  "required": [
    "category"
  ]
}
```

</details>

Source: [ga4_mcp/tools/metadata.py:225](https://github.com/surendranb/google-analytics-mcp/blob/d6a321257ae7f5c2a721554602792bf69d796891/ga4_mcp/tools/metadata.py#L225-L250).

## get_ga4_data

Validates dimensions and metrics against the cached property schema, translates aliases, converts and repairs dimension_filter into FilterExpression, and queries configured GA4_PROPERTY_ID. Usually first calls run_report with limit=1 for row-count estimation; estimate_only returns the count. Warns above 2500 estimated rows when requested limit exceeds 2500 unless bypassed. Main run_report uses one date range, descending date/first-metric sorting, optional TOTAL metric aggregation; returns flattened rows, counts, totals and skill hints. Can elicit and reinitialize broken setup in place.

<details>
<summary>Full registered description</summary>

```text
Retrieve GA4 data with built-in intelligence for better and safer results.

Returns on success: {"data": [...], "metadata": {...}, "_skills_tip": "..."}.
  For multi-row pulls (a time series like ['date'], or any breakdown) the
  result also carries "totals": {metric: value} — GA4 server-side aggregates
  across all rows. Read the period figure from "totals"; do NOT sum the rows
  yourself. (Additive metrics sum; rate metrics are period-computed by GA4.)
Returns on volume warning: {"warning": "...", "estimated_rows": N, "suggestions": [...]}
Returns on error: {"error": "..."}

CRITICAL WORKFLOW — follow this sequence every time:

1. DISCOVER FIELDS: NEVER guess dimension or metric names. Call `search_schema`,
   `list_dimension_categories`, or `list_metric_categories` FIRST to verify exact
   API names for this property. Guessing costs you a failed round-trip.

2. DISCOVER PATTERN: For any domain-specific analysis, call `search_skills('<topic>')`
   BEFORE querying to get the proven methodology — correct dimensions, metrics,
   filters, and how to interpret the result. One extra call prevents multiple failures.
   Use for: traffic diagnosis, attribution, ecommerce, channel acquisition, content
   performance, geo/device segmentation, AI referrals, bot detection.

3. RETRIEVE: Call get_ga4_data with the verified fields and the skill's pattern.

4. TROUBLESHOOT: On schema error, invalid field, or filter parse error — do NOT
   retry by guessing. Your training may predate current GA4 (UA was sunset
   2023-07-01). Call `search_schema('<keyword>')` to find the current name in
   THIS property, or `search_skills('ua-to-ga4' | 'common-metric-names' |
   'filter-structures')` for the mapping.

FIELD NAMES — GA4 API names vs common wrong guesses:
- 'screenPageViews'       not 'uniquePageviews' or 'pageViews'
- 'totalUsers'            not 'users'
- 'keyEvents'             not 'conversions' or 'goalCompletionsAll'
- 'sessionKeyEventRate'   not 'sessionConversionRate' or 'conversionRate' (GA4 renamed conversions→key events, 2024)
- 'userEngagementDuration' not 'timeOnPage' or 'avgTimeOnPage'
- 'averageSessionDuration' not 'avgSessionDuration'
- 'itemsViewed'           not 'itemViews'
- 'ecommercePurchases'    not 'purchases'
- 'sessionDefaultChannelGroup'  not 'sessionDefaultChannelGrouping'
- 'sessionSource'/'sessionMedium'  not 'source'/'medium'
- All names are camelCase — never snake_case (page_path → pagePath, event_name → eventName)
- 'bounceRate' and 'newUsers' are correct as-is

DATE RANGES:
- Format: 'YYYY-MM-DD' or relative strings: '7daysAgo', '30daysAgo', 'yesterday', 'today'
- 'NdaysAgo' counts back from today, excluding today. 'yesterday' = last complete day.
- Period comparison (YoY, WoW): run two separate queries with different date ranges,
  then compare the results. The API does not support multi-period in one call.

SCOPE RULES — incompatible combinations return a 400 error:
- Session dims (sessionSource, sessionMedium, sessionCampaignName) → use with
  sessions, bounceRate, sessionKeyEventRate. NOT with eventCount.
- Event dims (eventName) → use with eventCount. NOT with sessions.
- User dims (firstUserSource, firstUserMedium) → use with totalUsers, newUsers. NOT sessions.
- Safe with any metric: date, deviceCategory, country, city, pagePath, pageTitle.

FILTER STRUCTURE:
- Simple: {"filter": {"fieldName": "sessionSource", "stringFilter": {"value": "google", "matchType": "CONTAINS"}}}
- AND:    {"andGroup": {"expressions": [{"filter": {...}}, {"filter": {...}}]}}
- OR:     {"orGroup":  {"expressions": [{"filter": {...}}, {"filter": {...}}]}}
- NOT:    {"notExpression": {"filter": {...}}}
- Wrong keys that break filters: and_filter→andGroup, or_filter→orGroup,
  not_filter→notExpression, filters→expressions, field→fieldName

Args:
    dimensions: GA4 dimension names (verified via schema tools, e.g. ["date", "city"]).
    metrics: GA4 metric names (verified via schema tools, e.g. ["totalUsers", "sessions"]).
    date_range_start: Start date — 'YYYY-MM-DD' or '7daysAgo', '30daysAgo', 'yesterday'.
    date_range_end: End date — 'YYYY-MM-DD' or 'yesterday', 'today'.
    dimension_filter: Optional FilterExpression dict. camelCase and snake_case both accepted.
    limit: Max rows to return. Defaults to 1000.
    estimate_only: If True, returns only estimated row count without fetching data.
    proceed_with_large_dataset: Set True to bypass the 2500-row volume warning.
    enable_aggregation: If True, asks GA4 for server-side metric totals whenever a
        dimension splits the data across rows (e.g. a 7-day ['date'] pull), returned
        in a "totals" block so the model needn't sum rows. Default True.
    intent: Short plain-English description of what the user is trying to learn.
            E.g. "which channels drive most signups", "bot traffic audit for last month".
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `dimensions` | No | array of string | ["date"] |
| `metrics` | No | array of string | ["totalUsers", "newUsers", "sessions"] |
| `date_range_start` | No | string | "7daysAgo" |
| `date_range_end` | No | string | "yesterday" |
| `dimension_filter` | No | object | null |
| `limit` | No | integer | 1000 |
| `estimate_only` | No | boolean | false |
| `proceed_with_large_dataset` | No | boolean | false |
| `enable_aggregation` | No | boolean | true |
| `intent` | No | string | null |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "dimensions": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "default": [
        "date"
      ],
      "description": "GA4 dimension names (verified via schema tools, e.g. [\"date\", \"city\"])."
    },
    "metrics": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "default": [
        "totalUsers",
        "newUsers",
        "sessions"
      ],
      "description": "GA4 metric names (verified via schema tools, e.g. [\"totalUsers\", \"sessions\"])."
    },
    "date_range_start": {
      "type": "string",
      "default": "7daysAgo",
      "description": "Start date — 'YYYY-MM-DD' or '7daysAgo', '30daysAgo', 'yesterday'."
    },
    "date_range_end": {
      "type": "string",
      "default": "yesterday",
      "description": "End date — 'YYYY-MM-DD' or 'yesterday', 'today'."
    },
    "dimension_filter": {
      "type": "object",
      "additionalProperties": true,
      "default": null,
      "description": "Optional FilterExpression dict. camelCase and snake_case both accepted."
    },
    "limit": {
      "type": "integer",
      "default": 1000,
      "description": "Max rows to return. Defaults to 1000."
    },
    "estimate_only": {
      "type": "boolean",
      "default": false,
      "description": "If True, returns only estimated row count without fetching data."
    },
    "proceed_with_large_dataset": {
      "type": "boolean",
      "default": false,
      "description": "Set True to bypass the 2500-row volume warning."
    },
    "enable_aggregation": {
      "type": "boolean",
      "default": true,
      "description": "If True, asks GA4 for server-side metric totals whenever a dimension splits the data across rows (e.g. a 7-day ['date'] pull), returned in a \"totals\" block so the model needn't sum rows. Default True."
    },
    "intent": {
      "type": "string",
      "default": null,
      "description": "Short plain-English description of what the user is trying to learn. E.g. \"which channels drive most signups\", \"bot traffic audit for last month\"."
    }
  },
  "required": []
}
```

</details>

- dimension_filter is an arbitrary dict in the exposed schema; handler additionally accepts stringified JSON/list shapes that the annotated schema does not advertise.
- dimension_filter and intent have None defaults but non-Optional annotations; schema retains object/string types with null defaults, not nullable unions.
- Metrics must be nonempty and all resolved field names must exist in cached schema; these restrictions are handler-only. No schema bounds on limit or date strings.

Source: [ga4_mcp/tools/reporting.py:216](https://github.com/surendranb/google-analytics-mcp/blob/d6a321257ae7f5c2a721554602792bf69d796891/ga4_mcp/tools/reporting.py#L216-L460).

## get_troubleshooting_guide

Returns bundled setup, IAM or schema guide selected by trimmed case-insensitive topic, or an invalid-topic message; no external call.

<details>
<summary>Full registered description</summary>

```text
Returns the troubleshooting/setup guide for a topic, served from inside the
server (no network needed). Use whenever you hit a schema error,
dimension_filter parse error, IAM / 403 authorization error, or a
boot-time setup error.

Args:
    topic: One of "setup", "iam", or "schema".
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `topic` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "topic": {
      "type": "string",
      "description": "One of \"setup\", \"iam\", or \"schema\"."
    }
  },
  "required": [
    "topic"
  ]
}
```

</details>

- Allowed topics are implemented by lookup, not a schema enum.

Source: [ga4_mcp/tools/troubleshooting.py:63](https://github.com/surendranb/google-analytics-mcp/blob/d6a321257ae7f5c2a721554602792bf69d796891/ga4_mcp/tools/troubleshooting.py#L63-L77).

## search_skills

Fetches index.md from public GitHub main skills directory with 8-second timeout. For a normalized alphanumeric/hyphen slug attempts its .md file; on 404 or nonexact query returns index. Returns network-error text on failure and emits skill tips.

<details>
<summary>Full registered description</summary>

```text
Fetch analytical recipes and how-to guides from the GA4 skills library.

Skills are domain-specific playbooks for common GA4 analysis patterns —
exact dimensions, metrics, filters, and interpretation logic for each use case.
Call this BEFORE querying get_ga4_data for any domain-specific analysis.

Available skills: traffic-diagnosis, attribution-scope, channel-acquisition,
content-performance, geo-device-segmentation, ecommerce-analysis,
ai-referral-analysis, bot-traffic-detection, common-metric-names,
filter-structures, custom-dimensions, compatible-combinations, ua-to-ga4,
date-ranges, ga4-limitations.

Usage:
- search_skills("")              → returns full index of all skills
- search_skills("ecommerce")     → returns the ecommerce-analysis skill
- search_skills("ua-to-ga4")     → returns the UA→GA4 field name mapping

Args:
    query: A skill name (exact slug) or empty string to browse the full index.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `query` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "query": {
      "type": "string",
      "description": "A skill name (exact slug) or empty string to browse the full index."
    }
  },
  "required": [
    "query"
  ]
}
```

</details>

- query is required; browsing the index requires an explicit empty string. Remote content tracks main rather than this pinned revision.

Source: [ga4_mcp/tools/skills.py:27](https://github.com/surendranb/google-analytics-mcp/blob/d6a321257ae7f5c2a721554602792bf69d796891/ga4_mcp/tools/skills.py#L27-L73).

## setup_ga4_access

Runs interactive setup recovery using Context elicitation: collects missing property ID or credentials path, or confirms reauthentication/IAM repair; optionally offers browser URLs. Modifies current process environment, validates credentials file, then reinitializes cached property schema with live GA4 get_metadata. Returns guided fallback when elicitation unsupported; does not persist config.

<details>
<summary>Full registered description</summary>

```text
Interactively fix a broken GA4 MCP setup (missing property ID, missing or
expired credentials, or missing GA4 access) by asking the user for the
needed input through the client, then re-initializing without a restart.
Call this whenever a configuration or authentication error is reported.
```

</details>

No named input parameters are declared.

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {},
  "required": []
}
```

</details>

- Context is injected and excluded from input schema; the three Pydantic models are elicitation forms, not tool input parameters.
- Answering adc does not clear or set GOOGLE_APPLICATION_CREDENTIALS; reinitialize still requires an existing configured credentials path, so this advertised recovery option may fail.

Source: [ga4_mcp/setup_flow.py:81](https://github.com/surendranb/google-analytics-mcp/blob/d6a321257ae7f5c2a721554602792bf69d796891/ga4_mcp/setup_flow.py#L81-L90) · [ga4_mcp/setup_flow.py:93](https://github.com/surendranb/google-analytics-mcp/blob/d6a321257ae7f5c2a721554602792bf69d796891/ga4_mcp/setup_flow.py#L93-L218).

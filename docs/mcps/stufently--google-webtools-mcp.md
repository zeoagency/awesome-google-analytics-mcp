# stufently/google-webtools-mcp

[Catalog](../../README.md) · [All tool names](../tool-index.md) · [Upstream](https://github.com/stufently/google-webtools-mcp) · [JSON](../../data/mcps/stufently--google-webtools-mcp.json)

**39 tools:** 10 GA4, 29 other-service or server-support tools. Reviewed source: [`2d18361dffdd`](https://github.com/stufently/google-webtools-mcp/tree/2d18361dffddb441b92abc79667a11df1b19ac42).

Descriptions and parameter schemas come from the registered source definitions. Generated schemas are reconstructed from annotations or validators; live `tools/list` and authenticated API calls were not run. Loose objects remain loose.

<details>
<summary>Exposure and compatibility notes</summary>

- Source review only; no tools/list or live requests. All ten tool modules are registered unconditionally by createServer.
- CLI authenticates before starting stdio or stateless Streamable HTTP; valid Google credentials and appropriate API access are required. No permission tiers or optional tool modules found. Search Console reads use cache and rate limiting; GA4 client performs rate-limited real API operations.
- Schemas are source-derived representations of explicit Zod registrations, not runtime tools/list output. Object schemas use Zod default unknown-key stripping (additionalProperties false).

</details>

## Tools

| Tool | Scope | Effect |
| --- | --- | --- |
| [`ga4_list_accounts`](#ga4_list_accounts) | GA4 | read |
| [`ga4_list_properties`](#ga4_list_properties) | GA4 | read |
| [`ga4_get_property`](#ga4_get_property) | GA4 | read |
| [`ga4_create_property`](#ga4_create_property) | GA4 | write |
| [`ga4_create_data_stream`](#ga4_create_data_stream) | GA4 | write |
| [`ga4_list_data_streams`](#ga4_list_data_streams) | GA4 | read |
| [`ga4_get_data_stream`](#ga4_get_data_stream) | GA4 | read |
| [`ga4_run_report`](#ga4_run_report) | GA4 | read |
| [`ga4_run_realtime_report`](#ga4_run_realtime_report) | GA4 | read |
| [`ga4_get_metadata`](#ga4_get_metadata) | GA4 | read |
| [`inspect_url`](#inspect_url) | Other service | read |
| [`batch_inspect_urls`](#batch_inspect_urls) | Other service | read |
| [`check_indexing_issues`](#check_indexing_issues) | Other service | read |
| [`find_quick_wins`](#find_quick_wins) | Other service | read |
| [`find_declining_content`](#find_declining_content) | Other service | read |
| [`find_ctr_opportunities`](#find_ctr_opportunities) | Other service | read |
| [`find_content_gaps`](#find_content_gaps) | Other service | read |
| [`find_what_to_build_next`](#find_what_to_build_next) | Other service | read |
| [`get_search_analytics`](#get_search_analytics) | Other service | read |
| [`get_performance_summary`](#get_performance_summary) | Other service | read |
| [`compare_periods`](#compare_periods) | Other service | read |
| [`get_top_queries`](#get_top_queries) | Other service | read |
| [`get_top_pages`](#get_top_pages) | Other service | read |
| [`get_traffic_by_device`](#get_traffic_by_device) | Other service | read |
| [`analyze_query_landscape`](#analyze_query_landscape) | Other service | read |
| [`find_new_queries`](#find_new_queries) | Other service | read |
| [`find_cannibalization`](#find_cannibalization) | Other service | read |
| [`weekly_seo_report`](#weekly_seo_report) | Other service | read |
| [`seo_health_check`](#seo_health_check) | Other service | read |
| [`list_sitemaps`](#list_sitemaps) | Other service | read |
| [`get_sitemap_details`](#get_sitemap_details) | Other service | read |
| [`submit_sitemap`](#submit_sitemap) | Other service | write |
| [`delete_sitemap`](#delete_sitemap) | Other service | write |
| [`list_properties`](#list_properties) | Other service | read |
| [`get_property_details`](#get_property_details) | Other service | read |
| [`add_property`](#add_property) | Other service | write |
| [`delete_property`](#delete_property) | Other service | write |
| [`gsc_get_verification_token`](#gsc_get_verification_token) | Other service | read |
| [`gsc_verify_site`](#gsc_verify_site) | Other service | write |

## ga4_list_accounts

Paginates account summaries in pages of 200, lists reachable accounts and nested property summaries, and formats a Markdown summary.

<details>
<summary>Full registered description</summary>

```text
List every Google Analytics 4 account the credentials can reach, and the properties under each account. Use when the user does not yet know the account or property id. Call ga4_list_properties when they already named an account, and call ga4_get_property for one property settings.
```

</details>

No named input parameters are declared.

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {},
  "required": [],
  "additionalProperties": false
}
```

</details>

Source: [src/tools/ga4-admin/index.ts:10](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/ga4-admin/index.ts#L10-L49) · [src/api/ga4-client.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/ga4-client.ts#L1-L172) · [src/tools/schemas.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/schemas.ts#L1-L87).

## ga4_list_properties

Normalizes account ID into a parent filter, paginates properties in pages of 200, and formats their settings.

<details>
<summary>Full registered description</summary>

```text
List Google Analytics 4 properties under one account, including timezone, currency, and when each property was created. Use when the user names an account and wants its properties. Call ga4_list_accounts when the account id is unknown, and call ga4_get_property to open one property.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `account_id` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "account_id": {
      "type": "string",
      "description": "GA4 account ID (e.g., \"123456\" or \"accounts/123456\")"
    }
  },
  "required": [
    "account_id"
  ],
  "additionalProperties": false
}
```

</details>

Source: [src/tools/ga4-admin/index.ts:52](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/ga4-admin/index.ts#L52-L98) · [src/api/ga4-client.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/ga4-client.ts#L1-L172) · [src/tools/schemas.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/schemas.ts#L1-L87).

## ga4_get_property

Normalizes the property resource name, fetches one property, and formats settings and timestamps.

<details>
<summary>Full registered description</summary>

```text
Read one Google Analytics 4 property display name, timezone, currency, industry, and parent account. Use when the user asks how a known property is configured. Call ga4_list_properties to find the id first, and call ga4_list_data_streams for the streams on that property.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "property_id": {
      "type": "string",
      "description": "GA4 property ID (e.g., \"123456\" or \"properties/123456\")"
    }
  },
  "required": [
    "property_id"
  ],
  "additionalProperties": false
}
```

</details>

Source: [src/tools/ga4-admin/index.ts:101](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/ga4-admin/index.ts#L101-L139) · [src/api/ga4-client.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/ga4-client.ts#L1-L172) · [src/tools/schemas.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/schemas.ts#L1-L87).

## ga4_create_property

Normalizes the account parent and creates a property with display name, timezone, currency and optional industry category; formats the created property.

<details>
<summary>Full registered description</summary>

```text
Create a new Google Analytics 4 property under an account, with a display name, timezone, and currency. Use when the user asks to provision a GA4 property. This server cannot remove the property afterwards. Call ga4_list_properties to see properties that already exist, and call ga4_create_data_stream next when they need a measurement id.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `account_id` | Yes | string | Not declared |
| `display_name` | Yes | string | Not declared |
| `timezone` | Yes | string | Not declared |
| `currency_code` | No | string | "USD" |
| `industry_category` | No | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "account_id": {
      "type": "string",
      "description": "GA4 account ID (e.g., \"123456\" or \"accounts/123456\")"
    },
    "display_name": {
      "type": "string",
      "description": "Display name for the new property"
    },
    "timezone": {
      "type": "string",
      "description": "Reporting timezone (e.g., \"America/New_York\", \"Europe/Moscow\")"
    },
    "currency_code": {
      "type": "string",
      "default": "USD",
      "description": "Currency code (e.g., \"USD\", \"EUR\")"
    },
    "industry_category": {
      "type": "string",
      "description": "Industry category (e.g., \"TECHNOLOGY\", \"FINANCE\")"
    }
  },
  "required": [
    "account_id",
    "display_name",
    "timezone"
  ],
  "additionalProperties": false
}
```

</details>

Source: [src/tools/ga4-admin/index.ts:142](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/ga4-admin/index.ts#L142-L192) · [src/api/ga4-client.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/ga4-client.ts#L1-L172) · [src/tools/schemas.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/schemas.ts#L1-L87).

## ga4_create_data_stream

Normalizes the property parent, parses the URL hostname for the default stream name, creates a WEB_DATA_STREAM, and returns measurement ID and installation advice.

<details>
<summary>Full registered description</summary>

```text
Create a web data stream on a Google Analytics 4 property and return its measurement id for the tag. Use when the user needs a measurement id to install analytics on a site. This server cannot delete the stream afterwards. Call ga4_list_data_streams if a stream may already exist, and call ga4_create_property first when the property itself does not exist yet.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |
| `url` | Yes | string | Not declared |
| `stream_name` | No | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "property_id": {
      "type": "string",
      "description": "GA4 property ID (e.g., \"123456\" or \"properties/123456\")"
    },
    "url": {
      "type": "string",
      "description": "Website URL for the data stream (e.g., \"https://example.com\")"
    },
    "stream_name": {
      "type": "string",
      "description": "Display name for the stream (defaults to hostname)"
    }
  },
  "required": [
    "property_id",
    "url"
  ],
  "additionalProperties": false
}
```

</details>

- url is only a string in the input schema, but the handler requires it to parse with new URL(url).

Source: [src/tools/ga4-admin/index.ts:195](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/ga4-admin/index.ts#L195-L245) · [src/api/ga4-client.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/ga4-client.ts#L1-L172) · [src/tools/schemas.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/schemas.ts#L1-L87).

## ga4_list_data_streams

Paginates data streams in pages of 200 and formats stream names, types, measurement IDs, URIs and timestamps.

<details>
<summary>Full registered description</summary>

```text
List the data streams on a Google Analytics 4 property, including each web stream measurement id and default URI. Use when the user asks which streams or measurement ids a property already has. Call ga4_get_data_stream for one stream, and call ga4_create_data_stream only when they want a new stream.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "property_id": {
      "type": "string",
      "description": "GA4 property ID (e.g., \"123456\" or \"properties/123456\")"
    }
  },
  "required": [
    "property_id"
  ],
  "additionalProperties": false
}
```

</details>

Source: [src/tools/ga4-admin/index.ts:248](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/ga4-admin/index.ts#L248-L289) · [src/api/ga4-client.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/ga4-client.ts#L1-L172) · [src/tools/schemas.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/schemas.ts#L1-L87).

## ga4_get_data_stream

Builds properties/{property}/dataStreams/{stream} and fetches and formats a single stream.

<details>
<summary>Full registered description</summary>

```text
Read one Google Analytics 4 data stream, including its measurement id, default URI, and created and updated times. Use when the user names a stream and wants its measurement id or settings. Call ga4_list_data_streams when the stream id is not known yet.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |
| `stream_id` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "property_id": {
      "type": "string",
      "description": "GA4 property ID (e.g., \"123456\" or \"properties/123456\")"
    },
    "stream_id": {
      "type": "string",
      "description": "Data stream ID (numeric, e.g., \"789012\")"
    }
  },
  "required": [
    "property_id",
    "stream_id"
  ],
  "additionalProperties": false
}
```

</details>

Source: [src/tools/ga4-admin/index.ts:292](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/ga4-admin/index.ts#L292-L332) · [src/api/ga4-client.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/ga4-client.ts#L1-L172) · [src/tools/schemas.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/schemas.ts#L1-L87).

## ga4_run_report

Maps metric and dimension names to API objects and sends one date range and row limit to runReport; formats returned rows as a Markdown table. Does not expose filters, ordering or pagination despite those fields existing in internal request types.

<details>
<summary>Full registered description</summary>

```text
Run a Google Analytics 4 report for chosen metrics, dimensions, and an absolute or relative date range. Use when the user asks for historical GA4 numbers such as users, sessions, or page views. Call ga4_run_realtime_report for who is on the site right now, and call ga4_get_metadata before guessing a custom metric name.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |
| `start_date` | Yes | string | Not declared |
| `end_date` | Yes | string | Not declared |
| `metrics` | Yes | array of string | Not declared |
| `dimensions` | No | array of string | Not declared |
| `limit` | No | number | 100 |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "property_id": {
      "type": "string",
      "description": "GA4 property ID (e.g., \"123456\" or \"properties/123456\")"
    },
    "start_date": {
      "type": "string",
      "pattern": "^(\\d{4}-\\d{2}-\\d{2}|\\d+daysAgo|yesterday|today)$",
      "description": "Start date: YYYY-MM-DD or relative (\"7daysAgo\", \"30daysAgo\", \"yesterday\", \"today\")"
    },
    "end_date": {
      "type": "string",
      "pattern": "^(\\d{4}-\\d{2}-\\d{2}|\\d+daysAgo|yesterday|today)$",
      "description": "End date: YYYY-MM-DD or relative (\"yesterday\", \"today\")"
    },
    "metrics": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "minItems": 1,
      "description": "Metrics to retrieve (e.g., [\"activeUsers\", \"sessions\", \"screenPageViews\"])"
    },
    "dimensions": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Dimensions to group by (e.g., [\"date\", \"country\", \"pagePath\"])"
    },
    "limit": {
      "type": "number",
      "minimum": 1,
      "maximum": 100000,
      "default": 100,
      "description": "Maximum rows to return (1-100000, default 100)"
    }
  },
  "required": [
    "property_id",
    "start_date",
    "end_date",
    "metrics"
  ],
  "additionalProperties": false
}
```

</details>

Source: [src/tools/ga4-reporting/index.ts:37](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/ga4-reporting/index.ts#L37-L85) · [src/api/ga4-client.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/ga4-client.ts#L1-L172) · [src/tools/schemas.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/schemas.ts#L1-L87).

## ga4_run_realtime_report

Maps metric and dimension names to API objects and runs a realtime report; formats returned rows as a Markdown table.

<details>
<summary>Full registered description</summary>

```text
Run a Google Analytics 4 realtime report of active users and on-site activity from the last thirty minutes. Use when the user asks who is on the site right now. Call ga4_run_report for any date range older than that live window, and call ga4_get_metadata if a realtime metric name is rejected.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |
| `metrics` | Yes | array of string | Not declared |
| `dimensions` | No | array of string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "property_id": {
      "type": "string",
      "description": "GA4 property ID (e.g., \"123456\" or \"properties/123456\")"
    },
    "metrics": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "minItems": 1,
      "description": "Realtime metrics (e.g., [\"activeUsers\", \"screenPageViews\", \"conversions\"])"
    },
    "dimensions": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Realtime dimensions (e.g., [\"country\", \"city\", \"unifiedScreenName\"])"
    }
  },
  "required": [
    "property_id",
    "metrics"
  ],
  "additionalProperties": false
}
```

</details>

Source: [src/tools/ga4-reporting/index.ts:88](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/ga4-reporting/index.ts#L88-L122) · [src/api/ga4-client.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/ga4-client.ts#L1-L172) · [src/tools/schemas.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/schemas.ts#L1-L87).

## ga4_get_metadata

Retrieves property metadata, combines metrics and dimensions, groups them by category and marks custom definitions in Markdown.

<details>
<summary>Full registered description</summary>

```text
List the dimensions and metrics a Google Analytics 4 property accepts, including custom definitions. Use when a report needs valid metric and dimension names and guessing would be wrong. Call ga4_run_report once the names are known; this tool does not return the numbers.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "property_id": {
      "type": "string",
      "description": "GA4 property ID (e.g., \"123456\" or \"properties/123456\")"
    }
  },
  "required": [
    "property_id"
  ],
  "additionalProperties": false
}
```

</details>

Source: [src/tools/ga4-reporting/index.ts:125](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/ga4-reporting/index.ts#L125-L179) · [src/api/ga4-client.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/ga4-client.ts#L1-L172) · [src/tools/schemas.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/schemas.ts#L1-L87).

## inspect_url

Inspects one URL, normalizes index, mobile, rich result and canonical status and formats findings and recommendations.

<details>
<summary>Full registered description</summary>

```text
Inspect one URL in the Google Search Console index for coverage, mobile usability, and rich-result verdicts, including the issues behind a failure. Use when the user asks why a single URL is missing from search or looks wrong. Call batch_inspect_urls for a list of URLs, and call check_indexing_issues to audit the top traffic pages of the property.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `siteUrl` | Yes | string | Not declared |
| `url` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "siteUrl": {
      "type": "string",
      "description": "The site URL exactly as it appears in Google Search Console (e.g., \"https://example.com/\" or \"sc-domain:example.com\")"
    },
    "url": {
      "type": "string",
      "format": "uri",
      "description": "The fully qualified URL to inspect"
    }
  },
  "required": [
    "siteUrl",
    "url"
  ],
  "additionalProperties": false
}
```

</details>

Source: [src/tools/indexing/index.ts:478](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/indexing/index.ts#L478-L509) · [src/api/client.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/client.ts#L1-L205) · [src/api/url-inspection.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/url-inspection.ts#L1-L217) · [src/tools/schemas.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/schemas.ts#L1-L87).

## batch_inspect_urls

Sequentially inspects up to 50 URLs and formats aggregate and per-URL findings; an unhandled individual failure aborts the batch.

<details>
<summary>Full registered description</summary>

```text
Inspect up to 50 URLs in one call and group them into indexed, not indexed, and errors. Indexed URLs show coverage state and last crawl; not-indexed URLs show verdict, coverage state, robots.txt state, and page fetch state; URLs without index data are listed as errors. Use when the user hands over a list of URLs to check. Call inspect_url for a single URL, and call check_indexing_issues when they want the top traffic pages audited without supplying the list.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `siteUrl` | Yes | string | Not declared |
| `urls` | Yes | array of string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "siteUrl": {
      "type": "string",
      "description": "The site URL exactly as it appears in Google Search Console (e.g., \"https://example.com/\" or \"sc-domain:example.com\")"
    },
    "urls": {
      "type": "array",
      "items": {
        "type": "string",
        "format": "uri"
      },
      "minItems": 1,
      "maxItems": 50,
      "description": "Array of URLs to inspect (max 50)"
    }
  },
  "required": [
    "siteUrl",
    "urls"
  ],
  "additionalProperties": false
}
```

</details>

Source: [src/tools/indexing/index.ts:513](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/indexing/index.ts#L513-L631) · [src/api/client.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/client.ts#L1-L205) · [src/api/url-inspection.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/url-inspection.ts#L1-L217) · [src/tools/schemas.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/schemas.ts#L1-L87).

## check_indexing_issues

Queries top pages from Search Analytics, inspects selected URLs with per-URL settled outcomes, and reports indexability, canonical and coverage issues plus inspection failures.

<details>
<summary>Full registered description</summary>

```text
Audit the top traffic pages of a property for indexing failures, canonical mismatches, missing canonicals, and mobile problems. Use when the user wants an indexing health pass rather than a check of URLs they already named. Call inspect_url or batch_inspect_urls when they already have the URL list.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `siteUrl` | Yes | string | Not declared |
| `limit` | No | number | 20 |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "siteUrl": {
      "type": "string",
      "description": "The site URL exactly as it appears in Google Search Console (e.g., \"https://example.com/\" or \"sc-domain:example.com\")"
    },
    "limit": {
      "type": "number",
      "minimum": 1,
      "maximum": 100,
      "default": 20,
      "description": "Number of top pages to check (default 20, max 100)"
    }
  },
  "required": [
    "siteUrl"
  ],
  "additionalProperties": false
}
```

</details>

Source: [src/tools/indexing/index.ts:635](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/indexing/index.ts#L635-L816) · [src/api/client.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/client.ts#L1-L205) · [src/api/search-analytics.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/search-analytics.ts#L1-L248) · [src/api/url-inspection.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/url-inspection.ts#L1-L217) · [src/tools/schemas.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/schemas.ts#L1-L87) · [src/api/data-freshness.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/data-freshness.ts#L1-L141).

## find_quick_wins

Queries query/page Search Analytics rows, filters minimum impressions, classifies mutually exclusive CTR, position gain and page-two opportunities, scores them and estimates click potential.

<details>
<summary>Full registered description</summary>

```text
Find query and page pairs that rank well but are under-clicked, sit just off page one, or would gain clicks from a small position push. Use when the user asks where search traffic is being left on the table. Call find_ctr_opportunities for page-level CTR gaps, and call find_declining_content when the problem is traffic that is already falling.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `siteUrl` | Yes | string | Not declared |
| `period` | No | string | "last28d" |
| `searchType` | No | string | "web" |
| `minImpressions` | No | number | 100 |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "siteUrl": {
      "type": "string",
      "description": "The site URL exactly as it appears in Google Search Console (e.g., \"https://example.com/\" or \"sc-domain:example.com\")"
    },
    "period": {
      "type": "string",
      "enum": [
        "last7d",
        "last28d",
        "last3m",
        "last6m",
        "last12m",
        "last16m"
      ],
      "description": "Predefined date range period",
      "default": "last28d"
    },
    "searchType": {
      "type": "string",
      "enum": [
        "web",
        "image",
        "video",
        "news",
        "discover",
        "googleNews"
      ],
      "default": "web",
      "description": "Search type to analyze"
    },
    "minImpressions": {
      "type": "number",
      "minimum": 0,
      "default": 100,
      "description": "Minimum impressions to consider a query"
    }
  },
  "required": [
    "siteUrl"
  ],
  "additionalProperties": false
}
```

</details>

- Analysis requests use an internal rowLimit of 25000; this limit is not exposed as an input parameter.

Source: [src/tools/opportunities/index.ts:272](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/opportunities/index.ts#L272-L408) · [src/api/client.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/client.ts#L1-L205) · [src/api/search-analytics.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/search-analytics.ts#L1-L248) · [src/tools/schemas.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/schemas.ts#L1-L87) · [src/api/data-freshness.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/data-freshness.ts#L1-L141).

## find_declining_content

Queries current and previous periods for pages and queries, filters minimum prior clicks and finds traffic declines with local recommendations.

<details>
<summary>Full registered description</summary>

```text
Compare the current Search Console period with the previous one and rank the pages and the queries that lost clicks. Use when the user asks what stopped getting traffic or what dropped recently. Call find_quick_wins for under-clicked rankings that are not necessarily declining, and call weekly_seo_report for a full weekly digest.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `siteUrl` | Yes | string | Not declared |
| `period` | No | string | "last28d" |
| `searchType` | No | string | "web" |
| `minClicksInPrevious` | No | number | 10 |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "siteUrl": {
      "type": "string",
      "description": "The site URL exactly as it appears in Google Search Console (e.g., \"https://example.com/\" or \"sc-domain:example.com\")"
    },
    "period": {
      "type": "string",
      "enum": [
        "last7d",
        "last28d",
        "last3m",
        "last6m",
        "last12m",
        "last16m"
      ],
      "description": "Predefined date range period",
      "default": "last28d"
    },
    "searchType": {
      "type": "string",
      "enum": [
        "web",
        "image",
        "video",
        "news",
        "discover",
        "googleNews"
      ],
      "default": "web",
      "description": "Search type to analyze"
    },
    "minClicksInPrevious": {
      "type": "number",
      "minimum": 0,
      "default": 10,
      "description": "Minimum clicks in the previous period to consider a page or query"
    }
  },
  "required": [
    "siteUrl"
  ],
  "additionalProperties": false
}
```

</details>

- Analysis requests use an internal rowLimit of 25000; this limit is not exposed as an input parameter.

Source: [src/tools/opportunities/index.ts:413](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/opportunities/index.ts#L413-L629) · [src/api/client.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/client.ts#L1-L205) · [src/api/search-analytics.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/search-analytics.ts#L1-L248) · [src/tools/schemas.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/schemas.ts#L1-L87) · [src/api/data-freshness.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/data-freshness.ts#L1-L141).

## find_ctr_opportunities

Queries page Search Analytics rows, filters minimum impressions and compares CTR against position benchmarks to rank potential click gains.

<details>
<summary>Full registered description</summary>

```text
Find pages whose Search Console click-through rate sits well below the benchmark for their average position, with a fix note for each page. Use when the user asks which titles or snippets are wasting impressions. Call find_quick_wins for query and page pairs near page one, and call get_top_pages for a plain traffic ranking.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `siteUrl` | Yes | string | Not declared |
| `period` | No | string | "last28d" |
| `searchType` | No | string | "web" |
| `minImpressions` | No | number | 50 |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "siteUrl": {
      "type": "string",
      "description": "The site URL exactly as it appears in Google Search Console (e.g., \"https://example.com/\" or \"sc-domain:example.com\")"
    },
    "period": {
      "type": "string",
      "enum": [
        "last7d",
        "last28d",
        "last3m",
        "last6m",
        "last12m",
        "last16m"
      ],
      "description": "Predefined date range period",
      "default": "last28d"
    },
    "searchType": {
      "type": "string",
      "enum": [
        "web",
        "image",
        "video",
        "news",
        "discover",
        "googleNews"
      ],
      "default": "web",
      "description": "Search type to analyze"
    },
    "minImpressions": {
      "type": "number",
      "minimum": 0,
      "default": 50,
      "description": "Minimum impressions to include a page"
    }
  },
  "required": [
    "siteUrl"
  ],
  "additionalProperties": false
}
```

</details>

- Analysis requests use an internal rowLimit of 25000; this limit is not exposed as an input parameter.

Source: [src/tools/opportunities/index.ts:634](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/opportunities/index.ts#L634-L817) · [src/api/client.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/client.ts#L1-L205) · [src/api/search-analytics.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/search-analytics.ts#L1-L248) · [src/tools/schemas.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/schemas.ts#L1-L87) · [src/api/data-freshness.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/data-freshness.ts#L1-L141).

## find_content_gaps

Queries query/page rows across current and previous periods and locally identifies zero-click demand, landing-page mismatches and related content opportunities.

<details>
<summary>Full registered description</summary>

```text
Find Search Console queries that land on the wrong page, high-impression queries with no clicks, and topics that still need a dedicated page. Use when the user asks what content is missing. Call find_what_to_build_next to group that demand by intent, and call find_cannibalization when several pages already compete for one query.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `siteUrl` | Yes | string | Not declared |
| `period` | No | string | "last28d" |
| `searchType` | No | string | "web" |
| `minImpressions` | No | number | 20 |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "siteUrl": {
      "type": "string",
      "description": "The site URL exactly as it appears in Google Search Console (e.g., \"https://example.com/\" or \"sc-domain:example.com\")"
    },
    "period": {
      "type": "string",
      "enum": [
        "last7d",
        "last28d",
        "last3m",
        "last6m",
        "last12m",
        "last16m"
      ],
      "description": "Predefined date range period",
      "default": "last28d"
    },
    "searchType": {
      "type": "string",
      "enum": [
        "web",
        "image",
        "video",
        "news",
        "discover",
        "googleNews"
      ],
      "default": "web",
      "description": "Search type to analyze"
    },
    "minImpressions": {
      "type": "number",
      "minimum": 0,
      "default": 20,
      "description": "Minimum impressions to consider a query"
    }
  },
  "required": [
    "siteUrl"
  ],
  "additionalProperties": false
}
```

</details>

- Analysis requests use an internal rowLimit of 25000; this limit is not exposed as an input parameter.

Source: [src/tools/opportunities/index.ts:822](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/opportunities/index.ts#L822-L1117) · [src/api/client.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/client.ts#L1-L205) · [src/api/search-analytics.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/search-analytics.ts#L1-L248) · [src/tools/schemas.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/schemas.ts#L1-L87) · [src/api/data-freshness.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/data-freshness.ts#L1-L141).

## find_what_to_build_next

Queries query/page rows, filters impressions, aggregates by query, classifies intent and builds local topic clusters and suggested content.

<details>
<summary>Full registered description</summary>

```text
Group Search Console queries by user intent, covering questions, comparisons, problems, and buying signals, into topic clusters for what to write next. Use when the user asks what content to create. Call find_content_gaps for mismatched landing pages and zero-click queries, and call analyze_query_landscape for the overall intent mix.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `siteUrl` | Yes | string | Not declared |
| `period` | No | string | "last28d" |
| `searchType` | No | string | "web" |
| `minImpressions` | No | number | 10 |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "siteUrl": {
      "type": "string",
      "description": "The site URL exactly as it appears in Google Search Console (e.g., \"https://example.com/\" or \"sc-domain:example.com\")"
    },
    "period": {
      "type": "string",
      "enum": [
        "last7d",
        "last28d",
        "last3m",
        "last6m",
        "last12m",
        "last16m"
      ],
      "description": "Predefined date range period",
      "default": "last28d"
    },
    "searchType": {
      "type": "string",
      "enum": [
        "web",
        "image",
        "video",
        "news",
        "discover",
        "googleNews"
      ],
      "default": "web",
      "description": "Search type to analyze"
    },
    "minImpressions": {
      "type": "number",
      "minimum": 0,
      "default": 10,
      "description": "Minimum impressions to consider a query"
    }
  },
  "required": [
    "siteUrl"
  ],
  "additionalProperties": false
}
```

</details>

- Analysis requests use an internal rowLimit of 25000; this limit is not exposed as an input parameter.

Source: [src/tools/opportunities/index.ts:1122](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/opportunities/index.ts#L1122-L1410) · [src/api/client.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/client.ts#L1-L205) · [src/api/search-analytics.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/search-analytics.ts#L1-L248) · [src/tools/schemas.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/schemas.ts#L1-L87) · [src/api/data-freshness.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/data-freshness.ts#L1-L141).

## get_search_analytics

Forwards explicit dates, dimensions, filters, search type, data state, row limit and aggregation type to Search Analytics and formats rows and freshness limitations.

<details>
<summary>Full registered description</summary>

```text
Query raw Google Search Console search analytics with explicit dates, dimensions, filters, search type, row limit, and data state. Use when the user needs a custom breakdown that the shaped reports do not offer. Call get_performance_summary for a period overview, call get_top_queries or get_top_pages for a ranking, and call compare_periods for two named date ranges.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `siteUrl` | Yes | string | Not declared |
| `startDate` | Yes | string | Not declared |
| `endDate` | Yes | string | Not declared |
| `dimensions` | No | array of string | Not declared |
| `searchType` | No | string | "web" |
| `filters` | No | array of object | Not declared |
| `rowLimit` | No | number | 1000 |
| `dataState` | No | string | "all" |
| `aggregationType` | No | string | "auto" |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "siteUrl": {
      "type": "string",
      "description": "The site URL exactly as it appears in Google Search Console (e.g., \"https://example.com/\" or \"sc-domain:example.com\")"
    },
    "startDate": {
      "type": "string",
      "pattern": "^\\d{4}-\\d{2}-\\d{2}$",
      "description": "Start date in YYYY-MM-DD format"
    },
    "endDate": {
      "type": "string",
      "pattern": "^\\d{4}-\\d{2}-\\d{2}$",
      "description": "End date in YYYY-MM-DD format"
    },
    "dimensions": {
      "type": "array",
      "items": {
        "type": "string",
        "enum": [
          "date",
          "query",
          "page",
          "country",
          "device",
          "searchAppearance"
        ],
        "description": "Dimension to group results by"
      },
      "description": "Dimensions to group by (e.g. query, page, date, country, device, searchAppearance)"
    },
    "searchType": {
      "type": "string",
      "enum": [
        "web",
        "image",
        "video",
        "news",
        "discover",
        "googleNews"
      ],
      "default": "web",
      "description": "Search type to analyze"
    },
    "filters": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "dimension": {
            "type": "string",
            "description": "Dimension to filter on (query, page, country, device, searchAppearance)"
          },
          "operator": {
            "type": "string",
            "enum": [
              "contains",
              "equals",
              "notContains",
              "notEquals",
              "includingRegex",
              "excludingRegex"
            ],
            "default": "contains"
          },
          "expression": {
            "type": "string",
            "description": "Filter expression value"
          }
        },
        "required": [
          "dimension",
          "expression"
        ],
        "additionalProperties": false
      },
      "description": "Dimension filters to apply"
    },
    "rowLimit": {
      "type": "number",
      "minimum": 1,
      "maximum": 25000,
      "default": 1000,
      "description": "Maximum rows to return (1-25000)"
    },
    "dataState": {
      "type": "string",
      "enum": [
        "all",
        "final"
      ],
      "default": "all",
      "description": "\"final\" = finalized data only (the API's own default; the newest days are simply absent until they settle), \"all\" = also includes the freshest days, whose numbers may still change"
    },
    "aggregationType": {
      "type": "string",
      "enum": [
        "auto",
        "byPage",
        "byProperty"
      ],
      "default": "auto"
    }
  },
  "required": [
    "siteUrl",
    "startDate",
    "endDate"
  ],
  "additionalProperties": false
}
```

</details>

Source: [src/tools/performance/index.ts:143](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/performance/index.ts#L143-L245) · [src/api/client.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/client.ts#L1-L205) · [src/api/search-analytics.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/search-analytics.ts#L1-L248) · [src/tools/schemas.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/schemas.ts#L1-L87) · [src/api/data-freshness.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/data-freshness.ts#L1-L141).

## get_performance_summary

Resolves a predefined period and queries current and previous aggregate Search Analytics metrics to calculate changes and recommendations.

<details>
<summary>Full registered description</summary>

```text
Summarize clicks, impressions, CTR, and average position for one property against the previous period of the same length. Use when the user asks how search traffic is doing over a named period such as the last 28 days. Call compare_periods when they name two specific date ranges, and call get_search_analytics when they need the raw rows.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `siteUrl` | Yes | string | Not declared |
| `period` | No | string | "last28d" |
| `searchType` | No | string | "web" |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "siteUrl": {
      "type": "string",
      "description": "The site URL exactly as it appears in Google Search Console (e.g., \"https://example.com/\" or \"sc-domain:example.com\")"
    },
    "period": {
      "type": "string",
      "enum": [
        "last7d",
        "last28d",
        "last3m",
        "last6m",
        "last12m",
        "last16m"
      ],
      "description": "Predefined date range period",
      "default": "last28d"
    },
    "searchType": {
      "type": "string",
      "enum": [
        "web",
        "image",
        "video",
        "news",
        "discover",
        "googleNews"
      ],
      "default": "web",
      "description": "Search type to analyze"
    }
  },
  "required": [
    "siteUrl"
  ],
  "additionalProperties": false
}
```

</details>

Source: [src/tools/performance/index.ts:250](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/performance/index.ts#L250-L335) · [src/api/client.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/client.ts#L1-L205) · [src/api/search-analytics.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/search-analytics.ts#L1-L248) · [src/tools/schemas.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/schemas.ts#L1-L87) · [src/api/data-freshness.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/data-freshness.ts#L1-L141).

## compare_periods

Queries two explicit date ranges using chosen dimensions and search type, computes metric differences and formats comparisons.

<details>
<summary>Full registered description</summary>

```text
Compare Search Console clicks, impressions, CTR, and position between two explicit date ranges, optionally grouped by a dimension. Use when the user names a before and an after, such as a release or a season. Call get_performance_summary when they want the latest period against the one just before it, without choosing dates.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `siteUrl` | Yes | string | Not declared |
| `period1StartDate` | Yes | string | Not declared |
| `period1EndDate` | Yes | string | Not declared |
| `period2StartDate` | Yes | string | Not declared |
| `period2EndDate` | Yes | string | Not declared |
| `dimensions` | No | array of string | Not declared |
| `searchType` | No | string | "web" |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "siteUrl": {
      "type": "string",
      "description": "The site URL exactly as it appears in Google Search Console (e.g., \"https://example.com/\" or \"sc-domain:example.com\")"
    },
    "period1StartDate": {
      "type": "string",
      "pattern": "^\\d{4}-\\d{2}-\\d{2}$",
      "description": "Period 1 start date (YYYY-MM-DD)"
    },
    "period1EndDate": {
      "type": "string",
      "pattern": "^\\d{4}-\\d{2}-\\d{2}$",
      "description": "Period 1 end date (YYYY-MM-DD)"
    },
    "period2StartDate": {
      "type": "string",
      "pattern": "^\\d{4}-\\d{2}-\\d{2}$",
      "description": "Period 2 start date (YYYY-MM-DD)"
    },
    "period2EndDate": {
      "type": "string",
      "pattern": "^\\d{4}-\\d{2}-\\d{2}$",
      "description": "Period 2 end date (YYYY-MM-DD)"
    },
    "dimensions": {
      "type": "array",
      "items": {
        "type": "string",
        "enum": [
          "date",
          "query",
          "page",
          "country",
          "device",
          "searchAppearance"
        ],
        "description": "Dimension to group results by"
      },
      "description": "Dimensions to group by"
    },
    "searchType": {
      "type": "string",
      "enum": [
        "web",
        "image",
        "video",
        "news",
        "discover",
        "googleNews"
      ],
      "default": "web",
      "description": "Search type to analyze"
    }
  },
  "required": [
    "siteUrl",
    "period1StartDate",
    "period1EndDate",
    "period2StartDate",
    "period2EndDate"
  ],
  "additionalProperties": false
}
```

</details>

Source: [src/tools/performance/index.ts:340](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/performance/index.ts#L340-L477) · [src/api/client.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/client.ts#L1-L205) · [src/api/search-analytics.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/search-analytics.ts#L1-L248) · [src/tools/schemas.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/schemas.ts#L1-L87) · [src/api/data-freshness.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/data-freshness.ts#L1-L141).

## get_top_queries

Queries query rows and aggregate totals, applies device/page/country filters and ranks the returned queries by search performance.

<details>
<summary>Full registered description</summary>

```text
List the top Search Console queries by clicks and score each query against the CTR benchmark for its position. Use when the user asks which queries bring traffic or which queries underperform their rank. Call get_top_pages for pages rather than queries, and call find_quick_wins for opportunity buckets instead of a plain ranking.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `siteUrl` | Yes | string | Not declared |
| `period` | No | string | "last28d" |
| `searchType` | No | string | "web" |
| `device` | No | string | Not declared |
| `page` | No | string | Not declared |
| `country` | No | string | Not declared |
| `limit` | No | number | 20 |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "siteUrl": {
      "type": "string",
      "description": "The site URL exactly as it appears in Google Search Console (e.g., \"https://example.com/\" or \"sc-domain:example.com\")"
    },
    "period": {
      "type": "string",
      "enum": [
        "last7d",
        "last28d",
        "last3m",
        "last6m",
        "last12m",
        "last16m"
      ],
      "description": "Predefined date range period",
      "default": "last28d"
    },
    "searchType": {
      "type": "string",
      "enum": [
        "web",
        "image",
        "video",
        "news",
        "discover",
        "googleNews"
      ],
      "default": "web",
      "description": "Search type to analyze"
    },
    "device": {
      "type": "string",
      "enum": [
        "DESKTOP",
        "MOBILE",
        "TABLET"
      ],
      "description": "Filter by device type"
    },
    "page": {
      "type": "string",
      "description": "Filter to a specific page URL (contains match)"
    },
    "country": {
      "type": "string",
      "description": "Filter by country code (e.g. \"USA\", \"GBR\")"
    },
    "limit": {
      "type": "number",
      "minimum": 1,
      "maximum": 25000,
      "default": 20,
      "description": "Number of top queries to return"
    }
  },
  "required": [
    "siteUrl"
  ],
  "additionalProperties": false
}
```

</details>

Source: [src/tools/performance/index.ts:482](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/performance/index.ts#L482-L585) · [src/api/client.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/client.ts#L1-L205) · [src/api/search-analytics.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/search-analytics.ts#L1-L248) · [src/tools/schemas.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/schemas.ts#L1-L87) · [src/api/data-freshness.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/data-freshness.ts#L1-L141).

## get_top_pages

Queries page rows and aggregate totals with optional device and query filters, and formats top page metrics and recommendations.

<details>
<summary>Full registered description</summary>

```text
List the top Search Console pages by clicks and score each page against the CTR benchmark for its position. Use when the user asks which URLs earn the search traffic. Call get_top_queries for queries, call get_traffic_by_device for a device split, and call find_ctr_opportunities for pages far below the benchmark.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `siteUrl` | Yes | string | Not declared |
| `period` | No | string | "last28d" |
| `searchType` | No | string | "web" |
| `device` | No | string | Not declared |
| `query` | No | string | Not declared |
| `limit` | No | number | 20 |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "siteUrl": {
      "type": "string",
      "description": "The site URL exactly as it appears in Google Search Console (e.g., \"https://example.com/\" or \"sc-domain:example.com\")"
    },
    "period": {
      "type": "string",
      "enum": [
        "last7d",
        "last28d",
        "last3m",
        "last6m",
        "last12m",
        "last16m"
      ],
      "description": "Predefined date range period",
      "default": "last28d"
    },
    "searchType": {
      "type": "string",
      "enum": [
        "web",
        "image",
        "video",
        "news",
        "discover",
        "googleNews"
      ],
      "default": "web",
      "description": "Search type to analyze"
    },
    "device": {
      "type": "string",
      "enum": [
        "DESKTOP",
        "MOBILE",
        "TABLET"
      ],
      "description": "Filter by device type"
    },
    "query": {
      "type": "string",
      "description": "Filter to pages matching a specific query (contains match)"
    },
    "limit": {
      "type": "number",
      "minimum": 1,
      "maximum": 25000,
      "default": 20,
      "description": "Number of top pages to return"
    }
  },
  "required": [
    "siteUrl"
  ],
  "additionalProperties": false
}
```

</details>

Source: [src/tools/performance/index.ts:590](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/performance/index.ts#L590-L696) · [src/api/client.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/client.ts#L1-L205) · [src/api/search-analytics.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/search-analytics.ts#L1-L248) · [src/tools/schemas.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/schemas.ts#L1-L87) · [src/api/data-freshness.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/data-freshness.ts#L1-L141).

## get_traffic_by_device

Queries device-dimension Search Analytics rows and computes traffic shares and local device recommendations.

<details>
<summary>Full registered description</summary>

```text
Split Search Console clicks, impressions, CTR, and average position across desktop, mobile, and tablet. Use when the user asks whether one device is underperforming the others. Call get_top_pages or get_top_queries when they want the pages or queries behind that device split.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `siteUrl` | Yes | string | Not declared |
| `period` | No | string | "last28d" |
| `searchType` | No | string | "web" |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "siteUrl": {
      "type": "string",
      "description": "The site URL exactly as it appears in Google Search Console (e.g., \"https://example.com/\" or \"sc-domain:example.com\")"
    },
    "period": {
      "type": "string",
      "enum": [
        "last7d",
        "last28d",
        "last3m",
        "last6m",
        "last12m",
        "last16m"
      ],
      "description": "Predefined date range period",
      "default": "last28d"
    },
    "searchType": {
      "type": "string",
      "enum": [
        "web",
        "image",
        "video",
        "news",
        "discover",
        "googleNews"
      ],
      "default": "web",
      "description": "Search type to analyze"
    }
  },
  "required": [
    "siteUrl"
  ],
  "additionalProperties": false
}
```

</details>

Source: [src/tools/performance/index.ts:701](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/performance/index.ts#L701-L823) · [src/api/client.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/client.ts#L1-L205) · [src/api/search-analytics.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/search-analytics.ts#L1-L248) · [src/tools/schemas.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/schemas.ts#L1-L87) · [src/api/data-freshness.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/data-freshness.ts#L1-L141).

## analyze_query_landscape

Queries query rows, filters minimum impressions and locally classifies intent, brand demand and position bands with metrics and distribution tables.

<details>
<summary>Full registered description</summary>

```text
Classify the Search Console queries of a property by intent, branded versus non-branded demand, and position band. Use when the user wants the shape of search demand rather than a list of winners. Call find_new_queries for queries that just appeared, and call find_cannibalization when several pages share one query.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `siteUrl` | Yes | string | Not declared |
| `period` | No | string | "last28d" |
| `searchType` | No | string | "web" |
| `minImpressions` | No | integer | 5 |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "siteUrl": {
      "type": "string",
      "description": "The site URL exactly as it appears in Google Search Console (e.g., \"https://example.com/\" or \"sc-domain:example.com\")"
    },
    "period": {
      "type": "string",
      "enum": [
        "last7d",
        "last28d",
        "last3m",
        "last6m",
        "last12m",
        "last16m"
      ],
      "description": "Predefined date range period",
      "default": "last28d"
    },
    "searchType": {
      "type": "string",
      "enum": [
        "web",
        "image",
        "video",
        "news",
        "discover",
        "googleNews"
      ],
      "default": "web",
      "description": "Search type to analyze"
    },
    "minImpressions": {
      "type": "integer",
      "minimum": 0,
      "default": 5,
      "description": "Minimum impressions for a query to be included"
    }
  },
  "required": [
    "siteUrl"
  ],
  "additionalProperties": false
}
```

</details>

Source: [src/tools/queries/index.ts:147](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/queries/index.ts#L147-L360) · [src/api/client.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/client.ts#L1-L205) · [src/api/search-analytics.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/search-analytics.ts#L1-L248) · [src/tools/schemas.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/schemas.ts#L1-L87) · [src/api/data-freshness.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/data-freshness.ts#L1-L141).

## find_new_queries

Queries current and previous query rows, compares query sets and growth, filters current impressions and formats new and rising demand.

<details>
<summary>Full registered description</summary>

```text
Find queries that are new or rising fast by diffing this Search Console period against the previous one. Use when the user asks what people started searching recently. Call analyze_query_landscape for the overall mix of intent, and call find_what_to_build_next when they want those queries grouped into topics to write.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `siteUrl` | Yes | string | Not declared |
| `period` | No | string | "last28d" |
| `searchType` | No | string | "web" |
| `minImpressions` | No | integer | 5 |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "siteUrl": {
      "type": "string",
      "description": "The site URL exactly as it appears in Google Search Console (e.g., \"https://example.com/\" or \"sc-domain:example.com\")"
    },
    "period": {
      "type": "string",
      "enum": [
        "last7d",
        "last28d",
        "last3m",
        "last6m",
        "last12m",
        "last16m"
      ],
      "description": "Predefined date range period",
      "default": "last28d"
    },
    "searchType": {
      "type": "string",
      "enum": [
        "web",
        "image",
        "video",
        "news",
        "discover",
        "googleNews"
      ],
      "default": "web",
      "description": "Search type to analyze"
    },
    "minImpressions": {
      "type": "integer",
      "minimum": 0,
      "default": 5,
      "description": "Minimum impressions in the current period to be included"
    }
  },
  "required": [
    "siteUrl"
  ],
  "additionalProperties": false
}
```

</details>

Source: [src/tools/queries/index.ts:365](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/queries/index.ts#L365-L587) · [src/api/client.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/client.ts#L1-L205) · [src/api/search-analytics.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/search-analytics.ts#L1-L248) · [src/tools/schemas.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/schemas.ts#L1-L87) · [src/api/data-freshness.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/data-freshness.ts#L1-L141).

## find_cannibalization

Queries query/page rows, filters total and per-page impressions and locally detects multiple competing pages, winning pages and low-volume exclusions.

<details>
<summary>Full registered description</summary>

```text
Detect queries where more than one page of the property ranks, and name the page that wins the clicks. Use when the user asks whether their own pages compete for the same query. Call find_content_gaps when the query lands on the wrong page, and call get_top_pages for a plain page ranking.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `siteUrl` | Yes | string | Not declared |
| `period` | No | string | "last28d" |
| `searchType` | No | string | "web" |
| `minImpressions` | No | integer | 20 |
| `minPageImpressions` | No | integer | 30 |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "siteUrl": {
      "type": "string",
      "description": "The site URL exactly as it appears in Google Search Console (e.g., \"https://example.com/\" or \"sc-domain:example.com\")"
    },
    "period": {
      "type": "string",
      "enum": [
        "last7d",
        "last28d",
        "last3m",
        "last6m",
        "last12m",
        "last16m"
      ],
      "description": "Predefined date range period",
      "default": "last28d"
    },
    "searchType": {
      "type": "string",
      "enum": [
        "web",
        "image",
        "video",
        "news",
        "discover",
        "googleNews"
      ],
      "default": "web",
      "description": "Search type to analyze"
    },
    "minImpressions": {
      "type": "integer",
      "minimum": 0,
      "default": 20,
      "description": "Minimum total impressions for a query to be evaluated for cannibalization"
    },
    "minPageImpressions": {
      "type": "integer",
      "minimum": 0,
      "default": 30,
      "description": "Minimum impressions one page needs before it counts as a real contender. Queries where only a single page clears this bar are reported as low-volume and get no consolidation advice."
    }
  },
  "required": [
    "siteUrl"
  ],
  "additionalProperties": false
}
```

</details>

Source: [src/tools/queries/index.ts:592](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/queries/index.ts#L592-L784) · [src/api/client.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/client.ts#L1-L205) · [src/api/search-analytics.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/search-analytics.ts#L1-L248) · [src/tools/schemas.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/schemas.ts#L1-L87) · [src/analysis/cannibalization.ts:55](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/analysis/cannibalization.ts#L55-L55) · [src/api/data-freshness.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/data-freshness.ts#L1-L141).

## weekly_seo_report

Collects current and previous Search Analytics totals and breakdowns, opportunity and trend analyses plus sitemap status, then produces a Markdown weekly SEO report; individual report sections catch API errors.

<details>
<summary>Full registered description</summary>

```text
Build a one-call weekly SEO digest with traffic versus last week, top growers and decliners, quick wins, sitemap health, and prioritized recommendations. Use when the user asks for a weekly report or a regular status update. Call seo_health_check for a letter grade, and call get_performance_summary when they only want the headline numbers.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `siteUrl` | Yes | string | Not declared |
| `searchType` | No | string | "web" |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "siteUrl": {
      "type": "string",
      "description": "The site URL exactly as it appears in Google Search Console (e.g., \"https://example.com/\" or \"sc-domain:example.com\")"
    },
    "searchType": {
      "type": "string",
      "enum": [
        "web",
        "image",
        "video",
        "news",
        "discover",
        "googleNews"
      ],
      "default": "web",
      "description": "Search type to analyze"
    }
  },
  "required": [
    "siteUrl"
  ],
  "additionalProperties": false
}
```

</details>

Source: [src/tools/reports/index.ts:136](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/reports/index.ts#L136-L579) · [src/api/client.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/client.ts#L1-L205) · [src/api/search-analytics.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/search-analytics.ts#L1-L248) · [src/api/sitemaps.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/sitemaps.ts#L1-L163) · [src/tools/schemas.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/schemas.ts#L1-L87) · [src/api/data-freshness.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/data-freshness.ts#L1-L141).

## seo_health_check

Collects Search Analytics breakdowns and sitemap status, computes local SEO health assessments and recommendations and formats a report; individual sections catch API errors.

<details>
<summary>Full registered description</summary>

```text
Score a Search Console property from A to F, with sub-scores for traffic trend, CTR efficiency, position distribution, and sitemap health. Use when the user asks how healthy the site is in search or wants a grade. Call weekly_seo_report for the narrative digest, and call find_declining_content when they already know traffic fell.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `siteUrl` | Yes | string | Not declared |
| `searchType` | No | string | "web" |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "siteUrl": {
      "type": "string",
      "description": "The site URL exactly as it appears in Google Search Console (e.g., \"https://example.com/\" or \"sc-domain:example.com\")"
    },
    "searchType": {
      "type": "string",
      "enum": [
        "web",
        "image",
        "video",
        "news",
        "discover",
        "googleNews"
      ],
      "default": "web",
      "description": "Search type to analyze"
    }
  },
  "required": [
    "siteUrl"
  ],
  "additionalProperties": false
}
```

</details>

Source: [src/tools/reports/index.ts:585](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/reports/index.ts#L585-L1056) · [src/api/client.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/client.ts#L1-L205) · [src/api/search-analytics.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/search-analytics.ts#L1-L248) · [src/api/sitemaps.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/sitemaps.ts#L1-L163) · [src/tools/schemas.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/schemas.ts#L1-L87) · [src/api/data-freshness.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/data-freshness.ts#L1-L141).

## list_sitemaps

Lists submitted sitemaps and formats status, counts, warnings and errors.

<details>
<summary>Full registered description</summary>

```text
List the sitemaps submitted for one Google Search Console property, with status, URL counts, and error flags. Use when the user asks which sitemaps are filed or whether Google reports sitemap problems. Call get_sitemap_details to open one feed, and call submit_sitemap only when they want to file a sitemap.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `siteUrl` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "siteUrl": {
      "type": "string",
      "description": "The site URL exactly as it appears in Google Search Console (e.g., \"https://example.com/\" or \"sc-domain:example.com\")"
    }
  },
  "required": [
    "siteUrl"
  ],
  "additionalProperties": false
}
```

</details>

Source: [src/tools/sitemaps/index.ts:15](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/sitemaps/index.ts#L15-L76) · [src/api/client.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/client.ts#L1-L205) · [src/api/sitemaps.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/sitemaps.ts#L1-L163) · [src/tools/schemas.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/schemas.ts#L1-L87).

## get_sitemap_details

Gets a sitemap by feedpath and formats submission/download timestamps, status and content counts.

<details>
<summary>Full registered description</summary>

```text
Read one submitted sitemap, including its type, last download, URL counts by content type, and error and warning totals. Use when the user names a sitemap and wants its processing status. Call list_sitemaps when they do not yet know which feed to open.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `siteUrl` | Yes | string | Not declared |
| `feedpath` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "siteUrl": {
      "type": "string",
      "description": "The site URL exactly as it appears in Google Search Console (e.g., \"https://example.com/\" or \"sc-domain:example.com\")"
    },
    "feedpath": {
      "type": "string",
      "description": "The URL of the sitemap (e.g., \"https://example.com/sitemap.xml\")"
    }
  },
  "required": [
    "siteUrl",
    "feedpath"
  ],
  "additionalProperties": false
}
```

</details>

Source: [src/tools/sitemaps/index.ts:79](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/sitemaps/index.ts#L79-L153) · [src/api/client.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/client.ts#L1-L205) · [src/api/sitemaps.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/sitemaps.ts#L1-L163) · [src/tools/schemas.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/schemas.ts#L1-L87).

## submit_sitemap

Submits or resubmits the sitemap feedpath to Search Console and invalidates related sitemap cache entries.

<details>
<summary>Full registered description</summary>

```text
Submit a sitemap URL to Google Search Console so Google can discover the pages of that property. Use when the user has published or moved a sitemap and asks to file it. Submitting the same feed again refreshes it and does not delete anything. Call delete_sitemap to withdraw a feed, and call get_sitemap_details to check processing afterwards.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `siteUrl` | Yes | string | Not declared |
| `feedpath` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "siteUrl": {
      "type": "string",
      "description": "The site URL exactly as it appears in Google Search Console (e.g., \"https://example.com/\" or \"sc-domain:example.com\")"
    },
    "feedpath": {
      "type": "string",
      "description": "The URL of the sitemap (e.g., \"https://example.com/sitemap.xml\")"
    }
  },
  "required": [
    "siteUrl",
    "feedpath"
  ],
  "additionalProperties": false
}
```

</details>

Source: [src/tools/sitemaps/index.ts:156](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/sitemaps/index.ts#L156-L189) · [src/api/client.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/client.ts#L1-L205) · [src/api/sitemaps.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/sitemaps.ts#L1-L163) · [src/tools/schemas.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/schemas.ts#L1-L87).

## delete_sitemap

Removes a submitted sitemap from Search Console and invalidates related cache entries; does not delete the hosted file.

<details>
<summary>Full registered description</summary>

```text
Withdraw a previously submitted sitemap from a Google Search Console property. Use when the user asks to remove a stale, duplicated, or broken sitemap. Removing the sitemap does not drop its URLs from the Google index. Call submit_sitemap to file that feed again, and call list_sitemaps to see what is still submitted.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `siteUrl` | Yes | string | Not declared |
| `feedpath` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "siteUrl": {
      "type": "string",
      "description": "The site URL exactly as it appears in Google Search Console (e.g., \"https://example.com/\" or \"sc-domain:example.com\")"
    },
    "feedpath": {
      "type": "string",
      "description": "The URL of the sitemap (e.g., \"https://example.com/sitemap.xml\")"
    }
  },
  "required": [
    "siteUrl",
    "feedpath"
  ],
  "additionalProperties": false
}
```

</details>

Source: [src/tools/sitemaps/index.ts:192](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/sitemaps/index.ts#L192-L223) · [src/api/client.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/client.ts#L1-L205) · [src/api/sitemaps.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/sitemaps.ts#L1-L163) · [src/tools/schemas.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/schemas.ts#L1-L87).

## list_properties

Lists accessible Search Console sites and permission levels using cached API results.

<details>
<summary>Full registered description</summary>

```text
List every Google Search Console property the credentials can access, including each property type and permission level. Use when the user wants to see which sites they can query before choosing one. Call get_property_details for a single known property, and call add_property only when they ask to register a new site.
```

</details>

No named input parameters are declared.

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {},
  "required": [],
  "additionalProperties": false
}
```

</details>

Source: [src/tools/sites/index.ts:17](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/sites/index.ts#L17-L52) · [src/api/client.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/client.ts#L1-L205) · [src/api/sites.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/sites.ts#L1-L123) · [src/tools/schemas.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/schemas.ts#L1-L87).

## get_property_details

Reads one Search Console site and formats permission and verification advice.

<details>
<summary>Full registered description</summary>

```text
Read the type, permission level, and verification state of one Google Search Console property. Use when the user names a specific site and wants to know how that property is registered. Call list_properties when the property URL is not known yet.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `siteUrl` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "siteUrl": {
      "type": "string",
      "description": "The site URL exactly as it appears in Google Search Console (e.g., \"https://example.com/\" or \"sc-domain:example.com\")"
    }
  },
  "required": [
    "siteUrl"
  ],
  "additionalProperties": false
}
```

</details>

Source: [src/tools/sites/index.ts:55](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/sites/index.ts#L55-L99) · [src/api/client.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/client.ts#L1-L205) · [src/api/sites.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/sites.ts#L1-L123) · [src/tools/schemas.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/schemas.ts#L1-L87).

## add_property

Adds a Search Console site to the authenticated account and invalidates site cache entries; does not establish ownership verification.

<details>
<summary>Full registered description</summary>

```text
Register a site URL or a domain as a Google Search Console property on the authenticated account. Use when the user asks to add a site to Search Console. Adding a property does not verify it. Call gsc_get_verification_token and then gsc_verify_site to prove ownership, and call list_properties to see sites that are already listed.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `siteUrl` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "siteUrl": {
      "type": "string",
      "description": "The site URL exactly as it appears in Google Search Console (e.g., \"https://example.com/\" or \"sc-domain:example.com\")"
    }
  },
  "required": [
    "siteUrl"
  ],
  "additionalProperties": false
}
```

</details>

Source: [src/tools/sites/index.ts:102](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/sites/index.ts#L102-L137) · [src/api/client.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/client.ts#L1-L205) · [src/api/sites.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/sites.ts#L1-L123) · [src/tools/schemas.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/schemas.ts#L1-L87).

## delete_property

Removes the Search Console site from the authenticated account and invalidates site cache entries.

<details>
<summary>Full registered description</summary>

```text
Remove a Google Search Console property from the authenticated account site list. Use when the user explicitly asks to drop a property. The property can be added back later, and this call does not erase historical data held by Google. Call delete_sitemap to withdraw a sitemap instead, and call add_property to register the site again.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `siteUrl` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "siteUrl": {
      "type": "string",
      "description": "The site URL exactly as it appears in Google Search Console (e.g., \"https://example.com/\" or \"sc-domain:example.com\")"
    }
  },
  "required": [
    "siteUrl"
  ],
  "additionalProperties": false
}
```

</details>

Source: [src/tools/sites/index.ts:140](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/sites/index.ts#L140-L171) · [src/api/client.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/client.ts#L1-L205) · [src/api/sites.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/sites.ts#L1-L123) · [src/tools/schemas.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/schemas.ts#L1-L87).

## gsc_get_verification_token

Normalizes URL-prefix, sc-domain and bare-domain sites, requests a verification token and formats method-specific placement instructions; does not publish the proof.

<details>
<summary>Full registered description</summary>

```text
Request a site-verification token for FILE, DNS_TXT, META, or ANALYTICS, and the steps for placing that token. Use when the user needs the token before they can prove they own a site. Call gsc_verify_site only after the token is in place. Domain properties cannot use FILE or META; call this tool with DNS_TXT for those.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `site_url` | Yes | string | Not declared |
| `method` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "site_url": {
      "type": "string",
      "description": "Site URL or domain to verify (e.g., \"https://example.com/\" or \"example.com\" for domain verification)"
    },
    "method": {
      "type": "string",
      "enum": [
        "FILE",
        "DNS_TXT",
        "META",
        "ANALYTICS"
      ],
      "description": "Verification method to use"
    }
  },
  "required": [
    "site_url",
    "method"
  ],
  "additionalProperties": false
}
```

</details>

- Domain FILE and META restrictions are not enforced before the API call; warnings are added only after a successful response.

Source: [src/tools/verification/index.ts:50](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/verification/index.ts#L50-L93) · [src/api/verification-client.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/verification-client.ts#L1-L62) · [src/tools/schemas.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/schemas.ts#L1-L87).

## gsc_verify_site

Normalizes the site and inserts a Site Verification web resource using the requested verification method; formats returned ownership information.

<details>
<summary>Full registered description</summary>

```text
Record Google site ownership for a URL or a domain once the verification token is already in place. Use when the user says the file, DNS record, meta tag, or Analytics tag is published and asks to finish verification. Call gsc_get_verification_token first if they do not have a token yet. This does not add the Search Console property; call add_property for that.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `site_url` | Yes | string | Not declared |
| `method` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "site_url": {
      "type": "string",
      "description": "Site URL or domain to verify (e.g., \"https://example.com/\" or \"example.com\")"
    },
    "method": {
      "type": "string",
      "enum": [
        "FILE",
        "DNS_TXT",
        "META",
        "ANALYTICS"
      ],
      "description": "Verification method that was configured"
    }
  },
  "required": [
    "site_url",
    "method"
  ],
  "additionalProperties": false
}
```

</details>

Source: [src/tools/verification/index.ts:96](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/verification/index.ts#L96-L138) · [src/api/verification-client.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/api/verification-client.ts#L1-L62) · [src/tools/schemas.ts:1](https://github.com/stufently/google-webtools-mcp/blob/2d18361dffddb441b92abc79667a11df1b19ac42/src/tools/schemas.ts#L1-L87).

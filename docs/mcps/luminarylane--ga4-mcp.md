# luminarylane/ga4-mcp

[Catalog](../../README.md) · [All tool names](../tool-index.md) · [Upstream](https://github.com/luminarylane/ga4-mcp) · [JSON](../../data/mcps/luminarylane--ga4-mcp.json)

**7 tools:** 7 GA4, 0 other-service or server-support tools. Reviewed source: [`90e80869b6ad`](https://github.com/luminarylane/ga4-mcp/tree/90e80869b6ad043956e8fb2d551332d5dec5312a).

Descriptions and parameter schemas come from the registered source definitions. Generated schemas are reconstructed from annotations or validators; live `tools/list` and authenticated API calls were not run. Loose objects remain loose.

<details>
<summary>Exposure and compatibility notes</summary>

- Source review only; no tools/list or live requests. Git HEAD matches the supplied revision.
- All seven decorators are unconditional. No other modules, optional tool sets, aliases, nested input models or injected Context parameters are present.
- Schemas reconstructed from primitive Python signatures/defaults and parameter docstrings; parameter descriptions are source-derived documentation, not claimed runtime tools/list output. No minimum/maximum or enum constraints are exposed by annotations.
- Service-account authentication only: GA4_CREDENTIALS_PATH, GSC_CREDENTIALS_PATH or known service_account_credentials.json paths; analytics.readonly scope. Reports also need a property_id argument or GA4_PROPERTY_ID. OAuth is mentioned in module prose but has no implementation.
- Shared _format_value accesses MetricType.TYPE_SECONDS (line 262); this member reference requires dependency compatibility and was not runtime-tested. Integer formatting evaluates that attribute after the TYPE_FLOAT check.
- Reports use a shared token bucket and retry transient API errors three times; tool exceptions are returned as text. Admin account/property discovery bypasses those helpers.
- pyproject.toml packages ga4_server and exposes luminarylane-ga4-mcp = ga4_server:main; required Google, MCP and Sentry dependencies are declared.

</details>

## Tools

| Tool | Scope | Effect |
| --- | --- | --- |
| [`ga4_list_properties`](#ga4_list_properties) | GA4 | read |
| [`ga4_get_report`](#ga4_get_report) | GA4 | read |
| [`ga4_get_top_pages`](#ga4_get_top_pages) | GA4 | read |
| [`ga4_get_traffic_sources`](#ga4_get_traffic_sources) | GA4 | read |
| [`ga4_get_conversions`](#ga4_get_conversions) | GA4 | read |
| [`ga4_get_realtime`](#ga4_get_realtime) | GA4 | read |
| [`ga4_compare_periods`](#ga4_compare_periods) | GA4 | read |

## ga4_list_properties

Creates an AnalyticsAdminServiceClient using service account credentials, eagerly lists accessible accounts, and lists properties filtered by parent account for each account. Returns account names plus property IDs and display names as text. These synchronous Admin API calls run directly in the async handler without the report retry/token wrapper.

<details>
<summary>Full registered description</summary>

```text
List all GA4 properties accessible by the service account.
Returns property IDs and display names.
```

</details>

No named input parameters are declared.

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {},
  "title": "ga4_list_propertiesArguments",
  "required": []
}
```

</details>

- Properties are discovered only under accounts returned by list_accounts; no separate direct-property discovery path.

Source: [ga4_server.py:402](https://github.com/luminarylane/ga4-mcp/blob/90e80869b6ad043956e8fb2d551332d5dec5312a/ga4_server.py#L402-L437).

## ga4_get_report

Splits comma-separated dimension and metric names, strips whitespace and drops empty names. Calls run_report with one UTC date range from today minus days through today, row limit clamped to 1–100, and descending order on the first metric when present. Returns a formatted text table.

<details>
<summary>Full registered description</summary>

```text
Run a custom GA4 report with any combination of dimensions and metrics.

Args:
    property_id: GA4 property ID (numeric). Leave empty to use GA4_PROPERTY_ID env var.
    dimensions: Comma-separated dimension names (e.g., "date", "sessionSource,sessionMedium",
                "pagePath", "country", "deviceCategory"). Default: "date".
    metrics: Comma-separated metric names (e.g., "sessions,totalUsers,screenPageViews",
             "bounceRate,averageSessionDuration,conversions"). Default: "sessions,totalUsers,screenPageViews".
    days: Lookback period in days (default: 28).
    row_limit: Max rows to return (default: 20, max: 100).
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | No | string | "" |
| `dimensions` | No | string | "date" |
| `metrics` | No | string | "sessions,totalUsers,screenPageViews" |
| `days` | No | integer | 28 |
| `row_limit` | No | integer | 20 |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "property_id": {
      "type": "string",
      "title": "Property Id",
      "default": "",
      "description": "GA4 property ID (numeric). Leave empty to use GA4_PROPERTY_ID env var."
    },
    "dimensions": {
      "type": "string",
      "title": "Dimensions",
      "default": "date",
      "description": "Comma-separated dimension names (e.g., \"date\", \"sessionSource,sessionMedium\", \"pagePath\", \"country\", \"deviceCategory\"). Default: \"date\"."
    },
    "metrics": {
      "type": "string",
      "title": "Metrics",
      "default": "sessions,totalUsers,screenPageViews",
      "description": "Comma-separated metric names (e.g., \"sessions,totalUsers,screenPageViews\", \"bounceRate,averageSessionDuration,conversions\"). Default: \"sessions,totalUsers,screenPageViews\"."
    },
    "days": {
      "type": "integer",
      "title": "Days",
      "default": 28,
      "description": "Lookback period in days (default: 28)."
    },
    "row_limit": {
      "type": "integer",
      "title": "Row Limit",
      "default": 20,
      "description": "Max rows to return (default: 20, max: 100)."
    }
  },
  "title": "ga4_get_reportArguments",
  "required": []
}
```

</details>

- The 1–100 row limit is imposed in the handler, not JSON Schema. No positivity constraint is declared for days.

Source: [ga4_server.py:440](https://github.com/luminarylane/ga4-mcp/blob/90e80869b6ad043956e8fb2d551332d5dec5312a/ga4_server.py#L440-L491) · [ga4_server.py:376](https://github.com/luminarylane/ga4-mcp/blob/90e80869b6ad043956e8fb2d551332d5dec5312a/ga4_server.py#L376-L396) · [ga4_server.py:181](https://github.com/luminarylane/ga4-mcp/blob/90e80869b6ad043956e8fb2d551332d5dec5312a/ga4_server.py#L181-L254).

## ga4_get_top_pages

Report preset: calls run_report with pagePath dimension and sessions, totalUsers, screenPageViews, bounceRate, averageSessionDuration metrics; UTC date range from today minus days through today; row limit clamped to 1–100; descending sessions order. Returns a formatted text table.

<details>
<summary>Full registered description</summary>

```text
Get top pages by sessions. Shows page path, sessions, users, pageviews,
bounce rate, and average session duration.

Args:
    property_id: GA4 property ID (numeric). Leave empty to use GA4_PROPERTY_ID env var.
    days: Lookback period in days (default: 28).
    row_limit: Max rows to return (default: 20).
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | No | string | "" |
| `days` | No | integer | 28 |
| `row_limit` | No | integer | 20 |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "property_id": {
      "type": "string",
      "title": "Property Id",
      "default": "",
      "description": "GA4 property ID (numeric). Leave empty to use GA4_PROPERTY_ID env var."
    },
    "days": {
      "type": "integer",
      "title": "Days",
      "default": 28,
      "description": "Lookback period in days (default: 28)."
    },
    "row_limit": {
      "type": "integer",
      "title": "Row Limit",
      "default": 20,
      "description": "Max rows to return (default: 20)."
    }
  },
  "title": "ga4_get_top_pagesArguments",
  "required": []
}
```

</details>

- The handler clamps row_limit to 1–100 although its docstring does not mention the upper bound.

Source: [ga4_server.py:494](https://github.com/luminarylane/ga4-mcp/blob/90e80869b6ad043956e8fb2d551332d5dec5312a/ga4_server.py#L494-L536) · [ga4_server.py:376](https://github.com/luminarylane/ga4-mcp/blob/90e80869b6ad043956e8fb2d551332d5dec5312a/ga4_server.py#L376-L396) · [ga4_server.py:181](https://github.com/luminarylane/ga4-mcp/blob/90e80869b6ad043956e8fb2d551332d5dec5312a/ga4_server.py#L181-L254).

## ga4_get_traffic_sources

Report preset: calls run_report with sessionSource and sessionMedium dimensions and sessions, totalUsers, bounceRate, conversions metrics; UTC date range from today minus days through today; row limit clamped to 1–100; descending sessions order. Returns a formatted text table.

<details>
<summary>Full registered description</summary>

```text
Get traffic sources breakdown by source/medium. Shows sessions, users,
bounce rate, and conversions per traffic source.

Args:
    property_id: GA4 property ID (numeric). Leave empty to use GA4_PROPERTY_ID env var.
    days: Lookback period in days (default: 28).
    row_limit: Max rows to return (default: 20).
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | No | string | "" |
| `days` | No | integer | 28 |
| `row_limit` | No | integer | 20 |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "property_id": {
      "type": "string",
      "title": "Property Id",
      "default": "",
      "description": "GA4 property ID (numeric). Leave empty to use GA4_PROPERTY_ID env var."
    },
    "days": {
      "type": "integer",
      "title": "Days",
      "default": 28,
      "description": "Lookback period in days (default: 28)."
    },
    "row_limit": {
      "type": "integer",
      "title": "Row Limit",
      "default": 20,
      "description": "Max rows to return (default: 20)."
    }
  },
  "title": "ga4_get_traffic_sourcesArguments",
  "required": []
}
```

</details>

- The handler clamps row_limit to 1–100 although its docstring does not mention the upper bound.

Source: [ga4_server.py:539](https://github.com/luminarylane/ga4-mcp/blob/90e80869b6ad043956e8fb2d551332d5dec5312a/ga4_server.py#L539-L583) · [ga4_server.py:376](https://github.com/luminarylane/ga4-mcp/blob/90e80869b6ad043956e8fb2d551332d5dec5312a/ga4_server.py#L376-L396) · [ga4_server.py:181](https://github.com/luminarylane/ga4-mcp/blob/90e80869b6ad043956e8fb2d551332d5dec5312a/ga4_server.py#L181-L254).

## ga4_get_conversions

Report preset: calls run_report with eventName dimension and eventCount, totalUsers, conversions metrics; UTC date range from today minus days through today; row limit clamped to 1–100; descending eventCount order. Returns a formatted text table; no filter limits results to conversion events.

<details>
<summary>Full registered description</summary>

```text
Get conversion events and their counts. Shows which events are firing
and how often, broken down by event name.

Args:
    property_id: GA4 property ID (numeric). Leave empty to use GA4_PROPERTY_ID env var.
    days: Lookback period in days (default: 28).
    row_limit: Max rows to return (default: 20).
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | No | string | "" |
| `days` | No | integer | 28 |
| `row_limit` | No | integer | 20 |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "property_id": {
      "type": "string",
      "title": "Property Id",
      "default": "",
      "description": "GA4 property ID (numeric). Leave empty to use GA4_PROPERTY_ID env var."
    },
    "days": {
      "type": "integer",
      "title": "Days",
      "default": 28,
      "description": "Lookback period in days (default: 28)."
    },
    "row_limit": {
      "type": "integer",
      "title": "Row Limit",
      "default": 20,
      "description": "Max rows to return (default: 20)."
    }
  },
  "title": "ga4_get_conversionsArguments",
  "required": []
}
```

</details>

- All events are returned; the handler does not filter to conversion events. The handler clamps row_limit to 1–100 although its docstring does not mention the upper bound.

Source: [ga4_server.py:586](https://github.com/luminarylane/ga4-mcp/blob/90e80869b6ad043956e8fb2d551332d5dec5312a/ga4_server.py#L586-L628) · [ga4_server.py:376](https://github.com/luminarylane/ga4-mcp/blob/90e80869b6ad043956e8fb2d551332d5dec5312a/ga4_server.py#L376-L396) · [ga4_server.py:181](https://github.com/luminarylane/ga4-mcp/blob/90e80869b6ad043956e8fb2d551332d5dec5312a/ga4_server.py#L181-L254).

## ga4_get_realtime

Calls run_realtime_report with unifiedScreenName dimension, activeUsers metric and fixed limit 10. Sums activeUsers from returned rows and prints that sum plus page/user rows. Returns a no-active-users message when no rows are returned.

<details>
<summary>Full registered description</summary>

```text
Get realtime active users and current events on the site.
Shows what's happening RIGHT NOW — active users, top pages, traffic sources.

Args:
    property_id: GA4 property ID (numeric). Leave empty to use GA4_PROPERTY_ID env var.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | No | string | "" |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "property_id": {
      "type": "string",
      "title": "Property Id",
      "default": "",
      "description": "GA4 property ID (numeric). Leave empty to use GA4_PROPERTY_ID env var."
    }
  },
  "title": "ga4_get_realtimeArguments",
  "required": []
}
```

</details>

- Despite the description mentioning current events and traffic sources, only activeUsers grouped by unifiedScreenName is requested. The displayed total sums only up to 10 returned rows, not a separate property-wide aggregate.

Source: [ga4_server.py:631](https://github.com/luminarylane/ga4-mcp/blob/90e80869b6ad043956e8fb2d551332d5dec5312a/ga4_server.py#L631-L677) · [ga4_server.py:376](https://github.com/luminarylane/ga4-mcp/blob/90e80869b6ad043956e8fb2d551332d5dec5312a/ga4_server.py#L376-L396) · [ga4_server.py:181](https://github.com/luminarylane/ga4-mcp/blob/90e80869b6ad043956e8fb2d551332d5dec5312a/ga4_server.py#L181-L254).

## ga4_compare_periods

Splits comma-separated metric names and calls run_report with no requested dimensions and two date ranges: today minus days through today, and today minus twice days through today minus days. Treats first two returned rows as current and previous; formats absolute values and percent changes, using N/A for a zero previous value.

<details>
<summary>Full registered description</summary>

```text
Compare current period vs previous period for key metrics.
Shows absolute values and percentage change for each metric.

Args:
    property_id: GA4 property ID (numeric). Leave empty to use GA4_PROPERTY_ID env var.
    metrics: Comma-separated metrics to compare (default: sessions, users, pageviews,
             bounce rate, avg session duration, conversions).
    days: Period length in days (default: 28). Compares last N days vs the N days before that.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | No | string | "" |
| `metrics` | No | string | "sessions,totalUsers,screenPageViews,bounceRate,averageSessionDuration,conversions" |
| `days` | No | integer | 28 |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "property_id": {
      "type": "string",
      "title": "Property Id",
      "default": "",
      "description": "GA4 property ID (numeric). Leave empty to use GA4_PROPERTY_ID env var."
    },
    "metrics": {
      "type": "string",
      "title": "Metrics",
      "default": "sessions,totalUsers,screenPageViews,bounceRate,averageSessionDuration,conversions",
      "description": "Comma-separated metrics to compare (default: sessions, users, pageviews, bounce rate, avg session duration, conversions)."
    },
    "days": {
      "type": "integer",
      "title": "Days",
      "default": 28,
      "description": "Period length in days (default: 28). Compares last N days vs the N days before that."
    }
  },
  "title": "ga4_compare_periodsArguments",
  "required": []
}
```

</details>

- The two inclusive date ranges share their boundary date, and each contains days + 1 calendar dates. The handler assumes row order corresponds to current then previous rather than inspecting a dateRange dimension.

Source: [ga4_server.py:680](https://github.com/luminarylane/ga4-mcp/blob/90e80869b6ad043956e8fb2d551332d5dec5312a/ga4_server.py#L680-L767) · [ga4_server.py:376](https://github.com/luminarylane/ga4-mcp/blob/90e80869b6ad043956e8fb2d551332d5dec5312a/ga4_server.py#L376-L396) · [ga4_server.py:181](https://github.com/luminarylane/ga4-mcp/blob/90e80869b6ad043956e8fb2d551332d5dec5312a/ga4_server.py#L181-L254).

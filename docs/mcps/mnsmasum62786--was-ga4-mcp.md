# mnsmasum62786/was-ga4-mcp

[Catalog](../../README.md) · [All tool names](../tool-index.md) · [Upstream](https://github.com/mnsmasum62786/was-ga4-mcp) · [JSON](../../data/mcps/mnsmasum62786--was-ga4-mcp.json)

**31 tools:** 31 GA4, 0 other-service or server-support tools. Reviewed source: [`74d3244754dd`](https://github.com/mnsmasum62786/was-ga4-mcp/tree/74d3244754dde0d3cd3142de4d2e513796d38dca).

Descriptions and parameter schemas come from the registered source definitions. Generated schemas are reconstructed from annotations or validators; live `tools/list` and authenticated API calls were not run. Loose objects remain loose.

<details>
<summary>Exposure and compatibility notes</summary>

- Source review only, no tools/list or live requests; upstream code was not executed.
- All 31 tools are registered unconditionally; google-client.js exits during import if OAuth client ID, client secret or refresh token are missing. Credentials come from environment variables or ~/.was-ga4-mcp/config.json.
- cli.js auth/logout/status/help are CLI commands, not registered MCP tools. No optional modules or permission tiers were found.
- Shared client refreshes OAuth tokens and performs authenticated fetch, parsing JSON or raw text; server returns text JSON, truncates output above 60000 characters, and converts exceptions to isError responses.
- Server dispatcher passes arguments directly to handlers without explicit inputSchema validation or automatic default application.

</details>

## Tools

| Tool | Scope | Effect |
| --- | --- | --- |
| [`ga4_run_report`](#ga4_run_report) | GA4 | read |
| [`ga4_run_realtime_report`](#ga4_run_realtime_report) | GA4 | read |
| [`ga4_run_pivot_report`](#ga4_run_pivot_report) | GA4 | read |
| [`ga4_batch_run_reports`](#ga4_batch_run_reports) | GA4 | read |
| [`ga4_get_metadata`](#ga4_get_metadata) | GA4 | read |
| [`ga4_check_compatibility`](#ga4_check_compatibility) | GA4 | read |
| [`ga4_list_account_summaries`](#ga4_list_account_summaries) | GA4 | read |
| [`ga4_list_accounts`](#ga4_list_accounts) | GA4 | read |
| [`ga4_get_account`](#ga4_get_account) | GA4 | read |
| [`ga4_list_properties`](#ga4_list_properties) | GA4 | read |
| [`ga4_get_property`](#ga4_get_property) | GA4 | read |
| [`ga4_update_property`](#ga4_update_property) | GA4 | write |
| [`ga4_list_data_streams`](#ga4_list_data_streams) | GA4 | read |
| [`ga4_get_data_stream`](#ga4_get_data_stream) | GA4 | read |
| [`ga4_list_conversion_events`](#ga4_list_conversion_events) | GA4 | read |
| [`ga4_create_conversion_event`](#ga4_create_conversion_event) | GA4 | write |
| [`ga4_list_custom_dimensions`](#ga4_list_custom_dimensions) | GA4 | read |
| [`ga4_create_custom_dimension`](#ga4_create_custom_dimension) | GA4 | write |
| [`ga4_list_custom_metrics`](#ga4_list_custom_metrics) | GA4 | read |
| [`ga4_create_custom_metric`](#ga4_create_custom_metric) | GA4 | write |
| [`ga4_list_audiences`](#ga4_list_audiences) | GA4 | read |
| [`ga4_list_google_ads_links`](#ga4_list_google_ads_links) | GA4 | read |
| [`ga4_list_bigquery_links`](#ga4_list_bigquery_links) | GA4 | read |
| [`ga4_create_bigquery_link`](#ga4_create_bigquery_link) | GA4 | write |
| [`ga4_list_users`](#ga4_list_users) | GA4 | read |
| [`ga4_get_attribution_settings`](#ga4_get_attribution_settings) | GA4 | read |
| [`ga4_get_data_retention_settings`](#ga4_get_data_retention_settings) | GA4 | read |
| [`ga4_universal_call`](#ga4_universal_call) | GA4 | mixed |
| [`ga4_quick_overview`](#ga4_quick_overview) | GA4 | read |
| [`ga4_find_property`](#ga4_find_property) | GA4 | read |
| [`ga4_property_health_check`](#ga4_property_health_check) | GA4 | read |

## ga4_run_report

Posts selected report fields to /v1beta/properties/{propertyId}:runReport. Defaults dates to 7daysAgo–yesterday, dimensions to [], limit to 1000, offset to 0, keepEmptyRows to false; forwards supplied filters, ordering and currency.

<details>
<summary>Full registered description</summary>

```text
UNIVERSAL REPORT — run any GA4 report. propertyId is the numeric property ID.

dateRanges: array of { startDate, endDate }. Date format YYYY-MM-DD or relative like "today", "yesterday", "7daysAgo", "30daysAgo".

dimensions: array of { name } — examples: date, country, sessionDefaultChannelGroup, sessionSource, sessionMedium, deviceCategory, browser, pagePath, pageTitle, eventName, customEvent:my_param, audienceName, firstUserDefaultChannelGroup, etc.

metrics: array of { name } — examples: activeUsers, sessions, screenPageViews, eventCount, conversions, totalRevenue, engagedSessions, engagementRate, averageSessionDuration, bounceRate, transactions, purchaseRevenue, addToCarts, beginCheckouts.

dimensionFilter / metricFilter: filter expressions. Example: { "filter": { "fieldName": "sessionDefaultChannelGroup", "stringFilter": { "value": "Organic Search" } } }.

orderBys: [{ "dimension": { "dimensionName": "date" } }] or [{ "metric": { "metricName": "sessions" }, "desc": true }].

limit: max rows (default 1000, max 250000).
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `propertyId` | Yes | string | Not declared |
| `dateRanges` | No | array of object | [{"startDate": "7daysAgo", "endDate": "yesterday"}] |
| `dimensions` | No | array of object | Not declared |
| `metrics` | Yes | array of object | Not declared |
| `dimensionFilter` | No | object | Not declared |
| `metricFilter` | No | object | Not declared |
| `orderBys` | No | array of object | Not declared |
| `limit` | No | integer | 1000 |
| `offset` | No | integer | 0 |
| `keepEmptyRows` | No | boolean | false |
| `currencyCode` | No | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "propertyId": {
      "type": "string"
    },
    "dateRanges": {
      "type": "array",
      "items": {
        "type": "object"
      },
      "default": [
        {
          "startDate": "7daysAgo",
          "endDate": "yesterday"
        }
      ]
    },
    "dimensions": {
      "type": "array",
      "items": {
        "type": "object"
      }
    },
    "metrics": {
      "type": "array",
      "items": {
        "type": "object"
      }
    },
    "dimensionFilter": {
      "type": "object"
    },
    "metricFilter": {
      "type": "object"
    },
    "orderBys": {
      "type": "array",
      "items": {
        "type": "object"
      }
    },
    "limit": {
      "type": "integer",
      "default": 1000
    },
    "offset": {
      "type": "integer",
      "default": 0
    },
    "keepEmptyRows": {
      "type": "boolean",
      "default": false
    },
    "currencyCode": {
      "type": "string"
    }
  },
  "required": [
    "propertyId",
    "metrics"
  ]
}
```

</details>

- Exposed report objects/items are intentionally unrestricted object schemas; nested GA API fields are not specified. Handler forwards only the fields described in behavior.
- Description claims max limit 250000, but schema has no maximum and handler does not enforce it. Falsy limit (including 0) becomes 1000.

Source: [tools/data.js:8](https://github.com/mnsmasum62786/was-ga4-mcp/blob/74d3244754dde0d3cd3142de4d2e513796d38dca/tools/data.js#L8-L55) · [google-client.js:51](https://github.com/mnsmasum62786/was-ga4-mcp/blob/74d3244754dde0d3cd3142de4d2e513796d38dca/google-client.js#L51-L114).

## ga4_run_realtime_report

Posts metrics, dimensions (default []), limit (default 100) and optional filters/minuteRanges to /v1beta/properties/{propertyId}:runRealtimeReport.

<details>
<summary>Full registered description</summary>

```text
Real-time report (last 30 min of activity). Common metrics: activeUsers, screenPageViews, eventCount. Common dimensions: country, city, deviceCategory, browser, unifiedScreenName, eventName.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `propertyId` | Yes | string | Not declared |
| `dimensions` | No | array of object | Not declared |
| `metrics` | Yes | array of object | Not declared |
| `dimensionFilter` | No | object | Not declared |
| `metricFilter` | No | object | Not declared |
| `limit` | No | integer | 100 |
| `minuteRanges` | No | array of object | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "propertyId": {
      "type": "string"
    },
    "dimensions": {
      "type": "array",
      "items": {
        "type": "object"
      }
    },
    "metrics": {
      "type": "array",
      "items": {
        "type": "object"
      }
    },
    "dimensionFilter": {
      "type": "object"
    },
    "metricFilter": {
      "type": "object"
    },
    "limit": {
      "type": "integer",
      "default": 100
    },
    "minuteRanges": {
      "type": "array",
      "items": {
        "type": "object"
      },
      "description": "[{name, startMinutesAgo, endMinutesAgo}] — defaults to last 30 min"
    }
  },
  "required": [
    "propertyId",
    "metrics"
  ]
}
```

</details>

- Exposed report objects/items are intentionally unrestricted object schemas; nested GA API fields are not specified. Handler forwards only the fields described in behavior.

Source: [tools/data.js:56](https://github.com/mnsmasum62786/was-ga4-mcp/blob/74d3244754dde0d3cd3142de4d2e513796d38dca/tools/data.js#L56-L83) · [google-client.js:51](https://github.com/mnsmasum62786/was-ga4-mcp/blob/74d3244754dde0d3cd3142de4d2e513796d38dca/google-client.js#L51-L114).

## ga4_run_pivot_report

Posts metrics, pivots, dimensions (default []), dates (default 30daysAgo–yesterday) and optional dimensionFilter to /v1beta/properties/{propertyId}:runPivotReport.

<details>
<summary>Full registered description</summary>

```text
Pivoted report (cross-tabulation). Useful for heatmap-style breakdowns. pivots: [{ fieldNames: ["country"], limit: 10, orderBys: [...], offset: 0 }].
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `propertyId` | Yes | string | Not declared |
| `dateRanges` | No | array of object | [{"startDate": "30daysAgo", "endDate": "yesterday"}] |
| `dimensions` | No | array of object | Not declared |
| `metrics` | Yes | array of object | Not declared |
| `pivots` | Yes | array of object | Not declared |
| `dimensionFilter` | No | object | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "propertyId": {
      "type": "string"
    },
    "dateRanges": {
      "type": "array",
      "items": {
        "type": "object"
      },
      "default": [
        {
          "startDate": "30daysAgo",
          "endDate": "yesterday"
        }
      ]
    },
    "dimensions": {
      "type": "array",
      "items": {
        "type": "object"
      }
    },
    "metrics": {
      "type": "array",
      "items": {
        "type": "object"
      }
    },
    "pivots": {
      "type": "array",
      "items": {
        "type": "object"
      }
    },
    "dimensionFilter": {
      "type": "object"
    }
  },
  "required": [
    "propertyId",
    "metrics",
    "pivots"
  ]
}
```

</details>

- Exposed report objects/items are intentionally unrestricted object schemas; nested GA API fields are not specified. Handler forwards only the fields described in behavior.

Source: [tools/data.js:84](https://github.com/mnsmasum62786/was-ga4-mcp/blob/74d3244754dde0d3cd3142de4d2e513796d38dca/tools/data.js#L84-L106) · [google-client.js:51](https://github.com/mnsmasum62786/was-ga4-mcp/blob/74d3244754dde0d3cd3142de4d2e513796d38dca/google-client.js#L51-L114).

## ga4_batch_run_reports

Posts {requests} unchanged to /v1beta/properties/{propertyId}:batchRunReports.

<details>
<summary>Full registered description</summary>

```text
Run up to 5 reports in a single API call. Reduces round trips for dashboards. requests: array of report bodies (same shape as ga4_run_report).
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `propertyId` | Yes | string | Not declared |
| `requests` | Yes | array of object | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "propertyId": {
      "type": "string"
    },
    "requests": {
      "type": "array",
      "items": {
        "type": "object"
      },
      "minItems": 1,
      "maxItems": 5
    }
  },
  "required": [
    "propertyId",
    "requests"
  ]
}
```

</details>

- Exposed report objects/items are intentionally unrestricted object schemas; nested GA API fields are not specified. Handler forwards only the fields described in behavior.

Source: [tools/data.js:107](https://github.com/mnsmasum62786/was-ga4-mcp/blob/74d3244754dde0d3cd3142de4d2e513796d38dca/tools/data.js#L107-L119) · [google-client.js:51](https://github.com/mnsmasum62786/was-ga4-mcp/blob/74d3244754dde0d3cd3142de4d2e513796d38dca/google-client.js#L51-L114).

## ga4_get_metadata

Calls ga4Get with /v1beta/properties/{propertyId}/metadata. Shared routing sends this GET to analyticsadmin.googleapis.com rather than the Data API metadata endpoint.

<details>
<summary>Full registered description</summary>

```text
List all dimensions + metrics available for a property (including custom ones). Use to discover what you can query.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `propertyId` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "propertyId": {
      "type": "string"
    }
  },
  "required": [
    "propertyId"
  ]
}
```

</details>

- Defect: /metadata does not match ga4Get routing predicates (:getMetadata is checked instead), so request uses Admin API host and cannot fetch Data API metadata as intended.

Source: [tools/data.js:120](https://github.com/mnsmasum62786/was-ga4-mcp/blob/74d3244754dde0d3cd3142de4d2e513796d38dca/tools/data.js#L120-L125) · [google-client.js:51](https://github.com/mnsmasum62786/was-ga4-mcp/blob/74d3244754dde0d3cd3142de4d2e513796d38dca/google-client.js#L51-L114).

## ga4_check_compatibility

Posts dimensions and metrics, each defaulting to [], to /v1beta/properties/{propertyId}:checkCompatibility.

<details>
<summary>Full registered description</summary>

```text
Check whether requested dimensions + metrics are compatible (can be combined in one report).
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `propertyId` | Yes | string | Not declared |
| `dimensions` | No | array of object | Not declared |
| `metrics` | No | array of object | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "propertyId": {
      "type": "string"
    },
    "dimensions": {
      "type": "array",
      "items": {
        "type": "object"
      }
    },
    "metrics": {
      "type": "array",
      "items": {
        "type": "object"
      }
    }
  },
  "required": [
    "propertyId"
  ]
}
```

</details>

- Exposed report objects/items are intentionally unrestricted object schemas; nested GA API fields are not specified. Handler forwards only the fields described in behavior.

Source: [tools/data.js:126](https://github.com/mnsmasum62786/was-ga4-mcp/blob/74d3244754dde0d3cd3142de4d2e513796d38dca/tools/data.js#L126-L142) · [google-client.js:51](https://github.com/mnsmasum62786/was-ga4-mcp/blob/74d3244754dde0d3cd3142de4d2e513796d38dca/google-client.js#L51-L114).

## ga4_list_account_summaries

GET /v1beta/accountSummaries with pageSize default 200; returns the API response.

<details>
<summary>Full registered description</summary>

```text
List all GA4 account summaries the authenticated user can access. Each includes property summaries — fastest way to discover all properties.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `pageSize` | No | integer | 200 |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "pageSize": {
      "type": "integer",
      "default": 200
    }
  }
}
```

</details>

- No pagination loop or pageToken input: only first API response page is used.

Source: [tools/admin.js:9](https://github.com/mnsmasum62786/was-ga4-mcp/blob/74d3244754dde0d3cd3142de4d2e513796d38dca/tools/admin.js#L9-L14) · [google-client.js:51](https://github.com/mnsmasum62786/was-ga4-mcp/blob/74d3244754dde0d3cd3142de4d2e513796d38dca/google-client.js#L51-L114).

## ga4_list_accounts

GET /v1beta/accounts with pageSize default 50; returns the API response.

<details>
<summary>Full registered description</summary>

```text
List GA4 accounts.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `pageSize` | No | integer | 50 |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "pageSize": {
      "type": "integer",
      "default": 50
    }
  }
}
```

</details>

- No pagination loop or pageToken input: only first API response page is used.

Source: [tools/admin.js:15](https://github.com/mnsmasum62786/was-ga4-mcp/blob/74d3244754dde0d3cd3142de4d2e513796d38dca/tools/admin.js#L15-L20) · [google-client.js:51](https://github.com/mnsmasum62786/was-ga4-mcp/blob/74d3244754dde0d3cd3142de4d2e513796d38dca/google-client.js#L51-L114).

## ga4_get_account

GET /v1beta/accounts/{accountId}; directly appends supplied accountId.

<details>
<summary>Full registered description</summary>

```text
Get a single GA4 account by name. name format: accounts/{accountId}
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `accountId` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "accountId": {
      "type": "string"
    }
  },
  "required": [
    "accountId"
  ]
}
```

</details>

Source: [tools/admin.js:21](https://github.com/mnsmasum62786/was-ga4-mcp/blob/74d3244754dde0d3cd3142de4d2e513796d38dca/tools/admin.js#L21-L26) · [google-client.js:51](https://github.com/mnsmasum62786/was-ga4-mcp/blob/74d3244754dde0d3cd3142de4d2e513796d38dca/google-client.js#L51-L114).

## ga4_list_properties

GET /v1beta/properties with filter parent:accounts/{accountId}, pageSize default 100, and showDeleted default false.

<details>
<summary>Full registered description</summary>

```text
List GA4 properties under an account. accountId must be the numeric ID (without "accounts/" prefix).
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `accountId` | Yes | string | Not declared |
| `pageSize` | No | integer | 100 |
| `showDeleted` | No | boolean | false |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "accountId": {
      "type": "string",
      "description": "Numeric account ID (e.g. 111368097)"
    },
    "pageSize": {
      "type": "integer",
      "default": 100
    },
    "showDeleted": {
      "type": "boolean",
      "default": false
    }
  },
  "required": [
    "accountId"
  ]
}
```

</details>

- No pagination loop or pageToken input: only first API response page is used.

Source: [tools/admin.js:27](https://github.com/mnsmasum62786/was-ga4-mcp/blob/74d3244754dde0d3cd3142de4d2e513796d38dca/tools/admin.js#L27-L44) · [google-client.js:51](https://github.com/mnsmasum62786/was-ga4-mcp/blob/74d3244754dde0d3cd3142de4d2e513796d38dca/google-client.js#L51-L114).

## ga4_get_property

GET /v1beta/properties/{propertyId}; returns property settings.

<details>
<summary>Full registered description</summary>

```text
Get a single property's settings.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `propertyId` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "propertyId": {
      "type": "string"
    }
  },
  "required": [
    "propertyId"
  ]
}
```

</details>

Source: [tools/admin.js:45](https://github.com/mnsmasum62786/was-ga4-mcp/blob/74d3244754dde0d3cd3142de4d2e513796d38dca/tools/admin.js#L45-L50) · [google-client.js:51](https://github.com/mnsmasum62786/was-ga4-mcp/blob/74d3244754dde0d3cd3142de4d2e513796d38dca/google-client.js#L51-L114).

## ga4_update_property

PATCH /v1beta/properties/{propertyId}?updateMask={encoded updateMask} using payload unchanged.

<details>
<summary>Full registered description</summary>

```text
Update GA4 property fields. updateMask is comma-separated list of fields to update (e.g. "displayName,timeZone,currencyCode,industryCategory").
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `propertyId` | Yes | string | Not declared |
| `updateMask` | Yes | string | Not declared |
| `payload` | Yes | object | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "propertyId": {
      "type": "string"
    },
    "updateMask": {
      "type": "string"
    },
    "payload": {
      "type": "object",
      "description": "Fields to update — displayName, timeZone, currencyCode, industryCategory"
    }
  },
  "required": [
    "propertyId",
    "updateMask",
    "payload"
  ]
}
```

</details>

Source: [tools/admin.js:51](https://github.com/mnsmasum62786/was-ga4-mcp/blob/74d3244754dde0d3cd3142de4d2e513796d38dca/tools/admin.js#L51-L64) · [google-client.js:51](https://github.com/mnsmasum62786/was-ga4-mcp/blob/74d3244754dde0d3cd3142de4d2e513796d38dca/google-client.js#L51-L114).

## ga4_list_data_streams

GET /v1beta/properties/{propertyId}/dataStreams.

<details>
<summary>Full registered description</summary>

```text
List data streams in a GA4 property (web, app, etc.).
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `propertyId` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "propertyId": {
      "type": "string"
    }
  },
  "required": [
    "propertyId"
  ]
}
```

</details>

- No pagination loop or pageToken input: only first API response page is used.

Source: [tools/admin.js:65](https://github.com/mnsmasum62786/was-ga4-mcp/blob/74d3244754dde0d3cd3142de4d2e513796d38dca/tools/admin.js#L65-L70) · [google-client.js:51](https://github.com/mnsmasum62786/was-ga4-mcp/blob/74d3244754dde0d3cd3142de4d2e513796d38dca/google-client.js#L51-L114).

## ga4_get_data_stream

GET /v1beta/properties/{propertyId}/dataStreams/{streamId}.

<details>
<summary>Full registered description</summary>

```text
Get a data stream by ID, including the measurement ID and stream-specific settings.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `propertyId` | Yes | string | Not declared |
| `streamId` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "propertyId": {
      "type": "string"
    },
    "streamId": {
      "type": "string"
    }
  },
  "required": [
    "propertyId",
    "streamId"
  ]
}
```

</details>

Source: [tools/admin.js:71](https://github.com/mnsmasum62786/was-ga4-mcp/blob/74d3244754dde0d3cd3142de4d2e513796d38dca/tools/admin.js#L71-L80) · [google-client.js:51](https://github.com/mnsmasum62786/was-ga4-mcp/blob/74d3244754dde0d3cd3142de4d2e513796d38dca/google-client.js#L51-L114).

## ga4_list_conversion_events

GET /v1beta/properties/{propertyId}/keyEvents; uses key events despite the conversion-events tool name.

<details>
<summary>Full registered description</summary>

```text
List configured conversion events on a property.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `propertyId` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "propertyId": {
      "type": "string"
    }
  },
  "required": [
    "propertyId"
  ]
}
```

</details>

- No pagination loop or pageToken input: only first API response page is used.

Source: [tools/admin.js:81](https://github.com/mnsmasum62786/was-ga4-mcp/blob/74d3244754dde0d3cd3142de4d2e513796d38dca/tools/admin.js#L81-L86) · [google-client.js:51](https://github.com/mnsmasum62786/was-ga4-mcp/blob/74d3244754dde0d3cd3142de4d2e513796d38dca/google-client.js#L51-L114).

## ga4_create_conversion_event

POST /v1beta/properties/{propertyId}/keyEvents with eventName, countingMethod default ONCE_PER_EVENT, and optional defaultValue unchanged.

<details>
<summary>Full registered description</summary>

```text
Mark an event as a key event (conversion). eventName is the event name to mark (e.g. "purchase", "generate_lead", "form_submit"). countingMethod: ONCE_PER_EVENT or ONCE_PER_SESSION.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `propertyId` | Yes | string | Not declared |
| `eventName` | Yes | string | Not declared |
| `countingMethod` | No | string | "ONCE_PER_EVENT" |
| `defaultValue` | No | object | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "propertyId": {
      "type": "string"
    },
    "eventName": {
      "type": "string"
    },
    "countingMethod": {
      "type": "string",
      "enum": [
        "ONCE_PER_EVENT",
        "ONCE_PER_SESSION"
      ],
      "default": "ONCE_PER_EVENT"
    },
    "defaultValue": {
      "type": "object",
      "description": "{ numericValue: 0, currencyCode: \"USD\" }"
    }
  },
  "required": [
    "propertyId",
    "eventName"
  ]
}
```

</details>

Source: [tools/admin.js:87](https://github.com/mnsmasum62786/was-ga4-mcp/blob/74d3244754dde0d3cd3142de4d2e513796d38dca/tools/admin.js#L87-L105) · [google-client.js:51](https://github.com/mnsmasum62786/was-ga4-mcp/blob/74d3244754dde0d3cd3142de4d2e513796d38dca/google-client.js#L51-L114).

## ga4_list_custom_dimensions

GET /v1beta/properties/{propertyId}/customDimensions.

<details>
<summary>Full registered description</summary>

```text
List custom dimensions on a property.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `propertyId` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "propertyId": {
      "type": "string"
    }
  },
  "required": [
    "propertyId"
  ]
}
```

</details>

- No pagination loop or pageToken input: only first API response page is used.

Source: [tools/admin.js:106](https://github.com/mnsmasum62786/was-ga4-mcp/blob/74d3244754dde0d3cd3142de4d2e513796d38dca/tools/admin.js#L106-L111) · [google-client.js:51](https://github.com/mnsmasum62786/was-ga4-mcp/blob/74d3244754dde0d3cd3142de4d2e513796d38dca/google-client.js#L51-L114).

## ga4_create_custom_dimension

POST /v1beta/properties/{propertyId}/customDimensions with displayName, parameterName, scope default EVENT, and supplied description/disallowAdsPersonalization.

<details>
<summary>Full registered description</summary>

```text
Create a custom dimension. scope: EVENT | USER | ITEM. parameterName is the event/user parameter to bind.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `propertyId` | Yes | string | Not declared |
| `displayName` | Yes | string | Not declared |
| `parameterName` | Yes | string | Not declared |
| `scope` | No | string | "EVENT" |
| `description` | No | string | Not declared |
| `disallowAdsPersonalization` | No | boolean | false |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "propertyId": {
      "type": "string"
    },
    "displayName": {
      "type": "string"
    },
    "parameterName": {
      "type": "string"
    },
    "scope": {
      "type": "string",
      "enum": [
        "EVENT",
        "USER",
        "ITEM"
      ],
      "default": "EVENT"
    },
    "description": {
      "type": "string"
    },
    "disallowAdsPersonalization": {
      "type": "boolean",
      "default": false
    }
  },
  "required": [
    "propertyId",
    "displayName",
    "parameterName"
  ]
}
```

</details>

- Schema default disallowAdsPersonalization=false is not applied in handler; omitted field is undefined and omitted during JSON serialization.

Source: [tools/admin.js:112](https://github.com/mnsmasum62786/was-ga4-mcp/blob/74d3244754dde0d3cd3142de4d2e513796d38dca/tools/admin.js#L112-L134) · [google-client.js:51](https://github.com/mnsmasum62786/was-ga4-mcp/blob/74d3244754dde0d3cd3142de4d2e513796d38dca/google-client.js#L51-L114).

## ga4_list_custom_metrics

GET /v1beta/properties/{propertyId}/customMetrics.

<details>
<summary>Full registered description</summary>

```text
List custom metrics on a property.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `propertyId` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "propertyId": {
      "type": "string"
    }
  },
  "required": [
    "propertyId"
  ]
}
```

</details>

- No pagination loop or pageToken input: only first API response page is used.

Source: [tools/admin.js:135](https://github.com/mnsmasum62786/was-ga4-mcp/blob/74d3244754dde0d3cd3142de4d2e513796d38dca/tools/admin.js#L135-L140) · [google-client.js:51](https://github.com/mnsmasum62786/was-ga4-mcp/blob/74d3244754dde0d3cd3142de4d2e513796d38dca/google-client.js#L51-L114).

## ga4_create_custom_metric

POST /v1beta/properties/{propertyId}/customMetrics with displayName, parameterName, scope default EVENT, measurementUnit, description and restrictedMetricType.

<details>
<summary>Full registered description</summary>

```text
Create a custom metric. measurementUnit: STANDARD | CURRENCY | FEET | METERS | KILOMETERS | MILES | MILLISECONDS | SECONDS | MINUTES | HOURS.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `propertyId` | Yes | string | Not declared |
| `displayName` | Yes | string | Not declared |
| `parameterName` | Yes | string | Not declared |
| `scope` | No | string | "EVENT" |
| `measurementUnit` | Yes | string | "STANDARD" |
| `description` | No | string | Not declared |
| `restrictedMetricType` | No | array of string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "propertyId": {
      "type": "string"
    },
    "displayName": {
      "type": "string"
    },
    "parameterName": {
      "type": "string"
    },
    "scope": {
      "type": "string",
      "enum": [
        "EVENT"
      ],
      "default": "EVENT"
    },
    "measurementUnit": {
      "type": "string",
      "default": "STANDARD"
    },
    "description": {
      "type": "string"
    },
    "restrictedMetricType": {
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  },
  "required": [
    "propertyId",
    "displayName",
    "parameterName",
    "measurementUnit"
  ]
}
```

</details>

- measurementUnit is required despite its schema default STANDARD; handler does not apply that default. No enum constrains measurementUnit beyond its description.

Source: [tools/admin.js:141](https://github.com/mnsmasum62786/was-ga4-mcp/blob/74d3244754dde0d3cd3142de4d2e513796d38dca/tools/admin.js#L141-L165) · [google-client.js:51](https://github.com/mnsmasum62786/was-ga4-mcp/blob/74d3244754dde0d3cd3142de4d2e513796d38dca/google-client.js#L51-L114).

## ga4_list_audiences

GET /v1beta/properties/{propertyId}/audiences with pageSize default 50.

<details>
<summary>Full registered description</summary>

```text
List audiences on a property.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `propertyId` | Yes | string | Not declared |
| `pageSize` | No | integer | 50 |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "propertyId": {
      "type": "string"
    },
    "pageSize": {
      "type": "integer",
      "default": 50
    }
  },
  "required": [
    "propertyId"
  ]
}
```

</details>

- No pagination loop or pageToken input: only first API response page is used.

Source: [tools/admin.js:166](https://github.com/mnsmasum62786/was-ga4-mcp/blob/74d3244754dde0d3cd3142de4d2e513796d38dca/tools/admin.js#L166-L171) · [google-client.js:51](https://github.com/mnsmasum62786/was-ga4-mcp/blob/74d3244754dde0d3cd3142de4d2e513796d38dca/google-client.js#L51-L114).

## ga4_list_google_ads_links

GET /v1beta/properties/{propertyId}/googleAdsLinks.

<details>
<summary>Full registered description</summary>

```text
List Google Ads accounts linked to this property.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `propertyId` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "propertyId": {
      "type": "string"
    }
  },
  "required": [
    "propertyId"
  ]
}
```

</details>

- No pagination loop or pageToken input: only first API response page is used.

Source: [tools/admin.js:172](https://github.com/mnsmasum62786/was-ga4-mcp/blob/74d3244754dde0d3cd3142de4d2e513796d38dca/tools/admin.js#L172-L177) · [google-client.js:51](https://github.com/mnsmasum62786/was-ga4-mcp/blob/74d3244754dde0d3cd3142de4d2e513796d38dca/google-client.js#L51-L114).

## ga4_list_bigquery_links

GET /v1beta/properties/{propertyId}/bigQueryLinks.

<details>
<summary>Full registered description</summary>

```text
List BigQuery export links on a property.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `propertyId` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "propertyId": {
      "type": "string"
    }
  },
  "required": [
    "propertyId"
  ]
}
```

</details>

- No pagination loop or pageToken input: only first API response page is used.

Source: [tools/admin.js:178](https://github.com/mnsmasum62786/was-ga4-mcp/blob/74d3244754dde0d3cd3142de4d2e513796d38dca/tools/admin.js#L178-L183) · [google-client.js:51](https://github.com/mnsmasum62786/was-ga4-mcp/blob/74d3244754dde0d3cd3142de4d2e513796d38dca/google-client.js#L51-L114).

## ga4_create_bigquery_link

POST /v1beta/properties/{propertyId}/bigQueryLinks with project prefixed projects/, dataLocation default US, dailyExportEnabled/includeAdvertisingId true unless explicitly false, streamingExportEnabled true only when explicitly true, and excludedEvents default [].

<details>
<summary>Full registered description</summary>

```text
Create a BigQuery export link. project must be a GCP project ID. dataLocation: US | EU | asia-south1 | etc. dailyExportEnabled = true for daily exports, streamingExportEnabled = true for streaming.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `propertyId` | Yes | string | Not declared |
| `project` | Yes | string | Not declared |
| `dataLocation` | No | string | "US" |
| `dailyExportEnabled` | No | boolean | true |
| `streamingExportEnabled` | No | boolean | false |
| `includeAdvertisingId` | No | boolean | true |
| `excludedEvents` | No | array of string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "propertyId": {
      "type": "string"
    },
    "project": {
      "type": "string",
      "description": "GCP project ID (NOT number)"
    },
    "dataLocation": {
      "type": "string",
      "default": "US"
    },
    "dailyExportEnabled": {
      "type": "boolean",
      "default": true
    },
    "streamingExportEnabled": {
      "type": "boolean",
      "default": false
    },
    "includeAdvertisingId": {
      "type": "boolean",
      "default": true
    },
    "excludedEvents": {
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  },
  "required": [
    "propertyId",
    "project"
  ]
}
```

</details>

Source: [tools/admin.js:184](https://github.com/mnsmasum62786/was-ga4-mcp/blob/74d3244754dde0d3cd3142de4d2e513796d38dca/tools/admin.js#L184-L208) · [google-client.js:51](https://github.com/mnsmasum62786/was-ga4-mcp/blob/74d3244754dde0d3cd3142de4d2e513796d38dca/google-client.js#L51-L114).

## ga4_list_users

GET /v1beta/{parent}/accessBindings; parent directly supplies accounts/{id} or properties/{id} path.

<details>
<summary>Full registered description</summary>

```text
List access bindings (users) on an account or property. parent format: accounts/{id} or properties/{id}.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `parent` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "parent": {
      "type": "string"
    }
  },
  "required": [
    "parent"
  ]
}
```

</details>

- No pagination loop or pageToken input: only first API response page is used.

Source: [tools/admin.js:209](https://github.com/mnsmasum62786/was-ga4-mcp/blob/74d3244754dde0d3cd3142de4d2e513796d38dca/tools/admin.js#L209-L214) · [google-client.js:51](https://github.com/mnsmasum62786/was-ga4-mcp/blob/74d3244754dde0d3cd3142de4d2e513796d38dca/google-client.js#L51-L114).

## ga4_get_attribution_settings

GET /v1beta/properties/{propertyId}/attributionSettings.

<details>
<summary>Full registered description</summary>

```text
Get the attribution model settings for a property.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `propertyId` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "propertyId": {
      "type": "string"
    }
  },
  "required": [
    "propertyId"
  ]
}
```

</details>

Source: [tools/admin.js:215](https://github.com/mnsmasum62786/was-ga4-mcp/blob/74d3244754dde0d3cd3142de4d2e513796d38dca/tools/admin.js#L215-L220) · [google-client.js:51](https://github.com/mnsmasum62786/was-ga4-mcp/blob/74d3244754dde0d3cd3142de4d2e513796d38dca/google-client.js#L51-L114).

## ga4_get_data_retention_settings

GET /v1beta/properties/{propertyId}/dataRetentionSettings.

<details>
<summary>Full registered description</summary>

```text
Get the data retention period for a property.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `propertyId` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "propertyId": {
      "type": "string"
    }
  },
  "required": [
    "propertyId"
  ]
}
```

</details>

Source: [tools/admin.js:221](https://github.com/mnsmasum62786/was-ga4-mcp/blob/74d3244754dde0d3cd3142de4d2e513796d38dca/tools/admin.js#L221-L226) · [google-client.js:51](https://github.com/mnsmasum62786/was-ga4-mcp/blob/74d3244754dde0d3cd3142de4d2e513796d38dca/google-client.js#L51-L114).

## ga4_universal_call

Passes method (default GET), arbitrary fullUrl and optional body to googleFetch. Uses the same OAuth bearer token and JSON serialization; returns parsed response or raw text.

<details>
<summary>Full registered description</summary>

```text
UNIVERSAL — call any GA4 Data or Admin API endpoint. Use when no specialized tool exists. fullUrl must be the complete https URL (e.g. https://analyticsadmin.googleapis.com/v1beta/...).
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `method` | No | string | "GET" |
| `fullUrl` | Yes | string | Not declared |
| `body` | No | any | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "method": {
      "type": "string",
      "enum": [
        "GET",
        "POST",
        "PATCH",
        "DELETE"
      ],
      "default": "GET"
    },
    "fullUrl": {
      "type": "string"
    },
    "body": {
      "description": "JSON body for POST/PATCH"
    }
  },
  "required": [
    "fullUrl"
  ]
}
```

</details>

- fullUrl has no format/host/protocol restriction and handler does not restrict it to Google/GA4; body has no type restriction.

Source: [tools/helpers.js:8](https://github.com/mnsmasum62786/was-ga4-mcp/blob/74d3244754dde0d3cd3142de4d2e513796d38dca/tools/helpers.js#L8-L21) · [google-client.js:51](https://github.com/mnsmasum62786/was-ga4-mcp/blob/74d3244754dde0d3cd3142de4d2e513796d38dca/google-client.js#L51-L114).

## ga4_quick_overview

GET /v1beta/accountSummaries with pageSize 200, counts accounts and property summaries, returns first 10 account summaries and up to 3 sample properties per account.

<details>
<summary>Full registered description</summary>

```text
Cross-property snapshot: count of accessible accounts + properties + recent activity. Great as a starting point.
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

- No pagination loop or pageToken input: only first API response page is used.
- Description mentions recent activity, but implementation only reads account summaries and does not query activity.

Source: [tools/helpers.js:22](https://github.com/mnsmasum62786/was-ga4-mcp/blob/74d3244754dde0d3cd3142de4d2e513796d38dca/tools/helpers.js#L22-L45) · [google-client.js:51](https://github.com/mnsmasum62786/was-ga4-mcp/blob/74d3244754dde0d3cd3142de4d2e513796d38dca/google-client.js#L51-L114).

## ga4_find_property

GET /v1beta/accountSummaries with pageSize 500; scans property display names case-insensitively, using equality if exact is truthy and substring matching otherwise; returns match count and account/property metadata.

<details>
<summary>Full registered description</summary>

```text
Search across all your account summaries for properties matching a name substring (case-insensitive).
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `name` | Yes | string | Not declared |
| `exact` | No | boolean | false |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string"
    },
    "exact": {
      "type": "boolean",
      "default": false
    }
  },
  "required": [
    "name"
  ]
}
```

</details>

- No pagination loop or pageToken input: only first API response page is used.

Source: [tools/helpers.js:46](https://github.com/mnsmasum62786/was-ga4-mcp/blob/74d3244754dde0d3cd3142de4d2e513796d38dca/tools/helpers.js#L46-L79) · [google-client.js:51](https://github.com/mnsmasum62786/was-ga4-mcp/blob/74d3244754dde0d3cd3142de4d2e513796d38dca/google-client.js#L51-L114).

## ga4_property_health_check

Concurrently runs a report comparing yesterday and 7daysAgo for activeUsers, sessions, eventCount and conversions, lists key events and data streams. Returns raw report, event count/names, stream count and stream metadata. Each request catches errors independently.

<details>
<summary>Full registered description</summary>

```text
Quick health report for a property: yesterday vs 7-day-ago totals, conversion event count, data stream count, last data received hint.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `propertyId` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "propertyId": {
      "type": "string"
    }
  },
  "required": [
    "propertyId"
  ]
}
```

</details>

- No pagination loop or pageToken input: only first API response page is used.
- Description mentions last data received hint, but no such field is computed. Key-event/stream request errors are hidden as zero counts/empty arrays; report errors appear in yesterdayVs7dAgo.

Source: [tools/helpers.js:80](https://github.com/mnsmasum62786/was-ga4-mcp/blob/74d3244754dde0d3cd3142de4d2e513796d38dca/tools/helpers.js#L80-L109) · [google-client.js:51](https://github.com/mnsmasum62786/was-ga4-mcp/blob/74d3244754dde0d3cd3142de4d2e513796d38dca/google-client.js#L51-L114).

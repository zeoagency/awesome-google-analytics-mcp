# onionst/ga4-toolkit

[Catalog](../../README.md) · [All tool names](../tool-index.md) · [Upstream](https://github.com/onionst/ga4-toolkit) · [JSON](../../data/mcps/onionst--ga4-toolkit.json)

**8 tools:** 8 GA4, 0 other-service or server-support tools. Reviewed source: [`1fbfe9e929db`](https://github.com/onionst/ga4-toolkit/tree/1fbfe9e929dbdb055e556318b152be675e60071c).

Descriptions and parameter schemas come from the registered source definitions. Generated schemas are reconstructed from annotations or validators; live `tools/list` and authenticated API calls were not run. Loose objects remain loose.

<details>
<summary>Exposure and compatibility notes</summary>

- Source review only, no tools/list or live requests.
- No .git directory exists; supplied revision is authoritative.
- All eight registrations are unconditional. CLI auth/config commands are not MCP tools.
- Credentials load lazily from GOOGLE_APPLICATION_CREDENTIALS, local ga4-cli/google-credentials.json or Google ADC with analytics.readonly scope. Python >=3.11 and declared google-auth, mcp and requests dependencies are required; no definite entrypoint blocker found.

</details>

## Tools

| Tool | Scope | Effect |
| --- | --- | --- |
| [`ga4_list_properties`](#ga4_list_properties) | GA4 | read |
| [`ga4_overview`](#ga4_overview) | GA4 | read |
| [`ga4_top_pages`](#ga4_top_pages) | GA4 | read |
| [`ga4_acquisition`](#ga4_acquisition) | GA4 | read |
| [`ga4_events`](#ga4_events) | GA4 | read |
| [`ga4_run_report`](#ga4_run_report) | GA4 | read |
| [`ga4_realtime`](#ga4_realtime) | GA4 | read |
| [`ga4_metadata`](#ga4_metadata) | GA4 | read |

## ga4_list_properties

Paginate Admin API accountSummaries with pageSize 200 and nextPageToken; flatten account and property summaries into account_id, account_name, property_id, property_name and property_type.

<details>
<summary>Full registered description</summary>

```text
List every GA4 property accessible with the current read-only credentials.
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
  "title": "ga4_list_propertiesArguments"
}
```

</details>

Source: [src/ga4_toolkit/mcp_server.py:28](https://github.com/onionst/ga4-toolkit/blob/1fbfe9e929dbdb055e556318b152be675e60071c/src/ga4_toolkit/mcp_server.py#L28-L31) · [src/ga4_toolkit/client.py:179](https://github.com/onionst/ga4-toolkit/blob/1fbfe9e929dbdb055e556318b152be675e60071c/src/ga4_toolkit/client.py#L179-L207).

## ga4_overview

Run historical report with date dimension and activeUsers, newUsers, sessions, engagedSessions, engagementRate, keyEvents and totalRevenue metrics, fixed limit 366; return flattened rows.

<details>
<summary>Full registered description</summary>

```text
Return daily users, sessions, engagement, key events, and revenue.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |
| `start_date` | No | string | "28daysAgo" |
| `end_date` | No | string | "yesterday" |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "property_id": {
      "type": "string",
      "title": "Property Id"
    },
    "start_date": {
      "type": "string",
      "title": "Start Date",
      "default": "28daysAgo"
    },
    "end_date": {
      "type": "string",
      "title": "End Date",
      "default": "yesterday"
    }
  },
  "required": [
    "property_id"
  ],
  "title": "ga4_overviewArguments"
}
```

</details>

- Property IDs are stripped, accept a properties/ prefix, and must then be numeric; this restriction is enforced by the handler, not the exposed schema.
- Reports fetch one page only; flattened output includes row counts, truncation warnings, metadata and quota. No automatic report pagination.

Source: [src/ga4_toolkit/mcp_server.py:34](https://github.com/onionst/ga4-toolkit/blob/1fbfe9e929dbdb055e556318b152be675e60071c/src/ga4_toolkit/mcp_server.py#L34-L48) · [src/ga4_toolkit/client.py:209](https://github.com/onionst/ga4-toolkit/blob/1fbfe9e929dbdb055e556318b152be675e60071c/src/ga4_toolkit/client.py#L209-L248) · [src/ga4_toolkit/presets.py:8](https://github.com/onionst/ga4-toolkit/blob/1fbfe9e929dbdb055e556318b152be675e60071c/src/ga4_toolkit/presets.py#L8-L30) · [src/ga4_toolkit/client.py:71](https://github.com/onionst/ga4-toolkit/blob/1fbfe9e929dbdb055e556318b152be675e60071c/src/ga4_toolkit/client.py#L71-L112) · [src/ga4_toolkit/client.py:307](https://github.com/onionst/ga4-toolkit/blob/1fbfe9e929dbdb055e556318b152be675e60071c/src/ga4_toolkit/client.py#L307-L336).

## ga4_top_pages

Run historical report with pagePath/pageTitle dimensions and screenPageViews, activeUsers, sessions, engagementRate metrics, ordered by screenPageViews descending; return flattened rows.

<details>
<summary>Full registered description</summary>

```text
Return top page paths and titles ordered by page views.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |
| `start_date` | No | string | "28daysAgo" |
| `end_date` | No | string | "yesterday" |
| `limit` | No | integer | 25 |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "property_id": {
      "type": "string",
      "title": "Property Id"
    },
    "start_date": {
      "type": "string",
      "title": "Start Date",
      "default": "28daysAgo"
    },
    "end_date": {
      "type": "string",
      "title": "End Date",
      "default": "yesterday"
    },
    "limit": {
      "type": "integer",
      "title": "Limit",
      "default": 25
    }
  },
  "required": [
    "property_id"
  ],
  "title": "ga4_top_pagesArguments"
}
```

</details>

- Property IDs are stripped, accept a properties/ prefix, and must then be numeric; this restriction is enforced by the handler, not the exposed schema.
- Reports fetch one page only; flattened output includes row counts, truncation warnings, metadata and quota. No automatic report pagination.
- Handler enforces limit between 1 and 10000; no bounds are declared in the exposed schema.

Source: [src/ga4_toolkit/mcp_server.py:51](https://github.com/onionst/ga4-toolkit/blob/1fbfe9e929dbdb055e556318b152be675e60071c/src/ga4_toolkit/mcp_server.py#L51-L67) · [src/ga4_toolkit/client.py:209](https://github.com/onionst/ga4-toolkit/blob/1fbfe9e929dbdb055e556318b152be675e60071c/src/ga4_toolkit/client.py#L209-L248) · [src/ga4_toolkit/presets.py:33](https://github.com/onionst/ga4-toolkit/blob/1fbfe9e929dbdb055e556318b152be675e60071c/src/ga4_toolkit/presets.py#L33-L49) · [src/ga4_toolkit/client.py:71](https://github.com/onionst/ga4-toolkit/blob/1fbfe9e929dbdb055e556318b152be675e60071c/src/ga4_toolkit/client.py#L71-L112) · [src/ga4_toolkit/client.py:307](https://github.com/onionst/ga4-toolkit/blob/1fbfe9e929dbdb055e556318b152be675e60071c/src/ga4_toolkit/client.py#L307-L336).

## ga4_acquisition

Run historical report with sessionDefaultChannelGroup/sessionSourceMedium dimensions and sessions, activeUsers, engagedSessions, keyEvents metrics, ordered by sessions descending; return flattened rows.

<details>
<summary>Full registered description</summary>

```text
Return session channels and source/medium acquisition performance.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |
| `start_date` | No | string | "28daysAgo" |
| `end_date` | No | string | "yesterday" |
| `limit` | No | integer | 25 |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "property_id": {
      "type": "string",
      "title": "Property Id"
    },
    "start_date": {
      "type": "string",
      "title": "Start Date",
      "default": "28daysAgo"
    },
    "end_date": {
      "type": "string",
      "title": "End Date",
      "default": "yesterday"
    },
    "limit": {
      "type": "integer",
      "title": "Limit",
      "default": 25
    }
  },
  "required": [
    "property_id"
  ],
  "title": "ga4_acquisitionArguments"
}
```

</details>

- Property IDs are stripped, accept a properties/ prefix, and must then be numeric; this restriction is enforced by the handler, not the exposed schema.
- Reports fetch one page only; flattened output includes row counts, truncation warnings, metadata and quota. No automatic report pagination.
- Handler enforces limit between 1 and 10000; no bounds are declared in the exposed schema.

Source: [src/ga4_toolkit/mcp_server.py:70](https://github.com/onionst/ga4-toolkit/blob/1fbfe9e929dbdb055e556318b152be675e60071c/src/ga4_toolkit/mcp_server.py#L70-L86) · [src/ga4_toolkit/client.py:209](https://github.com/onionst/ga4-toolkit/blob/1fbfe9e929dbdb055e556318b152be675e60071c/src/ga4_toolkit/client.py#L209-L248) · [src/ga4_toolkit/presets.py:52](https://github.com/onionst/ga4-toolkit/blob/1fbfe9e929dbdb055e556318b152be675e60071c/src/ga4_toolkit/presets.py#L52-L68) · [src/ga4_toolkit/client.py:71](https://github.com/onionst/ga4-toolkit/blob/1fbfe9e929dbdb055e556318b152be675e60071c/src/ga4_toolkit/client.py#L71-L112) · [src/ga4_toolkit/client.py:307](https://github.com/onionst/ga4-toolkit/blob/1fbfe9e929dbdb055e556318b152be675e60071c/src/ga4_toolkit/client.py#L307-L336).

## ga4_events

Run historical report with eventName dimension and eventCount, totalUsers, keyEvents, eventValue metrics, ordered by eventCount descending; return flattened rows.

<details>
<summary>Full registered description</summary>

```text
Return top GA4 events, users, key events, and event values.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |
| `start_date` | No | string | "28daysAgo" |
| `end_date` | No | string | "yesterday" |
| `limit` | No | integer | 25 |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "property_id": {
      "type": "string",
      "title": "Property Id"
    },
    "start_date": {
      "type": "string",
      "title": "Start Date",
      "default": "28daysAgo"
    },
    "end_date": {
      "type": "string",
      "title": "End Date",
      "default": "yesterday"
    },
    "limit": {
      "type": "integer",
      "title": "Limit",
      "default": 25
    }
  },
  "required": [
    "property_id"
  ],
  "title": "ga4_eventsArguments"
}
```

</details>

- Property IDs are stripped, accept a properties/ prefix, and must then be numeric; this restriction is enforced by the handler, not the exposed schema.
- Reports fetch one page only; flattened output includes row counts, truncation warnings, metadata and quota. No automatic report pagination.
- Handler enforces limit between 1 and 10000; no bounds are declared in the exposed schema.

Source: [src/ga4_toolkit/mcp_server.py:89](https://github.com/onionst/ga4-toolkit/blob/1fbfe9e929dbdb055e556318b152be675e60071c/src/ga4_toolkit/mcp_server.py#L89-L105) · [src/ga4_toolkit/client.py:209](https://github.com/onionst/ga4-toolkit/blob/1fbfe9e929dbdb055e556318b152be675e60071c/src/ga4_toolkit/client.py#L209-L248) · [src/ga4_toolkit/presets.py:71](https://github.com/onionst/ga4-toolkit/blob/1fbfe9e929dbdb055e556318b152be675e60071c/src/ga4_toolkit/presets.py#L71-L87) · [src/ga4_toolkit/client.py:71](https://github.com/onionst/ga4-toolkit/blob/1fbfe9e929dbdb055e556318b152be675e60071c/src/ga4_toolkit/client.py#L71-L112) · [src/ga4_toolkit/client.py:307](https://github.com/onionst/ga4-toolkit/blob/1fbfe9e929dbdb055e556318b152be675e60071c/src/ga4_toolkit/client.py#L307-L336).

## ga4_run_report

POST historical runReport with supplied dimensions, metrics and date range, stringified limit and returnPropertyQuota=true. Truthy arbitrary dimension_filter/metric_filter objects are forwarded directly as dimensionFilter/metricFilter. Optional metric ordering is applied; return flattened rows.

<details>
<summary>Full registered description</summary>

```text
Run a custom historical GA4 report with requested dimensions and metrics.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `dimensions` | Yes | array of string | Not declared |
| `metrics` | Yes | array of string | Not declared |
| `property_id` | Yes | string | Not declared |
| `start_date` | No | string | "28daysAgo" |
| `end_date` | No | string | "yesterday" |
| `limit` | No | integer | 100 |
| `dimension_filter` | No | object or null | null |
| `metric_filter` | No | object or null | null |
| `order_by_metric` | No | string or null | null |
| `descending` | No | boolean | true |

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
      "title": "Dimensions"
    },
    "metrics": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "title": "Metrics"
    },
    "property_id": {
      "type": "string",
      "title": "Property Id"
    },
    "start_date": {
      "type": "string",
      "title": "Start Date",
      "default": "28daysAgo"
    },
    "end_date": {
      "type": "string",
      "title": "End Date",
      "default": "yesterday"
    },
    "limit": {
      "type": "integer",
      "title": "Limit",
      "default": 100
    },
    "dimension_filter": {
      "anyOf": [
        {
          "type": "object",
          "additionalProperties": true
        },
        {
          "type": "null"
        }
      ],
      "title": "Dimension Filter",
      "default": null
    },
    "metric_filter": {
      "anyOf": [
        {
          "type": "object",
          "additionalProperties": true
        },
        {
          "type": "null"
        }
      ],
      "title": "Metric Filter",
      "default": null
    },
    "order_by_metric": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Order By Metric",
      "default": null
    },
    "descending": {
      "type": "boolean",
      "title": "Descending",
      "default": true
    }
  },
  "required": [
    "dimensions",
    "metrics",
    "property_id"
  ],
  "title": "ga4_run_reportArguments"
}
```

</details>

- Property IDs are stripped, accept a properties/ prefix, and must then be numeric; this restriction is enforced by the handler, not the exposed schema.
- Reports fetch one page only; flattened output includes row counts, truncation warnings, metadata and quota. No automatic report pagination.
- Handler strips/drops empty names, requires 1–9 dimensions and 1–10 metrics and validates names against `[A-Za-z][A-Za-z0-9_]*`. It enforces limit 1–10000 and order_by_metric membership in requested metrics; these restrictions are absent from exposed schema.

Source: [src/ga4_toolkit/mcp_server.py:108](https://github.com/onionst/ga4-toolkit/blob/1fbfe9e929dbdb055e556318b152be675e60071c/src/ga4_toolkit/mcp_server.py#L108-L135) · [src/ga4_toolkit/client.py:209](https://github.com/onionst/ga4-toolkit/blob/1fbfe9e929dbdb055e556318b152be675e60071c/src/ga4_toolkit/client.py#L209-L248) · [src/ga4_toolkit/client.py:71](https://github.com/onionst/ga4-toolkit/blob/1fbfe9e929dbdb055e556318b152be675e60071c/src/ga4_toolkit/client.py#L71-L112) · [src/ga4_toolkit/client.py:307](https://github.com/onionst/ga4-toolkit/blob/1fbfe9e929dbdb055e556318b152be675e60071c/src/ga4_toolkit/client.py#L307-L336).

## ga4_realtime

POST runRealtimeReport with supplied dimensions and metrics, stringified limit, returnPropertyQuota=true and optional metric ordering; return flattened rows.

<details>
<summary>Full registered description</summary>

```text
Run a GA4 realtime report for activity from the last 30 minutes.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |
| `dimensions` | No | array of string | ["country"] |
| `metrics` | No | array of string | ["activeUsers", "eventCount"] |
| `limit` | No | integer | 100 |
| `order_by_metric` | No | string or null | null |
| `descending` | No | boolean | true |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "property_id": {
      "type": "string",
      "title": "Property Id"
    },
    "dimensions": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "title": "Dimensions",
      "default": [
        "country"
      ]
    },
    "metrics": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "title": "Metrics",
      "default": [
        "activeUsers",
        "eventCount"
      ]
    },
    "limit": {
      "type": "integer",
      "title": "Limit",
      "default": 100
    },
    "order_by_metric": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Order By Metric",
      "default": null
    },
    "descending": {
      "type": "boolean",
      "title": "Descending",
      "default": true
    }
  },
  "required": [
    "property_id"
  ],
  "title": "ga4_realtimeArguments"
}
```

</details>

- Property IDs are stripped, accept a properties/ prefix, and must then be numeric; this restriction is enforced by the handler, not the exposed schema.
- Reports fetch one page only; flattened output includes row counts, truncation warnings, metadata and quota. No automatic report pagination.
- Handler strips/drops empty names, requires 1–4 dimensions and 1–4 metrics and validates names against `[A-Za-z][A-Za-z0-9_]*`. It enforces limit 1–10000 and order_by_metric membership in requested metrics; these restrictions are absent from exposed schema.

Source: [src/ga4_toolkit/mcp_server.py:138](https://github.com/onionst/ga4-toolkit/blob/1fbfe9e929dbdb055e556318b152be675e60071c/src/ga4_toolkit/mcp_server.py#L138-L157) · [src/ga4_toolkit/client.py:250](https://github.com/onionst/ga4-toolkit/blob/1fbfe9e929dbdb055e556318b152be675e60071c/src/ga4_toolkit/client.py#L250-L279) · [src/ga4_toolkit/client.py:71](https://github.com/onionst/ga4-toolkit/blob/1fbfe9e929dbdb055e556318b152be675e60071c/src/ga4_toolkit/client.py#L71-L112) · [src/ga4_toolkit/client.py:307](https://github.com/onionst/ga4-toolkit/blob/1fbfe9e929dbdb055e556318b152be675e60071c/src/ga4_toolkit/client.py#L307-L336).

## ga4_metadata

GET property metadata. If search is truthy, case-insensitively filter dimensions and metrics by combined apiName, uiName, description and category text. Append propertyId and return metadata.

<details>
<summary>Full registered description</summary>

```text
List compatible GA4 dimensions and metrics, optionally filtered by text.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |
| `search` | No | string or null | null |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "property_id": {
      "type": "string",
      "title": "Property Id"
    },
    "search": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Search",
      "default": null
    }
  },
  "required": [
    "property_id"
  ],
  "title": "ga4_metadataArguments"
}
```

</details>

- Property IDs are stripped, accept a properties/ prefix, and must then be numeric; this restriction is enforced by the handler, not the exposed schema.
- Despite description saying compatible dimensions and metrics, this calls getMetadata only; no checkCompatibility request is made.

Source: [src/ga4_toolkit/mcp_server.py:160](https://github.com/onionst/ga4-toolkit/blob/1fbfe9e929dbdb055e556318b152be675e60071c/src/ga4_toolkit/mcp_server.py#L160-L165) · [src/ga4_toolkit/client.py:281](https://github.com/onionst/ga4-toolkit/blob/1fbfe9e929dbdb055e556318b152be675e60071c/src/ga4_toolkit/client.py#L281-L304) · [src/ga4_toolkit/client.py:71](https://github.com/onionst/ga4-toolkit/blob/1fbfe9e929dbdb055e556318b152be675e60071c/src/ga4_toolkit/client.py#L71-L112).

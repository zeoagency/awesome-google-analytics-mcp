# ESGEE-0562/google-analytics-mcp

[Catalog](../../README.md) · [All tool names](../tool-index.md) · [Upstream](https://github.com/ESGEE-0562/google-analytics-mcp) · [JSON](../../data/mcps/esgee-0562--google-analytics-mcp.json)

**7 tools:** 7 GA4, 0 other-service or server-support tools. Reviewed source: [`7e1e0873dde0`](https://github.com/ESGEE-0562/google-analytics-mcp/tree/7e1e0873dde071e23d416c09942573b74f199368).

Descriptions and parameter schemas come from the registered source definitions. Generated schemas are reconstructed from annotations or validators; live `tools/list` and authenticated API calls were not run. Loose objects remain loose.

<details>
<summary>Exposure and compatibility notes</summary>

- Source review only, no tools/list or live requests.
- All seven tools are advertised unconditionally by tools/list, which is permitted without authentication; tools/call requires an authenticated MCP token and Google credentials (server.py:638-711). No configurable tiers or optional tool modules are registered.
- The dispatcher has a defined callable src.ga_tools function for each advertised name. It does not validate arguments against inputSchema; missing required keys and protobuf construction errors become JSON-RPC -32603 errors.
- OAuth, health, status and SSE endpoints are HTTP routes, not additional MCP tools. src/provider.py is unused by the published server:app entrypoint and registers no tools; its mcp dependency is not listed in requirements.txt, but that unused module is not an entrypoint import blocker.
- Deployment requires Google OAuth client configuration and encryption key configuration; no definite published entrypoint import blocker was identified by source inspection.

</details>

## Tools

| Tool | Scope | Effect |
| --- | --- | --- |
| [`get_account_summaries`](#get_account_summaries) | GA4 | read |
| [`get_property_details`](#get_property_details) | GA4 | read |
| [`list_google_ads_links`](#list_google_ads_links) | GA4 | read |
| [`list_property_annotations`](#list_property_annotations) | GA4 | read |
| [`run_report`](#run_report) | GA4 | read |
| [`run_realtime_report`](#run_realtime_report) | GA4 | read |
| [`get_custom_dimensions_and_metrics`](#get_custom_dimensions_and_metrics) | GA4 | read |

## get_account_summaries

Retrieves and consumes the async account-summary pager, returning all account summaries as proto-field-name dictionaries.

<details>
<summary>Full registered description</summary>

```text
List all GA4 accounts and properties the user has access to. Call this first to discover property IDs.
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

Source: [server.py:71](https://github.com/ESGEE-0562/google-analytics-mcp/blob/7e1e0873dde071e23d416c09942573b74f199368/server.py#L71-L75) · [server.py:202](https://github.com/ESGEE-0562/google-analytics-mcp/blob/7e1e0873dde071e23d416c09942573b74f199368/server.py#L202-L203) · [src/ga_tools.py:55](https://github.com/ESGEE-0562/google-analytics-mcp/blob/7e1e0873dde071e23d416c09942573b74f199368/src/ga_tools.py#L55-L58).

## get_property_details

Normalizes the property resource name and retrieves a property, returning a proto-field-name dictionary.

<details>
<summary>Full registered description</summary>

```text
Returns full details for a specific GA4 property (time zone, currency, industry, etc.).
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | integer or string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "property_id": {
      "type": [
        "integer",
        "string"
      ],
      "description": "GA4 property ID — a number (123456789) or 'properties/123456789'"
    }
  },
  "required": [
    "property_id"
  ]
}
```

</details>

- Implementation normalizes integer/digit-string property IDs or accepts a string starting 'properties/' whose last segment is numeric; other strings raise ValueError. This restriction is not encoded in the exposed schema.

Source: [server.py:76](https://github.com/ESGEE-0562/google-analytics-mcp/blob/7e1e0873dde071e23d416c09942573b74f199368/server.py#L76-L84) · [server.py:204](https://github.com/ESGEE-0562/google-analytics-mcp/blob/7e1e0873dde071e23d416c09942573b74f199368/server.py#L204-L205) · [src/ga_tools.py:61](https://github.com/ESGEE-0562/google-analytics-mcp/blob/7e1e0873dde071e23d416c09942573b74f199368/src/ga_tools.py#L61-L66).

## list_google_ads_links

Normalizes the property resource name and consumes the Google Ads links pager, returning dictionaries.

<details>
<summary>Full registered description</summary>

```text
Lists Google Ads account links for a GA4 property.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | integer or string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "property_id": {
      "type": [
        "integer",
        "string"
      ],
      "description": "GA4 property ID — a number (123456789) or 'properties/123456789'"
    }
  },
  "required": [
    "property_id"
  ]
}
```

</details>

- Implementation normalizes integer/digit-string property IDs or accepts a string starting 'properties/' whose last segment is numeric; other strings raise ValueError. This restriction is not encoded in the exposed schema.

Source: [server.py:85](https://github.com/ESGEE-0562/google-analytics-mcp/blob/7e1e0873dde071e23d416c09942573b74f199368/server.py#L85-L93) · [server.py:206](https://github.com/ESGEE-0562/google-analytics-mcp/blob/7e1e0873dde071e23d416c09942573b74f199368/server.py#L206-L207) · [src/ga_tools.py:69](https://github.com/ESGEE-0562/google-analytics-mcp/blob/7e1e0873dde071e23d416c09942573b74f199368/src/ga_tools.py#L69-L74).

## list_property_annotations

Normalizes the property resource name and consumes the reporting-data annotations pager using the alpha Admin client.

<details>
<summary>Full registered description</summary>

```text
Returns date annotations for a GA4 property (release notes, campaign launches, traffic anomalies, etc.).
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | integer or string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "property_id": {
      "type": [
        "integer",
        "string"
      ],
      "description": "GA4 property ID — a number (123456789) or 'properties/123456789'"
    }
  },
  "required": [
    "property_id"
  ]
}
```

</details>

- Implementation normalizes integer/digit-string property IDs or accepts a string starting 'properties/' whose last segment is numeric; other strings raise ValueError. This restriction is not encoded in the exposed schema.

Source: [server.py:94](https://github.com/ESGEE-0562/google-analytics-mcp/blob/7e1e0873dde071e23d416c09942573b74f199368/server.py#L94-L102) · [server.py:208](https://github.com/ESGEE-0562/google-analytics-mcp/blob/7e1e0873dde071e23d416c09942573b74f199368/server.py#L208-L209) · [src/ga_tools.py:77](https://github.com/ESGEE-0562/google-analytics-mcp/blob/7e1e0873dde071e23d416c09942573b74f199368/src/ga_tools.py#L77-L82).

## run_report

Constructs a RunReportRequest from named dimensions and metrics and date-range dictionaries; converts supplied loose filter and ordering dictionaries to protobuf messages, applies pagination/currency/quota parameters, runs the report and serializes the response.

<details>
<summary>Full registered description</summary>

```text
Run a GA4 Data API report. Examples — top pages: dimensions=['pagePath'], metrics=['screenPageViews','sessions']. Traffic sources: dimensions=['sessionSource','sessionMedium'], metrics=['sessions','conversions']. Countries: dimensions=['country'], metrics=['sessions','newUsers']. Relative dates: '7daysAgo', '30daysAgo', 'yesterday', 'today'. Absolute dates: 'YYYY-MM-DD'.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | integer or string | Not declared |
| `date_ranges` | Yes | array of object | Not declared |
| `dimensions` | Yes | array of string | Not declared |
| `metrics` | Yes | array of string | Not declared |
| `dimension_filter` | No | object | Not declared |
| `metric_filter` | No | object | Not declared |
| `order_bys` | No | array of object | Not declared |
| `limit` | No | integer | Not declared |
| `offset` | No | integer | Not declared |
| `currency_code` | No | string | Not declared |
| `return_property_quota` | No | boolean | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "property_id": {
      "type": [
        "integer",
        "string"
      ],
      "description": "GA4 property ID — a number (123456789) or 'properties/123456789'"
    },
    "date_ranges": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "start_date": {
            "type": "string"
          },
          "end_date": {
            "type": "string"
          },
          "name": {
            "type": "string"
          }
        },
        "required": [
          "start_date",
          "end_date"
        ]
      },
      "description": "e.g. [{'start_date':'7daysAgo','end_date':'today'}]"
    },
    "dimensions": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "e.g. ['pagePath', 'country', 'deviceCategory', 'sessionSource']"
    },
    "metrics": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "e.g. ['sessions', 'screenPageViews', 'conversions', 'totalRevenue', 'newUsers']"
    },
    "dimension_filter": {
      "type": "object",
      "description": "FilterExpression for dimensions (see GA4 Data API docs)"
    },
    "metric_filter": {
      "type": "object",
      "description": "FilterExpression for metrics (see GA4 Data API docs)"
    },
    "order_bys": {
      "type": "array",
      "items": {
        "type": "object"
      },
      "description": "List of OrderBy objects"
    },
    "limit": {
      "type": "integer",
      "description": "Max rows (default: all)"
    },
    "offset": {
      "type": "integer",
      "description": "Row offset for pagination"
    },
    "currency_code": {
      "type": "string",
      "description": "ISO4217 currency code, e.g. 'EUR'"
    },
    "return_property_quota": {
      "type": "boolean"
    }
  },
  "required": [
    "property_id",
    "date_ranges",
    "dimensions",
    "metrics"
  ]
}
```

</details>

- Implementation normalizes integer/digit-string property IDs or accepts a string starting 'properties/' whose last segment is numeric; other strings raise ValueError. This restriction is not encoded in the exposed schema.
- Filter objects and ordering items intentionally have no exposed inner properties; the handler passes them to FilterExpression/OrderBy protobuf constructors. return_property_quota defaults to false in the dispatcher, but no schema default is declared.

Source: [server.py:103](https://github.com/ESGEE-0562/google-analytics-mcp/blob/7e1e0873dde071e23d416c09942573b74f199368/server.py#L103-L160) · [server.py:210](https://github.com/ESGEE-0562/google-analytics-mcp/blob/7e1e0873dde071e23d416c09942573b74f199368/server.py#L210-L224) · [src/ga_tools.py:87](https://github.com/ESGEE-0562/google-analytics-mcp/blob/7e1e0873dde071e23d416c09942573b74f199368/src/ga_tools.py#L87-L131).

## run_realtime_report

Constructs a RunRealtimeReportRequest from named dimensions and metrics; converts supplied loose filter and ordering dictionaries to protobuf messages, applies limit, offset and quota parameters, calls the realtime reporting method and serializes the response.

<details>
<summary>Full registered description</summary>

```text
Run a GA4 realtime report showing live active users. Use realtime dimensions/metrics.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | integer or string | Not declared |
| `dimensions` | Yes | array of string | Not declared |
| `metrics` | Yes | array of string | Not declared |
| `dimension_filter` | No | object | Not declared |
| `metric_filter` | No | object | Not declared |
| `order_bys` | No | array of object | Not declared |
| `limit` | No | integer | Not declared |
| `offset` | No | integer | Not declared |
| `return_property_quota` | No | boolean | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "property_id": {
      "type": [
        "integer",
        "string"
      ],
      "description": "GA4 property ID — a number (123456789) or 'properties/123456789'"
    },
    "dimensions": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Realtime dimensions, e.g. ['country', 'deviceCategory', 'unifiedScreenName']"
    },
    "metrics": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Realtime metrics, e.g. ['activeUsers']"
    },
    "dimension_filter": {
      "type": "object"
    },
    "metric_filter": {
      "type": "object"
    },
    "order_bys": {
      "type": "array",
      "items": {
        "type": "object"
      }
    },
    "limit": {
      "type": "integer"
    },
    "offset": {
      "type": "integer"
    },
    "return_property_quota": {
      "type": "boolean"
    }
  },
  "required": [
    "property_id",
    "dimensions",
    "metrics"
  ]
}
```

</details>

- Implementation normalizes integer/digit-string property IDs or accepts a string starting 'properties/' whose last segment is numeric; other strings raise ValueError. This restriction is not encoded in the exposed schema.
- Filter objects and ordering items intentionally have no exposed inner properties; the handler passes them to FilterExpression/OrderBy protobuf constructors. return_property_quota defaults to false in the dispatcher, but no schema default is declared.
- The advertised offset is assigned to RunRealtimeReportRequest.offset when supplied; the GA4 realtime request does not support offset, so this optional argument is a handler defect. No runtime execution was performed.

Source: [server.py:161](https://github.com/ESGEE-0562/google-analytics-mcp/blob/7e1e0873dde071e23d416c09942573b74f199368/server.py#L161-L187) · [server.py:225](https://github.com/ESGEE-0562/google-analytics-mcp/blob/7e1e0873dde071e23d416c09942573b74f199368/server.py#L225-L237) · [src/ga_tools.py:134](https://github.com/ESGEE-0562/google-analytics-mcp/blob/7e1e0873dde071e23d416c09942573b74f199368/src/ga_tools.py#L134-L168).

## get_custom_dimensions_and_metrics

Fetches property metadata and returns only dimensions and metrics whose custom_definition flag is true.

<details>
<summary>Full registered description</summary>

```text
Returns the property's custom dimensions and metrics. Use before run_report to find custom field names.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | integer or string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "property_id": {
      "type": [
        "integer",
        "string"
      ],
      "description": "GA4 property ID — a number (123456789) or 'properties/123456789'"
    }
  },
  "required": [
    "property_id"
  ]
}
```

</details>

- Implementation normalizes integer/digit-string property IDs or accepts a string starting 'properties/' whose last segment is numeric; other strings raise ValueError. This restriction is not encoded in the exposed schema.

Source: [server.py:188](https://github.com/ESGEE-0562/google-analytics-mcp/blob/7e1e0873dde071e23d416c09942573b74f199368/server.py#L188-L196) · [server.py:238](https://github.com/ESGEE-0562/google-analytics-mcp/blob/7e1e0873dde071e23d416c09942573b74f199368/server.py#L238-L239) · [src/ga_tools.py:171](https://github.com/ESGEE-0562/google-analytics-mcp/blob/7e1e0873dde071e23d416c09942573b74f199368/src/ga_tools.py#L171-L185).

# leonardosepulvedat/mcp-google-analytics

[Catalog](../../README.md) · [All tool names](../tool-index.md) · [Upstream](https://github.com/leonardosepulvedat/mcp-google-analytics) · [JSON](../../data/mcps/leonardosepulvedat--mcp-google-analytics.json)

**26 tools:** 26 GA4, 0 other-service or server-support tools. Reviewed source: [`97731c9bcf80`](https://github.com/leonardosepulvedat/mcp-google-analytics/tree/97731c9bcf801297b0c8f0cd34cdde903730f2a2).

Descriptions and parameter schemas come from the registered source definitions. Generated schemas are reconstructed from annotations or validators; live `tools/list` and authenticated API calls were not run. Loose objects remain loose.

<details>
<summary>Exposure and compatibility notes</summary>

- Source review only; no tools/list or live requests. Source snapshot has no .git; supplied revision is authoritative.
- All 26 tools register unconditionally; absent or invalid credentials cause handlers to fail, not conditional tool removal. Data/Admin tools need GA_SERVICE_ACCOUNT_JSON; Measurement Protocol tools need GA_MEASUREMENT_ID and GA_API_SECRET.
- Build entrypoint is build/index.js; package prepare runs TypeScript build. Node >=20 is declared. No definite unusable entrypoint established by inspection.
- Zod objects strip unknown properties (represented by additionalProperties:false); records of z.any preserve arbitrary JSON values. No runtime parsing of types.ts request validators occurs: only EcommerceItemSchema is imported as an exposed shared validator.
- Four registerPrompt calls and unregistered sendBatchEvents helper are not tools.
- Native Measurement Protocol restrictions are separate from exposed schema: body <130 kB, up to 25 events, 25 parameters/event, event and parameter names <=40 characters, 25 user properties with names <=24 and values <=36 characters. HTTP 2xx acknowledges receipt, not valid ingestion; session_id and engagement_time_msec affect Realtime/user engagement accuracy. Helpers add neither parameter. validation_behavior is not exposed, so debug validation cannot request ENFORCE_RECOMMENDATIONS through these tools. [Official Measurement Protocol reference](https://developers.google.com/analytics/devguides/collection/protocol/ga4/reference).

</details>

## Tools

| Tool | Scope | Effect |
| --- | --- | --- |
| [`ga_run_report`](#ga_run_report) | GA4 | read |
| [`ga_run_realtime_report`](#ga_run_realtime_report) | GA4 | read |
| [`ga_get_metadata`](#ga_get_metadata) | GA4 | read |
| [`ga_list_accounts`](#ga_list_accounts) | GA4 | read |
| [`ga_list_properties`](#ga_list_properties) | GA4 | read |
| [`ga_get_property`](#ga_get_property) | GA4 | read |
| [`ga_list_data_streams`](#ga_list_data_streams) | GA4 | read |
| [`ga_run_pivot_report`](#ga_run_pivot_report) | GA4 | read |
| [`ga_run_funnel_report`](#ga_run_funnel_report) | GA4 | read |
| [`ga_batch_run_reports`](#ga_batch_run_reports) | GA4 | read |
| [`ga_get_account_summaries`](#ga_get_account_summaries) | GA4 | read |
| [`ga_list_custom_dimensions`](#ga_list_custom_dimensions) | GA4 | read |
| [`ga_list_custom_metrics`](#ga_list_custom_metrics) | GA4 | read |
| [`ga_list_key_events`](#ga_list_key_events) | GA4 | read |
| [`ga_list_google_ads_links`](#ga_list_google_ads_links) | GA4 | read |
| [`ga_check_compatibility`](#ga_check_compatibility) | GA4 | read |
| [`ga_send_event`](#ga_send_event) | GA4 | write |
| [`ga_validate_event`](#ga_validate_event) | GA4 | read |
| [`ga_send_pageview`](#ga_send_pageview) | GA4 | write |
| [`ga_send_purchase`](#ga_send_purchase) | GA4 | write |
| [`ga_send_login`](#ga_send_login) | GA4 | write |
| [`ga_send_signup`](#ga_send_signup) | GA4 | write |
| [`ga_send_add_to_cart`](#ga_send_add_to_cart) | GA4 | write |
| [`ga_send_begin_checkout`](#ga_send_begin_checkout) | GA4 | write |
| [`ga_send_view_item`](#ga_send_view_item) | GA4 | write |
| [`ga_send_refund`](#ga_send_refund) | GA4 | write |

## ga_run_report

POSTs the report arguments to Data API v1beta properties:runReport and returns response.data.

<details>
<summary>Full registered description</summary>

```text
Run a custom Google Analytics report with dimensions and metrics.

⚠️ TOKEN OPTIMIZATION: Use 'limit' to control result size (default: 10).
This tool can consume significant tokens with large datasets.

Common dimensions: date, city, country, deviceCategory, browser, pagePath, eventName
Common metrics: activeUsers, sessions, screenPageViews, conversions, totalRevenue
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `dateRanges` | Yes | array of object | Not declared |
| `dimensions` | No | array of object | Not declared |
| `metrics` | Yes | array of object | Not declared |
| `limit` | No | integer | Not declared |
| `offset` | No | integer | Not declared |
| `orderBys` | No | array of object | Not declared |
| `dimensionFilter` | No | object | Not declared |
| `metricFilter` | No | object | Not declared |
| `propertyId` | No | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "dateRanges": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "startDate": {
            "type": "string",
            "description": "Start date (YYYY-MM-DD or \"yesterday\", \"today\", \"7daysAgo\")"
          },
          "endDate": {
            "type": "string",
            "description": "End date (YYYY-MM-DD or \"yesterday\", \"today\", \"7daysAgo\")"
          },
          "name": {
            "type": "string",
            "description": "Optional name for the date range"
          }
        },
        "required": [
          "startDate",
          "endDate"
        ],
        "additionalProperties": false
      },
      "description": "Date ranges for the report"
    },
    "dimensions": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          }
        },
        "required": [
          "name"
        ],
        "additionalProperties": false
      },
      "description": "Dimensions to group by (e.g., [{name: \"date\"}])"
    },
    "metrics": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          }
        },
        "required": [
          "name"
        ],
        "additionalProperties": false
      },
      "description": "Metrics to measure (e.g., [{name: \"activeUsers\"}])"
    },
    "limit": {
      "type": "integer",
      "exclusiveMinimum": 0,
      "description": "Maximum number of rows to return (default: 10)"
    },
    "offset": {
      "type": "integer",
      "minimum": 0,
      "description": "Number of rows to skip (for pagination)"
    },
    "orderBys": {
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": {}
      },
      "description": "Sorting specification"
    },
    "dimensionFilter": {
      "type": "object",
      "additionalProperties": {},
      "description": "Dimension filter expression"
    },
    "metricFilter": {
      "type": "object",
      "additionalProperties": {},
      "description": "Metric filter expression"
    },
    "propertyId": {
      "type": "string",
      "description": "GA4 property ID to query (overrides the default GA_PROPERTY_ID). Accepts \"123456789\" or \"properties/123456789\". Use ga_get_account_summaries to discover IDs."
    }
  },
  "required": [
    "dateRanges",
    "metrics"
  ],
  "additionalProperties": false
}
```

</details>

- propertyId overrides GA_PROPERTY_ID; a missing effective ID fails in the handler. A leading properties/ prefix is removed.
- The handler supplies limit=10 when omitted; this is an implementation default, not a Zod schema default.

Source: [src/index.ts:119](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/index.ts#L119-L144) · [src/ga-data-client.ts:83](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/ga-data-client.ts#L83-L94) · [src/index.ts:76](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/index.ts#L76-L95).

## ga_run_realtime_report

POSTs the report arguments to Data API v1beta properties:runRealtimeReport and returns response.data.

<details>
<summary>Full registered description</summary>

```text
Get real-time Google Analytics data (last 30 minutes).

⚠️ TOKEN OPTIMIZATION: Use 'limit' to control result size (default: 10).

Common dimensions: city, country, deviceCategory, unifiedScreenName
Common metrics: activeUsers, screenPageViews, conversions
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `dimensions` | No | array of object | Not declared |
| `metrics` | Yes | array of object | Not declared |
| `limit` | No | integer | Not declared |
| `propertyId` | No | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "dimensions": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          }
        },
        "required": [
          "name"
        ],
        "additionalProperties": false
      },
      "description": "Dimensions to group by"
    },
    "metrics": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          }
        },
        "required": [
          "name"
        ],
        "additionalProperties": false
      },
      "description": "Metrics to measure"
    },
    "limit": {
      "type": "integer",
      "exclusiveMinimum": 0,
      "description": "Maximum number of rows (default: 10)"
    },
    "propertyId": {
      "type": "string",
      "description": "GA4 property ID to query (overrides the default GA_PROPERTY_ID). Accepts \"123456789\" or \"properties/123456789\". Use ga_get_account_summaries to discover IDs."
    }
  },
  "required": [
    "metrics"
  ],
  "additionalProperties": false
}
```

</details>

- propertyId overrides GA_PROPERTY_ID; a missing effective ID fails in the handler. A leading properties/ prefix is removed.
- The handler supplies limit=10 when omitted; this is an implementation default, not a Zod schema default.

Source: [src/index.ts:146](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/index.ts#L146-L165) · [src/ga-data-client.ts:95](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/ga-data-client.ts#L95-L116) · [src/index.ts:76](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/index.ts#L76-L95).

## ga_get_metadata

GETs Data API v1beta properties/{id}/metadata and returns response.data.

<details>
<summary>Full registered description</summary>

```text
Get available dimensions and metrics metadata for your GA4 property.

⚠️ TOKEN OPTIMIZATION: This returns ALL available dimensions and metrics.
Response can be large (~500+ items). Use sparingly and cache results when possible.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `propertyId` | No | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "propertyId": {
      "type": "string",
      "description": "GA4 property ID to query (overrides the default GA_PROPERTY_ID). Accepts \"123456789\" or \"properties/123456789\". Use ga_get_account_summaries to discover IDs."
    }
  },
  "required": [],
  "additionalProperties": false
}
```

</details>

- propertyId overrides GA_PROPERTY_ID; a missing effective ID fails in the handler. A leading properties/ prefix is removed.

Source: [src/index.ts:167](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/index.ts#L167-L178) · [src/ga-data-client.ts:189](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/ga-data-client.ts#L189-L199) · [src/index.ts:76](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/index.ts#L76-L95).

## ga_list_accounts

GETs Admin API v1beta accounts and returns response.data.

<details>
<summary>Full registered description</summary>

```text
List all Google Analytics accounts accessible to the service account.

Use this to find account IDs for listing properties.
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

- No pageToken iteration: only the first API response page is returned (or first page per account for unfiltered properties).

Source: [src/index.ts:180](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/index.ts#L180-L190) · [src/ga-data-client.ts:200](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/ga-data-client.ts#L200-L212).

## ga_list_properties

GETs Admin API v1beta properties with parent:accounts/{accountId}; without accountId, GETs accounts then sequentially lists and aggregates properties for each returned account.

<details>
<summary>Full registered description</summary>

```text
List Google Analytics properties.

Optionally filter by account ID. Without an account ID, properties from all
accessible accounts are aggregated.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `accountId` | No | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "accountId": {
      "type": "string",
      "description": "Optional account ID to filter properties (e.g., \"123456789\")"
    }
  },
  "required": [],
  "additionalProperties": false
}
```

</details>

- No pageToken iteration: only the first API response page is returned (or first page per account for unfiltered properties).

Source: [src/index.ts:192](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/index.ts#L192-L205) · [src/ga-data-client.ts:213](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/ga-data-client.ts#L213-L236).

## ga_get_property

GETs Admin API v1beta properties/{id} and returns response.data.

<details>
<summary>Full registered description</summary>

```text
Get details about a GA4 property (the configured one, or any accessible property via propertyId).
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `propertyId` | No | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "propertyId": {
      "type": "string",
      "description": "GA4 property ID to query (overrides the default GA_PROPERTY_ID). Accepts \"123456789\" or \"properties/123456789\". Use ga_get_account_summaries to discover IDs."
    }
  },
  "required": [],
  "additionalProperties": false
}
```

</details>

- propertyId overrides GA_PROPERTY_ID; a missing effective ID fails in the handler. A leading properties/ prefix is removed.

Source: [src/index.ts:207](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/index.ts#L207-L215) · [src/ga-data-client.ts:237](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/ga-data-client.ts#L237-L247) · [src/index.ts:76](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/index.ts#L76-L95).

## ga_list_data_streams

GETs Admin API v1beta properties/{id}/dataStreams and returns response.data.

<details>
<summary>Full registered description</summary>

```text
List data streams for the configured GA4 property.

Use this to find measurement IDs for Measurement Protocol.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `propertyId` | No | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "propertyId": {
      "type": "string",
      "description": "GA4 property ID to query (overrides the default GA_PROPERTY_ID). Accepts \"123456789\" or \"properties/123456789\". Use ga_get_account_summaries to discover IDs."
    }
  },
  "required": [],
  "additionalProperties": false
}
```

</details>

- propertyId overrides GA_PROPERTY_ID; a missing effective ID fails in the handler. A leading properties/ prefix is removed.
- No pageToken iteration: only the first API response page is returned (or first page per account for unfiltered properties).

Source: [src/index.ts:217](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/index.ts#L217-L227) · [src/ga-data-client.ts:248](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/ga-data-client.ts#L248-L259) · [src/index.ts:76](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/index.ts#L76-L95).

## ga_run_pivot_report

POSTs exposed arguments to Data API v1beta properties:runPivotReport unchanged; no pivot limit default is supplied.

<details>
<summary>Full registered description</summary>

```text
Run a pivot table report with row and column dimensions.

⚠️ TOKEN OPTIMIZATION: Pivot reports can be VERY large.
Limit dimensions and use small date ranges. Recommended for analysis, not raw data extraction.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `dateRanges` | Yes | array of object | Not declared |
| `dimensions` | No | array of object | Not declared |
| `metrics` | Yes | array of object | Not declared |
| `pivots` | Yes | array of object | Not declared |
| `propertyId` | No | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "dateRanges": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "startDate": {
            "type": "string",
            "description": "Start date (YYYY-MM-DD or \"yesterday\", \"today\", \"7daysAgo\")"
          },
          "endDate": {
            "type": "string",
            "description": "End date (YYYY-MM-DD or \"yesterday\", \"today\", \"7daysAgo\")"
          },
          "name": {
            "type": "string",
            "description": "Optional name for the date range"
          }
        },
        "required": [
          "startDate",
          "endDate"
        ],
        "additionalProperties": false
      }
    },
    "dimensions": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          }
        },
        "required": [
          "name"
        ],
        "additionalProperties": false
      }
    },
    "metrics": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          }
        },
        "required": [
          "name"
        ],
        "additionalProperties": false
      }
    },
    "pivots": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "fieldNames": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "limit": {
            "type": "integer",
            "exclusiveMinimum": 0
          }
        },
        "required": [
          "fieldNames"
        ],
        "additionalProperties": false
      },
      "description": "Pivot specifications with fieldNames"
    },
    "propertyId": {
      "type": "string",
      "description": "GA4 property ID to query (overrides the default GA_PROPERTY_ID). Accepts \"123456789\" or \"properties/123456789\". Use ga_get_account_summaries to discover IDs."
    }
  },
  "required": [
    "dateRanges",
    "metrics",
    "pivots"
  ],
  "additionalProperties": false
}
```

</details>

- propertyId overrides GA_PROPERTY_ID; a missing effective ID fails in the handler. A leading properties/ prefix is removed.

Source: [src/index.ts:229](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/index.ts#L229-L254) · [src/ga-data-client.ts:117](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/ga-data-client.ts#L117-L134) · [src/index.ts:76](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/index.ts#L76-L95).

## ga_run_funnel_report

Builds Data API v1alpha funnel.steps with supplied filterExpression or funnelEventFilter eventName (fallback step name); wraps funnelBreakdown.name as breakdownDimension and POSTs properties:runFunnelReport.

<details>
<summary>Full registered description</summary>

```text
Run a funnel analysis report to track user progression through steps (Data API v1alpha).

Each step matches an event: set 'eventName' per step (defaults to the step name).
For advanced matching, pass a full 'filterExpression' instead.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `dateRanges` | Yes | array of object | Not declared |
| `funnelSteps` | Yes | array of object | Not declared |
| `funnelBreakdown` | No | object | Not declared |
| `funnelVisualizationType` | No | string | Not declared |
| `propertyId` | No | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "dateRanges": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "startDate": {
            "type": "string",
            "description": "Start date (YYYY-MM-DD or \"yesterday\", \"today\", \"7daysAgo\")"
          },
          "endDate": {
            "type": "string",
            "description": "End date (YYYY-MM-DD or \"yesterday\", \"today\", \"7daysAgo\")"
          },
          "name": {
            "type": "string",
            "description": "Optional name for the date range"
          }
        },
        "required": [
          "startDate",
          "endDate"
        ],
        "additionalProperties": false
      }
    },
    "funnelSteps": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "Display name for the step"
          },
          "eventName": {
            "type": "string",
            "description": "Event that defines the step (defaults to name)"
          },
          "isDirectlyFollowedBy": {
            "type": "boolean"
          },
          "withinDurationFromPriorStep": {
            "type": "string",
            "description": "e.g., \"3600s\""
          },
          "filterExpression": {
            "type": "object",
            "additionalProperties": {},
            "description": "Advanced FunnelFilterExpression (overrides eventName)"
          }
        },
        "required": [
          "name"
        ],
        "additionalProperties": false
      },
      "description": "Steps in the funnel"
    },
    "funnelBreakdown": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        }
      },
      "required": [
        "name"
      ],
      "additionalProperties": false,
      "description": "Optional dimension to break down funnel"
    },
    "funnelVisualizationType": {
      "type": "string",
      "enum": [
        "STANDARD_FUNNEL",
        "TRENDED_FUNNEL"
      ]
    },
    "propertyId": {
      "type": "string",
      "description": "GA4 property ID to query (overrides the default GA_PROPERTY_ID). Accepts \"123456789\" or \"properties/123456789\". Use ga_get_account_summaries to discover IDs."
    }
  },
  "required": [
    "dateRanges",
    "funnelSteps"
  ],
  "additionalProperties": false
}
```

</details>

- propertyId overrides GA_PROPERTY_ID; a missing effective ID fails in the handler. A leading properties/ prefix is removed.

Source: [src/index.ts:256](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/index.ts#L256-L284) · [src/ga-data-client.ts:135](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/ga-data-client.ts#L135-L174) · [src/index.ts:76](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/index.ts#L76-L95).

## ga_batch_run_reports

POSTs requests to Data API v1beta properties:batchRunReports, adding limit=10 to each request when absent. Arbitrary request keys are forwarded.

<details>
<summary>Full registered description</summary>

```text
Run multiple reports in a single request.

⚠️ TOKEN OPTIMIZATION: Can return LARGE amounts of data.
Limit to 2-5 reports per batch. Each report should have small limits.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `requests` | Yes | array of object | Not declared |
| `propertyId` | No | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "requests": {
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": {}
      },
      "description": "Array of report requests (same format as ga_run_report)"
    },
    "propertyId": {
      "type": "string",
      "description": "GA4 property ID to query (overrides the default GA_PROPERTY_ID). Accepts \"123456789\" or \"properties/123456789\". Use ga_get_account_summaries to discover IDs."
    }
  },
  "required": [
    "requests"
  ],
  "additionalProperties": false
}
```

</details>

- propertyId overrides GA_PROPERTY_ID; a missing effective ID fails in the handler. A leading properties/ prefix is removed.
- The handler supplies limit=10 when omitted; this is an implementation default, not a Zod schema default.
- Native API allows at most 5 requests per batch, for the same property; registration does not enforce this. [Official batchRunReports reference](https://developers.google.com/analytics/devguides/reporting/data/v1/rest/v1beta/properties/batchRunReports).

Source: [src/index.ts:286](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/index.ts#L286-L301) · [src/ga-data-client.ts:175](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/ga-data-client.ts#L175-L188) · [src/index.ts:76](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/index.ts#L76-L95).

## ga_get_account_summaries

GETs Admin API v1beta accountSummaries and returns response.data.

<details>
<summary>Full registered description</summary>

```text
Get a compact overview of all accessible GA accounts and their properties in a single call.

The fastest way to discover account IDs, property IDs, and property names.
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

- No pageToken iteration: only the first API response page is returned (or first page per account for unfiltered properties).

Source: [src/index.ts:303](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/index.ts#L303-L313) · [src/ga-data-client.ts:260](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/ga-data-client.ts#L260-L268).

## ga_list_custom_dimensions

GETs Admin API v1beta properties/{id}/customDimensions and returns response.data.

<details>
<summary>Full registered description</summary>

```text
List all custom dimensions defined for the configured GA4 property.

Use this to discover custom dimension API names (e.g., "customEvent:plan_type") for reports.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `propertyId` | No | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "propertyId": {
      "type": "string",
      "description": "GA4 property ID to query (overrides the default GA_PROPERTY_ID). Accepts \"123456789\" or \"properties/123456789\". Use ga_get_account_summaries to discover IDs."
    }
  },
  "required": [],
  "additionalProperties": false
}
```

</details>

- propertyId overrides GA_PROPERTY_ID; a missing effective ID fails in the handler. A leading properties/ prefix is removed.
- No pageToken iteration: only the first API response page is returned (or first page per account for unfiltered properties).

Source: [src/index.ts:315](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/index.ts#L315-L325) · [src/ga-data-client.ts:269](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/ga-data-client.ts#L269-L279) · [src/index.ts:76](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/index.ts#L76-L95).

## ga_list_custom_metrics

GETs Admin API v1beta properties/{id}/customMetrics and returns response.data.

<details>
<summary>Full registered description</summary>

```text
List all custom metrics defined for the configured GA4 property.

Use this to discover custom metric API names for reports.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `propertyId` | No | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "propertyId": {
      "type": "string",
      "description": "GA4 property ID to query (overrides the default GA_PROPERTY_ID). Accepts \"123456789\" or \"properties/123456789\". Use ga_get_account_summaries to discover IDs."
    }
  },
  "required": [],
  "additionalProperties": false
}
```

</details>

- propertyId overrides GA_PROPERTY_ID; a missing effective ID fails in the handler. A leading properties/ prefix is removed.
- No pageToken iteration: only the first API response page is returned (or first page per account for unfiltered properties).

Source: [src/index.ts:327](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/index.ts#L327-L337) · [src/ga-data-client.ts:280](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/ga-data-client.ts#L280-L290) · [src/index.ts:76](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/index.ts#L76-L95).

## ga_list_key_events

GETs Admin API v1beta properties/{id}/keyEvents and returns response.data.

<details>
<summary>Full registered description</summary>

```text
List the key events (conversions) configured for the GA4 property.

Useful to know which event names count as conversions before building reports or sending events.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `propertyId` | No | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "propertyId": {
      "type": "string",
      "description": "GA4 property ID to query (overrides the default GA_PROPERTY_ID). Accepts \"123456789\" or \"properties/123456789\". Use ga_get_account_summaries to discover IDs."
    }
  },
  "required": [],
  "additionalProperties": false
}
```

</details>

- propertyId overrides GA_PROPERTY_ID; a missing effective ID fails in the handler. A leading properties/ prefix is removed.
- No pageToken iteration: only the first API response page is returned (or first page per account for unfiltered properties).

Source: [src/index.ts:339](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/index.ts#L339-L349) · [src/ga-data-client.ts:291](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/ga-data-client.ts#L291-L301) · [src/index.ts:76](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/index.ts#L76-L95).

## ga_list_google_ads_links

GETs Admin API v1beta properties/{id}/googleAdsLinks and returns response.data.

<details>
<summary>Full registered description</summary>

```text
List Google Ads accounts linked to a GA4 property.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `propertyId` | No | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "propertyId": {
      "type": "string",
      "description": "GA4 property ID to query (overrides the default GA_PROPERTY_ID). Accepts \"123456789\" or \"properties/123456789\". Use ga_get_account_summaries to discover IDs."
    }
  },
  "required": [],
  "additionalProperties": false
}
```

</details>

- propertyId overrides GA_PROPERTY_ID; a missing effective ID fails in the handler. A leading properties/ prefix is removed.
- No pageToken iteration: only the first API response page is returned (or first page per account for unfiltered properties).

Source: [src/index.ts:351](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/index.ts#L351-L359) · [src/ga-data-client.ts:302](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/ga-data-client.ts#L302-L316) · [src/index.ts:76](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/index.ts#L76-L95).

## ga_check_compatibility

POSTs exposed arguments to Data API v1beta properties:checkCompatibility and returns response.data.

<details>
<summary>Full registered description</summary>

```text
Check whether a combination of dimensions and metrics is valid for this property BEFORE running a report.

Avoids wasted report requests and token-heavy error loops. Also lists which other fields remain compatible with the given combination.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `dimensions` | No | array of object | Not declared |
| `metrics` | No | array of object | Not declared |
| `compatibilityFilter` | No | string | Not declared |
| `propertyId` | No | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "dimensions": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          }
        },
        "required": [
          "name"
        ],
        "additionalProperties": false
      },
      "description": "Dimensions to check (e.g., [{name: \"city\"}])"
    },
    "metrics": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          }
        },
        "required": [
          "name"
        ],
        "additionalProperties": false
      },
      "description": "Metrics to check (e.g., [{name: \"activeUsers\"}])"
    },
    "compatibilityFilter": {
      "type": "string",
      "enum": [
        "COMPATIBLE",
        "INCOMPATIBLE"
      ],
      "description": "Only return fields with this compatibility (recommended: COMPATIBLE)"
    },
    "propertyId": {
      "type": "string",
      "description": "GA4 property ID to query (overrides the default GA_PROPERTY_ID). Accepts \"123456789\" or \"properties/123456789\". Use ga_get_account_summaries to discover IDs."
    }
  },
  "required": [],
  "additionalProperties": false
}
```

</details>

- propertyId overrides GA_PROPERTY_ID; a missing effective ID fails in the handler. A leading properties/ prefix is removed.

Source: [src/index.ts:361](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/index.ts#L361-L380) · [src/ga-data-client.ts:317](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/ga-data-client.ts#L317-L335) · [src/index.ts:76](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/index.ts#L76-L95).

## ga_send_event

POSTs the provided event body unchanged to <https://www.google-analytics.com/mp/collect> with configured measurement_id and api_secret query parameters. Returns success:true and HTTP status; does not validate ingestion.

<details>
<summary>Full registered description</summary>

```text
Send a custom event to Google Analytics via Measurement Protocol.

Use this for tracking custom user actions, conversions, or any GA4 event.
Events are processed asynchronously and appear in reports within minutes.

Common events: click, form_submit, video_play, file_download, custom_conversion
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `client_id` | No | string | Not declared |
| `user_id` | No | string | Not declared |
| `events` | Yes | array of object | Not declared |
| `user_properties` | No | object | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "client_id": {
      "type": "string",
      "description": "Client ID (UUID format recommended). Auto-generated if not provided."
    },
    "user_id": {
      "type": "string",
      "description": "Optional User ID for cross-device tracking"
    },
    "events": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "Event name (e.g., \"purchase\", \"sign_up\")"
          },
          "params": {
            "type": "object",
            "additionalProperties": {},
            "description": "Event parameters (key-value pairs)"
          }
        },
        "required": [
          "name"
        ],
        "additionalProperties": false
      },
      "description": "Events to send (can send multiple in one request)"
    },
    "user_properties": {
      "type": "object",
      "additionalProperties": {
        "type": "object",
        "properties": {
          "value": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "number"
              }
            ]
          }
        },
        "required": [
          "value"
        ],
        "additionalProperties": false
      },
      "description": "User properties (e.g., {subscription_tier: {value: \"premium\"}})"
    }
  },
  "required": [
    "events"
  ],
  "additionalProperties": false
}
```

</details>

- client_id is optional in the exposed schema, but this direct handler does not generate one. ga_send_event description claims auto-generation, which is implemented only by convenience event helpers. Native Measurement Protocol requires client_id for web streams.
- Configured GA_MEASUREMENT_ID/GA_API_SECRET select the web stream; neither can be overridden per call. Native API field/event limits and naming restrictions are not enforced locally; arrays have no size bounds, currency has no ISO validation, and item objects allow neither required identifier constraint nor custom item fields.

Source: [src/index.ts:391](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/index.ts#L391-L409) · [src/measurement-protocol-client.ts:27](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/measurement-protocol-client.ts#L27-L41) · [src/index.ts:76](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/index.ts#L76-L95) · [src/index.ts:386](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/index.ts#L386-L389).

## ga_validate_event

POSTs the provided event body unchanged to <https://www.google-analytics.com/debug/mp/collect>, via sendEvent(debug=true), and returns validation response data. Does not record events.

<details>
<summary>Full registered description</summary>

```text
Validate an event before sending it to Google Analytics.

Uses GA4's debug endpoint to check for errors without recording the event.
Returns validation messages and errors if any.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `client_id` | No | string | Not declared |
| `user_id` | No | string | Not declared |
| `events` | Yes | array of object | Not declared |
| `user_properties` | No | object | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "client_id": {
      "type": "string"
    },
    "user_id": {
      "type": "string"
    },
    "events": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "Event name (e.g., \"purchase\", \"sign_up\")"
          },
          "params": {
            "type": "object",
            "additionalProperties": {},
            "description": "Event parameters (key-value pairs)"
          }
        },
        "required": [
          "name"
        ],
        "additionalProperties": false
      }
    },
    "user_properties": {
      "type": "object",
      "additionalProperties": {
        "type": "object",
        "properties": {
          "value": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "number"
              }
            ]
          }
        },
        "required": [
          "value"
        ],
        "additionalProperties": false
      },
      "description": "User properties (e.g., {subscription_tier: {value: \"premium\"}})"
    }
  },
  "required": [
    "events"
  ],
  "additionalProperties": false
}
```

</details>

- client_id is optional in the exposed schema, but this direct handler does not generate one. ga_send_event description claims auto-generation, which is implemented only by convenience event helpers. Native Measurement Protocol requires client_id for web streams.
- Configured GA_MEASUREMENT_ID/GA_API_SECRET select the web stream; neither can be overridden per call. Native API field/event limits and naming restrictions are not enforced locally; arrays have no size bounds, currency has no ISO validation, and item objects allow neither required identifier constraint nor custom item fields.

Source: [src/index.ts:411](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/index.ts#L411-L427) · [src/measurement-protocol-client.ts:56](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/measurement-protocol-client.ts#L56-L60) · [src/index.ts:76](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/index.ts#L76-L95) · [src/index.ts:386](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/index.ts#L386-L389).

## ga_send_pageview

Builds one page_view event from the exposed arguments and posts it to Measurement Protocol /mp/collect. Maps snake_case inputs to helper parameters, generates client_id as timestamp.random when missing or empty, includes user_id/user_properties, and returns success:true plus HTTP status.

<details>
<summary>Full registered description</summary>

```text
Send a page view event to Google Analytics.

Standard event for tracking page/screen views. Automatically uses 'page_view' event name.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `client_id` | No | string | Not declared |
| `user_id` | No | string | Not declared |
| `page_location` | Yes | string | Not declared |
| `page_title` | No | string | Not declared |
| `page_referrer` | No | string | Not declared |
| `user_properties` | No | object | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "client_id": {
      "type": "string",
      "description": "Client ID (auto-generated if not provided)"
    },
    "user_id": {
      "type": "string",
      "description": "Optional User ID"
    },
    "page_location": {
      "type": "string",
      "description": "Full URL of the page"
    },
    "page_title": {
      "type": "string",
      "description": "Page title"
    },
    "page_referrer": {
      "type": "string",
      "description": "Referrer URL"
    },
    "user_properties": {
      "type": "object",
      "additionalProperties": {
        "type": "object",
        "properties": {
          "value": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "number"
              }
            ]
          }
        },
        "required": [
          "value"
        ],
        "additionalProperties": false
      },
      "description": "User properties (e.g., {subscription_tier: {value: \"premium\"}})"
    }
  },
  "required": [
    "page_location"
  ],
  "additionalProperties": false
}
```

</details>

- Configured GA_MEASUREMENT_ID/GA_API_SECRET select the web stream; neither can be overridden per call. Native API field/event limits and naming restrictions are not enforced locally; arrays have no size bounds, currency has no ISO validation, and item objects allow neither required identifier constraint nor custom item fields.
- Optional string event parameters are only included when truthy; numeric tax/shipping fields (purchase) are included when defined.

Source: [src/index.ts:429](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/index.ts#L429-L456) · [src/measurement-protocol-client.ts:61](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/measurement-protocol-client.ts#L61-L89) · [src/index.ts:76](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/index.ts#L76-L95).

## ga_send_purchase

Builds one purchase event from the exposed arguments and posts it to Measurement Protocol /mp/collect. Maps snake_case inputs to helper parameters, generates client_id as timestamp.random when missing or empty, includes user_id/user_properties, and returns success:true plus HTTP status.

<details>
<summary>Full registered description</summary>

```text
Send an ecommerce purchase event to Google Analytics.

Standard event for tracking completed purchases with transaction details and items.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `client_id` | No | string | Not declared |
| `user_id` | No | string | Not declared |
| `transaction_id` | Yes | string | Not declared |
| `value` | Yes | number | Not declared |
| `currency` | Yes | string | Not declared |
| `tax` | No | number | Not declared |
| `shipping` | No | number | Not declared |
| `coupon` | No | string | Not declared |
| `affiliation` | No | string | Not declared |
| `items` | Yes | array of object | Not declared |
| `user_properties` | No | object | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "client_id": {
      "type": "string"
    },
    "user_id": {
      "type": "string"
    },
    "transaction_id": {
      "type": "string",
      "description": "Unique transaction ID"
    },
    "value": {
      "type": "number",
      "description": "Total purchase value"
    },
    "currency": {
      "type": "string",
      "description": "Currency code (e.g., USD, EUR)"
    },
    "tax": {
      "type": "number",
      "description": "Tax amount"
    },
    "shipping": {
      "type": "number",
      "description": "Shipping cost"
    },
    "coupon": {
      "type": "string",
      "description": "Coupon code used"
    },
    "affiliation": {
      "type": "string",
      "description": "Store or affiliation"
    },
    "items": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "item_id": {
            "type": "string"
          },
          "item_name": {
            "type": "string"
          },
          "affiliation": {
            "type": "string"
          },
          "coupon": {
            "type": "string"
          },
          "currency": {
            "type": "string"
          },
          "discount": {
            "type": "number"
          },
          "index": {
            "type": "number"
          },
          "item_brand": {
            "type": "string"
          },
          "item_category": {
            "type": "string"
          },
          "item_category2": {
            "type": "string"
          },
          "item_category3": {
            "type": "string"
          },
          "item_category4": {
            "type": "string"
          },
          "item_category5": {
            "type": "string"
          },
          "item_list_id": {
            "type": "string"
          },
          "item_list_name": {
            "type": "string"
          },
          "item_variant": {
            "type": "string"
          },
          "location_id": {
            "type": "string"
          },
          "price": {
            "type": "number"
          },
          "quantity": {
            "type": "number"
          }
        },
        "required": [],
        "additionalProperties": false
      },
      "description": "Purchased items"
    },
    "user_properties": {
      "type": "object",
      "additionalProperties": {
        "type": "object",
        "properties": {
          "value": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "number"
              }
            ]
          }
        },
        "required": [
          "value"
        ],
        "additionalProperties": false
      },
      "description": "User properties (e.g., {subscription_tier: {value: \"premium\"}})"
    }
  },
  "required": [
    "transaction_id",
    "value",
    "currency",
    "items"
  ],
  "additionalProperties": false
}
```

</details>

- Configured GA_MEASUREMENT_ID/GA_API_SECRET select the web stream; neither can be overridden per call. Native API field/event limits and naming restrictions are not enforced locally; arrays have no size bounds, currency has no ISO validation, and item objects allow neither required identifier constraint nor custom item fields.
- Optional string event parameters are only included when truthy; numeric tax/shipping fields (purchase) are included when defined.

Source: [src/index.ts:458](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/index.ts#L458-L495) · [src/measurement-protocol-client.ts:90](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/measurement-protocol-client.ts#L90-L128) · [src/types.ts:101](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/types.ts#L101-L121) · [src/index.ts:76](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/index.ts#L76-L95).

## ga_send_login

Builds one login event from the exposed arguments and posts it to Measurement Protocol /mp/collect. Maps snake_case inputs to helper parameters, generates client_id as timestamp.random when missing or empty, includes user_id/user_properties, and returns success:true plus HTTP status.

<details>
<summary>Full registered description</summary>

```text
Send a login event to Google Analytics.

Standard event for tracking user logins with authentication method.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `client_id` | No | string | Not declared |
| `user_id` | No | string | Not declared |
| `method` | Yes | string | Not declared |
| `user_properties` | No | object | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "client_id": {
      "type": "string"
    },
    "user_id": {
      "type": "string",
      "description": "User ID (recommended for login events)"
    },
    "method": {
      "type": "string",
      "description": "Login method (e.g., \"Google\", \"Email\", \"Facebook\")"
    },
    "user_properties": {
      "type": "object",
      "additionalProperties": {
        "type": "object",
        "properties": {
          "value": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "number"
              }
            ]
          }
        },
        "required": [
          "value"
        ],
        "additionalProperties": false
      },
      "description": "User properties (e.g., {subscription_tier: {value: \"premium\"}})"
    }
  },
  "required": [
    "method"
  ],
  "additionalProperties": false
}
```

</details>

- Configured GA_MEASUREMENT_ID/GA_API_SECRET select the web stream; neither can be overridden per call. Native API field/event limits and naming restrictions are not enforced locally; arrays have no size bounds, currency has no ISO validation, and item objects allow neither required identifier constraint nor custom item fields.

Source: [src/index.ts:497](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/index.ts#L497-L520) · [src/measurement-protocol-client.ts:129](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/measurement-protocol-client.ts#L129-L151) · [src/index.ts:76](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/index.ts#L76-L95).

## ga_send_signup

Builds one sign_up event from the exposed arguments and posts it to Measurement Protocol /mp/collect. Maps snake_case inputs to helper parameters, generates client_id as timestamp.random when missing or empty, includes user_id/user_properties, and returns success:true plus HTTP status.

<details>
<summary>Full registered description</summary>

```text
Send a sign-up event to Google Analytics.

Standard event for tracking new user registrations.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `client_id` | No | string | Not declared |
| `user_id` | No | string | Not declared |
| `method` | Yes | string | Not declared |
| `user_properties` | No | object | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "client_id": {
      "type": "string"
    },
    "user_id": {
      "type": "string",
      "description": "User ID for the new user"
    },
    "method": {
      "type": "string",
      "description": "Sign-up method (e.g., \"Google\", \"Email\")"
    },
    "user_properties": {
      "type": "object",
      "additionalProperties": {
        "type": "object",
        "properties": {
          "value": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "number"
              }
            ]
          }
        },
        "required": [
          "value"
        ],
        "additionalProperties": false
      },
      "description": "User properties (e.g., {subscription_tier: {value: \"premium\"}})"
    }
  },
  "required": [
    "method"
  ],
  "additionalProperties": false
}
```

</details>

- Configured GA_MEASUREMENT_ID/GA_API_SECRET select the web stream; neither can be overridden per call. Native API field/event limits and naming restrictions are not enforced locally; arrays have no size bounds, currency has no ISO validation, and item objects allow neither required identifier constraint nor custom item fields.

Source: [src/index.ts:522](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/index.ts#L522-L545) · [src/measurement-protocol-client.ts:152](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/measurement-protocol-client.ts#L152-L174) · [src/index.ts:76](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/index.ts#L76-L95).

## ga_send_add_to_cart

Builds one add_to_cart event from the exposed arguments and posts it to Measurement Protocol /mp/collect. Maps snake_case inputs to helper parameters, generates client_id as timestamp.random when missing or empty, includes user_id/user_properties, and returns success:true plus HTTP status.

<details>
<summary>Full registered description</summary>

```text
Send an add to cart event to Google Analytics.

Ecommerce event for tracking when items are added to shopping cart.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `client_id` | No | string | Not declared |
| `user_id` | No | string | Not declared |
| `currency` | Yes | string | Not declared |
| `value` | Yes | number | Not declared |
| `items` | Yes | array of object | Not declared |
| `user_properties` | No | object | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "client_id": {
      "type": "string"
    },
    "user_id": {
      "type": "string"
    },
    "currency": {
      "type": "string",
      "description": "Currency code"
    },
    "value": {
      "type": "number",
      "description": "Total value of items added"
    },
    "items": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "item_id": {
            "type": "string"
          },
          "item_name": {
            "type": "string"
          },
          "affiliation": {
            "type": "string"
          },
          "coupon": {
            "type": "string"
          },
          "currency": {
            "type": "string"
          },
          "discount": {
            "type": "number"
          },
          "index": {
            "type": "number"
          },
          "item_brand": {
            "type": "string"
          },
          "item_category": {
            "type": "string"
          },
          "item_category2": {
            "type": "string"
          },
          "item_category3": {
            "type": "string"
          },
          "item_category4": {
            "type": "string"
          },
          "item_category5": {
            "type": "string"
          },
          "item_list_id": {
            "type": "string"
          },
          "item_list_name": {
            "type": "string"
          },
          "item_variant": {
            "type": "string"
          },
          "location_id": {
            "type": "string"
          },
          "price": {
            "type": "number"
          },
          "quantity": {
            "type": "number"
          }
        },
        "required": [],
        "additionalProperties": false
      },
      "description": "Items added to cart"
    },
    "user_properties": {
      "type": "object",
      "additionalProperties": {
        "type": "object",
        "properties": {
          "value": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "number"
              }
            ]
          }
        },
        "required": [
          "value"
        ],
        "additionalProperties": false
      },
      "description": "User properties (e.g., {subscription_tier: {value: \"premium\"}})"
    }
  },
  "required": [
    "currency",
    "value",
    "items"
  ],
  "additionalProperties": false
}
```

</details>

- Configured GA_MEASUREMENT_ID/GA_API_SECRET select the web stream; neither can be overridden per call. Native API field/event limits and naming restrictions are not enforced locally; arrays have no size bounds, currency has no ISO validation, and item objects allow neither required identifier constraint nor custom item fields.

Source: [src/index.ts:547](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/index.ts#L547-L574) · [src/measurement-protocol-client.ts:175](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/measurement-protocol-client.ts#L175-L201) · [src/types.ts:101](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/types.ts#L101-L121) · [src/index.ts:76](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/index.ts#L76-L95).

## ga_send_begin_checkout

Builds one begin_checkout event from the exposed arguments and posts it to Measurement Protocol /mp/collect. Maps snake_case inputs to helper parameters, generates client_id as timestamp.random when missing or empty, includes user_id/user_properties, and returns success:true plus HTTP status.

<details>
<summary>Full registered description</summary>

```text
Send a begin checkout event to Google Analytics.

Ecommerce event for tracking when users start the checkout process.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `client_id` | No | string | Not declared |
| `user_id` | No | string | Not declared |
| `currency` | Yes | string | Not declared |
| `value` | Yes | number | Not declared |
| `coupon` | No | string | Not declared |
| `items` | Yes | array of object | Not declared |
| `user_properties` | No | object | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "client_id": {
      "type": "string"
    },
    "user_id": {
      "type": "string"
    },
    "currency": {
      "type": "string",
      "description": "Currency code"
    },
    "value": {
      "type": "number",
      "description": "Total value of cart"
    },
    "coupon": {
      "type": "string",
      "description": "Coupon code applied"
    },
    "items": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "item_id": {
            "type": "string"
          },
          "item_name": {
            "type": "string"
          },
          "affiliation": {
            "type": "string"
          },
          "coupon": {
            "type": "string"
          },
          "currency": {
            "type": "string"
          },
          "discount": {
            "type": "number"
          },
          "index": {
            "type": "number"
          },
          "item_brand": {
            "type": "string"
          },
          "item_category": {
            "type": "string"
          },
          "item_category2": {
            "type": "string"
          },
          "item_category3": {
            "type": "string"
          },
          "item_category4": {
            "type": "string"
          },
          "item_category5": {
            "type": "string"
          },
          "item_list_id": {
            "type": "string"
          },
          "item_list_name": {
            "type": "string"
          },
          "item_variant": {
            "type": "string"
          },
          "location_id": {
            "type": "string"
          },
          "price": {
            "type": "number"
          },
          "quantity": {
            "type": "number"
          }
        },
        "required": [],
        "additionalProperties": false
      },
      "description": "Items in checkout"
    },
    "user_properties": {
      "type": "object",
      "additionalProperties": {
        "type": "object",
        "properties": {
          "value": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "number"
              }
            ]
          }
        },
        "required": [
          "value"
        ],
        "additionalProperties": false
      },
      "description": "User properties (e.g., {subscription_tier: {value: \"premium\"}})"
    }
  },
  "required": [
    "currency",
    "value",
    "items"
  ],
  "additionalProperties": false
}
```

</details>

- Configured GA_MEASUREMENT_ID/GA_API_SECRET select the web stream; neither can be overridden per call. Native API field/event limits and naming restrictions are not enforced locally; arrays have no size bounds, currency has no ISO validation, and item objects allow neither required identifier constraint nor custom item fields.
- Optional string event parameters are only included when truthy; numeric tax/shipping fields (purchase) are included when defined.

Source: [src/index.ts:576](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/index.ts#L576-L605) · [src/measurement-protocol-client.ts:202](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/measurement-protocol-client.ts#L202-L232) · [src/types.ts:101](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/types.ts#L101-L121) · [src/index.ts:76](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/index.ts#L76-L95).

## ga_send_view_item

Builds one view_item event from the exposed arguments and posts it to Measurement Protocol /mp/collect. Maps snake_case inputs to helper parameters, generates client_id as timestamp.random when missing or empty, includes user_id/user_properties, and returns success:true plus HTTP status.

<details>
<summary>Full registered description</summary>

```text
Send a view item event to Google Analytics.

Ecommerce event for tracking product/item detail views. Completes the standard
funnel: view_item → add_to_cart → begin_checkout → purchase.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `client_id` | No | string | Not declared |
| `user_id` | No | string | Not declared |
| `currency` | Yes | string | Not declared |
| `value` | Yes | number | Not declared |
| `items` | Yes | array of object | Not declared |
| `user_properties` | No | object | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "client_id": {
      "type": "string"
    },
    "user_id": {
      "type": "string"
    },
    "currency": {
      "type": "string",
      "description": "Currency code"
    },
    "value": {
      "type": "number",
      "description": "Value of the viewed item(s)"
    },
    "items": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "item_id": {
            "type": "string"
          },
          "item_name": {
            "type": "string"
          },
          "affiliation": {
            "type": "string"
          },
          "coupon": {
            "type": "string"
          },
          "currency": {
            "type": "string"
          },
          "discount": {
            "type": "number"
          },
          "index": {
            "type": "number"
          },
          "item_brand": {
            "type": "string"
          },
          "item_category": {
            "type": "string"
          },
          "item_category2": {
            "type": "string"
          },
          "item_category3": {
            "type": "string"
          },
          "item_category4": {
            "type": "string"
          },
          "item_category5": {
            "type": "string"
          },
          "item_list_id": {
            "type": "string"
          },
          "item_list_name": {
            "type": "string"
          },
          "item_variant": {
            "type": "string"
          },
          "location_id": {
            "type": "string"
          },
          "price": {
            "type": "number"
          },
          "quantity": {
            "type": "number"
          }
        },
        "required": [],
        "additionalProperties": false
      },
      "description": "Items viewed"
    },
    "user_properties": {
      "type": "object",
      "additionalProperties": {
        "type": "object",
        "properties": {
          "value": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "number"
              }
            ]
          }
        },
        "required": [
          "value"
        ],
        "additionalProperties": false
      },
      "description": "User properties (e.g., {subscription_tier: {value: \"premium\"}})"
    }
  },
  "required": [
    "currency",
    "value",
    "items"
  ],
  "additionalProperties": false
}
```

</details>

- Configured GA_MEASUREMENT_ID/GA_API_SECRET select the web stream; neither can be overridden per call. Native API field/event limits and naming restrictions are not enforced locally; arrays have no size bounds, currency has no ISO validation, and item objects allow neither required identifier constraint nor custom item fields.

Source: [src/index.ts:607](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/index.ts#L607-L635) · [src/measurement-protocol-client.ts:233](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/measurement-protocol-client.ts#L233-L259) · [src/types.ts:101](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/types.ts#L101-L121) · [src/index.ts:76](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/index.ts#L76-L95).

## ga_send_refund

Builds one refund event from the exposed arguments and posts it to Measurement Protocol /mp/collect. Maps snake_case inputs to helper parameters, generates client_id as timestamp.random when missing or empty, includes user_id/user_properties, and returns success:true plus HTTP status.

<details>
<summary>Full registered description</summary>

```text
Send a refund event to Google Analytics.

Ecommerce event for full or partial refunds. Omit 'items' for a full refund;
include them (with quantities) for a partial refund. Use the same transaction_id
as the original purchase.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `client_id` | No | string | Not declared |
| `user_id` | No | string | Not declared |
| `transaction_id` | Yes | string | Not declared |
| `currency` | No | string | Not declared |
| `value` | No | number | Not declared |
| `items` | No | array of object | Not declared |
| `user_properties` | No | object | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "client_id": {
      "type": "string"
    },
    "user_id": {
      "type": "string"
    },
    "transaction_id": {
      "type": "string",
      "description": "Transaction ID of the original purchase"
    },
    "currency": {
      "type": "string",
      "description": "Currency code"
    },
    "value": {
      "type": "number",
      "description": "Refunded amount"
    },
    "items": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "item_id": {
            "type": "string"
          },
          "item_name": {
            "type": "string"
          },
          "affiliation": {
            "type": "string"
          },
          "coupon": {
            "type": "string"
          },
          "currency": {
            "type": "string"
          },
          "discount": {
            "type": "number"
          },
          "index": {
            "type": "number"
          },
          "item_brand": {
            "type": "string"
          },
          "item_category": {
            "type": "string"
          },
          "item_category2": {
            "type": "string"
          },
          "item_category3": {
            "type": "string"
          },
          "item_category4": {
            "type": "string"
          },
          "item_category5": {
            "type": "string"
          },
          "item_list_id": {
            "type": "string"
          },
          "item_list_name": {
            "type": "string"
          },
          "item_variant": {
            "type": "string"
          },
          "location_id": {
            "type": "string"
          },
          "price": {
            "type": "number"
          },
          "quantity": {
            "type": "number"
          }
        },
        "required": [],
        "additionalProperties": false
      },
      "description": "Refunded items (only for partial refunds)"
    },
    "user_properties": {
      "type": "object",
      "additionalProperties": {
        "type": "object",
        "properties": {
          "value": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "number"
              }
            ]
          }
        },
        "required": [
          "value"
        ],
        "additionalProperties": false
      },
      "description": "User properties (e.g., {subscription_tier: {value: \"premium\"}})"
    }
  },
  "required": [
    "transaction_id"
  ],
  "additionalProperties": false
}
```

</details>

- Configured GA_MEASUREMENT_ID/GA_API_SECRET select the web stream; neither can be overridden per call. Native API field/event limits and naming restrictions are not enforced locally; arrays have no size bounds, currency has no ISO validation, and item objects allow neither required identifier constraint nor custom item fields.
- An omitted or empty items array is not sent; truthy currency and defined value are included.

Source: [src/index.ts:637](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/index.ts#L637-L668) · [src/measurement-protocol-client.ts:260](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/measurement-protocol-client.ts#L260-L291) · [src/types.ts:101](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/types.ts#L101-L121) · [src/index.ts:76](https://github.com/leonardosepulvedat/mcp-google-analytics/blob/97731c9bcf801297b0c8f0cd34cdde903730f2a2/src/index.ts#L76-L95).

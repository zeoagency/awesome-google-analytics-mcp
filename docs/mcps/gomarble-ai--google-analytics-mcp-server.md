# gomarble-ai/google-analytics-mcp-server

[Catalog](../../README.md) · [All tool names](../tool-index.md) · [Upstream](https://github.com/gomarble-ai/google-analytics-mcp-server) · [JSON](../../data/mcps/gomarble-ai--google-analytics-mcp-server.json)

**7 tools:** 7 GA4, 0 other-service or server-support tools. Reviewed source: [`42b4fa21874c`](https://github.com/gomarble-ai/google-analytics-mcp-server/tree/42b4fa21874c66d3b3bb0c5d47d0a8f0541cbc33).

Descriptions and parameter schemas come from the registered source definitions. Generated schemas are reconstructed from annotations or validators; live `tools/list` and authenticated API calls were not run. Loose objects remain loose.

<details>
<summary>Exposure and compatibility notes</summary>

- Source review only; no tools/list, server imports/execution, or live requests. Git HEAD matches supplied revision.
- All seven tools are registered unconditionally in server.py. ga4://reference is a resource, not a tool. OAuth module registers no tools.
- Schemas reconstruct signature annotations/defaults and Args docstrings; no custom Pydantic models, Field constraints, enums, or aliases. Unspecified additionalProperties at top level is left unspecified.
- Every GA call can trigger interactive OAuth, refresh credentials, and write google_analytics_token.json beside OAuth config. GOOGLE_ANALYTICS_OAUTH_CONFIG_PATH must point to a readable client config. OAuth scopes include analytics and analytics.readonly; handlers only read GA data.
- requirements.txt uses unpinned fastmcp>=0.8.0; exact runtime-generated schema cosmetic fields are version-dependent. Context logging methods are called without await in synchronous handlers; asynchronous FastMCP logging implementations may not emit these messages.
- OAuth console fallback calls flow.run_console(), whose availability depends on installed google-auth-oauthlib version. Local-server OAuth is the primary path.

</details>

## Tools

| Tool | Scope | Effect |
| --- | --- | --- |
| [`list_properties`](#list_properties) | GA4 | read |
| [`get_page_views`](#get_page_views) | GA4 | read |
| [`get_active_users`](#get_active_users) | GA4 | read |
| [`get_events`](#get_events) | GA4 | read |
| [`get_traffic_sources`](#get_traffic_sources) | GA4 | read |
| [`get_device_metrics`](#get_device_metrics) | GA4 | read |
| [`run_report`](#run_report) | GA4 | read |

## list_properties

GET a specified account or all accessible accounts, retry v1beta after an unsuccessful v1 account response; GET properties for each account, retry using /properties?filter=parent:accounts/{id} after the initial nested /accounts/{id}/properties URL fails. Return hierarchical account/property details and summary counts. Uses get_headers_with_auto_token for OAuth.

<details>
<summary>Full registered description</summary>

```text
List all Google Analytics 4 accounts with their associated properties in a hierarchical structure.

Args:
    account_id: Optional specific Google Analytics account ID to list properties for.
               If not provided, will list all accessible accounts with their properties.

Returns:
    Hierarchical structure showing Account ID/Name with all associated Property IDs/Names
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
      "description": "Optional specific Google Analytics account ID to list properties for.\nIf not provided, will list all accessible accounts with their properties.",
      "default": ""
    }
  },
  "required": []
}
```

</details>

- ctx: Context = None is an injected FastMCP Context and is excluded from the exposed input schema.
- Account and property listing do not follow nextPageToken; only first pages are included.
- In all-accounts mode property failures can silently produce empty property lists; specific-account mode raises.
- No numeric account-ID constraint is imposed by the signature.

Source: [server.py:24](https://github.com/gomarble-ai/google-analytics-mcp-server/blob/42b4fa21874c66d3b3bb0c5d47d0a8f0541cbc33/server.py#L24-L215).

## get_page_views

Obtain OAuth headers and POST the report_template payload, replacing dimensions when a nonempty list is supplied. Return raw JSON response when rows exist; otherwise return only a message. Unsuccessful HTTP responses raise an exception.

<details>
<summary>Full registered description</summary>

```text
Get page view metrics for a specific date range from Google Analytics 4.

Args:
    property_id: Google Analytics 4 property ID (numeric, e.g., "123456789")
    start_date: Start date in YYYY-MM-DD format
    end_date: End date in YYYY-MM-DD format
    dimensions: List of dimensions to group by (optional, defaults to ["pagePath"])

Returns:
    Page view metrics grouped by specified dimensions in JSON format
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |
| `start_date` | Yes | string | Not declared |
| `end_date` | Yes | string | Not declared |
| `dimensions` | No | array of string or null | null |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "property_id": {
      "type": "string",
      "description": "Google Analytics 4 property ID (numeric, e.g., \"123456789\")"
    },
    "start_date": {
      "type": "string",
      "description": "Start date in YYYY-MM-DD format"
    },
    "end_date": {
      "type": "string",
      "description": "End date in YYYY-MM-DD format"
    },
    "dimensions": {
      "anyOf": [
        {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        {
          "type": "null"
        }
      ],
      "description": "List of dimensions to group by (optional, defaults to [\"pagePath\"])",
      "default": null
    }
  },
  "required": [
    "property_id",
    "start_date",
    "end_date"
  ]
}
```

</details>

- ctx: Context = None is an injected FastMCP Context and is excluded from the exposed input schema.
- Date format and numeric property ID are docstring guidance only: no schema format, pattern or numeric constraint.
- No report pagination or retry logic; no timeout is passed to requests.post.

Source: [server.py:217](https://github.com/gomarble-ai/google-analytics-mcp-server/blob/42b4fa21874c66d3b3bb0c5d47d0a8f0541cbc33/server.py#L217-L282).

## get_active_users

Obtain OAuth headers and POST the report_template payload, replacing dimensions when a nonempty list is supplied. Return raw JSON response when rows exist; otherwise return only a message. Unsuccessful HTTP responses raise an exception.

<details>
<summary>Full registered description</summary>

```text
Get active users metrics for a specific date range from Google Analytics 4.

Args:
    property_id: Google Analytics 4 property ID (numeric, e.g., "123456789")
    start_date: Start date in YYYY-MM-DD format
    end_date: End date in YYYY-MM-DD format
    dimensions: List of dimensions to group by (optional, defaults to ["date"])

Returns:
    Active users metrics grouped by specified dimensions in JSON format
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |
| `start_date` | Yes | string | Not declared |
| `end_date` | Yes | string | Not declared |
| `dimensions` | No | array of string or null | null |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "property_id": {
      "type": "string",
      "description": "Google Analytics 4 property ID (numeric, e.g., \"123456789\")"
    },
    "start_date": {
      "type": "string",
      "description": "Start date in YYYY-MM-DD format"
    },
    "end_date": {
      "type": "string",
      "description": "End date in YYYY-MM-DD format"
    },
    "dimensions": {
      "anyOf": [
        {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        {
          "type": "null"
        }
      ],
      "description": "List of dimensions to group by (optional, defaults to [\"date\"])",
      "default": null
    }
  },
  "required": [
    "property_id",
    "start_date",
    "end_date"
  ]
}
```

</details>

- ctx: Context = None is an injected FastMCP Context and is excluded from the exposed input schema.
- Date format and numeric property ID are docstring guidance only: no schema format, pattern or numeric constraint.
- No report pagination or retry logic; no timeout is passed to requests.post.

Source: [server.py:284](https://github.com/gomarble-ai/google-analytics-mcp-server/blob/42b4fa21874c66d3b3bb0c5d47d0a8f0541cbc33/server.py#L284-L349).

## get_events

Obtain OAuth headers and POST the report_template payload, replacing dimensions when a nonempty list is supplied. Return raw JSON response when rows exist; otherwise return only a message. Unsuccessful HTTP responses raise an exception.

<details>
<summary>Full registered description</summary>

```text
Get event metrics for a specific date range from Google Analytics 4.

Args:
    property_id: Google Analytics 4 property ID (numeric, e.g., "123456789")
    start_date: Start date in YYYY-MM-DD format
    end_date: End date in YYYY-MM-DD format
    dimensions: List of dimensions to group by (optional, defaults to ["eventName"])

Returns:
    Event metrics grouped by specified dimensions in JSON format
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |
| `start_date` | Yes | string | Not declared |
| `end_date` | Yes | string | Not declared |
| `dimensions` | No | array of string or null | null |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "property_id": {
      "type": "string",
      "description": "Google Analytics 4 property ID (numeric, e.g., \"123456789\")"
    },
    "start_date": {
      "type": "string",
      "description": "Start date in YYYY-MM-DD format"
    },
    "end_date": {
      "type": "string",
      "description": "End date in YYYY-MM-DD format"
    },
    "dimensions": {
      "anyOf": [
        {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        {
          "type": "null"
        }
      ],
      "description": "List of dimensions to group by (optional, defaults to [\"eventName\"])",
      "default": null
    }
  },
  "required": [
    "property_id",
    "start_date",
    "end_date"
  ]
}
```

</details>

- ctx: Context = None is an injected FastMCP Context and is excluded from the exposed input schema.
- Date format and numeric property ID are docstring guidance only: no schema format, pattern or numeric constraint.
- No report pagination or retry logic; no timeout is passed to requests.post.

Source: [server.py:351](https://github.com/gomarble-ai/google-analytics-mcp-server/blob/42b4fa21874c66d3b3bb0c5d47d0a8f0541cbc33/server.py#L351-L416).

## get_traffic_sources

Obtain OAuth headers and POST the report_template payload, replacing dimensions when a nonempty list is supplied. Return raw JSON response when rows exist; otherwise return only a message. Unsuccessful HTTP responses raise an exception.

<details>
<summary>Full registered description</summary>

```text
Get traffic source metrics for a specific date range from Google Analytics 4.

Args:
    property_id: Google Analytics 4 property ID (numeric, e.g., "123456789")
    start_date: Start date in YYYY-MM-DD format
    end_date: End date in YYYY-MM-DD format
    dimensions: List of dimensions to group by (optional, defaults to ["source", "medium"])

Returns:
    Traffic source metrics grouped by specified dimensions in JSON format
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |
| `start_date` | Yes | string | Not declared |
| `end_date` | Yes | string | Not declared |
| `dimensions` | No | array of string or null | null |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "property_id": {
      "type": "string",
      "description": "Google Analytics 4 property ID (numeric, e.g., \"123456789\")"
    },
    "start_date": {
      "type": "string",
      "description": "Start date in YYYY-MM-DD format"
    },
    "end_date": {
      "type": "string",
      "description": "End date in YYYY-MM-DD format"
    },
    "dimensions": {
      "anyOf": [
        {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        {
          "type": "null"
        }
      ],
      "description": "List of dimensions to group by (optional, defaults to [\"source\", \"medium\"])",
      "default": null
    }
  },
  "required": [
    "property_id",
    "start_date",
    "end_date"
  ]
}
```

</details>

- ctx: Context = None is an injected FastMCP Context and is excluded from the exposed input schema.
- Date format and numeric property ID are docstring guidance only: no schema format, pattern or numeric constraint.
- No report pagination or retry logic; no timeout is passed to requests.post.

Source: [server.py:418](https://github.com/gomarble-ai/google-analytics-mcp-server/blob/42b4fa21874c66d3b3bb0c5d47d0a8f0541cbc33/server.py#L418-L483).

## get_device_metrics

Obtain OAuth headers and POST the report_template payload, replacing dimensions when a nonempty list is supplied. Return raw JSON response when rows exist; otherwise return only a message. Unsuccessful HTTP responses raise an exception.

<details>
<summary>Full registered description</summary>

```text
Get device metrics for a specific date range from Google Analytics 4.

Args:
    property_id: Google Analytics 4 property ID (numeric, e.g., "123456789")
    start_date: Start date in YYYY-MM-DD format
    end_date: End date in YYYY-MM-DD format
    dimensions: List of dimensions to group by (optional, defaults to ["deviceCategory"])

Returns:
    Device metrics grouped by specified dimensions in JSON format
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |
| `start_date` | Yes | string | Not declared |
| `end_date` | Yes | string | Not declared |
| `dimensions` | No | array of string or null | null |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "property_id": {
      "type": "string",
      "description": "Google Analytics 4 property ID (numeric, e.g., \"123456789\")"
    },
    "start_date": {
      "type": "string",
      "description": "Start date in YYYY-MM-DD format"
    },
    "end_date": {
      "type": "string",
      "description": "End date in YYYY-MM-DD format"
    },
    "dimensions": {
      "anyOf": [
        {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        {
          "type": "null"
        }
      ],
      "description": "List of dimensions to group by (optional, defaults to [\"deviceCategory\"])",
      "default": null
    }
  },
  "required": [
    "property_id",
    "start_date",
    "end_date"
  ]
}
```

</details>

- ctx: Context = None is an injected FastMCP Context and is excluded from the exposed input schema.
- Date format and numeric property ID are docstring guidance only: no schema format, pattern or numeric constraint.
- No report pagination or retry logic; no timeout is passed to requests.post.

Source: [server.py:485](https://github.com/gomarble-ai/google-analytics-mcp-server/blob/42b4fa21874c66d3b3bb0c5d47d0a8f0541cbc33/server.py#L485-L550).

## run_report

Validate nonempty string property_id/start_date/end_date and nonempty metrics list, obtain OAuth headers, and POST report_template. Strip metric/dimension names. Return GA response with metadata overwritten by local request metadata and returned row count; no rows returns a message with request metadata and total_rows=0. Unsuccessful HTTP responses raise.

<details>
<summary>Full registered description</summary>

```text
Execute a comprehensive Google Analytics 4 report with full customization capabilities.

IMPORTANT: Use STRING ARRAYS for metrics and dimensions, NOT objects!

CORRECT FORMAT:
- metrics: ["sessions", "totalUsers", "screenPageViews"]
- dimensions: ["country", "deviceCategory"]

INCORRECT FORMAT (will fail):
- metrics: [{"name": "sessions"}]
- dimensions: [{"name": "country"}]

VALID GA4 METRICS:
- sessions, totalUsers, activeUsers, newUsers
- screenPageViews, pageviews, bounceRate, engagementRate
- averageSessionDuration, userEngagementDuration, engagedSessions
- conversions, totalRevenue, purchaseRevenue
- eventCount, eventsPerSession

COMMON METRIC MISTAKES:
- uniquePageviews (not valid) → use screenPageViews
- pageViews (not valid) → use screenPageViews
- users (not valid) → use totalUsers or activeUsers
- sessionDuration (not valid) → use averageSessionDuration
- conversionsPerSession (not valid) → use eventsPerSession
- conversionRate (not valid) → calculate manually

VALID GA4 DIMENSIONS:
- country, city, region, continent
- deviceCategory, operatingSystem, browser
- source, medium, campaignName, sessionDefaultChannelGroup
- pagePath, pageTitle, landingPage
- date, month, year, hour, dayOfWeek
- sessionSource, sessionMedium, sessionCampaignName

COMMON DIMENSION MISTAKES:
- channelGroup (not valid) → use sessionDefaultChannelGroup
- sessionCampaign (not valid) → use sessionCampaignName
- campaign (not valid) → use campaignName

SORTING (order_bys) - EXPERIMENTAL:
- For metrics: [{"metric": {"metricName": "sessions"}, "desc": true}]
- For dimensions: [{"dimension": {"dimensionName": "country"}, "desc": false}]
- WARNING: Sorting may fail due to JSON parsing issues. Test without sorting first.

Args:
    property_id: Google Analytics 4 property ID (numeric, e.g., "421301275")
    start_date: Start date in YYYY-MM-DD format (e.g., "2025-01-01")
    end_date: End date in YYYY-MM-DD format (e.g., "2025-01-31")
    metrics: Array of metric names as STRINGS (e.g., ["sessions", "totalUsers"])
    dimensions: Optional array of dimension names as STRINGS (e.g., ["country", "deviceCategory"])
    limit: Optional maximum number of rows (default: 100)
    offset: Optional number of rows to skip (default: 0)
    order_bys: Optional sorting - see format above
    dimension_filter: Optional filter for dimensions
    metric_filter: Optional filter for metrics
    keep_empty_rows: Optional boolean to include empty rows

Returns:
    Comprehensive JSON report with requested metrics and dimensions

WORKING EXAMPLES:

Basic Sessions Report:
{
  "property_id": "421301275",
  "start_date": "2025-01-01",
  "end_date": "2025-01-31",
  "metrics": ["sessions", "totalUsers", "screenPageViews"]
}

Traffic by Country:
{
  "property_id": "421301275",
  "start_date": "2025-01-01",
  "end_date": "2025-01-31",
  "metrics": ["sessions", "totalUsers"],
  "dimensions": ["country", "deviceCategory"],
  "limit": 20
}

Top Pages Report:
{
  "property_id": "421301275",
  "start_date": "2025-01-01",
  "end_date": "2025-01-31",
  "metrics": ["screenPageViews", "sessions"],
  "dimensions": ["pagePath"],
  "limit": 10
}
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |
| `start_date` | Yes | string | Not declared |
| `end_date` | Yes | string | Not declared |
| `metrics` | Yes | array of string | Not declared |
| `dimensions` | No | array of string or null | null |
| `limit` | No | integer or null | null |
| `offset` | No | integer or null | null |
| `order_bys` | No | array of object or null | null |
| `dimension_filter` | No | object or null | null |
| `metric_filter` | No | object or null | null |
| `keep_empty_rows` | No | boolean or null | null |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "property_id": {
      "type": "string",
      "description": "Google Analytics 4 property ID (numeric, e.g., \"421301275\")"
    },
    "start_date": {
      "type": "string",
      "description": "Start date in YYYY-MM-DD format (e.g., \"2025-01-01\")"
    },
    "end_date": {
      "type": "string",
      "description": "End date in YYYY-MM-DD format (e.g., \"2025-01-31\")"
    },
    "metrics": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Array of metric names as STRINGS (e.g., [\"sessions\", \"totalUsers\"])"
    },
    "dimensions": {
      "anyOf": [
        {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        {
          "type": "null"
        }
      ],
      "description": "Optional array of dimension names as STRINGS (e.g., [\"country\", \"deviceCategory\"])",
      "default": null
    },
    "limit": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "description": "Optional maximum number of rows (default: 100)",
      "default": null
    },
    "offset": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "description": "Optional number of rows to skip (default: 0)",
      "default": null
    },
    "order_bys": {
      "anyOf": [
        {
          "type": "array",
          "items": {
            "type": "object",
            "additionalProperties": {}
          }
        },
        {
          "type": "null"
        }
      ],
      "description": "Optional sorting - see format above",
      "default": null
    },
    "dimension_filter": {
      "anyOf": [
        {
          "type": "object",
          "additionalProperties": {}
        },
        {
          "type": "null"
        }
      ],
      "description": "Optional filter for dimensions",
      "default": null
    },
    "metric_filter": {
      "anyOf": [
        {
          "type": "object",
          "additionalProperties": {}
        },
        {
          "type": "null"
        }
      ],
      "description": "Optional filter for metrics",
      "default": null
    },
    "keep_empty_rows": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "description": "Optional boolean to include empty rows",
      "default": null
    }
  },
  "required": [
    "property_id",
    "start_date",
    "end_date",
    "metrics"
  ]
}
```

</details>

- ctx: Context = None is an injected FastMCP Context and is excluded from the exposed input schema.
- Docstring advertises default limit=100 and offset=0, but signature defaults both to None; omitted values are not sent.
- limit <= 0 and offset < 0 are silently omitted; these are handler conditions, not schema constraints.
- metrics must be nonempty in handler, but signature has no minItems.
- order_bys items and filters are arbitrary Dict[str, Any] objects; nested GA filter/order structures are forwarded unchanged and have no exposed structured validators.
- Metric/dimension examples and validity claims in docstring are not enums or server validation.
- Handler overwrites upstream metadata rather than merging.
- Date format and numeric property ID are docstring guidance only: no schema format, pattern or numeric constraint.
- No report pagination or retry logic; no timeout is passed to requests.post.

Source: [server.py:552](https://github.com/gomarble-ai/google-analytics-mcp-server/blob/42b4fa21874c66d3b3bb0c5d47d0a8f0541cbc33/server.py#L552-L753).

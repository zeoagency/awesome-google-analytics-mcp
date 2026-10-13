# dhawalshah/google-analytics-mcp

[Catalog](../../README.md) · [All tool names](../tool-index.md) · [Upstream](https://github.com/dhawalshah/google-analytics-mcp) · [JSON](../../data/mcps/dhawalshah--google-analytics-mcp.json)

**10 tools:** 10 GA4, 0 other-service or server-support tools. Reviewed source: [`ef0a3415025f`](https://github.com/dhawalshah/google-analytics-mcp/tree/ef0a3415025f891d06354be3379a3c7c1f3bd1f7).

Descriptions and parameter schemas come from the registered source definitions. Generated schemas are reconstructed from annotations or validators; live `tools/list` and authenticated API calls were not run. Loose objects remain loose.

<details>
<summary>Exposure and compatibility notes</summary>

- Source review only, no tools/list or live requests; upstream code was not executed.
- All ten tools are registered unconditionally in server.py; no optional tool modules or permission tiers were found. main.py imports the same mcp instance. ga4://reference is a resource, not a tool; OAuth endpoints and setup_local_auth.py are not MCP tools.
- Schemas reconstructed from annotations/defaults and complete docstrings. Context ctx is injected and excluded. No Pydantic/TypedDict request models or explicit schema validators are present; nested Any dictionaries remain loose. Docstring parameter prose is retained as descriptions, with no invented date format or numeric property-ID constraints.
- Each handler uses get_headers_with_auto_token. STDIO requires MCP_USER_EMAIL plus an existing local OAuth token created by setup_local_auth.py; HTTP mode resolves a per-user Firestore token. No automatic interactive OAuth flow is actually initiated by this helper despite handler comments. Credential refresh can persist tokens locally or in Firestore; GA operations themselves are read-only.
- requirements.txt specifies fastmcp>=2.0.0 without an upper pin, so generated runtime schema details may depend on installed version; this is source-derived extraction.

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
| [`get_realtime_users`](#get_realtime_users) | GA4 | read |
| [`get_property_metadata`](#get_property_metadata) | GA4 | read |
| [`run_funnel_report`](#run_funnel_report) | GA4 | read |
| [`run_report`](#run_report) | GA4 | read |

## list_properties

GETs either a specific account or all accounts using v1 with v1beta fallback; retrieves each account’s properties, trying an account-nested URL first and then properties?filter=parent:accounts/ID. Returns hierarchy, counts and selected property/account metadata.

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
      "default": "",
      "description": "Optional specific Google Analytics account ID to list properties for.\nIf not provided, will list all accessible accounts with their properties."
    }
  },
  "required": []
}
```

</details>

- Does not follow account or property nextPageToken; results can be incomplete.
- For all-account mode, failed property requests can silently produce an empty property list. Account-nested property URL is attempted before the filtered properties.list fallback.

Source: [server.py:24](https://github.com/dhawalshah/google-analytics-mcp/blob/ef0a3415025f891d06354be3379a3c7c1f3bd1f7/server.py#L24-L215).

## get_page_views

POSTs a constructed runReport request for one date range with screenPageViews metrics. Converts dimension strings to name objects; missing, null or empty dimensions use pagePath. Returns raw report JSON, or a message when no rows exist.

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
      "default": null,
      "description": "List of dimensions to group by (optional, defaults to [\"pagePath\"])"
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

- Convenience wrapper over runReport, not a separate native GA API method. Handler dimension fallback applies to an empty array as well as null.

Source: [server.py:217](https://github.com/dhawalshah/google-analytics-mcp/blob/ef0a3415025f891d06354be3379a3c7c1f3bd1f7/server.py#L217-L282).

## get_active_users

POSTs a constructed runReport request for one date range with activeUsers metrics. Converts dimension strings to name objects; missing, null or empty dimensions use date. Returns raw report JSON, or a message when no rows exist.

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
      "default": null,
      "description": "List of dimensions to group by (optional, defaults to [\"date\"])"
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

- Convenience wrapper over runReport, not a separate native GA API method. Handler dimension fallback applies to an empty array as well as null.

Source: [server.py:284](https://github.com/dhawalshah/google-analytics-mcp/blob/ef0a3415025f891d06354be3379a3c7c1f3bd1f7/server.py#L284-L349).

## get_events

POSTs a constructed runReport request for one date range with eventCount metrics. Converts dimension strings to name objects; missing, null or empty dimensions use eventName. Returns raw report JSON, or a message when no rows exist.

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
      "default": null,
      "description": "List of dimensions to group by (optional, defaults to [\"eventName\"])"
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

- Convenience wrapper over runReport, not a separate native GA API method. Handler dimension fallback applies to an empty array as well as null.

Source: [server.py:351](https://github.com/dhawalshah/google-analytics-mcp/blob/ef0a3415025f891d06354be3379a3c7c1f3bd1f7/server.py#L351-L416).

## get_traffic_sources

POSTs a constructed runReport request for one date range with sessions and totalUsers metrics. Converts dimension strings to name objects; missing, null or empty dimensions use source and medium. Returns raw report JSON, or a message when no rows exist.

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
      "default": null,
      "description": "List of dimensions to group by (optional, defaults to [\"source\", \"medium\"])"
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

- Convenience wrapper over runReport, not a separate native GA API method. Handler dimension fallback applies to an empty array as well as null.

Source: [server.py:418](https://github.com/dhawalshah/google-analytics-mcp/blob/ef0a3415025f891d06354be3379a3c7c1f3bd1f7/server.py#L418-L483).

## get_device_metrics

POSTs a constructed runReport request for one date range with sessions and screenPageViews metrics. Converts dimension strings to name objects; missing, null or empty dimensions use deviceCategory. Returns raw report JSON, or a message when no rows exist.

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
      "default": null,
      "description": "List of dimensions to group by (optional, defaults to [\"deviceCategory\"])"
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

- Convenience wrapper over runReport, not a separate native GA API method. Handler dimension fallback applies to an empty array as well as null.

Source: [server.py:485](https://github.com/dhawalshah/google-analytics-mcp/blob/ef0a3415025f891d06354be3379a3c7c1f3bd1f7/server.py#L485-L550).

## get_realtime_users

POSTs runRealtimeReport with activeUsers and provided dimension name objects, falling back to unifiedScreenName on null or empty dimensions. Returns response JSON or message and activeUsers:0 when no rows exist; accepts no date range.

<details>
<summary>Full registered description</summary>

```text
Get active users in the last 30 minutes from Google Analytics 4.

This uses the Realtime API — a different endpoint from standard reports.
Data reflects activity within the last 30 minutes only; no date range applies.

Args:
    property_id: Google Analytics 4 property ID (numeric, e.g., "123456789")
    dimensions: Dimensions to break down by (optional, defaults to ["unifiedScreenName"])
               Other useful values: "country", "deviceCategory", "eventName"

Returns:
    Active user counts per dimension value for the last 30 minutes
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |
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
      "default": null,
      "description": "Dimensions to break down by (optional, defaults to [\"unifiedScreenName\"])\nOther useful values: \"country\", \"deviceCategory\", \"eventName\""
    }
  },
  "required": [
    "property_id"
  ]
}
```

</details>

Source: [server.py:552](https://github.com/dhawalshah/google-analytics-mcp/blob/ef0a3415025f891d06354be3379a3c7c1f3bd1f7/server.py#L552-L611).

## get_property_metadata

GETs properties/ID/metadata and maps dimensions and metrics to name, description, uiName, customDefinition and metric type, with counts.

<details>
<summary>Full registered description</summary>

```text
List all valid dimensions and metrics available for a Google Analytics 4 property.

Use this before calling run_report to discover which metric and dimension names
are valid for a specific property. Different properties may have custom dimensions
and metrics in addition to the standard GA4 ones.

Args:
    property_id: Google Analytics 4 property ID (numeric, e.g., "123456789")

Returns:
    Two lists — available dimensions and available metrics — each with name and description
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
      "description": "Google Analytics 4 property ID (numeric, e.g., \"123456789\")"
    }
  },
  "required": [
    "property_id"
  ]
}
```

</details>

Source: [server.py:613](https://github.com/dhawalshah/google-analytics-mcp/blob/ef0a3415025f891d06354be3379a3c7c1f3bd1f7/server.py#L613-L682).

## run_funnel_report

Validates at least two steps and POSTs one date range and funnel.steps unchanged to runFunnelReport; a nonempty breakdown_dimension builds funnelBreakdown.breakdownDimension.dimensionName. Returns API JSON.

<details>
<summary>Full registered description</summary>

```text
Run a funnel analysis report for a Google Analytics 4 property.

WARNING: EXPERIMENTAL: This uses the GA4 Data API v1alpha endpoint which is unstable
and may break or change without notice.

A funnel shows how many users complete each step in a sequence — e.g.
homepage -> product page -> add to cart -> purchase.

Each step in `steps` must be a dict with:
  - "name": human-readable step label (e.g. "Homepage")
  - "filterExpression": a GA4 funnel filter expression dict

STEP FORMAT EXAMPLES:

Page path step:
{
  "name": "Homepage",
  "filterExpression": {
    "funnelFieldFilter": {
      "fieldName": "pagePath",
      "stringFilter": {"matchType": "EXACT", "value": "/"}
    }
  }
}

Event step:
{
  "name": "Purchase",
  "filterExpression": {
    "funnelEventFilter": {
      "eventName": "purchase"
    }
  }
}

Args:
    property_id: Google Analytics 4 property ID (numeric, e.g., "123456789")
    start_date: Start date in YYYY-MM-DD format
    end_date: End date in YYYY-MM-DD format
    steps: List of funnel step dicts (minimum 2 steps)
    breakdown_dimension: Optional dimension to break down funnel by (e.g. "deviceCategory")

Returns:
    Funnel step data showing user counts and drop-off at each stage
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |
| `start_date` | Yes | string | Not declared |
| `end_date` | Yes | string | Not declared |
| `steps` | Yes | array of object | Not declared |
| `breakdown_dimension` | No | string or null | null |

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
    "steps": {
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": {}
      },
      "description": "List of funnel step dicts (minimum 2 steps)"
    },
    "breakdown_dimension": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional dimension to break down funnel by (e.g. \"deviceCategory\")"
    }
  },
  "required": [
    "property_id",
    "start_date",
    "end_date",
    "steps"
  ]
}
```

</details>

- Experimental v1alpha endpoint.
- Minimum two steps is a handler restriction, not an annotation/schema constraint. Step dictionaries are intentionally arbitrary Dict[str, Any]; name and filterExpression are documented but not schema-enforced.
- No full native funnel request schema is exposed; only the wrapper parameters are exposed.

Source: [server.py:684](https://github.com/dhawalshah/google-analytics-mcp/blob/ef0a3415025f891d06354be3379a3c7c1f3bd1f7/server.py#L684-L783).

## run_report

Checks nonempty property/date strings and metrics list, strips metric and dimension names and builds one date range. POSTs runReport, forwarding nonempty order_bys and filter dictionaries unchanged, positive limit, nonnegative offset, and non-null keep_empty_rows. Returns report JSON with server-generated metadata replacing any API metadata; no rows yields a summary message object.

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
      "default": null,
      "description": "Optional array of dimension names as STRINGS (e.g., [\"country\", \"deviceCategory\"])"
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
      "default": null,
      "description": "Optional maximum number of rows (default: 100)"
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
      "default": null,
      "description": "Optional number of rows to skip (default: 0)"
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
      "default": null,
      "description": "Optional sorting - see format above"
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
      "default": null,
      "description": "Optional filter for dimensions"
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
      "default": null,
      "description": "Optional filter for metrics"
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
      "default": null,
      "description": "Optional boolean to include empty rows"
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

- metrics must be nonempty by handler validation; schema has no minItems. property_id, start_date and end_date must be nonempty strings by handler validation but dates are not parsed.
- The declared defaults for limit and offset are null, despite docstring claims of 100 and 0; omitted values are not inserted into the API payload.
- limit <= 0 and offset < 0 are silently omitted by handler, rather than rejected by schema.
- order_bys entries, dimension_filter and metric_filter are arbitrary dictionaries, not typed nested GA models.
- This is a constructed runReport wrapper, not the full native RunReportRequest schema.

Source: [server.py:785](https://github.com/dhawalshah/google-analytics-mcp/blob/ef0a3415025f891d06354be3379a3c7c1f3bd1f7/server.py#L785-L986).

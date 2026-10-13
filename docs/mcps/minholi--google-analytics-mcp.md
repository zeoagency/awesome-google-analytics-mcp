# minholi/google-analytics-mcp

[Catalog](../../README.md) · [All tool names](../tool-index.md) · [Upstream](https://github.com/minholi/google-analytics-mcp) · [JSON](../../data/mcps/minholi--google-analytics-mcp.json)

**8 tools:** 8 GA4, 0 other-service or server-support tools. Reviewed source: [`21a816a16df6`](https://github.com/minholi/google-analytics-mcp/tree/21a816a16df6cb5d45783c1479ea72b585ab849b).

Descriptions and parameter schemas come from the registered source definitions. Generated schemas are reconstructed from annotations or validators; live `tools/list` and authenticated API calls were not run. Loose objects remain loose.

<details>
<summary>Exposure and compatibility notes</summary>

- Source review only, no tools/list or live requests. HEAD matches assigned revision.
- All eight tools are unconditional; MCP_PUBLIC_URL selects OAuth-enabled FastMCP construction, not a different tool inventory. HTTP mode requires Google web OAuth credentials; stdio entrypoint requires refresh-token credentials. A property_id or GOOGLE_ANALYTICS_PROPERTY_ID is required at call time.
- Schemas reconstructed from AST annotations and Pydantic Field declarations; nested required params object retained, enums expanded, no upstream code executed.
- pyproject.toml wheel packages selects only src while console script points to main:main; standalone wheel installation may omit root main.py. Source execution and Docker invoke the existing main.py directly.
- Async tool functions invoke synchronous httpx reporting calls. Shared client retries once after a 401 by clearing cached access token; in HTTP injected-token mode this leaves no refresh credentials, causing a configuration error on retry.

</details>

## Tools

| Tool | Scope | Effect |
| --- | --- | --- |
| [`google_analytics_get_overview`](#google_analytics_get_overview) | GA4 | read |
| [`google_analytics_get_traffic_sources`](#google_analytics_get_traffic_sources) | GA4 | read |
| [`google_analytics_get_top_pages`](#google_analytics_get_top_pages) | GA4 | read |
| [`google_analytics_get_geographic_performance`](#google_analytics_get_geographic_performance) | GA4 | read |
| [`google_analytics_get_audience`](#google_analytics_get_audience) | GA4 | read |
| [`google_analytics_get_events`](#google_analytics_get_events) | GA4 | read |
| [`google_analytics_get_conversions`](#google_analytics_get_conversions) | GA4 | read |
| [`google_analytics_get_realtime`](#google_analytics_get_realtime) | GA4 | read |

## google_analytics_get_overview

Calls runReport for sessions, activeUsers, newUsers, screenPageViews, bounceRate, averageSessionDuration, engagementRate and conversions. Optionally adds the immediately preceding equal-length date range and dateRange dimension; returns numeric current/previous metrics and periods. Markdown computes percentage deltas; JSON returns raw structured comparison data. Uses the per-call property_id or environment default, resolves presets when applicable, and returns formatted Markdown or JSON text. Configuration/API/timeouts/unexpected errors are caught and returned as strings.

<details>
<summary>Full registered description</summary>

```text
Returns the main KPIs of the GA4 property for the selected period.

Metrics: sessions, active users, new users, pageviews, bounce rate,
average session duration, engagement rate and conversions.
With compare_previous=True, includes a percentage comparison against
the previous period.

Args:
    params (OverviewInput): property_id, period, compare_previous, format.

Returns:
    str: KPIs as markdown (default) or structured JSON.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `params` | Yes | object | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "params": {
      "type": "object",
      "properties": {
        "property_id": {
          "anyOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "title": "Property Id",
          "default": null,
          "description": "Numeric GA4 property ID (e.g. 123456789). If omitted, uses GOOGLE_ANALYTICS_PROPERTY_ID from the environment."
        },
        "date_range": {
          "type": "string",
          "enum": [
            "last_7_days",
            "last_14_days",
            "last_30_days",
            "this_month",
            "last_month",
            "custom"
          ],
          "title": "Date Range",
          "default": "last_7_days",
          "description": "Period: last_7_days (default), last_14_days, last_30_days, this_month, last_month or custom."
        },
        "start_date": {
          "anyOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "title": "Start Date",
          "default": null,
          "description": "Start date for date_range='custom'. Format: YYYY-MM-DD.",
          "pattern": "^\\d{4}-\\d{2}-\\d{2}$"
        },
        "end_date": {
          "anyOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "title": "End Date",
          "default": null,
          "description": "End date for date_range='custom'. Format: YYYY-MM-DD.",
          "pattern": "^\\d{4}-\\d{2}-\\d{2}$"
        },
        "compare_previous": {
          "type": "boolean",
          "title": "Compare Previous",
          "default": false,
          "description": "If True, includes a comparison against the previous same-sized period."
        },
        "response_format": {
          "type": "string",
          "enum": [
            "markdown",
            "json"
          ],
          "title": "Response Format",
          "default": "markdown",
          "description": "'markdown' for human reading (default) or 'json' for structured data."
        }
      },
      "required": [],
      "additionalProperties": false,
      "title": "OverviewInput"
    }
  },
  "required": [
    "params"
  ]
}
```

</details>

- Input model strips surrounding whitespace from strings and rejects extra model fields.
- date_range='custom' requires both dates at handler time; schema permits either to be null/omitted. Date strings have a shape regex, without calendar-validity or chronological-order validation.

Source: [src/server.py:397](https://github.com/minholi/google-analytics-mcp/blob/21a816a16df6cb5d45783c1479ea72b585ab849b/src/server.py#L397-L434) · [src/server.py:237](https://github.com/minholi/google-analytics-mcp/blob/21a816a16df6cb5d45783c1479ea72b585ab849b/src/server.py#L237-L271) · [src/server.py:110](https://github.com/minholi/google-analytics-mcp/blob/21a816a16df6cb5d45783c1479ea72b585ab849b/src/server.py#L110-L139) · [src/client.py:113](https://github.com/minholi/google-analytics-mcp/blob/21a816a16df6cb5d45783c1479ea72b585ab849b/src/client.py#L113-L182) · [src/client.py:48](https://github.com/minholi/google-analytics-mcp/blob/21a816a16df6cb5d45783c1479ea72b585ab849b/src/client.py#L48-L83).

## google_analytics_get_traffic_sources

Calls runReport grouped by sessionDefaultChannelGroup, sessionSource/sessionMedium, or sessionDefaultChannelGroup/sessionCampaignName; reports sessions, activeUsers, newUsers, bounceRate, engagementRate and conversions, sorted descending by sessions with the requested limit. Uses the per-call property_id or environment default, resolves presets when applicable, and returns formatted Markdown or JSON text. Configuration/API/timeouts/unexpected errors are caught and returned as strings.

<details>
<summary>Full registered description</summary>

```text
Returns traffic acquisition grouped by channel, source/medium or campaign.

Per-source metrics: sessions, users, new users, bounce rate,
engagement rate and conversions.

Args:
    params (TrafficSourcesInput): property_id, period, group_by
        (channel/source_medium/campaign), limit and format.

Returns:
    str: Traffic sources table as markdown or JSON.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `params` | Yes | object | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "params": {
      "type": "object",
      "properties": {
        "property_id": {
          "anyOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "title": "Property Id",
          "default": null,
          "description": "Numeric GA4 property ID. If omitted, uses GOOGLE_ANALYTICS_PROPERTY_ID."
        },
        "date_range": {
          "type": "string",
          "enum": [
            "last_7_days",
            "last_14_days",
            "last_30_days",
            "this_month",
            "last_month",
            "custom"
          ],
          "title": "Date Range",
          "default": "last_7_days"
        },
        "start_date": {
          "anyOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "title": "Start Date",
          "default": null,
          "pattern": "^\\d{4}-\\d{2}-\\d{2}$"
        },
        "end_date": {
          "anyOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "title": "End Date",
          "default": null,
          "pattern": "^\\d{4}-\\d{2}-\\d{2}$"
        },
        "group_by": {
          "type": "string",
          "enum": [
            "channel",
            "source_medium",
            "campaign"
          ],
          "title": "Group By",
          "default": "channel",
          "description": "Grouping: 'channel' (default), 'source_medium' or 'campaign'."
        },
        "limit": {
          "type": "integer",
          "title": "Limit",
          "default": 25,
          "minimum": 1,
          "maximum": 100,
          "description": "Max rows to return (1–100)."
        },
        "response_format": {
          "type": "string",
          "enum": [
            "markdown",
            "json"
          ],
          "title": "Response Format",
          "default": "markdown"
        }
      },
      "required": [],
      "additionalProperties": false,
      "title": "TrafficSourcesInput"
    }
  },
  "required": [
    "params"
  ]
}
```

</details>

- Input model strips surrounding whitespace from strings and rejects extra model fields.
- date_range='custom' requires both dates at handler time; schema permits either to be null/omitted. Date strings have a shape regex, without calendar-validity or chronological-order validation.

Source: [src/server.py:437](https://github.com/minholi/google-analytics-mcp/blob/21a816a16df6cb5d45783c1479ea72b585ab849b/src/server.py#L437-L474) · [src/server.py:274](https://github.com/minholi/google-analytics-mcp/blob/21a816a16df6cb5d45783c1479ea72b585ab849b/src/server.py#L274-L289) · [src/server.py:110](https://github.com/minholi/google-analytics-mcp/blob/21a816a16df6cb5d45783c1479ea72b585ab849b/src/server.py#L110-L139) · [src/client.py:184](https://github.com/minholi/google-analytics-mcp/blob/21a816a16df6cb5d45783c1479ea72b585ab849b/src/client.py#L184-L246) · [src/client.py:48](https://github.com/minholi/google-analytics-mcp/blob/21a816a16df6cb5d45783c1479ea72b585ab849b/src/client.py#L48-L83).

## google_analytics_get_top_pages

Calls runReport grouped by pagePath and pageTitle for screenPageViews, sessions, activeUsers, averageSessionDuration, bounceRate and engagementRate; sorts descending by screenPageViews and optionally applies a pagePath BEGINS_WITH string filter. Uses the per-call property_id or environment default, resolves presets when applicable, and returns formatted Markdown or JSON text. Configuration/API/timeouts/unexpected errors are caught and returned as strings.

<details>
<summary>Full registered description</summary>

```text
Lists the most visited pages with engagement metrics.

Returns pageviews, sessions, active users, bounce rate and average
session duration per page. Supports filtering by path prefix.

Args:
    params (TopPagesInput): property_id, period, limit, page_path_filter and format.

Returns:
    str: Pages ordered by pageviews as markdown or JSON.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `params` | Yes | object | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "params": {
      "type": "object",
      "properties": {
        "property_id": {
          "anyOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "title": "Property Id",
          "default": null,
          "description": "Numeric GA4 property ID. If omitted, uses GOOGLE_ANALYTICS_PROPERTY_ID."
        },
        "date_range": {
          "type": "string",
          "enum": [
            "last_7_days",
            "last_14_days",
            "last_30_days",
            "this_month",
            "last_month",
            "custom"
          ],
          "title": "Date Range",
          "default": "last_7_days"
        },
        "start_date": {
          "anyOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "title": "Start Date",
          "default": null,
          "pattern": "^\\d{4}-\\d{2}-\\d{2}$"
        },
        "end_date": {
          "anyOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "title": "End Date",
          "default": null,
          "pattern": "^\\d{4}-\\d{2}-\\d{2}$"
        },
        "limit": {
          "type": "integer",
          "title": "Limit",
          "default": 25,
          "minimum": 1,
          "maximum": 100
        },
        "page_path_filter": {
          "anyOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "title": "Page Path Filter",
          "default": null,
          "description": "Filter pages whose path starts with this prefix (e.g. '/blog', '/products')."
        },
        "response_format": {
          "type": "string",
          "enum": [
            "markdown",
            "json"
          ],
          "title": "Response Format",
          "default": "markdown"
        }
      },
      "required": [],
      "additionalProperties": false,
      "title": "TopPagesInput"
    }
  },
  "required": [
    "params"
  ]
}
```

</details>

- Input model strips surrounding whitespace from strings and rejects extra model fields.
- date_range='custom' requires both dates at handler time; schema permits either to be null/omitted. Date strings have a shape regex, without calendar-validity or chronological-order validation.

Source: [src/server.py:477](https://github.com/minholi/google-analytics-mcp/blob/21a816a16df6cb5d45783c1479ea72b585ab849b/src/server.py#L477-L513) · [src/server.py:292](https://github.com/minholi/google-analytics-mcp/blob/21a816a16df6cb5d45783c1479ea72b585ab849b/src/server.py#L292-L309) · [src/server.py:110](https://github.com/minholi/google-analytics-mcp/blob/21a816a16df6cb5d45783c1479ea72b585ab849b/src/server.py#L110-L139) · [src/client.py:248](https://github.com/minholi/google-analytics-mcp/blob/21a816a16df6cb5d45783c1479ea72b585ab849b/src/client.py#L248-L308) · [src/client.py:48](https://github.com/minholi/google-analytics-mcp/blob/21a816a16df6cb5d45783c1479ea72b585ab849b/src/client.py#L48-L83).

## google_analytics_get_geographic_performance

Calls runReport grouped by country, region or city for sessions, activeUsers, newUsers, conversions and bounceRate, sorted descending by sessions. Markdown additionally highlights most conversions and most sessions with zero conversions among returned locations. Uses the per-call property_id or environment default, resolves presets when applicable, and returns formatted Markdown or JSON text. Configuration/API/timeouts/unexpected errors are caught and returned as strings.

<details>
<summary>Full registered description</summary>

```text
Returns performance by geographic location (country, region or city).

Metrics: sessions, active users, new users, conversions and bounce rate.
Highlights the location with the most conversions and the one with
the most sessions without conversions.

Args:
    params (GeographicPerformanceInput): property_id, period, granularity
        (country/region/city), limit and format.

Returns:
    str: Geographic table with metrics and highlights as markdown or JSON.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `params` | Yes | object | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "params": {
      "type": "object",
      "properties": {
        "property_id": {
          "anyOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "title": "Property Id",
          "default": null,
          "description": "Numeric GA4 property ID. If omitted, uses GOOGLE_ANALYTICS_PROPERTY_ID."
        },
        "date_range": {
          "type": "string",
          "enum": [
            "last_7_days",
            "last_14_days",
            "last_30_days",
            "this_month",
            "last_month",
            "custom"
          ],
          "title": "Date Range",
          "default": "last_30_days"
        },
        "start_date": {
          "anyOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "title": "Start Date",
          "default": null,
          "pattern": "^\\d{4}-\\d{2}-\\d{2}$"
        },
        "end_date": {
          "anyOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "title": "End Date",
          "default": null,
          "pattern": "^\\d{4}-\\d{2}-\\d{2}$"
        },
        "granularity": {
          "type": "string",
          "enum": [
            "country",
            "region",
            "city"
          ],
          "title": "Granularity",
          "default": "country",
          "description": "Geographic level: 'country' (default), 'region' or 'city'."
        },
        "limit": {
          "type": "integer",
          "title": "Limit",
          "default": 25,
          "minimum": 1,
          "maximum": 100
        },
        "response_format": {
          "type": "string",
          "enum": [
            "markdown",
            "json"
          ],
          "title": "Response Format",
          "default": "markdown"
        }
      },
      "required": [],
      "additionalProperties": false,
      "title": "GeographicPerformanceInput"
    }
  },
  "required": [
    "params"
  ]
}
```

</details>

- Input model strips surrounding whitespace from strings and rejects extra model fields.
- date_range='custom' requires both dates at handler time; schema permits either to be null/omitted. Date strings have a shape regex, without calendar-validity or chronological-order validation.

Source: [src/server.py:516](https://github.com/minholi/google-analytics-mcp/blob/21a816a16df6cb5d45783c1479ea72b585ab849b/src/server.py#L516-L556) · [src/server.py:312](https://github.com/minholi/google-analytics-mcp/blob/21a816a16df6cb5d45783c1479ea72b585ab849b/src/server.py#L312-L327) · [src/server.py:110](https://github.com/minholi/google-analytics-mcp/blob/21a816a16df6cb5d45783c1479ea72b585ab849b/src/server.py#L110-L139) · [src/client.py:310](https://github.com/minholi/google-analytics-mcp/blob/21a816a16df6cb5d45783c1479ea72b585ab849b/src/client.py#L310-L350) · [src/client.py:48](https://github.com/minholi/google-analytics-mcp/blob/21a816a16df6cb5d45783c1479ea72b585ab849b/src/client.py#L48-L83).

## google_analytics_get_audience

Calls runReport grouped by deviceCategory, browser or operatingSystem for sessions, activeUsers, screenPageViews, bounceRate and engagementRate, sorted descending by sessions. Uses the per-call property_id or environment default, resolves presets when applicable, and returns formatted Markdown or JSON text. Configuration/API/timeouts/unexpected errors are caught and returned as strings.

<details>
<summary>Full registered description</summary>

```text
Returns audience breakdown by device, browser or operating system.

Metrics: sessions, active users, pageviews, bounce rate and engagement.

Args:
    params (AudienceInput): property_id, period, breakdown
        (deviceCategory/browser/operatingSystem), limit and format.

Returns:
    str: Audience table as markdown or JSON.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `params` | Yes | object | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "params": {
      "type": "object",
      "properties": {
        "property_id": {
          "anyOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "title": "Property Id",
          "default": null,
          "description": "Numeric GA4 property ID. If omitted, uses GOOGLE_ANALYTICS_PROPERTY_ID."
        },
        "date_range": {
          "type": "string",
          "enum": [
            "last_7_days",
            "last_14_days",
            "last_30_days",
            "this_month",
            "last_month",
            "custom"
          ],
          "title": "Date Range",
          "default": "last_7_days"
        },
        "start_date": {
          "anyOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "title": "Start Date",
          "default": null,
          "pattern": "^\\d{4}-\\d{2}-\\d{2}$"
        },
        "end_date": {
          "anyOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "title": "End Date",
          "default": null,
          "pattern": "^\\d{4}-\\d{2}-\\d{2}$"
        },
        "breakdown": {
          "type": "string",
          "enum": [
            "deviceCategory",
            "browser",
            "operatingSystem"
          ],
          "title": "Breakdown",
          "default": "deviceCategory",
          "description": "Dimension: 'deviceCategory' (default), 'browser' or 'operatingSystem'."
        },
        "limit": {
          "type": "integer",
          "title": "Limit",
          "default": 25,
          "minimum": 1,
          "maximum": 100
        },
        "response_format": {
          "type": "string",
          "enum": [
            "markdown",
            "json"
          ],
          "title": "Response Format",
          "default": "markdown"
        }
      },
      "required": [],
      "additionalProperties": false,
      "title": "AudienceInput"
    }
  },
  "required": [
    "params"
  ]
}
```

</details>

- Input model strips surrounding whitespace from strings and rejects extra model fields.
- date_range='custom' requires both dates at handler time; schema permits either to be null/omitted. Date strings have a shape regex, without calendar-validity or chronological-order validation.

Source: [src/server.py:559](https://github.com/minholi/google-analytics-mcp/blob/21a816a16df6cb5d45783c1479ea72b585ab849b/src/server.py#L559-L595) · [src/server.py:330](https://github.com/minholi/google-analytics-mcp/blob/21a816a16df6cb5d45783c1479ea72b585ab849b/src/server.py#L330-L345) · [src/server.py:110](https://github.com/minholi/google-analytics-mcp/blob/21a816a16df6cb5d45783c1479ea72b585ab849b/src/server.py#L110-L139) · [src/client.py:352](https://github.com/minholi/google-analytics-mcp/blob/21a816a16df6cb5d45783c1479ea72b585ab849b/src/client.py#L352-L392) · [src/client.py:48](https://github.com/minholi/google-analytics-mcp/blob/21a816a16df6cb5d45783c1479ea72b585ab849b/src/client.py#L48-L83).

## google_analytics_get_events

Calls runReport grouped by eventName for eventCount, eventCountPerUser and totalUsers, sorted descending by eventCount. A nonempty event_names list adds an eventName inListFilter. Uses the per-call property_id or environment default, resolves presets when applicable, and returns formatted Markdown or JSON text. Configuration/API/timeouts/unexpected errors are caught and returned as strings.

<details>
<summary>Full registered description</summary>

```text
Lists the most-triggered events on the GA4 property.

Returns event name, total count, count per user and total users.
With event_names, filters to only the specified events.

Args:
    params (EventsInput): property_id, period, event_names (optional filter),
        limit and format.

Returns:
    str: Events ordered by count as markdown or JSON.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `params` | Yes | object | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "params": {
      "type": "object",
      "properties": {
        "property_id": {
          "anyOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "title": "Property Id",
          "default": null,
          "description": "Numeric GA4 property ID. If omitted, uses GOOGLE_ANALYTICS_PROPERTY_ID."
        },
        "date_range": {
          "type": "string",
          "enum": [
            "last_7_days",
            "last_14_days",
            "last_30_days",
            "this_month",
            "last_month",
            "custom"
          ],
          "title": "Date Range",
          "default": "last_7_days"
        },
        "start_date": {
          "anyOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "title": "Start Date",
          "default": null,
          "pattern": "^\\d{4}-\\d{2}-\\d{2}$"
        },
        "end_date": {
          "anyOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "title": "End Date",
          "default": null,
          "pattern": "^\\d{4}-\\d{2}-\\d{2}$"
        },
        "event_names": {
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
          "title": "Event Names",
          "default": null,
          "description": "Filter only these events (e.g. ['purchase', 'sign_up']). If None, returns all."
        },
        "limit": {
          "type": "integer",
          "title": "Limit",
          "default": 50,
          "minimum": 1,
          "maximum": 200
        },
        "response_format": {
          "type": "string",
          "enum": [
            "markdown",
            "json"
          ],
          "title": "Response Format",
          "default": "markdown"
        }
      },
      "required": [],
      "additionalProperties": false,
      "title": "EventsInput"
    }
  },
  "required": [
    "params"
  ]
}
```

</details>

- Input model strips surrounding whitespace from strings and rejects extra model fields.
- date_range='custom' requires both dates at handler time; schema permits either to be null/omitted. Date strings have a shape regex, without calendar-validity or chronological-order validation.
- An empty event_names list applies no filter.

Source: [src/server.py:598](https://github.com/minholi/google-analytics-mcp/blob/21a816a16df6cb5d45783c1479ea72b585ab849b/src/server.py#L598-L635) · [src/server.py:348](https://github.com/minholi/google-analytics-mcp/blob/21a816a16df6cb5d45783c1479ea72b585ab849b/src/server.py#L348-L365) · [src/server.py:110](https://github.com/minholi/google-analytics-mcp/blob/21a816a16df6cb5d45783c1479ea72b585ab849b/src/server.py#L110-L139) · [src/client.py:394](https://github.com/minholi/google-analytics-mcp/blob/21a816a16df6cb5d45783c1479ea72b585ab849b/src/client.py#L394-L440) · [src/client.py:48](https://github.com/minholi/google-analytics-mcp/blob/21a816a16df6cb5d45783c1479ea72b585ab849b/src/client.py#L48-L83).

## google_analytics_get_conversions

Calls runReport grouped by sessionDefaultChannelGroup and eventName for conversions, totalRevenue and sessions; filters conversions GREATER_THAN 0 and sorts descending by conversions. Returns rows and locally summed conversion/revenue totals. Uses the per-call property_id or environment default, resolves presets when applicable, and returns formatted Markdown or JSON text. Configuration/API/timeouts/unexpected errors are caught and returned as strings.

<details>
<summary>Full registered description</summary>

```text
Returns conversion and revenue data by channel and conversion event.

Only events flagged as conversions in GA4 appear here.
Includes conversion and revenue totals.

Args:
    params (ConversionsInput): property_id, period, limit and format.

Returns:
    str: Conversions table with revenue as markdown or JSON.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `params` | Yes | object | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "params": {
      "type": "object",
      "properties": {
        "property_id": {
          "anyOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "title": "Property Id",
          "default": null,
          "description": "Numeric GA4 property ID. If omitted, uses GOOGLE_ANALYTICS_PROPERTY_ID."
        },
        "date_range": {
          "type": "string",
          "enum": [
            "last_7_days",
            "last_14_days",
            "last_30_days",
            "this_month",
            "last_month",
            "custom"
          ],
          "title": "Date Range",
          "default": "last_30_days"
        },
        "start_date": {
          "anyOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "title": "Start Date",
          "default": null,
          "pattern": "^\\d{4}-\\d{2}-\\d{2}$"
        },
        "end_date": {
          "anyOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "title": "End Date",
          "default": null,
          "pattern": "^\\d{4}-\\d{2}-\\d{2}$"
        },
        "limit": {
          "type": "integer",
          "title": "Limit",
          "default": 50,
          "minimum": 1,
          "maximum": 200
        },
        "response_format": {
          "type": "string",
          "enum": [
            "markdown",
            "json"
          ],
          "title": "Response Format",
          "default": "markdown"
        }
      },
      "required": [],
      "additionalProperties": false,
      "title": "ConversionsInput"
    }
  },
  "required": [
    "params"
  ]
}
```

</details>

- Input model strips surrounding whitespace from strings and rejects extra model fields.
- date_range='custom' requires both dates at handler time; schema permits either to be null/omitted. Date strings have a shape regex, without calendar-validity or chronological-order validation.
- Totals are sums over returned limited rows, not independent property-wide aggregate totals.

Source: [src/server.py:638](https://github.com/minholi/google-analytics-mcp/blob/21a816a16df6cb5d45783c1479ea72b585ab849b/src/server.py#L638-L673) · [src/server.py:368](https://github.com/minholi/google-analytics-mcp/blob/21a816a16df6cb5d45783c1479ea72b585ab849b/src/server.py#L368-L379) · [src/server.py:110](https://github.com/minholi/google-analytics-mcp/blob/21a816a16df6cb5d45783c1479ea72b585ab849b/src/server.py#L110-L139) · [src/client.py:442](https://github.com/minholi/google-analytics-mcp/blob/21a816a16df6cb5d45783c1479ea72b585ab849b/src/client.py#L442-L494) · [src/client.py:48](https://github.com/minholi/google-analytics-mcp/blob/21a816a16df6cb5d45783c1479ea72b585ab849b/src/client.py#L48-L83).

## google_analytics_get_realtime

Makes five sequential runRealtimeReport requests for activeUsers: total, unifiedPagePathScreen, firstUserSource, country and deviceCategory. Each breakdown is sorted descending by activeUsers and limited to 10 rows. Returns numeric total and breakdown lists. Uses the per-call property_id or environment default, resolves presets when applicable, and returns formatted Markdown or JSON text. Configuration/API/timeouts/unexpected errors are caught and returned as strings.

<details>
<summary>Full registered description</summary>

```text
Returns realtime data on currently active users (last 30 minutes).

Shows total active users and breakdowns by page, source, country
and device. Does not accept a date_range — always reflects the current state.

Args:
    params (RealtimeInput): property_id and format.

Returns:
    str: Active users and breakdowns as markdown or JSON.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `params` | Yes | object | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "params": {
      "type": "object",
      "properties": {
        "property_id": {
          "anyOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "title": "Property Id",
          "default": null,
          "description": "Numeric GA4 property ID. If omitted, uses GOOGLE_ANALYTICS_PROPERTY_ID."
        },
        "response_format": {
          "type": "string",
          "enum": [
            "markdown",
            "json"
          ],
          "title": "Response Format",
          "default": "markdown"
        }
      },
      "required": [],
      "additionalProperties": false,
      "title": "RealtimeInput"
    }
  },
  "required": [
    "params"
  ]
}
```

</details>

- Input model strips surrounding whitespace from strings and rejects extra model fields.
- All five requests must succeed; a failure discards earlier data and returns the shared error string. The source forwards unifiedPagePathScreen and firstUserSource to the realtime API without compatibility checks.

Source: [src/server.py:676](https://github.com/minholi/google-analytics-mcp/blob/21a816a16df6cb5d45783c1479ea72b585ab849b/src/server.py#L676-L706) · [src/server.py:382](https://github.com/minholi/google-analytics-mcp/blob/21a816a16df6cb5d45783c1479ea72b585ab849b/src/server.py#L382-L389) · [src/server.py:110](https://github.com/minholi/google-analytics-mcp/blob/21a816a16df6cb5d45783c1479ea72b585ab849b/src/server.py#L110-L139) · [src/client.py:496](https://github.com/minholi/google-analytics-mcp/blob/21a816a16df6cb5d45783c1479ea72b585ab849b/src/client.py#L496-L583) · [src/client.py:48](https://github.com/minholi/google-analytics-mcp/blob/21a816a16df6cb5d45783c1479ea72b585ab849b/src/client.py#L48-L83).

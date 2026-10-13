# gviollaz/iita-ga4-mcp

[Catalog](../../README.md) · [All tool names](../tool-index.md) · [Upstream](https://github.com/gviollaz/iita-ga4-mcp) · [JSON](../../data/mcps/gviollaz--iita-ga4-mcp.json)

**7 tools:** 7 GA4, 0 other-service or server-support tools. Reviewed source: [`9d5fae652689`](https://github.com/gviollaz/iita-ga4-mcp/tree/9d5fae652689754a8e8aa64039f7d887c1018fd6).

Descriptions and parameter schemas come from the registered source definitions. Generated schemas are reconstructed from annotations or validators; live `tools/list` and authenticated API calls were not run. Loose objects remain loose.

<details>
<summary>Exposure and compatibility notes</summary>

- Source review only; no tools/list, upstream execution or live requests. HEAD checked against assigned revision. All seven registrations are unconditional; no imported tool modules, alternate names, configurable permission tiers or additional support tools. HTTP health/OAuth endpoints are not MCP tools.
- MCP authentication (server.py/oauth.py): MCP_AUTH_TOKEN is required at startup. MCP_OAUTH_ENABLED defaults true and accepts locally signed HS256 JWT Bearer tokens, with signing key derived from MCP_AUTH_TOKEN; OAuth discovery, registration, authorization-code/PKCE and token endpoints are public. authorize auto-consents without user login or checking the shared secret, so a client can obtain a token through public endpoints; this is distinct from Google OAuth. Disabled OAuth uses shared MCP_AUTH_TOKEN as Bearer token or /mcp/{token} URL token. OAuth token handler uses request.form(), but requirements.txt does not declare python-multipart; token exchange can fail with invalid_request when no form parser dependency is installed.
- GA4 API authentication (main.py:25-38): GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET and GOOGLE_REFRESH_TOKEN construct google.oauth2.credentials.Credentials using <https://oauth2.googleapis.com/token> for refresh. GA4_PROPERTY_ID is fallback property; each tool can override it. No GA OAuth setup tool, service-account path, per-MCP-user credentials or Admin API implementation exists. Missing Google credentials are not proactively validated.
- Production entrypoints Dockerfile and Procfile run server.py; asgi.py exports server.app. Legacy start.py refers to undefined mcp and fails if used directly, but is not the configured deployment entrypoint. requirements.txt pins mcp[cli]>=1.9.0,<2.0.0 and pydantic>=2.0; schemas are source-derived, not captured from any resolved runtime.
- DNS rebinding protection is configured via main.py transport settings and MCP_ALLOWED_HOSTS/RAILWAY host settings; it does not affect tool inventory.

</details>

## Tools

| Tool | Scope | Effect |
| --- | --- | --- |
| [`ga4_run_report`](#ga4_run_report) | GA4 | read |
| [`ga4_realtime_report`](#ga4_realtime_report) | GA4 | read |
| [`ga4_traffic_sources`](#ga4_traffic_sources) | GA4 | read |
| [`ga4_top_pages`](#ga4_top_pages) | GA4 | read |
| [`ga4_daily_trend`](#ga4_daily_trend) | GA4 | read |
| [`ga4_landing_pages`](#ga4_landing_pages) | GA4 | read |
| [`ga4_device_geo`](#ga4_device_geo) | GA4 | read |

## ga4_run_report

Runs a custom Data API report for caller property_id or GA4_PROPERTY_ID, using supplied dimensions/metrics and resolved dates, limit and descending metric order. Applies a case-insensitive CONTAINS dimension filter only if both filter name and value are truthy. Formats rows as Markdown.

<details>
<summary>Full registered description</summary>

```text
Run a GA4 report with custom dimensions, metrics, date range, and filters.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `params` | Yes | RunReportInput | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "title": "ga4_run_reportArguments",
  "properties": {
    "params": {
      "$ref": "#/$defs/RunReportInput"
    }
  },
  "required": [
    "params"
  ],
  "$defs": {
    "RunReportInput": {
      "type": "object",
      "title": "RunReportInput",
      "properties": {
        "dimensions": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "title": "Dimensions",
          "default": [
            "pagePath"
          ],
          "description": "GA4 dimensions: pagePath, pageTitle, sessionSource, sessionMedium, country, city, deviceCategory, date, hour, landingPage, sessionDefaultChannelGroup"
        },
        "metrics": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "title": "Metrics",
          "default": [
            "screenPageViews",
            "sessions",
            "totalUsers"
          ],
          "description": "GA4 metrics: screenPageViews, sessions, totalUsers, newUsers, bounceRate, averageSessionDuration, engagedSessions, conversions, eventCount"
        },
        "date_range": {
          "type": "string",
          "title": "Date Range",
          "default": "LAST_28_DAYS"
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
          "default": null
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
          "default": null
        },
        "limit": {
          "type": "integer",
          "title": "Limit",
          "default": 25,
          "minimum": 1,
          "maximum": 1000
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
        "dimension_filter_name": {
          "anyOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "title": "Dimension Filter Name",
          "default": null
        },
        "dimension_filter_value": {
          "anyOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "title": "Dimension Filter Value",
          "default": null
        },
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
          "default": null
        }
      },
      "additionalProperties": false
    }
  }
}
```

</details>

- The single params argument is required; all nested model fields have defaults. Nested model forbids extra fields; no aliases or custom validators are defined.
- date_range is an unrestricted string, not an enum. Handler recognizes TODAY, YESTERDAY, LAST_7_DAYS, LAST_14_DAYS, LAST_28_DAYS, LAST_30_DAYS, LAST_90_DAYS and THIS_MONTH; unknown strings fall back to last 28 days. Explicit dates override only when both are truthy. Dates have no exposed format validation; N-day presets include today and today minus N days.
- Returns an error string when neither property_id nor GA4_PROPERTY_ID is set.
- metrics permits an empty array, but when order_by_metric is absent the handler indexes metrics[0] and can fail. Dimensions/metric names are free strings, not constrained to the descriptive examples.
- Synchronous Google client call inside async handler; API errors are not caught locally.

Source: [main.py:101](https://github.com/gviollaz/iita-ga4-mcp/blob/9d5fae652689754a8e8aa64039f7d887c1018fd6/main.py#L101-L112) · [main.py:114](https://github.com/gviollaz/iita-ga4-mcp/blob/9d5fae652689754a8e8aa64039f7d887c1018fd6/main.py#L114-L127) · [main.py:35](https://github.com/gviollaz/iita-ga4-mcp/blob/9d5fae652689754a8e8aa64039f7d887c1018fd6/main.py#L35-L60).

## ga4_realtime_report

Runs a realtime Data API report for caller property_id or GA4_PROPERTY_ID, using supplied dimensions, metrics and limit; formats rows as Markdown.

<details>
<summary>Full registered description</summary>

```text
Get real-time GA4 data showing active users and pages right now.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `params` | Yes | RealtimeReportInput | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "title": "ga4_realtime_reportArguments",
  "properties": {
    "params": {
      "$ref": "#/$defs/RealtimeReportInput"
    }
  },
  "required": [
    "params"
  ],
  "$defs": {
    "RealtimeReportInput": {
      "type": "object",
      "title": "RealtimeReportInput",
      "properties": {
        "dimensions": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "title": "Dimensions",
          "default": [
            "unifiedScreenName"
          ]
        },
        "metrics": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "title": "Metrics",
          "default": [
            "activeUsers"
          ]
        },
        "limit": {
          "type": "integer",
          "title": "Limit",
          "default": 20,
          "minimum": 1,
          "maximum": 100
        },
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
          "default": null
        }
      },
      "additionalProperties": false
    }
  }
}
```

</details>

- The single params argument is required; all nested model fields have defaults. Nested model forbids extra fields; no aliases or custom validators are defined.
- Returns an error string when neither property_id nor GA4_PROPERTY_ID is set.
- Synchronous Google client call inside async handler; API errors are not caught locally.

Source: [main.py:129](https://github.com/gviollaz/iita-ga4-mcp/blob/9d5fae652689754a8e8aa64039f7d887c1018fd6/main.py#L129-L134) · [main.py:136](https://github.com/gviollaz/iita-ga4-mcp/blob/9d5fae652689754a8e8aa64039f7d887c1018fd6/main.py#L136-L143) · [main.py:35](https://github.com/gviollaz/iita-ga4-mcp/blob/9d5fae652689754a8e8aa64039f7d887c1018fd6/main.py#L35-L60).

## ga4_traffic_sources

Runs a Data API report with sessionDefaultChannelGroup, sessionSource and sessionMedium dimensions; sessions, totalUsers, newUsers and bounceRate metrics; resolved dates and caller limit; orders by sessions descending and formats Markdown.

<details>
<summary>Full registered description</summary>

```text
Get traffic sources: channels, sources, mediums with session/user counts.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `params` | Yes | TrafficSourcesInput | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "title": "ga4_traffic_sourcesArguments",
  "properties": {
    "params": {
      "$ref": "#/$defs/TrafficSourcesInput"
    }
  },
  "required": [
    "params"
  ],
  "$defs": {
    "TrafficSourcesInput": {
      "type": "object",
      "title": "TrafficSourcesInput",
      "properties": {
        "date_range": {
          "type": "string",
          "title": "Date Range",
          "default": "LAST_28_DAYS"
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
          "default": null
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
          "default": null
        },
        "limit": {
          "type": "integer",
          "title": "Limit",
          "default": 20,
          "minimum": 1,
          "maximum": 100
        },
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
          "default": null
        }
      },
      "additionalProperties": false
    }
  }
}
```

</details>

- The single params argument is required; all nested model fields have defaults. Nested model forbids extra fields; no aliases or custom validators are defined.
- date_range is an unrestricted string, not an enum. Handler recognizes TODAY, YESTERDAY, LAST_7_DAYS, LAST_14_DAYS, LAST_28_DAYS, LAST_30_DAYS, LAST_90_DAYS and THIS_MONTH; unknown strings fall back to last 28 days. Explicit dates override only when both are truthy. Dates have no exposed format validation; N-day presets include today and today minus N days.
- Does not guard against missing property_id/GA4_PROPERTY_ID and can submit properties/ to the API.
- Synchronous Google client call inside async handler; API errors are not caught locally.

Source: [main.py:145](https://github.com/gviollaz/iita-ga4-mcp/blob/9d5fae652689754a8e8aa64039f7d887c1018fd6/main.py#L145-L151) · [main.py:153](https://github.com/gviollaz/iita-ga4-mcp/blob/9d5fae652689754a8e8aa64039f7d887c1018fd6/main.py#L153-L163) · [main.py:35](https://github.com/gviollaz/iita-ga4-mcp/blob/9d5fae652689754a8e8aa64039f7d887c1018fd6/main.py#L35-L60).

## ga4_top_pages

Runs a Data API report with pagePath/pageTitle and screenPageViews, sessions, totalUsers, averageSessionDuration and bounceRate; resolved dates and caller limit; orders by screenPageViews descending. Optional path_contains adds case-insensitive CONTAINS pagePath filter; formats Markdown.

<details>
<summary>Full registered description</summary>

```text
Get top pages by views with engagement metrics.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `params` | Yes | TopPagesInput | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "title": "ga4_top_pagesArguments",
  "properties": {
    "params": {
      "$ref": "#/$defs/TopPagesInput"
    }
  },
  "required": [
    "params"
  ],
  "$defs": {
    "TopPagesInput": {
      "type": "object",
      "title": "TopPagesInput",
      "properties": {
        "date_range": {
          "type": "string",
          "title": "Date Range",
          "default": "LAST_28_DAYS"
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
          "default": null
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
          "default": null
        },
        "limit": {
          "type": "integer",
          "title": "Limit",
          "default": 20,
          "minimum": 1,
          "maximum": 100
        },
        "path_contains": {
          "anyOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "title": "Path Contains",
          "default": null
        },
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
          "default": null
        }
      },
      "additionalProperties": false
    }
  }
}
```

</details>

- The single params argument is required; all nested model fields have defaults. Nested model forbids extra fields; no aliases or custom validators are defined.
- date_range is an unrestricted string, not an enum. Handler recognizes TODAY, YESTERDAY, LAST_7_DAYS, LAST_14_DAYS, LAST_28_DAYS, LAST_30_DAYS, LAST_90_DAYS and THIS_MONTH; unknown strings fall back to last 28 days. Explicit dates override only when both are truthy. Dates have no exposed format validation; N-day presets include today and today minus N days.
- Does not guard against missing property_id/GA4_PROPERTY_ID and can submit properties/ to the API.
- Synchronous Google client call inside async handler; API errors are not caught locally.

Source: [main.py:165](https://github.com/gviollaz/iita-ga4-mcp/blob/9d5fae652689754a8e8aa64039f7d887c1018fd6/main.py#L165-L172) · [main.py:174](https://github.com/gviollaz/iita-ga4-mcp/blob/9d5fae652689754a8e8aa64039f7d887c1018fd6/main.py#L174-L187) · [main.py:35](https://github.com/gviollaz/iita-ga4-mcp/blob/9d5fae652689754a8e8aa64039f7d887c1018fd6/main.py#L35-L60).

## ga4_daily_trend

Runs a Data API report with date dimension and supplied metrics for resolved dates, fixed limit 366 and date ascending order; formats Markdown.

<details>
<summary>Full registered description</summary>

```text
Get daily trend of sessions, users, and pageviews.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `params` | Yes | DailyTrendInput | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "title": "ga4_daily_trendArguments",
  "properties": {
    "params": {
      "$ref": "#/$defs/DailyTrendInput"
    }
  },
  "required": [
    "params"
  ],
  "$defs": {
    "DailyTrendInput": {
      "type": "object",
      "title": "DailyTrendInput",
      "properties": {
        "metrics": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "title": "Metrics",
          "default": [
            "sessions",
            "totalUsers",
            "screenPageViews"
          ]
        },
        "date_range": {
          "type": "string",
          "title": "Date Range",
          "default": "LAST_28_DAYS"
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
          "default": null
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
          "default": null
        },
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
          "default": null
        }
      },
      "additionalProperties": false
    }
  }
}
```

</details>

- The single params argument is required; all nested model fields have defaults. Nested model forbids extra fields; no aliases or custom validators are defined.
- date_range is an unrestricted string, not an enum. Handler recognizes TODAY, YESTERDAY, LAST_7_DAYS, LAST_14_DAYS, LAST_28_DAYS, LAST_30_DAYS, LAST_90_DAYS and THIS_MONTH; unknown strings fall back to last 28 days. Explicit dates override only when both are truthy. Dates have no exposed format validation; N-day presets include today and today minus N days.
- Does not guard against missing property_id/GA4_PROPERTY_ID and can submit properties/ to the API.
- Synchronous Google client call inside async handler; API errors are not caught locally.

Source: [main.py:189](https://github.com/gviollaz/iita-ga4-mcp/blob/9d5fae652689754a8e8aa64039f7d887c1018fd6/main.py#L189-L195) · [main.py:197](https://github.com/gviollaz/iita-ga4-mcp/blob/9d5fae652689754a8e8aa64039f7d887c1018fd6/main.py#L197-L205) · [main.py:35](https://github.com/gviollaz/iita-ga4-mcp/blob/9d5fae652689754a8e8aa64039f7d887c1018fd6/main.py#L35-L60).

## ga4_landing_pages

Runs a Data API report with landingPage dimension and sessions, totalUsers, newUsers, bounceRate, averageSessionDuration and conversions metrics; resolved dates and caller limit; orders by sessions descending; formats Markdown.

<details>
<summary>Full registered description</summary>

```text
Get landing page performance: first-touch pages with sessions, bounce rate, conversions.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `params` | Yes | LandingPagesInput | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "title": "ga4_landing_pagesArguments",
  "properties": {
    "params": {
      "$ref": "#/$defs/LandingPagesInput"
    }
  },
  "required": [
    "params"
  ],
  "$defs": {
    "LandingPagesInput": {
      "type": "object",
      "title": "LandingPagesInput",
      "properties": {
        "date_range": {
          "type": "string",
          "title": "Date Range",
          "default": "LAST_28_DAYS"
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
          "default": null
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
          "default": null
        },
        "limit": {
          "type": "integer",
          "title": "Limit",
          "default": 20,
          "minimum": 1,
          "maximum": 100
        },
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
          "default": null
        }
      },
      "additionalProperties": false
    }
  }
}
```

</details>

- The single params argument is required; all nested model fields have defaults. Nested model forbids extra fields; no aliases or custom validators are defined.
- date_range is an unrestricted string, not an enum. Handler recognizes TODAY, YESTERDAY, LAST_7_DAYS, LAST_14_DAYS, LAST_28_DAYS, LAST_30_DAYS, LAST_90_DAYS and THIS_MONTH; unknown strings fall back to last 28 days. Explicit dates override only when both are truthy. Dates have no exposed format validation; N-day presets include today and today minus N days.
- Does not guard against missing property_id/GA4_PROPERTY_ID and can submit properties/ to the API.
- Synchronous Google client call inside async handler; API errors are not caught locally.

Source: [main.py:207](https://github.com/gviollaz/iita-ga4-mcp/blob/9d5fae652689754a8e8aa64039f7d887c1018fd6/main.py#L207-L213) · [main.py:215](https://github.com/gviollaz/iita-ga4-mcp/blob/9d5fae652689754a8e8aa64039f7d887c1018fd6/main.py#L215-L225) · [main.py:35](https://github.com/gviollaz/iita-ga4-mcp/blob/9d5fae652689754a8e8aa64039f7d887c1018fd6/main.py#L35-L60).

## ga4_device_geo

Runs a Data API report selecting deviceCategory, country or city dimension from breakdown; sessions, totalUsers, screenPageViews and bounceRate metrics; resolved dates and caller limit; orders by sessions descending; formats Markdown.

<details>
<summary>Full registered description</summary>

```text
Get traffic breakdown by device or geography.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `params` | Yes | DeviceGeoInput | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "title": "ga4_device_geoArguments",
  "properties": {
    "params": {
      "$ref": "#/$defs/DeviceGeoInput"
    }
  },
  "required": [
    "params"
  ],
  "$defs": {
    "DeviceGeoInput": {
      "type": "object",
      "title": "DeviceGeoInput",
      "properties": {
        "breakdown": {
          "type": "string",
          "title": "Breakdown",
          "default": "device",
          "description": "'device', 'country', or 'city'"
        },
        "date_range": {
          "type": "string",
          "title": "Date Range",
          "default": "LAST_28_DAYS"
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
          "default": null
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
          "default": null
        },
        "limit": {
          "type": "integer",
          "title": "Limit",
          "default": 20,
          "minimum": 1,
          "maximum": 100
        },
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
          "default": null
        }
      },
      "additionalProperties": false
    }
  }
}
```

</details>

- The single params argument is required; all nested model fields have defaults. Nested model forbids extra fields; no aliases or custom validators are defined.
- date_range is an unrestricted string, not an enum. Handler recognizes TODAY, YESTERDAY, LAST_7_DAYS, LAST_14_DAYS, LAST_28_DAYS, LAST_30_DAYS, LAST_90_DAYS and THIS_MONTH; unknown strings fall back to last 28 days. Explicit dates override only when both are truthy. Dates have no exposed format validation; N-day presets include today and today minus N days.
- Does not guard against missing property_id/GA4_PROPERTY_ID and can submit properties/ to the API.
- breakdown has no enum constraint; unknown strings use deviceCategory.
- Synchronous Google client call inside async handler; API errors are not caught locally.

Source: [main.py:227](https://github.com/gviollaz/iita-ga4-mcp/blob/9d5fae652689754a8e8aa64039f7d887c1018fd6/main.py#L227-L234) · [main.py:236](https://github.com/gviollaz/iita-ga4-mcp/blob/9d5fae652689754a8e8aa64039f7d887c1018fd6/main.py#L236-L248) · [main.py:35](https://github.com/gviollaz/iita-ga4-mcp/blob/9d5fae652689754a8e8aa64039f7d887c1018fd6/main.py#L35-L60).

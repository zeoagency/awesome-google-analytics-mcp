# TheTechBasket/GA4-Dashboard-MCP

[Catalog](../../README.md) · [All tool names](../tool-index.md) · [Upstream](https://github.com/TheTechBasket/GA4-Dashboard-MCP) · [JSON](../../data/mcps/thetechbasket--ga4-dashboard-mcp.json)

**11 tools:** 7 GA4, 4 other-service or server-support tools. Reviewed source: [`349560e7ba02`](https://github.com/TheTechBasket/GA4-Dashboard-MCP/tree/349560e7ba0221dccb152e0a87fd573d8974c785).

Descriptions and parameter schemas come from the registered source definitions. Generated schemas are reconstructed from annotations or validators; live `tools/list` and authenticated API calls were not run. Loose objects remain loose.

<details>
<summary>Exposure and compatibility notes</summary>

- Source review only; no tools/list, upstream execution or live requests. Source has no .git; supplied revision is authoritative.
- All 11 tools register unconditionally; package.json mcp script launches mcp-server/index.js and dependencies include SDK, Zod and GA client libraries. GA clients initialize lazily and require GA4_CLIENT_EMAIL and GA4_PRIVATE_KEY from root .env.
- Zod shapes reconstructed as JSON Schema; defaulted parameters are optional inputs. Zod objects strip unknown keys, represented by additionalProperties false. No exposed numeric-ID regex or date-format restriction beyond descriptions.
- cachedCall checks disk/memory cache before guards, then limits property spread (default 3 properties/10 minutes), concurrency (default 3/property), pool quota and cooldowns, and local API-family throttling. Report/realtime/funnel record quota in shared ledger. TTL defaults: metadata 21600s, report 3600s, realtime 60s, PSI 1800s, configurable by environment.
- Every output uses compact JSON text; guard.fitResult removes trailing report rows for default 12000-byte cap. Non-row responses can exceed this cap. API read tools also write local cache/ledger.
- rateLimit permits one retry for unavailable/server errors and concurrency exhaustion; PSI 429 is mapped to code 8 and retried once. No definite entrypoint blocker identified by source inspection.

</details>

## Tools

| Tool | Scope | Effect |
| --- | --- | --- |
| [`get_account_summaries`](#get_account_summaries) | GA4 | read |
| [`get_property_details`](#get_property_details) | GA4 | read |
| [`list_google_ads_links`](#list_google_ads_links) | GA4 | read |
| [`run_report`](#run_report) | GA4 | read |
| [`run_funnel_report`](#run_funnel_report) | GA4 | read |
| [`get_custom_dimensions_and_metrics`](#get_custom_dimensions_and_metrics) | GA4 | read |
| [`run_realtime_report`](#run_realtime_report) | GA4 | read |
| [`run_pagespeed_insights`](#run_pagespeed_insights) | Other service | read |
| [`request_indexing`](#request_indexing) | Other service | write |
| [`get_cache_status`](#get_cache_status) | Server support | local |
| [`get_rate_limit_status`](#get_rate_limit_status) | Server support | local |

## get_account_summaries

Lists accounts and property summaries; projects account, displayName, property name/displayName/type; cached metadata.

<details>
<summary>Full registered description</summary>

```text
Lists every GA4 account and its properties for the credentials in use. Admin API, no GA4 tokens. Call it once per session to find a property ID, then work on that one property.
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

Source: [mcp-server/index.js:138](https://github.com/TheTechBasket/GA4-Dashboard-MCP/blob/349560e7ba0221dccb152e0a87fd573d8974c785/mcp-server/index.js#L138-L167).

## get_property_details

Reads property details and selects name, displayName, timeZone, currencyCode, industryCategory, propertyType, createTime and parent; cached metadata.

<details>
<summary>Full registered description</summary>

```text
Returns details (display name, time zone, currency, industry, create time) for one GA4 property. Admin API, no GA4 tokens; cached 6h.
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
      "type": "string",
      "description": "Numeric GA4 property ID, e.g. 257579250"
    }
  },
  "required": [
    "propertyId"
  ],
  "additionalProperties": false
}
```

</details>

Source: [mcp-server/index.js:193](https://github.com/TheTechBasket/GA4-Dashboard-MCP/blob/349560e7ba0221dccb152e0a87fd573d8974c785/mcp-server/index.js#L193-L201) · [mcp-server/index.js:169](https://github.com/TheTechBasket/GA4-Dashboard-MCP/blob/349560e7ba0221dccb152e0a87fd573d8974c785/mcp-server/index.js#L169-L191).

## list_google_ads_links

Lists links under properties/{propertyId}; returns name, customerId, canManageClients and createTime; cached metadata.

<details>
<summary>Full registered description</summary>

```text
Lists the Google Ads accounts linked to a GA4 property. Admin API, no GA4 tokens; cached 6h.
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
      "type": "string",
      "description": "Numeric GA4 property ID"
    }
  },
  "required": [
    "propertyId"
  ],
  "additionalProperties": false
}
```

</details>

Source: [mcp-server/index.js:203](https://github.com/TheTechBasket/GA4-Dashboard-MCP/blob/349560e7ba0221dccb152e0a87fd573d8974c785/mcp-server/index.js#L203-L230).

## run_report

Builds one date range with named dimensions and metrics, limit/offset, metric or dimension sorting and ANDed string dimension filters. Requests property quota; returns compact headers/rows, rowCount, returned/truncated and quota, cached report. Money-like metric names trigger cached Admin getProperty lookup to append currencyCode.

<details>
<summary>Full registered description</summary>

```text
Runs a GA4 core report: dimensions x metrics over a date range. Pool: core. Cost grows with rows, dimensions, date range and cardinality, so use orderBys, a small limit and a dimensionFilter.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `propertyId` | Yes | string | Not declared |
| `startDate` | Yes | string | Not declared |
| `endDate` | Yes | string | Not declared |
| `dimensions` | Yes | array of string | Not declared |
| `metrics` | Yes | array of string | Not declared |
| `limit` | No | integer | 10 |
| `offset` | No | integer | 0 |
| `orderBys` | No | array of object | Not declared |
| `dimensionFilter` | No | object | Not declared |
| `dimensionFilters` | No | array of object | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "propertyId": {
      "type": "string",
      "description": "Numeric GA4 property ID"
    },
    "startDate": {
      "type": "string",
      "description": "e.g. 7daysAgo, 28daysAgo, today, or YYYY-MM-DD. Range max 93 days."
    },
    "endDate": {
      "type": "string",
      "description": "e.g. today, yesterday, or YYYY-MM-DD"
    },
    "dimensions": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Max 4, e.g. [\"country\", \"sessionSource\"]"
    },
    "metrics": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Max 6, e.g. [\"sessions\", \"activeUsers\"]"
    },
    "limit": {
      "type": "integer",
      "exclusiveMinimum": 0,
      "maximum": 250,
      "default": 10,
      "description": "Rows to return. Max 50 with a high-cardinality dimension."
    },
    "offset": {
      "type": "integer",
      "minimum": 0,
      "default": 0,
      "description": "Row offset for paging"
    },
    "orderBys": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "metric": {
            "type": "string",
            "description": "Metric name to sort by, e.g. \"totalAdRevenue\""
          },
          "dimension": {
            "type": "string",
            "description": "Dimension name to sort by instead of a metric"
          },
          "desc": {
            "type": "boolean",
            "default": true
          }
        },
        "required": [],
        "additionalProperties": false
      },
      "description": "Sort rows server-side, e.g. top pages by revenue. Required with pagePath, pageTitle, landingPage and custom dimensions."
    },
    "dimensionFilter": {
      "type": "object",
      "properties": {
        "dimension": {
          "type": "string",
          "description": "Dimension to filter on, e.g. \"pagePath\""
        },
        "matchType": {
          "type": "string",
          "enum": [
            "EXACT",
            "BEGINS_WITH",
            "ENDS_WITH",
            "CONTAINS",
            "FULL_REGEXP"
          ],
          "default": "EXACT"
        },
        "value": {
          "type": "string"
        },
        "caseSensitive": {
          "type": "boolean"
        }
      },
      "required": [
        "dimension",
        "value"
      ],
      "additionalProperties": false,
      "description": "Filter rows server-side instead of pulling them and filtering"
    },
    "dimensionFilters": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "dimension": {
            "type": "string",
            "description": "Dimension to filter on, e.g. \"pagePath\""
          },
          "matchType": {
            "type": "string",
            "enum": [
              "EXACT",
              "BEGINS_WITH",
              "ENDS_WITH",
              "CONTAINS",
              "FULL_REGEXP"
            ],
            "default": "EXACT"
          },
          "value": {
            "type": "string"
          },
          "caseSensitive": {
            "type": "boolean"
          }
        },
        "required": [
          "dimension",
          "value"
        ],
        "additionalProperties": false
      },
      "description": "Several filters, ANDed"
    }
  },
  "required": [
    "propertyId",
    "startDate",
    "endDate",
    "dimensions",
    "metrics"
  ],
  "additionalProperties": false
}
```

</details>

- Implementation guards, not schema constraints: at most 4 dimensions, 6 metrics and 93 inclusive days when dates parse; pagePath/pageLocation/pageTitle, landingPage* and customEvent:/customUser: dimensions require nonempty orderBys and limit <=50. Validation occurs only on cache miss.
- orderBys objects allow neither or both metric/dimension; handler prefers metric when truthy and otherwise forwards dimension, without enforcing exactly one.

Source: [mcp-server/index.js:236](https://github.com/TheTechBasket/GA4-Dashboard-MCP/blob/349560e7ba0221dccb152e0a87fd573d8974c785/mcp-server/index.js#L236-L300) · [mcp-server/index.js:114](https://github.com/TheTechBasket/GA4-Dashboard-MCP/blob/349560e7ba0221dccb152e0a87fd573d8974c785/mcp-server/index.js#L114-L132) · [mcp-server/lib/guard.js:15](https://github.com/TheTechBasket/GA4-Dashboard-MCP/blob/349560e7ba0221dccb152e0a87fd573d8974c785/mcp-server/lib/guard.js#L15-L115).

## run_funnel_report

Builds an ordered funnel whose steps filter eventName with stringFilter.value; requests property quota. Compacts funnelTable dimension/metric headers and rows and caps returned rows to 100; cached report.

<details>
<summary>Full registered description</summary>

```text
Runs a GA4 funnel report: how many users completed each step of an ordered event sequence. Pool: funnel. Use few steps and the shortest date range; rows are capped at 100.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `propertyId` | Yes | string | Not declared |
| `startDate` | Yes | string | Not declared |
| `endDate` | Yes | string | Not declared |
| `steps` | Yes | array of object | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "propertyId": {
      "type": "string",
      "description": "Numeric GA4 property ID"
    },
    "startDate": {
      "type": "string",
      "description": "e.g. 7daysAgo or YYYY-MM-DD"
    },
    "endDate": {
      "type": "string",
      "description": "e.g. today or YYYY-MM-DD"
    },
    "steps": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "eventName": {
            "type": "string"
          }
        },
        "required": [
          "name",
          "eventName"
        ],
        "additionalProperties": false
      },
      "minItems": 2,
      "description": "Ordered funnel steps, each matched by a single eventName"
    }
  },
  "required": [
    "propertyId",
    "startDate",
    "endDate",
    "steps"
  ],
  "additionalProperties": false
}
```

</details>

- 100-row cap is applied after API response; no request row limit or date-range guard. Event stringFilter lacks an explicit matchType.

Source: [mcp-server/index.js:302](https://github.com/TheTechBasket/GA4-Dashboard-MCP/blob/349560e7ba0221dccb152e0a87fd573d8974c785/mcp-server/index.js#L302-L357).

## get_custom_dimensions_and_metrics

Reads properties/{propertyId}/metadata; filters dimensions and metrics to customDefinition and returns apiName, uiName and description; cached metadata.

<details>
<summary>Full registered description</summary>

```text
Lists the custom dimensions and custom metrics defined on a GA4 property. Pool: core (getMetadata spends a few core tokens, no quota is returned). Cached 6h, so call it once.
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
      "type": "string",
      "description": "Numeric GA4 property ID"
    }
  },
  "required": [
    "propertyId"
  ],
  "additionalProperties": false
}
```

</details>

- Despite description naming core pool, cachedCall has no pool field, so shared quota gate/record is not used; getMetadata returns no quota.

Source: [mcp-server/index.js:359](https://github.com/TheTechBasket/GA4-Dashboard-MCP/blob/349560e7ba0221dccb152e0a87fd573d8974c785/mcp-server/index.js#L359-L384).

## run_realtime_report

Uses named dimensions and metrics and minuteRanges from minutesAgo to 0; requests property quota; compacts response with row counts and quota; cached realtime. Money-like metrics trigger cached Admin getProperty currency lookup.

<details>
<summary>Full registered description</summary>

```text
Runs a GA4 realtime report covering the last N minutes (max 30). Pool: realtime. Keep dimensions few and the limit small; results are cached 60s.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `propertyId` | Yes | string | Not declared |
| `dimensions` | No | array of string | ["country"] |
| `metrics` | No | array of string | ["activeUsers"] |
| `minutesAgo` | No | integer | 29 |
| `limit` | No | integer | 10 |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "propertyId": {
      "type": "string",
      "description": "Numeric GA4 property ID"
    },
    "dimensions": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "default": [
        "country"
      ]
    },
    "metrics": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "default": [
        "activeUsers"
      ]
    },
    "minutesAgo": {
      "type": "integer",
      "minimum": 1,
      "maximum": 30,
      "default": 29
    },
    "limit": {
      "type": "integer",
      "exclusiveMinimum": 0,
      "maximum": 250,
      "default": 10
    }
  },
  "required": [
    "propertyId"
  ],
  "additionalProperties": false
}
```

</details>

Source: [mcp-server/index.js:390](https://github.com/TheTechBasket/GA4-Dashboard-MCP/blob/349560e7ba0221dccb152e0a87fd573d8974c785/mcp-server/index.js#L390-L432).

## run_pagespeed_insights

GETs the PageSpeed endpoint with URL, strategy, repeated category parameters and PSI_API_KEY. Returns rounded Lighthouse category scores and display values for LCP, CLS, TBT and FCP; cached PSI.

<details>
<summary>Full registered description</summary>

```text
Runs a PageSpeed Insights audit for one URL (Lighthouse performance/SEO/accessibility/best-practices scores).
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `url` | Yes | string | Not declared |
| `strategy` | No | string | "mobile" |
| `categories` | No | array of string | ["performance"] |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "url": {
      "type": "string",
      "format": "uri"
    },
    "strategy": {
      "type": "string",
      "enum": [
        "mobile",
        "desktop"
      ],
      "default": "mobile"
    },
    "categories": {
      "type": "array",
      "items": {
        "type": "string",
        "enum": [
          "performance",
          "accessibility",
          "best-practices",
          "seo"
        ]
      },
      "default": [
        "performance"
      ]
    }
  },
  "required": [
    "url"
  ],
  "additionalProperties": false
}
```

</details>

- Tool is always registered; missing PSI_API_KEY returns an error result.

Source: [mcp-server/index.js:438](https://github.com/TheTechBasket/GA4-Dashboard-MCP/blob/349560e7ba0221dccb152e0a87fd573d8974c785/mcp-server/index.js#L438-L492).

## request_indexing

Obtains scoped service-account auth and POSTs {url,type} to urlNotifications:publish through the indexing rate limiter; returns response data or caught error plus ownership hint; no cache.

<details>
<summary>Full registered description</summary>

```text
Notifies Google's Indexing API that a URL changed, so it can be recrawled sooner. Requires the GA service account to be added as an Owner of the URL's property in Search Console, otherwise this returns a 403 ownership error. Not cached (it's an action, not a query).
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `url` | Yes | string | Not declared |
| `type` | No | string | "URL_UPDATED" |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "url": {
      "type": "string",
      "format": "uri"
    },
    "type": {
      "type": "string",
      "enum": [
        "URL_UPDATED",
        "URL_DELETED"
      ],
      "default": "URL_UPDATED"
    }
  },
  "required": [
    "url"
  ],
  "additionalProperties": false
}
```

</details>

- Uses the same GA4 service-account credentials with indexing scope; ownership errors become normal text error results.

Source: [mcp-server/index.js:498](https://github.com/TheTechBasket/GA4-Dashboard-MCP/blob/349560e7ba0221dccb152e0a87fd573d8974c785/mcp-server/index.js#L498-L525).

## get_cache_status

Reads on-disk cache JSON entries, consulting memory when available, and returns toolName, params, ageSeconds, ttlSeconds and freshness; creates cache directory if absent.

<details>
<summary>Full registered description</summary>

```text
Lists every cached tool response on disk: which tool, params, age, TTL, and whether it's still fresh.
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

- Malformed on-disk cache JSON is not caught by status().

Source: [mcp-server/index.js:531](https://github.com/TheTechBasket/GA4-Dashboard-MCP/blob/349560e7ba0221dccb152e0a87fd573d8974c785/mcp-server/index.js#L531-L535).

## get_rate_limit_status

Returns shared ledger project identifier, cooldowns, quota entries, next daily reset, reserve thresholds and standard limits, plus refreshed local token bucket state; no Google calls.

<details>
<summary>Full registered description</summary>

```text
Shows GA4 quota left per property and pool (from the shared ledger the dashboard also writes), the reserve thresholds, Google's limits and the local throttle state. Costs no GA4 tokens.
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

Source: [mcp-server/index.js:537](https://github.com/TheTechBasket/GA4-Dashboard-MCP/blob/349560e7ba0221dccb152e0a87fd573d8974c785/mcp-server/index.js#L537-L554).

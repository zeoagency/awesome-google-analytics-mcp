# delaren47/gsc-ga4-mcp

[Catalog](../../README.md) · [All tool names](../tool-index.md) · [Upstream](https://github.com/delaren47/gsc-ga4-mcp) · [JSON](../../data/mcps/delaren47--gsc-ga4-mcp.json)

**20 tools:** 11 GA4, 9 other-service or server-support tools. Reviewed source: [`b21d75c0baa6`](https://github.com/delaren47/gsc-ga4-mcp/tree/b21d75c0baa66e4a9f992aa864ef6aaa5196794f).

Descriptions and parameter schemas come from the registered source definitions. Generated schemas are reconstructed from annotations or validators; live `tools/list` and authenticated API calls were not run. Loose objects remain loose.

<details>
<summary>Exposure and compatibility notes</summary>

- Source review only; no tools/list, upstream execution, or live requests.
- All 20 tools are registered unconditionally in src/index.ts. Auth CLI is a separate npm auth command, not an MCP tool.
- Zod raw shapes are expanded including shared dateRange/gscSite/ga4Property objects. Zod objects strip unknown keys; additionalProperties false reflects exposed schema.
- API requests require OAuth token/client files or service-account key. Authentication requests read-only webmasters and analytics scopes. No concrete unusable entrypoint found by source inspection.

</details>

## Tools

| Tool | Scope | Effect |
| --- | --- | --- |
| [`project_mappings`](#project_mappings) | Server support | local |
| [`project_lookup`](#project_lookup) | Server support | local |
| [`gsc_list_sites`](#gsc_list_sites) | Other service | read |
| [`gsc_search_analytics`](#gsc_search_analytics) | Other service | read |
| [`gsc_top_queries`](#gsc_top_queries) | Other service | read |
| [`gsc_top_pages`](#gsc_top_pages) | Other service | read |
| [`gsc_query_page_matrix`](#gsc_query_page_matrix) | Other service | read |
| [`gsc_url_inspection`](#gsc_url_inspection) | Other service | read |
| [`ga4_list_properties`](#ga4_list_properties) | GA4 | read |
| [`ga4_run_report`](#ga4_run_report) | GA4 | read |
| [`ga4_top_pages`](#ga4_top_pages) | GA4 | read |
| [`ga4_traffic_sources`](#ga4_traffic_sources) | GA4 | read |
| [`ga4_landing_pages`](#ga4_landing_pages) | GA4 | read |
| [`ga4_events`](#ga4_events) | GA4 | read |
| [`ga4_realtime`](#ga4_realtime) | GA4 | read |
| [`find_high_impression_low_ctr_pages`](#find_high_impression_low_ctr_pages) | Other service | read |
| [`compare_gsc_ga4_pages`](#compare_gsc_ga4_pages) | GA4 | read |
| [`find_pages_with_clicks_but_low_engagement`](#find_pages_with_clicks_but_low_engagement) | GA4 | read |
| [`content_refresh_candidates`](#content_refresh_candidates) | GA4 | read |
| [`seo_opportunity_report`](#seo_opportunity_report) | GA4 | read |

## project_mappings

Reads PROJECTS_CONFIG JSON and returns its projects array, or an empty array for an unset/missing file. Returns JSON-stringified data in MCP text content.

<details>
<summary>Full registered description</summary>

```text
List local domain/client mappings from PROJECTS_CONFIG.
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

Source: [src/index.ts:44](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/index.ts#L44-L44) · [src/config.ts:51](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/config.ts#L51-L58).

## project_lookup

Reads local mappings and returns the first project whose name, client or domain equals or contains the case-insensitive query, otherwise {found:false}. Returns JSON-stringified data in MCP text content.

<details>
<summary>Full registered description</summary>

```text
Find a local project mapping by project name, client, or domain.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `nameOrDomain` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "nameOrDomain": {
      "type": "string"
    }
  },
  "required": [
    "nameOrDomain"
  ],
  "additionalProperties": false
}
```

</details>

Source: [src/index.ts:46](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/index.ts#L46-L51) · [src/config.ts:60](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/config.ts#L60-L67).

## gsc_list_sites

GETs Search Console sites visible to credentials. Returns JSON-stringified data in MCP text content.

<details>
<summary>Full registered description</summary>

```text
List Google Search Console sites visible to the current credentials.
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

Source: [src/index.ts:53](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/index.ts#L53-L53) · [src/google.ts:29](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/google.ts#L29-L31) · [src/google.ts:6](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/google.ts#L6-L15) · [src/auth.ts:48](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/auth.ts#L48-L65).

## gsc_search_analytics

POSTs startDate/endDate, named dimensions, capped rowLimit, startRow (default 0), type (default web) to the encoded site searchAnalytics/query endpoint. Returns JSON-stringified data in MCP text content.

<details>
<summary>Full registered description</summary>

```text
Run a raw Search Console Search Analytics query.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `siteUrl` | No | string | Not declared |
| `startDate` | Yes | string | Not declared |
| `endDate` | Yes | string | Not declared |
| `dimensions` | No | array of string | ["query"] |
| `rowLimit` | No | integer | Not declared |
| `startRow` | No | integer | Not declared |
| `type` | No | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "siteUrl": {
      "type": "string",
      "description": "GSC property, e.g. sc-domain:example.com or https://www.example.com/"
    },
    "startDate": {
      "type": "string",
      "description": "YYYY-MM-DD"
    },
    "endDate": {
      "type": "string",
      "description": "YYYY-MM-DD"
    },
    "dimensions": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "default": [
        "query"
      ]
    },
    "rowLimit": {
      "type": "integer",
      "exclusiveMinimum": 0
    },
    "startRow": {
      "type": "integer",
      "minimum": 0
    },
    "type": {
      "type": "string",
      "enum": [
        "web",
        "image",
        "video",
        "news",
        "discover",
        "googleNews"
      ]
    }
  },
  "required": [
    "startDate",
    "endDate"
  ],
  "additionalProperties": false
}
```

</details>

- Optional siteUrl/property requires MCP_DEFAULT_GSC_SITE/MCP_DEFAULT_GA4_PROPERTY respectively when omitted; missing effective value throws. Numeric GA4 property IDs gain properties/ prefix.
- Handler caps rows via MAX_ROWS (default 25000); omitted raw report/query limit becomes 1000. No automatic row pagination.
- Internal dimensionFilterGroups is not exposed in the registered schema.
- YYYY-MM-DD is descriptive only; dates have no format or regex validation.

Source: [src/index.ts:55](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/index.ts#L55-L67) · [src/google.ts:33](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/google.ts#L33-L58) · [src/config.ts:39](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/config.ts#L39-L49) · [src/google.ts:17](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/google.ts#L17-L19) · [src/config.ts:34](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/config.ts#L34-L37) · [src/google.ts:6](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/google.ts#L6-L15) · [src/auth.ts:48](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/auth.ts#L48-L65) · [src/index.ts:31](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/index.ts#L31-L42).

## gsc_top_queries

Queries GSC with dimensions [query]. Returns JSON-stringified data in MCP text content.

<details>
<summary>Full registered description</summary>

```text
Top GSC queries by clicks/impressions.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `siteUrl` | No | string | Not declared |
| `startDate` | Yes | string | Not declared |
| `endDate` | Yes | string | Not declared |
| `rowLimit` | No | integer | 100 |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "siteUrl": {
      "type": "string",
      "description": "GSC property, e.g. sc-domain:example.com or https://www.example.com/"
    },
    "startDate": {
      "type": "string",
      "description": "YYYY-MM-DD"
    },
    "endDate": {
      "type": "string",
      "description": "YYYY-MM-DD"
    },
    "rowLimit": {
      "type": "integer",
      "exclusiveMinimum": 0,
      "default": 100
    }
  },
  "required": [
    "startDate",
    "endDate"
  ],
  "additionalProperties": false
}
```

</details>

- Optional siteUrl/property requires MCP_DEFAULT_GSC_SITE/MCP_DEFAULT_GA4_PROPERTY respectively when omitted; missing effective value throws. Numeric GA4 property IDs gain properties/ prefix.
- Handler caps rows via MAX_ROWS (default 25000); omitted raw report/query limit becomes 1000. No automatic row pagination.
- YYYY-MM-DD is descriptive only; dates have no format or regex validation.

Source: [src/index.ts:69](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/index.ts#L69-L74) · [src/google.ts:33](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/google.ts#L33-L58) · [src/config.ts:39](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/config.ts#L39-L49) · [src/google.ts:17](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/google.ts#L17-L19) · [src/config.ts:34](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/config.ts#L34-L37) · [src/google.ts:6](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/google.ts#L6-L15) · [src/auth.ts:48](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/auth.ts#L48-L65) · [src/index.ts:31](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/index.ts#L31-L42).

## gsc_top_pages

Queries GSC with dimensions [page]. Returns JSON-stringified data in MCP text content.

<details>
<summary>Full registered description</summary>

```text
Top GSC pages by clicks/impressions.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `siteUrl` | No | string | Not declared |
| `startDate` | Yes | string | Not declared |
| `endDate` | Yes | string | Not declared |
| `rowLimit` | No | integer | 100 |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "siteUrl": {
      "type": "string",
      "description": "GSC property, e.g. sc-domain:example.com or https://www.example.com/"
    },
    "startDate": {
      "type": "string",
      "description": "YYYY-MM-DD"
    },
    "endDate": {
      "type": "string",
      "description": "YYYY-MM-DD"
    },
    "rowLimit": {
      "type": "integer",
      "exclusiveMinimum": 0,
      "default": 100
    }
  },
  "required": [
    "startDate",
    "endDate"
  ],
  "additionalProperties": false
}
```

</details>

- Optional siteUrl/property requires MCP_DEFAULT_GSC_SITE/MCP_DEFAULT_GA4_PROPERTY respectively when omitted; missing effective value throws. Numeric GA4 property IDs gain properties/ prefix.
- Handler caps rows via MAX_ROWS (default 25000); omitted raw report/query limit becomes 1000. No automatic row pagination.
- YYYY-MM-DD is descriptive only; dates have no format or regex validation.

Source: [src/index.ts:76](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/index.ts#L76-L81) · [src/google.ts:33](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/google.ts#L33-L58) · [src/config.ts:39](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/config.ts#L39-L49) · [src/google.ts:17](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/google.ts#L17-L19) · [src/config.ts:34](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/config.ts#L34-L37) · [src/google.ts:6](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/google.ts#L6-L15) · [src/auth.ts:48](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/auth.ts#L48-L65) · [src/index.ts:31](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/index.ts#L31-L42).

## gsc_query_page_matrix

Queries GSC with dimensions [query,page]. Returns JSON-stringified data in MCP text content.

<details>
<summary>Full registered description</summary>

```text
GSC query/page matrix for finding page-level keyword opportunities.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `siteUrl` | No | string | Not declared |
| `startDate` | Yes | string | Not declared |
| `endDate` | Yes | string | Not declared |
| `rowLimit` | No | integer | 1000 |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "siteUrl": {
      "type": "string",
      "description": "GSC property, e.g. sc-domain:example.com or https://www.example.com/"
    },
    "startDate": {
      "type": "string",
      "description": "YYYY-MM-DD"
    },
    "endDate": {
      "type": "string",
      "description": "YYYY-MM-DD"
    },
    "rowLimit": {
      "type": "integer",
      "exclusiveMinimum": 0,
      "default": 1000
    }
  },
  "required": [
    "startDate",
    "endDate"
  ],
  "additionalProperties": false
}
```

</details>

- Optional siteUrl/property requires MCP_DEFAULT_GSC_SITE/MCP_DEFAULT_GA4_PROPERTY respectively when omitted; missing effective value throws. Numeric GA4 property IDs gain properties/ prefix.
- Handler caps rows via MAX_ROWS (default 25000); omitted raw report/query limit becomes 1000. No automatic row pagination.
- YYYY-MM-DD is descriptive only; dates have no format or regex validation.

Source: [src/index.ts:83](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/index.ts#L83-L88) · [src/google.ts:33](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/google.ts#L33-L58) · [src/config.ts:39](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/config.ts#L39-L49) · [src/google.ts:17](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/google.ts#L17-L19) · [src/config.ts:34](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/config.ts#L34-L37) · [src/google.ts:6](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/google.ts#L6-L15) · [src/auth.ts:48](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/auth.ts#L48-L65) · [src/index.ts:31](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/index.ts#L31-L42).

## gsc_url_inspection

POSTs siteUrl and inspectionUrl to index:inspect; omitted languageCode becomes es-MX. Returns JSON-stringified data in MCP text content.

<details>
<summary>Full registered description</summary>

```text
Inspect Google index status for a URL under a GSC property.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `siteUrl` | No | string | Not declared |
| `inspectionUrl` | Yes | string | Not declared |
| `languageCode` | No | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "siteUrl": {
      "type": "string",
      "description": "GSC property, e.g. sc-domain:example.com or https://www.example.com/"
    },
    "inspectionUrl": {
      "type": "string",
      "format": "uri"
    },
    "languageCode": {
      "type": "string"
    }
  },
  "required": [
    "inspectionUrl"
  ],
  "additionalProperties": false
}
```

</details>

- Optional siteUrl/property requires MCP_DEFAULT_GSC_SITE/MCP_DEFAULT_GA4_PROPERTY respectively when omitted; missing effective value throws. Numeric GA4 property IDs gain properties/ prefix.

Source: [src/index.ts:90](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/index.ts#L90-L99) · [src/google.ts:60](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/google.ts#L60-L67) · [src/config.ts:39](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/config.ts#L39-L49) · [src/google.ts:6](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/google.ts#L6-L15) · [src/auth.ts:48](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/auth.ts#L48-L65) · [src/index.ts:31](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/index.ts#L31-L42).

## ga4_list_properties

GETs accountSummaries with pageSize 200, following nextPageToken until exhausted, and returns all account summaries. Returns JSON-stringified data in MCP text content.

<details>
<summary>Full registered description</summary>

```text
List GA4 accounts and property summaries visible to the credentials.
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

Source: [src/index.ts:101](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/index.ts#L101-L101) · [src/google.ts:69](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/google.ts#L69-L81) · [src/google.ts:6](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/google.ts#L6-L15) · [src/auth.ts:48](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/auth.ts#L48-L65).

## ga4_run_report

POSTs one date range, dimensions/metrics converted from names to {name} objects, capped limit and offset (default 0) encoded as strings to the property runReport endpoint. Returns JSON-stringified data in MCP text content.

<details>
<summary>Full registered description</summary>

```text
Run a raw GA4 Data API report.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property` | No | string | Not declared |
| `startDate` | Yes | string | Not declared |
| `endDate` | Yes | string | Not declared |
| `dimensions` | Yes | array of string | Not declared |
| `metrics` | Yes | array of string | Not declared |
| `limit` | No | integer | Not declared |
| `offset` | No | integer | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "property": {
      "type": "string",
      "description": "GA4 property, e.g. properties/123456789 or 123456789"
    },
    "startDate": {
      "type": "string",
      "description": "YYYY-MM-DD"
    },
    "endDate": {
      "type": "string",
      "description": "YYYY-MM-DD"
    },
    "dimensions": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "metrics": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "limit": {
      "type": "integer",
      "exclusiveMinimum": 0
    },
    "offset": {
      "type": "integer",
      "minimum": 0
    }
  },
  "required": [
    "startDate",
    "endDate",
    "dimensions",
    "metrics"
  ],
  "additionalProperties": false
}
```

</details>

- Optional siteUrl/property requires MCP_DEFAULT_GSC_SITE/MCP_DEFAULT_GA4_PROPERTY respectively when omitted; missing effective value throws. Numeric GA4 property IDs gain properties/ prefix.
- Handler caps rows via MAX_ROWS (default 25000); omitted raw report/query limit becomes 1000. No automatic row pagination.
- Internal dimensionFilter, metricFilter and orderBys are not exposed in the registered schema.
- YYYY-MM-DD is descriptive only; dates have no format or regex validation.

Source: [src/index.ts:103](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/index.ts#L103-L115) · [src/google.ts:83](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/google.ts#L83-L107) · [src/config.ts:39](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/config.ts#L39-L49) · [src/google.ts:17](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/google.ts#L17-L19) · [src/config.ts:34](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/config.ts#L34-L37) · [src/google.ts:6](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/google.ts#L6-L15) · [src/auth.ts:48](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/auth.ts#L48-L65) · [src/index.ts:31](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/index.ts#L31-L42).

## ga4_top_pages

Runs report with pagePathPlusQueryString,pageTitle and screenPageViews,activeUsers,sessions. Returns JSON-stringified data in MCP text content.

<details>
<summary>Full registered description</summary>

```text
Top GA4 pages by views, users, and sessions.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property` | No | string | Not declared |
| `startDate` | Yes | string | Not declared |
| `endDate` | Yes | string | Not declared |
| `limit` | No | integer | 100 |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "property": {
      "type": "string",
      "description": "GA4 property, e.g. properties/123456789 or 123456789"
    },
    "startDate": {
      "type": "string",
      "description": "YYYY-MM-DD"
    },
    "endDate": {
      "type": "string",
      "description": "YYYY-MM-DD"
    },
    "limit": {
      "type": "integer",
      "exclusiveMinimum": 0,
      "default": 100
    }
  },
  "required": [
    "startDate",
    "endDate"
  ],
  "additionalProperties": false
}
```

</details>

- Optional siteUrl/property requires MCP_DEFAULT_GSC_SITE/MCP_DEFAULT_GA4_PROPERTY respectively when omitted; missing effective value throws. Numeric GA4 property IDs gain properties/ prefix.
- Handler caps rows via MAX_ROWS (default 25000); omitted raw report/query limit becomes 1000. No automatic row pagination.
- YYYY-MM-DD is descriptive only; dates have no format or regex validation.

Source: [src/index.ts:117](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/index.ts#L117-L129) · [src/google.ts:83](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/google.ts#L83-L107) · [src/config.ts:39](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/config.ts#L39-L49) · [src/google.ts:17](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/google.ts#L17-L19) · [src/config.ts:34](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/config.ts#L34-L37) · [src/google.ts:6](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/google.ts#L6-L15) · [src/auth.ts:48](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/auth.ts#L48-L65) · [src/index.ts:31](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/index.ts#L31-L42).

## ga4_traffic_sources

Runs report with sessionDefaultChannelGroup,sessionSourceMedium and sessions,activeUsers,engagedSessions,conversions. Returns JSON-stringified data in MCP text content.

<details>
<summary>Full registered description</summary>

```text
GA4 traffic sources by default channel group and source/medium.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property` | No | string | Not declared |
| `startDate` | Yes | string | Not declared |
| `endDate` | Yes | string | Not declared |
| `limit` | No | integer | 100 |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "property": {
      "type": "string",
      "description": "GA4 property, e.g. properties/123456789 or 123456789"
    },
    "startDate": {
      "type": "string",
      "description": "YYYY-MM-DD"
    },
    "endDate": {
      "type": "string",
      "description": "YYYY-MM-DD"
    },
    "limit": {
      "type": "integer",
      "exclusiveMinimum": 0,
      "default": 100
    }
  },
  "required": [
    "startDate",
    "endDate"
  ],
  "additionalProperties": false
}
```

</details>

- Optional siteUrl/property requires MCP_DEFAULT_GSC_SITE/MCP_DEFAULT_GA4_PROPERTY respectively when omitted; missing effective value throws. Numeric GA4 property IDs gain properties/ prefix.
- Handler caps rows via MAX_ROWS (default 25000); omitted raw report/query limit becomes 1000. No automatic row pagination.
- YYYY-MM-DD is descriptive only; dates have no format or regex validation.

Source: [src/index.ts:131](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/index.ts#L131-L143) · [src/google.ts:83](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/google.ts#L83-L107) · [src/config.ts:39](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/config.ts#L39-L49) · [src/google.ts:17](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/google.ts#L17-L19) · [src/config.ts:34](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/config.ts#L34-L37) · [src/google.ts:6](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/google.ts#L6-L15) · [src/auth.ts:48](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/auth.ts#L48-L65) · [src/index.ts:31](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/index.ts#L31-L42).

## ga4_landing_pages

Runs report with landingPagePlusQueryString and sessions,engagedSessions,engagementRate. Returns JSON-stringified data in MCP text content.

<details>
<summary>Full registered description</summary>

```text
GA4 landing pages with engagement metrics.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property` | No | string | Not declared |
| `startDate` | Yes | string | Not declared |
| `endDate` | Yes | string | Not declared |
| `limit` | No | integer | 100 |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "property": {
      "type": "string",
      "description": "GA4 property, e.g. properties/123456789 or 123456789"
    },
    "startDate": {
      "type": "string",
      "description": "YYYY-MM-DD"
    },
    "endDate": {
      "type": "string",
      "description": "YYYY-MM-DD"
    },
    "limit": {
      "type": "integer",
      "exclusiveMinimum": 0,
      "default": 100
    }
  },
  "required": [
    "startDate",
    "endDate"
  ],
  "additionalProperties": false
}
```

</details>

- Optional siteUrl/property requires MCP_DEFAULT_GSC_SITE/MCP_DEFAULT_GA4_PROPERTY respectively when omitted; missing effective value throws. Numeric GA4 property IDs gain properties/ prefix.
- Handler caps rows via MAX_ROWS (default 25000); omitted raw report/query limit becomes 1000. No automatic row pagination.
- YYYY-MM-DD is descriptive only; dates have no format or regex validation.

Source: [src/index.ts:145](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/index.ts#L145-L157) · [src/google.ts:83](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/google.ts#L83-L107) · [src/config.ts:39](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/config.ts#L39-L49) · [src/google.ts:17](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/google.ts#L17-L19) · [src/config.ts:34](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/config.ts#L34-L37) · [src/google.ts:6](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/google.ts#L6-L15) · [src/auth.ts:48](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/auth.ts#L48-L65) · [src/index.ts:31](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/index.ts#L31-L42).

## ga4_events

Runs report with eventName and eventCount,activeUsers. Returns JSON-stringified data in MCP text content.

<details>
<summary>Full registered description</summary>

```text
GA4 events by event name.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property` | No | string | Not declared |
| `startDate` | Yes | string | Not declared |
| `endDate` | Yes | string | Not declared |
| `limit` | No | integer | 100 |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "property": {
      "type": "string",
      "description": "GA4 property, e.g. properties/123456789 or 123456789"
    },
    "startDate": {
      "type": "string",
      "description": "YYYY-MM-DD"
    },
    "endDate": {
      "type": "string",
      "description": "YYYY-MM-DD"
    },
    "limit": {
      "type": "integer",
      "exclusiveMinimum": 0,
      "default": 100
    }
  },
  "required": [
    "startDate",
    "endDate"
  ],
  "additionalProperties": false
}
```

</details>

- Optional siteUrl/property requires MCP_DEFAULT_GSC_SITE/MCP_DEFAULT_GA4_PROPERTY respectively when omitted; missing effective value throws. Numeric GA4 property IDs gain properties/ prefix.
- Handler caps rows via MAX_ROWS (default 25000); omitted raw report/query limit becomes 1000. No automatic row pagination.
- YYYY-MM-DD is descriptive only; dates have no format or regex validation.

Source: [src/index.ts:159](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/index.ts#L159-L171) · [src/google.ts:83](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/google.ts#L83-L107) · [src/config.ts:39](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/config.ts#L39-L49) · [src/google.ts:17](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/google.ts#L17-L19) · [src/config.ts:34](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/config.ts#L34-L37) · [src/google.ts:6](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/google.ts#L6-L15) · [src/auth.ts:48](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/auth.ts#L48-L65) · [src/index.ts:31](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/index.ts#L31-L42).

## ga4_realtime

POSTs dimensions and metrics converted to {name} objects and capped string limit to property runRealtimeReport. Returns JSON-stringified data in MCP text content.

<details>
<summary>Full registered description</summary>

```text
GA4 realtime active users report.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property` | No | string | Not declared |
| `dimensions` | No | array of string | ["unifiedScreenName"] |
| `metrics` | No | array of string | ["activeUsers"] |
| `limit` | No | integer | 100 |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "property": {
      "type": "string",
      "description": "GA4 property, e.g. properties/123456789 or 123456789"
    },
    "dimensions": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "default": [
        "unifiedScreenName"
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
    "limit": {
      "type": "integer",
      "exclusiveMinimum": 0,
      "default": 100
    }
  },
  "required": [],
  "additionalProperties": false
}
```

</details>

- Optional siteUrl/property requires MCP_DEFAULT_GSC_SITE/MCP_DEFAULT_GA4_PROPERTY respectively when omitted; missing effective value throws. Numeric GA4 property IDs gain properties/ prefix.
- Handler caps rows via MAX_ROWS (default 25000); omitted raw report/query limit becomes 1000. No automatic row pagination.

Source: [src/index.ts:173](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/index.ts#L173-L183) · [src/google.ts:109](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/google.ts#L109-L122) · [src/config.ts:39](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/config.ts#L39-L49) · [src/google.ts:17](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/google.ts#L17-L19) · [src/config.ts:34](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/config.ts#L34-L37) · [src/google.ts:6](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/google.ts#L6-L15) · [src/auth.ts:48](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/auth.ts#L48-L65) · [src/index.ts:31](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/index.ts#L31-L42).

## find_high_impression_low_ctr_pages

Queries GSC page rows, keeps impressions >= minImpressions and ctr <= maxCtr, emits metrics and opportunityScore = round(impressions*(maxCtr-ctr+0.001)), sorted descending. Returns JSON-stringified data in MCP text content.

<details>
<summary>Full registered description</summary>

```text
Find GSC pages with high impressions and low CTR.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `siteUrl` | No | string | Not declared |
| `startDate` | Yes | string | Not declared |
| `endDate` | Yes | string | Not declared |
| `minImpressions` | No | number | 500 |
| `maxCtr` | No | number | 0.02 |
| `rowLimit` | No | integer | 5000 |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "siteUrl": {
      "type": "string",
      "description": "GSC property, e.g. sc-domain:example.com or https://www.example.com/"
    },
    "startDate": {
      "type": "string",
      "description": "YYYY-MM-DD"
    },
    "endDate": {
      "type": "string",
      "description": "YYYY-MM-DD"
    },
    "minImpressions": {
      "type": "number",
      "exclusiveMinimum": 0,
      "default": 500
    },
    "maxCtr": {
      "type": "number",
      "exclusiveMinimum": 0,
      "maximum": 1,
      "default": 0.02
    },
    "rowLimit": {
      "type": "integer",
      "exclusiveMinimum": 0,
      "default": 5000
    }
  },
  "required": [
    "startDate",
    "endDate"
  ],
  "additionalProperties": false
}
```

</details>

- Optional siteUrl/property requires MCP_DEFAULT_GSC_SITE/MCP_DEFAULT_GA4_PROPERTY respectively when omitted; missing effective value throws. Numeric GA4 property IDs gain properties/ prefix.
- Handler caps rows via MAX_ROWS (default 25000); omitted raw report/query limit becomes 1000. No automatic row pagination.
- YYYY-MM-DD is descriptive only; dates have no format or regex validation.

Source: [src/index.ts:185](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/index.ts#L185-L196) · [src/analysis.ts:16](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/analysis.ts#L16-L45) · [src/config.ts:39](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/config.ts#L39-L49) · [src/google.ts:17](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/google.ts#L17-L19) · [src/config.ts:34](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/config.ts#L34-L37) · [src/google.ts:33](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/google.ts#L33-L58) · [src/google.ts:6](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/google.ts#L6-L15) · [src/auth.ts:48](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/auth.ts#L48-L65) · [src/index.ts:31](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/index.ts#L31-L42).

## compare_gsc_ga4_pages

Concurrently requests GSC page rows and GA4 landingPagePlusQueryString with sessions, engagedSessions, engagementRate. Maps GA4 rows by normalized path, then emits each GSC page with joined metrics; missing GA4 engagement is null and other GA4 metrics are zero. Returns JSON-stringified data in MCP text content.

<details>
<summary>Full registered description</summary>

```text
Join GSC page performance with GA4 landing-page engagement.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `siteUrl` | No | string | Not declared |
| `property` | No | string | Not declared |
| `startDate` | Yes | string | Not declared |
| `endDate` | Yes | string | Not declared |
| `rowLimit` | No | integer | 5000 |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "siteUrl": {
      "type": "string",
      "description": "GSC property, e.g. sc-domain:example.com or https://www.example.com/"
    },
    "property": {
      "type": "string",
      "description": "GA4 property, e.g. properties/123456789 or 123456789"
    },
    "startDate": {
      "type": "string",
      "description": "YYYY-MM-DD"
    },
    "endDate": {
      "type": "string",
      "description": "YYYY-MM-DD"
    },
    "rowLimit": {
      "type": "integer",
      "exclusiveMinimum": 0,
      "default": 5000
    }
  },
  "required": [
    "startDate",
    "endDate"
  ],
  "additionalProperties": false
}
```

</details>

- Optional siteUrl/property requires MCP_DEFAULT_GSC_SITE/MCP_DEFAULT_GA4_PROPERTY respectively when omitted; missing effective value throws. Numeric GA4 property IDs gain properties/ prefix.
- Handler caps rows via MAX_ROWS (default 25000); omitted raw report/query limit becomes 1000. No automatic row pagination.
- YYYY-MM-DD is descriptive only; dates have no format or regex validation.
- Join uses a Map with last row winning for duplicate normalized GA4 paths, without aggregating. Absolute URLs lose queries through URL.pathname, whereas relative landing paths keep query strings in the fallback; this can prevent matches. Results use only returned GSC rows.

Source: [src/index.ts:198](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/index.ts#L198-L203) · [src/analysis.ts:47](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/analysis.ts#L47-L99) · [src/config.ts:39](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/config.ts#L39-L49) · [src/google.ts:17](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/google.ts#L17-L19) · [src/config.ts:34](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/config.ts#L34-L37) · [src/analysis.ts:3](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/analysis.ts#L3-L14) · [src/analysis.ts:47](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/analysis.ts#L47-L99) · [src/google.ts:33](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/google.ts#L33-L58) · [src/google.ts:83](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/google.ts#L83-L107) · [src/google.ts:6](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/google.ts#L6-L15) · [src/auth.ts:48](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/auth.ts#L48-L65) · [src/index.ts:31](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/index.ts#L31-L42).

## find_pages_with_clicks_but_low_engagement

Concurrently requests GSC page rows and GA4 landingPagePlusQueryString with sessions, engagedSessions, engagementRate. Maps GA4 rows by normalized path, then emits each GSC page with joined metrics; missing GA4 engagement is null and other GA4 metrics are zero. Filters gscClicks >= minClicks and engagement <= maxEngagementRate (missing engagement treated as 1), sorts descending by clicks. Returns JSON-stringified data in MCP text content.

<details>
<summary>Full registered description</summary>

```text
Find pages with GSC clicks but weak GA4 engagement.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `siteUrl` | No | string | Not declared |
| `property` | No | string | Not declared |
| `startDate` | Yes | string | Not declared |
| `endDate` | Yes | string | Not declared |
| `minClicks` | No | number | 20 |
| `maxEngagementRate` | No | number | 0.35 |
| `rowLimit` | No | integer | 5000 |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "siteUrl": {
      "type": "string",
      "description": "GSC property, e.g. sc-domain:example.com or https://www.example.com/"
    },
    "property": {
      "type": "string",
      "description": "GA4 property, e.g. properties/123456789 or 123456789"
    },
    "startDate": {
      "type": "string",
      "description": "YYYY-MM-DD"
    },
    "endDate": {
      "type": "string",
      "description": "YYYY-MM-DD"
    },
    "minClicks": {
      "type": "number",
      "exclusiveMinimum": 0,
      "default": 20
    },
    "maxEngagementRate": {
      "type": "number",
      "exclusiveMinimum": 0,
      "maximum": 1,
      "default": 0.35
    },
    "rowLimit": {
      "type": "integer",
      "exclusiveMinimum": 0,
      "default": 5000
    }
  },
  "required": [
    "startDate",
    "endDate"
  ],
  "additionalProperties": false
}
```

</details>

- Optional siteUrl/property requires MCP_DEFAULT_GSC_SITE/MCP_DEFAULT_GA4_PROPERTY respectively when omitted; missing effective value throws. Numeric GA4 property IDs gain properties/ prefix.
- Handler caps rows via MAX_ROWS (default 25000); omitted raw report/query limit becomes 1000. No automatic row pagination.
- YYYY-MM-DD is descriptive only; dates have no format or regex validation.
- Join uses a Map with last row winning for duplicate normalized GA4 paths, without aggregating. Absolute URLs lose queries through URL.pathname, whereas relative landing paths keep query strings in the fallback; this can prevent matches. Results use only returned GSC rows.

Source: [src/index.ts:205](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/index.ts#L205-L217) · [src/analysis.ts:101](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/analysis.ts#L101-L116) · [src/config.ts:39](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/config.ts#L39-L49) · [src/google.ts:17](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/google.ts#L17-L19) · [src/config.ts:34](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/config.ts#L34-L37) · [src/analysis.ts:3](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/analysis.ts#L3-L14) · [src/analysis.ts:47](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/analysis.ts#L47-L99) · [src/google.ts:33](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/google.ts#L33-L58) · [src/google.ts:83](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/google.ts#L83-L107) · [src/analysis.ts:101](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/analysis.ts#L101-L116) · [src/google.ts:6](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/google.ts#L6-L15) · [src/auth.ts:48](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/auth.ts#L48-L65) · [src/index.ts:31](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/index.ts#L31-L42).

## content_refresh_candidates

Concurrently requests GSC page rows and GA4 landingPagePlusQueryString with sessions, engagedSessions, engagementRate. Maps GA4 rows by normalized path, then emits each GSC page with joined metrics; missing GA4 engagement is null and other GA4 metrics are zero. Computes refreshScore = impressions*max(0,0.08-ctr)+clicks*max(0,0.5-(engagementRate??0.5))*10, retains positive scores and sorts descending. Returns JSON-stringified data in MCP text content.

<details>
<summary>Full registered description</summary>

```text
Rank pages that may deserve a content refresh based on GSC opportunity and GA4 engagement.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `siteUrl` | No | string | Not declared |
| `property` | No | string | Not declared |
| `startDate` | Yes | string | Not declared |
| `endDate` | Yes | string | Not declared |
| `rowLimit` | No | integer | 5000 |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "siteUrl": {
      "type": "string",
      "description": "GSC property, e.g. sc-domain:example.com or https://www.example.com/"
    },
    "property": {
      "type": "string",
      "description": "GA4 property, e.g. properties/123456789 or 123456789"
    },
    "startDate": {
      "type": "string",
      "description": "YYYY-MM-DD"
    },
    "endDate": {
      "type": "string",
      "description": "YYYY-MM-DD"
    },
    "rowLimit": {
      "type": "integer",
      "exclusiveMinimum": 0,
      "default": 5000
    }
  },
  "required": [
    "startDate",
    "endDate"
  ],
  "additionalProperties": false
}
```

</details>

- Optional siteUrl/property requires MCP_DEFAULT_GSC_SITE/MCP_DEFAULT_GA4_PROPERTY respectively when omitted; missing effective value throws. Numeric GA4 property IDs gain properties/ prefix.
- Handler caps rows via MAX_ROWS (default 25000); omitted raw report/query limit becomes 1000. No automatic row pagination.
- YYYY-MM-DD is descriptive only; dates have no format or regex validation.
- Join uses a Map with last row winning for duplicate normalized GA4 paths, without aggregating. Absolute URLs lose queries through URL.pathname, whereas relative landing paths keep query strings in the fallback; this can prevent matches. Results use only returned GSC rows.

Source: [src/index.ts:219](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/index.ts#L219-L224) · [src/analysis.ts:118](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/analysis.ts#L118-L135) · [src/config.ts:39](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/config.ts#L39-L49) · [src/google.ts:17](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/google.ts#L17-L19) · [src/config.ts:34](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/config.ts#L34-L37) · [src/analysis.ts:3](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/analysis.ts#L3-L14) · [src/analysis.ts:47](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/analysis.ts#L47-L99) · [src/google.ts:33](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/google.ts#L33-L58) · [src/google.ts:83](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/google.ts#L83-L107) · [src/analysis.ts:118](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/analysis.ts#L118-L135) · [src/google.ts:6](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/google.ts#L6-L15) · [src/auth.ts:48](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/auth.ts#L48-L65) · [src/index.ts:31](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/index.ts#L31-L42).

## seo_opportunity_report

Sequentially calls highImpressionLowCtrPages, pagesWithClicksButLowEngagement and contentRefreshCandidates with default thresholds and returns their three lists. Each independently fetches reports: total three GSC queries and two GA4 reports. Returns JSON-stringified data in MCP text content.

<details>
<summary>Full registered description</summary>

```text
Compact SEO opportunity report combining high-impression/low-CTR and low-engagement candidates.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `siteUrl` | No | string | Not declared |
| `property` | No | string | Not declared |
| `startDate` | Yes | string | Not declared |
| `endDate` | Yes | string | Not declared |
| `rowLimit` | No | integer | 5000 |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "siteUrl": {
      "type": "string",
      "description": "GSC property, e.g. sc-domain:example.com or https://www.example.com/"
    },
    "property": {
      "type": "string",
      "description": "GA4 property, e.g. properties/123456789 or 123456789"
    },
    "startDate": {
      "type": "string",
      "description": "YYYY-MM-DD"
    },
    "endDate": {
      "type": "string",
      "description": "YYYY-MM-DD"
    },
    "rowLimit": {
      "type": "integer",
      "exclusiveMinimum": 0,
      "default": 5000
    }
  },
  "required": [
    "startDate",
    "endDate"
  ],
  "additionalProperties": false
}
```

</details>

- Optional siteUrl/property requires MCP_DEFAULT_GSC_SITE/MCP_DEFAULT_GA4_PROPERTY respectively when omitted; missing effective value throws. Numeric GA4 property IDs gain properties/ prefix.
- Handler caps rows via MAX_ROWS (default 25000); omitted raw report/query limit becomes 1000. No automatic row pagination.
- YYYY-MM-DD is descriptive only; dates have no format or regex validation.
- Join uses a Map with last row winning for duplicate normalized GA4 paths, without aggregating. Absolute URLs lose queries through URL.pathname, whereas relative landing paths keep query strings in the fallback; this can prevent matches. Results use only returned GSC rows.

Source: [src/index.ts:226](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/index.ts#L226-L236) · [src/analysis.ts:16](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/analysis.ts#L16-L135) · [src/config.ts:39](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/config.ts#L39-L49) · [src/google.ts:17](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/google.ts#L17-L19) · [src/config.ts:34](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/config.ts#L34-L37) · [src/analysis.ts:3](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/analysis.ts#L3-L14) · [src/analysis.ts:47](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/analysis.ts#L47-L99) · [src/google.ts:33](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/google.ts#L33-L58) · [src/google.ts:83](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/google.ts#L83-L107) · [src/analysis.ts:101](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/analysis.ts#L101-L116) · [src/analysis.ts:118](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/analysis.ts#L118-L135) · [src/google.ts:6](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/google.ts#L6-L15) · [src/auth.ts:48](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/auth.ts#L48-L65) · [src/index.ts:31](https://github.com/delaren47/gsc-ga4-mcp/blob/b21d75c0baa66e4a9f992aa864ef6aaa5196794f/src/index.ts#L31-L42).

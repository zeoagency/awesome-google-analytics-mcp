# get-mcp-ads/google-analytics-mcp-server

[Catalog](../../README.md) · [All tool names](../tool-index.md) · [Upstream](https://github.com/get-mcp-ads/google-analytics-mcp-server) · [JSON](../../data/mcps/get-mcp-ads--google-analytics-mcp-server.json)

**27 tools:** 27 GA4, 0 other-service or server-support tools. Reviewed source: [`f59104fd0edd`](https://github.com/get-mcp-ads/google-analytics-mcp-server/tree/f59104fd0edd96807944df94657e337e17c989be).

Descriptions and parameter schemas come from the registered source definitions. Generated schemas are reconstructed from annotations or validators; live `tools/list` and authenticated API calls were not run. Loose objects remain loose.

<details>
<summary>Exposure and compatibility notes</summary>

- Source review only; no upstream execution, tools/list or live requests. All 27 tools register unconditionally, with no permission tiers or optional module switch.
- CLI startup requires nonempty OAuth client ID, client secret and refresh token; package requires Node >=22.12.0.
- Descriptions preserve literal registered strings, including catalog-count claims; these are not treated as implementation inventory counts.
- Input schemas reconstructed from Zod; objects strip unknown keys and represented with additionalProperties=false. Arbitrary z.record(z.unknown()) fields retain open JSON. Custom refine predicates are noted per tool and not represented as invented standard JSON Schema constraints.
- installToolQuality adds top-level shared parameter descriptions, read-only annotations and structured result envelope without changing handler calls.

</details>

## Tools

| Tool | Scope | Effect |
| --- | --- | --- |
| [`ga4_health_check`](#ga4_health_check) | GA4 | read |
| [`ga4_list_properties`](#ga4_list_properties) | GA4 | read |
| [`ga4_run_report`](#ga4_run_report) | GA4 | read |
| [`ga4_run_realtime_report`](#ga4_run_realtime_report) | GA4 | read |
| [`ga4_get_metadata`](#ga4_get_metadata) | GA4 | read |
| [`ga4_get_custom_definitions`](#ga4_get_custom_definitions) | GA4 | read |
| [`ga4_get_key_events`](#ga4_get_key_events) | GA4 | read |
| [`ga4_get_ecommerce_diagnostics`](#ga4_get_ecommerce_diagnostics) | GA4 | read |
| [`ga4_get_event_parameters`](#ga4_get_event_parameters) | GA4 | read |
| [`ga4_run_funnel_recipe`](#ga4_run_funnel_recipe) | GA4 | read |
| [`ga4_get_audience_export_diagnostics`](#ga4_get_audience_export_diagnostics) | GA4 | read |
| [`ga4_get_audience_diagnostics`](#ga4_get_audience_diagnostics) | GA4 | read |
| [`ga4_get_bigquery_export_diagnostics`](#ga4_get_bigquery_export_diagnostics) | GA4 | read |
| [`ga4_get_server_side_tagging_diagnostics`](#ga4_get_server_side_tagging_diagnostics) | GA4 | read |
| [`ga4_run_advanced_funnel_report`](#ga4_run_advanced_funnel_report) | GA4 | read |
| [`ga4_get_channel_groups`](#ga4_get_channel_groups) | GA4 | read |
| [`ga4_validate_query`](#ga4_validate_query) | GA4 | local |
| [`ga4_run_pivot_report`](#ga4_run_pivot_report) | GA4 | read |
| [`ga4_batch_run_reports`](#ga4_batch_run_reports) | GA4 | read |
| [`ga4_batch_run_pivot_reports`](#ga4_batch_run_pivot_reports) | GA4 | read |
| [`ga4_check_compatibility`](#ga4_check_compatibility) | GA4 | read |
| [`ga4_get_property_quotas_snapshot`](#ga4_get_property_quotas_snapshot) | GA4 | read |
| [`ga4_list_accounts`](#ga4_list_accounts) | GA4 | read |
| [`ga4_list_admin_resources`](#ga4_list_admin_resources) | GA4 | read |
| [`ga4_get_property_configuration`](#ga4_get_property_configuration) | GA4 | read |
| [`ga4_list_audience_exports`](#ga4_list_audience_exports) | GA4 | read |
| [`ga4_query_audience_export`](#ga4_query_audience_export) | GA4 | read |

## ga4_health_check

Checks credential presence, lists accessible properties, chooses explicit/default/first property, then reads property details and Data API metadata. Reports partial failures and actionable diagnostics without exposing tokens.

<details>
<summary>Full registered description</summary>

```text
Read-only GA4 health check. Verifies configured credentials, accessible properties, and metadata/property access without exposing OAuth tokens.
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
      "description": "Optional property ID to check metadata and property details for"
    }
  },
  "required": [],
  "additionalProperties": false
}
```

</details>

Source: [src/platforms/ga4/tools.ts:536](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/tools.ts#L536-L664) · [src/platforms/ga4/client.ts:516](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/client.ts#L516-L525) · [src/platforms/ga4/client.ts:529](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/client.ts#L529-L538) · [src/platforms/ga4/client.ts:253](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/client.ts#L253-L322) · [src/tool-quality.ts:46](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/tool-quality.ts#L46-L58) · [src/platforms/ga4/tools.ts:29](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/tools.ts#L29-L53) · [src/parameter-descriptions.ts:1](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/parameter-descriptions.ts#L1-L235).

## ga4_list_properties

Lists Admin accountSummaries with pagination, extracts property summaries, then attempts property GET enrichment for timezone/currency with per-property failure tolerance.

<details>
<summary>Full registered description</summary>

```text
List all GA4 properties accessible with the current credentials. Returns property ID, display name, timezone, and currency.
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

Source: [src/platforms/ga4/tools.ts:667](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/tools.ts#L667-L677) · [src/platforms/ga4/client.ts:253](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/client.ts#L253-L322) · [src/tool-quality.ts:46](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/tool-quality.ts#L46-L58) · [src/platforms/ga4/tools.ts:29](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/tools.ts#L29-L53) · [src/parameter-descriptions.ts:1](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/parameter-descriptions.ts#L1-L235).

## ga4_run_report

Plans selected catalog/API fields and calculated metrics, validates local compatibility, then runs Core report and flattens rows; enriches calculated metrics locally. Explicit limit gives one page; autoPaginate removes limit and client reads 250000-row offset pages until reported rowCount or an empty page.

<details>
<summary>Full registered description</summary>

```text
Run a GA4 analytics report with intelligent query planning. Supports 52 metrics, 63 dimensions, auto-pagination.
Use ga4://metrics and ga4://dimensions resources for available fields. Max 9 dimensions + 10 metrics per request.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `propertyId` | Yes | string | Not declared |
| `metrics` | Yes | array of string | Not declared |
| `dimensions` | No | array of string | Not declared |
| `startDate` | No | string | Not declared |
| `endDate` | No | string | Not declared |
| `datePreset` | No | string | Not declared |
| `orderBy` | No | string | Not declared |
| `orderDirection` | No | string | "DESC" |
| `limit` | No | integer | 1000 |
| `offset` | No | integer | Not declared |
| `autoPaginate` | No | boolean | false |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "propertyId": {
      "type": "string",
      "description": "GA4 property ID (numeric, e.g., 123456789)"
    },
    "metrics": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "minItems": 1,
      "description": "Metric keys (e.g., sessions, activeUsers, totalRevenue)"
    },
    "dimensions": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Dimension keys (e.g., date, sessionSource, country)"
    },
    "startDate": {
      "type": "string",
      "description": "Start date YYYY-MM-DD or relative (7daysAgo, yesterday)"
    },
    "endDate": {
      "type": "string",
      "description": "End date YYYY-MM-DD or relative (today, yesterday)"
    },
    "datePreset": {
      "type": "string",
      "enum": [
        "today",
        "yesterday",
        "last7days",
        "last28days",
        "last30days",
        "last90days",
        "last12months",
        "thisMonth",
        "lastMonth",
        "thisYear"
      ],
      "description": "Named reporting period. Use the custom date range when you need exact start and end dates."
    },
    "orderBy": {
      "type": "string",
      "description": "Metric or dimension key to sort by"
    },
    "orderDirection": {
      "type": "string",
      "enum": [
        "ASC",
        "DESC"
      ],
      "default": "DESC",
      "description": "Sort direction for the selected ordering field."
    },
    "limit": {
      "type": "integer",
      "minimum": 1,
      "maximum": 250000,
      "default": 1000,
      "description": "Maximum number of returned items or rows. The declared bounds and default apply; use pagination for additional results."
    },
    "offset": {
      "type": "integer",
      "minimum": 0,
      "description": "Optional 0-based row offset for explicit pagination."
    },
    "autoPaginate": {
      "type": "boolean",
      "default": false,
      "description": "When true, omit the limit so the GA4 client paginates through all rows using offset."
    }
  },
  "required": [
    "propertyId",
    "metrics"
  ],
  "additionalProperties": false
}
```

</details>

- Explicit startDate/endDate only used together; otherwise planner resolves datePreset/default. Auto-pagination debug requestCount remains 1 even when several report requests occur.

Source: [src/platforms/ga4/tools.ts:680](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/tools.ts#L680-L745) · [src/platforms/ga4/client.ts:331](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/client.ts#L331-L400) · [src/tool-quality.ts:46](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/tool-quality.ts#L46-L58) · [src/platforms/ga4/tools.ts:29](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/tools.ts#L29-L53) · [src/parameter-descriptions.ts:1](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/parameter-descriptions.ts#L1-L235) · [src/platforms/ga4/query-planner.ts:43](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/query-planner.ts#L43-L185).

## ga4_run_realtime_report

Maps catalog field names and forwards raw filters, orderings, minute ranges and selected fields to realtime reporting, requesting quota state; returns flattened data and limited-field warning.

<details>
<summary>Full registered description</summary>

```text
Run a read-only GA4 Data API realtime report. Realtime supports only a limited subset of dimensions and metrics.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `propertyId` | Yes | string | Not declared |
| `metrics` | No | array of string | ["activeUsers"] |
| `dimensions` | No | array of string | Not declared |
| `dimensionFilter` | No | object | Not declared |
| `metricFilter` | No | object | Not declared |
| `minuteRanges` | No | array of object | Not declared |
| `orderBys` | No | array of object | Not declared |
| `limit` | No | integer | 100 |
| `keepEmptyRows` | No | boolean | false |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "propertyId": {
      "type": "string",
      "description": "GA4 property ID (numeric, e.g., 123456789)"
    },
    "metrics": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "minItems": 1,
      "maxItems": 10,
      "default": [
        "activeUsers"
      ],
      "description": "Realtime metric API names, e.g. activeUsers, eventCount"
    },
    "dimensions": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "maxItems": 9,
      "description": "Realtime dimension API names, e.g. eventName, city, deviceCategory"
    },
    "dimensionFilter": {
      "type": "object",
      "additionalProperties": {},
      "description": "Native realtime-compatible GA4 FilterExpression JSON."
    },
    "metricFilter": {
      "type": "object",
      "additionalProperties": {},
      "description": "Native realtime-compatible GA4 FilterExpression JSON."
    },
    "minuteRanges": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "startMinutesAgo": {
            "type": "integer",
            "minimum": 0,
            "maximum": 59
          },
          "endMinutesAgo": {
            "type": "integer",
            "minimum": 0,
            "maximum": 59
          }
        },
        "required": [],
        "additionalProperties": false
      },
      "maxItems": 2,
      "description": "Optional named realtime minute ranges; zero is the current minute."
    },
    "orderBys": {
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": {}
      },
      "maxItems": 10,
      "description": "Native GA4 OrderBy JSON."
    },
    "limit": {
      "type": "integer",
      "minimum": 1,
      "maximum": 10000,
      "default": 100,
      "description": "Maximum number of returned items or rows. The declared bounds and default apply; use pagination for additional results."
    },
    "keepEmptyRows": {
      "type": "boolean",
      "default": false,
      "description": "Keep provider rows whose selected metrics are all zero, where supported."
    }
  },
  "required": [
    "propertyId"
  ],
  "additionalProperties": false
}
```

</details>

Source: [src/platforms/ga4/tools.ts:748](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/tools.ts#L748-L792) · [src/platforms/ga4/client.ts:404](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/client.ts#L404-L419) · [src/tool-quality.ts:46](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/tool-quality.ts#L46-L58) · [src/platforms/ga4/tools.ts:29](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/tools.ts#L29-L53) · [src/parameter-descriptions.ts:1](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/parameter-descriptions.ts#L1-L235).

## ga4_get_metadata

Returns the property Data API metadata response.

<details>
<summary>Full registered description</summary>

```text
Get the complete list of dimensions and metrics available for a specific GA4 property. Useful for discovering custom dimensions/metrics.
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
      "description": "GA4 property ID (numeric, e.g., 123456789)"
    }
  },
  "required": [
    "propertyId"
  ],
  "additionalProperties": false
}
```

</details>

Source: [src/platforms/ga4/tools.ts:795](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/tools.ts#L795-L805) · [src/platforms/ga4/client.ts:516](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/client.ts#L516-L525) · [src/tool-quality.ts:46](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/tool-quality.ts#L46-L58) · [src/platforms/ga4/tools.ts:29](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/tools.ts#L29-L53) · [src/parameter-descriptions.ts:1](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/parameter-descriptions.ts#L1-L235).

## ga4_get_custom_definitions

Extracts reportable custom dimensions/metrics from Data API metadata using customDefinition flags and customEvent/customUser/customItem prefixes; does not call Admin custom-definition endpoints.

<details>
<summary>Full registered description</summary>

```text
List custom dimensions and custom metrics exposed by GA4 Data API metadata. Read-only fallback for custom definition inventory.
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
      "description": "GA4 property ID (numeric, e.g., 123456789)"
    }
  },
  "required": [
    "propertyId"
  ],
  "additionalProperties": false
}
```

</details>

Source: [src/platforms/ga4/tools.ts:808](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/tools.ts#L808-L836) · [src/platforms/ga4/client.ts:516](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/client.ts#L516-L525) · [src/tool-quality.ts:46](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/tool-quality.ts#L46-L58) · [src/platforms/ga4/tools.ts:29](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/tools.ts#L29-L53) · [src/parameter-descriptions.ts:1](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/parameter-descriptions.ts#L1-L235).

## ga4_get_key_events

Reads metadata to prefer isKeyEvent/keyEvents with legacy isConversionEvent/conversions fallbacks, reports eventName plus flag and metric, then retries eventName plus positive metric when no rows. Returns observed names/counts, not Admin configuration.

<details>
<summary>Full registered description</summary>

```text
Inventory GA4 key events/conversions using metadata-aware Data API reports. Returns best-effort event names and counts.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `propertyId` | Yes | string | Not declared |
| `startDate` | No | string | Not declared |
| `endDate` | No | string | Not declared |
| `datePreset` | No | string | "last28days" |
| `limit` | No | integer | 100 |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "propertyId": {
      "type": "string",
      "description": "GA4 property ID (numeric, e.g., 123456789)"
    },
    "startDate": {
      "type": "string",
      "description": "Start date YYYY-MM-DD or relative (7daysAgo, yesterday)"
    },
    "endDate": {
      "type": "string",
      "description": "End date YYYY-MM-DD or relative (today, yesterday)"
    },
    "datePreset": {
      "type": "string",
      "enum": [
        "today",
        "yesterday",
        "last7days",
        "last28days",
        "last30days",
        "last90days",
        "last12months",
        "thisMonth",
        "lastMonth",
        "thisYear"
      ],
      "default": "last28days",
      "description": "Named reporting period. Use the custom date range when you need exact start and end dates."
    },
    "limit": {
      "type": "integer",
      "minimum": 1,
      "maximum": 1000,
      "default": 100,
      "description": "Maximum number of returned items or rows. The declared bounds and default apply; use pagination for additional results."
    }
  },
  "required": [
    "propertyId"
  ],
  "additionalProperties": false
}
```

</details>

Source: [src/platforms/ga4/tools.ts:839](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/tools.ts#L839-L931) · [src/platforms/ga4/client.ts:516](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/client.ts#L516-L525) · [src/platforms/ga4/client.ts:331](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/client.ts#L331-L400) · [src/tool-quality.ts:46](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/tool-quality.ts#L46-L58) · [src/platforms/ga4/tools.ts:29](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/tools.ts#L29-L53) · [src/parameter-descriptions.ts:1](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/parameter-descriptions.ts#L1-L235).

## ga4_get_ecommerce_diagnostics

Best-effort metadata lookup; reports selected ecommerce event counts, separately requests available aggregate revenue/purchase/item metrics, and requests item-level dimensions/metrics. Computes coverage and warnings while retaining partial successes.

<details>
<summary>Full registered description</summary>

```text
Read-only ecommerce coverage diagnostics for core ecommerce events, revenue metrics, and item-level reporting over a date range.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `propertyId` | Yes | string | Not declared |
| `startDate` | No | string | Not declared |
| `endDate` | No | string | Not declared |
| `datePreset` | No | string | "last28days" |
| `limit` | No | integer | 100 |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "propertyId": {
      "type": "string",
      "description": "GA4 property ID (numeric, e.g., 123456789)"
    },
    "startDate": {
      "type": "string",
      "description": "Start date YYYY-MM-DD or relative (7daysAgo, yesterday)"
    },
    "endDate": {
      "type": "string",
      "description": "End date YYYY-MM-DD or relative (today, yesterday)"
    },
    "datePreset": {
      "type": "string",
      "enum": [
        "today",
        "yesterday",
        "last7days",
        "last28days",
        "last30days",
        "last90days",
        "last12months",
        "thisMonth",
        "lastMonth",
        "thisYear"
      ],
      "default": "last28days",
      "description": "Named reporting period. Use the custom date range when you need exact start and end dates."
    },
    "limit": {
      "type": "integer",
      "minimum": 1,
      "maximum": 1000,
      "default": 100,
      "description": "Maximum number of returned items or rows. The declared bounds and default apply; use pagination for additional results."
    }
  },
  "required": [
    "propertyId"
  ],
  "additionalProperties": false
}
```

</details>

Source: [src/platforms/ga4/tools.ts:934](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/tools.ts#L934-L1082) · [src/platforms/ga4/client.ts:516](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/client.ts#L516-L525) · [src/platforms/ga4/client.ts:331](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/client.ts#L331-L400) · [src/tool-quality.ts:46](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/tool-quality.ts#L46-L58) · [src/platforms/ga4/tools.ts:29](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/tools.ts#L29-L53) · [src/parameter-descriptions.ts:1](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/parameter-descriptions.ts#L1-L235).

## ga4_get_event_parameters

Reads metadata for registered event-scoped custom definitions and samples eventName/eventCount reports, optionally filtering event names. Cannot enumerate unregistered raw parameters or values.

<details>
<summary>Full registered description</summary>

```text
Best-effort event parameter inventory from GA4 metadata plus event reports. Documents Data API limitations for raw parameters.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `propertyId` | Yes | string | Not declared |
| `eventNames` | No | array of string | Not declared |
| `startDate` | No | string | Not declared |
| `endDate` | No | string | Not declared |
| `datePreset` | No | string | "last28days" |
| `limit` | No | integer | 50 |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "propertyId": {
      "type": "string",
      "description": "GA4 property ID (numeric, e.g., 123456789)"
    },
    "eventNames": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Optional event names to sample, e.g. purchase, add_to_cart"
    },
    "startDate": {
      "type": "string",
      "description": "Start date YYYY-MM-DD or relative (7daysAgo, yesterday)"
    },
    "endDate": {
      "type": "string",
      "description": "End date YYYY-MM-DD or relative (today, yesterday)"
    },
    "datePreset": {
      "type": "string",
      "enum": [
        "today",
        "yesterday",
        "last7days",
        "last28days",
        "last30days",
        "last90days",
        "last12months",
        "thisMonth",
        "lastMonth",
        "thisYear"
      ],
      "default": "last28days",
      "description": "Named reporting period. Use the custom date range when you need exact start and end dates."
    },
    "limit": {
      "type": "integer",
      "minimum": 1,
      "maximum": 1000,
      "default": 50,
      "description": "Maximum number of returned items or rows. The declared bounds and default apply; use pagination for additional results."
    }
  },
  "required": [
    "propertyId"
  ],
  "additionalProperties": false
}
```

</details>

Source: [src/platforms/ga4/tools.ts:1085](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/tools.ts#L1085-L1147) · [src/platforms/ga4/client.ts:516](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/client.ts#L516-L525) · [src/platforms/ga4/client.ts:331](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/client.ts#L331-L400) · [src/tool-quality.ts:46](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/tool-quality.ts#L46-L58) · [src/platforms/ga4/tools.ts:29](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/tools.ts#L29-L53) · [src/parameter-descriptions.ts:1](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/parameter-descriptions.ts#L1-L235).

## ga4_run_funnel_recipe

Runs one Core aggregate report per step, combining eventName EXACT and pagePath string filters with AND. Computes independent counts, ratios and dropoffs locally.

<details>
<summary>Full registered description</summary>

```text
Run a read-only configurable funnel recipe using one GA4 report per eventName/pagePath step and return simple step counts.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `propertyId` | Yes | string | Not declared |
| `steps` | Yes | array of object | Not declared |
| `metric` | No | string | "activeUsers" |
| `startDate` | No | string | Not declared |
| `endDate` | No | string | Not declared |
| `datePreset` | No | string | "last28days" |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "propertyId": {
      "type": "string",
      "description": "GA4 property ID (numeric, e.g., 123456789)"
    },
    "steps": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "Optional display name for this funnel step"
          },
          "eventName": {
            "type": "string",
            "description": "GA4 eventName to count for this step"
          },
          "pagePath": {
            "type": "string",
            "description": "GA4 pagePath to count for this step"
          },
          "matchType": {
            "type": "string",
            "enum": [
              "EXACT",
              "BEGINS_WITH",
              "ENDS_WITH",
              "CONTAINS",
              "FULL_REGEXP",
              "PARTIAL_REGEXP"
            ],
            "default": "EXACT",
            "description": "String match type for pagePath. eventName always uses EXACT."
          }
        },
        "required": [],
        "additionalProperties": false
      },
      "minItems": 2,
      "maxItems": 10,
      "description": "Ordered funnel steps. Each step needs eventName or pagePath."
    },
    "metric": {
      "type": "string",
      "enum": [
        "activeUsers",
        "totalUsers",
        "sessions",
        "eventCount",
        "screenPageViews"
      ],
      "default": "activeUsers",
      "description": "Metric used for the analysis; use a name from the platform metric catalogue."
    },
    "startDate": {
      "type": "string",
      "description": "Start date YYYY-MM-DD or relative (7daysAgo, yesterday)"
    },
    "endDate": {
      "type": "string",
      "description": "End date YYYY-MM-DD or relative (today, yesterday)"
    },
    "datePreset": {
      "type": "string",
      "enum": [
        "today",
        "yesterday",
        "last7days",
        "last28days",
        "last30days",
        "last90days",
        "last12months",
        "thisMonth",
        "lastMonth",
        "thisYear"
      ],
      "default": "last28days",
      "description": "Named reporting period. Use the custom date range when you need exact start and end dates."
    }
  },
  "required": [
    "propertyId",
    "steps"
  ],
  "additionalProperties": false
}
```

</details>

- Steps are counted independently; results do not track user sequences or deduplicate across steps. Zod refinement requires a truthy eventName or pagePath per step.

Source: [src/platforms/ga4/tools.ts:1150](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/tools.ts#L1150-L1228) · [src/platforms/ga4/client.ts:331](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/client.ts#L331-L400) · [src/tool-quality.ts:46](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/tool-quality.ts#L46-L58) · [src/platforms/ga4/tools.ts:29](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/tools.ts#L29-L53) · [src/parameter-descriptions.ts:1](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/parameter-descriptions.ts#L1-L235).

## ga4_get_audience_export_diagnostics

Lists existing export snapshots and summarizes states; optionally gets one export and queries a small sample. Samples only when resource name and includeRowSample are provided; identifier columns redact unless opted in. Creates no export.

<details>
<summary>Full registered description</summary>

```text
Read-only Audience Export diagnostics. Lists existing audience exports, state counts, and optionally samples rows from an existing export.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `propertyId` | Yes | string | Not declared |
| `audienceExportName` | No | string | Not declared |
| `pageSize` | No | integer | 100 |
| `includeRowSample` | No | boolean | false |
| `sampleLimit` | No | integer | 5 |
| `includePersonalIdentifiers` | No | boolean | false |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "propertyId": {
      "type": "string",
      "description": "GA4 property ID (numeric, e.g., 123456789)"
    },
    "audienceExportName": {
      "type": "string",
      "description": "Optional resource name, e.g. properties/123456789/audienceExports/abc123"
    },
    "pageSize": {
      "type": "integer",
      "minimum": 1,
      "maximum": 200,
      "default": 100,
      "description": "Maximum items requested per page. Follow the returned pagination information for remaining results."
    },
    "includeRowSample": {
      "type": "boolean",
      "default": false,
      "description": "If true, query a small row sample from audienceExportName. Can include user-level export dimensions."
    },
    "sampleLimit": {
      "type": "integer",
      "minimum": 1,
      "maximum": 10,
      "default": 5,
      "description": "Maximum records included in the diagnostic sample."
    },
    "includePersonalIdentifiers": {
      "type": "boolean",
      "default": false,
      "description": "Explicitly include user/device identifiers in the optional sample. False redacts them by default."
    }
  },
  "required": [
    "propertyId"
  ],
  "additionalProperties": false
}
```

</details>

- Shared listPagedRecords stops after 50 pages; a remaining page token is not returned.

Source: [src/platforms/ga4/tools.ts:1231](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/tools.ts#L1231-L1299) · [src/platforms/ga4/client.ts:600](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/client.ts#L600-L607) · [src/platforms/ga4/client.ts:587](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/client.ts#L587-L596) · [src/platforms/ga4/client.ts:611](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/client.ts#L611-L624) · [src/tool-quality.ts:46](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/tool-quality.ts#L46-L58) · [src/platforms/ga4/tools.ts:29](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/tools.ts#L29-L53) · [src/parameter-descriptions.ts:1](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/parameter-descriptions.ts#L1-L235).

## ga4_get_audience_diagnostics

Independently lists Admin audiences and recurring audience lists; optionally gets one recurring list. Uses metadata and audienceName/activeUsers Core report for observed traffic fallback, and returns partial errors as warnings. Definitions included only when requested.

<details>
<summary>Full registered description</summary>

```text
Read-only audience diagnostics from Admin API audiences, Data API recurring audience lists, and observed audienceName report fallback.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `propertyId` | Yes | string | Not declared |
| `recurringAudienceListName` | No | string | Not declared |
| `includeDefinitions` | No | boolean | false |
| `startDate` | No | string | Not declared |
| `endDate` | No | string | Not declared |
| `datePreset` | No | string | "last28days" |
| `limit` | No | integer | 100 |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "propertyId": {
      "type": "string",
      "description": "GA4 property ID (numeric, e.g., 123456789)"
    },
    "recurringAudienceListName": {
      "type": "string",
      "description": "Optional resource name, e.g. properties/123456789/recurringAudienceLists/abc123"
    },
    "includeDefinitions": {
      "type": "boolean",
      "default": false,
      "description": "Include full Admin API audience definitions when available"
    },
    "startDate": {
      "type": "string",
      "description": "Start date YYYY-MM-DD or relative (7daysAgo, yesterday)"
    },
    "endDate": {
      "type": "string",
      "description": "End date YYYY-MM-DD or relative (today, yesterday)"
    },
    "datePreset": {
      "type": "string",
      "enum": [
        "today",
        "yesterday",
        "last7days",
        "last28days",
        "last30days",
        "last90days",
        "last12months",
        "thisMonth",
        "lastMonth",
        "thisYear"
      ],
      "default": "last28days",
      "description": "Named reporting period. Use the custom date range when you need exact start and end dates."
    },
    "limit": {
      "type": "integer",
      "minimum": 1,
      "maximum": 1000,
      "default": 100,
      "description": "Maximum number of returned items or rows. The declared bounds and default apply; use pagination for additional results."
    }
  },
  "required": [
    "propertyId"
  ],
  "additionalProperties": false
}
```

</details>

- Shared listPagedRecords stops after 50 pages; a remaining page token is not returned.

Source: [src/platforms/ga4/tools.ts:1302](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/tools.ts#L1302-L1385) · [src/platforms/ga4/client.ts:516](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/client.ts#L516-L525) · [src/platforms/ga4/client.ts:654](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/client.ts#L654-L661) · [src/platforms/ga4/client.ts:628](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/client.ts#L628-L637) · [src/platforms/ga4/client.ts:641](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/client.ts#L641-L650) · [src/platforms/ga4/client.ts:331](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/client.ts#L331-L400) · [src/tool-quality.ts:46](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/tool-quality.ts#L46-L58) · [src/platforms/ga4/tools.ts:29](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/tools.ts#L29-L53) · [src/parameter-descriptions.ts:1](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/parameter-descriptions.ts#L1-L235).

## ga4_get_bigquery_export_diagnostics

Reads Admin BigQuery links and optionally data streams; summarizes export modes, dataset location, exclusions and stream coverage. Does not query BigQuery tables or assess freshness.

<details>
<summary>Full registered description</summary>

```text
Detect GA4 BigQuery export links and diagnose export modes, stream coverage, excluded events, and dataset location.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `propertyId` | Yes | string | Not declared |
| `includeDataStreams` | No | boolean | true |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "propertyId": {
      "type": "string",
      "description": "GA4 property ID (numeric, e.g., 123456789)"
    },
    "includeDataStreams": {
      "type": "boolean",
      "default": true,
      "description": "Include data stream summaries to compare against BigQuery exportStreams"
    }
  },
  "required": [
    "propertyId"
  ],
  "additionalProperties": false
}
```

</details>

- Shared listPagedRecords stops after 50 pages; a remaining page token is not returned.

Source: [src/platforms/ga4/tools.ts:1388](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/tools.ts#L1388-L1455) · [src/platforms/ga4/client.ts:669](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/client.ts#L669-L678) · [src/platforms/ga4/client.ts:682](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/client.ts#L682-L691) · [src/tool-quality.ts:46](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/tool-quality.ts#L46-L58) · [src/platforms/ga4/tools.ts:29](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/tools.ts#L29-L53) · [src/parameter-descriptions.ts:1](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/parameter-descriptions.ts#L1-L235).

## ga4_get_server_side_tagging_diagnostics

Lists streams and Measurement Protocol secret metadata with secretValue redacted; optionally gets web-stream enhanced measurement/data redaction settings and event create/edit rules. Infers server-to-server signals and returns per-stream warnings, without inspecting GTM routing.

<details>
<summary>Full registered description</summary>

```text
Best-effort read-only server-side tagging diagnostics from data streams, Measurement Protocol secrets, event rules, and stream settings.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `propertyId` | Yes | string | Not declared |
| `includeSettings` | No | boolean | true |
| `includeRules` | No | boolean | true |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "propertyId": {
      "type": "string",
      "description": "GA4 property ID (numeric, e.g., 123456789)"
    },
    "includeSettings": {
      "type": "boolean",
      "default": true,
      "description": "Fetch enhanced measurement and data redaction settings for web streams"
    },
    "includeRules": {
      "type": "boolean",
      "default": true,
      "description": "Fetch event create/edit rules for web streams"
    }
  },
  "required": [
    "propertyId"
  ],
  "additionalProperties": false
}
```

</details>

- Shared listPagedRecords stops after 50 pages; a remaining page token is not returned.

Source: [src/platforms/ga4/tools.ts:1458](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/tools.ts#L1458-L1567) · [src/platforms/ga4/client.ts:720](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/client.ts#L720-L727) · [src/platforms/ga4/client.ts:709](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/client.ts#L709-L716) · [src/platforms/ga4/client.ts:682](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/client.ts#L682-L691) · [src/platforms/ga4/client.ts:731](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/client.ts#L731-L740) · [src/platforms/ga4/client.ts:744](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/client.ts#L744-L753) · [src/platforms/ga4/client.ts:695](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/client.ts#L695-L705) · [src/tool-quality.ts:46](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/tool-quality.ts#L46-L58) · [src/platforms/ga4/tools.ts:29](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/tools.ts#L29-L53) · [src/parameter-descriptions.ts:1](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/parameter-descriptions.ts#L1-L235).

## ga4_run_advanced_funnel_report

Builds native v1alpha funnel event/field expressions and sequence/timing constraints, optional breakdown and next-action fields, then runs funnel report. On any endpoint failure, default fallback runs independent activeUsers Core counts for steps; disabling fallback rethrows.

<details>
<summary>Full registered description</summary>

```text
Run the GA4 Data API v1alpha runFunnelReport endpoint with optional breakdown/next-action, falling back to read-only step counts if unavailable.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `propertyId` | Yes | string | Not declared |
| `steps` | Yes | array of object | Not declared |
| `isOpenFunnel` | No | boolean | false |
| `visualizationType` | No | string | "STANDARD_FUNNEL" |
| `breakdownDimension` | No | string | Not declared |
| `breakdownLimit` | No | integer | 10 |
| `nextActionDimension` | No | string | Not declared |
| `nextActionLimit` | No | integer | 10 |
| `startDate` | No | string | Not declared |
| `endDate` | No | string | Not declared |
| `datePreset` | No | string | "last28days" |
| `limit` | No | integer | 10000 |
| `fallbackToStepCounts` | No | boolean | true |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "propertyId": {
      "type": "string",
      "description": "GA4 property ID (numeric, e.g., 123456789)"
    },
    "steps": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "Optional display name for this funnel step"
          },
          "eventName": {
            "type": "string",
            "description": "GA4 event name matched by a FunnelEventFilter"
          },
          "pagePath": {
            "type": "string",
            "description": "Shortcut for fieldName=pagePath string filter"
          },
          "fieldName": {
            "type": "string",
            "description": "Optional GA4 field name for a FunnelFieldFilter, e.g. pagePath, pageTitle, deviceCategory"
          },
          "fieldValue": {
            "type": "string",
            "description": "String value to match for fieldName"
          },
          "matchType": {
            "type": "string",
            "enum": [
              "EXACT",
              "BEGINS_WITH",
              "ENDS_WITH",
              "CONTAINS",
              "FULL_REGEXP",
              "PARTIAL_REGEXP"
            ],
            "default": "EXACT",
            "description": "String match type for pagePath or fieldName"
          },
          "isDirectlyFollowedBy": {
            "type": "boolean",
            "description": "Require this step to directly follow the previous step"
          },
          "withinSecondsFromPriorStep": {
            "type": "integer",
            "minimum": 1,
            "maximum": 2592000,
            "description": "Maximum seconds from the prior step"
          }
        },
        "required": [],
        "additionalProperties": false
      },
      "minItems": 2,
      "maxItems": 10,
      "description": "Ordered funnel steps using eventName, pagePath, or fieldName+fieldValue"
    },
    "isOpenFunnel": {
      "type": "boolean",
      "default": false,
      "description": "Allow users to enter at any funnel step instead of requiring the first step."
    },
    "visualizationType": {
      "type": "string",
      "enum": [
        "STANDARD_FUNNEL",
        "TRENDED_FUNNEL"
      ],
      "default": "STANDARD_FUNNEL",
      "description": "Supported funnel visualization mode."
    },
    "breakdownDimension": {
      "type": "string",
      "description": "Optional breakdown dimension, e.g. deviceCategory or sessionDefaultChannelGroup"
    },
    "breakdownLimit": {
      "type": "integer",
      "minimum": 1,
      "maximum": 50,
      "default": 10,
      "description": "Maximum breakdown values to include in the funnel response."
    },
    "nextActionDimension": {
      "type": "string",
      "description": "Optional next action dimension, commonly eventName"
    },
    "nextActionLimit": {
      "type": "integer",
      "minimum": 1,
      "maximum": 50,
      "default": 10,
      "description": "Maximum next actions returned for each funnel step."
    },
    "startDate": {
      "type": "string",
      "description": "Start date YYYY-MM-DD or relative (7daysAgo, yesterday)"
    },
    "endDate": {
      "type": "string",
      "description": "End date YYYY-MM-DD or relative (today, yesterday)"
    },
    "datePreset": {
      "type": "string",
      "enum": [
        "today",
        "yesterday",
        "last7days",
        "last28days",
        "last30days",
        "last90days",
        "last12months",
        "thisMonth",
        "lastMonth",
        "thisYear"
      ],
      "default": "last28days",
      "description": "Named reporting period. Use the custom date range when you need exact start and end dates."
    },
    "limit": {
      "type": "integer",
      "minimum": 1,
      "maximum": 250000,
      "default": 10000,
      "description": "Maximum number of returned items or rows. The declared bounds and default apply; use pagination for additional results."
    },
    "fallbackToStepCounts": {
      "type": "boolean",
      "default": true,
      "description": "If the advanced funnel is unavailable, return independent step counts with the limitation made explicit."
    }
  },
  "required": [
    "propertyId",
    "steps"
  ],
  "additionalProperties": false
}
```

</details>

- Zod refinement requires eventName, pagePath, or both fieldName and fieldValue per step. Fallback ignores sequence, timing, breakdown and next-action semantics.

Source: [src/platforms/ga4/tools.ts:1570](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/tools.ts#L1570-L1672) · [src/platforms/ga4/client.ts:493](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/client.ts#L493-L508) · [src/platforms/ga4/client.ts:331](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/client.ts#L331-L400) · [src/tool-quality.ts:46](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/tool-quality.ts#L46-L58) · [src/platforms/ga4/tools.ts:29](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/tools.ts#L29-L53) · [src/parameter-descriptions.ts:1](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/parameter-descriptions.ts#L1-L235) · [src/platforms/ga4/tools.ts:432](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/tools.ts#L432-L528).

## ga4_get_channel_groups

Returns Admin v1alpha channel groups; client uses one GET without auto-pagination.

<details>
<summary>Full registered description</summary>

```text
List custom channel groups defined for a GA4 property.
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
      "description": "GA4 property ID (numeric, e.g., 123456789)"
    }
  },
  "required": [
    "propertyId"
  ],
  "additionalProperties": false
}
```

</details>

Source: [src/platforms/ga4/tools.ts:1675](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/tools.ts#L1675-L1685) · [src/platforms/ga4/client.ts:762](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/client.ts#L762-L776) · [src/tool-quality.ts:46](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/tool-quality.ts#L46-L58) · [src/platforms/ga4/tools.ts:29](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/tools.ts#L29-L53) · [src/parameter-descriptions.ts:1](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/parameter-descriptions.ts#L1-L235).

## ga4_validate_query

Locally validates selected catalog metric/dimension combinations, field counts and ecommerce compatibility; no API calls.

<details>
<summary>Full registered description</summary>

```text
Validate a metric/dimension combination BEFORE executing. Checks max limits (9 dims, 10 metrics), ecommerce rules, and dimension compatibility.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `metrics` | Yes | array of string | Not declared |
| `dimensions` | No | array of string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "metrics": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "minItems": 1,
      "description": "Metric keys to validate"
    },
    "dimensions": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Dimension keys to validate"
    }
  },
  "required": [
    "metrics"
  ],
  "additionalProperties": false
}
```

</details>

Source: [src/platforms/ga4/tools.ts:1688](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/tools.ts#L1688-L1706) · [src/tool-quality.ts:46](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/tool-quality.ts#L46-L58) · [src/platforms/ga4/tools.ts:29](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/tools.ts#L29-L53) · [src/parameter-descriptions.ts:1](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/parameter-descriptions.ts#L1-L235).

## ga4_run_pivot_report

Maps names to native GA dimension/metric objects, validates pivot field declarations/uniqueness and cell budget, strips property from request body, runs native pivot report and returns raw and flattened rows.

<details>
<summary>Full registered description</summary>

```text
Run a read-only GA4 Data API pivot report with native filters, ordering, quota state, multiple date ranges, and up to 250,000 pivot cells. Every pivot requires an explicit limit.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `propertyId` | Yes | string | Not declared |
| `report` | Yes | object | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "propertyId": {
      "type": "string",
      "minLength": 1,
      "description": "Numeric GA4 property ID or properties/{id}."
    },
    "report": {
      "type": "object",
      "properties": {
        "dateRanges": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "startDate": {
                "type": "string",
                "minLength": 1,
                "description": "YYYY-MM-DD or a GA4 relative date such as 28daysAgo."
              },
              "endDate": {
                "type": "string",
                "minLength": 1,
                "description": "YYYY-MM-DD or a GA4 relative date such as today."
              }
            },
            "required": [
              "startDate",
              "endDate"
            ],
            "additionalProperties": false
          },
          "minItems": 1,
          "maxItems": 4
        },
        "dimensions": {
          "type": "array",
          "items": {
            "type": "string",
            "minLength": 1
          },
          "minItems": 1,
          "maxItems": 9
        },
        "metrics": {
          "type": "array",
          "items": {
            "type": "string",
            "minLength": 1
          },
          "minItems": 1,
          "maxItems": 10
        },
        "pivots": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "fieldNames": {
                "type": "array",
                "items": {
                  "type": "string",
                  "minLength": 1
                },
                "minItems": 1,
                "maxItems": 9
              },
              "orderBys": {
                "type": "array",
                "items": {
                  "type": "object",
                  "additionalProperties": {},
                  "description": "Native GA4 OrderBy JSON."
                },
                "maxItems": 10
              },
              "offset": {
                "type": "integer",
                "minimum": 0
              },
              "limit": {
                "type": "integer",
                "minimum": 1,
                "maximum": 250000
              },
              "metricAggregations": {
                "type": "array",
                "items": {
                  "type": "string",
                  "enum": [
                    "TOTAL",
                    "MINIMUM",
                    "MAXIMUM",
                    "COUNT"
                  ]
                },
                "maxItems": 4
              }
            },
            "required": [
              "fieldNames",
              "limit"
            ],
            "additionalProperties": false
          },
          "minItems": 1,
          "maxItems": 9
        },
        "dimensionFilter": {
          "type": "object",
          "additionalProperties": {},
          "description": "Native GA4 FilterExpression JSON."
        },
        "metricFilter": {
          "type": "object",
          "additionalProperties": {},
          "description": "Native GA4 FilterExpression JSON."
        },
        "currencyCode": {
          "type": "string",
          "minLength": 3,
          "maxLength": 3
        },
        "keepEmptyRows": {
          "type": "boolean"
        },
        "returnPropertyQuota": {
          "type": "boolean",
          "default": true
        },
        "cohortSpec": {
          "type": "object",
          "additionalProperties": {},
          "description": "Native GA4 CohortSpec JSON. Omit dateRanges for cohort requests."
        },
        "comparisons": {
          "type": "array",
          "items": {
            "type": "object",
            "additionalProperties": {}
          },
          "maxItems": 4,
          "description": "Native GA4 Comparison objects."
        }
      },
      "required": [
        "dimensions",
        "metrics",
        "pivots"
      ],
      "additionalProperties": false,
      "description": "Native GA4 report request object for this endpoint."
    }
  },
  "required": [
    "propertyId",
    "report"
  ],
  "additionalProperties": false
}
```

</details>

- Report refinement requires nonempty dateRanges or cohortSpec. Native filters, orderings, cohortSpec and comparisons are arbitrary JSON records; their internal GA API shapes are intentionally not validated.
- Handler requires pivot fields to be declared dimensions (except dateRange/comparisons), forbids repeated fields across pivots, and limits product of pivot limits to 250000.

Source: [src/platforms/ga4/surface-tools.ts:162](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/surface-tools.ts#L162-L180) · [src/platforms/ga4/client.ts:435](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/client.ts#L435-L449) · [src/tool-quality.ts:46](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/tool-quality.ts#L46-L58) · [src/platforms/ga4/surface-tools.ts:26](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/surface-tools.ts#L26-L78) · [src/parameter-descriptions.ts:1](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/parameter-descriptions.ts#L1-L235).

## ga4_batch_run_reports

Maps 1-5 report objects to native requests and submits one property-scoped batch call, returning flattened rows, metadata, aggregation and quota for each report. Does not client-auto-paginate batches.

<details>
<summary>Full registered description</summary>

```text
Run 1-5 independent read-only GA4 Core reports for the same property in one official Data API batch request.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `propertyId` | Yes | string | Not declared |
| `reports` | Yes | array of object | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "propertyId": {
      "type": "string",
      "minLength": 1,
      "description": "Numeric GA4 property ID or properties/{id}."
    },
    "reports": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "dateRanges": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "startDate": {
                  "type": "string",
                  "minLength": 1,
                  "description": "YYYY-MM-DD or a GA4 relative date such as 28daysAgo."
                },
                "endDate": {
                  "type": "string",
                  "minLength": 1,
                  "description": "YYYY-MM-DD or a GA4 relative date such as today."
                }
              },
              "required": [
                "startDate",
                "endDate"
              ],
              "additionalProperties": false
            },
            "minItems": 1,
            "maxItems": 4
          },
          "dimensions": {
            "type": "array",
            "items": {
              "type": "string",
              "minLength": 1
            },
            "maxItems": 9,
            "default": []
          },
          "metrics": {
            "type": "array",
            "items": {
              "type": "string",
              "minLength": 1
            },
            "minItems": 1,
            "maxItems": 10
          },
          "dimensionFilter": {
            "type": "object",
            "additionalProperties": {},
            "description": "Native GA4 FilterExpression JSON."
          },
          "metricFilter": {
            "type": "object",
            "additionalProperties": {},
            "description": "Native GA4 FilterExpression JSON."
          },
          "orderBys": {
            "type": "array",
            "items": {
              "type": "object",
              "additionalProperties": {},
              "description": "Native GA4 OrderBy JSON."
            },
            "maxItems": 10
          },
          "limit": {
            "type": "integer",
            "minimum": 1,
            "maximum": 250000
          },
          "offset": {
            "type": "integer",
            "minimum": 0
          },
          "keepEmptyRows": {
            "type": "boolean"
          },
          "metricAggregations": {
            "type": "array",
            "items": {
              "type": "string",
              "enum": [
                "TOTAL",
                "MINIMUM",
                "MAXIMUM",
                "COUNT"
              ]
            },
            "maxItems": 4
          },
          "currencyCode": {
            "type": "string",
            "minLength": 3,
            "maxLength": 3
          },
          "returnPropertyQuota": {
            "type": "boolean",
            "default": true
          },
          "cohortSpec": {
            "type": "object",
            "additionalProperties": {},
            "description": "Native GA4 CohortSpec JSON. Omit dateRanges for cohort requests."
          },
          "comparisons": {
            "type": "array",
            "items": {
              "type": "object",
              "additionalProperties": {}
            },
            "maxItems": 4,
            "description": "Native GA4 Comparison objects."
          }
        },
        "required": [
          "metrics"
        ],
        "additionalProperties": false
      },
      "minItems": 1,
      "maxItems": 5,
      "description": "Native GA4 report request objects to execute in one batch."
    }
  },
  "required": [
    "propertyId",
    "reports"
  ],
  "additionalProperties": false
}
```

</details>

- Report refinement requires nonempty dateRanges or cohortSpec. Native filters, orderings, cohortSpec and comparisons are arbitrary JSON records; their internal GA API shapes are intentionally not validated.

Source: [src/platforms/ga4/surface-tools.ts:182](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/surface-tools.ts#L182-L203) · [src/platforms/ga4/client.ts:420](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/client.ts#L420-L434) · [src/tool-quality.ts:46](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/tool-quality.ts#L46-L58) · [src/platforms/ga4/surface-tools.ts:26](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/surface-tools.ts#L26-L78) · [src/parameter-descriptions.ts:1](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/parameter-descriptions.ts#L1-L235).

## ga4_batch_run_pivot_reports

Maps 1-5 pivot report objects, validates each pivot configuration, and submits one batch request; returns raw reports and flattened rows.

<details>
<summary>Full registered description</summary>

```text
Run 1-5 independent read-only GA4 pivot reports for the same property in one official Data API batch request.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `propertyId` | Yes | string | Not declared |
| `reports` | Yes | array of object | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "propertyId": {
      "type": "string",
      "minLength": 1,
      "description": "Numeric GA4 property ID or properties/{id}."
    },
    "reports": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "dateRanges": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "startDate": {
                  "type": "string",
                  "minLength": 1,
                  "description": "YYYY-MM-DD or a GA4 relative date such as 28daysAgo."
                },
                "endDate": {
                  "type": "string",
                  "minLength": 1,
                  "description": "YYYY-MM-DD or a GA4 relative date such as today."
                }
              },
              "required": [
                "startDate",
                "endDate"
              ],
              "additionalProperties": false
            },
            "minItems": 1,
            "maxItems": 4
          },
          "dimensions": {
            "type": "array",
            "items": {
              "type": "string",
              "minLength": 1
            },
            "minItems": 1,
            "maxItems": 9
          },
          "metrics": {
            "type": "array",
            "items": {
              "type": "string",
              "minLength": 1
            },
            "minItems": 1,
            "maxItems": 10
          },
          "pivots": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "fieldNames": {
                  "type": "array",
                  "items": {
                    "type": "string",
                    "minLength": 1
                  },
                  "minItems": 1,
                  "maxItems": 9
                },
                "orderBys": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "additionalProperties": {},
                    "description": "Native GA4 OrderBy JSON."
                  },
                  "maxItems": 10
                },
                "offset": {
                  "type": "integer",
                  "minimum": 0
                },
                "limit": {
                  "type": "integer",
                  "minimum": 1,
                  "maximum": 250000
                },
                "metricAggregations": {
                  "type": "array",
                  "items": {
                    "type": "string",
                    "enum": [
                      "TOTAL",
                      "MINIMUM",
                      "MAXIMUM",
                      "COUNT"
                    ]
                  },
                  "maxItems": 4
                }
              },
              "required": [
                "fieldNames",
                "limit"
              ],
              "additionalProperties": false
            },
            "minItems": 1,
            "maxItems": 9
          },
          "dimensionFilter": {
            "type": "object",
            "additionalProperties": {},
            "description": "Native GA4 FilterExpression JSON."
          },
          "metricFilter": {
            "type": "object",
            "additionalProperties": {},
            "description": "Native GA4 FilterExpression JSON."
          },
          "currencyCode": {
            "type": "string",
            "minLength": 3,
            "maxLength": 3
          },
          "keepEmptyRows": {
            "type": "boolean"
          },
          "returnPropertyQuota": {
            "type": "boolean",
            "default": true
          },
          "cohortSpec": {
            "type": "object",
            "additionalProperties": {},
            "description": "Native GA4 CohortSpec JSON. Omit dateRanges for cohort requests."
          },
          "comparisons": {
            "type": "array",
            "items": {
              "type": "object",
              "additionalProperties": {}
            },
            "maxItems": 4,
            "description": "Native GA4 Comparison objects."
          }
        },
        "required": [
          "dimensions",
          "metrics",
          "pivots"
        ],
        "additionalProperties": false
      },
      "minItems": 1,
      "maxItems": 5,
      "description": "Native GA4 report request objects to execute in one batch."
    }
  },
  "required": [
    "propertyId",
    "reports"
  ],
  "additionalProperties": false
}
```

</details>

- Report refinement requires nonempty dateRanges or cohortSpec. Native filters, orderings, cohortSpec and comparisons are arbitrary JSON records; their internal GA API shapes are intentionally not validated.
- Handler requires pivot fields to be declared dimensions (except dateRange/comparisons), forbids repeated fields across pivots, and limits product of pivot limits to 250000.

Source: [src/platforms/ga4/surface-tools.ts:205](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/surface-tools.ts#L205-L227) · [src/platforms/ga4/client.ts:450](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/client.ts#L450-L464) · [src/tool-quality.ts:46](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/tool-quality.ts#L46-L58) · [src/platforms/ga4/surface-tools.ts:26](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/surface-tools.ts#L26-L78) · [src/parameter-descriptions.ts:1](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/parameter-descriptions.ts#L1-L235).

## ga4_check_compatibility

Maps dimension/metric name arrays to native objects and forwards optional filters/category to official Core compatibility endpoint.

<details>
<summary>Full registered description</summary>

```text
Ask the official GA4 Data API which dimensions and metrics are compatible with a proposed Core report selection.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `propertyId` | Yes | string | Not declared |
| `dimensions` | No | array of string | [] |
| `metrics` | No | array of string | [] |
| `dimensionFilter` | No | object | Not declared |
| `metricFilter` | No | object | Not declared |
| `compatibilityFilter` | No | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "propertyId": {
      "type": "string",
      "minLength": 1,
      "description": "Numeric GA4 property ID or properties/{id}."
    },
    "dimensions": {
      "type": "array",
      "items": {
        "type": "string",
        "minLength": 1
      },
      "maxItems": 9,
      "default": [],
      "description": "Native reporting dimensions. Validate compatibility with the selected metrics."
    },
    "metrics": {
      "type": "array",
      "items": {
        "type": "string",
        "minLength": 1
      },
      "maxItems": 10,
      "default": [],
      "description": "Native or documented calculated metric names to request. Check compatibility with the selected dimensions."
    },
    "dimensionFilter": {
      "type": "object",
      "additionalProperties": {},
      "description": "Native GA4 FilterExpression JSON."
    },
    "metricFilter": {
      "type": "object",
      "additionalProperties": {},
      "description": "Native GA4 FilterExpression JSON."
    },
    "compatibilityFilter": {
      "type": "string",
      "enum": [
        "COMPATIBILITY_UNSPECIFIED",
        "COMPATIBLE",
        "INCOMPATIBLE"
      ],
      "description": "Limit compatibility results to the requested GA4 compatibility category."
    }
  },
  "required": [
    "propertyId"
  ],
  "additionalProperties": false
}
```

</details>

Source: [src/platforms/ga4/surface-tools.ts:229](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/surface-tools.ts#L229-L252) · [src/platforms/ga4/client.ts:465](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/client.ts#L465-L479) · [src/tool-quality.ts:46](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/tool-quality.ts#L46-L58) · [src/platforms/ga4/surface-tools.ts:26](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/surface-tools.ts#L26-L78) · [src/parameter-descriptions.ts:1](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/parameter-descriptions.ts#L1-L235).

## ga4_get_property_quotas_snapshot

Gets v1alpha Data API property quota snapshot without running a report.

<details>
<summary>Full registered description</summary>

```text
Read the current GA4 Data API property quota snapshot from the official v1alpha endpoint. This does not run a report, but Google still charges one property-quota token to the category with the most remaining quota.
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
      "minLength": 1,
      "description": "Numeric GA4 property ID or properties/{id}."
    }
  },
  "required": [
    "propertyId"
  ],
  "additionalProperties": false
}
```

</details>

Source: [src/platforms/ga4/surface-tools.ts:254](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/surface-tools.ts#L254-L264) · [src/platforms/ga4/client.ts:480](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/client.ts#L480-L489) · [src/tool-quality.ts:46](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/tool-quality.ts#L46-L58) · [src/platforms/ga4/surface-tools.ts:26](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/surface-tools.ts#L26-L78) · [src/parameter-descriptions.ts:1](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/parameter-descriptions.ts#L1-L235).

## ga4_list_accounts

Reads raw Admin v1beta accounts with page-size selection and automatic page-token iteration.

<details>
<summary>Full registered description</summary>

```text
List raw GA4 Analytics Admin accounts accessible to the authenticated user (read-only, auto-paginated).
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
      "minimum": 1,
      "maximum": 200,
      "default": 200,
      "description": "Maximum items requested per page. Follow the returned pagination information for remaining results."
    }
  },
  "required": [],
  "additionalProperties": false
}
```

</details>

- Shared listPagedRecords stops after 50 pages; a remaining page token is not returned.

Source: [src/platforms/ga4/surface-tools.ts:266](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/surface-tools.ts#L266-L276) · [src/platforms/ga4/client.ts:539](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/client.ts#L539-L547) · [src/tool-quality.ts:46](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/tool-quality.ts#L46-L58) · [src/platforms/ga4/surface-tools.ts:26](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/surface-tools.ts#L26-L78) · [src/parameter-descriptions.ts:1](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/parameter-descriptions.ts#L1-L235).

## ga4_list_admin_resources

Looks up selected collection in 20-entry allowlist and GETs Admin v1beta or v1alpha property collection with page-token iteration. Access-binding personal identifiers redact by default and opt-in output adds a warning.

<details>
<summary>Full registered description</summary>

```text
List an allowlisted GA4 Admin collection in read-only mode: streams, custom definitions, key events, audiences, product links, annotations, channel groups, expanded datasets, subproperty/rollup configuration, and access bindings.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `propertyId` | Yes | string | Not declared |
| `collection` | Yes | string | Not declared |
| `pageSize` | No | integer | 200 |
| `includePersonalIdentifiers` | No | boolean | false |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "propertyId": {
      "type": "string",
      "minLength": 1,
      "description": "Numeric GA4 property ID or properties/{id}."
    },
    "collection": {
      "type": "string",
      "enum": [
        "accessBindings",
        "adSenseLinks",
        "audiences",
        "bigQueryLinks",
        "calculatedMetrics",
        "channelGroups",
        "customDimensions",
        "customMetrics",
        "dataStreams",
        "displayVideo360AdvertiserLinkProposals",
        "displayVideo360AdvertiserLinks",
        "expandedDataSets",
        "firebaseLinks",
        "googleAdsLinks",
        "keyEvents",
        "reportingDataAnnotations",
        "rollupPropertySourceLinks",
        "searchAds360Links",
        "subpropertyEventFilters",
        "subpropertySyncConfigs"
      ],
      "description": "Allowlisted administrative resource collection to read."
    },
    "pageSize": {
      "type": "integer",
      "minimum": 1,
      "maximum": 200,
      "default": 200,
      "description": "Maximum items requested per page. Follow the returned pagination information for remaining results."
    },
    "includePersonalIdentifiers": {
      "type": "boolean",
      "default": false,
      "description": "Access bindings only. Explicitly include user/email identifiers; false redacts them by default."
    }
  },
  "required": [
    "propertyId",
    "collection"
  ],
  "additionalProperties": false
}
```

</details>

- Shared listPagedRecords stops after 50 pages; a remaining page token is not returned.

Source: [src/platforms/ga4/surface-tools.ts:279](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/surface-tools.ts#L279-L309) · [src/platforms/ga4/client.ts:551](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/client.ts#L551-L566) · [src/tool-quality.ts:46](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/tool-quality.ts#L46-L58) · [src/platforms/ga4/surface-tools.ts:26](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/surface-tools.ts#L26-L78) · [src/parameter-descriptions.ts:1](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/parameter-descriptions.ts#L1-L235) · [src/platforms/ga4/client.ts:39](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/client.ts#L39-L60).

## ga4_get_property_configuration

Gets Admin v1beta property and each unique requested singleton setting; retention uses v1beta, other settings v1alpha. Individual setting failures become warnings without discarding property result.

<details>
<summary>Full registered description</summary>

```text
Read GA4 property details plus selected singleton Admin settings (attribution, retention, Google Signals, reporting identity, or user-provided-data settings).
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `propertyId` | Yes | string | Not declared |
| `settings` | No | array of string | [] |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "propertyId": {
      "type": "string",
      "minLength": 1,
      "description": "Numeric GA4 property ID or properties/{id}."
    },
    "settings": {
      "type": "array",
      "items": {
        "type": "string",
        "enum": [
          "attributionSettings",
          "dataRetentionSettings",
          "googleSignalsSettings",
          "reportingIdentitySettings",
          "userProvidedDataSettings"
        ]
      },
      "maxItems": 5,
      "default": [],
      "description": "Property configuration surfaces to inspect."
    }
  },
  "required": [
    "propertyId"
  ],
  "additionalProperties": false
}
```

</details>

Source: [src/platforms/ga4/surface-tools.ts:318](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/surface-tools.ts#L318-L340) · [src/platforms/ga4/client.ts:529](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/client.ts#L529-L538) · [src/platforms/ga4/client.ts:567](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/client.ts#L567-L579) · [src/tool-quality.ts:46](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/tool-quality.ts#L46-L58) · [src/platforms/ga4/surface-tools.ts:26](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/surface-tools.ts#L26-L78) · [src/parameter-descriptions.ts:1](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/parameter-descriptions.ts#L1-L235).

## ga4_list_audience_exports

Lists existing Data API v1beta audience exports and optionally v1alpha recurring audience lists; creates no exports. Recurring list page size is capped at 100.

<details>
<summary>Full registered description</summary>

```text
List existing GA4 Audience Export snapshots and Recurring Audience Lists without creating new exports.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `propertyId` | Yes | string | Not declared |
| `includeRecurring` | No | boolean | true |
| `pageSize` | No | integer | 100 |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "propertyId": {
      "type": "string",
      "minLength": 1,
      "description": "Numeric GA4 property ID or properties/{id}."
    },
    "includeRecurring": {
      "type": "boolean",
      "default": true,
      "description": "Include recurring audience-export configurations."
    },
    "pageSize": {
      "type": "integer",
      "minimum": 1,
      "maximum": 200,
      "default": 100,
      "description": "Maximum items requested per page. Follow the returned pagination information for remaining results."
    }
  },
  "required": [
    "propertyId"
  ],
  "additionalProperties": false
}
```

</details>

- Shared listPagedRecords stops after 50 pages; a remaining page token is not returned.

Source: [src/platforms/ga4/surface-tools.ts:342](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/surface-tools.ts#L342-L364) · [src/platforms/ga4/client.ts:587](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/client.ts#L587-L596) · [src/platforms/ga4/client.ts:641](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/client.ts#L641-L650) · [src/tool-quality.ts:46](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/tool-quality.ts#L46-L58) · [src/platforms/ga4/surface-tools.ts:26](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/surface-tools.ts#L26-L78) · [src/parameter-descriptions.ts:1](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/parameter-descriptions.ts#L1-L235).

## ga4_query_audience_export

Queries existing export with stringified offset/limit, redacts user/device identifier columns by default, and emits disclosure warnings for opt-in identifiers.

<details>
<summary>Full registered description</summary>

```text
Query rows from an existing GA4 Audience Export. User/device identifiers are redacted by default; include them only through explicit opt-in.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `audienceExportName` | Yes | string | Not declared |
| `offset` | No | integer | 0 |
| `limit` | No | integer | 100 |
| `includePersonalIdentifiers` | No | boolean | false |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "audienceExportName": {
      "type": "string",
      "pattern": "^properties/[^/]+/audienceExports/[^/]+$",
      "description": "Full GA4 audience-export resource name returned by list_audience_exports."
    },
    "offset": {
      "type": "integer",
      "minimum": 0,
      "default": 0,
      "description": "Zero-based number of rows to skip before returning results."
    },
    "limit": {
      "type": "integer",
      "minimum": 1,
      "maximum": 10000,
      "default": 100,
      "description": "Maximum number of returned items or rows. The declared bounds and default apply; use pagination for additional results."
    },
    "includePersonalIdentifiers": {
      "type": "boolean",
      "default": false,
      "description": "Explicitly return user/device identifiers. False redacts identifier columns by default."
    }
  },
  "required": [
    "audienceExportName"
  ],
  "additionalProperties": false
}
```

</details>

Source: [src/platforms/ga4/surface-tools.ts:366](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/surface-tools.ts#L366-L391) · [src/platforms/ga4/client.ts:611](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/client.ts#L611-L624) · [src/tool-quality.ts:46](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/tool-quality.ts#L46-L58) · [src/platforms/ga4/surface-tools.ts:26](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/platforms/ga4/surface-tools.ts#L26-L78) · [src/parameter-descriptions.ts:1](https://github.com/get-mcp-ads/google-analytics-mcp-server/blob/f59104fd0edd96807944df94657e337e17c989be/src/parameter-descriptions.ts#L1-L235).

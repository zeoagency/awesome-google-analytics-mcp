# CUTolu2021/ga4-mcp-server

[Catalog](../../README.md) · [All tool names](../tool-index.md) · [Upstream](https://github.com/CUTolu2021/ga4-mcp-server) · [JSON](../../data/mcps/cutolu2021--ga4-mcp-server.json)

**6 tools:** 6 GA4, 0 other-service or server-support tools. Reviewed source: [`02b6e355b412`](https://github.com/CUTolu2021/ga4-mcp-server/tree/02b6e355b412dbd303daf1cdd1f17679bb449046).

Descriptions and parameter schemas come from the registered source definitions. Generated schemas are reconstructed from annotations or validators; live `tools/list` and authenticated API calls were not run. Loose objects remain loose.

<details>
<summary>Exposure and compatibility notes</summary>

- Source review only; no tools/list, upstream execution, authenticated GA requests or runtime schema validation. Git HEAD matches supplied revision.
- All six registrations are unconditional in one ListTools handler and all six have matching switch cases. No realtime tool or runRealtimeReport API call exists.
- Startup requires GOOGLE_CLIENT_EMAIL and GOOGLE_PRIVATE_KEY; GA_PROPERTY_ID is optional. No credential values were inspected.
- package.json build/start/bin target dist/index.js; source checkout has no dist and requires TypeScript build. prepare runs husky, although no .husky directory is present in this checkout; installation was not tested.

</details>

## Tools

| Tool | Scope | Effect |
| --- | --- | --- |
| [`listProperties`](#listproperties) | GA4 | read |
| [`runReport`](#runreport) | GA4 | read |
| [`getPageViews`](#getpageviews) | GA4 | read |
| [`getActiveUsers`](#getactiveusers) | GA4 | read |
| [`getEvents`](#getevents) | GA4 | read |
| [`getUserBehavior`](#getuserbehavior) | GA4 | read |

## listProperties

Lists every accessible account and each nondeleted child GA4 property using paginated Admin API requests (pageSize 200). Caches property records for five minutes; force_refresh bypasses cache. Returns compact JSON property IDs, display names, account identifiers, currency/time zone when present; verbose adds property resource name.

<details>
<summary>Full registered description</summary>

```text
List accessible GA4 properties and their property IDs
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `force_refresh` | No | boolean | false |
| `verbose` | No | boolean | false |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "force_refresh": {
      "type": "boolean",
      "description": "Refresh properties from Google Analytics Admin API instead of using the cache.",
      "default": false
    },
    "verbose": {
      "type": "boolean",
      "description": "Include property resource names and other optional identifiers.",
      "default": false
    }
  }
}
```

</details>

- Schema omits required entirely (both properties optional). Handler defaults force_refresh=false and verbose=false. force_refresh is not runtime type-validated and is used by truthiness; verbose accepts null as omitted despite boolean schema.

Source: [src/index.ts:702](https://github.com/CUTolu2021/ga4-mcp-server/blob/02b6e355b412dbd303daf1cdd1f17679bb449046/src/index.ts#L702-L722) · [src/index.ts:914](https://github.com/CUTolu2021/ga4-mcp-server/blob/02b6e355b412dbd303daf1cdd1f17679bb449046/src/index.ts#L914-L953) · [src/index.ts:462](https://github.com/CUTolu2021/ga4-mcp-server/blob/02b6e355b412dbd303daf1cdd1f17679bb449046/src/index.ts#L462-L535).

## runReport

Validates dates and output options, resolves the property, and calls Data API runReport with one date range, supplied dimension and metric objects, optional dimensionFilter, limit and offset. Returns compact row dictionaries and pagination information; verbose requests quota and includes metric types; include_raw includes the API response.

<details>
<summary>Full registered description</summary>

```text
Run a report to get analytics data
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | No | string | Not declared |
| `property_name` | No | string | Not declared |
| `startDate` | Yes | string | Not declared |
| `endDate` | Yes | string | Not declared |
| `dimensions` | Yes | array of object | Not declared |
| `metrics` | Yes | array of object | Not declared |
| `dimensionFilter` | No | object | Not declared |
| `limit` | No | integer | Not declared |
| `offset` | No | integer | Not declared |
| `verbose` | No | boolean | false |
| `include_raw` | No | boolean | false |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "property_id": {
      "type": "string",
      "description": "GA4 property ID to query. If omitted, uses GA_PROPERTY_ID from environment."
    },
    "property_name": {
      "type": "string",
      "description": "GA4 property display name to query. Used when property_id is not provided."
    },
    "startDate": {
      "type": "string",
      "description": "Start date in YYYY-MM-DD format"
    },
    "endDate": {
      "type": "string",
      "description": "End date in YYYY-MM-DD format"
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
        ]
      },
      "description": "Dimensions to group by (e.g., page, country)"
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
        ]
      },
      "description": "Metrics to include in the report"
    },
    "dimensionFilter": {
      "type": "object",
      "description": "Filter for dimensions"
    },
    "limit": {
      "type": "integer",
      "minimum": 0,
      "description": "Maximum number of rows to return. Use with offset for pagination."
    },
    "offset": {
      "type": "integer",
      "minimum": 0,
      "description": "Zero-based row offset for pagination. Use next_offset from the previous response."
    },
    "verbose": {
      "type": "boolean",
      "description": "Include compact diagnostic metadata such as metric types and quota details.",
      "default": false
    },
    "include_raw": {
      "type": "boolean",
      "description": "Include the raw Google Analytics API response for debugging or compatibility.",
      "default": false
    }
  },
  "required": [
    "startDate",
    "endDate",
    "metrics",
    "dimensions"
  ]
}
```

</details>

- Dates are validated in the handler as real YYYY-MM-DD dates with startDate <= endDate; schema advertises string without format or pattern. Relative GA date strings are rejected. Invalid calendar strings can throw during toISOString and become InternalError.
- Property fields are schema-optional, but the handler requires a nonblank property_id, resolvable property_name, or GA_PROPERTY_ID. Resolution prioritizes ID, then case-insensitive exact/unique substring display-name matching via Admin API, then environment default. IDs are only trimmed and get a properties/ prefix.
- Handlers accept null for limit, offset, verbose and include_raw as omitted even though the exposed schema does not permit null. verbose/include_raw default false; limit and offset are omitted from API requests when unset. No additionalProperties restriction is advertised.
- Schema requires dimensions and metrics, but handler destructuring defaults each to [] if omitted. dimensionFilter is deliberately exposed as an unrestricted object without nested properties and forwarded unchanged; dimension/metric item schemas only declare name but do not prohibit extra fields.

Source: [src/index.ts:723](https://github.com/CUTolu2021/ga4-mcp-server/blob/02b6e355b412dbd303daf1cdd1f17679bb449046/src/index.ts#L723-L777) · [src/index.ts:954](https://github.com/CUTolu2021/ga4-mcp-server/blob/02b6e355b412dbd303daf1cdd1f17679bb449046/src/index.ts#L954-L1006) · [src/index.ts:671](https://github.com/CUTolu2021/ga4-mcp-server/blob/02b6e355b412dbd303daf1cdd1f17679bb449046/src/index.ts#L671-L696) · [src/index.ts:537](https://github.com/CUTolu2021/ga4-mcp-server/blob/02b6e355b412dbd303daf1cdd1f17679bb449046/src/index.ts#L537-L669) · [src/index.ts:389](https://github.com/CUTolu2021/ga4-mcp-server/blob/02b6e355b412dbd303daf1cdd1f17679bb449046/src/index.ts#L389-L460).

## getPageViews

Calls Data API runReport with screenPageViews, supplied string dimensions mapped to name objects (handler default ["page"]), and one date range. Returns the shared compact report output.

<details>
<summary>Full registered description</summary>

```text
Get page view metrics for a specific date range
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | No | string | Not declared |
| `property_name` | No | string | Not declared |
| `startDate` | Yes | string | Not declared |
| `endDate` | Yes | string | Not declared |
| `dimensions` | No | array of string | Not declared |
| `limit` | No | integer | Not declared |
| `offset` | No | integer | Not declared |
| `verbose` | No | boolean | false |
| `include_raw` | No | boolean | false |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "property_id": {
      "type": "string",
      "description": "GA4 property ID to query. If omitted, uses GA_PROPERTY_ID from environment."
    },
    "property_name": {
      "type": "string",
      "description": "GA4 property display name to query. Used when property_id is not provided."
    },
    "startDate": {
      "type": "string",
      "description": "Start date in YYYY-MM-DD format"
    },
    "endDate": {
      "type": "string",
      "description": "End date in YYYY-MM-DD format"
    },
    "dimensions": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Dimensions to group by (e.g., page, country)"
    },
    "limit": {
      "type": "integer",
      "minimum": 0,
      "description": "Maximum number of rows to return. Use with offset for pagination."
    },
    "offset": {
      "type": "integer",
      "minimum": 0,
      "description": "Zero-based row offset for pagination. Use next_offset from the previous response."
    },
    "verbose": {
      "type": "boolean",
      "description": "Include compact diagnostic metadata such as metric types and quota details.",
      "default": false
    },
    "include_raw": {
      "type": "boolean",
      "description": "Include the raw Google Analytics API response for debugging or compatibility.",
      "default": false
    }
  },
  "required": [
    "startDate",
    "endDate"
  ]
}
```

</details>

- Dates are validated in the handler as real YYYY-MM-DD dates with startDate <= endDate; schema advertises string without format or pattern. Relative GA date strings are rejected. Invalid calendar strings can throw during toISOString and become InternalError.
- Property fields are schema-optional, but the handler requires a nonblank property_id, resolvable property_name, or GA_PROPERTY_ID. Resolution prioritizes ID, then case-insensitive exact/unique substring display-name matching via Admin API, then environment default. IDs are only trimmed and get a properties/ prefix.
- Handlers accept null for limit, offset, verbose and include_raw as omitted even though the exposed schema does not permit null. verbose/include_raw default false; limit and offset are omitted from API requests when unset. No additionalProperties restriction is advertised.
- Schema has optional dimensions with no default; handler defaults to ["page"]. That default is forwarded verbatim as a GA dimension name; no mapping to pagePath or API metadata validation exists, so the convenience default may be rejected by GA.

Source: [src/index.ts:778](https://github.com/CUTolu2021/ga4-mcp-server/blob/02b6e355b412dbd303daf1cdd1f17679bb449046/src/index.ts#L778-L811) · [src/index.ts:1007](https://github.com/CUTolu2021/ga4-mcp-server/blob/02b6e355b412dbd303daf1cdd1f17679bb449046/src/index.ts#L1007-L1054) · [src/index.ts:671](https://github.com/CUTolu2021/ga4-mcp-server/blob/02b6e355b412dbd303daf1cdd1f17679bb449046/src/index.ts#L671-L696) · [src/index.ts:537](https://github.com/CUTolu2021/ga4-mcp-server/blob/02b6e355b412dbd303daf1cdd1f17679bb449046/src/index.ts#L537-L669) · [src/index.ts:389](https://github.com/CUTolu2021/ga4-mcp-server/blob/02b6e355b412dbd303daf1cdd1f17679bb449046/src/index.ts#L389-L460).

## getActiveUsers

Calls Data API runReport with activeUsers and newUsers grouped by date over the requested date range. Returns the shared compact report output. This is a historical date-range report, not runRealtimeReport.

<details>
<summary>Full registered description</summary>

```text
Get active users metrics for a specific date range
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | No | string | Not declared |
| `property_name` | No | string | Not declared |
| `startDate` | Yes | string | Not declared |
| `endDate` | Yes | string | Not declared |
| `limit` | No | integer | Not declared |
| `offset` | No | integer | Not declared |
| `verbose` | No | boolean | false |
| `include_raw` | No | boolean | false |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "property_id": {
      "type": "string",
      "description": "GA4 property ID to query. If omitted, uses GA_PROPERTY_ID from environment."
    },
    "property_name": {
      "type": "string",
      "description": "GA4 property display name to query. Used when property_id is not provided."
    },
    "startDate": {
      "type": "string",
      "description": "Start date in YYYY-MM-DD format"
    },
    "endDate": {
      "type": "string",
      "description": "End date in YYYY-MM-DD format"
    },
    "limit": {
      "type": "integer",
      "minimum": 0,
      "description": "Maximum number of rows to return. Use with offset for pagination."
    },
    "offset": {
      "type": "integer",
      "minimum": 0,
      "description": "Zero-based row offset for pagination. Use next_offset from the previous response."
    },
    "verbose": {
      "type": "boolean",
      "description": "Include compact diagnostic metadata such as metric types and quota details.",
      "default": false
    },
    "include_raw": {
      "type": "boolean",
      "description": "Include the raw Google Analytics API response for debugging or compatibility.",
      "default": false
    }
  },
  "required": [
    "startDate",
    "endDate"
  ]
}
```

</details>

- Dates are validated in the handler as real YYYY-MM-DD dates with startDate <= endDate; schema advertises string without format or pattern. Relative GA date strings are rejected. Invalid calendar strings can throw during toISOString and become InternalError.
- Property fields are schema-optional, but the handler requires a nonblank property_id, resolvable property_name, or GA_PROPERTY_ID. Resolution prioritizes ID, then case-insensitive exact/unique substring display-name matching via Admin API, then environment default. IDs are only trimmed and get a properties/ prefix.
- Handlers accept null for limit, offset, verbose and include_raw as omitted even though the exposed schema does not permit null. verbose/include_raw default false; limit and offset are omitted from API requests when unset. No additionalProperties restriction is advertised.

Source: [src/index.ts:812](https://github.com/CUTolu2021/ga4-mcp-server/blob/02b6e355b412dbd303daf1cdd1f17679bb449046/src/index.ts#L812-L840) · [src/index.ts:1056](https://github.com/CUTolu2021/ga4-mcp-server/blob/02b6e355b412dbd303daf1cdd1f17679bb449046/src/index.ts#L1056-L1101) · [src/index.ts:671](https://github.com/CUTolu2021/ga4-mcp-server/blob/02b6e355b412dbd303daf1cdd1f17679bb449046/src/index.ts#L671-L696) · [src/index.ts:537](https://github.com/CUTolu2021/ga4-mcp-server/blob/02b6e355b412dbd303daf1cdd1f17679bb449046/src/index.ts#L537-L669) · [src/index.ts:389](https://github.com/CUTolu2021/ga4-mcp-server/blob/02b6e355b412dbd303daf1cdd1f17679bb449046/src/index.ts#L389-L460).

## getEvents

Calls Data API runReport with eventCount grouped by eventName and date. A truthy eventName adds a dimensionFilter with fieldName eventName and stringFilter.value; no matchType is set. Returns the shared compact report output.

<details>
<summary>Full registered description</summary>

```text
Get event metrics for a specific date range
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | No | string | Not declared |
| `property_name` | No | string | Not declared |
| `startDate` | Yes | string | Not declared |
| `endDate` | Yes | string | Not declared |
| `eventName` | No | string | Not declared |
| `limit` | No | integer | Not declared |
| `offset` | No | integer | Not declared |
| `verbose` | No | boolean | false |
| `include_raw` | No | boolean | false |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "property_id": {
      "type": "string",
      "description": "GA4 property ID to query. If omitted, uses GA_PROPERTY_ID from environment."
    },
    "property_name": {
      "type": "string",
      "description": "GA4 property display name to query. Used when property_id is not provided."
    },
    "startDate": {
      "type": "string",
      "description": "Start date in YYYY-MM-DD format"
    },
    "endDate": {
      "type": "string",
      "description": "End date in YYYY-MM-DD format"
    },
    "eventName": {
      "type": "string",
      "description": "Specific event name to filter by (optional)"
    },
    "limit": {
      "type": "integer",
      "minimum": 0,
      "description": "Maximum number of rows to return. Use with offset for pagination."
    },
    "offset": {
      "type": "integer",
      "minimum": 0,
      "description": "Zero-based row offset for pagination. Use next_offset from the previous response."
    },
    "verbose": {
      "type": "boolean",
      "description": "Include compact diagnostic metadata such as metric types and quota details.",
      "default": false
    },
    "include_raw": {
      "type": "boolean",
      "description": "Include the raw Google Analytics API response for debugging or compatibility.",
      "default": false
    }
  },
  "required": [
    "startDate",
    "endDate"
  ]
}
```

</details>

- Dates are validated in the handler as real YYYY-MM-DD dates with startDate <= endDate; schema advertises string without format or pattern. Relative GA date strings are rejected. Invalid calendar strings can throw during toISOString and become InternalError.
- Property fields are schema-optional, but the handler requires a nonblank property_id, resolvable property_name, or GA_PROPERTY_ID. Resolution prioritizes ID, then case-insensitive exact/unique substring display-name matching via Admin API, then environment default. IDs are only trimmed and get a properties/ prefix.
- Handlers accept null for limit, offset, verbose and include_raw as omitted even though the exposed schema does not permit null. verbose/include_raw default false; limit and offset are omitted from API requests when unset. No additionalProperties restriction is advertised.

Source: [src/index.ts:841](https://github.com/CUTolu2021/ga4-mcp-server/blob/02b6e355b412dbd303daf1cdd1f17679bb449046/src/index.ts#L841-L873) · [src/index.ts:1103](https://github.com/CUTolu2021/ga4-mcp-server/blob/02b6e355b412dbd303daf1cdd1f17679bb449046/src/index.ts#L1103-L1158) · [src/index.ts:671](https://github.com/CUTolu2021/ga4-mcp-server/blob/02b6e355b412dbd303daf1cdd1f17679bb449046/src/index.ts#L671-L696) · [src/index.ts:537](https://github.com/CUTolu2021/ga4-mcp-server/blob/02b6e355b412dbd303daf1cdd1f17679bb449046/src/index.ts#L537-L669) · [src/index.ts:389](https://github.com/CUTolu2021/ga4-mcp-server/blob/02b6e355b412dbd303daf1cdd1f17679bb449046/src/index.ts#L389-L460).

## getUserBehavior

Calls Data API runReport with averageSessionDuration, bounceRate and sessionsPerUser grouped by date. Returns the shared compact report output.

<details>
<summary>Full registered description</summary>

```text
Get user behavior metrics like session duration and bounce rate
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | No | string | Not declared |
| `property_name` | No | string | Not declared |
| `startDate` | Yes | string | Not declared |
| `endDate` | Yes | string | Not declared |
| `limit` | No | integer | Not declared |
| `offset` | No | integer | Not declared |
| `verbose` | No | boolean | false |
| `include_raw` | No | boolean | false |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "property_id": {
      "type": "string",
      "description": "GA4 property ID to query. If omitted, uses GA_PROPERTY_ID from environment."
    },
    "property_name": {
      "type": "string",
      "description": "GA4 property display name to query. Used when property_id is not provided."
    },
    "startDate": {
      "type": "string",
      "description": "Start date in YYYY-MM-DD format"
    },
    "endDate": {
      "type": "string",
      "description": "End date in YYYY-MM-DD format"
    },
    "limit": {
      "type": "integer",
      "minimum": 0,
      "description": "Maximum number of rows to return. Use with offset for pagination."
    },
    "offset": {
      "type": "integer",
      "minimum": 0,
      "description": "Zero-based row offset for pagination. Use next_offset from the previous response."
    },
    "verbose": {
      "type": "boolean",
      "description": "Include compact diagnostic metadata such as metric types and quota details.",
      "default": false
    },
    "include_raw": {
      "type": "boolean",
      "description": "Include the raw Google Analytics API response for debugging or compatibility.",
      "default": false
    }
  },
  "required": [
    "startDate",
    "endDate"
  ]
}
```

</details>

- Dates are validated in the handler as real YYYY-MM-DD dates with startDate <= endDate; schema advertises string without format or pattern. Relative GA date strings are rejected. Invalid calendar strings can throw during toISOString and become InternalError.
- Property fields are schema-optional, but the handler requires a nonblank property_id, resolvable property_name, or GA_PROPERTY_ID. Resolution prioritizes ID, then case-insensitive exact/unique substring display-name matching via Admin API, then environment default. IDs are only trimmed and get a properties/ prefix.
- Handlers accept null for limit, offset, verbose and include_raw as omitted even though the exposed schema does not permit null. verbose/include_raw default false; limit and offset are omitted from API requests when unset. No additionalProperties restriction is advertised.

Source: [src/index.ts:874](https://github.com/CUTolu2021/ga4-mcp-server/blob/02b6e355b412dbd303daf1cdd1f17679bb449046/src/index.ts#L874-L903) · [src/index.ts:1160](https://github.com/CUTolu2021/ga4-mcp-server/blob/02b6e355b412dbd303daf1cdd1f17679bb449046/src/index.ts#L1160-L1209) · [src/index.ts:671](https://github.com/CUTolu2021/ga4-mcp-server/blob/02b6e355b412dbd303daf1cdd1f17679bb449046/src/index.ts#L671-L696) · [src/index.ts:537](https://github.com/CUTolu2021/ga4-mcp-server/blob/02b6e355b412dbd303daf1cdd1f17679bb449046/src/index.ts#L537-L669) · [src/index.ts:389](https://github.com/CUTolu2021/ga4-mcp-server/blob/02b6e355b412dbd303daf1cdd1f17679bb449046/src/index.ts#L389-L460).

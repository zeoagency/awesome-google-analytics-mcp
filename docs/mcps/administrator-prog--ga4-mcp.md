# administrator-prog/ga4-mcp

[Catalog](../../README.md) · [All tool names](../tool-index.md) · [Upstream](https://github.com/administrator-prog/ga4-mcp) · [JSON](../../data/mcps/administrator-prog--ga4-mcp.json)

**11 tools:** 11 GA4, 0 other-service or server-support tools. Reviewed source: [`5a2453257e66`](https://github.com/administrator-prog/ga4-mcp/tree/5a2453257e66c2c53dc961611fd2bb55c729e0f5).

Descriptions and parameter schemas come from the registered source definitions. Generated schemas are reconstructed from annotations or validators; live `tools/list` and authenticated API calls were not run. Loose objects remain loose.

<details>
<summary>Exposure and compatibility notes</summary>

- Source review only; no tools/list or live requests. HEAD matches the supplied revision.
- All 11 tools are unconditionally registered by createServer for each MCP HTTP request. No optional modules or permission tiers exist. The root and OAuth Express routes are HTTP endpoints, not MCP tools.
- Schemas are reconstructed from the explicit Zod raw shapes supplied to server.tool, including optional/default parameters and descriptions; additionalProperties false reflects the SDK object-schema conversion of default Zod object shapes. No nested schemas or references occur.
- Authentication uses GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET, GOOGLE_REDIRECT_URI and optional GOOGLE_REFRESH_TOKEN. The provided OAuth endpoint requests analytics.readonly scope. Credentials and authorized GA access are required for API calls.
- Date and property parameters are unconstrained strings. Every report handler prefixes propertyId with properties/ and returns raw API response data via JSON text.
- Several reports request conversions; API metric availability and dimension/metric compatibility were not validated with live requests.
- The OAuth routes are registered inside createServer, so each MCP request adds another set of Express route handlers.
- Dependencies are declared as latest, though package-lock.json pins installed versions. The start script requires dist/index.js produced by npm run build; dist is not committed.

</details>

## Tools

| Tool | Scope | Effect |
| --- | --- | --- |
| [`list_ga4_properties`](#list_ga4_properties) | GA4 | read |
| [`get_ga4_traffic_summary`](#get_ga4_traffic_summary) | GA4 | read |
| [`get_ga4_top_landing_pages`](#get_ga4_top_landing_pages) | GA4 | read |
| [`get_ga4_traffic_by_channel`](#get_ga4_traffic_by_channel) | GA4 | read |
| [`compare_ga4_date_ranges`](#compare_ga4_date_ranges) | GA4 | read |
| [`analyse_organic_performance`](#analyse_organic_performance) | GA4 | read |
| [`analyse_landing_page`](#analyse_landing_page) | GA4 | read |
| [`analyse_conversion_drop`](#analyse_conversion_drop) | GA4 | read |
| [`analyse_devices`](#analyse_devices) | GA4 | read |
| [`analyse_events_by_page`](#analyse_events_by_page) | GA4 | read |
| [`analyse_site_search`](#analyse_site_search) | GA4 | read |

## list_ga4_properties

Lists accounts with Analytics Admin v1beta accounts.list, then lists properties filtered by each account parent. Returns account display/resource names and property display/resource names, extracted property IDs, timezone and currency.

<details>
<summary>Full registered description</summary>

```text
List GA4 accounts and properties available to the authenticated Google account.
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

- Neither accounts.list nor properties.list paginates, so results may omit later pages.

Source: [src/index.ts:61](https://github.com/administrator-prog/ga4-mcp/blob/5a2453257e66c2c53dc961611fd2bb55c729e0f5/src/index.ts#L61-L92).

## get_ga4_traffic_summary

Runs a single date-range report with sessions, totalUsers, newUsers, screenPageViews, engagedSessions and conversions; returns the raw API response data as JSON text.

<details>
<summary>Full registered description</summary>

```text
Get GA4 traffic summary for a property and date range.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `propertyId` | Yes | string | Not declared |
| `startDate` | Yes | string | Not declared |
| `endDate` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "propertyId": {
      "type": "string"
    },
    "startDate": {
      "type": "string",
      "description": "YYYY-MM-DD or relative date like 30daysAgo"
    },
    "endDate": {
      "type": "string",
      "description": "YYYY-MM-DD or today"
    }
  },
  "required": [
    "propertyId",
    "startDate",
    "endDate"
  ],
  "additionalProperties": false
}
```

</details>

Source: [src/index.ts:94](https://github.com/administrator-prog/ga4-mcp/blob/5a2453257e66c2c53dc961611fd2bb55c729e0f5/src/index.ts#L94-L122).

## get_ga4_top_landing_pages

Runs a report grouped by landingPagePlusQueryString with sessions, totalUsers, engagedSessions and conversions, passing the numeric limit as a string. Returns raw report data.

<details>
<summary>Full registered description</summary>

```text
Get top landing pages from GA4.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `propertyId` | Yes | string | Not declared |
| `startDate` | Yes | string | Not declared |
| `endDate` | Yes | string | Not declared |
| `limit` | No | number | 20 |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "propertyId": {
      "type": "string"
    },
    "startDate": {
      "type": "string"
    },
    "endDate": {
      "type": "string"
    },
    "limit": {
      "type": "number",
      "default": 20
    }
  },
  "required": [
    "propertyId",
    "startDate",
    "endDate"
  ],
  "additionalProperties": false
}
```

</details>

- limit is an unconstrained number, not restricted to positive integers; the handler stringifies it for the GA API.
- No orderBys is supplied, so the handler does not explicitly sort the returned rows.

Source: [src/index.ts:124](https://github.com/administrator-prog/ga4-mcp/blob/5a2453257e66c2c53dc961611fd2bb55c729e0f5/src/index.ts#L124-L153).

## get_ga4_traffic_by_channel

Runs a report grouped by sessionDefaultChannelGroup, sessionSource and sessionMedium with sessions, totalUsers and conversions. Passes limit as a string and returns raw report data.

<details>
<summary>Full registered description</summary>

```text
Get traffic grouped by GA4 default channel group, source and medium.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `propertyId` | Yes | string | Not declared |
| `startDate` | Yes | string | Not declared |
| `endDate` | Yes | string | Not declared |
| `limit` | No | number | 50 |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "propertyId": {
      "type": "string"
    },
    "startDate": {
      "type": "string"
    },
    "endDate": {
      "type": "string"
    },
    "limit": {
      "type": "number",
      "default": 50
    }
  },
  "required": [
    "propertyId",
    "startDate",
    "endDate"
  ],
  "additionalProperties": false
}
```

</details>

- limit is an unconstrained number, not restricted to positive integers; the handler stringifies it for the GA API.
- No orderBys is supplied, so the handler does not explicitly sort the returned rows.

Source: [src/index.ts:155](https://github.com/administrator-prog/ga4-mcp/blob/5a2453257e66c2c53dc961611fd2bb55c729e0f5/src/index.ts#L155-L187).

## compare_ga4_date_ranges

Runs one report with named current and previous date ranges and sessions, totalUsers, newUsers, screenPageViews, engagedSessions and conversions. Returns raw report data without calculating comparison deltas.

<details>
<summary>Full registered description</summary>

```text
Compare GA4 traffic between two date ranges.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `propertyId` | Yes | string | Not declared |
| `currentStart` | Yes | string | Not declared |
| `currentEnd` | Yes | string | Not declared |
| `previousStart` | Yes | string | Not declared |
| `previousEnd` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "propertyId": {
      "type": "string"
    },
    "currentStart": {
      "type": "string"
    },
    "currentEnd": {
      "type": "string"
    },
    "previousStart": {
      "type": "string"
    },
    "previousEnd": {
      "type": "string"
    }
  },
  "required": [
    "propertyId",
    "currentStart",
    "currentEnd",
    "previousStart",
    "previousEnd"
  ],
  "additionalProperties": false
}
```

</details>

Source: [src/index.ts:189](https://github.com/administrator-prog/ga4-mcp/blob/5a2453257e66c2c53dc961611fd2bb55c729e0f5/src/index.ts#L189-L222).

## analyse_organic_performance

Runs a report grouped by landingPagePlusQueryString and deviceCategory, filtered to exact sessionDefaultChannelGroup Organic Search, with sessions, totalUsers, engagedSessions, engagementRate, averageSessionDuration, screenPageViews and conversions. Orders sessions descending and returns raw report data.

<details>
<summary>Full registered description</summary>

```text
Analyse organic traffic quality, engagement and conversions for a GA4 property.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `propertyId` | Yes | string | Not declared |
| `startDate` | Yes | string | Not declared |
| `endDate` | Yes | string | Not declared |
| `limit` | No | number | 25 |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "propertyId": {
      "type": "string"
    },
    "startDate": {
      "type": "string"
    },
    "endDate": {
      "type": "string"
    },
    "limit": {
      "type": "number",
      "default": 25
    }
  },
  "required": [
    "propertyId",
    "startDate",
    "endDate"
  ],
  "additionalProperties": false
}
```

</details>

- limit is an unconstrained number, not restricted to positive integers; the handler stringifies it for the GA API.

Source: [src/index.ts:225](https://github.com/administrator-prog/ga4-mcp/blob/5a2453257e66c2c53dc961611fd2bb55c729e0f5/src/index.ts#L225-L262).

## analyse_landing_page

Runs a report grouped by landingPagePlusQueryString, sessionDefaultChannelGroup and deviceCategory, filtered by landingPagePlusQueryString CONTAINS pagePath. Requests sessions, totalUsers, engagedSessions, engagementRate, averageSessionDuration, screenPageViews, conversions and eventCount with fixed limit 50. Returns raw report data.

<details>
<summary>Full registered description</summary>

```text
Diagnose behaviour and conversion performance for one landing page.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `propertyId` | Yes | string | Not declared |
| `pagePath` | Yes | string | Not declared |
| `startDate` | Yes | string | Not declared |
| `endDate` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "propertyId": {
      "type": "string"
    },
    "pagePath": {
      "type": "string",
      "description": "Example: /property/for-sale/"
    },
    "startDate": {
      "type": "string"
    },
    "endDate": {
      "type": "string"
    }
  },
  "required": [
    "propertyId",
    "pagePath",
    "startDate",
    "endDate"
  ],
  "additionalProperties": false
}
```

</details>

Source: [src/index.ts:264](https://github.com/administrator-prog/ga4-mcp/blob/5a2453257e66c2c53dc961611fd2bb55c729e0f5/src/index.ts#L264-L301).

## analyse_conversion_drop

Runs a report for named current and previous date ranges grouped by landingPagePlusQueryString and deviceCategory, filtered to an exact channel. Requests sessions, engagedSessions, engagementRate, averageSessionDuration and conversions, ordered by sessions descending with fixed limit 50. Returns raw data without computing or attributing a conversion drop.

<details>
<summary>Full registered description</summary>

```text
Compare conversion performance between two date ranges and show where the drop may be coming from.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `propertyId` | Yes | string | Not declared |
| `currentStart` | Yes | string | Not declared |
| `currentEnd` | Yes | string | Not declared |
| `previousStart` | Yes | string | Not declared |
| `previousEnd` | Yes | string | Not declared |
| `channel` | No | string | "Organic Search" |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "propertyId": {
      "type": "string"
    },
    "currentStart": {
      "type": "string"
    },
    "currentEnd": {
      "type": "string"
    },
    "previousStart": {
      "type": "string"
    },
    "previousEnd": {
      "type": "string"
    },
    "channel": {
      "type": "string",
      "default": "Organic Search"
    }
  },
  "required": [
    "propertyId",
    "currentStart",
    "currentEnd",
    "previousStart",
    "previousEnd"
  ],
  "additionalProperties": false
}
```

</details>

Source: [src/index.ts:303](https://github.com/administrator-prog/ga4-mcp/blob/5a2453257e66c2c53dc961611fd2bb55c729e0f5/src/index.ts#L303-L343).

## analyse_devices

Runs a deviceCategory report with sessions, totalUsers, engagedSessions, engagementRate, averageSessionDuration and conversions. Adds an exact sessionDefaultChannelGroup filter only when channel is truthy. Returns raw report data.

<details>
<summary>Full registered description</summary>

```text
Compare GA4 performance by device category.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `propertyId` | Yes | string | Not declared |
| `startDate` | Yes | string | Not declared |
| `endDate` | Yes | string | Not declared |
| `channel` | No | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "propertyId": {
      "type": "string"
    },
    "startDate": {
      "type": "string"
    },
    "endDate": {
      "type": "string"
    },
    "channel": {
      "type": "string"
    }
  },
  "required": [
    "propertyId",
    "startDate",
    "endDate"
  ],
  "additionalProperties": false
}
```

</details>

Source: [src/index.ts:345](https://github.com/administrator-prog/ga4-mcp/blob/5a2453257e66c2c53dc961611fd2bb55c729e0f5/src/index.ts#L345-L379).

## analyse_events_by_page

Runs a pagePath and eventName report with eventCount, totalUsers and conversions, ordered by eventCount descending. Adds a pagePath CONTAINS filter only when pagePath is truthy, passes limit as a string and returns raw report data.

<details>
<summary>Full registered description</summary>

```text
Show key events and user actions by page.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `propertyId` | Yes | string | Not declared |
| `startDate` | Yes | string | Not declared |
| `endDate` | Yes | string | Not declared |
| `pagePath` | No | string | Not declared |
| `limit` | No | number | 50 |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "propertyId": {
      "type": "string"
    },
    "startDate": {
      "type": "string"
    },
    "endDate": {
      "type": "string"
    },
    "pagePath": {
      "type": "string"
    },
    "limit": {
      "type": "number",
      "default": 50
    }
  },
  "required": [
    "propertyId",
    "startDate",
    "endDate"
  ],
  "additionalProperties": false
}
```

</details>

- limit is an unconstrained number, not restricted to positive integers; the handler stringifies it for the GA API.

Source: [src/index.ts:381](https://github.com/administrator-prog/ga4-mcp/blob/5a2453257e66c2c53dc961611fd2bb55c729e0f5/src/index.ts#L381-L411).

## analyse_site_search

Runs a report grouped by searchTerm with eventCount and totalUsers, ordered by eventCount descending, passing limit as a string. Returns raw report data.

<details>
<summary>Full registered description</summary>

```text
Analyse internal site search behaviour if GA4 search_term events are tracked.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `propertyId` | Yes | string | Not declared |
| `startDate` | Yes | string | Not declared |
| `endDate` | Yes | string | Not declared |
| `limit` | No | number | 50 |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "propertyId": {
      "type": "string"
    },
    "startDate": {
      "type": "string"
    },
    "endDate": {
      "type": "string"
    },
    "limit": {
      "type": "number",
      "default": 50
    }
  },
  "required": [
    "propertyId",
    "startDate",
    "endDate"
  ],
  "additionalProperties": false
}
```

</details>

- limit is an unconstrained number, not restricted to positive integers; the handler stringifies it for the GA API.

Source: [src/index.ts:413](https://github.com/administrator-prog/ga4-mcp/blob/5a2453257e66c2c53dc961611fd2bb55c729e0f5/src/index.ts#L413-L436).

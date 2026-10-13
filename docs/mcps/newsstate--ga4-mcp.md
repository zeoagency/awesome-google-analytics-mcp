# Newsstate/ga4-mcp

[Catalog](../../README.md) · [All tool names](../tool-index.md) · [Upstream](https://github.com/Newsstate/ga4-mcp) · [JSON](../../data/mcps/newsstate--ga4-mcp.json)

**11 tools:** 7 GA4, 4 other-service or server-support tools. Reviewed source: [`54ba34d17043`](https://github.com/Newsstate/ga4-mcp/tree/54ba34d170438ad186f78cf412b0aaefd6ebe6c0).

Descriptions and parameter schemas come from the registered source definitions. Generated schemas are reconstructed from annotations or validators; live `tools/list` and authenticated API calls were not run. Loose objects remain loose.

<details>
<summary>Exposure and compatibility notes</summary>

- Source review only, no tools/list or live requests. HEAD verified against supplied revision.
- HTTP MCP route uses its own TOOLS_LIST and dispatcher, not buildMCPServer. Alternate unused SDK registrations are preserved per tool with complete Zod-derived schemas/descriptions. No optional modules or permission tiers found.
- HTTP calls require bearer access token validated via oauth2 tokeninfo or stored token cookie. Cookie OAuth client can refresh expired credentials. GA4 and Search Console read-only scopes configured in lib/google.ts:58-63.
- No install/build/runtime check performed. Dependencies and Next.js entrypoint exist; no definite unusable entrypoint found. OAuth configuration and valid credentials required.

</details>

## Tools

| Tool | Scope | Effect |
| --- | --- | --- |
| [`list_properties`](#list_properties) | GA4 | read |
| [`run_report`](#run_report) | GA4 | read |
| [`run_realtime_report`](#run_realtime_report) | GA4 | read |
| [`get_top_pages`](#get_top_pages) | GA4 | read |
| [`get_traffic_sources`](#get_traffic_sources) | GA4 | read |
| [`get_audience_overview`](#get_audience_overview) | GA4 | read |
| [`get_events`](#get_events) | GA4 | read |
| [`list_search_console_sites`](#list_search_console_sites) | Other service | read |
| [`get_search_queries`](#get_search_queries) | Other service | read |
| [`get_search_pages`](#get_search_pages) | Other service | read |
| [`get_search_performance`](#get_search_performance) | Other service | read |

## list_properties

Calls GA4 Admin v1beta accountSummaries.list({}) once, flattens account property summaries to name/displayName; timezone and currency undefined. Returns JSON text array.

<details>
<summary>Full registered description</summary>

```text
List all GA4 properties accessible by the authenticated user.
```

</details>

No named input parameters are declared.

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {}
}
```

</details>

- HTTP dispatcher does not validate advertised schemas; defaults exist in implementation only.
- No pagination loop for accountSummaries.list; may omit properties on subsequent pages.

Source: [app/api/mcp/route.ts:22](https://github.com/Newsstate/ga4-mcp/blob/54ba34d170438ad186f78cf412b0aaefd6ebe6c0/app/api/mcp/route.ts#L22-L22) · [app/api/mcp/route.ts:203](https://github.com/Newsstate/ga4-mcp/blob/54ba34d170438ad186f78cf412b0aaefd6ebe6c0/app/api/mcp/route.ts#L203-L206) · [lib/ga4.ts:38](https://github.com/Newsstate/ga4-mcp/blob/54ba34d170438ad186f78cf412b0aaefd6ebe6c0/lib/ga4.ts#L38-L66).

## run_report

Calls GA4 Data v1beta runReport with property prefix normalized, one date range (defaults 7daysAgo/today), metric names (default sessions/activeUsers), optional dimension names and limit (default 100). No orderByMetric forwarded. Returns JSON text with headers, rows and rowCount.

<details>
<summary>Full registered description</summary>

```text
Run a GA4 analytics report for a date range.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `propertyId` | Yes | string | Not declared |
| `metrics` | No | array of string | Not declared |
| `dimensions` | No | array of string | Not declared |
| `startDate` | No | string | Not declared |
| `endDate` | No | string | Not declared |
| `limit` | No | number | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "propertyId": {
      "type": "string"
    },
    "metrics": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "dimensions": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "startDate": {
      "type": "string"
    },
    "endDate": {
      "type": "string"
    },
    "limit": {
      "type": "number"
    }
  },
  "required": [
    "propertyId"
  ]
}
```

</details>

- HTTP dispatcher does not validate advertised schemas; defaults exist in implementation only.

Source: [app/api/mcp/route.ts:23](https://github.com/Newsstate/ga4-mcp/blob/54ba34d170438ad186f78cf412b0aaefd6ebe6c0/app/api/mcp/route.ts#L23-L23) · [app/api/mcp/route.ts:207](https://github.com/Newsstate/ga4-mcp/blob/54ba34d170438ad186f78cf412b0aaefd6ebe6c0/app/api/mcp/route.ts#L207-L217) · [lib/ga4.ts:70](https://github.com/Newsstate/ga4-mcp/blob/54ba34d170438ad186f78cf412b0aaefd6ebe6c0/lib/ga4.ts#L70-L98).

## run_realtime_report

Calls GA4 Data v1beta runRealtimeReport with normalized property and metric names (default activeUsers). Endpoint forwards neither dimensions nor limit; helper uses empty dimensions and limit 50. Returns headers, rows and rowCount as JSON text.

<details>
<summary>Full registered description</summary>

```text
Get realtime active users in the last 30 minutes.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `propertyId` | Yes | string | Not declared |
| `metrics` | No | array of string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "propertyId": {
      "type": "string"
    },
    "metrics": {
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  },
  "required": [
    "propertyId"
  ]
}
```

</details>

- HTTP dispatcher does not validate advertised schemas; defaults exist in implementation only.

Source: [app/api/mcp/route.ts:24](https://github.com/Newsstate/ga4-mcp/blob/54ba34d170438ad186f78cf412b0aaefd6ebe6c0/app/api/mcp/route.ts#L24-L24) · [app/api/mcp/route.ts:218](https://github.com/Newsstate/ga4-mcp/blob/54ba34d170438ad186f78cf412b0aaefd6ebe6c0/app/api/mcp/route.ts#L218-L224) · [lib/ga4.ts:102](https://github.com/Newsstate/ga4-mcp/blob/54ba34d170438ad186f78cf412b0aaefd6ebe6c0/lib/ga4.ts#L102-L126).

## get_top_pages

Runs GA4 runReport for 7daysAgo/today by default with screenPageViews,sessions,bounceRate,averageSessionDuration and pagePath,pageTitle; descending screenPageViews; limit defaults 10. Returns headers, rows and rowCount.

<details>
<summary>Full registered description</summary>

```text
Get top pages by page views.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `propertyId` | Yes | string | Not declared |
| `startDate` | No | string | Not declared |
| `endDate` | No | string | Not declared |
| `limit` | No | number | Not declared |

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
      "type": "number"
    }
  },
  "required": [
    "propertyId"
  ]
}
```

</details>

- HTTP dispatcher does not validate advertised schemas; defaults exist in implementation only.

Source: [app/api/mcp/route.ts:25](https://github.com/Newsstate/ga4-mcp/blob/54ba34d170438ad186f78cf412b0aaefd6ebe6c0/app/api/mcp/route.ts#L25-L25) · [app/api/mcp/route.ts:225](https://github.com/Newsstate/ga4-mcp/blob/54ba34d170438ad186f78cf412b0aaefd6ebe6c0/app/api/mcp/route.ts#L225-L236) · [lib/ga4.ts:70](https://github.com/Newsstate/ga4-mcp/blob/54ba34d170438ad186f78cf412b0aaefd6ebe6c0/lib/ga4.ts#L70-L98).

## get_traffic_sources

Runs GA4 runReport for 30daysAgo/today by default with sessions,activeUsers,bounceRate and sessionDefaultChannelGroup,sessionSource,sessionMedium; descending sessions; limit defaults 20.

<details>
<summary>Full registered description</summary>

```text
Breakdown of sessions by traffic source and medium.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `propertyId` | Yes | string | Not declared |
| `startDate` | No | string | Not declared |
| `endDate` | No | string | Not declared |
| `limit` | No | number | Not declared |

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
      "type": "number"
    }
  },
  "required": [
    "propertyId"
  ]
}
```

</details>

- HTTP dispatcher does not validate advertised schemas; defaults exist in implementation only.
- Unused builder includes conversions metric; HTTP handler does not.

Source: [app/api/mcp/route.ts:26](https://github.com/Newsstate/ga4-mcp/blob/54ba34d170438ad186f78cf412b0aaefd6ebe6c0/app/api/mcp/route.ts#L26-L26) · [app/api/mcp/route.ts:237](https://github.com/Newsstate/ga4-mcp/blob/54ba34d170438ad186f78cf412b0aaefd6ebe6c0/app/api/mcp/route.ts#L237-L248) · [lib/ga4.ts:70](https://github.com/Newsstate/ga4-mcp/blob/54ba34d170438ad186f78cf412b0aaefd6ebe6c0/lib/ga4.ts#L70-L98).

## get_audience_overview

Runs GA4 runReport for 30daysAgo/today by default with activeUsers,sessions,newUsers; dimension groupBy defaults country; fixed limit 20; descending activeUsers.

<details>
<summary>Full registered description</summary>

```text
Get audience demographics: country, device, browser.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `propertyId` | Yes | string | Not declared |
| `startDate` | No | string | Not declared |
| `endDate` | No | string | Not declared |
| `groupBy` | No | string | Not declared |

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
    "groupBy": {
      "type": "string",
      "enum": [
        "country",
        "deviceCategory",
        "browser",
        "operatingSystem"
      ]
    }
  },
  "required": [
    "propertyId"
  ]
}
```

</details>

- HTTP dispatcher does not validate advertised schemas; defaults exist in implementation only.

Source: [app/api/mcp/route.ts:27](https://github.com/Newsstate/ga4-mcp/blob/54ba34d170438ad186f78cf412b0aaefd6ebe6c0/app/api/mcp/route.ts#L27-L27) · [app/api/mcp/route.ts:249](https://github.com/Newsstate/ga4-mcp/blob/54ba34d170438ad186f78cf412b0aaefd6ebe6c0/app/api/mcp/route.ts#L249-L260) · [lib/ga4.ts:70](https://github.com/Newsstate/ga4-mcp/blob/54ba34d170438ad186f78cf412b0aaefd6ebe6c0/lib/ga4.ts#L70-L98).

## get_events

Runs GA4 runReport for 7daysAgo/today by default with eventCount,eventCountPerUser,totalUsers and eventName; descending eventCount; limit defaults 25.

<details>
<summary>Full registered description</summary>

```text
Get event counts for a date range.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `propertyId` | Yes | string | Not declared |
| `startDate` | No | string | Not declared |
| `endDate` | No | string | Not declared |
| `limit` | No | number | Not declared |

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
      "type": "number"
    }
  },
  "required": [
    "propertyId"
  ]
}
```

</details>

- HTTP dispatcher does not validate advertised schemas; defaults exist in implementation only.

Source: [app/api/mcp/route.ts:28](https://github.com/Newsstate/ga4-mcp/blob/54ba34d170438ad186f78cf412b0aaefd6ebe6c0/app/api/mcp/route.ts#L28-L28) · [app/api/mcp/route.ts:261](https://github.com/Newsstate/ga4-mcp/blob/54ba34d170438ad186f78cf412b0aaefd6ebe6c0/app/api/mcp/route.ts#L261-L272) · [lib/ga4.ts:70](https://github.com/Newsstate/ga4-mcp/blob/54ba34d170438ad186f78cf412b0aaefd6ebe6c0/lib/ga4.ts#L70-L98).

## list_search_console_sites

Calls Search Console webmasters v3 sites.list; maps siteEntry to siteUrl and permissionLevel, returns JSON text array.

<details>
<summary>Full registered description</summary>

```text
List all websites verified in Google Search Console.
```

</details>

No named input parameters are declared.

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {}
}
```

</details>

- HTTP dispatcher does not validate advertised schemas; defaults exist in implementation only.

Source: [app/api/mcp/route.ts:29](https://github.com/Newsstate/ga4-mcp/blob/54ba34d170438ad186f78cf412b0aaefd6ebe6c0/app/api/mcp/route.ts#L29-L29) · [app/api/mcp/route.ts:273](https://github.com/Newsstate/ga4-mcp/blob/54ba34d170438ad186f78cf412b0aaefd6ebe6c0/app/api/mcp/route.ts#L273-L277) · [lib/searchconsole.ts:23](https://github.com/Newsstate/ga4-mcp/blob/54ba34d170438ad186f78cf412b0aaefd6ebe6c0/lib/searchconsole.ts#L23-L30).

## get_search_queries

Calls Search Console webmasters v3 searchanalytics.query with siteUrl, startDate (default 28daysAgo), endDate (default today), dimensions [query], rowLimit (default 25) and startRow 0. Returns rows with keys,clicks,impressions,CTR rounded as percentage,position rounded to one decimal and rowCount equal to returned rows.

<details>
<summary>Full registered description</summary>

```text
Get top search queries from Google Search Console with clicks, impressions, CTR and position.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `siteUrl` | Yes | string | Not declared |
| `startDate` | No | string | Not declared |
| `endDate` | No | string | Not declared |
| `limit` | No | number | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "siteUrl": {
      "type": "string"
    },
    "startDate": {
      "type": "string"
    },
    "endDate": {
      "type": "string"
    },
    "limit": {
      "type": "number"
    }
  },
  "required": [
    "siteUrl"
  ]
}
```

</details>

- HTTP dispatcher does not validate advertised schemas; defaults exist in implementation only.
- Relative date defaults are passed unchanged to Search Console; no conversion to YYYY-MM-DD exists, so default requests can fail.

Source: [app/api/mcp/route.ts:30](https://github.com/Newsstate/ga4-mcp/blob/54ba34d170438ad186f78cf412b0aaefd6ebe6c0/app/api/mcp/route.ts#L30-L30) · [app/api/mcp/route.ts:278](https://github.com/Newsstate/ga4-mcp/blob/54ba34d170438ad186f78cf412b0aaefd6ebe6c0/app/api/mcp/route.ts#L278-L295) · [lib/searchconsole.ts:34](https://github.com/Newsstate/ga4-mcp/blob/54ba34d170438ad186f78cf412b0aaefd6ebe6c0/lib/searchconsole.ts#L34-L60).

## get_search_pages

Calls Search Console webmasters v3 searchanalytics.query with siteUrl, startDate (default 28daysAgo), endDate (default today), dimensions [page], rowLimit (default 25) and startRow 0. Returns rows with keys,clicks,impressions,CTR rounded as percentage,position rounded to one decimal and rowCount equal to returned rows.

<details>
<summary>Full registered description</summary>

```text
Get top pages from Google Search Console by clicks and impressions.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `siteUrl` | Yes | string | Not declared |
| `startDate` | No | string | Not declared |
| `endDate` | No | string | Not declared |
| `limit` | No | number | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "siteUrl": {
      "type": "string"
    },
    "startDate": {
      "type": "string"
    },
    "endDate": {
      "type": "string"
    },
    "limit": {
      "type": "number"
    }
  },
  "required": [
    "siteUrl"
  ]
}
```

</details>

- HTTP dispatcher does not validate advertised schemas; defaults exist in implementation only.
- Relative date defaults are passed unchanged to Search Console; no conversion to YYYY-MM-DD exists, so default requests can fail.

Source: [app/api/mcp/route.ts:31](https://github.com/Newsstate/ga4-mcp/blob/54ba34d170438ad186f78cf412b0aaefd6ebe6c0/app/api/mcp/route.ts#L31-L31) · [app/api/mcp/route.ts:278](https://github.com/Newsstate/ga4-mcp/blob/54ba34d170438ad186f78cf412b0aaefd6ebe6c0/app/api/mcp/route.ts#L278-L295) · [lib/searchconsole.ts:34](https://github.com/Newsstate/ga4-mcp/blob/54ba34d170438ad186f78cf412b0aaefd6ebe6c0/lib/searchconsole.ts#L34-L60).

## get_search_performance

Calls Search Console webmasters v3 searchanalytics.query with siteUrl, startDate (default 28daysAgo), endDate (default today), dimensions [date], rowLimit (default 25) and startRow 0. Returns rows with keys,clicks,impressions,CTR rounded as percentage,position rounded to one decimal and rowCount equal to returned rows.

<details>
<summary>Full registered description</summary>

```text
Get daily search performance trend from Google Search Console.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `siteUrl` | Yes | string | Not declared |
| `startDate` | No | string | Not declared |
| `endDate` | No | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "siteUrl": {
      "type": "string"
    },
    "startDate": {
      "type": "string"
    },
    "endDate": {
      "type": "string"
    }
  },
  "required": [
    "siteUrl"
  ]
}
```

</details>

- HTTP dispatcher does not validate advertised schemas; defaults exist in implementation only.
- Relative date defaults are passed unchanged to Search Console; no conversion to YYYY-MM-DD exists, so default requests can fail.
- Unused builder uses fixed rowLimit 90; HTTP handler defaults to 25 and accepts unadvertised limit.

Source: [app/api/mcp/route.ts:32](https://github.com/Newsstate/ga4-mcp/blob/54ba34d170438ad186f78cf412b0aaefd6ebe6c0/app/api/mcp/route.ts#L32-L32) · [app/api/mcp/route.ts:278](https://github.com/Newsstate/ga4-mcp/blob/54ba34d170438ad186f78cf412b0aaefd6ebe6c0/app/api/mcp/route.ts#L278-L295) · [lib/searchconsole.ts:34](https://github.com/Newsstate/ga4-mcp/blob/54ba34d170438ad186f78cf412b0aaefd6ebe6c0/lib/searchconsole.ts#L34-L60).

# Callince/ga4-mcp-server

[Catalog](../../README.md) · [All tool names](../tool-index.md) · [Upstream](https://github.com/Callince/ga4-mcp-server) · [JSON](../../data/mcps/callince--ga4-mcp-server.json)

**4 tools:** 4 GA4, 0 other-service or server-support tools. Reviewed source: [`4b0eeba11a24`](https://github.com/Callince/ga4-mcp-server/tree/4b0eeba11a24aaf1b20fdee12209db5d4d795371).

Descriptions and parameter schemas come from the registered source definitions. Generated schemas are reconstructed from annotations or validators; live `tools/list` and authenticated API calls were not run. Loose objects remain loose.

<details>
<summary>Exposure and compatibility notes</summary>

- Source review only; no tools/list or live requests. HEAD matches the supplied revision.
- All four tools are unconditionally registered in normal server mode; --login performs local OAuth browser consent/token persistence and exits, and is not an MCP tool.
- Calls require a saved OAuth token with refresh_token, client_id, and client_secret at GA4_TOKEN_PATH or ~/.ga4-mcp/token.json. Clients initialize lazily, so absent authentication does not block tool listing. OAuth uses analytics.readonly.
- Property-dependent calls require the property argument or GA4_PROPERTY_ID. No explicit input-schema validation occurs in the call dispatcher; handler/API errors are returned as MCP isError text.
- Entrypoint/dependencies are declared in package.json and manifest.json. No authenticated runtime viability test was performed.

</details>

## Tools

| Tool | Scope | Effect |
| --- | --- | --- |
| [`list_properties`](#list_properties) | GA4 | read |
| [`run_report`](#run_report) | GA4 | read |
| [`run_realtime_report`](#run_realtime_report) | GA4 | read |
| [`get_metadata`](#get_metadata) | GA4 | read |

## list_properties

Calls Admin listAccountSummaries with an empty request; returns account names/resources and property names/resources/numeric IDs, or a message when no accounts are visible.

<details>
<summary>Full registered description</summary>

```text
List the GA4 accounts and properties the signed-in Google account can access, with their numeric property IDs. Use this first to discover the property ID to pass to other tools.
```

</details>

No named input parameters are declared.

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {},
  "additionalProperties": false
}
```

</details>

Source: [server/index.js:236](https://github.com/Callince/ga4-mcp-server/blob/4b0eeba11a24aaf1b20fdee12209db5d4d795371/server/index.js#L236-L241) · [server/index.js:138](https://github.com/Callince/ga4-mcp-server/blob/4b0eeba11a24aaf1b20fdee12209db5d4d795371/server/index.js#L138-L153) · [server/index.js:329](https://github.com/Callince/ga4-mcp-server/blob/4b0eeba11a24aaf1b20fdee12209db5d4d795371/server/index.js#L329-L334) · [server/index.js:343](https://github.com/Callince/ga4-mcp-server/blob/4b0eeba11a24aaf1b20fdee12209db5d4d795371/server/index.js#L343-L362).

## run_report

Resolves the property from the argument or GA4_PROPERTY_ID, normalizes it to properties/{id}, converts dimension and metric names to name objects, and calls Data API runReport with one date range. Forwards dimensionFilter and orderBys unchanged when truthy; defaults dates to 7daysAgo/today and limit to 100. Returns property/date range and report headers, rowCount, and flattened rows.

<details>
<summary>Full registered description</summary>

```text
Run a GA4 core report. Provide metric API names (e.g. activeUsers, sessions, screenPageViews) and optional dimension API names (e.g. date, country, pagePath). Date range defaults to the last 7 days.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property` | No | string | Not declared |
| `startDate` | No | string | Not declared |
| `endDate` | No | string | Not declared |
| `dimensions` | No | array of string | Not declared |
| `metrics` | Yes | array of string | Not declared |
| `limit` | No | number | Not declared |
| `dimensionFilter` | No | object | Not declared |
| `orderBys` | No | array of any | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "property": {
      "type": "string",
      "description": "GA4 property ID, numeric (e.g. 123456789) or 'properties/123456789'. Omit to use the configured default."
    },
    "startDate": {
      "type": "string",
      "description": "Start date as YYYY-MM-DD or relative ('7daysAgo', 'yesterday', 'today'). Default '7daysAgo'."
    },
    "endDate": {
      "type": "string",
      "description": "End date. Default 'today'."
    },
    "dimensions": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Dimension API names, e.g. ['date','country']."
    },
    "metrics": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Metric API names, e.g. ['activeUsers','sessions']. At least one required."
    },
    "limit": {
      "type": "number",
      "description": "Max rows to return (default 100)."
    },
    "dimensionFilter": {
      "type": "object",
      "description": "Optional GA4 FilterExpression applied to dimensions (passed through to the API)."
    },
    "orderBys": {
      "type": "array",
      "description": "Optional GA4 OrderBy array (passed through to the API)."
    }
  },
  "required": [
    "metrics"
  ]
}
```

</details>

- dimensionFilter is an unrestricted object and orderBys is an array without an items schema; their full values are forwarded to the API.
- The metrics description says at least one is required, but the schema has no minItems and the handler does not enforce nonempty metrics.
- Date and limit defaults exist in the handler/descriptions, not JSON Schema default keywords.

Source: [server/index.js:242](https://github.com/Callince/ga4-mcp-server/blob/4b0eeba11a24aaf1b20fdee12209db5d4d795371/server/index.js#L242-L284) · [server/index.js:155](https://github.com/Callince/ga4-mcp-server/blob/4b0eeba11a24aaf1b20fdee12209db5d4d795371/server/index.js#L155-L169) · [server/index.js:329](https://github.com/Callince/ga4-mcp-server/blob/4b0eeba11a24aaf1b20fdee12209db5d4d795371/server/index.js#L329-L334) · [server/index.js:343](https://github.com/Callince/ga4-mcp-server/blob/4b0eeba11a24aaf1b20fdee12209db5d4d795371/server/index.js#L343-L362) · [server/index.js:88](https://github.com/Callince/ga4-mcp-server/blob/4b0eeba11a24aaf1b20fdee12209db5d4d795371/server/index.js#L88-L104) · [server/index.js:106](https://github.com/Callince/ga4-mcp-server/blob/4b0eeba11a24aaf1b20fdee12209db5d4d795371/server/index.js#L106-L125).

## run_realtime_report

Resolves and normalizes property, converts dimension and metric names to name objects, and calls Data API runRealtimeReport with limit defaulting to 100. Returns property, a fixed last 30 minutes window label, and report headers, rowCount, and flattened rows.

<details>
<summary>Full registered description</summary>

```text
Run a GA4 realtime report covering roughly the last 30 minutes. Provide metric API names (e.g. activeUsers) and optional realtime dimensions (e.g. country, unifiedScreenName).
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property` | No | string | Not declared |
| `dimensions` | No | array of string | Not declared |
| `metrics` | Yes | array of string | Not declared |
| `limit` | No | number | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "property": {
      "type": "string",
      "description": "GA4 property ID (numeric or 'properties/...'). Omit to use the configured default."
    },
    "dimensions": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Realtime dimension API names."
    },
    "metrics": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Realtime metric API names. At least one required."
    },
    "limit": {
      "type": "number",
      "description": "Max rows (default 100)."
    }
  },
  "required": [
    "metrics"
  ]
}
```

</details>

- The metrics description says at least one is required, but the schema has no minItems and the handler does not enforce nonempty metrics.
- The limit default exists in the handler/description, not a JSON Schema default keyword.

Source: [server/index.js:285](https://github.com/Callince/ga4-mcp-server/blob/4b0eeba11a24aaf1b20fdee12209db5d4d795371/server/index.js#L285-L311) · [server/index.js:171](https://github.com/Callince/ga4-mcp-server/blob/4b0eeba11a24aaf1b20fdee12209db5d4d795371/server/index.js#L171-L180) · [server/index.js:329](https://github.com/Callince/ga4-mcp-server/blob/4b0eeba11a24aaf1b20fdee12209db5d4d795371/server/index.js#L329-L334) · [server/index.js:343](https://github.com/Callince/ga4-mcp-server/blob/4b0eeba11a24aaf1b20fdee12209db5d4d795371/server/index.js#L343-L362) · [server/index.js:88](https://github.com/Callince/ga4-mcp-server/blob/4b0eeba11a24aaf1b20fdee12209db5d4d795371/server/index.js#L88-L104) · [server/index.js:106](https://github.com/Callince/ga4-mcp-server/blob/4b0eeba11a24aaf1b20fdee12209db5d4d795371/server/index.js#L106-L125).

## get_metadata

Resolves and normalizes property and calls Data API getMetadata with properties/{id}/metadata. Returns property plus dimension API/UI names, categories/descriptions, and metric API/UI names, types, categories/descriptions.

<details>
<summary>Full registered description</summary>

```text
List the dimensions and metrics available for a GA4 property (API names, UI names, descriptions). Use this to discover valid names for run_report.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property` | No | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "property": {
      "type": "string",
      "description": "GA4 property ID (numeric or 'properties/...'). Omit to use the configured default."
    }
  }
}
```

</details>

Source: [server/index.js:312](https://github.com/Callince/ga4-mcp-server/blob/4b0eeba11a24aaf1b20fdee12209db5d4d795371/server/index.js#L312-L326) · [server/index.js:182](https://github.com/Callince/ga4-mcp-server/blob/4b0eeba11a24aaf1b20fdee12209db5d4d795371/server/index.js#L182-L201) · [server/index.js:329](https://github.com/Callince/ga4-mcp-server/blob/4b0eeba11a24aaf1b20fdee12209db5d4d795371/server/index.js#L329-L334) · [server/index.js:343](https://github.com/Callince/ga4-mcp-server/blob/4b0eeba11a24aaf1b20fdee12209db5d4d795371/server/index.js#L343-L362) · [server/index.js:88](https://github.com/Callince/ga4-mcp-server/blob/4b0eeba11a24aaf1b20fdee12209db5d4d795371/server/index.js#L88-L104).

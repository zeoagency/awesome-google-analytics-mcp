# buyte-io/GA4-MCP-Server

[Catalog](../../README.md) · [All tool names](../tool-index.md) · [Upstream](https://github.com/buyte-io/GA4-MCP-Server) · [JSON](../../data/mcps/buyte-io--ga4-mcp-server.json)

**4 tools:** 4 GA4, 0 other-service or server-support tools. Reviewed source: [`0c8287619727`](https://github.com/buyte-io/GA4-MCP-Server/tree/0c828761972759a32432c36ed4b32e6af7677acd).

Descriptions and parameter schemas come from the registered source definitions. Generated schemas are reconstructed from annotations or validators; live `tools/list` and authenticated API calls were not run. Loose objects remain loose.

<details>
<summary>Exposure and compatibility notes</summary>

- Source review only; no upstream execution, tools/list, or live requests. Git HEAD matches supplied revision.
- All four tools register unconditionally; service is constructed lazily on first call. No optional tool modules, permission-tier tool inventories, aliases, or further registerTool/tool calls found. REST endpoints in manifest.ts are not MCP tools.
- package.json start/main targets dist/index.js, while tsconfig.json rootDir "." emits src/index.ts to dist/src/index.js. Plain tsc also retains extensionless ESM imports and tsconfig aliases. npm run mcp instead uses tsx src/mcp/cli-entry.ts; Worker transport uses the same shared factory and Workers-specific real REST clients.
- Root wrangler.toml targets dist/src/worker.js. cloudflare/wrangler.toml instead says src/worker.ts relative to its own directory (which has no such source) and contains malformed stray inline-table entries; this alternate config is defective. Worker deployment/build not tested.
- Schemas reconstructed from explicit Zod registration shapes; standard object schemas reject additional properties in JSON Schema conversion while Zod validation strips unknown keys. No runtime schema claim.

</details>

## Tools

| Tool | Scope | Effect |
| --- | --- | --- |
| [`ga4_listAccounts`](#ga4_listaccounts) | GA4 | read |
| [`ga4_listProperties`](#ga4_listproperties) | GA4 | read |
| [`ga4_getMetadata`](#ga4_getmetadata) | GA4 | read |
| [`ga4_runReport`](#ga4_runreport) | GA4 | read |

## ga4_listAccounts

Returns cached or fetched account summaries and nested property summaries as JSON text and structured accounts. Node uses paginated Admin API async iterator; Worker calls REST accountSummaries once.

<details>
<summary>Full registered description</summary>

```text
Return the GA4 accounts visible to the configured service account
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

- No inputSchema supplied in registration; empty object represents SDK no-argument tool.
- Worker ignores nextPageToken; results can omit later pages.

Source: [src/mcp/server.ts:108](https://github.com/buyte-io/GA4-MCP-Server/blob/0c828761972759a32432c36ed4b32e6af7677acd/src/mcp/server.ts#L108-L122) · [src/features/ga4/services/analytics.service.ts:259](https://github.com/buyte-io/GA4-MCP-Server/blob/0c828761972759a32432c36ed4b32e6af7677acd/src/features/ga4/services/analytics.service.ts#L259-L310) · [src/features/ga4/services/analytics.service.worker.ts:169](https://github.com/buyte-io/GA4-MCP-Server/blob/0c828761972759a32432c36ed4b32e6af7677acd/src/features/ga4/services/analytics.service.worker.ts#L169-L204) · [src/features/ga4/services/rest-client.ts:161](https://github.com/buyte-io/GA4-MCP-Server/blob/0c828761972759a32432c36ed4b32e6af7677acd/src/features/ga4/services/rest-client.ts#L161-L178).

## ga4_listProperties

Fetches/caches properties using Admin API parent account filter and returns normalized property summaries as JSON text and structured properties. Node normalizes optional accounts/ prefix.

<details>
<summary>Full registered description</summary>

```text
List properties that belong to a given GA4 account
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `accountId` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "accountId": {
      "type": "string",
      "description": "GA4 account identifier, with or without the accounts/ prefix",
      "minLength": 1
    }
  },
  "required": [
    "accountId"
  ],
  "additionalProperties": false
}
```

</details>

- Worker unconditionally prepends accounts/ in REST filter and parent output, so accountId accounts/123 yields parent:accounts/accounts/123 despite advertised prefix support.
- Worker ignores nextPageToken; Node paginates with listPropertiesAsync.

Source: [src/mcp/server.ts:124](https://github.com/buyte-io/GA4-MCP-Server/blob/0c828761972759a32432c36ed4b32e6af7677acd/src/mcp/server.ts#L124-L139) · [src/mcp/server.ts:52](https://github.com/buyte-io/GA4-MCP-Server/blob/0c828761972759a32432c36ed4b32e6af7677acd/src/mcp/server.ts#L52-L56) · [src/features/ga4/services/analytics.service.ts:317](https://github.com/buyte-io/GA4-MCP-Server/blob/0c828761972759a32432c36ed4b32e6af7677acd/src/features/ga4/services/analytics.service.ts#L317-L368) · [src/features/ga4/services/analytics.service.worker.ts:206](https://github.com/buyte-io/GA4-MCP-Server/blob/0c828761972759a32432c36ed4b32e6af7677acd/src/features/ga4/services/analytics.service.worker.ts#L206-L251) · [src/features/ga4/services/rest-client.ts:183](https://github.com/buyte-io/GA4-MCP-Server/blob/0c828761972759a32432c36ed4b32e6af7677acd/src/features/ga4/services/rest-client.ts#L183-L205).

## ga4_getMetadata

Resolves propertyId or configured default, fails if neither exists, normalizes properties/ prefix and retrieves/caches property dimensions and metrics metadata; returns JSON text and structured metadata.

<details>
<summary>Full registered description</summary>

```text
Retrieve dimensions and metrics metadata for a GA4 property. If propertyId is omitted, falls back to config DEFAULT_GA4_PROPERTY_ID.
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
      "description": "GA4 property identifier, with or without the properties/ prefix",
      "minLength": 1
    }
  },
  "required": [],
  "additionalProperties": false
}
```

</details>

- Omitted propertyId requires DEFAULT_GA4_PROPERTY_ID configured; no schema default exists.

Source: [src/mcp/server.ts:141](https://github.com/buyte-io/GA4-MCP-Server/blob/0c828761972759a32432c36ed4b32e6af7677acd/src/mcp/server.ts#L141-L163) · [src/mcp/server.ts:58](https://github.com/buyte-io/GA4-MCP-Server/blob/0c828761972759a32432c36ed4b32e6af7677acd/src/mcp/server.ts#L58-L63) · [src/features/ga4/services/analytics.service.ts:375](https://github.com/buyte-io/GA4-MCP-Server/blob/0c828761972759a32432c36ed4b32e6af7677acd/src/features/ga4/services/analytics.service.ts#L375-L405) · [src/features/ga4/services/analytics.service.worker.ts:253](https://github.com/buyte-io/GA4-MCP-Server/blob/0c828761972759a32432c36ed4b32e6af7677acd/src/features/ga4/services/analytics.service.worker.ts#L253-L278) · [src/features/ga4/services/rest-client.ts:123](https://github.com/buyte-io/GA4-MCP-Server/blob/0c828761972759a32432c36ed4b32e6af7677acd/src/features/ga4/services/rest-client.ts#L123-L149).

## ga4_runReport

Converts metric/dimension names to GA name objects; uses nonempty dateRanges or startDate/endDate with handler fallbacks 7daysAgo/today; forwards property, metrics, dimensions, dateRanges and limit to Data API runReport. Returns report structured content plus row/header summary and up to three sample rows.

<details>
<summary>Full registered description</summary>

```text
Execute a GA4 report query for the provided property, metrics, and optional dimensions.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `propertyId` | Yes | string | Not declared |
| `metrics` | Yes | array of string | Not declared |
| `dimensions` | No | array of string | Not declared |
| `dateRanges` | No | array of object | Not declared |
| `startDate` | No | string | Not declared |
| `endDate` | No | string | Not declared |
| `limit` | No | integer | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "propertyId": {
      "type": "string",
      "description": "GA4 property identifier, with or without the properties/ prefix",
      "minLength": 1
    },
    "metrics": {
      "type": "array",
      "items": {
        "type": "string",
        "description": "API name of the metric to include in the report",
        "minLength": 1
      },
      "minItems": 1
    },
    "dimensions": {
      "type": "array",
      "items": {
        "type": "string",
        "description": "API name of the dimension to include in the report",
        "minLength": 1
      }
    },
    "dateRanges": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "startDate": {
            "type": "string",
            "description": "Start date (YYYY-MM-DD or relative, e.g. 7daysAgo)"
          },
          "endDate": {
            "type": "string",
            "description": "End date (YYYY-MM-DD or relative, e.g. today)"
          }
        },
        "required": [
          "startDate",
          "endDate"
        ],
        "additionalProperties": false
      }
    },
    "startDate": {
      "type": "string"
    },
    "endDate": {
      "type": "string"
    },
    "limit": {
      "type": "integer",
      "minimum": 1,
      "maximum": 100000
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

- Date strings have no format constraint; dateRanges may be empty and triggers handler fallback. Fallback dates are handler behavior, not schema defaults.
- Underlying services support filters, offset, orderBys and quota options but MCP input schema does not expose them.

Source: [src/mcp/server.ts:165](https://github.com/buyte-io/GA4-MCP-Server/blob/0c828761972759a32432c36ed4b32e6af7677acd/src/mcp/server.ts#L165-L198) · [src/mcp/server.ts:65](https://github.com/buyte-io/GA4-MCP-Server/blob/0c828761972759a32432c36ed4b32e6af7677acd/src/mcp/server.ts#L65-L92) · [src/features/ga4/services/analytics.service.ts:160](https://github.com/buyte-io/GA4-MCP-Server/blob/0c828761972759a32432c36ed4b32e6af7677acd/src/features/ga4/services/analytics.service.ts#L160-L180) · [src/features/ga4/services/analytics.service.worker.ts:98](https://github.com/buyte-io/GA4-MCP-Server/blob/0c828761972759a32432c36ed4b32e6af7677acd/src/features/ga4/services/analytics.service.worker.ts#L98-L122) · [src/features/ga4/services/rest-client.ts:93](https://github.com/buyte-io/GA4-MCP-Server/blob/0c828761972759a32432c36ed4b32e6af7677acd/src/features/ga4/services/rest-client.ts#L93-L121).

# K41R0N/ga4-mcp

[Catalog](../../README.md) · [All tool names](../tool-index.md) · [Upstream](https://github.com/K41R0N/ga4-mcp) · [JSON](../../data/mcps/k41r0n--ga4-mcp.json)

**2 tools:** 2 GA4, 0 other-service or server-support tools. Reviewed source: [`aa90b1568a08`](https://github.com/K41R0N/ga4-mcp/tree/aa90b1568a0800eb4dfdc96700e6c10ef1d36ecd).

Descriptions and parameter schemas come from the registered source definitions. Generated schemas are reconstructed from annotations or validators; live `tools/list` and authenticated API calls were not run. Loose objects remain loose.

<details>
<summary>Exposure and compatibility notes</summary>

- Source review only; no upstream execution, tools/list request, or live API requests.
- Both tools register unconditionally in the sole createMcpHandler callback. The HTTP endpoint requires a bearer token equal to MCP_BEARER_TOKEN via withMcpAuth(required: true).
- Deployment requires Upstash Redis environment configuration, GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET, GOOGLE_REDIRECT_URI, and MCP_BEARER_TOKEN; each selected user must have an OAuth refresh token in Redis. Google OAuth start/callback routes request analytics.readonly and store the token; these HTTP routes are not MCP tools.
- Input schemas reconstructed from explicit Zod registration shapes. additionalProperties false represents the default Zod object conversion; unknown keys are stripped by default validation, rather than a custom strict() constraint.
- No definite entrypoint blocker found by source inspection.

</details>

## Tools

| Tool | Scope | Effect |
| --- | --- | --- |
| [`list_properties`](#list_properties) | GA4 | read |
| [`run_report`](#run_report) | GA4 | read |

## list_properties

Loads google_refresh:<user> from Redis, constructs an AnalyticsAdminServiceClient with authorized-user OAuth credentials and REST fallback, calls listAccountSummaries({}), flattens all returned propertySummaries to account display name, property display name, and propertyId with properties/ removed, and returns pretty-printed JSON in text content. Catches errors and returns diagnostic text with isError true.

<details>
<summary>Full registered description</summary>

```text
Lists GA4 properties YOU have access to. Pass user=<your-email>.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `user` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "user": {
      "type": "string",
      "description": "Your teammate identifier (usually email)."
    }
  },
  "required": [
    "user"
  ],
  "additionalProperties": false
}
```

</details>

- The user string has no email-format constraint; it is a Redis refresh-token lookup identifier.

Source: [app/api/mcp/route.ts:56](https://github.com/K41R0N/ga4-mcp/blob/aa90b1568a0800eb4dfdc96700e6c10ef1d36ecd/app/api/mcp/route.ts#L56-L80) · [app/api/mcp/route.ts:9](https://github.com/K41R0N/ga4-mcp/blob/aa90b1568a0800eb4dfdc96700e6c10ef1d36ecd/app/api/mcp/route.ts#L9-L31).

## run_report

Loads the selected user OAuth refresh token from Redis and calls BetaAnalyticsDataClient.runReport with property properties/<propertyId>, one date range, metrics mapped to name objects, dimensions mapped to name objects (empty when omitted), and the limit (default 100). Returns the entire API response as pretty-printed JSON text. Catches errors and returns diagnostic text with isError true.

<details>
<summary>Full registered description</summary>

```text
Runs a GA4 report as the specified user.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `user` | Yes | string | Not declared |
| `propertyId` | Yes | string | Not declared |
| `startDate` | Yes | string | Not declared |
| `endDate` | Yes | string | Not declared |
| `metrics` | Yes | array of string | Not declared |
| `dimensions` | No | array of string | Not declared |
| `limit` | No | integer | 100 |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "user": {
      "type": "string"
    },
    "propertyId": {
      "type": "string"
    },
    "startDate": {
      "type": "string"
    },
    "endDate": {
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
    "limit": {
      "type": "integer",
      "minimum": 1,
      "maximum": 10000,
      "default": 100
    }
  },
  "required": [
    "user",
    "propertyId",
    "startDate",
    "endDate",
    "metrics"
  ],
  "additionalProperties": false
}
```

</details>

- Schema accepts unrestricted strings for dates and propertyId and allows empty metric/dimension arrays; GA API validity is not checked locally.
- The registration exposes only these report fields, not an arbitrary full runReport request.

Source: [app/api/mcp/route.ts:82](https://github.com/K41R0N/ga4-mcp/blob/aa90b1568a0800eb4dfdc96700e6c10ef1d36ecd/app/api/mcp/route.ts#L82-L113) · [app/api/mcp/route.ts:9](https://github.com/K41R0N/ga4-mcp/blob/aa90b1568a0800eb4dfdc96700e6c10ef1d36ecd/app/api/mcp/route.ts#L9-L31).

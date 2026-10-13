# devli13/mcp-ga4

[Catalog](../../README.md) · [All tool names](../tool-index.md) · [Upstream](https://github.com/devli13/mcp-ga4) · [JSON](../../data/mcps/devli13--mcp-ga4.json)

**6 tools:** 5 GA4, 1 other-service or server-support tools. Reviewed source: [`30727d04fe68`](https://github.com/devli13/mcp-ga4/tree/30727d04fe681872700ba5bce5c9e06b876218a7).

Descriptions and parameter schemas come from the registered source definitions. Generated schemas are reconstructed from annotations or validators; live `tools/list` and authenticated API calls were not run. Loose objects remain loose.

<details>
<summary>Exposure and compatibility notes</summary>

- Source review only; no tools/list, upstream execution, or live requests performed. Git HEAD matches the supplied revision.
- All six tools are unconditionally listed after successful credential initialization; no optional modules or permission tiers. Startup exits before registration when none of GOOGLE_APPLICATION_CREDENTIALS, GA4_SERVICE_ACCOUNT_JSON, or GA4_SERVICE_ACCOUNT_B64 is set, or when inline credentials cannot be parsed. package.json points main/bin/start to server.js and requires Node >=18.
- Every call resolves args.propertyId or GA4_PROPERTY_ID before the handler try/catch. Missing/blank property throws outside the formatted GA4 error response. Non-prefixed IDs are prefixed with properties/.
- Registered schemas omit additionalProperties, required lists except on ga4_run_report and its dateRanges items, and numeric bounds. Defaults mentioned in descriptions are not schema default keywords.

</details>

## Tools

| Tool | Scope | Effect |
| --- | --- | --- |
| [`ga4_run_report`](#ga4_run_report) | GA4 | read |
| [`ga4_realtime`](#ga4_realtime) | GA4 | read |
| [`ga4_top_events`](#ga4_top_events) | GA4 | read |
| [`ga4_daily_users`](#ga4_daily_users) | GA4 | read |
| [`ga4_retention`](#ga4_retention) | GA4 | read |
| [`ga4_list_properties`](#ga4_list_properties) | Server support | local |

## ga4_run_report

Calls runReport on the selected property, maps metric/dimension name arrays to name objects, forwards dateRanges unchanged, optionally sorts a single metric descending, and uses args.limit || 100. Formats response rows using dimension and metric headers and returns property, the number of returned rows, and rows as JSON text.

<details>
<summary>Full registered description</summary>

```text
Run an arbitrary GA4 runReport query. Most flexible tool — use when the convenience tools below do not cover what you need.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `propertyId` | No | string | Not declared |
| `metrics` | Yes | array of string | Not declared |
| `dimensions` | No | array of string | Not declared |
| `dateRanges` | Yes | array of object | Not declared |
| `orderBy` | No | string | Not declared |
| `limit` | No | number | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "propertyId": {
      "type": "string",
      "description": "GA4 property ID. Falls back to GA4_PROPERTY_ID env if not provided."
    },
    "metrics": {
      "type": "array",
      "description": "Metrics by name (e.g. [\"activeUsers\",\"sessions\",\"screenPageViews\",\"engagementRate\",\"eventCount\"]).",
      "items": {
        "type": "string"
      }
    },
    "dimensions": {
      "type": "array",
      "description": "Dimensions by name (e.g. [\"date\",\"eventName\",\"country\",\"deviceCategory\"]).",
      "items": {
        "type": "string"
      }
    },
    "dateRanges": {
      "type": "array",
      "description": "Date ranges. Each item is {startDate, endDate} with \"YYYY-MM-DD\" or relative \"NdaysAgo\" / \"today\" / \"yesterday\".",
      "items": {
        "type": "object",
        "required": [
          "startDate",
          "endDate"
        ],
        "properties": {
          "startDate": {
            "type": "string"
          },
          "endDate": {
            "type": "string"
          },
          "name": {
            "type": "string"
          }
        }
      }
    },
    "orderBy": {
      "type": "string",
      "description": "Metric name to sort desc by. Optional."
    },
    "limit": {
      "type": "number",
      "description": "Max rows (default 100)."
    }
  },
  "required": [
    "metrics",
    "dateRanges"
  ]
}
```

</details>

- The exposed request is a restricted runReport subset: no filters, pagination offset, metric aggregations, or cohortSpec are exposed. Date range objects are forwarded unchanged, including any additional fields allowed by the schema. limit uses a truthiness fallback, so zero becomes 100; no numeric constraints are registered.

Source: [server.js:60](https://github.com/devli13/mcp-ga4/blob/30727d04fe681872700ba5bce5c9e06b876218a7/server.js#L60-L95) · [server.js:168](https://github.com/devli13/mcp-ga4/blob/30727d04fe681872700ba5bce5c9e06b876218a7/server.js#L168-L171) · [server.js:172](https://github.com/devli13/mcp-ga4/blob/30727d04fe681872700ba5bce5c9e06b876218a7/server.js#L172-L183) · [server.js:53](https://github.com/devli13/mcp-ga4/blob/30727d04fe681872700ba5bce5c9e06b876218a7/server.js#L53-L57).

## ga4_realtime

Calls runRealtimeReport with activeUsers and country/deviceCategory dimensions. Returns property and formatted realtime rows as JSON text.

<details>
<summary>Full registered description</summary>

```text
Active users right now + top countries + events in the last 30 minutes.
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
      "type": "string"
    }
  }
}
```

</details>

- Description promises events and top countries, but the handler requests only activeUsers grouped by country and deviceCategory, with no event metric/dimension or ranking.

Source: [server.js:96](https://github.com/devli13/mcp-ga4/blob/30727d04fe681872700ba5bce5c9e06b876218a7/server.js#L96-L105) · [server.js:168](https://github.com/devli13/mcp-ga4/blob/30727d04fe681872700ba5bce5c9e06b876218a7/server.js#L168-L171) · [server.js:185](https://github.com/devli13/mcp-ga4/blob/30727d04fe681872700ba5bce5c9e06b876218a7/server.js#L185-L193) · [server.js:53](https://github.com/devli13/mcp-ga4/blob/30727d04fe681872700ba5bce5c9e06b876218a7/server.js#L53-L57).

## ga4_top_events

Calls runReport with eventCount by eventName over Number(args.days) || 7 daysAgo through today, descending eventCount sort, and Number(args.limit) || 20 rows. Returns property, days, and topEvents as JSON text.

<details>
<summary>Full registered description</summary>

```text
Top events by count over last N days.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `propertyId` | No | string | Not declared |
| `days` | No | number | Not declared |
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
    "days": {
      "type": "number",
      "description": "Default 7."
    },
    "limit": {
      "type": "number",
      "description": "Default 20."
    }
  }
}
```

</details>

- days and limit are converted with Number and truthiness defaults: zero falls back; no positive/integer constraints are registered.

Source: [server.js:106](https://github.com/devli13/mcp-ga4/blob/30727d04fe681872700ba5bce5c9e06b876218a7/server.js#L106-L117) · [server.js:168](https://github.com/devli13/mcp-ga4/blob/30727d04fe681872700ba5bce5c9e06b876218a7/server.js#L168-L171) · [server.js:195](https://github.com/devli13/mcp-ga4/blob/30727d04fe681872700ba5bce5c9e06b876218a7/server.js#L195-L208) · [server.js:53](https://github.com/devli13/mcp-ga4/blob/30727d04fe681872700ba5bce5c9e06b876218a7/server.js#L53-L57).

## ga4_daily_users

Calls runReport with activeUsers, sessions, and newUsers by date over Number(args.days) || 28 daysAgo through today, ascending date order, and days + 10 row limit. Returns property, days, and daily rows as JSON text.

<details>
<summary>Full registered description</summary>

```text
Daily active users and sessions over last N days.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `propertyId` | No | string | Not declared |
| `days` | No | number | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "propertyId": {
      "type": "string"
    },
    "days": {
      "type": "number",
      "description": "Default 28."
    }
  }
}
```

</details>

- Also returns newUsers, beyond the description. days is converted with Number and truthiness default, so zero falls back; no positive/integer constraints are registered.

Source: [server.js:118](https://github.com/devli13/mcp-ga4/blob/30727d04fe681872700ba5bce5c9e06b876218a7/server.js#L118-L128) · [server.js:168](https://github.com/devli13/mcp-ga4/blob/30727d04fe681872700ba5bce5c9e06b876218a7/server.js#L168-L171) · [server.js:210](https://github.com/devli13/mcp-ga4/blob/30727d04fe681872700ba5bce5c9e06b876218a7/server.js#L210-L222) · [server.js:53](https://github.com/devli13/mcp-ga4/blob/30727d04fe681872700ba5bce5c9e06b876218a7/server.js#L53-L57).

## ga4_retention

Calls runReport with activeUsers by firstSessionDate and date over Number(args.days) || 28 daysAgo through today and Number(args.limit) || 500 row limit. Returns property, days, and retention rows as JSON text.

<details>
<summary>Full registered description</summary>

```text
Retention-style cohort view: active users by firstSessionDate (cohort) and date (day of return).
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `propertyId` | No | string | Not declared |
| `days` | No | number | Not declared |
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
    "days": {
      "type": "number",
      "description": "How many days back to look. Default 28."
    },
    "limit": {
      "type": "number",
      "description": "Default 500."
    }
  }
}
```

</details>

- This is a dimension-based report, not an Analytics Data API cohortSpec request or calculated retention rate. days and limit use Number and truthiness defaults; no positive/integer constraints are registered.

Source: [server.js:129](https://github.com/devli13/mcp-ga4/blob/30727d04fe681872700ba5bce5c9e06b876218a7/server.js#L129-L140) · [server.js:168](https://github.com/devli13/mcp-ga4/blob/30727d04fe681872700ba5bce5c9e06b876218a7/server.js#L168-L171) · [server.js:224](https://github.com/devli13/mcp-ga4/blob/30727d04fe681872700ba5bce5c9e06b876218a7/server.js#L224-L236) · [server.js:53](https://github.com/devli13/mcp-ga4/blob/30727d04fe681872700ba5bce5c9e06b876218a7/server.js#L53-L57).

## ga4_list_properties

Returns local JSON text containing DEFAULT_PROPERTY and a note suggesting the Admin API and asserting access to the default property. Makes no API request, does not enumerate accessible properties, and does not verify access.

<details>
<summary>Full registered description</summary>

```text
List GA4 properties accessible to the service account. Useful if the Property ID is unclear.
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

- Misleading advertised description: this is a configured-ID echo, not an Admin API property listing. The claimed service-account access is unverified. Its empty input schema exposes no propertyId, yet the common dispatcher resolves a property before reaching this branch; without GA4_PROPERTY_ID (or an unadvertised propertyId argument), it throws before the try/catch.

Source: [server.js:141](https://github.com/devli13/mcp-ga4/blob/30727d04fe681872700ba5bce5c9e06b876218a7/server.js#L141-L145) · [server.js:168](https://github.com/devli13/mcp-ga4/blob/30727d04fe681872700ba5bce5c9e06b876218a7/server.js#L168-L171) · [server.js:238](https://github.com/devli13/mcp-ga4/blob/30727d04fe681872700ba5bce5c9e06b876218a7/server.js#L238-L241) · [server.js:53](https://github.com/devli13/mcp-ga4/blob/30727d04fe681872700ba5bce5c9e06b876218a7/server.js#L53-L57).

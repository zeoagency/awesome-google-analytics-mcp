# mharnett/mcp-ga4

[Catalog](../../README.md) · [All tool names](../tool-index.md) · [Upstream](https://github.com/mharnett/mcp-ga4) · [JSON](../../data/mcps/mharnett--mcp-ga4.json)

**9 tools:** 6 GA4, 3 other-service or server-support tools. Reviewed source: [`e44f8b02cb84`](https://github.com/mharnett/mcp-ga4/tree/e44f8b02cb84e7b1f7c56b5b25ea7e0590c330a5).

Descriptions and parameter schemas come from the registered source definitions. Generated schemas are reconstructed from annotations or validators; live `tools/list` and authenticated API calls were not run. Loose objects remain loose.

<details>
<summary>Exposure and compatibility notes</summary>

- Source review only; no tools/list, upstream execution or live requests. Git HEAD matches supplied revision.
- Nine total tools: eight advertised by default; ga4_create_custom_dimension additionally appears when GA4_MCP_WRITE=true. CLI auth/setup commands are not MCP tools.
- Startup requires GA4_PROPERTY_ID or config.json and valid configuration of service-account keyfile or user OAuth trio; missing config/auth prevents startup (src/index.ts:106-161,186-193; src/oauthClient.ts). Startup attempts listDataStreams unless MCP_GA4_SKIP_STARTUP_CHECK is set, warning and continuing on failed API health check.
- All results use safeResponse: arrays in responses above 200000 bytes are recursively shortened with truncated=true; row_count updated for shortened rows (src/resilience.ts:32-85). Google API methods use 30-second aggressive timeout, retries and per-operation circuit breakers (src/resilience.ts:87-127).

</details>

## Tools

| Tool | Scope | Effect |
| --- | --- | --- |
| [`ga4_get_client_context`](#ga4_get_client_context) | Server support | local |
| [`ga4_run_report`](#ga4_run_report) | GA4 | read |
| [`ga4_realtime_report`](#ga4_realtime_report) | GA4 | read |
| [`ga4_list_custom_dimensions`](#ga4_list_custom_dimensions) | GA4 | read |
| [`ga4_create_custom_dimension`](#ga4_create_custom_dimension) | GA4 | write |
| [`ga4_list_custom_metrics`](#ga4_list_custom_metrics) | GA4 | read |
| [`ga4_list_data_streams`](#ga4_list_data_streams) | GA4 | read |
| [`ga4_send_feedback`](#ga4_send_feedback) | Server support | local |
| [`ga4_suggest_improvement`](#ga4_suggest_improvement) | Server support | local |

## ga4_get_client_context

Resolves a configured client by working directory: returns the default client in single-property mode, otherwise first folder-prefix or client-key substring match. Returns client name, property ID, folder and measurement IDs, or an error and available clients. Performs no health/API request.

<details>
<summary>Full registered description</summary>

```text
Get the current GA4 client context and health status based on working directory. Call this first to confirm which GA4 property you're working with.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `working_directory` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "additionalProperties": false,
  "type": "object",
  "properties": {
    "working_directory": {
      "type": "string",
      "description": "The current working directory"
    }
  },
  "required": [
    "working_directory"
  ]
}
```

</details>

- Description mentions health status, but handler only reads configuration.
- Required string arguments reject missing/null, non-string, whitespace-only and literal undefined/null sentinel values at handler time (src/errors.ts:41-56); numeric property ID format is not validated.

Source: [src/tools.ts:4](https://github.com/mharnett/mcp-ga4/blob/e44f8b02cb84e7b1f7c56b5b25ea7e0590c330a5/src/tools.ts#L4-L15) · [src/index.ts:458](https://github.com/mharnett/mcp-ga4/blob/e44f8b02cb84e7b1f7c56b5b25ea7e0590c330a5/src/index.ts#L458-L477) · [src/index.ts:163](https://github.com/mharnett/mcp-ga4/blob/e44f8b02cb84e7b1f7c56b5b25ea7e0590c330a5/src/index.ts#L163-L174) · [src/errors.ts:41](https://github.com/mharnett/mcp-ga4/blob/e44f8b02cb84e7b1f7c56b5b25ea7e0590c330a5/src/errors.ts#L41-L56).

## ga4_run_report

Builds Data API runReport request for properties/{property_id}; splits comma-separated dimensions/metrics, defaults to eventName/eventCount and 7daysAgo/today, applies optional dimension equality filter and descending metric order. Defaults limit to 100 and caps it at 10000. Returns flattened string-valued rows, returned row_count and date_range; future start date yields empty rows with error.

<details>
<summary>Full registered description</summary>

```text
Query GA4 historical report. Common patterns: top pages (dimensions="pagePath", metrics="screenPageViews"), traffic sources (dimensions="sessionSource,sessionMedium", metrics="sessions,totalUsers"), daily trend (dimensions="date", metrics="sessions").
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |
| `dimensions` | No | string | Not declared |
| `metrics` | No | string | Not declared |
| `start_date` | No | string | Not declared |
| `end_date` | No | string | Not declared |
| `dimension_filter` | No | string | Not declared |
| `limit` | No | number | Not declared |
| `order_by` | No | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "additionalProperties": false,
  "type": "object",
  "properties": {
    "property_id": {
      "type": "string",
      "description": "GA4 property ID (numeric)"
    },
    "dimensions": {
      "type": "string",
      "description": "Comma-separated dimensions (e.g., \"eventName,date\")"
    },
    "metrics": {
      "type": "string",
      "description": "Comma-separated metrics (e.g., \"eventCount,activeUsers\")"
    },
    "start_date": {
      "type": "string",
      "description": "Start date (YYYY-MM-DD or \"7daysAgo\")"
    },
    "end_date": {
      "type": "string",
      "description": "End date (YYYY-MM-DD or \"today\")"
    },
    "dimension_filter": {
      "type": "string",
      "description": "Optional equality filter (e.g., \"eventName==page_view\")"
    },
    "limit": {
      "type": "number",
      "description": "Max rows (default 100)"
    },
    "order_by": {
      "type": "string",
      "description": "Optional metric to sort by descending (e.g., \"eventCount\")"
    }
  },
  "required": [
    "property_id"
  ]
}
```

</details>

- Defaults and limit cap are implemented in handler rather than JSON Schema; limit has no minimum/integer constraint. Filters lacking == are silently ignored; supplied filter splits only the first two segments and does not explicitly set stringFilter.matchType. Start-date future check is lexical and skips strings containing daysAgo/yesterday/today.
- Required string arguments reject missing/null, non-string, whitespace-only and literal undefined/null sentinel values at handler time (src/errors.ts:41-56); numeric property ID format is not validated.

Source: [src/tools.ts:16](https://github.com/mharnett/mcp-ga4/blob/e44f8b02cb84e7b1f7c56b5b25ea7e0590c330a5/src/tools.ts#L16-L34) · [src/index.ts:479](https://github.com/mharnett/mcp-ga4/blob/e44f8b02cb84e7b1f7c56b5b25ea7e0590c330a5/src/index.ts#L479-L488) · [src/index.ts:236](https://github.com/mharnett/mcp-ga4/blob/e44f8b02cb84e7b1f7c56b5b25ea7e0590c330a5/src/index.ts#L236-L294) · [src/errors.ts:41](https://github.com/mharnett/mcp-ga4/blob/e44f8b02cb84e7b1f7c56b5b25ea7e0590c330a5/src/errors.ts#L41-L56).

## ga4_realtime_report

Builds Data API runRealtimeReport for properties/{property_id}, splitting comma-separated dimensions/metrics (defaults eventName/eventCount) and optional dimension equality filter. Returns flattened string-valued rows and returned row_count.

<details>
<summary>Full registered description</summary>

```text
Query GA4 Realtime Report (last 30 minutes).
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |
| `dimensions` | No | string | Not declared |
| `metrics` | No | string | Not declared |
| `dimension_filter` | No | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "additionalProperties": false,
  "type": "object",
  "properties": {
    "property_id": {
      "type": "string",
      "description": "GA4 property ID (numeric)"
    },
    "dimensions": {
      "type": "string",
      "description": "Comma-separated dimension names (e.g., \"eventName\")"
    },
    "metrics": {
      "type": "string",
      "description": "Comma-separated metric names (e.g., \"eventCount,activeUsers\")"
    },
    "dimension_filter": {
      "type": "string",
      "description": "Optional equality filter (e.g., \"eventName==pardot_form_submit\")"
    }
  },
  "required": [
    "property_id"
  ]
}
```

</details>

- Filters lacking == are silently ignored; supplied filter splits only first two segments and does not explicitly set stringFilter.matchType.
- Required string arguments reject missing/null, non-string, whitespace-only and literal undefined/null sentinel values at handler time (src/errors.ts:41-56); numeric property ID format is not validated.

Source: [src/tools.ts:35](https://github.com/mharnett/mcp-ga4/blob/e44f8b02cb84e7b1f7c56b5b25ea7e0590c330a5/src/tools.ts#L35-L49) · [src/index.ts:490](https://github.com/mharnett/mcp-ga4/blob/e44f8b02cb84e7b1f7c56b5b25ea7e0590c330a5/src/index.ts#L490-L495) · [src/index.ts:296](https://github.com/mharnett/mcp-ga4/blob/e44f8b02cb84e7b1f7c56b5b25ea7e0590c330a5/src/index.ts#L296-L326) · [src/errors.ts:41](https://github.com/mharnett/mcp-ga4/blob/e44f8b02cb84e7b1f7c56b5b25ea7e0590c330a5/src/errors.ts#L41-L56).

## ga4_list_custom_dimensions

Calls Admin API listCustomDimensions with property parent, maps displayName, parameterName, scope and description to custom_dimensions plus count.

<details>
<summary>Full registered description</summary>

```text
List all registered custom dimensions for a GA4 property.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "additionalProperties": false,
  "type": "object",
  "properties": {
    "property_id": {
      "type": "string",
      "description": "GA4 property ID (numeric)"
    }
  },
  "required": [
    "property_id"
  ]
}
```

</details>

- Required string arguments reject missing/null, non-string, whitespace-only and literal undefined/null sentinel values at handler time (src/errors.ts:41-56); numeric property ID format is not validated.

Source: [src/tools.ts:50](https://github.com/mharnett/mcp-ga4/blob/e44f8b02cb84e7b1f7c56b5b25ea7e0590c330a5/src/tools.ts#L50-L61) · [src/index.ts:497](https://github.com/mharnett/mcp-ga4/blob/e44f8b02cb84e7b1f7c56b5b25ea7e0590c330a5/src/index.ts#L497-L498) · [src/index.ts:330](https://github.com/mharnett/mcp-ga4/blob/e44f8b02cb84e7b1f7c56b5b25ea7e0590c330a5/src/index.ts#L330-L342) · [src/errors.ts:41](https://github.com/mharnett/mcp-ga4/blob/e44f8b02cb84e7b1f7c56b5b25ea7e0590c330a5/src/errors.ts#L41-L56).

## ga4_create_custom_dimension

Calls Admin API createCustomDimension with property parent and supplied parameter/display names; maps case-insensitive USER to USER, every other scope to EVENT, and missing description to empty string. Returns created display name, parameter_name and scope.

<details>
<summary>Full registered description</summary>

```text
Register a new custom dimension in a GA4 property.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |
| `parameter_name` | Yes | string | Not declared |
| `display_name` | Yes | string | Not declared |
| `scope` | No | string | Not declared |
| `description` | No | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "additionalProperties": false,
  "type": "object",
  "properties": {
    "property_id": {
      "type": "string",
      "description": "GA4 property ID (numeric)"
    },
    "parameter_name": {
      "type": "string",
      "description": "The event parameter name (e.g., \"form_type\")"
    },
    "display_name": {
      "type": "string",
      "description": "Human-readable name (e.g., \"Form Type\")"
    },
    "scope": {
      "type": "string",
      "description": "Either \"EVENT\" or \"USER\" (default: EVENT)"
    },
    "description": {
      "type": "string",
      "description": "Optional description"
    }
  },
  "required": [
    "property_id",
    "parameter_name",
    "display_name"
  ]
}
```

</details>

- Conditionally advertised and callable only with GA4_MCP_WRITE=true; write gate is delegated to mcp-write-gate. Scope is unrestricted string in schema, with implementation coercion to EVENT except USER.
- Required string arguments reject missing/null, non-string, whitespace-only and literal undefined/null sentinel values at handler time (src/errors.ts:41-56); numeric property ID format is not validated.

Source: [src/tools.ts:62](https://github.com/mharnett/mcp-ga4/blob/e44f8b02cb84e7b1f7c56b5b25ea7e0590c330a5/src/tools.ts#L62-L77) · [src/index.ts:500](https://github.com/mharnett/mcp-ga4/blob/e44f8b02cb84e7b1f7c56b5b25ea7e0590c330a5/src/index.ts#L500-L506) · [src/index.ts:344](https://github.com/mharnett/mcp-ga4/blob/e44f8b02cb84e7b1f7c56b5b25ea7e0590c330a5/src/index.ts#L344-L369) · [src/errors.ts:41](https://github.com/mharnett/mcp-ga4/blob/e44f8b02cb84e7b1f7c56b5b25ea7e0590c330a5/src/errors.ts#L41-L56) · [src/writeGate.ts:1](https://github.com/mharnett/mcp-ga4/blob/e44f8b02cb84e7b1f7c56b5b25ea7e0590c330a5/src/writeGate.ts#L1-L57).

## ga4_list_custom_metrics

Calls Admin API listCustomMetrics with property parent and returns display names, parameter names, scopes, measurement units and descriptions plus count.

<details>
<summary>Full registered description</summary>

```text
List all registered custom metrics for a GA4 property.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "additionalProperties": false,
  "type": "object",
  "properties": {
    "property_id": {
      "type": "string",
      "description": "GA4 property ID (numeric)"
    }
  },
  "required": [
    "property_id"
  ]
}
```

</details>

- Required string arguments reject missing/null, non-string, whitespace-only and literal undefined/null sentinel values at handler time (src/errors.ts:41-56); numeric property ID format is not validated.

Source: [src/tools.ts:78](https://github.com/mharnett/mcp-ga4/blob/e44f8b02cb84e7b1f7c56b5b25ea7e0590c330a5/src/tools.ts#L78-L89) · [src/index.ts:508](https://github.com/mharnett/mcp-ga4/blob/e44f8b02cb84e7b1f7c56b5b25ea7e0590c330a5/src/index.ts#L508-L509) · [src/index.ts:371](https://github.com/mharnett/mcp-ga4/blob/e44f8b02cb84e7b1f7c56b5b25ea7e0590c330a5/src/index.ts#L371-L384) · [src/errors.ts:41](https://github.com/mharnett/mcp-ga4/blob/e44f8b02cb84e7b1f7c56b5b25ea7e0590c330a5/src/errors.ts#L41-L56).

## ga4_list_data_streams

Calls Admin API listDataStreams with property parent and returns display name/type; web streams also include measurement_id and default_uri, plus count.

<details>
<summary>Full registered description</summary>

```text
List all data streams for a GA4 property.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "additionalProperties": false,
  "type": "object",
  "properties": {
    "property_id": {
      "type": "string",
      "description": "GA4 property ID (numeric)"
    }
  },
  "required": [
    "property_id"
  ]
}
```

</details>

- Required string arguments reject missing/null, non-string, whitespace-only and literal undefined/null sentinel values at handler time (src/errors.ts:41-56); numeric property ID format is not validated.

Source: [src/tools.ts:90](https://github.com/mharnett/mcp-ga4/blob/e44f8b02cb84e7b1f7c56b5b25ea7e0590c330a5/src/tools.ts#L90-L101) · [src/index.ts:511](https://github.com/mharnett/mcp-ga4/blob/e44f8b02cb84e7b1f7c56b5b25ea7e0590c330a5/src/index.ts#L511-L512) · [src/index.ts:386](https://github.com/mharnett/mcp-ga4/blob/e44f8b02cb84e7b1f7c56b5b25ea7e0590c330a5/src/index.ts#L386-L400) · [src/errors.ts:41](https://github.com/mharnett/mcp-ga4/blob/e44f8b02cb84e7b1f7c56b5b25ea7e0590c330a5/src/errors.ts#L41-L56).

## ga4_send_feedback

Validates feedback type against bug/feature/question; appends type, message, optional query_context and ISO timestamp as JSONL to ~/.config/mcp-ga4/feedback/feedback.jsonl. Returns recorded status; invalid feedback type returns error object. Does not send feedback remotely.

<details>
<summary>Full registered description</summary>

```text
Send feedback about the GA4 MCP tools. Use when a query didn't work as expected.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `feedback_type` | Yes | string | Not declared |
| `message` | Yes | string | Not declared |
| `query_context` | No | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "additionalProperties": false,
  "type": "object",
  "properties": {
    "feedback_type": {
      "type": "string",
      "description": "One of: bug, feature, question"
    },
    "message": {
      "type": "string",
      "description": "Description of the issue, request, or question"
    },
    "query_context": {
      "type": "string",
      "description": "Optional context about what was queried"
    }
  },
  "required": [
    "feedback_type",
    "message"
  ]
}
```

</details>

- feedback_type choices are enforced by handler, but schema has no enum. Local logging remains enabled with remote writes disabled.
- Required string arguments reject missing/null, non-string, whitespace-only and literal undefined/null sentinel values at handler time (src/errors.ts:41-56); numeric property ID format is not validated.

Source: [src/tools.ts:102](https://github.com/mharnett/mcp-ga4/blob/e44f8b02cb84e7b1f7c56b5b25ea7e0590c330a5/src/tools.ts#L102-L115) · [src/index.ts:514](https://github.com/mharnett/mcp-ga4/blob/e44f8b02cb84e7b1f7c56b5b25ea7e0590c330a5/src/index.ts#L514-L527) · [src/index.ts:404](https://github.com/mharnett/mcp-ga4/blob/e44f8b02cb84e7b1f7c56b5b25ea7e0590c330a5/src/index.ts#L404-L408) · [src/errors.ts:41](https://github.com/mharnett/mcp-ga4/blob/e44f8b02cb84e7b1f7c56b5b25ea7e0590c330a5/src/errors.ts#L41-L56).

## ga4_suggest_improvement

Appends improvement type, failed_query, expected_result, optional actual_result and ISO timestamp as JSONL to ~/.config/mcp-ga4/feedback/improvements.jsonl and returns recorded status/message.

<details>
<summary>Full registered description</summary>

```text
Log a GA4 query pattern that didn't work well, so it can be improved.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `failed_query` | Yes | string | Not declared |
| `expected_result` | Yes | string | Not declared |
| `actual_result` | No | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "additionalProperties": false,
  "type": "object",
  "properties": {
    "failed_query": {
      "type": "string",
      "description": "The natural language question the user asked"
    },
    "expected_result": {
      "type": "string",
      "description": "What the user expected to see"
    },
    "actual_result": {
      "type": "string",
      "description": "What actually happened"
    }
  },
  "required": [
    "failed_query",
    "expected_result"
  ]
}
```

</details>

- Local logging remains enabled with remote writes disabled.
- Required string arguments reject missing/null, non-string, whitespace-only and literal undefined/null sentinel values at handler time (src/errors.ts:41-56); numeric property ID format is not validated.

Source: [src/tools.ts:116](https://github.com/mharnett/mcp-ga4/blob/e44f8b02cb84e7b1f7c56b5b25ea7e0590c330a5/src/tools.ts#L116-L129) · [src/index.ts:529](https://github.com/mharnett/mcp-ga4/blob/e44f8b02cb84e7b1f7c56b5b25ea7e0590c330a5/src/index.ts#L529-L538) · [src/index.ts:410](https://github.com/mharnett/mcp-ga4/blob/e44f8b02cb84e7b1f7c56b5b25ea7e0590c330a5/src/index.ts#L410-L414) · [src/errors.ts:41](https://github.com/mharnett/mcp-ga4/blob/e44f8b02cb84e7b1f7c56b5b25ea7e0590c330a5/src/errors.ts#L41-L56).

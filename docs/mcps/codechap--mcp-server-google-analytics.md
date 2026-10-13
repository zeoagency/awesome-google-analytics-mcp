# codeChap/mcp-server-google-analytics

[Catalog](../../README.md) · [All tool names](../tool-index.md) · [Upstream](https://github.com/codeChap/mcp-server-google-analytics) · [JSON](../../data/mcps/codechap--mcp-server-google-analytics.json)

**15 tools:** 14 GA4, 1 other-service or server-support tools. Reviewed source: [`b003d8ade81a`](https://github.com/codeChap/mcp-server-google-analytics/tree/b003d8ade81adc672fd338bc50a0d5287e10d890).

Descriptions and parameter schemas come from the registered source definitions. Generated schemas are reconstructed from annotations or validators; live `tools/list` and authenticated API calls were not run. Loose objects remain loose.

<details>
<summary>Exposure and compatibility notes</summary>

- Source review only; no tools/list, upstream execution or live requests. Git HEAD matches supplied revision.
- All 15 tools register unconditionally through tool_router/tool_handler; write scope is required by Google APIs, not a local registration permission tier.
- Schemars schemas reconstructed from JsonSchema/Deserialize models. No serde default/rename/flatten, enums or nested typed models occur. Option fields can be omitted or null; arbitrary Value schemas remain unconstrained. Additional properties are allowed by default.
- Startup requires valid config credentials or ADC-discovered credentials before stdio serving. Runtime OAuth permissions and API enablement were not tested.

</details>

## Tools

| Tool | Scope | Effect |
| --- | --- | --- |
| [`get_account_summaries`](#get_account_summaries) | GA4 | read |
| [`get_property_details`](#get_property_details) | GA4 | read |
| [`list_google_ads_links`](#list_google_ads_links) | GA4 | read |
| [`list_property_annotations`](#list_property_annotations) | GA4 | read |
| [`get_custom_dimensions_and_metrics`](#get_custom_dimensions_and_metrics) | GA4 | read |
| [`run_report`](#run_report) | GA4 | read |
| [`login`](#login) | Server support | mixed |
| [`run_realtime_report`](#run_realtime_report) | GA4 | read |
| [`create_custom_dimension`](#create_custom_dimension) | GA4 | write |
| [`list_custom_dimensions`](#list_custom_dimensions) | GA4 | read |
| [`archive_custom_dimension`](#archive_custom_dimension) | GA4 | write |
| [`create_key_event`](#create_key_event) | GA4 | write |
| [`list_key_events`](#list_key_events) | GA4 | read |
| [`delete_key_event`](#delete_key_event) | GA4 | write |
| [`create_property_annotation`](#create_property_annotation) | GA4 | write |

## get_account_summaries

Auto-paginates accountSummaries for each configured client with pageSize=200; caches property-to-client mappings. Multiple clients tag each summary with _account and embed individual errors while continuing.

<details>
<summary>Full registered description</summary>

```text
Retrieves all Google Analytics account summaries the authenticated user(s) have access to, including account names and their GA4 properties. When multiple accounts are configured, results include an _account field identifying which account owns each summary. Use this first to discover available property IDs. No parameters required.
```

</details>

No named input parameters are declared.

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {},
  "required": []
}
```

</details>

Source: [src/server.rs:220](https://github.com/codeChap/mcp-server-google-analytics/blob/b003d8ade81adc672fd338bc50a0d5287e10d890/src/server.rs#L220-L230) · [src/api.rs:178](https://github.com/codeChap/mcp-server-google-analytics/blob/b003d8ade81adc672fd338bc50a0d5287e10d890/src/api.rs#L178-L182).

## get_property_details

GET property resource, accepting bare string ID or properties/ prefix. Property operations route through the cached Google account, or probe configured clients on cache miss; cached HTTP 403 clears the entry. API errors become MCP tool-error content.

<details>
<summary>Full registered description</summary>

```text
Get detailed information about a specific GA4 property including display name, industry category, time zone, currency code, service level, create time, and parent account.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "property_id": {
      "type": "string",
      "description": "GA4 property ID. Accepts: bare number (12345), string (\"12345\"), or resource name (\"properties/12345\")"
    }
  },
  "required": [
    "property_id"
  ],
  "title": "PropertyIdParams",
  "description": "Parameters for tools that only need a property ID."
}
```

</details>

- property_id is a JSON string despite description claiming acceptance of a bare number; there is no coercion annotation.

Source: [src/server.rs:231](https://github.com/codeChap/mcp-server-google-analytics/blob/b003d8ade81adc672fd338bc50a0d5287e10d890/src/server.rs#L231-L243) · [src/params.rs:17](https://github.com/codeChap/mcp-server-google-analytics/blob/b003d8ade81adc672fd338bc50a0d5287e10d890/src/params.rs#L17-L25) · [src/api.rs:184](https://github.com/codeChap/mcp-server-google-analytics/blob/b003d8ade81adc672fd338bc50a0d5287e10d890/src/api.rs#L184-L189).

## list_google_ads_links

Auto-paginates Google Ads links with pageSize=200 and returns the collected array. Property operations route through the cached Google account, or probe configured clients on cache miss; cached HTTP 403 clears the entry. API errors become MCP tool-error content.

<details>
<summary>Full registered description</summary>

```text
List all Google Ads links for a GA4 property. Returns linked Google Ads customer IDs and their configuration.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "property_id": {
      "type": "string",
      "description": "GA4 property ID. Accepts: bare number (12345), string (\"12345\"), or resource name (\"properties/12345\")"
    }
  },
  "required": [
    "property_id"
  ],
  "title": "PropertyIdParams",
  "description": "Parameters for tools that only need a property ID."
}
```

</details>

- property_id is a JSON string despite description claiming acceptance of a bare number; there is no coercion annotation.

Source: [src/server.rs:244](https://github.com/codeChap/mcp-server-google-analytics/blob/b003d8ade81adc672fd338bc50a0d5287e10d890/src/server.rs#L244-L253) · [src/params.rs:17](https://github.com/codeChap/mcp-server-google-analytics/blob/b003d8ade81adc672fd338bc50a0d5287e10d890/src/params.rs#L17-L25) · [src/api.rs:191](https://github.com/codeChap/mcp-server-google-analytics/blob/b003d8ade81adc672fd338bc50a0d5287e10d890/src/api.rs#L191-L196).

## list_property_annotations

Auto-paginates reporting data annotations with pageSize=200 and returns the collected array. Property operations route through the cached Google account, or probe configured clients on cache miss; cached HTTP 403 clears the entry. API errors become MCP tool-error content.

<details>
<summary>Full registered description</summary>

```text
List reporting data annotations for a GA4 property (Admin API alpha). Annotations are notes on specific dates or periods used to mark releases, campaigns, traffic changes, etc.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "property_id": {
      "type": "string",
      "description": "GA4 property ID. Accepts: bare number (12345), string (\"12345\"), or resource name (\"properties/12345\")"
    }
  },
  "required": [
    "property_id"
  ],
  "title": "PropertyIdParams",
  "description": "Parameters for tools that only need a property ID."
}
```

</details>

- property_id is a JSON string despite description claiming acceptance of a bare number; there is no coercion annotation.

Source: [src/server.rs:254](https://github.com/codeChap/mcp-server-google-analytics/blob/b003d8ade81adc672fd338bc50a0d5287e10d890/src/server.rs#L254-L266) · [src/params.rs:17](https://github.com/codeChap/mcp-server-google-analytics/blob/b003d8ade81adc672fd338bc50a0d5287e10d890/src/params.rs#L17-L25) · [src/api.rs:200](https://github.com/codeChap/mcp-server-google-analytics/blob/b003d8ade81adc672fd338bc50a0d5287e10d890/src/api.rs#L200-L205).

## get_custom_dimensions_and_metrics

GET metadata and retain dimensions/metrics whose customDefinition is true; return custom_dimensions and custom_metrics arrays. Property operations route through the cached Google account, or probe configured clients on cache miss; cached HTTP 403 clears the entry. API errors become MCP tool-error content.

<details>
<summary>Full registered description</summary>

```text
Get custom dimensions and custom metrics defined for a GA4 property. Returns only user-defined custom dimensions and metrics, not the standard built-in ones.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "property_id": {
      "type": "string",
      "description": "GA4 property ID. Accepts: bare number (12345), string (\"12345\"), or resource name (\"properties/12345\")"
    }
  },
  "required": [
    "property_id"
  ],
  "title": "PropertyIdParams",
  "description": "Parameters for tools that only need a property ID."
}
```

</details>

- property_id is a JSON string despite description claiming acceptance of a bare number; there is no coercion annotation.

Source: [src/server.rs:267](https://github.com/codeChap/mcp-server-google-analytics/blob/b003d8ade81adc672fd338bc50a0d5287e10d890/src/server.rs#L267-L279) · [src/params.rs:17](https://github.com/codeChap/mcp-server-google-analytics/blob/b003d8ade81adc672fd338bc50a0d5287e10d890/src/params.rs#L17-L25) · [src/api.rs:209](https://github.com/codeChap/mcp-server-google-analytics/blob/b003d8ade81adc672fd338bc50a0d5287e10d890/src/api.rs#L209-L223).

## run_report

Builds dateRanges, dimensions and metrics; names are wrapped as {name}. Recursively converts snake_case keys of date ranges, filters and ordering to camelCase. Optional limit/offset are sent as decimal strings, with currencyCode and returnPropertyQuota when supplied. POST runReport and return JSON. Property operations route through the cached Google account, or probe configured clients on cache miss; cached HTTP 403 clears the entry. API errors become MCP tool-error content.

<details>
<summary>Full registered description</summary>

```text
Run a report on a GA4 property. Retrieves event-based analytics data for the specified dimensions and metrics over the given date range(s).

## References
- Dimensions: https://developers.google.com/analytics/devguides/reporting/data/v1/api-schema#dimensions
- Metrics: https://developers.google.com/analytics/devguides/reporting/data/v1/api-schema#metrics

## Date ranges
Format: YYYY-MM-DD or relative strings: "today", "yesterday", "NdaysAgo".
Example: [{"start_date": "30daysAgo", "end_date": "today"}]

## Dimension filter
A FilterExpression with one of:
- filter: {field_name, string_filter: {match_type: EXACT|BEGINS_WITH|ENDS_WITH|CONTAINS|FULL_REGEXP|PARTIAL_REGEXP, value, case_sensitive}}
- filter: {field_name, numeric_filter: {operation: EQUAL|LESS_THAN|GREATER_THAN|..., value: {int64_value or double_value}}}
- filter: {field_name, in_list_filter: {values: [...], case_sensitive}}
- filter: {field_name, between_filter: {from_value: {...}, to_value: {...}}}
- and_group: {expressions: [...]}
- or_group: {expressions: [...]}
- not_expression: {<filter_expression>}

## Order by
- By dimension: {dimension: {dimension_name, order_type: ALPHANUMERIC|CASE_INSENSITIVE_ALPHANUMERIC|NUMERIC}, desc: bool}
- By metric: {metric: {metric_name}, desc: bool}
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |
| `date_ranges` | Yes | array of any | Not declared |
| `dimensions` | Yes | array of string | Not declared |
| `metrics` | Yes | array of string | Not declared |
| `dimension_filter` | No | any | Not declared |
| `metric_filter` | No | any | Not declared |
| `order_bys` | No | any | Not declared |
| `limit` | No | integer or null | Not declared |
| `offset` | No | integer or null | Not declared |
| `currency_code` | No | string or null | Not declared |
| `return_property_quota` | No | boolean or null | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "property_id": {
      "type": "string",
      "description": "GA4 property ID. Accepts: bare number (12345), string (\"12345\"), or resource name (\"properties/12345\")"
    },
    "date_ranges": {
      "type": "array",
      "items": {},
      "description": "Date ranges for the report. Each object has: start_date (required, YYYY-MM-DD or relative: \"today\", \"yesterday\", \"NdaysAgo\"), end_date (required, same format), name (optional). Example: [{\"start_date\": \"30daysAgo\", \"end_date\": \"today\"}]"
    },
    "dimensions": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "List of dimension names. See: https://developers.google.com/analytics/devguides/reporting/data/v1/api-schema#dimensions Example: [\"country\", \"city\"]"
    },
    "metrics": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "List of metric names. See: https://developers.google.com/analytics/devguides/reporting/data/v1/api-schema#metrics Example: [\"activeUsers\", \"sessions\"]"
    },
    "dimension_filter": {
      "description": "Optional dimension filter expression. Supports: simple filter (string_filter, numeric_filter, in_list_filter, between_filter), not_expression, and_group, or_group. Example: {\"filter\": {\"field_name\": \"country\", \"string_filter\": {\"match_type\": \"EXACT\", \"value\": \"US\"}}}"
    },
    "metric_filter": {
      "description": "Optional metric filter expression. Same structure as dimension_filter. Example: {\"filter\": {\"field_name\": \"activeUsers\", \"numeric_filter\": {\"operation\": \"GREATER_THAN\", \"value\": {\"int64_value\": 100}}}}"
    },
    "order_bys": {
      "description": "Optional ordering. List of order_by objects. Each can have: dimension (with dimension_name and optional order_type: ALPHANUMERIC, CASE_INSENSITIVE_ALPHANUMERIC, NUMERIC), metric (with metric_name), or pivot; plus desc (bool). Example: [{\"metric\": {\"metric_name\": \"activeUsers\"}, \"desc\": true}]"
    },
    "limit": {
      "type": [
        "integer",
        "null"
      ],
      "format": "int64",
      "description": "Maximum rows to return (max 250000). Used for pagination."
    },
    "offset": {
      "type": [
        "integer",
        "null"
      ],
      "format": "int64",
      "description": "Row offset for pagination."
    },
    "currency_code": {
      "type": [
        "string",
        "null"
      ],
      "description": "ISO 4217 currency code (e.g. \"USD\", \"EUR\")."
    },
    "return_property_quota": {
      "type": [
        "boolean",
        "null"
      ],
      "description": "Whether to include property quota information in the response."
    }
  },
  "required": [
    "property_id",
    "date_ranges",
    "dimensions",
    "metrics"
  ],
  "title": "RunReportParams",
  "description": "Parameters for the `run_report` tool."
}
```

</details>

- property_id is a JSON string despite description claiming acceptance of a bare number; there is no coercion annotation.
- Filter, order and range structures use arbitrary serde_json::Value; documented nested shapes and numeric limits are not schema constraints. No local validation of GA field names or row limits.

Source: [src/server.rs:280](https://github.com/codeChap/mcp-server-google-analytics/blob/b003d8ade81adc672fd338bc50a0d5287e10d890/src/server.rs#L280-L322) · [src/params.rs:27](https://github.com/codeChap/mcp-server-google-analytics/blob/b003d8ade81adc672fd338bc50a0d5287e10d890/src/params.rs#L27-L88) · [src/api.rs:225](https://github.com/codeChap/mcp-server-google-analytics/blob/b003d8ade81adc672fd338bc50a0d5287e10d890/src/api.rs#L225-L234) · [src/api.rs:356](https://github.com/codeChap/mcp-server-google-analytics/blob/b003d8ade81adc672fd338bc50a0d5287e10d890/src/api.rs#L356-L459).

## login

Loads the named account from config.toml, resolves Desktop OAuth client credentials, binds 127.0.0.1 on an ephemeral port, opens Google consent for analytics.edit and analytics.readonly, waits up to 300 seconds for a callback, checks state, exchanges the code and overwrites that account credentials JSON. Existing in-memory clients require restart.

<details>
<summary>Full registered description</summary>

```text
Re-authenticate a configured Google account via interactive OAuth. Starts a local loopback listener, opens Google's consent screen in the default browser, captures the callback, and writes a new refresh_token to the account's credentials file. Use when an existing refresh_token has been revoked or expired. The MCP server must be restarted after success for the new token to take effect. Requires an OAuth Desktop-app client_id/client_secret, either in the [[accounts]] entry in config.toml or already present in the existing credentials file.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `name` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string",
      "description": "The account name from config.toml ([[accounts]] `name` field) to re-authenticate. Starts a loopback OAuth flow, opens the consent URL in the default browser, captures the callback, and writes a new refresh_token to that account's credentials file."
    }
  },
  "required": [
    "name"
  ],
  "title": "LoginParams",
  "description": "Parameters for the `login` tool."
}
```

</details>

- Always registered, but requires a config.toml account; ADC-only startup provides no configured account for this tool. Startup loads credential files first, so this tool cannot bootstrap a server with missing credentials.

Source: [src/server.rs:323](https://github.com/codeChap/mcp-server-google-analytics/blob/b003d8ade81adc672fd338bc50a0d5287e10d890/src/server.rs#L323-L345) · [src/params.rs:5](https://github.com/codeChap/mcp-server-google-analytics/blob/b003d8ade81adc672fd338bc50a0d5287e10d890/src/params.rs#L5-L15) · [src/login.rs:31](https://github.com/codeChap/mcp-server-google-analytics/blob/b003d8ade81adc672fd338bc50a0d5287e10d890/src/login.rs#L31-L76).

## run_realtime_report

Builds named dimensions/metrics and shared filter/order/quota/limit/offset fields as for run_report; recursively converts minute_ranges to camelCase and POSTs runRealtimeReport. Property operations route through the cached Google account, or probe configured clients on cache miss; cached HTTP 403 clears the entry. API errors become MCP tool-error content.

<details>
<summary>Full registered description</summary>

```text
Run a realtime report on a GA4 property. Returns data for the last 30 minutes by default (configurable via minute_ranges).

## References
- Realtime dimensions: https://developers.google.com/analytics/devguides/reporting/data/v1/realtime-api-schema#dimensions
- Realtime metrics: https://developers.google.com/analytics/devguides/reporting/data/v1/realtime-api-schema#metrics

No date_ranges parameter — use minute_ranges to control the time window.
Only user-scoped custom dimensions (customUser:*) are supported; custom metrics are not.

Filters and ordering use the same format as run_report.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |
| `dimensions` | Yes | array of string | Not declared |
| `metrics` | Yes | array of string | Not declared |
| `dimension_filter` | No | any | Not declared |
| `metric_filter` | No | any | Not declared |
| `order_bys` | No | any | Not declared |
| `limit` | No | integer or null | Not declared |
| `offset` | No | integer or null | Not declared |
| `minute_ranges` | No | any | Not declared |
| `return_property_quota` | No | boolean or null | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "property_id": {
      "type": "string",
      "description": "GA4 property ID. Accepts: bare number (12345), string (\"12345\"), or resource name (\"properties/12345\")"
    },
    "dimensions": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "List of realtime dimension names. See: https://developers.google.com/analytics/devguides/reporting/data/v1/realtime-api-schema#dimensions Example: [\"country\", \"unifiedScreenName\"]"
    },
    "metrics": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "List of realtime metric names. See: https://developers.google.com/analytics/devguides/reporting/data/v1/realtime-api-schema#metrics Example: [\"activeUsers\"]"
    },
    "dimension_filter": {
      "description": "Optional dimension filter expression. Same structure as run_report's dimension_filter."
    },
    "metric_filter": {
      "description": "Optional metric filter expression. Same structure as run_report's metric_filter."
    },
    "order_bys": {
      "description": "Optional ordering. Same structure as run_report's order_bys."
    },
    "limit": {
      "type": [
        "integer",
        "null"
      ],
      "format": "int64",
      "description": "Maximum rows to return."
    },
    "offset": {
      "type": [
        "integer",
        "null"
      ],
      "format": "int64",
      "description": "Row offset for pagination."
    },
    "minute_ranges": {
      "description": "Optional minute ranges for the realtime report. By default covers the last 30 minutes. Each object has: start_minutes_ago (int, max 29), end_minutes_ago (int, min 0), name (optional). Example: [{\"start_minutes_ago\": 10, \"end_minutes_ago\": 0}]"
    },
    "return_property_quota": {
      "type": [
        "boolean",
        "null"
      ],
      "description": "Whether to include property quota information in the response."
    }
  },
  "required": [
    "property_id",
    "dimensions",
    "metrics"
  ],
  "title": "RunRealtimeReportParams",
  "description": "Parameters for the `run_realtime_report` tool."
}
```

</details>

- property_id is a JSON string despite description claiming acceptance of a bare number; there is no coercion annotation.
- Filter, order and range structures use arbitrary serde_json::Value; documented nested shapes and numeric limits are not schema constraints. No local validation of GA field names or row limits.
- offset is forwarded to the realtime API despite not being a RunRealtimeReportRequest field; supplying it may cause API rejection.

Source: [src/server.rs:346](https://github.com/codeChap/mcp-server-google-analytics/blob/b003d8ade81adc672fd338bc50a0d5287e10d890/src/server.rs#L346-L375) · [src/params.rs:211](https://github.com/codeChap/mcp-server-google-analytics/blob/b003d8ade81adc672fd338bc50a0d5287e10d890/src/params.rs#L211-L258) · [src/api.rs:236](https://github.com/codeChap/mcp-server-google-analytics/blob/b003d8ade81adc672fd338bc50a0d5287e10d890/src/api.rs#L236-L245) · [src/api.rs:356](https://github.com/codeChap/mcp-server-google-analytics/blob/b003d8ade81adc672fd338bc50a0d5287e10d890/src/api.rs#L356-L494).

## create_custom_dimension

POST parameterName, displayName, scope (fallback EVENT), optional description and disallowAdsPersonalization. Property operations route through the cached Google account, or probe configured clients on cache miss; cached HTTP 403 clears the entry. API errors become MCP tool-error content.

<details>
<summary>Full registered description</summary>

```text
Create a custom dimension on a GA4 property (registers an event parameter or user property so it can be used in reports). Requires the account to have edit rights and the `analytics.edit` OAuth scope. scope defaults to "EVENT"; parameter_name cannot be changed later.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |
| `parameter_name` | Yes | string | Not declared |
| `display_name` | Yes | string | Not declared |
| `scope` | No | string or null | Not declared |
| `description` | No | string or null | Not declared |
| `disallow_ads_personalization` | No | boolean or null | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "property_id": {
      "type": "string",
      "description": "GA4 property ID. Accepts: bare number (12345), string (\"12345\"), or resource name (\"properties/12345\")"
    },
    "parameter_name": {
      "type": "string",
      "description": "The event parameter (or user property) name this dimension is registered against, e.g. \"website_id\", \"suburb\", \"city\". Max 24 chars for EVENT scope, 24 for USER scope. Cannot be changed after creation."
    },
    "display_name": {
      "type": "string",
      "description": "Human-readable display name shown in the GA UI, e.g. \"Website ID\"."
    },
    "scope": {
      "type": [
        "string",
        "null"
      ],
      "description": "Scope of the dimension: \"EVENT\" (event parameter), \"USER\" (user property), or \"ITEM\" (ecommerce item parameter). Defaults to \"EVENT\"."
    },
    "description": {
      "type": [
        "string",
        "null"
      ],
      "description": "Optional description of the custom dimension (max 150 chars)."
    },
    "disallow_ads_personalization": {
      "type": [
        "boolean",
        "null"
      ],
      "description": "EVENT-scope only: if true, this dimension is NOT sent to Google signals / used for ads personalization. Optional."
    }
  },
  "required": [
    "property_id",
    "parameter_name",
    "display_name"
  ],
  "title": "CreateCustomDimensionParams",
  "description": "Parameters for the `create_custom_dimension` tool."
}
```

</details>

- property_id is a JSON string despite description claiming acceptance of a bare number; there is no coercion annotation.
- Documented enum choices, length limits and handler fallback defaults are prose/implementation only; no schemars enum, length, format or serde default constraints.

Source: [src/server.rs:376](https://github.com/codeChap/mcp-server-google-analytics/blob/b003d8ade81adc672fd338bc50a0d5287e10d890/src/server.rs#L376-L401) · [src/params.rs:90](https://github.com/codeChap/mcp-server-google-analytics/blob/b003d8ade81adc672fd338bc50a0d5287e10d890/src/params.rs#L90-L125) · [src/api.rs:249](https://github.com/codeChap/mcp-server-google-analytics/blob/b003d8ade81adc672fd338bc50a0d5287e10d890/src/api.rs#L249-L259).

## list_custom_dimensions

Auto-paginates customDimensions with pageSize=200 and returns their JSON array; no local archived-status filter. Property operations route through the cached Google account, or probe configured clients on cache miss; cached HTTP 403 clears the entry. API errors become MCP tool-error content.

<details>
<summary>Full registered description</summary>

```text
List all custom dimensions on a GA4 property, including archived ones, with their full resource names. The trailing segment of the name is the ID needed by archive_custom_dimension.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "property_id": {
      "type": "string",
      "description": "GA4 property ID. Accepts: bare number (12345), string (\"12345\"), or resource name (\"properties/12345\")"
    }
  },
  "required": [
    "property_id"
  ],
  "title": "PropertyIdParams",
  "description": "Parameters for tools that only need a property ID."
}
```

</details>

- property_id is a JSON string despite description claiming acceptance of a bare number; there is no coercion annotation.

Source: [src/server.rs:402](https://github.com/codeChap/mcp-server-google-analytics/blob/b003d8ade81adc672fd338bc50a0d5287e10d890/src/server.rs#L402-L414) · [src/params.rs:17](https://github.com/codeChap/mcp-server-google-analytics/blob/b003d8ade81adc672fd338bc50a0d5287e10d890/src/params.rs#L17-L25) · [src/api.rs:261](https://github.com/codeChap/mcp-server-google-analytics/blob/b003d8ade81adc672fd338bc50a0d5287e10d890/src/api.rs#L261-L267).

## archive_custom_dimension

POST properties/{id}/customDimensions/{custom_dimension_id}:archive without a body. An empty successful response becomes {success:true}. Property operations route through the cached Google account, or probe configured clients on cache miss; cached HTTP 403 clears the entry. API errors become MCP tool-error content.

<details>
<summary>Full registered description</summary>

```text
Archive (soft-delete) a custom dimension by its trailing ID. Requires `analytics.edit`. Use list_custom_dimensions to find the ID.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |
| `custom_dimension_id` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "property_id": {
      "type": "string",
      "description": "GA4 property ID (bare number, string, or \"properties/12345\")."
    },
    "custom_dimension_id": {
      "type": "string",
      "description": "The trailing ID of the custom dimension to archive — the last segment of its resource name (e.g. \"3\" from \"properties/123/customDimensions/3\"). Use list_custom_dimensions to find it."
    }
  },
  "required": [
    "property_id",
    "custom_dimension_id"
  ],
  "title": "ArchiveCustomDimensionParams",
  "description": "Parameters for the `archive_custom_dimension` tool."
}
```

</details>

- property_id is a JSON string despite description claiming acceptance of a bare number; there is no coercion annotation.

Source: [src/server.rs:415](https://github.com/codeChap/mcp-server-google-analytics/blob/b003d8ade81adc672fd338bc50a0d5287e10d890/src/server.rs#L415-L429) · [src/params.rs:127](https://github.com/codeChap/mcp-server-google-analytics/blob/b003d8ade81adc672fd338bc50a0d5287e10d890/src/params.rs#L127-L139) · [src/api.rs:269](https://github.com/codeChap/mcp-server-google-analytics/blob/b003d8ade81adc672fd338bc50a0d5287e10d890/src/api.rs#L269-L279).

## create_key_event

POST eventName, countingMethod (fallback ONCE_PER_EVENT), and optional defaultValue forwarded unchanged. Property operations route through the cached Google account, or probe configured clients on cache miss; cached HTTP 403 clears the entry. API errors become MCP tool-error content.

<details>
<summary>Full registered description</summary>

```text
Mark an event as a key event (conversion) on a GA4 property. Requires `analytics.edit`. counting_method defaults to "ONCE_PER_EVENT". Optionally set a default conversion value.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |
| `event_name` | Yes | string | Not declared |
| `counting_method` | No | string or null | Not declared |
| `default_value` | No | any | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "property_id": {
      "type": "string",
      "description": "GA4 property ID (bare number, string, or \"properties/12345\")."
    },
    "event_name": {
      "type": "string",
      "description": "The event name to mark as a key event (conversion), e.g. \"enquiry\", \"book\". Must match the event name as collected."
    },
    "counting_method": {
      "type": [
        "string",
        "null"
      ],
      "description": "How conversions are counted: \"ONCE_PER_EVENT\" (every occurrence) or \"ONCE_PER_SESSION\" (at most once per session). Defaults to \"ONCE_PER_EVENT\"."
    },
    "default_value": {
      "description": "Optional default conversion value, as an object: {\"numericValue\": 100.0, \"currencyCode\": \"ZAR\"}. Both fields required together if supplied."
    }
  },
  "required": [
    "property_id",
    "event_name"
  ],
  "title": "CreateKeyEventParams",
  "description": "Parameters for the `create_key_event` tool."
}
```

</details>

- property_id is a JSON string despite description claiming acceptance of a bare number; there is no coercion annotation.
- Documented enum choices, length limits and handler fallback defaults are prose/implementation only; no schemars enum, length, format or serde default constraints.

Source: [src/server.rs:430](https://github.com/codeChap/mcp-server-google-analytics/blob/b003d8ade81adc672fd338bc50a0d5287e10d890/src/server.rs#L430-L451) · [src/params.rs:141](https://github.com/codeChap/mcp-server-google-analytics/blob/b003d8ade81adc672fd338bc50a0d5287e10d890/src/params.rs#L141-L164) · [src/api.rs:281](https://github.com/codeChap/mcp-server-google-analytics/blob/b003d8ade81adc672fd338bc50a0d5287e10d890/src/api.rs#L281-L291).

## list_key_events

Auto-paginates keyEvents with pageSize=200 and returns their JSON array. Property operations route through the cached Google account, or probe configured clients on cache miss; cached HTTP 403 clears the entry. API errors become MCP tool-error content.

<details>
<summary>Full registered description</summary>

```text
List all key events (conversions) on a GA4 property, with their resource names. The trailing segment of the name is the ID needed by delete_key_event.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "property_id": {
      "type": "string",
      "description": "GA4 property ID. Accepts: bare number (12345), string (\"12345\"), or resource name (\"properties/12345\")"
    }
  },
  "required": [
    "property_id"
  ],
  "title": "PropertyIdParams",
  "description": "Parameters for tools that only need a property ID."
}
```

</details>

- property_id is a JSON string despite description claiming acceptance of a bare number; there is no coercion annotation.

Source: [src/server.rs:452](https://github.com/codeChap/mcp-server-google-analytics/blob/b003d8ade81adc672fd338bc50a0d5287e10d890/src/server.rs#L452-L464) · [src/params.rs:17](https://github.com/codeChap/mcp-server-google-analytics/blob/b003d8ade81adc672fd338bc50a0d5287e10d890/src/params.rs#L17-L25) · [src/api.rs:293](https://github.com/codeChap/mcp-server-google-analytics/blob/b003d8ade81adc672fd338bc50a0d5287e10d890/src/api.rs#L293-L298).

## delete_key_event

DELETE properties/{id}/keyEvents/{key_event_id}; empty successful responses become {success:true}. Property operations route through the cached Google account, or probe configured clients on cache miss; cached HTTP 403 clears the entry. API errors become MCP tool-error content.

<details>
<summary>Full registered description</summary>

```text
Delete a key event (conversion) by its trailing ID. Requires `analytics.edit`. Use list_key_events to find the ID.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |
| `key_event_id` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "property_id": {
      "type": "string",
      "description": "GA4 property ID (bare number, string, or \"properties/12345\")."
    },
    "key_event_id": {
      "type": "string",
      "description": "The trailing ID of the key event to delete — the last segment of its resource name (e.g. \"5\" from \"properties/123/keyEvents/5\"). Use list_key_events to find it."
    }
  },
  "required": [
    "property_id",
    "key_event_id"
  ],
  "title": "DeleteKeyEventParams",
  "description": "Parameters for the `delete_key_event` tool."
}
```

</details>

- property_id is a JSON string despite description claiming acceptance of a bare number; there is no coercion annotation.

Source: [src/server.rs:465](https://github.com/codeChap/mcp-server-google-analytics/blob/b003d8ade81adc672fd338bc50a0d5287e10d890/src/server.rs#L465-L476) · [src/params.rs:166](https://github.com/codeChap/mcp-server-google-analytics/blob/b003d8ade81adc672fd338bc50a0d5287e10d890/src/params.rs#L166-L178) · [src/api.rs:300](https://github.com/codeChap/mcp-server-google-analytics/blob/b003d8ade81adc672fd338bc50a0d5287e10d890/src/api.rs#L300-L310).

## create_property_annotation

Parses date/end_date into integer year/month/day objects. POSTs title, color (fallback PURPLE), optional description and either annotationDate or annotationDateRange; local parsing errors return tool errors. Property operations route through the cached Google account, or probe configured clients on cache miss; cached HTTP 403 clears the entry. API errors become MCP tool-error content.

<details>
<summary>Full registered description</summary>

```text
Create a reporting-data annotation on a GA4 property's timeline (e.g. to mark a deploy or campaign). Requires `analytics.edit`. Supply date as "YYYY-MM-DD"; add end_date for a date-range annotation.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |
| `title` | Yes | string | Not declared |
| `description` | No | string or null | Not declared |
| `date` | Yes | string | Not declared |
| `end_date` | No | string or null | Not declared |
| `color` | No | string or null | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "property_id": {
      "type": "string",
      "description": "GA4 property ID (bare number, string, or \"properties/12345\")."
    },
    "title": {
      "type": "string",
      "description": "Annotation title, e.g. \"Deployed bounding-box proximity search\"."
    },
    "description": {
      "type": [
        "string",
        "null"
      ],
      "description": "Optional longer description of what changed."
    },
    "date": {
      "type": "string",
      "description": "The date the annotation marks, as \"YYYY-MM-DD\". If end_date is also given, this is the start of a date-range annotation."
    },
    "end_date": {
      "type": [
        "string",
        "null"
      ],
      "description": "Optional end date \"YYYY-MM-DD\" to make this a date-range annotation instead of a single day."
    },
    "color": {
      "type": [
        "string",
        "null"
      ],
      "description": "Annotation color. One of: PURPLE, BROWN, BLUE, GREEN, RED, CYAN, ORANGE. Defaults to PURPLE. (The API rejects an unset color.)"
    }
  },
  "required": [
    "property_id",
    "title",
    "date"
  ],
  "title": "CreatePropertyAnnotationParams",
  "description": "Parameters for the `create_property_annotation` tool."
}
```

</details>

- property_id is a JSON string despite description claiming acceptance of a bare number; there is no coercion annotation.
- Documented enum choices, length limits and handler fallback defaults are prose/implementation only; no schemars enum, length, format or serde default constraints.
- Date parsing checks three integer components only; does not validate calendar ranges or date ordering.

Source: [src/server.rs:477](https://github.com/codeChap/mcp-server-google-analytics/blob/b003d8ade81adc672fd338bc50a0d5287e10d890/src/server.rs#L477-L497) · [src/params.rs:180](https://github.com/codeChap/mcp-server-google-analytics/blob/b003d8ade81adc672fd338bc50a0d5287e10d890/src/params.rs#L180-L209) · [src/api.rs:314](https://github.com/codeChap/mcp-server-google-analytics/blob/b003d8ade81adc672fd338bc50a0d5287e10d890/src/api.rs#L314-L324) · [src/api.rs:496](https://github.com/codeChap/mcp-server-google-analytics/blob/b003d8ade81adc672fd338bc50a0d5287e10d890/src/api.rs#L496-L543).

# sednalabs/ga4-mcp

[Catalog](../../README.md) · [All tool names](../tool-index.md) · [Upstream](https://github.com/sednalabs/ga4-mcp) · [JSON](../../data/mcps/sednalabs--ga4-mcp.json)

**35 tools:** 25 GA4, 10 other-service or server-support tools. Reviewed source: [`847406e7ce36`](https://github.com/sednalabs/ga4-mcp/tree/847406e7ce36360216ba5bd0a71b218619b0fa8e).

Descriptions and parameter schemas come from the registered source definitions. Generated schemas are reconstructed from annotations or validators; live `tools/list` and authenticated API calls were not run. Loose objects remain loose.

<details>
<summary>Exposure and compatibility notes</summary>

- Source review only; no tools/list or live requests, no upstream code executed. Git HEAD matches supplied revision.
- All 35 tools are always listed; default read_only capability denies the 15 scratchpad_* tools only at invocation. scratchpad profile permits all tools.
- Full schemas preserved from committed spec/tool_schema_snapshot.v1.json and cross-checked against source registration descriptions, every request struct field, serde flatten/default/deny_unknown_fields and schemars overrides; these are source-derived, not freshly claimed runtime output.
- Arbitrary serde_json::Value fields intentionally retain loose schemas, including filters, order_bys, pivots, segments and funnel expressions. Report date ranges use a schemars Vec<ReportDateRangeSchema> override although handlers accept snake_case or camelCase dates.
- Cargo dependencies include pinned sednalabs/mcp-toolkit-rs Git revision and bundled DuckDB; build/install not executed or validated. No definite unusable entrypoint found.

</details>

## Tools

| Tool | Scope | Effect |
| --- | --- | --- |
| [`ga4_get_started`](#ga4_get_started) | Server support | local |
| [`ga4_auth_status`](#ga4_auth_status) | Server support | read |
| [`ga4_auth_login_command`](#ga4_auth_login_command) | Server support | local |
| [`get_account_summaries`](#get_account_summaries) | GA4 | read |
| [`get_property_details`](#get_property_details) | GA4 | read |
| [`get_account_data_sharing_settings`](#get_account_data_sharing_settings) | GA4 | read |
| [`get_property_data_retention_settings`](#get_property_data_retention_settings) | GA4 | read |
| [`list_google_ads_links`](#list_google_ads_links) | GA4 | read |
| [`list_property_annotations`](#list_property_annotations) | GA4 | read |
| [`run_property_access_report`](#run_property_access_report) | GA4 | read |
| [`run_account_access_report`](#run_account_access_report) | GA4 | read |
| [`run_report`](#run_report) | GA4 | read |
| [`run_conversions_report`](#run_conversions_report) | GA4 | read |
| [`run_funnel_report`](#run_funnel_report) | GA4 | read |
| [`preview_report_request`](#preview_report_request) | GA4 | local |
| [`run_realtime_report`](#run_realtime_report) | GA4 | read |
| [`run_pivot_report`](#run_pivot_report) | GA4 | read |
| [`batch_run_reports`](#batch_run_reports) | GA4 | read |
| [`get_custom_dimensions_and_metrics`](#get_custom_dimensions_and_metrics) | GA4 | read |
| [`check_report_compatibility`](#check_report_compatibility) | GA4 | read |
| [`scratchpad_get_runtime_limits`](#scratchpad_get_runtime_limits) | Server support | local |
| [`scratchpad_set_runtime_limits`](#scratchpad_set_runtime_limits) | Server support | local |
| [`scratchpad_open_session`](#scratchpad_open_session) | Server support | local |
| [`scratchpad_close_session`](#scratchpad_close_session) | Server support | local |
| [`scratchpad_list_sessions`](#scratchpad_list_sessions) | Server support | local |
| [`scratchpad_list_tables`](#scratchpad_list_tables) | Server support | local |
| [`scratchpad_drop_table`](#scratchpad_drop_table) | Server support | local |
| [`scratchpad_ingest_report`](#scratchpad_ingest_report) | GA4 | mixed |
| [`scratchpad_ingest_realtime_report`](#scratchpad_ingest_realtime_report) | GA4 | mixed |
| [`scratchpad_query`](#scratchpad_query) | GA4 | local |
| [`scratchpad_describe_table`](#scratchpad_describe_table) | GA4 | local |
| [`scratchpad_summarize_table`](#scratchpad_summarize_table) | GA4 | local |
| [`scratchpad_release_regression_report`](#scratchpad_release_regression_report) | GA4 | local |
| [`scratchpad_landing_param_shift_report`](#scratchpad_landing_param_shift_report) | GA4 | local |
| [`scratchpad_export_evidence_bundle`](#scratchpad_export_evidence_bundle) | GA4 | local |

## ga4_get_started

Returns configured auth/capability modes, copyable CLI setup instructions, credential options, and recommended starter tools; performs no login or API request.

<details>
<summary>Full registered description</summary>

```text
Return the recommended GA4 first-run auth flow, credential modes, and safe starter tools.
```

</details>

No named input parameters are declared.

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "properties": {},
  "type": "object"
}
```

</details>

Source: [src/tools.rs:929](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L929-L1011) · [src/tools.rs:113](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L113-L875).

## ga4_auth_status

Returns configured credential source, material-presence indicators, scope, quota project and next steps. When verify_token is true, acquires a token and checks account summaries; does not return the token. In request_header-only mode verification explicitly uses configured server credentials.

<details>
<summary>Full registered description</summary>

```text
Explain configured Google Analytics auth source and optionally verify Google API access without returning secrets.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `verify_token` | No | boolean | false |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "properties": {
    "verify_token": {
      "default": false,
      "description": "When true, acquire a Google access token and call GA account summaries. The token is never returned.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

</details>

Source: [src/tools.rs:1014](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L1014-L1076) · [src/tools.rs:113](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L113-L117) · [src/tools.rs:113](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L113-L875) · [src/ga_client.rs:336](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/ga_client.rs#L336-L736).

## ga4_auth_login_command

Builds copyable CLI login and quota-project commands from configured scope and supplied OAuth client/account/port/headless/shared-ADC options; does not execute login.

<details>
<summary>Full registered description</summary>

```text
Return copyable Google Analytics auth login commands, including direct browser OAuth when a client id file is supplied.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `account` | No | string or null | null |
| `callback_port` | No | integer or null | null |
| `client_id_file` | No | string or null | null |
| `headless` | No | boolean | false |
| `quota_project` | No | string or null | null |
| `shared_adc` | No | boolean or null | null |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "properties": {
    "account": {
      "default": null,
      "description": "Optional Google account hint for browser login.",
      "type": [
        "string",
        "null"
      ]
    },
    "callback_port": {
      "default": null,
      "description": "Optional fixed loopback callback port for direct browser OAuth.",
      "format": "uint16",
      "maximum": 65535,
      "minimum": 0,
      "type": [
        "integer",
        "null"
      ]
    },
    "client_id_file": {
      "default": null,
      "description": "Optional Google OAuth client id file for direct browser OAuth.",
      "type": [
        "string",
        "null"
      ]
    },
    "headless": {
      "default": false,
      "description": "Include the headless browser flag for SSH or remote environments.",
      "type": "boolean"
    },
    "quota_project": {
      "default": null,
      "description": "Optional quota project to include as a follow-up command.",
      "type": [
        "string",
        "null"
      ]
    },
    "shared_adc": {
      "default": null,
      "description": "Use the conventional shared gcloud ADC file instead of the server-specific file.",
      "type": [
        "boolean",
        "null"
      ]
    }
  },
  "type": "object"
}
```

</details>

Source: [src/tools.rs:1079](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L1079-L1225) · [src/tools.rs:120](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L120-L139) · [src/tools.rs:113](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L113-L875).

## get_account_summaries

Fetches paginated account summaries and property summaries accessible to the credential.

<details>
<summary>Full registered description</summary>

```text
Retrieves information about the user's Google Analytics accounts and properties.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `max_pages` | No | integer or null | null |
| `page_size` | No | integer or null | null |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "properties": {
    "max_pages": {
      "default": null,
      "description": "Optional max pages to fetch before stopping.",
      "format": "uint32",
      "minimum": 0,
      "type": [
        "integer",
        "null"
      ]
    },
    "page_size": {
      "default": null,
      "description": "Optional page size used during pagination. Defaults to server max.",
      "format": "uint32",
      "minimum": 0,
      "type": [
        "integer",
        "null"
      ]
    }
  },
  "type": "object"
}
```

</details>

Source: [src/tools.rs:1228](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L1228-L1248) · [src/tools.rs:184](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L184-L191) · [src/tools.rs:113](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L113-L875) · [src/ga_client.rs:336](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/ga_client.rs#L336-L736).

## get_property_details

Reads a normalized GA4 property resource.

<details>
<summary>Full registered description</summary>

```text
Returns details about a property.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | PropertyId | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "$defs": {
    "PropertyId": {
      "anyOf": [
        {
          "format": "uint64",
          "minimum": 0,
          "type": "integer"
        },
        {
          "type": "string"
        }
      ]
    }
  },
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "properties": {
    "property_id": {
      "$ref": "#/$defs/PropertyId",
      "description": "The Google Analytics property id as integer or \"properties/<id>\"."
    }
  },
  "required": [
    "property_id"
  ],
  "type": "object"
}
```

</details>

Source: [src/tools.rs:1251](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L1251-L1264) · [src/tools.rs:202](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L202-L205) · [src/tools.rs:113](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L113-L875) · [src/ga_client.rs:336](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/ga_client.rs#L336-L736).

## get_account_data_sharing_settings

Reads account data sharing settings.

<details>
<summary>Full registered description</summary>

```text
Returns account-level data sharing settings for a Google Analytics account.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `account_id` | Yes | AccountId | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "$defs": {
    "AccountId": {
      "anyOf": [
        {
          "format": "uint64",
          "minimum": 0,
          "type": "integer"
        },
        {
          "type": "string"
        }
      ]
    }
  },
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "properties": {
    "account_id": {
      "$ref": "#/$defs/AccountId",
      "description": "The Google Analytics account id as integer or \"accounts/<id>\"."
    }
  },
  "required": [
    "account_id"
  ],
  "type": "object"
}
```

</details>

Source: [src/tools.rs:1267](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L1267-L1284) · [src/tools.rs:218](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L218-L221) · [src/tools.rs:113](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L113-L875) · [src/ga_client.rs:336](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/ga_client.rs#L336-L736).

## get_property_data_retention_settings

Reads property data retention settings.

<details>
<summary>Full registered description</summary>

```text
Returns property-level data retention settings for a Google Analytics property.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | PropertyId | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "$defs": {
    "PropertyId": {
      "anyOf": [
        {
          "format": "uint64",
          "minimum": 0,
          "type": "integer"
        },
        {
          "type": "string"
        }
      ]
    }
  },
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "properties": {
    "property_id": {
      "$ref": "#/$defs/PropertyId",
      "description": "The Google Analytics property id as integer or \"properties/<id>\"."
    }
  },
  "required": [
    "property_id"
  ],
  "type": "object"
}
```

</details>

Source: [src/tools.rs:1287](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L1287-L1304) · [src/tools.rs:202](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L202-L205) · [src/tools.rs:113](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L113-L875) · [src/ga_client.rs:336](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/ga_client.rs#L336-L736).

## list_google_ads_links

Fetches paginated Google Ads link resources for a property.

<details>
<summary>Full registered description</summary>

```text
Returns a list of links to Google Ads accounts for a property.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `max_pages` | No | integer or null | null |
| `page_size` | No | integer or null | null |
| `property_id` | Yes | PropertyId | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "$defs": {
    "PropertyId": {
      "anyOf": [
        {
          "format": "uint64",
          "minimum": 0,
          "type": "integer"
        },
        {
          "type": "string"
        }
      ]
    }
  },
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "properties": {
    "max_pages": {
      "default": null,
      "description": "Optional max pages to fetch before stopping.",
      "format": "uint32",
      "minimum": 0,
      "type": [
        "integer",
        "null"
      ]
    },
    "page_size": {
      "default": null,
      "description": "Optional page size used during pagination. Defaults to server max.",
      "format": "uint32",
      "minimum": 0,
      "type": [
        "integer",
        "null"
      ]
    },
    "property_id": {
      "$ref": "#/$defs/PropertyId",
      "description": "The Google Analytics property id as integer or \"properties/<id>\"."
    }
  },
  "required": [
    "property_id"
  ],
  "type": "object"
}
```

</details>

Source: [src/tools.rs:1307](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L1307-L1330) · [src/tools.rs:224](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L224-L233) · [src/tools.rs:113](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L113-L875) · [src/ga_client.rs:336](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/ga_client.rs#L336-L736).

## list_property_annotations

Fetches paginated property reporting data annotations.

<details>
<summary>Full registered description</summary>

```text
Returns reporting data annotations for a property.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `max_pages` | No | integer or null | null |
| `page_size` | No | integer or null | null |
| `property_id` | Yes | PropertyId | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "$defs": {
    "PropertyId": {
      "anyOf": [
        {
          "format": "uint64",
          "minimum": 0,
          "type": "integer"
        },
        {
          "type": "string"
        }
      ]
    }
  },
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "properties": {
    "max_pages": {
      "default": null,
      "description": "Optional max pages to fetch before stopping.",
      "format": "uint32",
      "minimum": 0,
      "type": [
        "integer",
        "null"
      ]
    },
    "page_size": {
      "default": null,
      "description": "Optional page size used during pagination. Defaults to server max.",
      "format": "uint32",
      "minimum": 0,
      "type": [
        "integer",
        "null"
      ]
    },
    "property_id": {
      "$ref": "#/$defs/PropertyId",
      "description": "The Google Analytics property id as integer or \"properties/<id>\"."
    }
  },
  "required": [
    "property_id"
  ],
  "type": "object"
}
```

</details>

Source: [src/tools.rs:1333](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L1333-L1356) · [src/tools.rs:224](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L224-L233) · [src/tools.rs:113](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L113-L875) · [src/ga_client.rs:336](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/ga_client.rs#L336-L736).

## run_property_access_report

Runs an access report for a property using normalized access-report request fields and returns bounded Contract V1 rows with cursor/quota metadata.

<details>
<summary>Full registered description</summary>

```text
Runs a Google Analytics Admin API access report for a property.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `cursor` | No | string or null | null |
| `date_ranges` | Yes | array of ReportDateRangeSchema | Not declared |
| `dimension_filter` | No | any | null |
| `dimensions` | Yes | array of string | Not declared |
| `limit` | No | integer or null | null |
| `max_cell_chars` | No | integer or null | null |
| `max_rows` | No | integer or null | null |
| `metric_filter` | No | any | null |
| `metrics` | Yes | array of string | Not declared |
| `offset` | No | integer or null | null |
| `order_bys` | No | array or null | null |
| `output_mode` | No | TabularOutputMode or null | Not declared |
| `property_id` | Yes | PropertyId | Not declared |
| `summary_only` | No | boolean | false |
| `time_zone` | No | string or null | null |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "$defs": {
    "PropertyId": {
      "anyOf": [
        {
          "format": "uint64",
          "minimum": 0,
          "type": "integer"
        },
        {
          "type": "string"
        }
      ]
    },
    "ReportDateRangeSchema": {
      "properties": {
        "end_date": {
          "description": "Inclusive end date (for example `2026-02-07`, `yesterday`).",
          "type": "string"
        },
        "start_date": {
          "description": "Inclusive start date (for example `2026-02-01`, `7daysAgo`).",
          "type": "string"
        }
      },
      "required": [
        "start_date",
        "end_date"
      ],
      "type": "object"
    },
    "TabularOutputMode": {
      "enum": [
        "rows",
        "tuples",
        "scalar",
        "compact"
      ],
      "type": "string"
    }
  },
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "properties": {
    "cursor": {
      "default": null,
      "description": "Opaque pagination cursor from `meta.next_cursor`.",
      "type": [
        "string",
        "null"
      ]
    },
    "date_ranges": {
      "items": {
        "$ref": "#/$defs/ReportDateRangeSchema"
      },
      "type": "array"
    },
    "dimension_filter": {
      "default": null,
      "description": "GA FilterExpression. Accepts an object, JSON-object string, or `field==value` shorthand."
    },
    "dimensions": {
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "limit": {
      "default": null,
      "format": "uint64",
      "minimum": 0,
      "type": [
        "integer",
        "null"
      ]
    },
    "max_cell_chars": {
      "default": null,
      "description": "Optional string clipping limit applied to response cell values.",
      "format": "uint",
      "minimum": 0,
      "type": [
        "integer",
        "null"
      ]
    },
    "max_rows": {
      "default": null,
      "description": "Optional response row cap for Contract V1 tabular payloads.",
      "format": "uint",
      "minimum": 0,
      "type": [
        "integer",
        "null"
      ]
    },
    "metric_filter": {
      "default": null,
      "description": "GA FilterExpression. Accepts an object or JSON-object string."
    },
    "metrics": {
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "offset": {
      "default": null,
      "format": "uint64",
      "minimum": 0,
      "type": [
        "integer",
        "null"
      ]
    },
    "order_bys": {
      "default": null,
      "items": true,
      "type": [
        "array",
        "null"
      ]
    },
    "output_mode": {
      "anyOf": [
        {
          "$ref": "#/$defs/TabularOutputMode"
        },
        {
          "type": "null"
        }
      ],
      "description": "Tabular output shape for the response payload."
    },
    "property_id": {
      "$ref": "#/$defs/PropertyId"
    },
    "summary_only": {
      "default": false,
      "description": "If true, omit row payload and return metadata only.",
      "type": "boolean"
    },
    "time_zone": {
      "default": null,
      "type": [
        "string",
        "null"
      ]
    }
  },
  "required": [
    "property_id",
    "date_ranges",
    "dimensions",
    "metrics"
  ],
  "type": "object"
}
```

</details>

- Handler tabular controls require max_rows 1..25,000 (default effective cap 200), max_cell_chars 1..16,384 when supplied; cursor is query-bound. These upper bounds are implementation constraints, not numeric schema maxima.
- Report validation requires 1..50 dimensions and 1..50 metrics with nonempty names; where present limit must be 1..250,000 and offset at most 2,500,000. These constraints are enforced by handlers rather than schema.

Source: [src/tools.rs:1359](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L1359-L1444) · [src/tools.rs:452](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L452-L487) · [src/tools.rs:113](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L113-L875) · [src/ga_client.rs:336](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/ga_client.rs#L336-L736).

## run_account_access_report

Runs an access report for an account using normalized access-report request fields and returns bounded Contract V1 rows with cursor/quota metadata.

<details>
<summary>Full registered description</summary>

```text
Runs a Google Analytics Admin API access report for an account.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `account_id` | Yes | AccountId | Not declared |
| `cursor` | No | string or null | null |
| `date_ranges` | Yes | array of ReportDateRangeSchema | Not declared |
| `dimension_filter` | No | any | null |
| `dimensions` | Yes | array of string | Not declared |
| `limit` | No | integer or null | null |
| `max_cell_chars` | No | integer or null | null |
| `max_rows` | No | integer or null | null |
| `metric_filter` | No | any | null |
| `metrics` | Yes | array of string | Not declared |
| `offset` | No | integer or null | null |
| `order_bys` | No | array or null | null |
| `output_mode` | No | TabularOutputMode or null | Not declared |
| `summary_only` | No | boolean | false |
| `time_zone` | No | string or null | null |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "$defs": {
    "AccountId": {
      "anyOf": [
        {
          "format": "uint64",
          "minimum": 0,
          "type": "integer"
        },
        {
          "type": "string"
        }
      ]
    },
    "ReportDateRangeSchema": {
      "properties": {
        "end_date": {
          "description": "Inclusive end date (for example `2026-02-07`, `yesterday`).",
          "type": "string"
        },
        "start_date": {
          "description": "Inclusive start date (for example `2026-02-01`, `7daysAgo`).",
          "type": "string"
        }
      },
      "required": [
        "start_date",
        "end_date"
      ],
      "type": "object"
    },
    "TabularOutputMode": {
      "enum": [
        "rows",
        "tuples",
        "scalar",
        "compact"
      ],
      "type": "string"
    }
  },
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "properties": {
    "account_id": {
      "$ref": "#/$defs/AccountId"
    },
    "cursor": {
      "default": null,
      "description": "Opaque pagination cursor from `meta.next_cursor`.",
      "type": [
        "string",
        "null"
      ]
    },
    "date_ranges": {
      "items": {
        "$ref": "#/$defs/ReportDateRangeSchema"
      },
      "type": "array"
    },
    "dimension_filter": {
      "default": null,
      "description": "GA FilterExpression. Accepts an object, JSON-object string, or `field==value` shorthand."
    },
    "dimensions": {
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "limit": {
      "default": null,
      "format": "uint64",
      "minimum": 0,
      "type": [
        "integer",
        "null"
      ]
    },
    "max_cell_chars": {
      "default": null,
      "description": "Optional string clipping limit applied to response cell values.",
      "format": "uint",
      "minimum": 0,
      "type": [
        "integer",
        "null"
      ]
    },
    "max_rows": {
      "default": null,
      "description": "Optional response row cap for Contract V1 tabular payloads.",
      "format": "uint",
      "minimum": 0,
      "type": [
        "integer",
        "null"
      ]
    },
    "metric_filter": {
      "default": null,
      "description": "GA FilterExpression. Accepts an object or JSON-object string."
    },
    "metrics": {
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "offset": {
      "default": null,
      "format": "uint64",
      "minimum": 0,
      "type": [
        "integer",
        "null"
      ]
    },
    "order_bys": {
      "default": null,
      "items": true,
      "type": [
        "array",
        "null"
      ]
    },
    "output_mode": {
      "anyOf": [
        {
          "$ref": "#/$defs/TabularOutputMode"
        },
        {
          "type": "null"
        }
      ],
      "description": "Tabular output shape for the response payload."
    },
    "summary_only": {
      "default": false,
      "description": "If true, omit row payload and return metadata only.",
      "type": "boolean"
    },
    "time_zone": {
      "default": null,
      "type": [
        "string",
        "null"
      ]
    }
  },
  "required": [
    "account_id",
    "date_ranges",
    "dimensions",
    "metrics"
  ],
  "type": "object"
}
```

</details>

- Handler tabular controls require max_rows 1..25,000 (default effective cap 200), max_cell_chars 1..16,384 when supplied; cursor is query-bound. These upper bounds are implementation constraints, not numeric schema maxima.
- Report validation requires 1..50 dimensions and 1..50 metrics with nonempty names; where present limit must be 1..250,000 and offset at most 2,500,000. These constraints are enforced by handlers rather than schema.

Source: [src/tools.rs:1447](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L1447-L1532) · [src/tools.rs:490](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L490-L525) · [src/tools.rs:113](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L113-L875) · [src/ga_client.rs:336](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/ga_client.rs#L336-L736).

## run_report

Validates report fields, normalizes snake_case request fields to GA JSON, resolves a query-bound cursor and effective limit/offset, then projects report rows into Contract V1 output with quota and pagination metadata.

<details>
<summary>Full registered description</summary>

```text
Runs a Google Analytics report using the Data API.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `currency_code` | No | string or null | null |
| `cursor` | No | string or null | null |
| `date_ranges` | Yes | array of ReportDateRangeSchema | Not declared |
| `dimension_filter` | No | any | null |
| `dimensions` | Yes | array of string | Not declared |
| `limit` | No | integer or null | null |
| `max_cell_chars` | No | integer or null | null |
| `max_rows` | No | integer or null | null |
| `metric_filter` | No | any | null |
| `metrics` | Yes | array of string | Not declared |
| `offset` | No | integer or null | null |
| `order_bys` | No | array or null | null |
| `output_mode` | No | TabularOutputMode or null | Not declared |
| `property_id` | Yes | PropertyId | Not declared |
| `return_property_quota` | No | boolean | true |
| `summary_only` | No | boolean | false |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "$defs": {
    "PropertyId": {
      "anyOf": [
        {
          "format": "uint64",
          "minimum": 0,
          "type": "integer"
        },
        {
          "type": "string"
        }
      ]
    },
    "ReportDateRangeSchema": {
      "properties": {
        "end_date": {
          "description": "Inclusive end date (for example `2026-02-07`, `yesterday`).",
          "type": "string"
        },
        "start_date": {
          "description": "Inclusive start date (for example `2026-02-01`, `7daysAgo`).",
          "type": "string"
        }
      },
      "required": [
        "start_date",
        "end_date"
      ],
      "type": "object"
    },
    "TabularOutputMode": {
      "enum": [
        "rows",
        "tuples",
        "scalar",
        "compact"
      ],
      "type": "string"
    }
  },
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "properties": {
    "currency_code": {
      "default": null,
      "type": [
        "string",
        "null"
      ]
    },
    "cursor": {
      "default": null,
      "description": "Opaque pagination cursor from `meta.next_cursor`.",
      "type": [
        "string",
        "null"
      ]
    },
    "date_ranges": {
      "items": {
        "$ref": "#/$defs/ReportDateRangeSchema"
      },
      "type": "array"
    },
    "dimension_filter": {
      "default": null,
      "description": "GA FilterExpression. Accepts an object, JSON-object string, or `field==value` shorthand."
    },
    "dimensions": {
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "limit": {
      "default": null,
      "format": "uint64",
      "minimum": 0,
      "type": [
        "integer",
        "null"
      ]
    },
    "max_cell_chars": {
      "default": null,
      "description": "Optional string clipping limit applied to response cell values.",
      "format": "uint",
      "minimum": 0,
      "type": [
        "integer",
        "null"
      ]
    },
    "max_rows": {
      "default": null,
      "description": "Optional response row cap for Contract V1 tabular payloads.",
      "format": "uint",
      "minimum": 0,
      "type": [
        "integer",
        "null"
      ]
    },
    "metric_filter": {
      "default": null,
      "description": "GA FilterExpression. Accepts an object or JSON-object string."
    },
    "metrics": {
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "offset": {
      "default": null,
      "format": "uint64",
      "minimum": 0,
      "type": [
        "integer",
        "null"
      ]
    },
    "order_bys": {
      "default": null,
      "items": true,
      "type": [
        "array",
        "null"
      ]
    },
    "output_mode": {
      "anyOf": [
        {
          "$ref": "#/$defs/TabularOutputMode"
        },
        {
          "type": "null"
        }
      ],
      "description": "Tabular output shape for the response payload."
    },
    "property_id": {
      "$ref": "#/$defs/PropertyId"
    },
    "return_property_quota": {
      "default": true,
      "type": "boolean"
    },
    "summary_only": {
      "default": false,
      "description": "If true, omit row payload and return metadata only.",
      "type": "boolean"
    }
  },
  "required": [
    "property_id",
    "date_ranges",
    "dimensions",
    "metrics"
  ],
  "type": "object"
}
```

</details>

- Handler tabular controls require max_rows 1..25,000 (default effective cap 200), max_cell_chars 1..16,384 when supplied; cursor is query-bound. These upper bounds are implementation constraints, not numeric schema maxima.
- Report validation requires 1..50 dimensions and 1..50 metrics with nonempty names; where present limit must be 1..250,000 and offset at most 2,500,000. These constraints are enforced by handlers rather than schema.

Source: [src/tools.rs:1535](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L1535-L1618) · [src/tools.rs:236](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L236-L273) · [src/tools.rs:113](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L113-L875) · [src/ga_client.rs:336](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/ga_client.rs#L336-L736).

## run_conversions_report

Validates supported conversion dimensions/metrics and conversion action resources, forwards conversionSpec and normalized report fields, then returns bounded Contract V1 report rows.

<details>
<summary>Full registered description</summary>

```text
Runs a Google Analytics conversion report using the Data API v1alpha surface. Use this for conversions, ad performance, ROAS, or attribution. Supported dimensions: campaignName, continent, country, defaultChannelGroup, deviceCategory, medium, platform, primaryChannelGroup, source, sourceMedium, sourcePlatform, subcontinent. Supported metrics: advertiserAdClicks, advertiserAdCost, advertiserAdCostPerAllConversionsByConversionDate, advertiserAdCostPerAllConversionsByInteractionDate, advertiserAdCostPerClick, advertiserAdImpressions, allConversionsByConversionDate, allConversionsByInteractionDate, returnOnAdSpendByConversionDate, returnOnAdSpendByInteractionDate, totalRevenueByConversionDate, totalRevenueByInteractionDate. This alpha feature may not be available to every property.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `conversion_spec` | Yes | ConversionSpecArgs | Not declared |
| `currency_code` | No | string or null | null |
| `cursor` | No | string or null | null |
| `date_ranges` | Yes | array of ReportDateRangeSchema | Not declared |
| `dimension_filter` | No | any | null |
| `dimensions` | Yes | array of string | Not declared |
| `limit` | No | integer or null | null |
| `max_cell_chars` | No | integer or null | null |
| `max_rows` | No | integer or null | null |
| `metric_filter` | No | any | null |
| `metrics` | Yes | array of string | Not declared |
| `offset` | No | integer or null | null |
| `order_bys` | No | array or null | null |
| `output_mode` | No | TabularOutputMode or null | Not declared |
| `property_id` | Yes | PropertyId | Not declared |
| `return_property_quota` | No | boolean | false |
| `summary_only` | No | boolean | false |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "$defs": {
    "AttributionModel": {
      "enum": [
        "DATA_DRIVEN",
        "LAST_CLICK"
      ],
      "type": "string"
    },
    "ConversionSpecArgs": {
      "additionalProperties": false,
      "properties": {
        "attribution_model": {
          "anyOf": [
            {
              "$ref": "#/$defs/AttributionModel"
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "description": "Attribution model. Google defaults to DATA_DRIVEN when omitted."
        },
        "conversion_actions": {
          "default": [],
          "description": "Conversion action resource names such as `conversionActions/1234`. An empty list means all conversions.",
          "items": {
            "type": "string"
          },
          "type": "array"
        }
      },
      "type": "object"
    },
    "PropertyId": {
      "anyOf": [
        {
          "format": "uint64",
          "minimum": 0,
          "type": "integer"
        },
        {
          "type": "string"
        }
      ]
    },
    "ReportDateRangeSchema": {
      "properties": {
        "end_date": {
          "description": "Inclusive end date (for example `2026-02-07`, `yesterday`).",
          "type": "string"
        },
        "start_date": {
          "description": "Inclusive start date (for example `2026-02-01`, `7daysAgo`).",
          "type": "string"
        }
      },
      "required": [
        "start_date",
        "end_date"
      ],
      "type": "object"
    },
    "TabularOutputMode": {
      "enum": [
        "rows",
        "tuples",
        "scalar",
        "compact"
      ],
      "type": "string"
    }
  },
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "properties": {
    "conversion_spec": {
      "$ref": "#/$defs/ConversionSpecArgs"
    },
    "currency_code": {
      "default": null,
      "type": [
        "string",
        "null"
      ]
    },
    "cursor": {
      "default": null,
      "description": "Opaque pagination cursor from `meta.next_cursor`.",
      "type": [
        "string",
        "null"
      ]
    },
    "date_ranges": {
      "items": {
        "$ref": "#/$defs/ReportDateRangeSchema"
      },
      "type": "array"
    },
    "dimension_filter": {
      "default": null,
      "description": "GA FilterExpression. Accepts an object, JSON-object string, or `field==value` shorthand."
    },
    "dimensions": {
      "description": "Conversion-report dimensions. See the tool description for the supported names.",
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "limit": {
      "default": null,
      "format": "uint64",
      "minimum": 0,
      "type": [
        "integer",
        "null"
      ]
    },
    "max_cell_chars": {
      "default": null,
      "description": "Optional string clipping limit applied to response cell values.",
      "format": "uint",
      "minimum": 0,
      "type": [
        "integer",
        "null"
      ]
    },
    "max_rows": {
      "default": null,
      "description": "Optional response row cap for Contract V1 tabular payloads.",
      "format": "uint",
      "minimum": 0,
      "type": [
        "integer",
        "null"
      ]
    },
    "metric_filter": {
      "default": null,
      "description": "GA FilterExpression. Accepts an object or JSON-object string."
    },
    "metrics": {
      "description": "Conversion-report metrics. See the tool description for the supported names.",
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "offset": {
      "default": null,
      "format": "uint64",
      "minimum": 0,
      "type": [
        "integer",
        "null"
      ]
    },
    "order_bys": {
      "default": null,
      "items": true,
      "type": [
        "array",
        "null"
      ]
    },
    "output_mode": {
      "anyOf": [
        {
          "$ref": "#/$defs/TabularOutputMode"
        },
        {
          "type": "null"
        }
      ],
      "description": "Tabular output shape for the response payload."
    },
    "property_id": {
      "$ref": "#/$defs/PropertyId"
    },
    "return_property_quota": {
      "default": false,
      "type": "boolean"
    },
    "summary_only": {
      "default": false,
      "description": "If true, omit row payload and return metadata only.",
      "type": "boolean"
    }
  },
  "required": [
    "property_id",
    "date_ranges",
    "dimensions",
    "metrics",
    "conversion_spec"
  ],
  "type": "object"
}
```

</details>

- Handler tabular controls require max_rows 1..25,000 (default effective cap 200), max_cell_chars 1..16,384 when supplied; cursor is query-bound. These upper bounds are implementation constraints, not numeric schema maxima.
- Report validation requires 1..50 dimensions and 1..50 metrics with nonempty names; where present limit must be 1..250,000 and offset at most 2,500,000. These constraints are enforced by handlers rather than schema.
- Handler enforces the dimension/metric allowlists in its full description and at most 50 numeric conversionActions/<id> names.

Source: [src/tools.rs:1621](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L1621-L1714) · [src/tools.rs:303](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L303-L343) · [src/tools.rs:113](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L113-L875) · [src/ga_client.rs:336](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/ga_client.rs#L336-L736).

## run_funnel_report

Validates and normalizes event shorthand or funnel filter expressions, builds funnel steps and optional breakdown/next action/segments, then projects table and visualization subreports independently into bounded Contract V1 output.

<details>
<summary>Full registered description</summary>

```text
Runs a Google Analytics funnel report using the Data API v1alpha surface. Each funnel step must provide either an event shorthand or a complete FunnelFilterExpression. Supports open or closed funnels, standard or trended visualization, breakdowns, next-action analysis, up to four segments, dimension filters, and bounded per-subreport Contract V1 output.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `date_ranges` | No | array of ReportDateRangeSchema | [] |
| `dimension_filter` | No | any | null |
| `funnel_breakdown` | No | FunnelBreakdownArgs or null | null |
| `funnel_next_action` | No | FunnelNextActionArgs or null | null |
| `funnel_steps` | Yes | array of FunnelStepArgs | Not declared |
| `funnel_visualization_type` | No | FunnelVisualizationType or null | null |
| `is_open_funnel` | No | boolean | false |
| `limit` | No | integer or null | null |
| `max_cell_chars` | No | integer or null | null |
| `max_rows` | No | integer or null | null |
| `output_mode` | No | TabularOutputMode or null | Not declared |
| `property_id` | Yes | PropertyId | Not declared |
| `return_property_quota` | No | boolean | false |
| `segments` | No | array or null | null |
| `summary_only` | No | boolean | false |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "$defs": {
    "FunnelBreakdownArgs": {
      "additionalProperties": false,
      "properties": {
        "breakdown_dimension": {
          "description": "Dimension used to break down each funnel step, such as `deviceCategory`.",
          "type": "string"
        },
        "limit": {
          "default": null,
          "description": "Maximum distinct breakdown values. Must be 1 through 15.",
          "format": "uint64",
          "minimum": 0,
          "type": [
            "integer",
            "null"
          ]
        }
      },
      "required": [
        "breakdown_dimension"
      ],
      "type": "object"
    },
    "FunnelNextActionArgs": {
      "additionalProperties": false,
      "properties": {
        "limit": {
          "default": null,
          "description": "Maximum distinct next-action values. Must be 1 through 5.",
          "format": "uint64",
          "minimum": 0,
          "type": [
            "integer",
            "null"
          ]
        },
        "next_action_dimension": {
          "description": "Dimension used to analyze the next action, such as `eventName` or `pagePath`.",
          "type": "string"
        }
      },
      "required": [
        "next_action_dimension"
      ],
      "type": "object"
    },
    "FunnelStepArgs": {
      "additionalProperties": false,
      "properties": {
        "event": {
          "description": "Simple event-name shorthand. Mutually exclusive with `filter_expression`.",
          "type": [
            "string",
            "null"
          ]
        },
        "filter_expression": {
          "description": "Complete GA FunnelFilterExpression. Mutually exclusive with `event`."
        },
        "is_directly_followed_by": {
          "description": "Require this step to directly follow the prior step.",
          "type": [
            "boolean",
            "null"
          ]
        },
        "name": {
          "description": "Display name for the funnel step.",
          "type": [
            "string",
            "null"
          ]
        },
        "within_duration_from_prior_step": {
          "description": "Protobuf duration such as `3600s` relative to the prior step.",
          "type": [
            "string",
            "null"
          ]
        }
      },
      "type": "object"
    },
    "FunnelVisualizationType": {
      "enum": [
        "STANDARD_FUNNEL",
        "TRENDED_FUNNEL"
      ],
      "type": "string"
    },
    "PropertyId": {
      "anyOf": [
        {
          "format": "uint64",
          "minimum": 0,
          "type": "integer"
        },
        {
          "type": "string"
        }
      ]
    },
    "ReportDateRangeSchema": {
      "properties": {
        "end_date": {
          "description": "Inclusive end date (for example `2026-02-07`, `yesterday`).",
          "type": "string"
        },
        "start_date": {
          "description": "Inclusive start date (for example `2026-02-01`, `7daysAgo`).",
          "type": "string"
        }
      },
      "required": [
        "start_date",
        "end_date"
      ],
      "type": "object"
    },
    "TabularOutputMode": {
      "enum": [
        "rows",
        "tuples",
        "scalar",
        "compact"
      ],
      "type": "string"
    }
  },
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "properties": {
    "date_ranges": {
      "default": [],
      "description": "Optional report date ranges.",
      "items": {
        "$ref": "#/$defs/ReportDateRangeSchema"
      },
      "type": "array"
    },
    "dimension_filter": {
      "default": null,
      "description": "GA FilterExpression applied to dimensions. Accepts an object, JSON-object string, or `field==value` shorthand."
    },
    "funnel_breakdown": {
      "anyOf": [
        {
          "$ref": "#/$defs/FunnelBreakdownArgs"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "funnel_next_action": {
      "anyOf": [
        {
          "$ref": "#/$defs/FunnelNextActionArgs"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "funnel_steps": {
      "description": "Ordered funnel steps. Each step must set exactly one of `event` or `filter_expression`.",
      "items": {
        "$ref": "#/$defs/FunnelStepArgs"
      },
      "type": "array"
    },
    "funnel_visualization_type": {
      "anyOf": [
        {
          "$ref": "#/$defs/FunnelVisualizationType"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "is_open_funnel": {
      "default": false,
      "description": "Allow users to enter at any funnel step. Defaults to a closed funnel.",
      "type": "boolean"
    },
    "limit": {
      "default": null,
      "description": "Maximum rows requested from Google. Must be 1 through 250,000.",
      "format": "uint64",
      "minimum": 0,
      "type": [
        "integer",
        "null"
      ]
    },
    "max_cell_chars": {
      "default": null,
      "description": "Optional string clipping limit applied to subreport cell values.",
      "format": "uint",
      "minimum": 0,
      "type": [
        "integer",
        "null"
      ]
    },
    "max_rows": {
      "default": null,
      "description": "Per-subreport response row cap. Defaults to 200 and is also used to bound the upstream request.",
      "format": "uint",
      "minimum": 0,
      "type": [
        "integer",
        "null"
      ]
    },
    "output_mode": {
      "anyOf": [
        {
          "$ref": "#/$defs/TabularOutputMode"
        },
        {
          "type": "null"
        }
      ],
      "description": "Tabular output shape applied independently to the table and visualization subreports."
    },
    "property_id": {
      "$ref": "#/$defs/PropertyId"
    },
    "return_property_quota": {
      "default": false,
      "type": "boolean"
    },
    "segments": {
      "default": null,
      "description": "Optional GA segment objects. Google permits at most four.",
      "items": true,
      "type": [
        "array",
        "null"
      ]
    },
    "summary_only": {
      "default": false,
      "description": "If true, omit both subreport row payloads and return metadata only.",
      "type": "boolean"
    }
  },
  "required": [
    "property_id",
    "funnel_steps"
  ],
  "type": "object"
}
```

</details>

- Handler tabular controls require max_rows 1..25,000 (default effective cap 200), max_cell_chars 1..16,384 when supplied; cursor is query-bound. These upper bounds are implementation constraints, not numeric schema maxima.
- Handler requires 1..10 steps with exactly one event/filter_expression each, at most four nonempty segment objects, breakdown limit 1..15, next-action limit 1..5, and a combined provider-boundary JSON size at most 64 KiB; event/filter objects are normalized and validated before forwarding.

Source: [src/tools.rs:1717](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L1717-L1802) · [src/tools.rs:402](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L402-L442) · [src/tools.rs:113](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L113-L875) · [src/ga_client.rs:336](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/ga_client.rs#L336-L736).

## preview_report_request

Validates flattened run_report arguments, normalizes request payload, resolves cursor/limit/offset and returns projected columns and query hash without an upstream API call.

<details>
<summary>Full registered description</summary>

```text
Validates and previews a normalized run_report request payload and projected columns without executing the upstream GA API call.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `currency_code` | No | string or null | null |
| `cursor` | No | string or null | null |
| `date_ranges` | Yes | array of ReportDateRangeSchema | Not declared |
| `dimension_filter` | No | any | null |
| `dimensions` | Yes | array of string | Not declared |
| `limit` | No | integer or null | null |
| `max_cell_chars` | No | integer or null | null |
| `max_rows` | No | integer or null | null |
| `metric_filter` | No | any | null |
| `metrics` | Yes | array of string | Not declared |
| `offset` | No | integer or null | null |
| `order_bys` | No | array or null | null |
| `output_mode` | No | TabularOutputMode or null | Not declared |
| `property_id` | Yes | PropertyId | Not declared |
| `return_property_quota` | No | boolean | true |
| `summary_only` | No | boolean | false |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "$defs": {
    "PropertyId": {
      "anyOf": [
        {
          "format": "uint64",
          "minimum": 0,
          "type": "integer"
        },
        {
          "type": "string"
        }
      ]
    },
    "ReportDateRangeSchema": {
      "properties": {
        "end_date": {
          "description": "Inclusive end date (for example `2026-02-07`, `yesterday`).",
          "type": "string"
        },
        "start_date": {
          "description": "Inclusive start date (for example `2026-02-01`, `7daysAgo`).",
          "type": "string"
        }
      },
      "required": [
        "start_date",
        "end_date"
      ],
      "type": "object"
    },
    "TabularOutputMode": {
      "enum": [
        "rows",
        "tuples",
        "scalar",
        "compact"
      ],
      "type": "string"
    }
  },
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "properties": {
    "currency_code": {
      "default": null,
      "type": [
        "string",
        "null"
      ]
    },
    "cursor": {
      "default": null,
      "description": "Opaque pagination cursor from `meta.next_cursor`.",
      "type": [
        "string",
        "null"
      ]
    },
    "date_ranges": {
      "items": {
        "$ref": "#/$defs/ReportDateRangeSchema"
      },
      "type": "array"
    },
    "dimension_filter": {
      "default": null,
      "description": "GA FilterExpression. Accepts an object, JSON-object string, or `field==value` shorthand."
    },
    "dimensions": {
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "limit": {
      "default": null,
      "format": "uint64",
      "minimum": 0,
      "type": [
        "integer",
        "null"
      ]
    },
    "max_cell_chars": {
      "default": null,
      "description": "Optional string clipping limit applied to response cell values.",
      "format": "uint",
      "minimum": 0,
      "type": [
        "integer",
        "null"
      ]
    },
    "max_rows": {
      "default": null,
      "description": "Optional response row cap for Contract V1 tabular payloads.",
      "format": "uint",
      "minimum": 0,
      "type": [
        "integer",
        "null"
      ]
    },
    "metric_filter": {
      "default": null,
      "description": "GA FilterExpression. Accepts an object or JSON-object string."
    },
    "metrics": {
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "offset": {
      "default": null,
      "format": "uint64",
      "minimum": 0,
      "type": [
        "integer",
        "null"
      ]
    },
    "order_bys": {
      "default": null,
      "items": true,
      "type": [
        "array",
        "null"
      ]
    },
    "output_mode": {
      "anyOf": [
        {
          "$ref": "#/$defs/TabularOutputMode"
        },
        {
          "type": "null"
        }
      ],
      "description": "Tabular output shape for the response payload."
    },
    "property_id": {
      "$ref": "#/$defs/PropertyId"
    },
    "return_property_quota": {
      "default": true,
      "type": "boolean"
    },
    "summary_only": {
      "default": false,
      "description": "If true, omit row payload and return metadata only.",
      "type": "boolean"
    }
  },
  "required": [
    "property_id",
    "date_ranges",
    "dimensions",
    "metrics"
  ],
  "type": "object"
}
```

</details>

- Handler tabular controls require max_rows 1..25,000 (default effective cap 200), max_cell_chars 1..16,384 when supplied; cursor is query-bound. These upper bounds are implementation constraints, not numeric schema maxima.
- Report validation requires 1..50 dimensions and 1..50 metrics with nonempty names; where present limit must be 1..250,000 and offset at most 2,500,000. These constraints are enforced by handlers rather than schema.

Source: [src/tools.rs:1805](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L1805-L1857) · [src/tools.rs:445](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L445-L449) · [src/tools.rs:113](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L113-L875).

## run_realtime_report

Validates dimensions/metrics and row controls, resolves cursor/offset, requests sufficient realtime rows and projects a bounded Contract V1 result.

<details>
<summary>Full registered description</summary>

```text
Runs a Google Analytics realtime report using the Data API.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `cursor` | No | string or null | null |
| `dimension_filter` | No | any | null |
| `dimensions` | Yes | array of string | Not declared |
| `limit` | No | integer or null | null |
| `max_cell_chars` | No | integer or null | null |
| `max_rows` | No | integer or null | null |
| `metric_filter` | No | any | null |
| `metrics` | Yes | array of string | Not declared |
| `offset` | No | integer or null | null |
| `order_bys` | No | array or null | null |
| `output_mode` | No | TabularOutputMode or null | Not declared |
| `property_id` | Yes | PropertyId | Not declared |
| `return_property_quota` | No | boolean | true |
| `summary_only` | No | boolean | false |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "$defs": {
    "PropertyId": {
      "anyOf": [
        {
          "format": "uint64",
          "minimum": 0,
          "type": "integer"
        },
        {
          "type": "string"
        }
      ]
    },
    "TabularOutputMode": {
      "enum": [
        "rows",
        "tuples",
        "scalar",
        "compact"
      ],
      "type": "string"
    }
  },
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "properties": {
    "cursor": {
      "default": null,
      "description": "Opaque pagination cursor from `meta.next_cursor`.",
      "type": [
        "string",
        "null"
      ]
    },
    "dimension_filter": {
      "default": null,
      "description": "GA FilterExpression. Accepts an object, JSON-object string, or `field==value` shorthand."
    },
    "dimensions": {
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "limit": {
      "default": null,
      "format": "uint64",
      "minimum": 0,
      "type": [
        "integer",
        "null"
      ]
    },
    "max_cell_chars": {
      "default": null,
      "description": "Optional string clipping limit applied to response cell values.",
      "format": "uint",
      "minimum": 0,
      "type": [
        "integer",
        "null"
      ]
    },
    "max_rows": {
      "default": null,
      "description": "Optional response row cap for Contract V1 tabular payloads.",
      "format": "uint",
      "minimum": 0,
      "type": [
        "integer",
        "null"
      ]
    },
    "metric_filter": {
      "default": null,
      "description": "GA FilterExpression. Accepts an object or JSON-object string."
    },
    "metrics": {
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "offset": {
      "default": null,
      "format": "uint64",
      "minimum": 0,
      "type": [
        "integer",
        "null"
      ]
    },
    "order_bys": {
      "default": null,
      "items": true,
      "type": [
        "array",
        "null"
      ]
    },
    "output_mode": {
      "anyOf": [
        {
          "$ref": "#/$defs/TabularOutputMode"
        },
        {
          "type": "null"
        }
      ],
      "description": "Tabular output shape for the response payload."
    },
    "property_id": {
      "$ref": "#/$defs/PropertyId"
    },
    "return_property_quota": {
      "default": true,
      "type": "boolean"
    },
    "summary_only": {
      "default": false,
      "description": "If true, omit row payload and return metadata only.",
      "type": "boolean"
    }
  },
  "required": [
    "property_id",
    "dimensions",
    "metrics"
  ],
  "type": "object"
}
```

</details>

- Handler tabular controls require max_rows 1..25,000 (default effective cap 200), max_cell_chars 1..16,384 when supplied; cursor is query-bound. These upper bounds are implementation constraints, not numeric schema maxima.
- Report validation requires 1..50 dimensions and 1..50 metrics with nonempty names; where present limit must be 1..250,000 and offset at most 2,500,000. These constraints are enforced by handlers rather than schema.

Source: [src/tools.rs:1860](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L1860-L1937) · [src/tools.rs:528](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L528-L561) · [src/tools.rs:113](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L113-L875) · [src/ga_client.rs:336](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/ga_client.rs#L336-L736).

## run_pivot_report

Validates report fields and pivot definitions, resolves row controls, forwards normalized pivots and filters and projects pivot rows into Contract V1 output.

<details>
<summary>Full registered description</summary>

```text
Runs a Google Analytics pivot report using the Data API.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `currency_code` | No | string or null | null |
| `cursor` | No | string or null | null |
| `date_ranges` | Yes | array of ReportDateRangeSchema | Not declared |
| `dimension_filter` | No | any | null |
| `dimensions` | Yes | array of string | Not declared |
| `keep_empty_rows` | No | boolean | false |
| `max_cell_chars` | No | integer or null | null |
| `max_rows` | No | integer or null | null |
| `metric_filter` | No | any | null |
| `metrics` | Yes | array of string | Not declared |
| `order_bys` | No | array or null | null |
| `output_mode` | No | TabularOutputMode or null | Not declared |
| `pivots` | Yes | array of any | Not declared |
| `property_id` | Yes | PropertyId | Not declared |
| `return_property_quota` | No | boolean | true |
| `summary_only` | No | boolean | false |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "$defs": {
    "PropertyId": {
      "anyOf": [
        {
          "format": "uint64",
          "minimum": 0,
          "type": "integer"
        },
        {
          "type": "string"
        }
      ]
    },
    "ReportDateRangeSchema": {
      "properties": {
        "end_date": {
          "description": "Inclusive end date (for example `2026-02-07`, `yesterday`).",
          "type": "string"
        },
        "start_date": {
          "description": "Inclusive start date (for example `2026-02-01`, `7daysAgo`).",
          "type": "string"
        }
      },
      "required": [
        "start_date",
        "end_date"
      ],
      "type": "object"
    },
    "TabularOutputMode": {
      "enum": [
        "rows",
        "tuples",
        "scalar",
        "compact"
      ],
      "type": "string"
    }
  },
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "properties": {
    "currency_code": {
      "default": null,
      "type": [
        "string",
        "null"
      ]
    },
    "cursor": {
      "default": null,
      "description": "Opaque pagination cursor from `meta.next_cursor`.",
      "type": [
        "string",
        "null"
      ]
    },
    "date_ranges": {
      "items": {
        "$ref": "#/$defs/ReportDateRangeSchema"
      },
      "type": "array"
    },
    "dimension_filter": {
      "default": null,
      "description": "GA FilterExpression. Accepts an object, JSON-object string, or `field==value` shorthand."
    },
    "dimensions": {
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "keep_empty_rows": {
      "default": false,
      "type": "boolean"
    },
    "max_cell_chars": {
      "default": null,
      "description": "Optional string clipping limit applied to response cell values.",
      "format": "uint",
      "minimum": 0,
      "type": [
        "integer",
        "null"
      ]
    },
    "max_rows": {
      "default": null,
      "description": "Optional response row cap for Contract V1 tabular payloads.",
      "format": "uint",
      "minimum": 0,
      "type": [
        "integer",
        "null"
      ]
    },
    "metric_filter": {
      "default": null,
      "description": "GA FilterExpression. Accepts an object or JSON-object string."
    },
    "metrics": {
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "order_bys": {
      "default": null,
      "items": true,
      "type": [
        "array",
        "null"
      ]
    },
    "output_mode": {
      "anyOf": [
        {
          "$ref": "#/$defs/TabularOutputMode"
        },
        {
          "type": "null"
        }
      ],
      "description": "Tabular output shape for the response payload."
    },
    "pivots": {
      "items": true,
      "type": "array"
    },
    "property_id": {
      "$ref": "#/$defs/PropertyId"
    },
    "return_property_quota": {
      "default": true,
      "type": "boolean"
    },
    "summary_only": {
      "default": false,
      "description": "If true, omit row payload and return metadata only.",
      "type": "boolean"
    }
  },
  "required": [
    "property_id",
    "date_ranges",
    "dimensions",
    "metrics",
    "pivots"
  ],
  "type": "object"
}
```

</details>

- Handler tabular controls require max_rows 1..25,000 (default effective cap 200), max_cell_chars 1..16,384 when supplied; cursor is query-bound. These upper bounds are implementation constraints, not numeric schema maxima.
- Report validation requires 1..50 dimensions and 1..50 metrics with nonempty names; where present limit must be 1..250,000 and offset at most 2,500,000. These constraints are enforced by handlers rather than schema.
- Handler requires nonempty pivots with nonempty field_names present in dimensions; product of pivot limits must be <=100,000. Pivot JSON remains deliberately loose in schema.

Source: [src/tools.rs:1940](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L1940-L2030) · [src/tools.rs:564](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L564-L600) · [src/tools.rs:113](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L113-L875) · [src/ga_client.rs:336](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/ga_client.rs#L336-L736).

## batch_run_reports

Validates up to five requests against a common property, resolves each request cursor and tabular controls, executes one batch request and projects each report independently.

<details>
<summary>Full registered description</summary>

```text
Runs multiple Google Analytics reports in a single Data API batch request.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | PropertyId | Not declared |
| `requests` | Yes | array of BatchRunReportItemArgs | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "$defs": {
    "BatchRunReportItemArgs": {
      "properties": {
        "currency_code": {
          "default": null,
          "type": [
            "string",
            "null"
          ]
        },
        "cursor": {
          "default": null,
          "description": "Opaque pagination cursor from `meta.next_cursor`.",
          "type": [
            "string",
            "null"
          ]
        },
        "date_ranges": {
          "items": {
            "$ref": "#/$defs/ReportDateRangeSchema"
          },
          "type": "array"
        },
        "dimension_filter": {
          "default": null,
          "description": "GA FilterExpression. Accepts an object, JSON-object string, or `field==value` shorthand."
        },
        "dimensions": {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        "limit": {
          "default": null,
          "format": "uint64",
          "minimum": 0,
          "type": [
            "integer",
            "null"
          ]
        },
        "max_cell_chars": {
          "default": null,
          "description": "Optional string clipping limit applied to response cell values.",
          "format": "uint",
          "minimum": 0,
          "type": [
            "integer",
            "null"
          ]
        },
        "max_rows": {
          "default": null,
          "description": "Optional response row cap for Contract V1 tabular payloads.",
          "format": "uint",
          "minimum": 0,
          "type": [
            "integer",
            "null"
          ]
        },
        "metric_filter": {
          "default": null,
          "description": "GA FilterExpression. Accepts an object or JSON-object string."
        },
        "metrics": {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        "offset": {
          "default": null,
          "format": "uint64",
          "minimum": 0,
          "type": [
            "integer",
            "null"
          ]
        },
        "order_bys": {
          "default": null,
          "items": true,
          "type": [
            "array",
            "null"
          ]
        },
        "output_mode": {
          "anyOf": [
            {
              "$ref": "#/$defs/TabularOutputMode"
            },
            {
              "type": "null"
            }
          ],
          "description": "Tabular output shape for the response payload."
        },
        "return_property_quota": {
          "default": true,
          "type": "boolean"
        },
        "summary_only": {
          "default": false,
          "description": "If true, omit row payload and return metadata only.",
          "type": "boolean"
        }
      },
      "required": [
        "date_ranges",
        "dimensions",
        "metrics"
      ],
      "type": "object"
    },
    "PropertyId": {
      "anyOf": [
        {
          "format": "uint64",
          "minimum": 0,
          "type": "integer"
        },
        {
          "type": "string"
        }
      ]
    },
    "ReportDateRangeSchema": {
      "properties": {
        "end_date": {
          "description": "Inclusive end date (for example `2026-02-07`, `yesterday`).",
          "type": "string"
        },
        "start_date": {
          "description": "Inclusive start date (for example `2026-02-01`, `7daysAgo`).",
          "type": "string"
        }
      },
      "required": [
        "start_date",
        "end_date"
      ],
      "type": "object"
    },
    "TabularOutputMode": {
      "enum": [
        "rows",
        "tuples",
        "scalar",
        "compact"
      ],
      "type": "string"
    }
  },
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "properties": {
    "property_id": {
      "$ref": "#/$defs/PropertyId"
    },
    "requests": {
      "items": {
        "$ref": "#/$defs/BatchRunReportItemArgs"
      },
      "type": "array"
    }
  },
  "required": [
    "property_id",
    "requests"
  ],
  "type": "object"
}
```

</details>

- Handler requires 1..5 batch requests and validates each nested report and its tabular controls.

Source: [src/tools.rs:2033](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L2033-L2191) · [src/tools.rs:642](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L642-L645) · [src/tools.rs:113](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L113-L875) · [src/ga_client.rs:336](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/ga_client.rs#L336-L736).

## get_custom_dimensions_and_metrics

Fetches property metadata and returns only dimensions/metrics marked customDefinition.

<details>
<summary>Full registered description</summary>

```text
Retrieves the custom dimensions and custom metrics for a specific property.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | PropertyId | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "$defs": {
    "PropertyId": {
      "anyOf": [
        {
          "format": "uint64",
          "minimum": 0,
          "type": "integer"
        },
        {
          "type": "string"
        }
      ]
    }
  },
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "properties": {
    "property_id": {
      "$ref": "#/$defs/PropertyId",
      "description": "The Google Analytics property id as integer or \"properties/<id>\"."
    }
  },
  "required": [
    "property_id"
  ],
  "type": "object"
}
```

</details>

Source: [src/tools.rs:2194](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L2194-L2211) · [src/tools.rs:202](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L202-L205) · [src/tools.rs:113](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L113-L875) · [src/ga_client.rs:336](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/ga_client.rs#L336-L736).

## check_report_compatibility

Validates requested dimensions/metrics, requests compatibility and summarizes incompatible dimensions/metrics and reason codes.

<details>
<summary>Full registered description</summary>

```text
Preflights report dimensions/metrics via GA checkCompatibility and returns compatibility reason codes plus custom dimension/metric inventory.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `dimensions` | Yes | array of string | Not declared |
| `metrics` | Yes | array of string | Not declared |
| `property_id` | Yes | PropertyId | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "$defs": {
    "PropertyId": {
      "anyOf": [
        {
          "format": "uint64",
          "minimum": 0,
          "type": "integer"
        },
        {
          "type": "string"
        }
      ]
    }
  },
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "properties": {
    "dimensions": {
      "description": "Requested dimensions for preflight compatibility checks.",
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "metrics": {
      "description": "Requested metrics for preflight compatibility checks.",
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "property_id": {
      "$ref": "#/$defs/PropertyId",
      "description": "The Google Analytics property id as integer or \"properties/<id>\"."
    }
  },
  "required": [
    "property_id",
    "dimensions",
    "metrics"
  ],
  "type": "object"
}
```

</details>

- Report validation requires 1..50 dimensions and 1..50 metrics with nonempty names; where present limit must be 1..250,000 and offset at most 2,500,000. These constraints are enforced by handlers rather than schema.

Source: [src/tools.rs:2214](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L2214-L2262) · [src/tools.rs:208](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L208-L215) · [src/tools.rs:113](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L113-L875) · [src/ga_client.rs:336](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/ga_client.rs#L336-L736).

## scratchpad_get_runtime_limits

Reads active runtime/session limits, counts active sessions and samples session memory pressure.

<details>
<summary>Full registered description</summary>

```text
Returns active runtime scratchpad limits (including max_sessions and max_tables_per_session) without restarting the server.
```

</details>

No named input parameters are declared.

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object"
}
```

</details>

- Always advertised, but call_tool rejects all scratchpad_* tools under default read_only profile; enable scratchpad capability profile to call it.

Source: [src/tools.rs:2265](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L2265-L2299) · [src/tools.rs:654](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L654-L654) · [src/tools.rs:113](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L113-L875) · [src/config.rs:27](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/config.rs#L27-L48).

## scratchpad_set_runtime_limits

Updates maximum sessions and/or tables per session in the shared session manager and returns previous/updated limits and active-session metadata; existing sessions remain active when lowering session capacity.

<details>
<summary>Full registered description</summary>

```text
Updates runtime scratchpad limits (currently max_sessions and max_tables_per_session) without restarting the server.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `max_sessions` | No | integer or null | null |
| `max_tables_per_session` | No | integer or null | null |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "properties": {
    "max_sessions": {
      "default": null,
      "description": "Maximum number of active scratchpad sessions allowed at runtime.",
      "format": "uint",
      "minimum": 0,
      "type": [
        "integer",
        "null"
      ]
    },
    "max_tables_per_session": {
      "default": null,
      "description": "Maximum number of tables allowed per scratchpad session at runtime.",
      "format": "uint",
      "minimum": 0,
      "type": [
        "integer",
        "null"
      ]
    }
  },
  "type": "object"
}
```

</details>

- Always advertised, but call_tool rejects all scratchpad_* tools under default read_only profile; enable scratchpad capability profile to call it.
- Handler requires at least one limit; applies max_sessions before max_tables_per_session, so a later failure can leave the earlier update applied.

Source: [src/tools.rs:2302](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L2302-L2370) · [src/tools.rs:657](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L657-L664) · [src/tools.rs:113](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L113-L875) · [src/config.rs:27](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/config.rs#L27-L48).

## scratchpad_open_session

Creates or touches a temporary DuckDB session and returns TTL, row/table usage and active limits.

<details>
<summary>Full registered description</summary>

```text
Opens or refreshes a DuckDB scratchpad session and returns lifecycle metadata.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `session_id` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "properties": {
    "session_id": {
      "description": "Logical scratchpad session identifier.",
      "type": "string"
    }
  },
  "required": [
    "session_id"
  ],
  "type": "object"
}
```

</details>

- Always advertised, but call_tool rejects all scratchpad_* tools under default read_only profile; enable scratchpad capability profile to call it.

Source: [src/tools.rs:2373](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L2373-L2414) · [src/tools.rs:648](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L648-L651) · [src/tools.rs:113](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L113-L875) · [src/config.rs:27](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/config.rs#L27-L48).

## scratchpad_close_session

Releases the named DuckDB session and removes temporary state, returning whether it was closed.

<details>
<summary>Full registered description</summary>

```text
Closes a DuckDB scratchpad session and removes its temporary state.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `session_id` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "properties": {
    "session_id": {
      "description": "Logical scratchpad session identifier.",
      "type": "string"
    }
  },
  "required": [
    "session_id"
  ],
  "type": "object"
}
```

</details>

- Always advertised, but call_tool rejects all scratchpad_* tools under default read_only profile; enable scratchpad capability profile to call it.

Source: [src/tools.rs:2417](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L2417-L2436) · [src/tools.rs:648](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L648-L651) · [src/tools.rs:113](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L113-L875) · [src/config.rs:27](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/config.rs#L27-L48).

## scratchpad_list_sessions

Returns bounded active-session inventory with lifecycle and row/table usage.

<details>
<summary>Full registered description</summary>

```text
Lists active DuckDB scratchpad sessions with bounded lifecycle/usage metadata.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `limit` | No | integer or null | null |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "properties": {
    "limit": {
      "default": null,
      "description": "Optional row cap for inventory listing.",
      "format": "uint",
      "minimum": 0,
      "type": [
        "integer",
        "null"
      ]
    }
  },
  "type": "object"
}
```

</details>

- Always advertised, but call_tool rejects all scratchpad_* tools under default read_only profile; enable scratchpad capability profile to call it.
- Implementation list limit defaults to 50 and must be 1..200.

Source: [src/tools.rs:2439](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L2439-L2471) · [src/tools.rs:667](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L667-L671) · [src/tools.rs:113](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L113-L875) · [src/config.rs:27](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/config.rs#L27-L48).

## scratchpad_list_tables

Lists bounded table inventory in an existing session.

<details>
<summary>Full registered description</summary>

```text
Lists table inventory for an existing DuckDB scratchpad session.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `limit` | No | integer or null | null |
| `session_id` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "properties": {
    "limit": {
      "default": null,
      "description": "Optional row cap for table inventory listing.",
      "format": "uint",
      "minimum": 0,
      "type": [
        "integer",
        "null"
      ]
    },
    "session_id": {
      "description": "Logical scratchpad session identifier.",
      "type": "string"
    }
  },
  "required": [
    "session_id"
  ],
  "type": "object"
}
```

</details>

- Always advertised, but call_tool rejects all scratchpad_* tools under default read_only profile; enable scratchpad capability profile to call it.
- Implementation list limit defaults to 50 and must be 1..200.

Source: [src/tools.rs:2474](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L2474-L2503) · [src/tools.rs:674](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L674-L680) · [src/tools.rs:113](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L113-L875) · [src/config.rs:27](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/config.rs#L27-L48).

## scratchpad_drop_table

Normalizes the identifier, drops the temporary DuckDB table with optional if_exists semantics and reclaims table/row quota.

<details>
<summary>Full registered description</summary>

```text
Drops a scratchpad table and reclaims its table slot and row quota for the session.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `if_exists` | No | boolean | false |
| `session_id` | Yes | string | Not declared |
| `table_name` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "properties": {
    "if_exists": {
      "default": false,
      "description": "If true, return success when the table is absent.",
      "type": "boolean"
    },
    "session_id": {
      "description": "Logical scratchpad session identifier.",
      "type": "string"
    },
    "table_name": {
      "description": "Scratchpad table name to drop.",
      "type": "string"
    }
  },
  "required": [
    "session_id",
    "table_name"
  ],
  "type": "object"
}
```

</details>

- Always advertised, but call_tool rejects all scratchpad_* tools under default read_only profile; enable scratchpad capability profile to call it.

Source: [src/tools.rs:2506](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L2506-L2545) · [src/tools.rs:683](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L683-L691) · [src/tools.rs:113](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L113-L875) · [src/config.rs:27](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/config.rs#L27-L48).

## scratchpad_ingest_report

Fetches paginated GA runReport results, normalizes and deduplicates SQL column names, adds parsed temporal columns and creates or appends a DuckDB table in the selected session.

<details>
<summary>Full registered description</summary>

```text
Runs a GA report and ingests the returned rows into a normalized scratchpad DuckDB table.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `append` | No | boolean | false |
| `currency_code` | No | string or null | null |
| `cursor` | No | string or null | null |
| `date_ranges` | Yes | array of ReportDateRangeSchema | Not declared |
| `dimension_filter` | No | any | null |
| `dimensions` | Yes | array of string | Not declared |
| `limit` | No | integer or null | null |
| `max_cell_chars` | No | integer or null | null |
| `max_rows` | No | integer or null | null |
| `metric_filter` | No | any | null |
| `metrics` | Yes | array of string | Not declared |
| `offset` | No | integer or null | null |
| `order_bys` | No | array or null | null |
| `output_mode` | No | TabularOutputMode or null | Not declared |
| `property_id` | Yes | PropertyId | Not declared |
| `return_property_quota` | No | boolean | true |
| `session_id` | Yes | string | Not declared |
| `summary_only` | No | boolean | false |
| `table_name` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "$defs": {
    "PropertyId": {
      "anyOf": [
        {
          "format": "uint64",
          "minimum": 0,
          "type": "integer"
        },
        {
          "type": "string"
        }
      ]
    },
    "ReportDateRangeSchema": {
      "properties": {
        "end_date": {
          "description": "Inclusive end date (for example `2026-02-07`, `yesterday`).",
          "type": "string"
        },
        "start_date": {
          "description": "Inclusive start date (for example `2026-02-01`, `7daysAgo`).",
          "type": "string"
        }
      },
      "required": [
        "start_date",
        "end_date"
      ],
      "type": "object"
    },
    "TabularOutputMode": {
      "enum": [
        "rows",
        "tuples",
        "scalar",
        "compact"
      ],
      "type": "string"
    }
  },
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "properties": {
    "append": {
      "default": false,
      "description": "If true, append rows into an existing scratchpad table with identical schema.",
      "type": "boolean"
    },
    "currency_code": {
      "default": null,
      "type": [
        "string",
        "null"
      ]
    },
    "cursor": {
      "default": null,
      "description": "Opaque pagination cursor from `meta.next_cursor`.",
      "type": [
        "string",
        "null"
      ]
    },
    "date_ranges": {
      "items": {
        "$ref": "#/$defs/ReportDateRangeSchema"
      },
      "type": "array"
    },
    "dimension_filter": {
      "default": null,
      "description": "GA FilterExpression. Accepts an object, JSON-object string, or `field==value` shorthand."
    },
    "dimensions": {
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "limit": {
      "default": null,
      "format": "uint64",
      "minimum": 0,
      "type": [
        "integer",
        "null"
      ]
    },
    "max_cell_chars": {
      "default": null,
      "description": "Optional string clipping limit applied to response cell values.",
      "format": "uint",
      "minimum": 0,
      "type": [
        "integer",
        "null"
      ]
    },
    "max_rows": {
      "default": null,
      "description": "Optional response row cap for Contract V1 tabular payloads.",
      "format": "uint",
      "minimum": 0,
      "type": [
        "integer",
        "null"
      ]
    },
    "metric_filter": {
      "default": null,
      "description": "GA FilterExpression. Accepts an object or JSON-object string."
    },
    "metrics": {
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "offset": {
      "default": null,
      "format": "uint64",
      "minimum": 0,
      "type": [
        "integer",
        "null"
      ]
    },
    "order_bys": {
      "default": null,
      "items": true,
      "type": [
        "array",
        "null"
      ]
    },
    "output_mode": {
      "anyOf": [
        {
          "$ref": "#/$defs/TabularOutputMode"
        },
        {
          "type": "null"
        }
      ],
      "description": "Tabular output shape for the response payload."
    },
    "property_id": {
      "$ref": "#/$defs/PropertyId"
    },
    "return_property_quota": {
      "default": true,
      "type": "boolean"
    },
    "session_id": {
      "description": "Logical scratchpad session identifier.",
      "type": "string"
    },
    "summary_only": {
      "default": false,
      "description": "If true, omit row payload and return metadata only.",
      "type": "boolean"
    },
    "table_name": {
      "description": "Destination scratchpad table name.",
      "type": "string"
    }
  },
  "required": [
    "session_id",
    "table_name",
    "property_id",
    "date_ranges",
    "dimensions",
    "metrics"
  ],
  "type": "object"
}
```

</details>

- Always advertised, but call_tool rejects all scratchpad_* tools under default read_only profile; enable scratchpad capability profile to call it.
- Handler rejects cursor and summary_only=true; ingestion is bounded to 100,000 rows, 256 columns and 128 upstream pages.
- Handler tabular controls require max_rows 1..25,000 (default effective cap 200), max_cell_chars 1..16,384 when supplied; cursor is query-bound. These upper bounds are implementation constraints, not numeric schema maxima.

Source: [src/tools.rs:2548](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L2548-L2615) · [src/tools.rs:694](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L694-L705) · [src/tools.rs:113](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L113-L875) · [src/ga_client.rs:336](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/ga_client.rs#L336-L736) · [src/config.rs:27](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/config.rs#L27-L48).

## scratchpad_ingest_realtime_report

Fetches GA realtime report rows, normalizes SQL columns and temporal values and creates or appends a DuckDB table in the selected session.

<details>
<summary>Full registered description</summary>

```text
Runs a GA realtime report and ingests the returned rows into a normalized scratchpad DuckDB table.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `append` | No | boolean | false |
| `cursor` | No | string or null | null |
| `dimension_filter` | No | any | null |
| `dimensions` | Yes | array of string | Not declared |
| `limit` | No | integer or null | null |
| `max_cell_chars` | No | integer or null | null |
| `max_rows` | No | integer or null | null |
| `metric_filter` | No | any | null |
| `metrics` | Yes | array of string | Not declared |
| `offset` | No | integer or null | null |
| `order_bys` | No | array or null | null |
| `output_mode` | No | TabularOutputMode or null | Not declared |
| `property_id` | Yes | PropertyId | Not declared |
| `return_property_quota` | No | boolean | true |
| `session_id` | Yes | string | Not declared |
| `summary_only` | No | boolean | false |
| `table_name` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "$defs": {
    "PropertyId": {
      "anyOf": [
        {
          "format": "uint64",
          "minimum": 0,
          "type": "integer"
        },
        {
          "type": "string"
        }
      ]
    },
    "TabularOutputMode": {
      "enum": [
        "rows",
        "tuples",
        "scalar",
        "compact"
      ],
      "type": "string"
    }
  },
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "properties": {
    "append": {
      "default": false,
      "description": "If true, append rows into an existing scratchpad table with identical schema.",
      "type": "boolean"
    },
    "cursor": {
      "default": null,
      "description": "Opaque pagination cursor from `meta.next_cursor`.",
      "type": [
        "string",
        "null"
      ]
    },
    "dimension_filter": {
      "default": null,
      "description": "GA FilterExpression. Accepts an object, JSON-object string, or `field==value` shorthand."
    },
    "dimensions": {
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "limit": {
      "default": null,
      "format": "uint64",
      "minimum": 0,
      "type": [
        "integer",
        "null"
      ]
    },
    "max_cell_chars": {
      "default": null,
      "description": "Optional string clipping limit applied to response cell values.",
      "format": "uint",
      "minimum": 0,
      "type": [
        "integer",
        "null"
      ]
    },
    "max_rows": {
      "default": null,
      "description": "Optional response row cap for Contract V1 tabular payloads.",
      "format": "uint",
      "minimum": 0,
      "type": [
        "integer",
        "null"
      ]
    },
    "metric_filter": {
      "default": null,
      "description": "GA FilterExpression. Accepts an object or JSON-object string."
    },
    "metrics": {
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "offset": {
      "default": null,
      "format": "uint64",
      "minimum": 0,
      "type": [
        "integer",
        "null"
      ]
    },
    "order_bys": {
      "default": null,
      "items": true,
      "type": [
        "array",
        "null"
      ]
    },
    "output_mode": {
      "anyOf": [
        {
          "$ref": "#/$defs/TabularOutputMode"
        },
        {
          "type": "null"
        }
      ],
      "description": "Tabular output shape for the response payload."
    },
    "property_id": {
      "$ref": "#/$defs/PropertyId"
    },
    "return_property_quota": {
      "default": true,
      "type": "boolean"
    },
    "session_id": {
      "description": "Logical scratchpad session identifier.",
      "type": "string"
    },
    "summary_only": {
      "default": false,
      "description": "If true, omit row payload and return metadata only.",
      "type": "boolean"
    },
    "table_name": {
      "description": "Destination scratchpad table name.",
      "type": "string"
    }
  },
  "required": [
    "session_id",
    "table_name",
    "property_id",
    "dimensions",
    "metrics"
  ],
  "type": "object"
}
```

</details>

- Always advertised, but call_tool rejects all scratchpad_* tools under default read_only profile; enable scratchpad capability profile to call it.
- Handler rejects cursor and summary_only=true; ingestion is bounded to 100,000 rows, 256 columns and 128 upstream pages.
- Handler tabular controls require max_rows 1..25,000 (default effective cap 200), max_cell_chars 1..16,384 when supplied; cursor is query-bound. These upper bounds are implementation constraints, not numeric schema maxima.

Source: [src/tools.rs:2618](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L2618-L2684) · [src/tools.rs:708](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L708-L719) · [src/tools.rs:113](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L113-L875) · [src/ga_client.rs:336](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/ga_client.rs#L336-L736) · [src/config.rs:27](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/config.rs#L27-L48).

## scratchpad_query

Executes policy-checked read-only DuckDB SQL in a session, computes a session/SQL-bound query hash and returns bounded rows, cursor, clipping, output-mode and summary metadata.

<details>
<summary>Full registered description</summary>

```text
Executes a read-only SQL query against a DuckDB scratchpad session with Contract V1 tabular metadata controls.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `cursor` | No | string or null | null |
| `max_cell_chars` | No | integer or null | null |
| `max_rows` | No | integer or null | null |
| `output_mode` | No | TabularOutputMode or null | Not declared |
| `session_id` | Yes | string | Not declared |
| `sql` | Yes | string | Not declared |
| `summary_only` | No | boolean | false |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "$defs": {
    "TabularOutputMode": {
      "enum": [
        "rows",
        "tuples",
        "scalar",
        "compact"
      ],
      "type": "string"
    }
  },
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "properties": {
    "cursor": {
      "default": null,
      "description": "Opaque pagination cursor from `meta.next_cursor`.",
      "type": [
        "string",
        "null"
      ]
    },
    "max_cell_chars": {
      "default": null,
      "description": "Optional string clipping limit applied to response cell values.",
      "format": "uint",
      "minimum": 0,
      "type": [
        "integer",
        "null"
      ]
    },
    "max_rows": {
      "default": null,
      "description": "Optional response row cap for Contract V1 tabular payloads.",
      "format": "uint",
      "minimum": 0,
      "type": [
        "integer",
        "null"
      ]
    },
    "output_mode": {
      "anyOf": [
        {
          "$ref": "#/$defs/TabularOutputMode"
        },
        {
          "type": "null"
        }
      ],
      "description": "Tabular output shape for the response payload."
    },
    "session_id": {
      "description": "Logical scratchpad session identifier.",
      "type": "string"
    },
    "sql": {
      "description": "Read-only SQL query against the scratchpad session.",
      "type": "string"
    },
    "summary_only": {
      "default": false,
      "description": "If true, omit row payload and return metadata only.",
      "type": "boolean"
    }
  },
  "required": [
    "session_id",
    "sql"
  ],
  "type": "object"
}
```

</details>

- Always advertised, but call_tool rejects all scratchpad_* tools under default read_only profile; enable scratchpad capability profile to call it.
- Handler tabular controls require max_rows 1..25,000 (default effective cap 200), max_cell_chars 1..16,384 when supplied; cursor is query-bound. These upper bounds are implementation constraints, not numeric schema maxima.

Source: [src/tools.rs:2687](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L2687-L2713) · [src/tools.rs:722](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L722-L742) · [src/tools.rs:113](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L113-L875) · [src/config.rs:27](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/config.rs#L27-L48).

## scratchpad_describe_table

Normalizes and quotes the table name and executes DESCRIBE SELECT * FROM the table through the scratchpad query contract.

<details>
<summary>Full registered description</summary>

```text
Describes schema metadata for a scratchpad table using DuckDB DESCRIBE.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `cursor` | No | string or null | null |
| `max_cell_chars` | No | integer or null | null |
| `max_rows` | No | integer or null | null |
| `output_mode` | No | TabularOutputMode or null | Not declared |
| `session_id` | Yes | string | Not declared |
| `summary_only` | No | boolean | false |
| `table_name` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "$defs": {
    "TabularOutputMode": {
      "enum": [
        "rows",
        "tuples",
        "scalar",
        "compact"
      ],
      "type": "string"
    }
  },
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "properties": {
    "cursor": {
      "default": null,
      "description": "Opaque pagination cursor from `meta.next_cursor`.",
      "type": [
        "string",
        "null"
      ]
    },
    "max_cell_chars": {
      "default": null,
      "description": "Optional string clipping limit applied to response cell values.",
      "format": "uint",
      "minimum": 0,
      "type": [
        "integer",
        "null"
      ]
    },
    "max_rows": {
      "default": null,
      "description": "Optional response row cap for Contract V1 tabular payloads.",
      "format": "uint",
      "minimum": 0,
      "type": [
        "integer",
        "null"
      ]
    },
    "output_mode": {
      "anyOf": [
        {
          "$ref": "#/$defs/TabularOutputMode"
        },
        {
          "type": "null"
        }
      ],
      "description": "Tabular output shape for the response payload."
    },
    "session_id": {
      "description": "Logical scratchpad session identifier.",
      "type": "string"
    },
    "summary_only": {
      "default": false,
      "description": "If true, omit row payload and return metadata only.",
      "type": "boolean"
    },
    "table_name": {
      "description": "Scratchpad table to target.",
      "type": "string"
    }
  },
  "required": [
    "session_id",
    "table_name"
  ],
  "type": "object"
}
```

</details>

- Always advertised, but call_tool rejects all scratchpad_* tools under default read_only profile; enable scratchpad capability profile to call it.
- Handler tabular controls require max_rows 1..25,000 (default effective cap 200), max_cell_chars 1..16,384 when supplied; cursor is query-bound. These upper bounds are implementation constraints, not numeric schema maxima.

Source: [src/tools.rs:2716](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L2716-L2755) · [src/tools.rs:745](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L745-L765) · [src/tools.rs:113](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L113-L875) · [src/config.rs:27](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/config.rs#L27-L48).

## scratchpad_summarize_table

Normalizes and quotes the table name and executes SUMMARIZE SELECT * FROM the table through the scratchpad query contract.

<details>
<summary>Full registered description</summary>

```text
Runs DuckDB SUMMARIZE over a scratchpad table and returns column profile statistics.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `cursor` | No | string or null | null |
| `max_cell_chars` | No | integer or null | null |
| `max_rows` | No | integer or null | null |
| `output_mode` | No | TabularOutputMode or null | Not declared |
| `session_id` | Yes | string | Not declared |
| `summary_only` | No | boolean | false |
| `table_name` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "$defs": {
    "TabularOutputMode": {
      "enum": [
        "rows",
        "tuples",
        "scalar",
        "compact"
      ],
      "type": "string"
    }
  },
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "properties": {
    "cursor": {
      "default": null,
      "description": "Opaque pagination cursor from `meta.next_cursor`.",
      "type": [
        "string",
        "null"
      ]
    },
    "max_cell_chars": {
      "default": null,
      "description": "Optional string clipping limit applied to response cell values.",
      "format": "uint",
      "minimum": 0,
      "type": [
        "integer",
        "null"
      ]
    },
    "max_rows": {
      "default": null,
      "description": "Optional response row cap for Contract V1 tabular payloads.",
      "format": "uint",
      "minimum": 0,
      "type": [
        "integer",
        "null"
      ]
    },
    "output_mode": {
      "anyOf": [
        {
          "$ref": "#/$defs/TabularOutputMode"
        },
        {
          "type": "null"
        }
      ],
      "description": "Tabular output shape for the response payload."
    },
    "session_id": {
      "description": "Logical scratchpad session identifier.",
      "type": "string"
    },
    "summary_only": {
      "default": false,
      "description": "If true, omit row payload and return metadata only.",
      "type": "boolean"
    },
    "table_name": {
      "description": "Scratchpad table to target.",
      "type": "string"
    }
  },
  "required": [
    "session_id",
    "table_name"
  ],
  "type": "object"
}
```

</details>

- Always advertised, but call_tool rejects all scratchpad_* tools under default read_only profile; enable scratchpad capability profile to call it.
- Handler tabular controls require max_rows 1..25,000 (default effective cap 200), max_cell_chars 1..16,384 when supplied; cursor is query-bound. These upper bounds are implementation constraints, not numeric schema maxima.

Source: [src/tools.rs:2758](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L2758-L2797) · [src/tools.rs:745](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L745-L765) · [src/tools.rs:113](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L113-L875) · [src/config.rs:27](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/config.rs#L27-L48).

## scratchpad_release_regression_report

Builds and runs local DuckDB SQL comparing distinct anchor/comparison events across pre/transition/post release windows, calculating ratios, baseline deviations and likely instrumentation-break confidence flags.

<details>
<summary>Full registered description</summary>

```text
Builds release-window diagnostics (pre/transition/post) with confidence flags for likely instrumentation regressions.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `anchor_event` | Yes | string | Not declared |
| `comparison_event` | Yes | string | Not declared |
| `cursor` | No | string or null | null |
| `date_column` | No | string or null | null |
| `event_column` | No | string or null | null |
| `max_cell_chars` | No | integer or null | null |
| `max_rows` | No | integer or null | null |
| `metric_column` | No | string or null | null |
| `output_mode` | No | TabularOutputMode or null | Not declared |
| `post_days` | No | integer or null | null |
| `pre_days` | No | integer or null | null |
| `release_date` | Yes | string | Not declared |
| `session_id` | Yes | string | Not declared |
| `summary_only` | No | boolean | false |
| `table_name` | Yes | string | Not declared |
| `transition_days` | No | integer or null | null |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "$defs": {
    "TabularOutputMode": {
      "enum": [
        "rows",
        "tuples",
        "scalar",
        "compact"
      ],
      "type": "string"
    }
  },
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "properties": {
    "anchor_event": {
      "description": "Anchor event used as the instrumentation signal.",
      "type": "string"
    },
    "comparison_event": {
      "description": "Comparison event used as behavior baseline.",
      "type": "string"
    },
    "cursor": {
      "default": null,
      "description": "Opaque pagination cursor from `meta.next_cursor`.",
      "type": [
        "string",
        "null"
      ]
    },
    "date_column": {
      "default": null,
      "description": "Optional date column name (defaults to `date`).",
      "type": [
        "string",
        "null"
      ]
    },
    "event_column": {
      "default": null,
      "description": "Optional event-name column (defaults to `event_name`).",
      "type": [
        "string",
        "null"
      ]
    },
    "max_cell_chars": {
      "default": null,
      "description": "Optional string clipping limit applied to response cell values.",
      "format": "uint",
      "minimum": 0,
      "type": [
        "integer",
        "null"
      ]
    },
    "max_rows": {
      "default": null,
      "description": "Optional response row cap for Contract V1 tabular payloads.",
      "format": "uint",
      "minimum": 0,
      "type": [
        "integer",
        "null"
      ]
    },
    "metric_column": {
      "default": null,
      "description": "Optional numeric metric column (defaults to row-count weighting).",
      "type": [
        "string",
        "null"
      ]
    },
    "output_mode": {
      "anyOf": [
        {
          "$ref": "#/$defs/TabularOutputMode"
        },
        {
          "type": "null"
        }
      ],
      "description": "Tabular output shape for the response payload."
    },
    "post_days": {
      "default": null,
      "description": "Number of post-release days after transition window (default: 7).",
      "format": "uint32",
      "minimum": 0,
      "type": [
        "integer",
        "null"
      ]
    },
    "pre_days": {
      "default": null,
      "description": "Number of baseline days before `release_date` (default: 7).",
      "format": "uint32",
      "minimum": 0,
      "type": [
        "integer",
        "null"
      ]
    },
    "release_date": {
      "description": "Release date in `YYYY-MM-DD`.",
      "type": "string"
    },
    "session_id": {
      "description": "Logical scratchpad session identifier.",
      "type": "string"
    },
    "summary_only": {
      "default": false,
      "description": "If true, omit row payload and return metadata only.",
      "type": "boolean"
    },
    "table_name": {
      "description": "Scratchpad table to target.",
      "type": "string"
    },
    "transition_days": {
      "default": null,
      "description": "Number of transition days from `release_date` (default: 1).",
      "format": "uint32",
      "minimum": 0,
      "type": [
        "integer",
        "null"
      ]
    }
  },
  "required": [
    "session_id",
    "table_name",
    "release_date",
    "anchor_event",
    "comparison_event"
  ],
  "type": "object"
}
```

</details>

- Always advertised, but call_tool rejects all scratchpad_* tools under default read_only profile; enable scratchpad capability profile to call it.
- Handler tabular controls require max_rows 1..25,000 (default effective cap 200), max_cell_chars 1..16,384 when supplied; cursor is query-bound. These upper bounds are implementation constraints, not numeric schema maxima.
- Handler parses an actual YYYY-MM-DD date and resolves release windows with defaults 7/1/7 days and maximum 90 days per window.

Source: [src/tools.rs:2800](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L2800-L2922) · [src/tools.rs:768](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L768-L812) · [src/tools.rs:113](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L113-L875) · [src/config.rs:27](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/config.rs#L27-L48).

## scratchpad_landing_param_shift_report

Builds and runs local DuckDB SQL extracting URL query parameters, comparing pre/post release windows and ranking parameter shifts by absolute delta with optional channel/source-medium grouping.

<details>
<summary>Full registered description</summary>

```text
Builds landing URL parameter shift diagnostics (pre vs post windows) with channel/source splits.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `channel_column` | No | string or null | null |
| `cursor` | No | string or null | null |
| `date_column` | No | string or null | null |
| `landing_url_column` | No | string or null | null |
| `max_cell_chars` | No | integer or null | null |
| `max_rows` | No | integer or null | null |
| `output_mode` | No | TabularOutputMode or null | Not declared |
| `post_days` | No | integer or null | null |
| `pre_days` | No | integer or null | null |
| `release_date` | Yes | string | Not declared |
| `session_id` | Yes | string | Not declared |
| `source_medium_column` | No | string or null | null |
| `summary_only` | No | boolean | false |
| `table_name` | Yes | string | Not declared |
| `top_n` | No | integer or null | null |
| `transition_days` | No | integer or null | null |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "$defs": {
    "TabularOutputMode": {
      "enum": [
        "rows",
        "tuples",
        "scalar",
        "compact"
      ],
      "type": "string"
    }
  },
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "properties": {
    "channel_column": {
      "default": null,
      "description": "Optional channel column; when unset, all rows are grouped under `all`.",
      "type": [
        "string",
        "null"
      ]
    },
    "cursor": {
      "default": null,
      "description": "Opaque pagination cursor from `meta.next_cursor`.",
      "type": [
        "string",
        "null"
      ]
    },
    "date_column": {
      "default": null,
      "description": "Optional date column name (defaults to `date_parsed`).",
      "type": [
        "string",
        "null"
      ]
    },
    "landing_url_column": {
      "default": null,
      "description": "Optional landing URL column (defaults to `landingpageplusquerystring`).",
      "type": [
        "string",
        "null"
      ]
    },
    "max_cell_chars": {
      "default": null,
      "description": "Optional string clipping limit applied to response cell values.",
      "format": "uint",
      "minimum": 0,
      "type": [
        "integer",
        "null"
      ]
    },
    "max_rows": {
      "default": null,
      "description": "Optional response row cap for Contract V1 tabular payloads.",
      "format": "uint",
      "minimum": 0,
      "type": [
        "integer",
        "null"
      ]
    },
    "output_mode": {
      "anyOf": [
        {
          "$ref": "#/$defs/TabularOutputMode"
        },
        {
          "type": "null"
        }
      ],
      "description": "Tabular output shape for the response payload."
    },
    "post_days": {
      "default": null,
      "description": "Number of post-release days after transition window (default: 7).",
      "format": "uint32",
      "minimum": 0,
      "type": [
        "integer",
        "null"
      ]
    },
    "pre_days": {
      "default": null,
      "description": "Number of baseline days before `release_date` (default: 7).",
      "format": "uint32",
      "minimum": 0,
      "type": [
        "integer",
        "null"
      ]
    },
    "release_date": {
      "description": "Release date in `YYYY-MM-DD`.",
      "type": "string"
    },
    "session_id": {
      "description": "Logical scratchpad session identifier.",
      "type": "string"
    },
    "source_medium_column": {
      "default": null,
      "description": "Optional source/medium column; when unset, all rows are grouped under `all`.",
      "type": [
        "string",
        "null"
      ]
    },
    "summary_only": {
      "default": false,
      "description": "If true, omit row payload and return metadata only.",
      "type": "boolean"
    },
    "table_name": {
      "description": "Scratchpad table to target.",
      "type": "string"
    },
    "top_n": {
      "default": null,
      "description": "Maximum number of ranked parameter shifts to return (default: 100).",
      "format": "uint",
      "minimum": 0,
      "type": [
        "integer",
        "null"
      ]
    },
    "transition_days": {
      "default": null,
      "description": "Number of transition days from `release_date` (default: 1).",
      "format": "uint32",
      "minimum": 0,
      "type": [
        "integer",
        "null"
      ]
    }
  },
  "required": [
    "session_id",
    "table_name",
    "release_date"
  ],
  "type": "object"
}
```

</details>

- Always advertised, but call_tool rejects all scratchpad_* tools under default read_only profile; enable scratchpad capability profile to call it.
- Handler tabular controls require max_rows 1..25,000 (default effective cap 200), max_cell_chars 1..16,384 when supplied; cursor is query-bound. These upper bounds are implementation constraints, not numeric schema maxima.
- Handler parses an actual YYYY-MM-DD date and resolves release windows with defaults 7/1/7 days and maximum 90 days per window.
- Handler top_n defaults to 100 and requires 1..1,000.

Source: [src/tools.rs:2925](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L2925-L3035) · [src/tools.rs:815](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L815-L861) · [src/tools.rs:113](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L113-L875) · [src/config.rs:27](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/config.rs#L27-L48).

## scratchpad_export_evidence_bundle

Reads selected session tables, counts rows and samples rows with query hashes and column metadata, returning a JSON evidence payload and generated Markdown string; does not write export files.

<details>
<summary>Full registered description</summary>

```text
Exports a bounded JSON+Markdown evidence bundle from a scratchpad session (table inventory, sample query hashes, row counts, and sample rows).
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `sample_rows_per_table` | No | integer or null | null |
| `session_id` | Yes | string | Not declared |
| `table_names` | No | array or null | null |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "properties": {
    "sample_rows_per_table": {
      "default": null,
      "description": "Optional number of sample rows to include per table (default: 20).",
      "format": "uint",
      "minimum": 0,
      "type": [
        "integer",
        "null"
      ]
    },
    "session_id": {
      "description": "Logical scratchpad session identifier.",
      "type": "string"
    },
    "table_names": {
      "default": null,
      "description": "Optional subset of tables to include; defaults to all session tables (bounded).",
      "items": {
        "type": "string"
      },
      "type": [
        "array",
        "null"
      ]
    }
  },
  "required": [
    "session_id"
  ],
  "type": "object"
}
```

</details>

- Always advertised, but call_tool rejects all scratchpad_* tools under default read_only profile; enable scratchpad capability profile to call it.
- Sample rows per table defaults to 20 and requires 1..200; explicit table_names must contain 1..50 entries; otherwise inventory is bounded to 50 tables.

Source: [src/tools.rs:3038](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L3038-L3188) · [src/tools.rs:864](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L864-L873) · [src/tools.rs:113](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/tools.rs#L113-L875) · [src/config.rs:27](https://github.com/sednalabs/ga4-mcp/blob/847406e7ce36360216ba5bd0a71b218619b0fa8e/src/config.rs#L27-L48).

# arcbaslow/google-analytics-agent

[Catalog](../../README.md) · [All tool names](../tool-index.md) · [Upstream](https://github.com/arcbaslow/google-analytics-agent) · [JSON](../../data/mcps/arcbaslow--google-analytics-agent.json)

**47 tools:** 44 GA4, 3 other-service or server-support tools. Reviewed source: [`305af22aa787`](https://github.com/arcbaslow/google-analytics-agent/tree/305af22aa78797e3348e045d46e61814fb6b45a3).

Descriptions and parameter schemas come from the registered source definitions. Generated schemas are reconstructed from annotations or validators; live `tools/list` and authenticated API calls were not run. Loose objects remain loose.

<details>
<summary>Exposure and compatibility notes</summary>

- Source review only; no upstream code, tools/list, authenticated requests or runtime server executed.
- Source has no .git; supplied revision is authoritative.
- All 47 decorators register unconditionally in scripts/ga4_mcp.py. No optional module adds tools. Optional MCP dependency (mcp>=1.2,<2) is required for ga4-mcp; BigQuery and PDF capability dependencies are optional.
- Schemas reconstructed from AST annotations/defaults and full function docstrings. No Context injection, Pydantic input models, Field constraints or parameter docstrings are present. dict[str,Any] remains arbitrary object; dict[str,str] has string additionalProperties. Runtime FastMCP/Pydantic presentation details may vary with installed versions.
- Admin writer tools default to previews; the non-TTY MCP transport cannot satisfy interactive terminal approval. Local proposal support deliberately has no MCP execution tool.
- Auth-guarded tools apply a read budget, PII scrubbing and structured auth/API/confirmation error handling; cache and support file writes may accompany read operations.

</details>

## Tools

| Tool | Scope | Effect |
| --- | --- | --- |
| [`bigquery_dry_run`](#bigquery_dry_run) | GA4 | read |
| [`realtime_report`](#realtime_report) | GA4 | read |
| [`comparison_report`](#comparison_report) | GA4 | read |
| [`reporting_annotations`](#reporting_annotations) | GA4 | read |
| [`change_history`](#change_history) | GA4 | read |
| [`audience_template`](#audience_template) | GA4 | local |
| [`benchmarks`](#benchmarks) | Server support | local |
| [`audit`](#audit) | GA4 | read |
| [`context`](#context) | GA4 | read |
| [`funnel`](#funnel) | GA4 | read |
| [`events`](#events) | GA4 | read |
| [`check_events`](#check_events) | GA4 | read |
| [`quality`](#quality) | GA4 | read |
| [`conversions`](#conversions) | GA4 | read |
| [`attribution`](#attribution) | GA4 | read |
| [`property_config`](#property_config) | GA4 | read |
| [`user_provided_data_settings`](#user_provided_data_settings) | GA4 | read |
| [`consent_diagnostics`](#consent_diagnostics) | GA4 | read |
| [`report`](#report) | GA4 | read |
| [`report_metadata`](#report_metadata) | GA4 | read |
| [`conversion_metadata`](#conversion_metadata) | GA4 | read |
| [`advertising_report`](#advertising_report) | GA4 | read |
| [`check_compatibility`](#check_compatibility) | GA4 | read |
| [`propose_admin_write`](#propose_admin_write) | GA4 | local |
| [`admin_proposal_status`](#admin_proposal_status) | GA4 | local |
| [`add_key_event`](#add_key_event) | GA4 | mixed |
| [`delete_key_event`](#delete_key_event) | GA4 | mixed |
| [`create_audience`](#create_audience) | GA4 | mixed |
| [`archive_audience`](#archive_audience) | GA4 | mixed |
| [`add_custom_dimension`](#add_custom_dimension) | GA4 | mixed |
| [`add_custom_metric`](#add_custom_metric) | GA4 | mixed |
| [`archive_custom_dimension`](#archive_custom_dimension) | GA4 | mixed |
| [`archive_custom_metric`](#archive_custom_metric) | GA4 | mixed |
| [`add_event_edit_rule`](#add_event_edit_rule) | GA4 | mixed |
| [`add_event_create_rule`](#add_event_create_rule) | GA4 | mixed |
| [`delete_event_edit_rule`](#delete_event_edit_rule) | GA4 | mixed |
| [`property_details`](#property_details) | GA4 | read |
| [`data_streams`](#data_streams) | GA4 | read |
| [`custom_defs`](#custom_defs) | GA4 | read |
| [`key_events`](#key_events) | GA4 | read |
| [`attribution_settings`](#attribution_settings) | GA4 | read |
| [`reporting_identity`](#reporting_identity) | GA4 | read |
| [`list_audiences`](#list_audiences) | GA4 | read |
| [`list_event_rules`](#list_event_rules) | GA4 | read |
| [`list_segments`](#list_segments) | Server support | local |
| [`list_saved_reports`](#list_saved_reports) | Server support | local |
| [`run_saved_report`](#run_saved_report) | GA4 | read |

## bigquery_dry_run

Builds a fixed SELECT aggregate query against GA4 BigQuery daily export tables and submits a dry-run job to estimate bytes and cost controls; never executes the query.

<details>
<summary>Full registered description</summary>

```text
Estimate a fixed GA4 export aggregate query. Execution is CLI-only and may incur costs.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `billing_project` | Yes | string | Not declared |
| `source_project` | Yes | string | Not declared |
| `dataset` | Yes | string | Not declared |
| `location` | Yes | string | Not declared |
| `start_date` | Yes | string | Not declared |
| `end_date` | Yes | string | Not declared |
| `template` | Yes | string | Not declared |
| `event_name` | No | string or null | null |
| `parameters` | No | array of string or null | null |
| `steps` | No | array of string or null | null |
| `window_seconds` | No | integer | 3600 |
| `max_bytes` | No | integer | 1073741824 |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "title": "bigquery_dry_runArguments",
  "properties": {
    "billing_project": {
      "type": "string",
      "title": "Billing Project"
    },
    "source_project": {
      "type": "string",
      "title": "Source Project"
    },
    "dataset": {
      "type": "string",
      "title": "Dataset"
    },
    "location": {
      "type": "string",
      "title": "Location"
    },
    "start_date": {
      "type": "string",
      "title": "Start Date"
    },
    "end_date": {
      "type": "string",
      "title": "End Date"
    },
    "template": {
      "type": "string",
      "title": "Template"
    },
    "event_name": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Event Name"
    },
    "parameters": {
      "anyOf": [
        {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Parameters"
    },
    "steps": {
      "anyOf": [
        {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Steps"
    },
    "window_seconds": {
      "type": "integer",
      "default": 3600,
      "title": "Window Seconds"
    },
    "max_bytes": {
      "type": "integer",
      "default": 1073741824,
      "title": "Max Bytes"
    }
  },
  "required": [
    "billing_project",
    "source_project",
    "dataset",
    "location",
    "start_date",
    "end_date",
    "template"
  ]
}
```

</details>

- Optional google-cloud-bigquery dependency is loaded on invocation. Handler accepts fixed parameters/consent/freshness/funnel templates, dates spanning 1–31 days and validated project/dataset/event identifiers; these restrictions are not exposed as schema enums/patterns.
- max_bytes must be 1–107374182400. Missing BigQuery dependency returns unsupported. Parameter template requires 1–50 parameter names and an event; funnel template requires 2–7 steps and window_seconds 1–2678400.

Source: [scripts/ga4_mcp.py:108](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_mcp.py#L108-L139) · [scripts/ga4_bigquery.py:118](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_bigquery.py#L118-L224).

## realtime_report

Constructs a RunRealtimeReportRequest for the supplied fields, minute range, dimension filter and limit; returns uncached rows, quota and completeness without pagination.

<details>
<summary>Full registered description</summary>

```text
Read uncached realtime rows; inspect completeness. Minute 30–59 needs GA360.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |
| `metrics` | Yes | array of string | Not declared |
| `dimensions` | Yes | array of string | Not declared |
| `start_minutes_ago` | No | integer | 29 |
| `end_minutes_ago` | No | integer | 0 |
| `filter_dict` | No | object or null | null |
| `limit` | No | integer | 10000 |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "title": "realtime_reportArguments",
  "properties": {
    "property_id": {
      "type": "string",
      "title": "Property Id"
    },
    "metrics": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "title": "Metrics"
    },
    "dimensions": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "title": "Dimensions"
    },
    "start_minutes_ago": {
      "type": "integer",
      "default": 29,
      "title": "Start Minutes Ago"
    },
    "end_minutes_ago": {
      "type": "integer",
      "default": 0,
      "title": "End Minutes Ago"
    },
    "filter_dict": {
      "anyOf": [
        {
          "type": "object",
          "additionalProperties": true
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Filter Dict"
    },
    "limit": {
      "type": "integer",
      "default": 10000,
      "title": "Limit"
    }
  },
  "required": [
    "property_id",
    "metrics",
    "dimensions"
  ]
}
```

</details>

- Handler enforces 0 <= end_minutes_ago <= start_minutes_ago <= 59; minutes over 29 require GA360. Limit must be 1–250000; these bounds are not in the exposed schema. filter_dict is deliberately an arbitrary JSON object interpreted as a dimension filter.

Source: [scripts/ga4_mcp.py:142](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_mcp.py#L142-L156) · [scripts/ga4_explore.py:16](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_explore.py#L16-L63).

## comparison_report

Validates named comparisons and date ranges, converts inline filters or saved comparison identifiers, and pages a Core runReport while preserving rows, quota and metadata.

<details>
<summary>Full registered description</summary>

```text
Compare named groups and dates within one property, preserving API rows and metadata.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |
| `metrics` | Yes | array of string | Not declared |
| `dimensions` | Yes | array of string | Not declared |
| `comparisons` | Yes | array of object | Not declared |
| `date_ranges` | Yes | array of object | Not declared |
| `limit` | No | integer | 10000 |
| `page_size` | No | integer | 10000 |
| `max_pages` | No | integer | 10 |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "title": "comparison_reportArguments",
  "properties": {
    "property_id": {
      "type": "string",
      "title": "Property Id"
    },
    "metrics": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "title": "Metrics"
    },
    "dimensions": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "title": "Dimensions"
    },
    "comparisons": {
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": true
      },
      "title": "Comparisons"
    },
    "date_ranges": {
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": {
          "type": "string"
        }
      },
      "title": "Date Ranges"
    },
    "limit": {
      "type": "integer",
      "default": 10000,
      "title": "Limit"
    },
    "page_size": {
      "type": "integer",
      "default": 10000,
      "title": "Page Size"
    },
    "max_pages": {
      "type": "integer",
      "default": 10,
      "title": "Max Pages"
    }
  },
  "required": [
    "property_id",
    "metrics",
    "dimensions",
    "comparisons",
    "date_ranges"
  ]
}
```

</details>

- comparisons and date_ranges each require 1–4 uniquely named objects; names are nonblank, <=100 characters, and cannot start RESERVED_ or date_range_. Each comparison accepts name and exactly one dimension_filter or comparison; saved comparison must match comparisons/ID. Each date range requires exactly name,start_date,end_date. These are handler restrictions, not schema structure. limit/page_size: 1–250000; max_pages: 1–100.

Source: [scripts/ga4_mcp.py:159](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_mcp.py#L159-L174) · [scripts/ga4_explore.py:81](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_explore.py#L81-L145).

## reporting_annotations

Lists alpha reporting-data annotations for the property and explicit UTC date interval.

<details>
<summary>Full registered description</summary>

```text
Read annotations in an explicit date range; annotations do not prove causation.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |
| `start_date` | Yes | string | Not declared |
| `end_date` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "title": "reporting_annotationsArguments",
  "properties": {
    "property_id": {
      "type": "string",
      "title": "Property Id"
    },
    "start_date": {
      "type": "string",
      "title": "Start Date"
    },
    "end_date": {
      "type": "string",
      "title": "End Date"
    }
  },
  "required": [
    "property_id",
    "start_date",
    "end_date"
  ]
}
```

</details>

- Unconditionally registered but returns unsupported if the installed Admin client lacks ListReportingDataAnnotationsRequest. Handler requires numeric property ID and explicit YYYY-MM-DD dates spanning 1–366 days, which are not constraints in the exposed schema.

Source: [scripts/ga4_mcp.py:177](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_mcp.py#L177-L181) · [scripts/ga4_admin.py:146](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_admin.py#L146-L165).

## change_history

Searches account change-history events filtered to the property and explicit UTC date interval, using edit-scope credentials but performing only reads.

<details>
<summary>Full registered description</summary>

```text
Read API-supported changes in UTC dates. Requires edit scope but performs no write.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `account_id` | Yes | string | Not declared |
| `property_id` | Yes | string | Not declared |
| `start_date` | Yes | string | Not declared |
| `end_date` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "title": "change_historyArguments",
  "properties": {
    "account_id": {
      "type": "string",
      "title": "Account Id"
    },
    "property_id": {
      "type": "string",
      "title": "Property Id"
    },
    "start_date": {
      "type": "string",
      "title": "Start Date"
    },
    "end_date": {
      "type": "string",
      "title": "End Date"
    }
  },
  "required": [
    "account_id",
    "property_id",
    "start_date",
    "end_date"
  ]
}
```

</details>

- Requires analytics.edit scope despite being read-only; returns only selected change metadata, omitting actor identities and resource snapshots. Handler requires numeric account/property IDs and explicit YYYY-MM-DD dates spanning 1–366 days.

Source: [scripts/ga4_mcp.py:184](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_mcp.py#L184-L190) · [scripts/ga4_admin.py:168](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_admin.py#L168-L201).

## audience_template

Builds and validates an Audience protobuf definition locally for event participants, numeric event-parameter threshold, or an event sequence; no credentials or GA API calls.

<details>
<summary>Full registered description</summary>

```text
Build an offline audience definition. Creating it separately still requires terminal y/N.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `template` | Yes | string | Not declared |
| `display_name` | Yes | string | Not declared |
| `events` | Yes | array of string | Not declared |
| `membership_days` | No | integer | 30 |
| `parameter` | No | string or null | null |
| `threshold` | No | number or null | null |
| `window_seconds` | No | integer or null | null |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "title": "audience_templateArguments",
  "properties": {
    "template": {
      "type": "string",
      "title": "Template"
    },
    "display_name": {
      "type": "string",
      "title": "Display Name"
    },
    "events": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "title": "Events"
    },
    "membership_days": {
      "type": "integer",
      "default": 30,
      "title": "Membership Days"
    },
    "parameter": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Parameter"
    },
    "threshold": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Threshold"
    },
    "window_seconds": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Window Seconds"
    }
  },
  "required": [
    "template",
    "display_name",
    "events"
  ]
}
```

</details>

- Handler template choices: event_participants, event_parameter_threshold, event_sequence. Membership is 1–540 days; display name 1–100 nonblank characters; events are unique valid event names. Sequence: 2–5 events, window 1–2592000 seconds; simple templates: exactly one event and no window; threshold template requires finite numeric threshold and valid non-eventCount parameter. Schema uses plain strings/numbers without these constraints.

Source: [scripts/ga4_mcp.py:193](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_mcp.py#L193-L207) · [scripts/ga4_audience_templates.py:46](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_audience_templates.py#L46-L139).

## benchmarks

Normalizes a vertical and returns bundled heuristic benchmark bands with provenance labels; no GA API calls.

<details>
<summary>Full registered description</summary>

```text
Return unverified heuristic bands for a vertical, with provenance labels.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `vertical` | No | string | "other" |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "title": "benchmarksArguments",
  "properties": {
    "vertical": {
      "type": "string",
      "default": "other",
      "title": "Vertical"
    }
  },
  "required": []
}
```

</details>

Source: [scripts/ga4_mcp.py:210](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_mcp.py#L210-L214) · [scripts/ga4_benchmarks.py:181](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_benchmarks.py#L181-L185) · [scripts/ga4_benchmarks.py:188](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_benchmarks.py#L188-L192).

## audit

Orchestrates property context and quality, event taxonomy, funnel, key-event, attribution, property configuration and segment audits, returning their findings and resolved vertical confidence.

<details>
<summary>Full registered description</summary>

```text
Run the full GA4 audit. Returns agent outputs, context, vertical, confidence.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |
| `days` | No | integer | 28 |
| `vertical` | No | string or null | null |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "title": "auditArguments",
  "properties": {
    "property_id": {
      "type": "string",
      "title": "Property Id"
    },
    "days": {
      "type": "integer",
      "default": 28,
      "title": "Days"
    },
    "vertical": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Vertical"
    }
  },
  "required": [
    "property_id"
  ]
}
```

</details>

- Property audit reports data-filter inspection unsupported; attribution audit is skipped when no key events are configured.

Source: [scripts/ga4_mcp.py:217](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_mcp.py#L217-L229) · [scripts/ga4_audit.py:844](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_audit.py#L844-L916).

## context

Obtains website URLs from Admin data streams, fetches public website HTML/robots/sitemaps, infers vertical/platform/framework and saves or reuses property context locally.

<details>
<summary>Full registered description</summary>

```text
Profile the property's live site: vertical, platform, framework, sitemap.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |
| `refresh` | No | boolean | false |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "title": "contextArguments",
  "properties": {
    "property_id": {
      "type": "string",
      "title": "Property Id"
    },
    "refresh": {
      "type": "boolean",
      "default": false,
      "title": "Refresh"
    }
  },
  "required": [
    "property_id"
  ]
}
```

</details>

Source: [scripts/ga4_mcp.py:232](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_mcp.py#L232-L236) · [scripts/ga4_context.py:663](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_context.py#L663-L707).

## funnel

Validates event steps against a Core report, runs the alpha funnel report, computes step conversion/dropoff rates, and optionally probes postpayment events.

<details>
<summary>Full registered description</summary>

```text
Build a funnel from an ordered list of event names.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |
| `steps` | Yes | array of string | Not declared |
| `days` | No | integer | 28 |
| `check_postpayment` | No | boolean | false |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "title": "funnelArguments",
  "properties": {
    "property_id": {
      "type": "string",
      "title": "Property Id"
    },
    "steps": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "title": "Steps"
    },
    "days": {
      "type": "integer",
      "default": 28,
      "title": "Days"
    },
    "check_postpayment": {
      "type": "boolean",
      "default": false,
      "title": "Check Postpayment"
    }
  },
  "required": [
    "property_id",
    "steps"
  ]
}
```

</details>

- Handler requires 2–10 unique steps, a restriction absent from the input schema. Missing-data validation and optional postpayment diagnostics do not infer sequential ordering.

Source: [scripts/ga4_mcp.py:239](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_mcp.py#L239-L250) · [scripts/ga4_funnel.py:56](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_funnel.py#L56-L106).

## events

Runs a Core report of eventCount by eventName to list events observed in the selected lookback.

<details>
<summary>Full registered description</summary>

```text
List distinct events seen on the property.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |
| `days` | No | integer | 7 |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "title": "eventsArguments",
  "properties": {
    "property_id": {
      "type": "string",
      "title": "Property Id"
    },
    "days": {
      "type": "integer",
      "default": 7,
      "title": "Days"
    }
  },
  "required": [
    "property_id"
  ]
}
```

</details>

Source: [scripts/ga4_mcp.py:253](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_mcp.py#L253-L257) · [scripts/ga4_events.py:35](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_events.py#L35-L41).

## check_events

Lists observed event names with a Core report and marks requested event names present or missing.

<details>
<summary>Full registered description</summary>

```text
Check presence of specific events.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |
| `event_names` | Yes | array of string | Not declared |
| `days` | No | integer | 7 |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "title": "check_eventsArguments",
  "properties": {
    "property_id": {
      "type": "string",
      "title": "Property Id"
    },
    "event_names": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "title": "Event Names"
    },
    "days": {
      "type": "integer",
      "default": 7,
      "title": "Days"
    }
  },
  "required": [
    "property_id",
    "event_names"
  ]
}
```

</details>

Source: [scripts/ga4_mcp.py:260](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_mcp.py#L260-L264) · [scripts/ga4_events.py:44](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_events.py#L44-L61).

## quality

Reads Core reports to assess sampling/completeness, direct traffic and not-set shares, returning findings.

<details>
<summary>Full registered description</summary>

```text
Run the data-quality audit (sampling, direct share, not-set share).
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |
| `days` | No | integer | 28 |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "title": "qualityArguments",
  "properties": {
    "property_id": {
      "type": "string",
      "title": "Property Id"
    },
    "days": {
      "type": "integer",
      "default": 28,
      "title": "Days"
    }
  },
  "required": [
    "property_id"
  ]
}
```

</details>

Source: [scripts/ga4_mcp.py:267](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_mcp.py#L267-L271) · [scripts/ga4_audit.py:89](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_audit.py#L89-L253).

## conversions

Reads configured key events (with legacy conversion-event fallback) and checks configuration/capacity; no write.

<details>
<summary>Full registered description</summary>

```text
Audit key-events (conversions) configuration.
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
  "title": "conversionsArguments",
  "properties": {
    "property_id": {
      "type": "string",
      "title": "Property Id"
    }
  },
  "required": [
    "property_id"
  ]
}
```

</details>

Source: [scripts/ga4_mcp.py:274](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_mcp.py#L274-L278) · [scripts/ga4_audit.py:431](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_audit.py#L431-L488).

## attribution

Reads property attribution settings and a Core channel report filtered to the primary event, then computes channel analysis.

<details>
<summary>Full registered description</summary>

```text
Channel attribution analysis.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |
| `days` | No | integer | 28 |
| `primary_event` | No | string | "purchase" |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "title": "attributionArguments",
  "properties": {
    "property_id": {
      "type": "string",
      "title": "Property Id"
    },
    "days": {
      "type": "integer",
      "default": 28,
      "title": "Days"
    },
    "primary_event": {
      "type": "string",
      "default": "purchase",
      "title": "Primary Event"
    }
  },
  "required": [
    "property_id"
  ]
}
```

</details>

Source: [scripts/ga4_mcp.py:281](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_mcp.py#L281-L287) · [scripts/ga4_audit.py:494](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_audit.py#L494-L566).

## property_config

Reads property details, retention, streams and custom definitions and produces configuration findings; public data-filter coverage is reported unsupported.

<details>
<summary>Full registered description</summary>

```text
Property configuration audit.
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
  "title": "property_configArguments",
  "properties": {
    "property_id": {
      "type": "string",
      "title": "Property Id"
    }
  },
  "required": [
    "property_id"
  ]
}
```

</details>

- Data filters are a structured unsupported placeholder because this implementation has no public Admin API method for them.

Source: [scripts/ga4_mcp.py:290](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_mcp.py#L290-L294) · [scripts/ga4_audit.py:572](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_audit.py#L572-L669).

## user_provided_data_settings

Reads the alpha property user-provided-data configuration and returns structured settings/status.

<details>
<summary>Full registered description</summary>

```text
Read property UPD configuration; does not establish event consent.
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
  "title": "user_provided_data_settingsArguments",
  "properties": {
    "property_id": {
      "type": "string",
      "title": "Property Id"
    }
  },
  "required": [
    "property_id"
  ]
}
```

</details>

- Unconditionally registered; returns unsupported when the installed alpha Admin client lacks this method.

Source: [scripts/ga4_mcp.py:297](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_mcp.py#L297-L301) · [scripts/ga4_admin.py:447](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_admin.py#L447-L472).

## consent_diagnostics

Combines user-provided-data and reporting identity settings with a list of missing tag/export evidence; cannot infer consent from configuration.

<details>
<summary>Full registered description</summary>

```text
Read UPD/identity settings and list the tag/export evidence still needed.
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
  "title": "consent_diagnosticsArguments",
  "properties": {
    "property_id": {
      "type": "string",
      "title": "Property Id"
    }
  },
  "required": [
    "property_id"
  ]
}
```

</details>

- Installed-client method availability and API errors are returned separately for each setting; tool remains registered.

Source: [scripts/ga4_mcp.py:304](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_mcp.py#L304-L308) · [scripts/ga4_admin.py:475](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_admin.py#L475-L498).

## report

Runs a Core report with requested metric/dimension names and relative days, inheriting local cache, paging, quota and PII scrubbing.

<details>
<summary>Full registered description</summary>

```text
Generic GA4 runReport.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |
| `metrics` | Yes | array of string | Not declared |
| `dimensions` | Yes | array of string | Not declared |
| `days` | No | integer | 28 |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "title": "reportArguments",
  "properties": {
    "property_id": {
      "type": "string",
      "title": "Property Id"
    },
    "metrics": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "title": "Metrics"
    },
    "dimensions": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "title": "Dimensions"
    },
    "days": {
      "type": "integer",
      "default": 28,
      "title": "Days"
    }
  },
  "required": [
    "property_id",
    "metrics",
    "dimensions"
  ]
}
```

</details>

Source: [scripts/ga4_mcp.py:311](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_mcp.py#L311-L317) · [scripts/ga4_data.py:195](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_data.py#L195-L278).

## report_metadata

Reads Data API metadata for property-specific standard/custom fields, optionally using local cache; property 0 requests standard metadata.

<details>
<summary>Full registered description</summary>

```text
Discover standard/custom report fields; property 0 returns standard fields only.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |
| `use_cache` | No | boolean | true |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "title": "report_metadataArguments",
  "properties": {
    "property_id": {
      "type": "string",
      "title": "Property Id"
    },
    "use_cache": {
      "type": "boolean",
      "default": true,
      "title": "Use Cache"
    }
  },
  "required": [
    "property_id"
  ]
}
```

</details>

Source: [scripts/ga4_mcp.py:320](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_mcp.py#L320-L324) · [scripts/ga4_data.py:146](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_data.py#L146-L166).

## conversion_metadata

Reads alpha Data metadata including conversion actions/comparisons if the installed client supports ConversionSpec; otherwise returns unsupported.

<details>
<summary>Full registered description</summary>

```text
Discover alpha conversion action identifiers and advertising report fields.
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
  "title": "conversion_metadataArguments",
  "properties": {
    "property_id": {
      "type": "string",
      "title": "Property Id"
    }
  },
  "required": [
    "property_id"
  ]
}
```

</details>

- Registered unconditionally; returns unsupported if installed Data client lacks alpha ConversionSpec.

Source: [scripts/ga4_mcp.py:327](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_mcp.py#L327-L331) · [scripts/ga4_advertising.py:28](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_advertising.py#L28-L41).

## advertising_report

Builds and pages an alpha runReport with ConversionSpec, explicit dates/actions/attribution model; returns metadata and verifies the Advertising section.

<details>
<summary>Full registered description</summary>

```text
Explicit alpha advertising conversion report, separate from key-event reports.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |
| `metrics` | Yes | array of string | Not declared |
| `dimensions` | Yes | array of string | Not declared |
| `start_date` | Yes | string | Not declared |
| `end_date` | Yes | string | Not declared |
| `conversion_actions` | No | array of string or null | null |
| `attribution_model` | No | string | "DATA_DRIVEN" |
| `limit` | No | integer | 10000 |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "title": "advertising_reportArguments",
  "properties": {
    "property_id": {
      "type": "string",
      "title": "Property Id"
    },
    "metrics": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "title": "Metrics"
    },
    "dimensions": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "title": "Dimensions"
    },
    "start_date": {
      "type": "string",
      "title": "Start Date"
    },
    "end_date": {
      "type": "string",
      "title": "End Date"
    },
    "conversion_actions": {
      "anyOf": [
        {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Conversion Actions"
    },
    "attribution_model": {
      "type": "string",
      "default": "DATA_DRIVEN",
      "title": "Attribution Model"
    },
    "limit": {
      "type": "integer",
      "default": 10000,
      "title": "Limit"
    }
  },
  "required": [
    "property_id",
    "metrics",
    "dimensions",
    "start_date",
    "end_date"
  ]
}
```

</details>

- Registered unconditionally; returns unsupported if installed Data client lacks alpha ConversionSpec. Handler accepts only DATA_DRIVEN or LAST_CLICK and conversionActions/ID action identifiers, validates explicit dates and limit 1–250000; not expressed in input schema.

Source: [scripts/ga4_mcp.py:334](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_mcp.py#L334-L356) · [scripts/ga4_advertising.py:44](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_advertising.py#L44-L98).

## check_compatibility

Sends an uncached Core checkCompatibility request with selected fields and optional dimension-filter semantics; filter_dict takes precedence over filter_expr.

<details>
<summary>Full registered description</summary>

```text
Explicit uncached Core report compatibility read, not a funnel/realtime check.

Uses report dimension-filter semantics; filter_dict takes precedence.
Incompatible selected fields may return an API error.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |
| `metrics` | Yes | array of string | Not declared |
| `dimensions` | Yes | array of string | Not declared |
| `filter_expr` | No | string or null | null |
| `filter_dict` | No | object or null | null |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "title": "check_compatibilityArguments",
  "properties": {
    "property_id": {
      "type": "string",
      "title": "Property Id"
    },
    "metrics": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "title": "Metrics"
    },
    "dimensions": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "title": "Dimensions"
    },
    "filter_expr": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Filter Expr"
    },
    "filter_dict": {
      "anyOf": [
        {
          "type": "object",
          "additionalProperties": true
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Filter Dict"
    }
  },
  "required": [
    "property_id",
    "metrics",
    "dimensions"
  ]
}
```

</details>

- filter_dict is intentionally arbitrary JSON; handler builds GA dimension filter objects rather than exposing the protobuf schema.

Source: [scripts/ga4_mcp.py:359](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_mcp.py#L359-L375) · [scripts/ga4_data.py:169](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_data.py#L169-L192).

## propose_admin_write

Binds and validates an allowlisted Admin operation and arbitrary argument object, persists an expiring immutable local proposal, and returns digest and terminal approval command. Never calls an Admin writer.

<details>
<summary>Full registered description</summary>

```text
Save one exact write for the user's terminal approval; never execute it.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `operation` | Yes | string | Not declared |
| `arguments` | Yes | object | Not declared |
| `expires_seconds` | No | integer | 300 |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "title": "propose_admin_writeArguments",
  "properties": {
    "operation": {
      "type": "string",
      "title": "Operation"
    },
    "arguments": {
      "type": "object",
      "additionalProperties": true,
      "title": "Arguments"
    },
    "expires_seconds": {
      "type": "integer",
      "default": 300,
      "title": "Expires Seconds"
    }
  },
  "required": [
    "operation",
    "arguments"
  ]
}
```

</details>

- Operation must be one of the 15 ga4_approval.OPERATIONS Admin writers; arguments bind to that writer signature rather than an exposed nested model. expires_seconds must be 30–900; sensitive/scrubbed values and proposals exceeding 64 KB are rejected.

Source: [scripts/ga4_mcp.py:387](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_mcp.py#L387-L393) · [scripts/ga4_approval.py:74](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_approval.py#L74-L105).

## admin_proposal_status

Loads and verifies a local proposal and digest, then reports pending, expired, execution-unknown or stored result; never approves or executes.

<details>
<summary>Full registered description</summary>

```text
Inspect a proposal's outcome. This tool cannot approve or execute a write.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `proposal_id` | Yes | string | Not declared |
| `digest` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "title": "admin_proposal_statusArguments",
  "properties": {
    "proposal_id": {
      "type": "string",
      "title": "Proposal Id"
    },
    "digest": {
      "type": "string",
      "title": "Digest"
    }
  },
  "required": [
    "proposal_id",
    "digest"
  ]
}
```

</details>

Source: [scripts/ga4_mcp.py:396](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_mcp.py#L396-L400) · [scripts/ga4_approval.py:122](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_approval.py#L122-L137).

## add_key_event

With confirm=false returns a local dry-run preview. With confirm=true delegates to the underlying Admin writer for key-event creation with capacity checks. The writer requires interactive terminal y/N approval before obtaining write credentials or making API calls; stdio MCP cannot approve it.

<details>
<summary>Full registered description</summary>

```text
Create a key event (conversion). Preview by default; execution also requires interactive y/N approval.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |
| `event_name` | Yes | string | Not declared |
| `counting_method` | No | string | "ONCE_PER_EVENT" |
| `confirm` | No | boolean | false |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "title": "add_key_eventArguments",
  "properties": {
    "property_id": {
      "type": "string",
      "title": "Property Id"
    },
    "event_name": {
      "type": "string",
      "title": "Event Name"
    },
    "counting_method": {
      "type": "string",
      "default": "ONCE_PER_EVENT",
      "title": "Counting Method"
    },
    "confirm": {
      "type": "boolean",
      "default": false,
      "title": "Confirm"
    }
  },
  "required": [
    "property_id",
    "event_name"
  ]
}
```

</details>

- confirm=true is not approval: non-TTY stdio returns confirmation_required with applied=false before any API call. Plain definition/parameter strings have no exposed protobuf/enum constraints.

Source: [scripts/ga4_mcp.py:407](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_mcp.py#L407-L420) · [scripts/ga4_admin.py:760](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_admin.py#L760-L784).

## delete_key_event

With confirm=false returns a local dry-run preview. With confirm=true delegates to the underlying Admin writer for key-event deletion. The writer requires interactive terminal y/N approval before obtaining write credentials or making API calls; stdio MCP cannot approve it.

<details>
<summary>Full registered description</summary>

```text
Delete a key event by full resource name. Preview by default; execution also requires interactive y/N approval.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `name` | Yes | string | Not declared |
| `confirm` | No | boolean | false |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "title": "delete_key_eventArguments",
  "properties": {
    "name": {
      "type": "string",
      "title": "Name"
    },
    "confirm": {
      "type": "boolean",
      "default": false,
      "title": "Confirm"
    }
  },
  "required": [
    "name"
  ]
}
```

</details>

- confirm=true is not approval: non-TTY stdio returns confirmation_required with applied=false before any API call. Plain definition/parameter strings have no exposed protobuf/enum constraints.

Source: [scripts/ga4_mcp.py:423](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_mcp.py#L423-L429) · [scripts/ga4_admin.py:787](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_admin.py#L787-L795).

## create_audience

With confirm=false returns a local dry-run preview. With confirm=true delegates to the underlying Admin writer for audience creation from an arbitrary definition converted to an Audience protobuf. The writer requires interactive terminal y/N approval before obtaining write credentials or making API calls; stdio MCP cannot approve it.

<details>
<summary>Full registered description</summary>

```text
Create an audience from a definition dict. Preview by default; execution also requires interactive y/N approval.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |
| `definition` | Yes | object | Not declared |
| `confirm` | No | boolean | false |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "title": "create_audienceArguments",
  "properties": {
    "property_id": {
      "type": "string",
      "title": "Property Id"
    },
    "definition": {
      "type": "object",
      "additionalProperties": true,
      "title": "Definition"
    },
    "confirm": {
      "type": "boolean",
      "default": false,
      "title": "Confirm"
    }
  },
  "required": [
    "property_id",
    "definition"
  ]
}
```

</details>

- confirm=true is not approval: non-TTY stdio returns confirmation_required with applied=false before any API call. Plain definition/parameter strings have no exposed protobuf/enum constraints.

Source: [scripts/ga4_mcp.py:432](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_mcp.py#L432-L440) · [scripts/ga4_admin.py:609](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_admin.py#L609-L621).

## archive_audience

With confirm=false returns a local dry-run preview. With confirm=true delegates to the underlying Admin writer for audience archiving. The writer requires interactive terminal y/N approval before obtaining write credentials or making API calls; stdio MCP cannot approve it.

<details>
<summary>Full registered description</summary>

```text
Archive an audience by full resource name. Preview by default; execution also requires interactive y/N approval.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `audience_name` | Yes | string | Not declared |
| `confirm` | No | boolean | false |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "title": "archive_audienceArguments",
  "properties": {
    "audience_name": {
      "type": "string",
      "title": "Audience Name"
    },
    "confirm": {
      "type": "boolean",
      "default": false,
      "title": "Confirm"
    }
  },
  "required": [
    "audience_name"
  ]
}
```

</details>

- confirm=true is not approval: non-TTY stdio returns confirmation_required with applied=false before any API call. Plain definition/parameter strings have no exposed protobuf/enum constraints.

Source: [scripts/ga4_mcp.py:443](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_mcp.py#L443-L449) · [scripts/ga4_admin.py:648](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_admin.py#L648-L656).

## add_custom_dimension

With confirm=false returns a local dry-run preview. With confirm=true delegates to the underlying Admin writer for custom-dimension creation. The writer requires interactive terminal y/N approval before obtaining write credentials or making API calls; stdio MCP cannot approve it.

<details>
<summary>Full registered description</summary>

```text
Create a custom dimension. Preview by default; execution also requires interactive y/N approval.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |
| `parameter_name` | Yes | string | Not declared |
| `display_name` | Yes | string | Not declared |
| `scope` | No | string | "EVENT" |
| `description` | No | string | "" |
| `confirm` | No | boolean | false |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "title": "add_custom_dimensionArguments",
  "properties": {
    "property_id": {
      "type": "string",
      "title": "Property Id"
    },
    "parameter_name": {
      "type": "string",
      "title": "Parameter Name"
    },
    "display_name": {
      "type": "string",
      "title": "Display Name"
    },
    "scope": {
      "type": "string",
      "default": "EVENT",
      "title": "Scope"
    },
    "description": {
      "type": "string",
      "default": "",
      "title": "Description"
    },
    "confirm": {
      "type": "boolean",
      "default": false,
      "title": "Confirm"
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

- confirm=true is not approval: non-TTY stdio returns confirmation_required with applied=false before any API call. Plain definition/parameter strings have no exposed protobuf/enum constraints.

Source: [scripts/ga4_mcp.py:452](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_mcp.py#L452-L476) · [scripts/ga4_admin.py:677](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_admin.py#L677-L696).

## add_custom_metric

With confirm=false returns a local dry-run preview. With confirm=true delegates to the underlying Admin writer for custom-metric creation. The writer requires interactive terminal y/N approval before obtaining write credentials or making API calls; stdio MCP cannot approve it.

<details>
<summary>Full registered description</summary>

```text
Create a custom metric. Preview by default; execution also requires interactive y/N approval.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |
| `parameter_name` | Yes | string | Not declared |
| `display_name` | Yes | string | Not declared |
| `measurement_unit` | Yes | string | Not declared |
| `scope` | No | string | "EVENT" |
| `description` | No | string | "" |
| `confirm` | No | boolean | false |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "title": "add_custom_metricArguments",
  "properties": {
    "property_id": {
      "type": "string",
      "title": "Property Id"
    },
    "parameter_name": {
      "type": "string",
      "title": "Parameter Name"
    },
    "display_name": {
      "type": "string",
      "title": "Display Name"
    },
    "measurement_unit": {
      "type": "string",
      "title": "Measurement Unit"
    },
    "scope": {
      "type": "string",
      "default": "EVENT",
      "title": "Scope"
    },
    "description": {
      "type": "string",
      "default": "",
      "title": "Description"
    },
    "confirm": {
      "type": "boolean",
      "default": false,
      "title": "Confirm"
    }
  },
  "required": [
    "property_id",
    "parameter_name",
    "display_name",
    "measurement_unit"
  ]
}
```

</details>

- confirm=true is not approval: non-TTY stdio returns confirmation_required with applied=false before any API call. Plain definition/parameter strings have no exposed protobuf/enum constraints.

Source: [scripts/ga4_mcp.py:479](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_mcp.py#L479-L505) · [scripts/ga4_admin.py:710](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_admin.py#L710-L730).

## archive_custom_dimension

With confirm=false returns a local dry-run preview. With confirm=true delegates to the underlying Admin writer for custom-dimension archiving. The writer requires interactive terminal y/N approval before obtaining write credentials or making API calls; stdio MCP cannot approve it.

<details>
<summary>Full registered description</summary>

```text
Archive a custom dimension by full resource name. Preview by default; execution also requires interactive y/N approval.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `name` | Yes | string | Not declared |
| `confirm` | No | boolean | false |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "title": "archive_custom_dimensionArguments",
  "properties": {
    "name": {
      "type": "string",
      "title": "Name"
    },
    "confirm": {
      "type": "boolean",
      "default": false,
      "title": "Confirm"
    }
  },
  "required": [
    "name"
  ]
}
```

</details>

- confirm=true is not approval: non-TTY stdio returns confirmation_required with applied=false before any API call. Plain definition/parameter strings have no exposed protobuf/enum constraints.

Source: [scripts/ga4_mcp.py:508](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_mcp.py#L508-L514) · [scripts/ga4_admin.py:699](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_admin.py#L699-L707).

## archive_custom_metric

With confirm=false returns a local dry-run preview. With confirm=true delegates to the underlying Admin writer for custom-metric archiving. The writer requires interactive terminal y/N approval before obtaining write credentials or making API calls; stdio MCP cannot approve it.

<details>
<summary>Full registered description</summary>

```text
Archive a custom metric by full resource name. Preview by default; execution also requires interactive y/N approval.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `name` | Yes | string | Not declared |
| `confirm` | No | boolean | false |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "title": "archive_custom_metricArguments",
  "properties": {
    "name": {
      "type": "string",
      "title": "Name"
    },
    "confirm": {
      "type": "boolean",
      "default": false,
      "title": "Confirm"
    }
  },
  "required": [
    "name"
  ]
}
```

</details>

- confirm=true is not approval: non-TTY stdio returns confirmation_required with applied=false before any API call. Plain definition/parameter strings have no exposed protobuf/enum constraints.

Source: [scripts/ga4_mcp.py:517](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_mcp.py#L517-L523) · [scripts/ga4_admin.py:733](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_admin.py#L733-L741).

## add_event_edit_rule

With confirm=false returns a local dry-run preview. With confirm=true delegates to the underlying Admin writer for event edit rule creation from an arbitrary definition converted to a protobuf. The writer requires interactive terminal y/N approval before obtaining write credentials or making API calls; stdio MCP cannot approve it.

<details>
<summary>Full registered description</summary>

```text
Create an event edit rule on a data stream. Preview by default; execution also requires interactive y/N approval.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |
| `stream_id` | Yes | string | Not declared |
| `definition` | Yes | object | Not declared |
| `confirm` | No | boolean | false |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "title": "add_event_edit_ruleArguments",
  "properties": {
    "property_id": {
      "type": "string",
      "title": "Property Id"
    },
    "stream_id": {
      "type": "string",
      "title": "Stream Id"
    },
    "definition": {
      "type": "object",
      "additionalProperties": true,
      "title": "Definition"
    },
    "confirm": {
      "type": "boolean",
      "default": false,
      "title": "Confirm"
    }
  },
  "required": [
    "property_id",
    "stream_id",
    "definition"
  ]
}
```

</details>

- confirm=true is not approval: non-TTY stdio returns confirmation_required with applied=false before any API call. Plain definition/parameter strings have no exposed protobuf/enum constraints.

Source: [scripts/ga4_mcp.py:526](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_mcp.py#L526-L534) · [scripts/ga4_admin.py:513](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_admin.py#L513-L524).

## add_event_create_rule

With confirm=false returns a local dry-run preview. With confirm=true delegates to the underlying Admin writer for event create rule creation from an arbitrary definition converted to a protobuf. The writer requires interactive terminal y/N approval before obtaining write credentials or making API calls; stdio MCP cannot approve it.

<details>
<summary>Full registered description</summary>

```text
Create an event create rule on a data stream. Preview by default; execution also requires interactive y/N approval.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |
| `stream_id` | Yes | string | Not declared |
| `definition` | Yes | object | Not declared |
| `confirm` | No | boolean | false |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "title": "add_event_create_ruleArguments",
  "properties": {
    "property_id": {
      "type": "string",
      "title": "Property Id"
    },
    "stream_id": {
      "type": "string",
      "title": "Stream Id"
    },
    "definition": {
      "type": "object",
      "additionalProperties": true,
      "title": "Definition"
    },
    "confirm": {
      "type": "boolean",
      "default": false,
      "title": "Confirm"
    }
  },
  "required": [
    "property_id",
    "stream_id",
    "definition"
  ]
}
```

</details>

- confirm=true is not approval: non-TTY stdio returns confirmation_required with applied=false before any API call. Plain definition/parameter strings have no exposed protobuf/enum constraints.

Source: [scripts/ga4_mcp.py:537](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_mcp.py#L537-L545) · [scripts/ga4_admin.py:563](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_admin.py#L563-L574).

## delete_event_edit_rule

With confirm=false returns a local dry-run preview. With confirm=true delegates to the underlying Admin writer for event edit rule deletion. The writer requires interactive terminal y/N approval before obtaining write credentials or making API calls; stdio MCP cannot approve it.

<details>
<summary>Full registered description</summary>

```text
Delete an event edit rule by full resource name. Preview by default; execution also requires interactive y/N approval.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `rule_name` | Yes | string | Not declared |
| `confirm` | No | boolean | false |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "title": "delete_event_edit_ruleArguments",
  "properties": {
    "rule_name": {
      "type": "string",
      "title": "Rule Name"
    },
    "confirm": {
      "type": "boolean",
      "default": false,
      "title": "Confirm"
    }
  },
  "required": [
    "rule_name"
  ]
}
```

</details>

- confirm=true is not approval: non-TTY stdio returns confirmation_required with applied=false before any API call. Plain definition/parameter strings have no exposed protobuf/enum constraints.

Source: [scripts/ga4_mcp.py:548](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_mcp.py#L548-L554) · [scripts/ga4_admin.py:542](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_admin.py#L542-L549).

## property_details

Reads and optionally caches the Admin property summary.

<details>
<summary>Full registered description</summary>

```text
Fetch the property summary from the Admin API.
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
  "title": "property_detailsArguments",
  "properties": {
    "property_id": {
      "type": "string",
      "title": "Property Id"
    }
  },
  "required": [
    "property_id"
  ]
}
```

</details>

Source: [scripts/ga4_mcp.py:557](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_mcp.py#L557-L561) · [scripts/ga4_admin.py:219](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_admin.py#L219-L231).

## data_streams

Lists Admin data streams for the property.

<details>
<summary>Full registered description</summary>

```text
List the data streams configured on the property.
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
  "title": "data_streamsArguments",
  "properties": {
    "property_id": {
      "type": "string",
      "title": "Property Id"
    }
  },
  "required": [
    "property_id"
  ]
}
```

</details>

Source: [scripts/ga4_mcp.py:564](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_mcp.py#L564-L568) · [scripts/ga4_admin.py:234](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_admin.py#L234-L247).

## custom_defs

Lists Admin custom dimensions and custom metrics for the property.

<details>
<summary>Full registered description</summary>

```text
List custom dimensions and metrics on the property.
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
  "title": "custom_defsArguments",
  "properties": {
    "property_id": {
      "type": "string",
      "title": "Property Id"
    }
  },
  "required": [
    "property_id"
  ]
}
```

</details>

Source: [scripts/ga4_mcp.py:571](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_mcp.py#L571-L575) · [scripts/ga4_admin.py:292](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_admin.py#L292-L310).

## key_events

Lists and caches Admin key events; falls back to legacy conversion events when supported methods are absent.

<details>
<summary>Full registered description</summary>

```text
List the key events (conversions) on the property.
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
  "title": "key_eventsArguments",
  "properties": {
    "property_id": {
      "type": "string",
      "title": "Property Id"
    }
  },
  "required": [
    "property_id"
  ]
}
```

</details>

Source: [scripts/ga4_mcp.py:578](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_mcp.py#L578-L582) · [scripts/ga4_admin.py:313](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_admin.py#L313-L333).

## attribution_settings

Reads alpha Admin attribution settings and returns status when unavailable.

<details>
<summary>Full registered description</summary>

```text
Read the property's attribution settings.
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
  "title": "attribution_settingsArguments",
  "properties": {
    "property_id": {
      "type": "string",
      "title": "Property Id"
    }
  },
  "required": [
    "property_id"
  ]
}
```

</details>

Source: [scripts/ga4_mcp.py:585](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_mcp.py#L585-L589) · [scripts/ga4_admin.py:336](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_admin.py#L336-L352).

## reporting_identity

Reads alpha Admin reporting identity settings, without changing the property.

<details>
<summary>Full registered description</summary>

```text
Read the selected reporting identity; does not change the property.
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
  "title": "reporting_identityArguments",
  "properties": {
    "property_id": {
      "type": "string",
      "title": "Property Id"
    }
  },
  "required": [
    "property_id"
  ]
}
```

</details>

- Unconditionally registered; returns unsupported when the installed alpha Admin client lacks this method.

Source: [scripts/ga4_mcp.py:592](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_mcp.py#L592-L596) · [scripts/ga4_admin.py:420](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_admin.py#L420-L441).

## list_audiences

Lists alpha Admin audiences for the property.

<details>
<summary>Full registered description</summary>

```text
List the audiences on the property.
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
  "title": "list_audiencesArguments",
  "properties": {
    "property_id": {
      "type": "string",
      "title": "Property Id"
    }
  },
  "required": [
    "property_id"
  ]
}
```

</details>

Source: [scripts/ga4_mcp.py:599](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_mcp.py#L599-L603) · [scripts/ga4_admin.py:590](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_admin.py#L590-L599).

## list_event_rules

Lists alpha Admin event edit and event create rules under the property/data-stream parent.

<details>
<summary>Full registered description</summary>

```text
List event edit and create rules for a data stream.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |
| `stream_id` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "title": "list_event_rulesArguments",
  "properties": {
    "property_id": {
      "type": "string",
      "title": "Property Id"
    },
    "stream_id": {
      "type": "string",
      "title": "Stream Id"
    }
  },
  "required": [
    "property_id",
    "stream_id"
  ]
}
```

</details>

Source: [scripts/ga4_mcp.py:606](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_mcp.py#L606-L610) · [scripts/ga4_admin.py:501](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_admin.py#L501-L510).

## list_segments

Reads locally saved segment-definition JSON files; no GA API calls.

<details>
<summary>Full registered description</summary>

```text
List locally stored segment definitions.
```

</details>

No named input parameters are declared.

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "title": "list_segmentsArguments",
  "properties": {},
  "required": []
}
```

</details>

Source: [scripts/ga4_mcp.py:613](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_mcp.py#L613-L616) · [scripts/ga4_definitions.py:73](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_definitions.py#L73-L85).

## list_saved_reports

Reads locally saved custom-report-definition JSON files; no GA API calls.

<details>
<summary>Full registered description</summary>

```text
List locally stored custom report definitions.
```

</details>

No named input parameters are declared.

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "title": "list_saved_reportsArguments",
  "properties": {},
  "required": []
}
```

</details>

Source: [scripts/ga4_mcp.py:619](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_mcp.py#L619-L622) · [scripts/ga4_definitions.py:186](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_definitions.py#L186-L204).

## run_saved_report

Loads a saved report definition locally and runs a Core report using its metrics/dimensions/filter/paging/date options, overriding relative days when supplied; renders its configured output format.

<details>
<summary>Full registered description</summary>

```text
Run a saved custom report definition against a property.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `name` | Yes | string | Not declared |
| `property_id` | Yes | string | Not declared |
| `days` | No | integer or null | null |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "title": "run_saved_reportArguments",
  "properties": {
    "name": {
      "type": "string",
      "title": "Name"
    },
    "property_id": {
      "type": "string",
      "title": "Property Id"
    },
    "days": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Days"
    }
  },
  "required": [
    "name",
    "property_id"
  ]
}
```

</details>

- Output depends on saved default_format and may be JSON, CSV, Markdown, HTML or PDF bytes; optional PDF rendering dependencies may be required.

Source: [scripts/ga4_mcp.py:625](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_mcp.py#L625-L629) · [scripts/ga4_definitions.py:223](https://github.com/arcbaslow/google-analytics-agent/blob/305af22aa78797e3348e045d46e61814fb6b45a3/scripts/ga4_definitions.py#L223-L302).

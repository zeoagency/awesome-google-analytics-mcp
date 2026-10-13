# scalably-io/ga4-mcp

[Catalog](../../README.md) · [All tool names](../tool-index.md) · [Upstream](https://github.com/scalably-io/ga4-mcp) · [JSON](../../data/mcps/scalably-io--ga4-mcp.json)

**17 tools:** 17 GA4, 0 other-service or server-support tools. Reviewed source: [`90b8c28b4e62`](https://github.com/scalably-io/ga4-mcp/tree/90b8c28b4e62844fe1f1b765e3b95ce08367285b).

Descriptions and parameter schemas come from the registered source definitions. Generated schemas are reconstructed from annotations or validators; live `tools/list` and authenticated API calls were not run. Loose objects remain loose.

<details>
<summary>Exposure and compatibility notes</summary>

- Source review only; no tools/list, upstream execution or live requests. HEAD verified against supplied revision.
- All seventeen decorators register unconditionally. Imported BatchRunPivotReportsRequest has no corresponding registered tool.
- Schemas reconstructed from signatures, defaults and standard FastMCP/Pydantic annotation mapping; no Field, Annotated, custom models or injected Context. Docstrings are preserved as tool descriptions; parameter prose adds no schema bounds/enums.
- Clients load service-account credentials or ADC lazily with analytics.readonly scope. Startup credential failures are logged and server still runs.
- Wrapper completeness detection considers only top-level rows/row_count with a top-level limit; batch and nested funnel response quality/pagination may not be detected.
- pyproject.toml pins google-analytics-data==0.21.0 and google-analytics-admin==0.28.0; imports and newer alpha method availability were not verified by running/installing dependencies.

</details>

## Tools

| Tool | Scope | Effect |
| --- | --- | --- |
| [`ga4_list_account_summaries`](#ga4_list_account_summaries) | GA4 | read |
| [`ga4_get_property_details`](#ga4_get_property_details) | GA4 | read |
| [`ga4_list_data_streams`](#ga4_list_data_streams) | GA4 | read |
| [`ga4_list_custom_dimensions`](#ga4_list_custom_dimensions) | GA4 | read |
| [`ga4_list_custom_metrics`](#ga4_list_custom_metrics) | GA4 | read |
| [`ga4_list_key_events`](#ga4_list_key_events) | GA4 | read |
| [`ga4_list_audiences`](#ga4_list_audiences) | GA4 | read |
| [`ga4_list_google_ads_links`](#ga4_list_google_ads_links) | GA4 | read |
| [`ga4_list_property_annotations`](#ga4_list_property_annotations) | GA4 | read |
| [`ga4_run_access_report`](#ga4_run_access_report) | GA4 | read |
| [`ga4_get_metadata`](#ga4_get_metadata) | GA4 | read |
| [`ga4_run_report`](#ga4_run_report) | GA4 | read |
| [`ga4_batch_run_reports`](#ga4_batch_run_reports) | GA4 | read |
| [`ga4_run_pivot_report`](#ga4_run_pivot_report) | GA4 | read |
| [`ga4_run_realtime_report`](#ga4_run_realtime_report) | GA4 | read |
| [`ga4_check_compatibility`](#ga4_check_compatibility) | GA4 | read |
| [`ga4_run_funnel_report`](#ga4_run_funnel_report) | GA4 | read |

## ga4_list_account_summaries

Exhausts the account-summary pager and returns accounts plus count. Serializes protobufs to snake_case dictionaries; the shared registration wrapper returns a JSON string envelope with status, result, target, completeness/quality proof and recovery guidance, and redacts errors before raising RuntimeError.

<details>
<summary>Full registered description</summary>

```text
List every GA4 account and its child properties accessible to this service account.

CALL THIS FIRST to discover which property_id to pass into other tools. The SA
only sees accounts/properties where its email has been explicitly added as a user.

Response: {"accounts": [{account, display_name, property_summaries: [...], ...}]}.
Each property_summary has property, display_name, property_type, parent.
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
  "title": "ga4_list_account_summariesArguments"
}
```

</details>

Source: [src/scalably_ga4_mcp/server.py:338](https://github.com/scalably-io/ga4-mcp/blob/90b8c28b4e62844fe1f1b765e3b95ce08367285b/src/scalably_ga4_mcp/server.py#L338-L351) · [src/scalably_ga4_mcp/server.py:77](https://github.com/scalably-io/ga4-mcp/blob/90b8c28b4e62844fe1f1b765e3b95ce08367285b/src/scalably_ga4_mcp/server.py#L77-L116).

## ga4_get_property_details

Normalizes the property resource name and returns property metadata. Serializes protobufs to snake_case dictionaries; the shared registration wrapper returns a JSON string envelope with status, result, target, completeness/quality proof and recovery guidance, and redacts errors before raising RuntimeError.

<details>
<summary>Full registered description</summary>

```text
Full metadata for a single GA4 property.

Returns display_name, property_type, parent account, time_zone, currency_code,
industry_category, service_level, delete_time, expire_time, account reference,
create_time, update_time.

property_id: numeric (e.g. "123456789") or resource (e.g. "properties/123456789").
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
      "title": "Property Id"
    }
  },
  "required": [
    "property_id"
  ],
  "title": "ga4_get_property_detailsArguments"
}
```

</details>

- Handler requires numeric property_id or properties/NNN; this restriction is not an input-schema pattern.

Source: [src/scalably_ga4_mcp/server.py:354](https://github.com/scalably-io/ga4-mcp/blob/90b8c28b4e62844fe1f1b765e3b95ce08367285b/src/scalably_ga4_mcp/server.py#L354-L366) · [src/scalably_ga4_mcp/server.py:77](https://github.com/scalably-io/ga4-mcp/blob/90b8c28b4e62844fe1f1b765e3b95ce08367285b/src/scalably_ga4_mcp/server.py#L77-L116).

## ga4_list_data_streams

Exhausts the property data-stream pager; returns property, streams and count. Serializes protobufs to snake_case dictionaries; the shared registration wrapper returns a JSON string envelope with status, result, target, completeness/quality proof and recovery guidance, and redacts errors before raising RuntimeError.

<details>
<summary>Full registered description</summary>

```text
List all data streams (web, iOS, Android) on a GA4 property.

Useful for finding the Measurement ID (web), firebase_app_id (mobile),
or the hostname of a web stream. Each stream has its creation/update timestamps.
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
      "title": "Property Id"
    }
  },
  "required": [
    "property_id"
  ],
  "title": "ga4_list_data_streamsArguments"
}
```

</details>

- Handler requires numeric property_id or properties/NNN; this restriction is not an input-schema pattern.

Source: [src/scalably_ga4_mcp/server.py:369](https://github.com/scalably-io/ga4-mcp/blob/90b8c28b4e62844fe1f1b765e3b95ce08367285b/src/scalably_ga4_mcp/server.py#L369-L379) · [src/scalably_ga4_mcp/server.py:77](https://github.com/scalably-io/ga4-mcp/blob/90b8c28b4e62844fe1f1b765e3b95ce08367285b/src/scalably_ga4_mcp/server.py#L77-L116).

## ga4_list_custom_dimensions

Exhausts the property custom-dimension pager; returns property, dimensions and count. Serializes protobufs to snake_case dictionaries; the shared registration wrapper returns a JSON string envelope with status, result, target, completeness/quality proof and recovery guidance, and redacts errors before raising RuntimeError.

<details>
<summary>Full registered description</summary>

```text
List custom dimensions configured on a GA4 property.

Each entry contains the parameter_name (how you query it, use prefix
'customEvent:' or 'customUser:' when passing to get_metadata / run_report),
display_name, scope (EVENT|USER|ITEM), and description. Essential grounding
before running reports that reference custom fields.
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
      "title": "Property Id"
    }
  },
  "required": [
    "property_id"
  ],
  "title": "ga4_list_custom_dimensionsArguments"
}
```

</details>

- Handler requires numeric property_id or properties/NNN; this restriction is not an input-schema pattern.

Source: [src/scalably_ga4_mcp/server.py:382](https://github.com/scalably-io/ga4-mcp/blob/90b8c28b4e62844fe1f1b765e3b95ce08367285b/src/scalably_ga4_mcp/server.py#L382-L394) · [src/scalably_ga4_mcp/server.py:77](https://github.com/scalably-io/ga4-mcp/blob/90b8c28b4e62844fe1f1b765e3b95ce08367285b/src/scalably_ga4_mcp/server.py#L77-L116).

## ga4_list_custom_metrics

Exhausts the property custom-metric pager; returns property, metrics and count. Serializes protobufs to snake_case dictionaries; the shared registration wrapper returns a JSON string envelope with status, result, target, completeness/quality proof and recovery guidance, and redacts errors before raising RuntimeError.

<details>
<summary>Full registered description</summary>

```text
List custom metrics configured on a GA4 property.

Each entry: parameter_name, display_name, measurement_unit, scope, restricted_metric_type.
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
      "title": "Property Id"
    }
  },
  "required": [
    "property_id"
  ],
  "title": "ga4_list_custom_metricsArguments"
}
```

</details>

- Handler requires numeric property_id or properties/NNN; this restriction is not an input-schema pattern.

Source: [src/scalably_ga4_mcp/server.py:397](https://github.com/scalably-io/ga4-mcp/blob/90b8c28b4e62844fe1f1b765e3b95ce08367285b/src/scalably_ga4_mcp/server.py#L397-L406) · [src/scalably_ga4_mcp/server.py:77](https://github.com/scalably-io/ga4-mcp/blob/90b8c28b4e62844fe1f1b765e3b95ce08367285b/src/scalably_ga4_mcp/server.py#L77-L116).

## ga4_list_key_events

Exhausts the property key-event pager; returns property, key events and count. Serializes protobufs to snake_case dictionaries; the shared registration wrapper returns a JSON string envelope with status, result, target, completeness/quality proof and recovery guidance, and redacts errors before raising RuntimeError.

<details>
<summary>Full registered description</summary>

```text
List key events (formerly conversions) on a GA4 property.

These are the events the client has marked as conversion-worthy. Query
conversion metrics via `conversions` dimension or direct metric names.
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
      "title": "Property Id"
    }
  },
  "required": [
    "property_id"
  ],
  "title": "ga4_list_key_eventsArguments"
}
```

</details>

- Handler requires numeric property_id or properties/NNN; this restriction is not an input-schema pattern.

Source: [src/scalably_ga4_mcp/server.py:409](https://github.com/scalably-io/ga4-mcp/blob/90b8c28b4e62844fe1f1b765e3b95ce08367285b/src/scalably_ga4_mcp/server.py#L409-L419) · [src/scalably_ga4_mcp/server.py:77](https://github.com/scalably-io/ga4-mcp/blob/90b8c28b4e62844fe1f1b765e3b95ce08367285b/src/scalably_ga4_mcp/server.py#L77-L116).

## ga4_list_audiences

Exhausts the property audience pager; returns property, audiences and count. Serializes protobufs to snake_case dictionaries; the shared registration wrapper returns a JSON string envelope with status, result, target, completeness/quality proof and recovery guidance, and redacts errors before raising RuntimeError.

<details>
<summary>Full registered description</summary>

```text
List audiences defined on a GA4 property.

Each audience has name, display_name, description, membership_duration_days,
ads_personalization_enabled, event_trigger, exclusion_duration_mode, filter_clauses.
Reference audienceId as a dimension in run_report for audience-based breakdowns.

NOTE: Uses Admin v1alpha since audiences are still alpha in April 2026.
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
      "title": "Property Id"
    }
  },
  "required": [
    "property_id"
  ],
  "title": "ga4_list_audiencesArguments"
}
```

</details>

- Handler requires numeric property_id or properties/NNN; this restriction is not an input-schema pattern.

Source: [src/scalably_ga4_mcp/server.py:422](https://github.com/scalably-io/ga4-mcp/blob/90b8c28b4e62844fe1f1b765e3b95ce08367285b/src/scalably_ga4_mcp/server.py#L422-L435) · [src/scalably_ga4_mcp/server.py:77](https://github.com/scalably-io/ga4-mcp/blob/90b8c28b4e62844fe1f1b765e3b95ce08367285b/src/scalably_ga4_mcp/server.py#L77-L116).

## ga4_list_google_ads_links

Exhausts the property Google Ads link pager; returns property, links and count. Serializes protobufs to snake_case dictionaries; the shared registration wrapper returns a JSON string envelope with status, result, target, completeness/quality proof and recovery guidance, and redacts errors before raising RuntimeError.

<details>
<summary>Full registered description</summary>

```text
List Google Ads links attached to a GA4 property.

Returns customer_id (the Ads account), can_manage_clients, ads_personalization_enabled,
and creator_email. Useful to confirm Ads ↔ GA4 cross-reporting availability before
querying Ads-related dimensions like sessionGoogleAdsCampaignId.
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
      "title": "Property Id"
    }
  },
  "required": [
    "property_id"
  ],
  "title": "ga4_list_google_ads_linksArguments"
}
```

</details>

- Handler requires numeric property_id or properties/NNN; this restriction is not an input-schema pattern.

Source: [src/scalably_ga4_mcp/server.py:438](https://github.com/scalably-io/ga4-mcp/blob/90b8c28b4e62844fe1f1b765e3b95ce08367285b/src/scalably_ga4_mcp/server.py#L438-L449) · [src/scalably_ga4_mcp/server.py:77](https://github.com/scalably-io/ga4-mcp/blob/90b8c28b4e62844fe1f1b765e3b95ce08367285b/src/scalably_ga4_mcp/server.py#L77-L116).

## ga4_list_property_annotations

Exhausts the property annotation pager; returns property, annotations and count. Serializes protobufs to snake_case dictionaries; the shared registration wrapper returns a JSON string envelope with status, result, target, completeness/quality proof and recovery guidance, and redacts errors before raising RuntimeError.

<details>
<summary>Full registered description</summary>

```text
List reporting annotations on a GA4 property.

Annotations are markers (user-added or Google-system) flagging important
events on a timeline: product launches, outages, marketing pushes, so
downstream analysis can correlate metric swings with known events.

Each annotation has: name, title, description, annotation_date,
annotation_date_range, color, creator_email, system_generated.

NOTE: Uses Admin v1alpha since annotations are still alpha in April 2026.
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
      "title": "Property Id"
    }
  },
  "required": [
    "property_id"
  ],
  "title": "ga4_list_property_annotationsArguments"
}
```

</details>

- Handler requires numeric property_id or properties/NNN; this restriction is not an input-schema pattern.

Source: [src/scalably_ga4_mcp/server.py:452](https://github.com/scalably-io/ga4-mcp/blob/90b8c28b4e62844fe1f1b765e3b95ce08367285b/src/scalably_ga4_mcp/server.py#L452-L468) · [src/scalably_ga4_mcp/server.py:77](https://github.com/scalably-io/ga4-mcp/blob/90b8c28b4e62844fe1f1b765e3b95ce08367285b/src/scalably_ga4_mcp/server.py#L77-L116).

## ga4_run_access_report

Builds an access report with userEmail/accessCount and last seven days when selections are absent or empty; caps limit at 100000 and returns serialized response. Serializes protobufs to snake_case dictionaries; the shared registration wrapper returns a JSON string envelope with status, result, target, completeness/quality proof and recovery guidance, and redacts errors before raising RuntimeError.

<details>
<summary>Full registered description</summary>

```text
Audit log of who-read-what on a GA4 property (last 12 months).

dimensions (common): userEmail, accessedPropertyName.
metrics: accessCount.
date_ranges: list of {start_date, end_date} (YYYY-MM-DD or relative). Defaults to last 7d.

Use cases: identify usage of GA4 data by staff, confirm SA activity, compliance audits.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |
| `dimensions` | No | array of string or null | null |
| `metrics` | No | array of string or null | null |
| `date_ranges` | No | array of object or null | null |
| `limit` | No | integer | 1000 |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "property_id": {
      "type": "string",
      "title": "Property Id"
    },
    "dimensions": {
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
      "title": "Dimensions",
      "default": null
    },
    "metrics": {
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
      "title": "Metrics",
      "default": null
    },
    "date_ranges": {
      "anyOf": [
        {
          "type": "array",
          "items": {
            "type": "object",
            "additionalProperties": {
              "type": "string"
            }
          }
        },
        {
          "type": "null"
        }
      ],
      "title": "Date Ranges",
      "default": null
    },
    "limit": {
      "type": "integer",
      "title": "Limit",
      "default": 1000
    }
  },
  "required": [
    "property_id"
  ],
  "title": "ga4_run_access_reportArguments"
}
```

</details>

- Handler requires numeric property_id or properties/NNN; this restriction is not an input-schema pattern.
- Dictionary arguments intentionally expose arbitrary keys/values according to annotations; documented GA shapes and API protobuf validation are not nested input-schema constraints.

Source: [src/scalably_ga4_mcp/server.py:471](https://github.com/scalably-io/ga4-mcp/blob/90b8c28b4e62844fe1f1b765e3b95ce08367285b/src/scalably_ga4_mcp/server.py#L471-L499) · [src/scalably_ga4_mcp/server.py:77](https://github.com/scalably-io/ga4-mcp/blob/90b8c28b4e62844fe1f1b765e3b95ce08367285b/src/scalably_ga4_mcp/server.py#L77-L116) · [src/scalably_ga4_mcp/server.py:228](https://github.com/scalably-io/ga4-mcp/blob/90b8c28b4e62844fe1f1b765e3b95ce08367285b/src/scalably_ga4_mcp/server.py#L228-L322).

## ga4_get_metadata

Retrieves property metadata or properties/0/metadata for the universal catalog. Serializes protobufs to snake_case dictionaries; the shared registration wrapper returns a JSON string envelope with status, result, target, completeness/quality proof and recovery guidance, and redacts errors before raising RuntimeError.

<details>
<summary>Full registered description</summary>

```text
Fetch the full GA4 dimension + metric catalog for a property.

If property_id is omitted, returns the universal catalog (excludes
property-specific custom fields). Pass a property_id to include custom
dimensions and metrics like 'customEvent:foo' and 'customUser:signup_plan'.

Response: {"dimensions": [...], "metrics": [...]}. Each entry has api_name,
ui_name, description, category, custom_definition.

Call this before run_report when the agent is uncertain about field names:
GA4's catalog is large and custom fields require the property to resolve.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | No | string or null | null |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "property_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Property Id",
      "default": null
    }
  },
  "required": [],
  "title": "ga4_get_metadataArguments"
}
```

</details>

- Handler normalizes numeric IDs or properties/NNN; this restriction is not an input-schema pattern. Metadata permits omitted/empty property_id for the universal catalog.

Source: [src/scalably_ga4_mcp/server.py:505](https://github.com/scalably-io/ga4-mcp/blob/90b8c28b4e62844fe1f1b765e3b95ce08367285b/src/scalably_ga4_mcp/server.py#L505-L524) · [src/scalably_ga4_mcp/server.py:77](https://github.com/scalably-io/ga4-mcp/blob/90b8c28b4e62844fe1f1b765e3b95ce08367285b/src/scalably_ga4_mcp/server.py#L77-L116).

## ga4_run_report

Builds dimensions, metrics, date ranges, filter expressions, ordering and aggregations; forwards cohort_spec/comparisons to RunReportRequest; caps limit at 250000 and always requests quota. Serializes protobufs to snake_case dictionaries; the shared registration wrapper returns a JSON string envelope with status, result, target, completeness/quality proof and recovery guidance, and redacts errors before raising RuntimeError.

<details>
<summary>Full registered description</summary>

```text
Run a GA4 standard report. The workhorse tool.

Args:
  property_id: numeric or 'properties/NNN'.
  dimensions: list of dimension api_names (e.g. ["country", "deviceCategory", "date"]).
    Custom dims require 'customEvent:' or 'customUser:' prefixes.
  metrics: list of metric api_names (e.g. ["activeUsers", "sessions", "totalRevenue"]).
  date_ranges: list of {start_date, end_date, name?}. Accepts 'YYYY-MM-DD',
    'NdaysAgo', 'today', 'yesterday'. Up to 4 ranges.
  dimension_filter / metric_filter: filter expression dicts. Shapes:
    {"filter": {"field_name": "country", "string_filter": {"value": "US"}}}
    {"and_group": {"expressions": [...]}}
    {"or_group": {"expressions": [...]}}
    {"not_expression": {...}}
  order_bys: list of {metric: {metric_name}, desc} or {dimension: {...}}.
  metric_aggregations: list of TOTAL|MINIMUM|MAXIMUM|COUNT.
  limit: max rows (hard cap 250000 per response).
  offset: pagination offset.
  keep_empty_rows: include rows where all metrics are zero.
  currency_code: override property default for revenue metrics.
  cohort_spec / comparisons: advanced specs (see REST docs).

Gotchas surfaced in response.metadata:
  - samplingMetadatas: present if query was sampled (&gt; 10M events scanned)
  - dataLossFromOtherRow: true if high-cardinality dims collapsed into "(other)"
  - schemaRestrictionResponse: active thresholding rules
  - subjectToThresholding: true if user-privacy thresholding dropped rows

propertyQuota always included so the agent can self-throttle.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |
| `dimensions` | No | array of string or null | null |
| `metrics` | No | array of string or null | null |
| `date_ranges` | No | array of object or null | null |
| `dimension_filter` | No | object or null | null |
| `metric_filter` | No | object or null | null |
| `order_bys` | No | array of object or null | null |
| `metric_aggregations` | No | array of string or null | null |
| `limit` | No | integer | 10000 |
| `offset` | No | integer | 0 |
| `keep_empty_rows` | No | boolean | false |
| `currency_code` | No | string or null | null |
| `cohort_spec` | No | object or null | null |
| `comparisons` | No | array of object or null | null |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "property_id": {
      "type": "string",
      "title": "Property Id"
    },
    "dimensions": {
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
      "title": "Dimensions",
      "default": null
    },
    "metrics": {
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
      "title": "Metrics",
      "default": null
    },
    "date_ranges": {
      "anyOf": [
        {
          "type": "array",
          "items": {
            "type": "object",
            "additionalProperties": {
              "type": "string"
            }
          }
        },
        {
          "type": "null"
        }
      ],
      "title": "Date Ranges",
      "default": null
    },
    "dimension_filter": {
      "anyOf": [
        {
          "type": "object",
          "additionalProperties": true
        },
        {
          "type": "null"
        }
      ],
      "title": "Dimension Filter",
      "default": null
    },
    "metric_filter": {
      "anyOf": [
        {
          "type": "object",
          "additionalProperties": true
        },
        {
          "type": "null"
        }
      ],
      "title": "Metric Filter",
      "default": null
    },
    "order_bys": {
      "anyOf": [
        {
          "type": "array",
          "items": {
            "type": "object",
            "additionalProperties": true
          }
        },
        {
          "type": "null"
        }
      ],
      "title": "Order Bys",
      "default": null
    },
    "metric_aggregations": {
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
      "title": "Metric Aggregations",
      "default": null
    },
    "limit": {
      "type": "integer",
      "title": "Limit",
      "default": 10000
    },
    "offset": {
      "type": "integer",
      "title": "Offset",
      "default": 0
    },
    "keep_empty_rows": {
      "type": "boolean",
      "title": "Keep Empty Rows",
      "default": false
    },
    "currency_code": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Currency Code",
      "default": null
    },
    "cohort_spec": {
      "anyOf": [
        {
          "type": "object",
          "additionalProperties": true
        },
        {
          "type": "null"
        }
      ],
      "title": "Cohort Spec",
      "default": null
    },
    "comparisons": {
      "anyOf": [
        {
          "type": "array",
          "items": {
            "type": "object",
            "additionalProperties": true
          }
        },
        {
          "type": "null"
        }
      ],
      "title": "Comparisons",
      "default": null
    }
  },
  "required": [
    "property_id"
  ],
  "title": "ga4_run_reportArguments"
}
```

</details>

- Handler requires numeric property_id or properties/NNN; this restriction is not an input-schema pattern.
- Dictionary arguments intentionally expose arbitrary keys/values according to annotations; documented GA shapes and API protobuf validation are not nested input-schema constraints.
- Row limits are capped in handler without schema minimum/maximum; negative values are not rejected locally.

Source: [src/scalably_ga4_mcp/server.py:581](https://github.com/scalably-io/ga4-mcp/blob/90b8c28b4e62844fe1f1b765e3b95ce08367285b/src/scalably_ga4_mcp/server.py#L581-L647) · [src/scalably_ga4_mcp/server.py:77](https://github.com/scalably-io/ga4-mcp/blob/90b8c28b4e62844fe1f1b765e3b95ce08367285b/src/scalably_ga4_mcp/server.py#L77-L116) · [src/scalably_ga4_mcp/server.py:526](https://github.com/scalably-io/ga4-mcp/blob/90b8c28b4e62844fe1f1b765e3b95ce08367285b/src/scalably_ga4_mcp/server.py#L526-L578) · [src/scalably_ga4_mcp/server.py:228](https://github.com/scalably-io/ga4-mcp/blob/90b8c28b4e62844fe1f1b765e3b95ce08367285b/src/scalably_ga4_mcp/server.py#L228-L322).

## ga4_batch_run_reports

Builds up to five standard reports for the shared property using the same builder, including cohort_spec/comparisons; each report requests quota; returns batch response. Serializes protobufs to snake_case dictionaries; the shared registration wrapper returns a JSON string envelope with status, result, target, completeness/quality proof and recovery guidance, and redacts errors before raising RuntimeError.

<details>
<summary>Full registered description</summary>

```text
Run up to 5 GA4 reports in a single round-trip.

requests: list of run_report-shaped dicts. Same top-level parameters as
ga4_run_report (minus property_id, inferred from the batch). Each entry
accepts: dimensions, metrics, date_ranges, dimension_filter, metric_filter,
order_bys, metric_aggregations, limit, offset, keep_empty_rows, currency_code.

Useful when the agent needs paired views (e.g. landing pages + referrers
for the same window) and wants them atomically + under one quota call.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |
| `requests` | Yes | array of object | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "property_id": {
      "type": "string",
      "title": "Property Id"
    },
    "requests": {
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": true
      },
      "title": "Requests"
    }
  },
  "required": [
    "property_id",
    "requests"
  ],
  "title": "ga4_batch_run_reportsArguments"
}
```

</details>

- Handler requires numeric property_id or properties/NNN; this restriction is not an input-schema pattern.
- Dictionary arguments intentionally expose arbitrary keys/values according to annotations; documented GA shapes and API protobuf validation are not nested input-schema constraints.
- Maximum five requests is enforced only by handler; empty batches are not rejected locally.

Source: [src/scalably_ga4_mcp/server.py:650](https://github.com/scalably-io/ga4-mcp/blob/90b8c28b4e62844fe1f1b765e3b95ce08367285b/src/scalably_ga4_mcp/server.py#L650-L690) · [src/scalably_ga4_mcp/server.py:77](https://github.com/scalably-io/ga4-mcp/blob/90b8c28b4e62844fe1f1b765e3b95ce08367285b/src/scalably_ga4_mcp/server.py#L77-L116) · [src/scalably_ga4_mcp/server.py:526](https://github.com/scalably-io/ga4-mcp/blob/90b8c28b4e62844fe1f1b765e3b95ce08367285b/src/scalably_ga4_mcp/server.py#L526-L578) · [src/scalably_ga4_mcp/server.py:228](https://github.com/scalably-io/ga4-mcp/blob/90b8c28b4e62844fe1f1b765e3b95ce08367285b/src/scalably_ga4_mcp/server.py#L228-L322).

## ga4_run_pivot_report

Builds dimensions, metrics, date ranges, filters and Pivot objects with ordering/aggregations; caps each pivot limit at 250000 and requests quota. Serializes protobufs to snake_case dictionaries; the shared registration wrapper returns a JSON string envelope with status, result, target, completeness/quality proof and recovery guidance, and redacts errors before raising RuntimeError.

<details>
<summary>Full registered description</summary>

```text
Run a GA4 pivot report.

pivots: list of pivot specs, each with:
  - field_names: list of dimension names to pivot on
  - limit: max rows per pivot
  - offset: pagination offset
  - order_bys: list of OrderBy dicts (same shape as run_report's order_bys)
  - metric_aggregations: list of TOTAL|MINIMUM|MAXIMUM|COUNT

Use when you want a 2D view: e.g. rows=date, columns=device, values=sessions.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |
| `dimensions` | No | array of string or null | null |
| `metrics` | No | array of string or null | null |
| `pivots` | No | array of object or null | null |
| `date_ranges` | No | array of object or null | null |
| `dimension_filter` | No | object or null | null |
| `metric_filter` | No | object or null | null |
| `currency_code` | No | string or null | null |
| `keep_empty_rows` | No | boolean | false |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "property_id": {
      "type": "string",
      "title": "Property Id"
    },
    "dimensions": {
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
      "title": "Dimensions",
      "default": null
    },
    "metrics": {
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
      "title": "Metrics",
      "default": null
    },
    "pivots": {
      "anyOf": [
        {
          "type": "array",
          "items": {
            "type": "object",
            "additionalProperties": true
          }
        },
        {
          "type": "null"
        }
      ],
      "title": "Pivots",
      "default": null
    },
    "date_ranges": {
      "anyOf": [
        {
          "type": "array",
          "items": {
            "type": "object",
            "additionalProperties": {
              "type": "string"
            }
          }
        },
        {
          "type": "null"
        }
      ],
      "title": "Date Ranges",
      "default": null
    },
    "dimension_filter": {
      "anyOf": [
        {
          "type": "object",
          "additionalProperties": true
        },
        {
          "type": "null"
        }
      ],
      "title": "Dimension Filter",
      "default": null
    },
    "metric_filter": {
      "anyOf": [
        {
          "type": "object",
          "additionalProperties": true
        },
        {
          "type": "null"
        }
      ],
      "title": "Metric Filter",
      "default": null
    },
    "currency_code": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Currency Code",
      "default": null
    },
    "keep_empty_rows": {
      "type": "boolean",
      "title": "Keep Empty Rows",
      "default": false
    }
  },
  "required": [
    "property_id"
  ],
  "title": "ga4_run_pivot_reportArguments"
}
```

</details>

- Handler requires numeric property_id or properties/NNN; this restriction is not an input-schema pattern.
- Dictionary arguments intentionally expose arbitrary keys/values according to annotations; documented GA shapes and API protobuf validation are not nested input-schema constraints.
- Row limits are capped in handler without schema minimum/maximum; negative values are not rejected locally.

Source: [src/scalably_ga4_mcp/server.py:693](https://github.com/scalably-io/ga4-mcp/blob/90b8c28b4e62844fe1f1b765e3b95ce08367285b/src/scalably_ga4_mcp/server.py#L693-L751) · [src/scalably_ga4_mcp/server.py:77](https://github.com/scalably-io/ga4-mcp/blob/90b8c28b4e62844fe1f1b765e3b95ce08367285b/src/scalably_ga4_mcp/server.py#L77-L116) · [src/scalably_ga4_mcp/server.py:228](https://github.com/scalably-io/ga4-mcp/blob/90b8c28b4e62844fe1f1b765e3b95ce08367285b/src/scalably_ga4_mcp/server.py#L228-L322).

## ga4_run_realtime_report

Builds dimensions, metrics, filters, minute ranges, ordering and aggregations; caps limit at 250000 and requests quota. Serializes protobufs to snake_case dictionaries; the shared registration wrapper returns a JSON string envelope with status, result, target, completeness/quality proof and recovery guidance, and redacts errors before raising RuntimeError.

<details>
<summary>Full registered description</summary>

```text
Run a GA4 real-time report. Covers the last 30 minutes only.

IMPORTANT: realtime uses a SEPARATE, smaller dimension/metric catalog. Do NOT
pass 'date', 'totalRevenue', etc: they don't exist in realtime. Common dims:
'minutesAgo', 'country', 'deviceCategory', 'unifiedScreenName', 'eventName'.
Common metrics: 'activeUsers', 'screenPageViews', 'eventCount'.

minute_ranges: list of {start_minutes_ago, end_minutes_ago, name?}. Max 2
ranges. Values are 0-29 (0 = now, 29 = 30 min ago).

For historical / batch reports use ga4_run_report instead.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |
| `dimensions` | No | array of string or null | null |
| `metrics` | No | array of string or null | null |
| `dimension_filter` | No | object or null | null |
| `metric_filter` | No | object or null | null |
| `limit` | No | integer | 10000 |
| `minute_ranges` | No | array of object or null | null |
| `order_bys` | No | array of object or null | null |
| `metric_aggregations` | No | array of string or null | null |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "property_id": {
      "type": "string",
      "title": "Property Id"
    },
    "dimensions": {
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
      "title": "Dimensions",
      "default": null
    },
    "metrics": {
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
      "title": "Metrics",
      "default": null
    },
    "dimension_filter": {
      "anyOf": [
        {
          "type": "object",
          "additionalProperties": true
        },
        {
          "type": "null"
        }
      ],
      "title": "Dimension Filter",
      "default": null
    },
    "metric_filter": {
      "anyOf": [
        {
          "type": "object",
          "additionalProperties": true
        },
        {
          "type": "null"
        }
      ],
      "title": "Metric Filter",
      "default": null
    },
    "limit": {
      "type": "integer",
      "title": "Limit",
      "default": 10000
    },
    "minute_ranges": {
      "anyOf": [
        {
          "type": "array",
          "items": {
            "type": "object",
            "additionalProperties": {
              "type": "integer"
            }
          }
        },
        {
          "type": "null"
        }
      ],
      "title": "Minute Ranges",
      "default": null
    },
    "order_bys": {
      "anyOf": [
        {
          "type": "array",
          "items": {
            "type": "object",
            "additionalProperties": true
          }
        },
        {
          "type": "null"
        }
      ],
      "title": "Order Bys",
      "default": null
    },
    "metric_aggregations": {
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
      "title": "Metric Aggregations",
      "default": null
    }
  },
  "required": [
    "property_id"
  ],
  "title": "ga4_run_realtime_reportArguments"
}
```

</details>

- Handler requires numeric property_id or properties/NNN; this restriction is not an input-schema pattern.
- Dictionary arguments intentionally expose arbitrary keys/values according to annotations; documented GA shapes and API protobuf validation are not nested input-schema constraints.
- minute_ranges is annotated list[dict[str,int]], so a string name described in the docstring conflicts with its exposed integer value schema. Max two ranges and 0–29 bounds are documented but not checked locally.
- Row limits are capped in handler without schema minimum/maximum; negative values are not rejected locally.

Source: [src/scalably_ga4_mcp/server.py:754](https://github.com/scalably-io/ga4-mcp/blob/90b8c28b4e62844fe1f1b765e3b95ce08367285b/src/scalably_ga4_mcp/server.py#L754-L804) · [src/scalably_ga4_mcp/server.py:77](https://github.com/scalably-io/ga4-mcp/blob/90b8c28b4e62844fe1f1b765e3b95ce08367285b/src/scalably_ga4_mcp/server.py#L77-L116) · [src/scalably_ga4_mcp/server.py:228](https://github.com/scalably-io/ga4-mcp/blob/90b8c28b4e62844fe1f1b765e3b95ce08367285b/src/scalably_ga4_mcp/server.py#L228-L322).

## ga4_check_compatibility

Builds requested fields and filters, maps compatibility_filter case-insensitively to the API enum and returns compatibility response. Serializes protobufs to snake_case dictionaries; the shared registration wrapper returns a JSON string envelope with status, result, target, completeness/quality proof and recovery guidance, and redacts errors before raising RuntimeError.

<details>
<summary>Full registered description</summary>

```text
Validate whether a dim/metric combo can be queried together. Cheap pre-flight.

compatibility_filter: 'COMPATIBLE' (default, returns only fields that work
with the provided selection) or 'INCOMPATIBLE' (returns only fields that
would conflict).

Use before run_report when composing exploratory queries, cheaper than
catching a GoogleAdsException after a big failed report.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |
| `dimensions` | No | array of string or null | null |
| `metrics` | No | array of string or null | null |
| `dimension_filter` | No | object or null | null |
| `metric_filter` | No | object or null | null |
| `compatibility_filter` | No | string | "COMPATIBLE" |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "property_id": {
      "type": "string",
      "title": "Property Id"
    },
    "dimensions": {
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
      "title": "Dimensions",
      "default": null
    },
    "metrics": {
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
      "title": "Metrics",
      "default": null
    },
    "dimension_filter": {
      "anyOf": [
        {
          "type": "object",
          "additionalProperties": true
        },
        {
          "type": "null"
        }
      ],
      "title": "Dimension Filter",
      "default": null
    },
    "metric_filter": {
      "anyOf": [
        {
          "type": "object",
          "additionalProperties": true
        },
        {
          "type": "null"
        }
      ],
      "title": "Metric Filter",
      "default": null
    },
    "compatibility_filter": {
      "type": "string",
      "title": "Compatibility Filter",
      "default": "COMPATIBLE"
    }
  },
  "required": [
    "property_id"
  ],
  "title": "ga4_check_compatibilityArguments"
}
```

</details>

- Handler requires numeric property_id or properties/NNN; this restriction is not an input-schema pattern.
- Dictionary arguments intentionally expose arbitrary keys/values according to annotations; documented GA shapes and API protobuf validation are not nested input-schema constraints.
- Handler accepts COMPATIBILITY_UNSPECIFIED, COMPATIBLE or INCOMPATIBLE case-insensitively; input schema is a plain string.

Source: [src/scalably_ga4_mcp/server.py:807](https://github.com/scalably-io/ga4-mcp/blob/90b8c28b4e62844fe1f1b765e3b95ce08367285b/src/scalably_ga4_mcp/server.py#L807-L847) · [src/scalably_ga4_mcp/server.py:77](https://github.com/scalably-io/ga4-mcp/blob/90b8c28b4e62844fe1f1b765e3b95ce08367285b/src/scalably_ga4_mcp/server.py#L77-L116) · [src/scalably_ga4_mcp/server.py:228](https://github.com/scalably-io/ga4-mcp/blob/90b8c28b4e62844fe1f1b765e3b95ce08367285b/src/scalably_ga4_mcp/server.py#L228-L322).

## ga4_run_funnel_report

Builds date ranges/filter and forwards loose funnel, funnel_breakdown and funnel_next_action dictionaries into protobuf constructors; rejects over ten steps, caps limit at 250000 and uses caller quota flag. Serializes protobufs to snake_case dictionaries; the shared registration wrapper returns a JSON string envelope with status, result, target, completeness/quality proof and recovery guidance, and redacts errors before raising RuntimeError.

<details>
<summary>Full registered description</summary>

```text
Run a GA4 funnel report. v1alpha, API surface may change.

funnel: {
  is_open_funnel: bool,
  steps: [
    {
      name: str,
      is_directly_followed_by: bool,
      filter_expression: FunnelFilterExpression,
      within_duration_from_prior_step: {seconds: int},
    }, ...
  ]
}
funnel_breakdown: {dimension_name, limit}, optional per-step breakdown.
funnel_next_action: {dimension_name, limit}, optional "what came after".

Use for drop-off analysis across a sequence of events. Behind an alpha flag
because Google can change the shape, check the Feb 2026 release notes if
this fails with a validation error.

Ref: https://developers.google.com/analytics/devguides/reporting/data/v1/rest/v1alpha/properties/runFunnelReport
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |
| `funnel` | Yes | object | Not declared |
| `date_ranges` | No | array of object or null | null |
| `dimension_filter` | No | object or null | null |
| `funnel_breakdown` | No | object or null | null |
| `funnel_next_action` | No | object or null | null |
| `limit` | No | integer | 10000 |
| `return_property_quota` | No | boolean | true |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "property_id": {
      "type": "string",
      "title": "Property Id"
    },
    "funnel": {
      "type": "object",
      "additionalProperties": true,
      "title": "Funnel"
    },
    "date_ranges": {
      "anyOf": [
        {
          "type": "array",
          "items": {
            "type": "object",
            "additionalProperties": {
              "type": "string"
            }
          }
        },
        {
          "type": "null"
        }
      ],
      "title": "Date Ranges",
      "default": null
    },
    "dimension_filter": {
      "anyOf": [
        {
          "type": "object",
          "additionalProperties": true
        },
        {
          "type": "null"
        }
      ],
      "title": "Dimension Filter",
      "default": null
    },
    "funnel_breakdown": {
      "anyOf": [
        {
          "type": "object",
          "additionalProperties": true
        },
        {
          "type": "null"
        }
      ],
      "title": "Funnel Breakdown",
      "default": null
    },
    "funnel_next_action": {
      "anyOf": [
        {
          "type": "object",
          "additionalProperties": true
        },
        {
          "type": "null"
        }
      ],
      "title": "Funnel Next Action",
      "default": null
    },
    "limit": {
      "type": "integer",
      "title": "Limit",
      "default": 10000
    },
    "return_property_quota": {
      "type": "boolean",
      "title": "Return Property Quota",
      "default": true
    }
  },
  "required": [
    "property_id",
    "funnel"
  ],
  "title": "ga4_run_funnel_reportArguments"
}
```

</details>

- Handler requires numeric property_id or properties/NNN; this restriction is not an input-schema pattern.
- Dictionary arguments intentionally expose arbitrary keys/values according to annotations; documented GA shapes and API protobuf validation are not nested input-schema constraints.
- Unconditionally registered despite docstring claiming an alpha flag; no feature gate exists.
- Row limits are capped in handler without schema minimum/maximum; negative values are not rejected locally.

Source: [src/scalably_ga4_mcp/server.py:850](https://github.com/scalably-io/ga4-mcp/blob/90b8c28b4e62844fe1f1b765e3b95ce08367285b/src/scalably_ga4_mcp/server.py#L850-L906) · [src/scalably_ga4_mcp/server.py:77](https://github.com/scalably-io/ga4-mcp/blob/90b8c28b4e62844fe1f1b765e3b95ce08367285b/src/scalably_ga4_mcp/server.py#L77-L116) · [src/scalably_ga4_mcp/server.py:228](https://github.com/scalably-io/ga4-mcp/blob/90b8c28b4e62844fe1f1b765e3b95ce08367285b/src/scalably_ga4_mcp/server.py#L228-L322).

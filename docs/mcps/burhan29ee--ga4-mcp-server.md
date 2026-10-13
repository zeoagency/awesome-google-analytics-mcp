# burhan29ee/ga4-mcp-server

[Catalog](../../README.md) · [All tool names](../tool-index.md) · [Upstream](https://github.com/burhan29ee/ga4-mcp-server) · [JSON](../../data/mcps/burhan29ee--ga4-mcp-server.json)

**19 tools:** 19 GA4, 0 other-service or server-support tools. Reviewed source: [`e8bd5db77475`](https://github.com/burhan29ee/ga4-mcp-server/tree/e8bd5db77475e8b7e5dd312ea3ab91f6ea4355c3).

Descriptions and parameter schemas come from the registered source definitions. Generated schemas are reconstructed from annotations or validators; live `tools/list` and authenticated API calls were not run. Loose objects remain loose.

<details>
<summary>Exposure and compatibility notes</summary>

- Source review only; no tools/list, upstream execution or live requests. Source snapshot has no .git; supplied revision is authoritative.
- All 19 tools are registered unconditionally in one module; no optional tool imports or permission tiers. No Pydantic input models, Field constraints or injected Context parameters. FastMCP derives schemas from plain Python annotations and defaults.
- Service-account credentials and Analytics access are required for Data/Admin calls; credentials are constructed lazily. send_ga4_event instead uses provided Measurement Protocol identifiers and secret.
- Dependencies are version ranges (mcp>=1.2,<2, google-analytics-data>=0.18, google-analytics-admin>=0.22); imported SDK types and clients were inspected statically, not runtime tested.

</details>

## Tools

| Tool | Scope | Effect |
| --- | --- | --- |
| [`list_account_summaries`](#list_account_summaries) | GA4 | read |
| [`get_property_details`](#get_property_details) | GA4 | read |
| [`list_data_streams`](#list_data_streams) | GA4 | read |
| [`run_report`](#run_report) | GA4 | read |
| [`run_realtime_report`](#run_realtime_report) | GA4 | read |
| [`list_custom_dimensions`](#list_custom_dimensions) | GA4 | read |
| [`create_custom_dimension`](#create_custom_dimension) | GA4 | write |
| [`archive_custom_dimension`](#archive_custom_dimension) | GA4 | write |
| [`list_custom_metrics`](#list_custom_metrics) | GA4 | read |
| [`create_custom_metric`](#create_custom_metric) | GA4 | write |
| [`list_key_events`](#list_key_events) | GA4 | read |
| [`create_key_event`](#create_key_event) | GA4 | write |
| [`list_audiences`](#list_audiences) | GA4 | read |
| [`create_event_audience`](#create_event_audience) | GA4 | write |
| [`archive_audience`](#archive_audience) | GA4 | write |
| [`list_measurement_protocol_secrets`](#list_measurement_protocol_secrets) | GA4 | read |
| [`create_measurement_protocol_secret`](#create_measurement_protocol_secret) | GA4 | write |
| [`delete_measurement_protocol_secret`](#delete_measurement_protocol_secret) | GA4 | write |
| [`send_ga4_event`](#send_ga4_event) | GA4 | write |

## list_account_summaries

Iterates Admin API account summaries and returns accounts plus visible property names, IDs and display names.

<details>
<summary>Full registered description</summary>

```text
List every GA4 account and its properties the service account can see.
Returns account name/id plus each property's display name and numeric id.
Call this first to discover property ids for the other tools.
```

</details>

No named input parameters are declared.

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {},
  "title": "list_account_summariesArguments"
}
```

</details>

Source: [src/ga4_mcp_server/server.py:113](https://github.com/burhan29ee/ga4-mcp-server/blob/e8bd5db77475e8b7e5dd312ea3ab91f6ea4355c3/src/ga4_mcp_server/server.py#L113-L134).

## get_property_details

Gets normalized GA4 property resource and returns its configuration, enum industry name and ISO create time.

<details>
<summary>Full registered description</summary>

```text
Get configuration details for one GA4 property (name, time zone,
currency, industry, create time).
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
  "title": "get_property_detailsArguments",
  "required": [
    "property_id"
  ]
}
```

</details>

Source: [src/ga4_mcp_server/server.py:137](https://github.com/burhan29ee/ga4-mcp-server/blob/e8bd5db77475e8b7e5dd312ea3ab91f6ea4355c3/src/ga4_mcp_server/server.py#L137-L149).

## list_data_streams

Lists property data streams and returns resource names, IDs, display names, stream types and web measurement IDs.

<details>
<summary>Full registered description</summary>

```text
List the data streams (web/app) on a GA4 property. The stream id (last
path segment of 'name') is needed by the Measurement Protocol secret tools.
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
  "title": "list_data_streamsArguments",
  "required": [
    "property_id"
  ]
}
```

</details>

Source: [src/ga4_mcp_server/server.py:152](https://github.com/burhan29ee/ga4-mcp-server/blob/e8bd5db77475e8b7e5dd312ea3ab91f6ea4355c3/src/ga4_mcp_server/server.py#L152-L167).

## run_report

Constructs a Data API RunReportRequest from metrics, dimensions, one date range and limit; returns headers, total row count and rows of string values.

<details>
<summary>Full registered description</summary>

```text
Run a GA4 report. metrics/dimensions are GA4 API names (e.g. metrics
['activeUsers','conversions'], dimensions ['date','sessionDefaultChannelGroup']).
Dates accept YYYY-MM-DD or relative forms like '28daysAgo' / 'today'.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |
| `metrics` | Yes | array of string | Not declared |
| `dimensions` | No | array of string or null | null |
| `start_date` | No | string | "28daysAgo" |
| `end_date` | No | string | "today" |
| `limit` | No | integer | 100 |

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
    "metrics": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "title": "Metrics"
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
    "start_date": {
      "type": "string",
      "title": "Start Date",
      "default": "28daysAgo"
    },
    "end_date": {
      "type": "string",
      "title": "End Date",
      "default": "today"
    },
    "limit": {
      "type": "integer",
      "title": "Limit",
      "default": 100
    }
  },
  "title": "run_reportArguments",
  "required": [
    "property_id",
    "metrics"
  ]
}
```

</details>

Source: [src/ga4_mcp_server/server.py:174](https://github.com/burhan29ee/ga4-mcp-server/blob/e8bd5db77475e8b7e5dd312ea3ab91f6ea4355c3/src/ga4_mcp_server/server.py#L174-L208).

## run_realtime_report

Constructs RunRealtimeReportRequest from metrics, dimensions and limit; returns headers and rows of string values.

<details>
<summary>Full registered description</summary>

```text
Run a GA4 realtime report (last ~30 minutes). Example: metrics
['activeUsers'], dimensions ['country','unifiedScreenName'].
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |
| `metrics` | Yes | array of string | Not declared |
| `dimensions` | No | array of string or null | null |
| `limit` | No | integer | 100 |

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
    "metrics": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "title": "Metrics"
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
    "limit": {
      "type": "integer",
      "title": "Limit",
      "default": 100
    }
  },
  "title": "run_realtime_reportArguments",
  "required": [
    "property_id",
    "metrics"
  ]
}
```

</details>

Source: [src/ga4_mcp_server/server.py:211](https://github.com/burhan29ee/ga4-mcp-server/blob/e8bd5db77475e8b7e5dd312ea3ab91f6ea4355c3/src/ga4_mcp_server/server.py#L211-L236).

## list_custom_dimensions

Lists custom dimension resource names, display names, parameter names, scope enum names and descriptions.

<details>
<summary>Full registered description</summary>

```text
List custom dimensions defined on a GA4 property.
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
  "title": "list_custom_dimensionsArguments",
  "required": [
    "property_id"
  ]
}
```

</details>

Source: [src/ga4_mcp_server/server.py:243](https://github.com/burhan29ee/ga4-mcp-server/blob/e8bd5db77475e8b7e5dd312ea3ab91f6ea4355c3/src/ga4_mcp_server/server.py#L243-L255).

## create_custom_dimension

Constructs CustomDimension using uppercased scope enum lookup, then creates it on the property and returns identifiers and scope.

<details>
<summary>Full registered description</summary>

```text
Create a custom dimension. parameter_name is the event parameter / user
property key; scope is 'EVENT', 'USER' or 'ITEM'. display_name may contain
only letters, numbers, underscores and spaces.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |
| `parameter_name` | Yes | string | Not declared |
| `display_name` | Yes | string | Not declared |
| `scope` | No | string | "EVENT" |
| `description` | No | string | "" |

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
      "title": "Scope",
      "default": "EVENT"
    },
    "description": {
      "type": "string",
      "title": "Description",
      "default": ""
    }
  },
  "title": "create_custom_dimensionArguments",
  "required": [
    "property_id",
    "parameter_name",
    "display_name"
  ]
}
```

</details>

- scope is exposed as an unrestricted string; handler uppercases it and indexes the Google SDK enum. Display-name character restrictions in the docstring are not enforced locally or encoded in the schema.

Source: [src/ga4_mcp_server/server.py:258](https://github.com/burhan29ee/ga4-mcp-server/blob/e8bd5db77475e8b7e5dd312ea3ab91f6ea4355c3/src/ga4_mcp_server/server.py#L258-L281).

## archive_custom_dimension

Resolves a numeric custom dimension ID or supplied resource name and archives the dimension.

<details>
<summary>Full registered description</summary>

```text
Archive (delete) a custom dimension. custom_dimension_id may be the
numeric id or the full 'properties/NNN/customDimensions/MMM' name.
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
      "title": "Property Id"
    },
    "custom_dimension_id": {
      "type": "string",
      "title": "Custom Dimension Id"
    }
  },
  "title": "archive_custom_dimensionArguments",
  "required": [
    "property_id",
    "custom_dimension_id"
  ]
}
```

</details>

Source: [src/ga4_mcp_server/server.py:284](https://github.com/burhan29ee/ga4-mcp-server/blob/e8bd5db77475e8b7e5dd312ea3ab91f6ea4355c3/src/ga4_mcp_server/server.py#L284-L291).

## list_custom_metrics

Lists custom metric names, display names, parameters, measurement units, scopes and descriptions.

<details>
<summary>Full registered description</summary>

```text
List custom metrics defined on a GA4 property.
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
  "title": "list_custom_metricsArguments",
  "required": [
    "property_id"
  ]
}
```

</details>

Source: [src/ga4_mcp_server/server.py:298](https://github.com/burhan29ee/ga4-mcp-server/blob/e8bd5db77475e8b7e5dd312ea3ab91f6ea4355c3/src/ga4_mcp_server/server.py#L298-L311).

## create_custom_metric

Constructs CustomMetric using uppercased measurement unit and scope enum lookups, creates it and returns its identifiers and unit.

<details>
<summary>Full registered description</summary>

```text
Create a custom metric. measurement_unit is one of STANDARD, CURRENCY,
FEET, METERS, KILOMETERS, MILES, MILLISECONDS, SECONDS, MINUTES, HOURS.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |
| `parameter_name` | Yes | string | Not declared |
| `display_name` | Yes | string | Not declared |
| `measurement_unit` | No | string | "STANDARD" |
| `scope` | No | string | "EVENT" |
| `description` | No | string | "" |

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
      "title": "Measurement Unit",
      "default": "STANDARD"
    },
    "scope": {
      "type": "string",
      "title": "Scope",
      "default": "EVENT"
    },
    "description": {
      "type": "string",
      "title": "Description",
      "default": ""
    }
  },
  "title": "create_custom_metricArguments",
  "required": [
    "property_id",
    "parameter_name",
    "display_name"
  ]
}
```

</details>

- measurement_unit and scope are unrestricted strings in the schema; handler uppercases and indexes Google SDK enums.

Source: [src/ga4_mcp_server/server.py:314](https://github.com/burhan29ee/ga4-mcp-server/blob/e8bd5db77475e8b7e5dd312ea3ab91f6ea4355c3/src/ga4_mcp_server/server.py#L314-L338).

## list_key_events

Lists property key events with names, counting methods and deletable/custom flags.

<details>
<summary>Full registered description</summary>

```text
List key events (conversions) on a GA4 property.
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
  "title": "list_key_eventsArguments",
  "required": [
    "property_id"
  ]
}
```

</details>

Source: [src/ga4_mcp_server/server.py:345](https://github.com/burhan29ee/ga4-mcp-server/blob/e8bd5db77475e8b7e5dd312ea3ab91f6ea4355c3/src/ga4_mcp_server/server.py#L345-L357).

## create_key_event

Constructs KeyEvent using uppercased counting method enum lookup and creates it on the property.

<details>
<summary>Full registered description</summary>

```text
Mark an event as a key event (conversion). counting_method is
'ONCE_PER_EVENT' or 'ONCE_PER_SESSION'.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |
| `event_name` | Yes | string | Not declared |
| `counting_method` | No | string | "ONCE_PER_EVENT" |

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
    "event_name": {
      "type": "string",
      "title": "Event Name"
    },
    "counting_method": {
      "type": "string",
      "title": "Counting Method",
      "default": "ONCE_PER_EVENT"
    }
  },
  "title": "create_key_eventArguments",
  "required": [
    "property_id",
    "event_name"
  ]
}
```

</details>

- counting_method is an unrestricted string in the schema; handler uppercases and indexes the SDK enum.

Source: [src/ga4_mcp_server/server.py:360](https://github.com/burhan29ee/ga4-mcp-server/blob/e8bd5db77475e8b7e5dd312ea3ab91f6ea4355c3/src/ga4_mcp_server/server.py#L360-L370).

## list_audiences

Lists audiences through Admin API v1alpha and returns names, descriptions and membership durations.

<details>
<summary>Full registered description</summary>

```text
List audiences defined on a GA4 property.
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
  "title": "list_audiencesArguments",
  "required": [
    "property_id"
  ]
}
```

</details>

Source: [src/ga4_mcp_server/server.py:377](https://github.com/burhan29ee/ga4-mcp-server/blob/e8bd5db77475e8b7e5dd312ea3ab91f6ea4355c3/src/ga4_mcp_server/server.py#L377-L388).

## create_event_audience

Creates an audience with one INCLUDE filter for the supplied event, across all sessions, using an and_group containing an or_group and event filter.

<details>
<summary>Full registered description</summary>

```text
Create a GA4 audience of users who triggered a given event (e.g.
'purchase', 'generate_lead') — useful for remarketing lists that can be
shared to Google Ads. membership_duration_days is how long a user stays in
the audience (max 540).
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |
| `display_name` | Yes | string | Not declared |
| `event_name` | Yes | string | Not declared |
| `membership_duration_days` | No | integer | 30 |
| `description` | No | string | "" |

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
    "display_name": {
      "type": "string",
      "title": "Display Name"
    },
    "event_name": {
      "type": "string",
      "title": "Event Name"
    },
    "membership_duration_days": {
      "type": "integer",
      "title": "Membership Duration Days",
      "default": 30
    },
    "description": {
      "type": "string",
      "title": "Description",
      "default": ""
    }
  },
  "title": "create_event_audienceArguments",
  "required": [
    "property_id",
    "display_name",
    "event_name"
  ]
}
```

</details>

- Docstring max membership duration 540 is not enforced locally or encoded as a schema maximum.

Source: [src/ga4_mcp_server/server.py:391](https://github.com/burhan29ee/ga4-mcp-server/blob/e8bd5db77475e8b7e5dd312ea3ab91f6ea4355c3/src/ga4_mcp_server/server.py#L391-L426).

## archive_audience

Resolves numeric audience ID or supplied resource name and calls Admin API v1alpha archive_audience.

<details>
<summary>Full registered description</summary>

```text
Archive a GA4 audience. audience_id may be the numeric id or the full
'properties/NNN/audiences/MMM' name.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |
| `audience_id` | Yes | string | Not declared |

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
    "audience_id": {
      "type": "string",
      "title": "Audience Id"
    }
  },
  "title": "archive_audienceArguments",
  "required": [
    "property_id",
    "audience_id"
  ]
}
```

</details>

Source: [src/ga4_mcp_server/server.py:429](https://github.com/burhan29ee/ga4-mcp-server/blob/e8bd5db77475e8b7e5dd312ea3ab91f6ea4355c3/src/ga4_mcp_server/server.py#L429-L436).

## list_measurement_protocol_secrets

Lists stream Measurement Protocol secrets, including their secret values.

<details>
<summary>Full registered description</summary>

```text
List Measurement Protocol API secrets for a data stream. stream_id is
the numeric id from list_data_streams.
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
  "title": "list_measurement_protocol_secretsArguments",
  "required": [
    "property_id",
    "stream_id"
  ]
}
```

</details>

Source: [src/ga4_mcp_server/server.py:443](https://github.com/burhan29ee/ga4-mcp-server/blob/e8bd5db77475e8b7e5dd312ea3ab91f6ea4355c3/src/ga4_mcp_server/server.py#L443-L451).

## create_measurement_protocol_secret

Creates a named stream Measurement Protocol secret and returns its secret value.

<details>
<summary>Full registered description</summary>

```text
Create a Measurement Protocol API secret on a data stream. Returns the
secret_value (api_secret) needed by send_ga4_event. Treat it as sensitive.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |
| `stream_id` | Yes | string | Not declared |
| `display_name` | Yes | string | Not declared |

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
    "stream_id": {
      "type": "string",
      "title": "Stream Id"
    },
    "display_name": {
      "type": "string",
      "title": "Display Name"
    }
  },
  "title": "create_measurement_protocol_secretArguments",
  "required": [
    "property_id",
    "stream_id",
    "display_name"
  ]
}
```

</details>

Source: [src/ga4_mcp_server/server.py:454](https://github.com/burhan29ee/ga4-mcp-server/blob/e8bd5db77475e8b7e5dd312ea3ab91f6ea4355c3/src/ga4_mcp_server/server.py#L454-L462).

## delete_measurement_protocol_secret

Resolves secret ID or full resource name and deletes the stream Measurement Protocol secret.

<details>
<summary>Full registered description</summary>

```text
Delete a Measurement Protocol API secret. secret_id may be the numeric
id or the full resource name.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |
| `stream_id` | Yes | string | Not declared |
| `secret_id` | Yes | string | Not declared |

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
    "stream_id": {
      "type": "string",
      "title": "Stream Id"
    },
    "secret_id": {
      "type": "string",
      "title": "Secret Id"
    }
  },
  "title": "delete_measurement_protocol_secretArguments",
  "required": [
    "property_id",
    "stream_id",
    "secret_id"
  ]
}
```

</details>

Source: [src/ga4_mcp_server/server.py:465](https://github.com/burhan29ee/ga4-mcp-server/blob/e8bd5db77475e8b7e5dd312ea3ab91f6ea4355c3/src/ga4_mcp_server/server.py#L465-L472).

## send_ga4_event

POSTs one event with arbitrary params and client_id to the Measurement Protocol collect endpoint, or debug endpoint when validate is true. Returns HTTP status and parsed/text response; HTTPError returns status and error text.

<details>
<summary>Full registered description</summary>

```text
Send an event into a GA4 property via the Measurement Protocol.
measurement_id is the stream's 'G-XXXXXXX'; api_secret comes from a
Measurement Protocol secret; client_id identifies the user/device. Set
validate=True to hit GA4's debug/validation endpoint (checks the payload
WITHOUT ingesting it) — recommended before real sends.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `measurement_id` | Yes | string | Not declared |
| `api_secret` | Yes | string | Not declared |
| `client_id` | Yes | string | Not declared |
| `event_name` | Yes | string | Not declared |
| `params` | No | object or null | null |
| `validate` | No | boolean | false |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "measurement_id": {
      "type": "string",
      "title": "Measurement Id"
    },
    "api_secret": {
      "type": "string",
      "title": "Api Secret"
    },
    "client_id": {
      "type": "string",
      "title": "Client Id"
    },
    "event_name": {
      "type": "string",
      "title": "Event Name"
    },
    "params": {
      "anyOf": [
        {
          "type": "object",
          "additionalProperties": true
        },
        {
          "type": "null"
        }
      ],
      "title": "Params",
      "default": null
    },
    "validate": {
      "type": "boolean",
      "title": "Validate",
      "default": false
    }
  },
  "title": "send_ga4_eventArguments",
  "required": [
    "measurement_id",
    "api_secret",
    "client_id",
    "event_name"
  ]
}
```

</details>

- params is a nullable arbitrary dictionary; no event parameter structures are constrained. validate=True performs remote payload validation without ingestion; default False sends an ingestible event. Query parameters are interpolated without URL encoding.

Source: [src/ga4_mcp_server/server.py:475](https://github.com/burhan29ee/ga4-mcp-server/blob/e8bd5db77475e8b7e5dd312ea3ab91f6ea4355c3/src/ga4_mcp_server/server.py#L475-L507).

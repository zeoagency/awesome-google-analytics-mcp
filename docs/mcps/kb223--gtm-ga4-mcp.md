# kb223/gtm-ga4-mcp

[Catalog](../../README.md) · [All tool names](../tool-index.md) · [Upstream](https://github.com/kb223/gtm-ga4-mcp) · [JSON](../../data/mcps/kb223--gtm-ga4-mcp.json)

**16 tools:** 9 GA4, 7 other-service or server-support tools. Reviewed source: [`40862b6e92d0`](https://github.com/kb223/gtm-ga4-mcp/tree/40862b6e92d0b70e04b543a6f7ec854258e392cd).

Descriptions and parameter schemas come from the registered source definitions. Generated schemas are reconstructed from annotations or validators; live `tools/list` and authenticated API calls were not run. Loose objects remain loose.

<details>
<summary>Exposure and compatibility notes</summary>

- Source review only; no upstream execution, tools/list or live requests. HEAD matches supplied revision.
- Inventory is full union of 16 tools: READ 8, WRITE 4, DESTRUCTIVE 4. Default advertises READ only (8); --allow-write or GTM_GA4_MCP_ALLOW_WRITE enables READ+WRITE (12); --allow-destructive or GTM_GA4_MCP_ALLOW_DESTRUCTIVE enables all (16). --deny TOOL and comma-separated GTM_GA4_MCP_DENY remove named tools at registration.
- OAuth scopes are cumulative by tier and configured before registration; denylist does not reduce scopes. ADC clients are created lazily and cached per thread. No OAuth, GCP setup, auth, diagnostic, or support function is registered as a tool.
- pyproject.toml uses mcp>=2,<3 and imports mcp.server.mcpserver.MCPServer (current v2 API); do not infer a v1 FastMCP import defect. Dependencies are not authenticated/runtime tested.

</details>

## Tools

| Tool | Scope | Effect |
| --- | --- | --- |
| [`ga4_account_summaries`](#ga4_account_summaries) | GA4 | read |
| [`ga4_admin_create`](#ga4_admin_create) | GA4 | write |
| [`ga4_admin_delete`](#ga4_admin_delete) | GA4 | write |
| [`ga4_admin_list`](#ga4_admin_list) | GA4 | read |
| [`ga4_admin_update`](#ga4_admin_update) | GA4 | write |
| [`ga4_metadata`](#ga4_metadata) | GA4 | read |
| [`ga4_property_get`](#ga4_property_get) | GA4 | read |
| [`ga4_run_realtime_report`](#ga4_run_realtime_report) | GA4 | read |
| [`ga4_run_report`](#ga4_run_report) | GA4 | read |
| [`gtm_create`](#gtm_create) | Other service | write |
| [`gtm_delete`](#gtm_delete) | Other service | write |
| [`gtm_get`](#gtm_get) | Other service | read |
| [`gtm_list`](#gtm_list) | Other service | read |
| [`gtm_permissions`](#gtm_permissions) | Other service | write |
| [`gtm_publish`](#gtm_publish) | Other service | write |
| [`gtm_update`](#gtm_update) | Other service | write |

## ga4_account_summaries

Lists account summaries with pageSize 200 and optional page token; returns trimmed accounts and property summaries.

<details>
<summary>Full registered description</summary>

```text
List every GA4 account and property the authenticated user can access.

This is the entry point for all GA4 work — it returns the property IDs the
other ga4_* tools need.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `page_token` | No | string or null | null |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "properties": {
    "page_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Pagination token from a previous response.",
      "title": "Page Token"
    }
  },
  "type": "object",
  "required": []
}
```

</details>

Source: [src/gtm_ga4_mcp/tools/ga4_admin.py:49](https://github.com/kb223/gtm-ga4-mcp/blob/40862b6e92d0b70e04b543a6f7ec854258e392cd/src/gtm_ga4_mcp/tools/ga4_admin.py#L49-L83) · [src/gtm_ga4_mcp/tools/ga4_admin.py:133](https://github.com/kb223/gtm-ga4-mcp/blob/40862b6e92d0b70e04b543a6f7ec854258e392cd/src/gtm_ga4_mcp/tools/ga4_admin.py#L133-L138).

## ga4_admin_create

Returns the request locally when dry_run is true; otherwise creates the selected property sub-entity using the arbitrary JSON body.

<details>
<summary>Full registered description</summary>

```text
Create a GA4 custom dimension, custom metric, key event, or data stream on a property.

Defaults to dry-run: nothing is sent until called with dry_run=False.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `entity_type` | Yes | Ga4WriteEntityType | Not declared |
| `property_id` | Yes | string | Not declared |
| `body` | Yes | object | Not declared |
| `dry_run` | No | boolean | true |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "$defs": {
    "Ga4WriteEntityType": {
      "enum": [
        "custom_dimensions",
        "custom_metrics",
        "key_events",
        "data_streams",
        "property"
      ],
      "title": "Ga4WriteEntityType",
      "type": "string"
    }
  },
  "properties": {
    "entity_type": {
      "$ref": "#/$defs/Ga4WriteEntityType",
      "description": "What to create: custom_dimensions, custom_metrics, key_events, or data_streams."
    },
    "property_id": {
      "description": "GA4 property ID, e.g. '123456' or 'properties/123456'.",
      "title": "Property Id",
      "type": "string"
    },
    "body": {
      "additionalProperties": true,
      "description": "Entity JSON per the Admin API, e.g. a custom dimension: {'parameterName': 'lead_type', 'displayName': 'Lead Type', 'scope': 'EVENT'}.",
      "title": "Body",
      "type": "object"
    },
    "dry_run": {
      "default": true,
      "description": "True (default) echoes the request without sending it.",
      "title": "Dry Run",
      "type": "boolean"
    }
  },
  "required": [
    "entity_type",
    "property_id",
    "body"
  ],
  "type": "object"
}
```

</details>

- Schema enum also accepts property, but handler rejects creating properties.
- Requires write/destructive tier; dry_run defaults true. Arbitrary dict bodies expose additionalProperties=true, not an API-specific body model.

Source: [src/gtm_ga4_mcp/tools/ga4_write.py:41](https://github.com/kb223/gtm-ga4-mcp/blob/40862b6e92d0b70e04b543a6f7ec854258e392cd/src/gtm_ga4_mcp/tools/ga4_write.py#L41-L83) · [src/gtm_ga4_mcp/tools/ga4_write.py:145](https://github.com/kb223/gtm-ga4-mcp/blob/40862b6e92d0b70e04b543a6f7ec854258e392cd/src/gtm_ga4_mcp/tools/ga4_write.py#L145-L145).

## ga4_admin_delete

First call issues an operation-bound confirmation token. Redeeming it archives a custom dimension/metric or deletes a key event/data stream.

<details>
<summary>Full registered description</summary>

```text
Delete or archive a GA4 entity by resource name. Two-phase.

Custom dimensions/metrics are ARCHIVED (permanent — GA4 has no unarchive
or true delete for them); key events and data streams are DELETED.
Deleting a data stream stops collection for it. Properties cannot be
deleted through this tool by design.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `name` | Yes | string | Not declared |
| `confirm_token` | No | string or null | null |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "properties": {
    "name": {
      "description": "Full resource name from a read tool, e.g. 'properties/123/customDimensions/456' or 'properties/123/dataStreams/789'.",
      "minLength": 1,
      "title": "Name",
      "type": "string"
    },
    "confirm_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Omit on the first call — it returns a token and a summary instead of deleting. Pass the token back (same name) to execute.",
      "title": "Confirm Token"
    }
  },
  "required": [
    "name"
  ],
  "type": "object"
}
```

</details>

- Only four-segment properties/{id}/{collection}/{id} names accepted; collection must be customDimensions, customMetrics, keyEvents or dataStreams. Return key for archive is archived; delete produces deleted.
- Requires destructive tier. Confirmation tokens are in-memory, single-use, expire after 600 seconds and bind to exact operation arguments; consumed before API execution.

Source: [src/gtm_ga4_mcp/tools/ga4_destructive.py:27](https://github.com/kb223/gtm-ga4-mcp/blob/40862b6e92d0b70e04b543a6f7ec854258e392cd/src/gtm_ga4_mcp/tools/ga4_destructive.py#L27-L91) · [src/gtm_ga4_mcp/tools/ga4_destructive.py:95](https://github.com/kb223/gtm-ga4-mcp/blob/40862b6e92d0b70e04b543a6f7ec854258e392cd/src/gtm_ga4_mcp/tools/ga4_destructive.py#L95-L100).

## ga4_admin_list

Dispatches entity type to property resource list and returns items with pagination token.

<details>
<summary>Full registered description</summary>

```text
List a GA4 property's sub-entities.

Covers data streams, key events, custom dimensions/metrics, Google Ads
links, and Firebase links.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `entity_type` | Yes | Ga4AdminEntityType | Not declared |
| `property_id` | Yes | string | Not declared |
| `page_token` | No | string or null | null |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "$defs": {
    "Ga4AdminEntityType": {
      "enum": [
        "data_streams",
        "key_events",
        "custom_dimensions",
        "custom_metrics",
        "google_ads_links",
        "firebase_links"
      ],
      "title": "Ga4AdminEntityType",
      "type": "string"
    }
  },
  "properties": {
    "entity_type": {
      "$ref": "#/$defs/Ga4AdminEntityType",
      "description": "Which property sub-entity to list."
    },
    "property_id": {
      "description": "GA4 property ID, e.g. '123456' or 'properties/123456'.",
      "title": "Property Id",
      "type": "string"
    },
    "page_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Pagination token from a previous response.",
      "title": "Page Token"
    }
  },
  "required": [
    "entity_type",
    "property_id"
  ],
  "type": "object"
}
```

</details>

Source: [src/gtm_ga4_mcp/tools/ga4_admin.py:97](https://github.com/kb223/gtm-ga4-mcp/blob/40862b6e92d0b70e04b543a6f7ec854258e392cd/src/gtm_ga4_mcp/tools/ga4_admin.py#L97-L129) · [src/gtm_ga4_mcp/tools/ga4_admin.py:140](https://github.com/kb223/gtm-ga4-mcp/blob/40862b6e92d0b70e04b543a6f7ec854258e392cd/src/gtm_ga4_mcp/tools/ga4_admin.py#L140-L140).

## ga4_admin_update

Returns the request locally when dry_run is true; otherwise patches the selected resource with the arbitrary JSON body and updateMask.

<details>
<summary>Full registered description</summary>

```text
Update a GA4 entity (or the property itself) by resource name. Defaults to dry-run.

Unlike GTM, GA4 updates are partial: only fields named in update_mask change.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `entity_type` | Yes | Ga4WriteEntityType | Not declared |
| `name` | Yes | string | Not declared |
| `body` | Yes | object | Not declared |
| `update_mask` | Yes | string | Not declared |
| `dry_run` | No | boolean | true |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "$defs": {
    "Ga4WriteEntityType": {
      "enum": [
        "custom_dimensions",
        "custom_metrics",
        "key_events",
        "data_streams",
        "property"
      ],
      "title": "Ga4WriteEntityType",
      "type": "string"
    }
  },
  "properties": {
    "entity_type": {
      "$ref": "#/$defs/Ga4WriteEntityType",
      "description": "What to update, including 'property' for the property itself."
    },
    "name": {
      "description": "Full resource name from a read tool, e.g. 'properties/123/customDimensions/456' or 'properties/123' for the property.",
      "minLength": 1,
      "title": "Name",
      "type": "string"
    },
    "body": {
      "additionalProperties": true,
      "description": "Fields to change, e.g. {'displayName': 'New name'}.",
      "title": "Body",
      "type": "object"
    },
    "update_mask": {
      "description": "Comma-separated field names being updated (e.g. 'displayName,description'), or '*' to update every field present in body.",
      "minLength": 1,
      "title": "Update Mask",
      "type": "string"
    },
    "dry_run": {
      "default": true,
      "description": "True (default) echoes the request without sending it.",
      "title": "Dry Run",
      "type": "boolean"
    }
  },
  "required": [
    "entity_type",
    "name",
    "body",
    "update_mask"
  ],
  "type": "object"
}
```

</details>

- Resource name must start with properties/; validation does not verify selected entity type matches the name.
- Requires write/destructive tier; dry_run defaults true. Arbitrary dict bodies expose additionalProperties=true, not an API-specific body model.

Source: [src/gtm_ga4_mcp/tools/ga4_write.py:86](https://github.com/kb223/gtm-ga4-mcp/blob/40862b6e92d0b70e04b543a6f7ec854258e392cd/src/gtm_ga4_mcp/tools/ga4_write.py#L86-L141) · [src/gtm_ga4_mcp/tools/ga4_write.py:146](https://github.com/kb223/gtm-ga4-mcp/blob/40862b6e92d0b70e04b543a6f7ec854258e392cd/src/gtm_ga4_mcp/tools/ga4_write.py#L146-L146).

## ga4_metadata

Fetches property metadata, trims dimensions/metrics to API name, UI name and custom flag, optionally filters case-insensitively.

<details>
<summary>Full registered description</summary>

```text
List the dimension/metric API names available on a property (standard + custom).

Use this before ga4_run_report to find exact API names.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |
| `search` | No | string or null | null |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "properties": {
    "property_id": {
      "description": "GA4 property ID, e.g. '123456' or 'properties/123456'.",
      "title": "Property Id",
      "type": "string"
    },
    "search": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional case-insensitive filter on API/UI names, e.g. 'revenue'.",
      "title": "Search"
    }
  },
  "required": [
    "property_id"
  ],
  "type": "object"
}
```

</details>

Source: [src/gtm_ga4_mcp/tools/ga4_data.py:120](https://github.com/kb223/gtm-ga4-mcp/blob/40862b6e92d0b70e04b543a6f7ec854258e392cd/src/gtm_ga4_mcp/tools/ga4_data.py#L120-L166) · [src/gtm_ga4_mcp/tools/ga4_data.py:177](https://github.com/kb223/gtm-ga4-mcp/blob/40862b6e92d0b70e04b543a6f7ec854258e392cd/src/gtm_ga4_mcp/tools/ga4_data.py#L177-L177).

## ga4_property_get

Normalizes numeric property ID and fetches full property configuration.

<details>
<summary>Full registered description</summary>

```text
Fetch one GA4 property's full configuration (timezone, currency, industry, service level).
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "properties": {
    "property_id": {
      "description": "GA4 property ID, e.g. '123456' or 'properties/123456'.",
      "title": "Property Id",
      "type": "string"
    }
  },
  "required": [
    "property_id"
  ],
  "type": "object"
}
```

</details>

Source: [src/gtm_ga4_mcp/tools/ga4_admin.py:86](https://github.com/kb223/gtm-ga4-mcp/blob/40862b6e92d0b70e04b543a6f7ec854258e392cd/src/gtm_ga4_mcp/tools/ga4_admin.py#L86-L94) · [src/gtm_ga4_mcp/tools/ga4_admin.py:139](https://github.com/kb223/gtm-ga4-mcp/blob/40862b6e92d0b70e04b543a6f7ec854258e392cd/src/gtm_ga4_mcp/tools/ga4_admin.py#L139-L139).

## ga4_run_realtime_report

Builds a realtime report; normalizes property ID, executes runRealtimeReport and reshapes response rows.

<details>
<summary>Full registered description</summary>

```text
Run a GA4 realtime report (last 30 minutes) — e.g. to verify events are firing now.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |
| `metrics` | Yes | array of string | Not declared |
| `dimensions` | No | array of string or null | null |
| `limit` | No | integer | 50 |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "properties": {
    "property_id": {
      "description": "GA4 property ID, e.g. '123456' or 'properties/123456'.",
      "title": "Property Id",
      "type": "string"
    },
    "metrics": {
      "description": "Realtime metric API names, e.g. ['activeUsers', 'eventCount'].",
      "items": {
        "type": "string"
      },
      "minItems": 1,
      "title": "Metrics",
      "type": "array"
    },
    "dimensions": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Realtime dimension API names, e.g. ['eventName', 'country'].",
      "title": "Dimensions"
    },
    "limit": {
      "default": 50,
      "description": "Maximum rows to return.",
      "maximum": 250,
      "minimum": 1,
      "title": "Limit",
      "type": "integer"
    }
  },
  "required": [
    "property_id",
    "metrics"
  ],
  "type": "object"
}
```

</details>

Source: [src/gtm_ga4_mcp/tools/ga4_data.py:85](https://github.com/kb223/gtm-ga4-mcp/blob/40862b6e92d0b70e04b543a6f7ec854258e392cd/src/gtm_ga4_mcp/tools/ga4_data.py#L85-L117) · [src/gtm_ga4_mcp/tools/ga4_data.py:171](https://github.com/kb223/gtm-ga4-mcp/blob/40862b6e92d0b70e04b543a6f7ec854258e392cd/src/gtm_ga4_mcp/tools/ga4_data.py#L171-L176).

## ga4_run_report

Builds a date-range report from metric/dimension names; normalizes property ID, executes runReport, reshapes parallel arrays into rows and returns rowCount.

<details>
<summary>Full registered description</summary>

```text
Run a GA4 report over a date range and return one dict per row.

Rows are keyed by the requested dimension/metric API names. `row_count` is
the total available on the server; raise `limit` or refine dimensions if
rows were truncated.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |
| `metrics` | Yes | array of string | Not declared |
| `dimensions` | No | array of string or null | null |
| `start_date` | No | string | "28daysAgo" |
| `end_date` | No | string | "today" |
| `limit` | No | integer | 50 |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "properties": {
    "property_id": {
      "description": "GA4 property ID, e.g. '123456' or 'properties/123456'.",
      "title": "Property Id",
      "type": "string"
    },
    "metrics": {
      "description": "Metric API names, e.g. ['sessions', 'conversions', 'totalRevenue']. Discover names via ga4_metadata.",
      "items": {
        "type": "string"
      },
      "minItems": 1,
      "title": "Metrics",
      "type": "array"
    },
    "dimensions": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Dimension API names, e.g. ['date', 'sessionDefaultChannelGroup'].",
      "title": "Dimensions"
    },
    "start_date": {
      "default": "28daysAgo",
      "description": "Start date: 'YYYY-MM-DD', 'NdaysAgo', 'yesterday', or 'today'.",
      "title": "Start Date",
      "type": "string"
    },
    "end_date": {
      "default": "today",
      "description": "End date: 'YYYY-MM-DD', 'NdaysAgo', 'yesterday', or 'today'.",
      "title": "End Date",
      "type": "string"
    },
    "limit": {
      "default": 50,
      "description": "Maximum rows to return.",
      "maximum": 250,
      "minimum": 1,
      "title": "Limit",
      "type": "integer"
    }
  },
  "required": [
    "property_id",
    "metrics"
  ],
  "type": "object"
}
```

</details>

Source: [src/gtm_ga4_mcp/tools/ga4_data.py:33](https://github.com/kb223/gtm-ga4-mcp/blob/40862b6e92d0b70e04b543a6f7ec854258e392cd/src/gtm_ga4_mcp/tools/ga4_data.py#L33-L82) · [src/gtm_ga4_mcp/tools/ga4_data.py:170](https://github.com/kb223/gtm-ga4-mcp/blob/40862b6e92d0b70e04b543a6f7ec854258e392cd/src/gtm_ga4_mcp/tools/ga4_data.py#L170-L170).

## gtm_create

Validates writable entity type and parent segment count. Dry-run echoes request; otherwise forwards arbitrary JSON to resource create.

<details>
<summary>Full registered description</summary>

```text
Create a GTM entity in a workspace (or a new workspace/environment in a container).

Defaults to dry-run: nothing is sent until called with dry_run=False.
Changes land in the workspace only — nothing goes live without gtm_publish.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `entity_type` | Yes | GtmEntityType | Not declared |
| `parent` | Yes | string | Not declared |
| `body` | Yes | object | Not declared |
| `dry_run` | No | boolean | true |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "$defs": {
    "GtmEntityType": {
      "enum": [
        "accounts",
        "user_permissions",
        "containers",
        "destinations",
        "environments",
        "versions",
        "workspaces",
        "built_in_variables",
        "clients",
        "folders",
        "tags",
        "templates",
        "transformations",
        "triggers",
        "variables",
        "zones"
      ],
      "title": "GtmEntityType",
      "type": "string"
    }
  },
  "properties": {
    "entity_type": {
      "$ref": "#/$defs/GtmEntityType",
      "description": "Entity to create: tags, triggers, variables, workspaces, ..."
    },
    "parent": {
      "description": "Parent path: a container path for workspaces/environments, a workspace path for tags/triggers/variables/etc.",
      "minLength": 1,
      "title": "Parent",
      "type": "string"
    },
    "body": {
      "additionalProperties": true,
      "description": "Entity JSON per the GTM API, e.g. a tag: {'name': ..., 'type': 'gaawe', 'parameter': [...], 'firingTriggerId': [...]}. Read a similar existing entity with gtm_get to see the expected shape.",
      "title": "Body",
      "type": "object"
    },
    "dry_run": {
      "default": true,
      "description": "True (default) echoes the request without sending it.",
      "title": "Dry Run",
      "type": "boolean"
    }
  },
  "required": [
    "entity_type",
    "parent",
    "body"
  ],
  "type": "object"
}
```

</details>

- Enum includes read-only entities; handler restricts to workspaces, environments, tags, triggers, variables, folders, templates, clients, transformations, zones. Parent path validation checks segment count only.
- Requires write/destructive tier; dry_run defaults true. Arbitrary dict bodies expose additionalProperties=true, not an API-specific body model.

Source: [src/gtm_ga4_mcp/tools/gtm_write.py:54](https://github.com/kb223/gtm-ga4-mcp/blob/40862b6e92d0b70e04b543a6f7ec854258e392cd/src/gtm_ga4_mcp/tools/gtm_write.py#L54-L105) · [src/gtm_ga4_mcp/tools/gtm_write.py:172](https://github.com/kb223/gtm-ga4-mcp/blob/40862b6e92d0b70e04b543a6f7ec854258e392cd/src/gtm_ga4_mcp/tools/gtm_write.py#L172-L172).

## gtm_delete

Validates deletable collection; first call issues a confirmation token, second matching call deletes the entity.

<details>
<summary>Full registered description</summary>

```text
Delete a GTM entity (tag, trigger, variable, workspace, version, ...). Two-phase.

Without confirm_token nothing is deleted; you get a summary + token to
confirm with. Deleting a workspace discards its unpublished changes.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `path` | Yes | string | Not declared |
| `confirm_token` | No | string or null | null |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "properties": {
    "path": {
      "description": "Full path of the entity to delete, from gtm_list/gtm_get.",
      "minLength": 1,
      "title": "Path",
      "type": "string"
    },
    "confirm_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Omit on the first call — it returns a token and a summary instead of deleting. Pass the token back (same path) to execute.",
      "title": "Confirm Token"
    }
  },
  "required": [
    "path"
  ],
  "type": "object"
}
```

</details>

- Only workspaces, environments, tags, triggers, variables, folders, templates, clients, transformations, zones, versions collections may be deleted; accounts and containers excluded.
- Requires destructive tier. Confirmation tokens are in-memory, single-use, expire after 600 seconds and bind to exact operation arguments; consumed before API execution.

Source: [src/gtm_ga4_mcp/tools/gtm_destructive.py:46](https://github.com/kb223/gtm-ga4-mcp/blob/40862b6e92d0b70e04b543a6f7ec854258e392cd/src/gtm_ga4_mcp/tools/gtm_destructive.py#L46-L93) · [src/gtm_ga4_mcp/tools/gtm_destructive.py:243](https://github.com/kb223/gtm-ga4-mcp/blob/40862b6e92d0b70e04b543a6f7ec854258e392cd/src/gtm_ga4_mcp/tools/gtm_destructive.py#L243-L243).

## gtm_get

Validates alternating path segments, dispatches final collection to its discovery resource and gets full JSON.

<details>
<summary>Full registered description</summary>

```text
Fetch one GTM entity's complete JSON by its path (tag, trigger, variable, version, ...).

Note: fetching a version returns the entire published container (large).
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `path` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "properties": {
    "path": {
      "description": "Full GTM entity path from a gtm_list result, e.g. 'accounts/123/containers/456/workspaces/7/tags/8' or 'accounts/123/containers/456/versions/42'.",
      "minLength": 1,
      "title": "Path",
      "type": "string"
    }
  },
  "required": [
    "path"
  ],
  "type": "object"
}
```

</details>

- Handler checks even segment count and known final collection; schema only enforces nonempty string. Built-in-variable paths are dispatched to get without a special endpoint check.

Source: [src/gtm_ga4_mcp/tools/gtm.py:214](https://github.com/kb223/gtm-ga4-mcp/blob/40862b6e92d0b70e04b543a6f7ec854258e392cd/src/gtm_ga4_mcp/tools/gtm.py#L214-L244) · [src/gtm_ga4_mcp/tools/gtm.py:249](https://github.com/kb223/gtm-ga4-mcp/blob/40862b6e92d0b70e04b543a6f7ec854258e392cd/src/gtm_ga4_mcp/tools/gtm.py#L249-L249).

## gtm_list

Dispatches an entity type to a GTM resource list, validates parent segment count, returns full JSON or trimmed summaries and pagination token.

<details>
<summary>Full registered description</summary>

```text
List Google Tag Manager entities one hierarchy level at a time.

Returns trimmed summaries (path, name, type, IDs) to keep context small;
each item's `path` feeds gtm_get (full detail) or a deeper gtm_list call.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `entity_type` | Yes | GtmEntityType | Not declared |
| `parent` | No | string | "" |
| `page_token` | No | string or null | null |
| `full` | No | boolean | false |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "$defs": {
    "GtmEntityType": {
      "enum": [
        "accounts",
        "user_permissions",
        "containers",
        "destinations",
        "environments",
        "versions",
        "workspaces",
        "built_in_variables",
        "clients",
        "folders",
        "tags",
        "templates",
        "transformations",
        "triggers",
        "variables",
        "zones"
      ],
      "title": "GtmEntityType",
      "type": "string"
    }
  },
  "properties": {
    "entity_type": {
      "$ref": "#/$defs/GtmEntityType",
      "description": "Which GTM entity to list. Walk the hierarchy: accounts -> containers -> workspaces -> tags/triggers/variables/..."
    },
    "parent": {
      "default": "",
      "description": "Parent path from a previous result, e.g. '' for accounts, 'accounts/123' for containers, 'accounts/123/containers/456' for workspaces/versions/environments, 'accounts/123/containers/456/workspaces/7' for tags/triggers/variables.",
      "title": "Parent",
      "type": "string"
    },
    "page_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Pagination token from a previous response.",
      "title": "Page Token"
    },
    "full": {
      "default": false,
      "description": "Return complete entity JSON instead of trimmed summaries. Prefer gtm_get for a single entity.",
      "title": "Full",
      "type": "boolean"
    }
  },
  "required": [
    "entity_type"
  ],
  "type": "object"
}
```

</details>

- Handler enforces parent segment count by entity, but does not validate collection names in parent path.

Source: [src/gtm_ga4_mcp/tools/gtm.py:152](https://github.com/kb223/gtm-ga4-mcp/blob/40862b6e92d0b70e04b543a6f7ec854258e392cd/src/gtm_ga4_mcp/tools/gtm.py#L152-L211) · [src/gtm_ga4_mcp/tools/gtm.py:248](https://github.com/kb223/gtm-ga4-mcp/blob/40862b6e92d0b70e04b543a6f7ec854258e392cd/src/gtm_ga4_mcp/tools/gtm.py#L248-L248).

## gtm_permissions

Validates action and conditional arguments; issues confirmation token, then creates, updates or deletes an account user permission.

<details>
<summary>Full registered description</summary>

```text
Grant, update, or revoke a user's access to a GTM account. Two-phase.

Access changes are security-sensitive: always show the summary to the
user before confirming.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `action` | Yes | string | Not declared |
| `account_id` | No | string or null | null |
| `path` | No | string or null | null |
| `body` | No | object or null | null |
| `confirm_token` | No | string or null | null |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "properties": {
    "action": {
      "description": "'grant' (new user), 'update' (existing permission), or 'revoke'.",
      "title": "Action",
      "type": "string"
    },
    "account_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "For 'grant': the GTM account ID, e.g. '123456'.",
      "title": "Account Id"
    },
    "path": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "For 'update'/'revoke': the permission path from gtm_list(user_permissions), e.g. 'accounts/123/user_permissions/456'.",
      "title": "Path"
    },
    "body": {
      "anyOf": [
        {
          "additionalProperties": true,
          "type": "object"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "For 'grant'/'update': permission JSON, e.g. {'emailAddress': ..., 'accountAccess': {'permission': 'user'}, 'containerAccess': [{'containerId': ..., 'permission': 'edit'}]}.",
      "title": "Body"
    },
    "confirm_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Omit first to get a summary + token; pass back to execute.",
      "title": "Confirm Token"
    }
  },
  "required": [
    "action"
  ],
  "type": "object"
}
```

</details>

- action is unconstrained string in schema; handler allows grant/update/revoke only. grant requires nonempty account_id/body; update requires path/body; revoke requires path.
- Requires destructive tier. Confirmation tokens are in-memory, single-use, expire after 600 seconds and bind to exact operation arguments; consumed before API execution.

Source: [src/gtm_ga4_mcp/tools/gtm_destructive.py:171](https://github.com/kb223/gtm-ga4-mcp/blob/40862b6e92d0b70e04b543a6f7ec854258e392cd/src/gtm_ga4_mcp/tools/gtm_destructive.py#L171-L239) · [src/gtm_ga4_mcp/tools/gtm_destructive.py:247](https://github.com/kb223/gtm-ga4-mcp/blob/40862b6e92d0b70e04b543a6f7ec854258e392cd/src/gtm_ga4_mcp/tools/gtm_destructive.py#L247-L252).

## gtm_publish

First call issues confirmation. Redeeming compiles workspace into a version, checks compilerError and version path, then publishes the version live.

<details>
<summary>Full registered description</summary>

```text
Compile a GTM workspace into a version and publish it LIVE. Two-phase.

Publishing deploys the container to every page that loads it — treat it
like a production release. The source workspace is consumed by versioning.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `workspace_path` | Yes | string | Not declared |
| `version_name` | No | string or null | null |
| `notes` | No | string or null | null |
| `confirm_token` | No | string or null | null |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "properties": {
    "workspace_path": {
      "description": "Workspace to publish, e.g. 'accounts/123/containers/456/workspaces/7'.",
      "minLength": 1,
      "title": "Workspace Path",
      "type": "string"
    },
    "version_name": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Name for the created version.",
      "title": "Version Name"
    },
    "notes": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Notes for the created version.",
      "title": "Notes"
    },
    "confirm_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Omit on the first call — it returns a token and a summary instead of publishing. Pass the token back (same arguments) to execute.",
      "title": "Confirm Token"
    }
  },
  "required": [
    "workspace_path"
  ],
  "type": "object"
}
```

</details>

- Workspace path must have six nonempty segments and penultimate collection workspaces. Compilation consumes the source workspace before publish; compiler failure or missing version path aborts publishing.
- Requires destructive tier. Confirmation tokens are in-memory, single-use, expire after 600 seconds and bind to exact operation arguments; consumed before API execution.

Source: [src/gtm_ga4_mcp/tools/gtm_destructive.py:96](https://github.com/kb223/gtm-ga4-mcp/blob/40862b6e92d0b70e04b543a6f7ec854258e392cd/src/gtm_ga4_mcp/tools/gtm_destructive.py#L96-L168) · [src/gtm_ga4_mcp/tools/gtm_destructive.py:244](https://github.com/kb223/gtm-ga4-mcp/blob/40862b6e92d0b70e04b543a6f7ec854258e392cd/src/gtm_ga4_mcp/tools/gtm_destructive.py#L244-L246).

## gtm_update

Validates path and writable collection. Dry-run echoes request; otherwise sends full replacement JSON to update with optional fingerprint.

<details>
<summary>Full registered description</summary>

```text
Update (replace) a GTM entity by path. Defaults to dry-run.

GTM updates are full replacements — always start from gtm_get output.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `path` | Yes | string | Not declared |
| `body` | Yes | object | Not declared |
| `fingerprint` | No | string or null | null |
| `dry_run` | No | boolean | true |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "properties": {
    "path": {
      "description": "Full path of the entity to update, from gtm_list/gtm_get.",
      "minLength": 1,
      "title": "Path",
      "type": "string"
    },
    "body": {
      "additionalProperties": true,
      "description": "COMPLETE entity JSON (the GTM API replaces the entity, not merges). Fetch with gtm_get, modify, and send the whole object back.",
      "title": "Body",
      "type": "object"
    },
    "fingerprint": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional optimistic-lock fingerprint from gtm_get; the update fails if someone changed the entity since.",
      "title": "Fingerprint"
    },
    "dry_run": {
      "default": true,
      "description": "True (default) echoes the request without sending it.",
      "title": "Dry Run",
      "type": "boolean"
    }
  },
  "required": [
    "path",
    "body"
  ],
  "type": "object"
}
```

</details>

- Only workspaces, environments, tags, triggers, variables, folders, templates, clients, transformations, zones collections may be updated. Body is intentionally unconstrained JSON and replaces the entity.
- Requires write/destructive tier; dry_run defaults true. Arbitrary dict bodies expose additionalProperties=true, not an API-specific body model.

Source: [src/gtm_ga4_mcp/tools/gtm_write.py:108](https://github.com/kb223/gtm-ga4-mcp/blob/40862b6e92d0b70e04b543a6f7ec854258e392cd/src/gtm_ga4_mcp/tools/gtm_write.py#L108-L168) · [src/gtm_ga4_mcp/tools/gtm_write.py:173](https://github.com/kb223/gtm-ga4-mcp/blob/40862b6e92d0b70e04b543a6f7ec854258e392cd/src/gtm_ga4_mcp/tools/gtm_write.py#L173-L173).

# HappyMonkeyAI/ai-google-analytics-mcp

[Catalog](../../README.md) · [All tool names](../tool-index.md) · [Upstream](https://github.com/HappyMonkeyAI/ai-google-analytics-mcp) · [JSON](../../data/mcps/happymonkeyai--ai-google-analytics-mcp.json)

**18 tools:** 12 GA4, 6 other-service or server-support tools. Reviewed source: [`170ca6d97a07`](https://github.com/HappyMonkeyAI/ai-google-analytics-mcp/tree/170ca6d97a076393f5ef530c8cc39f3ffb50951f).

Descriptions and parameter schemas come from the registered source definitions. Generated schemas are reconstructed from annotations or validators; live `tools/list` and authenticated API calls were not run. Loose objects remain loose.

<details>
<summary>Exposure and compatibility notes</summary>

- Source review only; no tools/list, upstream execution or live requests. Source supplied without .git; supplied revision is authoritative.
- All 18 @mcp.tool registrations are unconditional. ga4://workflow is a resource, excluded from tool count. Separate analytics-mcp and Keymaster tools mentioned in docs/hints are not registered here.
- Published console entrypoint ga4-provision-mcp resolves to ga4_provision_mcp.server:main and uses MCP SDK 1 FastMCP, stdio transport. README documents uv sync; uv.lock pins mcp 1.28.1 and provides the compatible MCP 1 install path. Install/runtime not executed in this extraction.
- Schema reconstructed from annotations/defaults: no Pydantic/TypedDict request models or injected Context parameters; Optional dict/list nullability retained, arbitrary Any dict values preserved. Docstrings are complete tool descriptions; colon parameter prose is not a Field description or schema constraint.
- Credentials use AnalyticsAdminServiceClient application-default credentials. Optional integrations only read/write local registry and inspect Keymaster files; no Data API calls.

</details>

## Tools

| Tool | Scope | Effect |
| --- | --- | --- |
| [`get_ga4_auth_setup_instructions`](#get_ga4_auth_setup_instructions) | Server support | local |
| [`list_ga_account_summaries`](#list_ga_account_summaries) | GA4 | read |
| [`provision_ga4_property`](#provision_ga4_property) | GA4 | write |
| [`create_web_data_stream`](#create_web_data_stream) | GA4 | write |
| [`render_ga4_gtag_snippet`](#render_ga4_gtag_snippet) | GA4 | local |
| [`inject_ga4_gtag_into_file`](#inject_ga4_gtag_into_file) | GA4 | local |
| [`render_ga4_nextjs_component`](#render_ga4_nextjs_component) | GA4 | local |
| [`scaffold_ga4_nextjs_tracking`](#scaffold_ga4_nextjs_tracking) | GA4 | local |
| [`save_project_ga4_config`](#save_project_ga4_config) | GA4 | local |
| [`provision_project_ga4_setup`](#provision_project_ga4_setup) | GA4 | mixed |
| [`scan_local_ga4_configs`](#scan_local_ga4_configs) | GA4 | read |
| [`list_projects_needing_ga4`](#list_projects_needing_ga4) | Other service | read |
| [`detect_project_tracking_stack`](#detect_project_tracking_stack) | GA4 | read |
| [`get_analytics_monitoring_companion_guide`](#get_analytics_monitoring_companion_guide) | Server support | local |
| [`get_ga4_integration_status`](#get_ga4_integration_status) | Other service | read |
| [`list_registry_projects_for_ga4`](#list_registry_projects_for_ga4) | Other service | read |
| [`resolve_project_for_ga4`](#resolve_project_for_ga4) | Other service | read |
| [`sync_ga4_to_launcher_registry`](#sync_ga4_to_launcher_registry) | GA4 | local |

## get_ga4_auth_setup_instructions

Return static service-account, ADC, API-enablement and companion-server setup instructions.

<details>
<summary>Full registered description</summary>

```text
Return GCP/GA auth steps. Prefer service account if gcloud ADC shows 'This app is blocked'.
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
  "title": "get_ga4_auth_setup_instructionsArguments"
}
```

</details>

Source: [src/ga4_provision_mcp/server.py:31](https://github.com/HappyMonkeyAI/ai-google-analytics-mcp/blob/170ca6d97a076393f5ef530c8cc39f3ffb50951f/src/ga4_provision_mcp/server.py#L31-L55).

## list_ga_account_summaries

Call Admin API list_account_summaries and return account and child property summaries.

<details>
<summary>Full registered description</summary>

```text
List GA account summaries and child properties (read-only Admin API).
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `limit` | No | integer | 20 |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "limit": {
      "type": "integer",
      "title": "Limit",
      "default": 20
    }
  },
  "required": [],
  "title": "list_ga_account_summariesArguments"
}
```

</details>

- Handler caps limit at 50; no exposed numeric bounds.

Source: [src/ga4_provision_mcp/server.py:58](https://github.com/HappyMonkeyAI/ai-google-analytics-mcp/blob/170ca6d97a076393f5ef530c8cc39f3ffb50951f/src/ga4_provision_mcp/server.py#L58-L65) · [src/ga4_provision_mcp/admin.py:110](https://github.com/HappyMonkeyAI/ai-google-analytics-mcp/blob/170ca6d97a076393f5ef530c8cc39f3ffb50951f/src/ga4_provision_mcp/admin.py#L110-L133).

## provision_ga4_property

Normalize account ID and create a Property with display name project_name - environment, account parent, timezone and currency. Blank account_id uses GA4_DEFAULT_ACCOUNT_ID.

<details>
<summary>Full registered description</summary>

```text
Create a new GA4 property for a project under a GA account.
account_id: numeric id only (e.g. 12345678) or accounts/12345678.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `account_id` | Yes | string | Not declared |
| `project_name` | Yes | string | Not declared |
| `timezone` | No | string | "Europe/London" |
| `currency_code` | No | string | "GBP" |
| `environment` | No | string | "Production" |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "account_id": {
      "type": "string",
      "title": "Account Id"
    },
    "project_name": {
      "type": "string",
      "title": "Project Name"
    },
    "timezone": {
      "type": "string",
      "title": "Timezone",
      "default": "Europe/London"
    },
    "currency_code": {
      "type": "string",
      "title": "Currency Code",
      "default": "GBP"
    },
    "environment": {
      "type": "string",
      "title": "Environment",
      "default": "Production"
    }
  },
  "required": [
    "account_id",
    "project_name"
  ],
  "title": "provision_ga4_propertyArguments"
}
```

</details>

- Blank timezone/currency fall back to GA4_DEFAULT_TIMEZONE/GA4_DEFAULT_CURRENCY or hardcoded defaults; account normalization strips all nondigits.

Source: [src/ga4_provision_mcp/server.py:68](https://github.com/HappyMonkeyAI/ai-google-analytics-mcp/blob/170ca6d97a076393f5ef530c8cc39f3ffb50951f/src/ga4_provision_mcp/server.py#L68-L98) · [src/ga4_provision_mcp/admin.py:49](https://github.com/HappyMonkeyAI/ai-google-analytics-mcp/blob/170ca6d97a076393f5ef530c8cc39f3ffb50951f/src/ga4_provision_mcp/admin.py#L49-L76).

## create_web_data_stream

Create a WEB_DATA_STREAM under the normalized property with stream name and website default URI; return measurement ID.

<details>
<summary>Full registered description</summary>

```text
Create a web data stream for a GA4 property. Returns measurement_id (G-XXXXXXXX).
property_id: numeric or properties/<id>.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |
| `stream_name` | Yes | string | Not declared |
| `website_url` | Yes | string | Not declared |

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
    "stream_name": {
      "type": "string",
      "title": "Stream Name"
    },
    "website_url": {
      "type": "string",
      "title": "Website Url"
    }
  },
  "required": [
    "property_id",
    "stream_name",
    "website_url"
  ],
  "title": "create_web_data_streamArguments"
}
```

</details>

- Handler accepts numeric property ID or properties/<numeric ID>; website URL has no local format validation.

Source: [src/ga4_provision_mcp/server.py:101](https://github.com/HappyMonkeyAI/ai-google-analytics-mcp/blob/170ca6d97a076393f5ef530c8cc39f3ffb50951f/src/ga4_provision_mcp/server.py#L101-L115) · [src/ga4_provision_mcp/admin.py:79](https://github.com/HappyMonkeyAI/ai-google-analytics-mcp/blob/170ca6d97a076393f5ef530c8cc39f3ffb50951f/src/ga4_provision_mcp/admin.py#L79-L107).

## render_ga4_gtag_snippet

Generate the standard HTML gtag.js loader and configuration block.

<details>
<summary>Full registered description</summary>

```text
Return HTML gtag snippet for a measurement ID.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `measurement_id` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "measurement_id": {
      "type": "string",
      "title": "Measurement Id"
    }
  },
  "required": [
    "measurement_id"
  ],
  "title": "render_ga4_gtag_snippetArguments"
}
```

</details>

- Measurement ID is stripped then validated against G-[A-Z0-9]+ in implementation, not input schema.

Source: [src/ga4_provision_mcp/server.py:118](https://github.com/HappyMonkeyAI/ai-google-analytics-mcp/blob/170ca6d97a076393f5ef530c8cc39f3ffb50951f/src/ga4_provision_mcp/server.py#L118-L125) · [src/ga4_provision_mcp/snippets.py:10](https://github.com/HappyMonkeyAI/ai-google-analytics-mcp/blob/170ca6d97a076393f5ef530c8cc39f3ffb50951f/src/ga4_provision_mcp/snippets.py#L10-L24).

## inject_ga4_gtag_into_file

Read a local file; replace GA4 placeholder, update an existing gtag ID, insert before closing head, or append; write changes unless dry_run.

<details>
<summary>Full registered description</summary>

```text
Inject or update GA4 gtag in a local HTML/layout file (absolute path recommended).
Set dry_run=true to preview without writing.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `file_path` | Yes | string | Not declared |
| `measurement_id` | Yes | string | Not declared |
| `dry_run` | No | boolean | false |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "file_path": {
      "type": "string",
      "title": "File Path"
    },
    "measurement_id": {
      "type": "string",
      "title": "Measurement Id"
    },
    "dry_run": {
      "type": "boolean",
      "title": "Dry Run",
      "default": false
    }
  },
  "required": [
    "file_path",
    "measurement_id"
  ],
  "title": "inject_ga4_gtag_into_fileArguments"
}
```

</details>

- Measurement ID must match G-[A-Z0-9]+ after trimming; dry_run returns actions and size rather than full updated source.

Source: [src/ga4_provision_mcp/server.py:128](https://github.com/HappyMonkeyAI/ai-google-analytics-mcp/blob/170ca6d97a076393f5ef530c8cc39f3ffb50951f/src/ga4_provision_mcp/server.py#L128-L156) · [src/ga4_provision_mcp/snippets.py:27](https://github.com/HappyMonkeyAI/ai-google-analytics-mcp/blob/170ca6d97a076393f5ef530c8cc39f3ffb50951f/src/ga4_provision_mcp/snippets.py#L27-L80).

## render_ga4_nextjs_component

Generate a Next.js next/script client component, suggested path and env line; optionally gate loading on cookie_consent accepted in localStorage and consent events.

<details>
<summary>Full registered description</summary>

```text
Return a Next.js client component (next/script) for GA4.
mode: env (read NEXT_PUBLIC_GA_MEASUREMENT_ID) or inline (embed id).
consent_gated: only load gtag after localStorage cookie consent is accepted.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `measurement_id` | Yes | string | Not declared |
| `mode` | No | string | "env" |
| `consent_gated` | No | boolean | false |

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
    "mode": {
      "type": "string",
      "title": "Mode",
      "default": "env"
    },
    "consent_gated": {
      "type": "boolean",
      "title": "Consent Gated",
      "default": false
    }
  },
  "required": [
    "measurement_id"
  ],
  "title": "render_ga4_nextjs_componentArguments"
}
```

</details>

- mode is a plain string schema but handler restricts it to env or inline; measurement ID must match G-[A-Z0-9]+.

Source: [src/ga4_provision_mcp/server.py:159](https://github.com/HappyMonkeyAI/ai-google-analytics-mcp/blob/170ca6d97a076393f5ef530c8cc39f3ffb50951f/src/ga4_provision_mcp/server.py#L159-L188) · [src/ga4_provision_mcp/nextjs.py:25](https://github.com/HappyMonkeyAI/ai-google-analytics-mcp/blob/170ca6d97a076393f5ef530c8cc39f3ffb50951f/src/ga4_provision_mcp/nextjs.py#L25-L120).

## scaffold_ga4_nextjs_tracking

Require package.json and existing layout; generate GoogleAnalytics.tsx, patch import/body usage, and upsert .env.local when mode=env, unless dry_run.

<details>
<summary>Full registered description</summary>

```text
Scaffold GA4 for a Next.js app: write GoogleAnalytics.tsx, wire layout.tsx,
and set NEXT_PUBLIC_GA_MEASUREMENT_ID in .env.local (when mode=env).
web_root must be the Next.js package root (directory containing package.json).
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `web_root` | Yes | string | Not declared |
| `measurement_id` | Yes | string | Not declared |
| `layout_relative` | No | string | "src/app/layout.tsx" |
| `mode` | No | string | "env" |
| `consent_gated` | No | boolean | false |
| `dry_run` | No | boolean | false |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "web_root": {
      "type": "string",
      "title": "Web Root"
    },
    "measurement_id": {
      "type": "string",
      "title": "Measurement Id"
    },
    "layout_relative": {
      "type": "string",
      "title": "Layout Relative",
      "default": "src/app/layout.tsx"
    },
    "mode": {
      "type": "string",
      "title": "Mode",
      "default": "env"
    },
    "consent_gated": {
      "type": "boolean",
      "title": "Consent Gated",
      "default": false
    },
    "dry_run": {
      "type": "boolean",
      "title": "Dry Run",
      "default": false
    }
  },
  "required": [
    "web_root",
    "measurement_id"
  ],
  "title": "scaffold_ga4_nextjs_trackingArguments"
}
```

</details>

- mode is a plain string schema but handler restricts it to env or inline; measurement ID must match G-[A-Z0-9]+.
- If layout has no body tag or usage placeholder, layout is unchanged but component/env can still be written.

Source: [src/ga4_provision_mcp/server.py:191](https://github.com/HappyMonkeyAI/ai-google-analytics-mcp/blob/170ca6d97a076393f5ef530c8cc39f3ffb50951f/src/ga4_provision_mcp/server.py#L191-L218) · [src/ga4_provision_mcp/nextjs.py:224](https://github.com/HappyMonkeyAI/ai-google-analytics-mcp/blob/170ca6d97a076393f5ef530c8cc39f3ffb50951f/src/ga4_provision_mcp/nextjs.py#L224-L302) · [src/ga4_provision_mcp/nextjs.py:156](https://github.com/HappyMonkeyAI/ai-google-analytics-mcp/blob/170ca6d97a076393f5ef530c8cc39f3ffb50951f/src/ga4_provision_mcp/nextjs.py#L156-L205).

## save_project_ga4_config

Write .ga4.config.json under an existing directory with trimmed metadata and normalized numeric property ID; include arbitrary extra dictionary if truthy.

<details>
<summary>Full registered description</summary>

```text
Write .ga4.config.json in a project root for agents and humans to reference later.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `project_dir` | Yes | string | Not declared |
| `measurement_id` | Yes | string | Not declared |
| `property_id` | Yes | string | Not declared |
| `website_url` | Yes | string | Not declared |
| `stream_name` | No | string | "" |
| `extra` | No | object or null | null |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "project_dir": {
      "type": "string",
      "title": "Project Dir"
    },
    "measurement_id": {
      "type": "string",
      "title": "Measurement Id"
    },
    "property_id": {
      "type": "string",
      "title": "Property Id"
    },
    "website_url": {
      "type": "string",
      "title": "Website Url"
    },
    "stream_name": {
      "type": "string",
      "title": "Stream Name",
      "default": ""
    },
    "extra": {
      "anyOf": [
        {
          "type": "object",
          "additionalProperties": {}
        },
        {
          "type": "null"
        }
      ],
      "title": "Extra",
      "default": null
    }
  },
  "required": [
    "project_dir",
    "measurement_id",
    "property_id",
    "website_url"
  ],
  "title": "save_project_ga4_configArguments"
}
```

</details>

- extra intentionally accepts arbitrary nested JSON values; no extra model exists. Property normalization errors and filesystem errors are not caught.

Source: [src/ga4_provision_mcp/server.py:221](https://github.com/HappyMonkeyAI/ai-google-analytics-mcp/blob/170ca6d97a076393f5ef530c8cc39f3ffb50951f/src/ga4_provision_mcp/server.py#L221-L244).

## provision_project_ga4_setup

Create property then web stream; optionally write config, detect/apply HTML or Next.js tracking, and sync launcher registry metadata.

<details>
<summary>Full registered description</summary>

```text
End-to-end: create property + web stream, optionally save .ga4.config.json and wire tracking.
tracking_mode: none | html | nextjs | auto (auto uses detect_tracking_stack when project_dir set).
inject_html_path used for html mode (or explicit path). scaffold_nextjs_web_root for nextjs mode.
If registry_slug is set and GA4_LAUNCHER_REGISTRY_* env is configured, syncs analytics.ga4 metadata.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `account_id` | Yes | string | Not declared |
| `project_name` | Yes | string | Not declared |
| `website_url` | Yes | string | Not declared |
| `project_dir` | No | string | "" |
| `timezone` | No | string | "Europe/London" |
| `inject_html_path` | No | string | "" |
| `registry_slug` | No | string | "" |
| `scaffold_nextjs_web_root` | No | string | "" |
| `nextjs_layout_relative` | No | string | "" |
| `nextjs_dry_run` | No | boolean | false |
| `tracking_mode` | No | string | "none" |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "account_id": {
      "type": "string",
      "title": "Account Id"
    },
    "project_name": {
      "type": "string",
      "title": "Project Name"
    },
    "website_url": {
      "type": "string",
      "title": "Website Url"
    },
    "project_dir": {
      "type": "string",
      "title": "Project Dir",
      "default": ""
    },
    "timezone": {
      "type": "string",
      "title": "Timezone",
      "default": "Europe/London"
    },
    "inject_html_path": {
      "type": "string",
      "title": "Inject Html Path",
      "default": ""
    },
    "registry_slug": {
      "type": "string",
      "title": "Registry Slug",
      "default": ""
    },
    "scaffold_nextjs_web_root": {
      "type": "string",
      "title": "Scaffold Nextjs Web Root",
      "default": ""
    },
    "nextjs_layout_relative": {
      "type": "string",
      "title": "Nextjs Layout Relative",
      "default": ""
    },
    "nextjs_dry_run": {
      "type": "boolean",
      "title": "Nextjs Dry Run",
      "default": false
    },
    "tracking_mode": {
      "type": "string",
      "title": "Tracking Mode",
      "default": "none"
    }
  },
  "required": [
    "account_id",
    "project_name",
    "website_url"
  ],
  "title": "provision_project_ga4_setupArguments"
}
```

</details>

- nextjs_dry_run affects only Next.js scaffolding; property/stream provisioning, config writing, HTML injection and registry sync still occur.
- No rollback if stream creation fails after property creation; returned ok may remain true when optional wiring/sync results fail.
- tracking_mode has no schema enum or handler rejection of unknown modes; auto uses filesystem heuristics. Explicit inject_html_path triggers injection even outside html mode.

Source: [src/ga4_provision_mcp/server.py:331](https://github.com/HappyMonkeyAI/ai-google-analytics-mcp/blob/170ca6d97a076393f5ef530c8cc39f3ffb50951f/src/ga4_provision_mcp/server.py#L331-L408) · [src/ga4_provision_mcp/admin.py:49](https://github.com/HappyMonkeyAI/ai-google-analytics-mcp/blob/170ca6d97a076393f5ef530c8cc39f3ffb50951f/src/ga4_provision_mcp/admin.py#L49-L76) · [src/ga4_provision_mcp/admin.py:79](https://github.com/HappyMonkeyAI/ai-google-analytics-mcp/blob/170ca6d97a076393f5ef530c8cc39f3ffb50951f/src/ga4_provision_mcp/admin.py#L79-L107) · [src/ga4_provision_mcp/integrations.py:216](https://github.com/HappyMonkeyAI/ai-google-analytics-mcp/blob/170ca6d97a076393f5ef530c8cc39f3ffb50951f/src/ga4_provision_mcp/integrations.py#L216-L260).

## scan_local_ga4_configs

Walk specified roots or ~/projects for .ga4.config.json, skipping common dependency/VCS directories and applying max_depth; return sorted metadata inventory.

<details>
<summary>Full registered description</summary>

```text
Scan filesystem roots (default ~/projects) for `.ga4.config.json` inventory.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `scan_roots` | No | array of string or null | null |
| `max_depth` | No | integer | 4 |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "scan_roots": {
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
      "title": "Scan Roots",
      "default": null
    },
    "max_depth": {
      "type": "integer",
      "title": "Max Depth",
      "default": 4
    }
  },
  "required": [],
  "title": "scan_local_ga4_configsArguments"
}
```

</details>

- Empty list and null both use default roots; directories at depth >= max_depth are not processed.

Source: [src/ga4_provision_mcp/server.py:411](https://github.com/HappyMonkeyAI/ai-google-analytics-mcp/blob/170ca6d97a076393f5ef530c8cc39f3ffb50951f/src/ga4_provision_mcp/server.py#L411-L417) · [src/ga4_provision_mcp/inventory.py:55](https://github.com/HappyMonkeyAI/ai-google-analytics-mcp/blob/170ca6d97a076393f5ef530c8cc39f3ffb50951f/src/ga4_provision_mcp/inventory.py#L55-L68) · [src/ga4_provision_mcp/inventory.py:25](https://github.com/HappyMonkeyAI/ai-google-analytics-mcp/blob/170ca6d97a076393f5ef530c8cc39f3ffb50951f/src/ga4_provision_mcp/inventory.py#L25-L52).

## list_projects_needing_ga4

Read launcher registry, filter candidates, inspect local configs and registry measurement IDs, return missing-both or partial gaps and tracking stack hints.

<details>
<summary>Full registered description</summary>

```text
Launcher registry projects missing local config and/or registry analytics.ga4 metadata.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `filter_query` | No | string | "" |
| `limit` | No | integer | 50 |
| `include_partial` | No | boolean | true |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "filter_query": {
      "type": "string",
      "title": "Filter Query",
      "default": ""
    },
    "limit": {
      "type": "integer",
      "title": "Limit",
      "default": 50
    },
    "include_partial": {
      "type": "boolean",
      "title": "Include Partial",
      "default": true
    }
  },
  "required": [],
  "title": "list_projects_needing_ga4Arguments"
}
```

</details>

- Requires configured existing launcher registry; limit clamped to 1..100 before gap filtering.

Source: [src/ga4_provision_mcp/server.py:420](https://github.com/HappyMonkeyAI/ai-google-analytics-mcp/blob/170ca6d97a076393f5ef530c8cc39f3ffb50951f/src/ga4_provision_mcp/server.py#L420-L431) · [src/ga4_provision_mcp/inventory.py:155](https://github.com/HappyMonkeyAI/ai-google-analytics-mcp/blob/170ca6d97a076393f5ef530c8cc39f3ffb50951f/src/ga4_provision_mcp/inventory.py#L155-L193).

## detect_project_tracking_stack

Inspect existing project directory and candidate web roots for App Router layouts or HTML entrypoints; recommend nextjs, html or unknown.

<details>
<summary>Full registered description</summary>

```text
Recommend html vs nextjs wiring for a project directory.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `project_dir` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "project_dir": {
      "type": "string",
      "title": "Project Dir"
    }
  },
  "required": [
    "project_dir"
  ],
  "title": "detect_project_tracking_stackArguments"
}
```

</details>

Source: [src/ga4_provision_mcp/server.py:434](https://github.com/HappyMonkeyAI/ai-google-analytics-mcp/blob/170ca6d97a076393f5ef530c8cc39f3ffb50951f/src/ga4_provision_mcp/server.py#L434-L437) · [src/ga4_provision_mcp/inventory.py:92](https://github.com/HappyMonkeyAI/ai-google-analytics-mcp/blob/170ca6d97a076393f5ef530c8cc39f3ffb50951f/src/ga4_provision_mcp/inventory.py#L92-L118).

## get_analytics_monitoring_companion_guide

Return a static dual-server workflow and example configuration for separate official analytics-mcp reporting.

<details>
<summary>Full registered description</summary>

```text
How to pair this provision server with official read-only analytics-mcp for reports.
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
  "title": "get_analytics_monitoring_companion_guideArguments"
}
```

</details>

- Documentation only: no run_report, realtime or other Data API reporting implemented by this server.

Source: [src/ga4_provision_mcp/server.py:440](https://github.com/HappyMonkeyAI/ai-google-analytics-mcp/blob/170ca6d97a076393f5ef530c8cc39f3ffb50951f/src/ga4_provision_mcp/server.py#L440-L460).

## get_ga4_integration_status

Inspect optional launcher registry and Keymaster environment paths and return availability plus environment documentation.

<details>
<summary>Full registered description</summary>

```text
Report optional launcher registry and keymaster hook availability (graceful when unset).
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
  "title": "get_ga4_integration_statusArguments"
}
```

</details>

- Keymaster hooks inspect paths and provide composition hints; no Keymaster credential ingestion API is called.

Source: [src/ga4_provision_mcp/server.py:463](https://github.com/HappyMonkeyAI/ai-google-analytics-mcp/blob/170ca6d97a076393f5ef530c8cc39f3ffb50951f/src/ga4_provision_mcp/server.py#L463-L466) · [src/ga4_provision_mcp/integrations.py:335](https://github.com/HappyMonkeyAI/ai-google-analytics-mcp/blob/170ca6d97a076393f5ef530c8cc39f3ffb50951f/src/ga4_provision_mcp/integrations.py#L335-L346) · [src/ga4_provision_mcp/integrations.py:42](https://github.com/HappyMonkeyAI/ai-google-analytics-mcp/blob/170ca6d97a076393f5ef530c8cc39f3ffb50951f/src/ga4_provision_mcp/integrations.py#L42-L59) · [src/ga4_provision_mcp/integrations.py:263](https://github.com/HappyMonkeyAI/ai-google-analytics-mcp/blob/170ca6d97a076393f5ef530c8cc39f3ffb50951f/src/ga4_provision_mcp/integrations.py#L263-L288).

## list_registry_projects_for_ga4

Read optional launcher registry, apply case-insensitive filter and enrich projects with config, Keymaster bootstrap and web-root hints.

<details>
<summary>Full registered description</summary>

```text
List launcher registry projects with .ga4.config.json and .keymaster hints when registry env is set.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `filter_query` | No | string | "" |
| `limit` | No | integer | 50 |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "filter_query": {
      "type": "string",
      "title": "Filter Query",
      "default": ""
    },
    "limit": {
      "type": "integer",
      "title": "Limit",
      "default": 50
    }
  },
  "required": [],
  "title": "list_registry_projects_for_ga4Arguments"
}
```

</details>

- Requires GA4_LAUNCHER_REGISTRY_JSON or LAUNCHER_REGISTRY_JSON existing file; limit clamped to 1..100.

Source: [src/ga4_provision_mcp/server.py:469](https://github.com/HappyMonkeyAI/ai-google-analytics-mcp/blob/170ca6d97a076393f5ef530c8cc39f3ffb50951f/src/ga4_provision_mcp/server.py#L469-L472) · [src/ga4_provision_mcp/integrations.py:135](https://github.com/HappyMonkeyAI/ai-google-analytics-mcp/blob/170ca6d97a076393f5ef530c8cc39f3ffb50951f/src/ga4_provision_mcp/integrations.py#L135-L159).

## resolve_project_for_ga4

Resolve registry slug and/or local directory; read GA4 config and Keymaster bootstrap metadata, suggest web roots and URL, emit agent integration hints.

<details>
<summary>Full registered description</summary>

```text
Resolve registry slug and/or filesystem path for GA4 provisioning (paths, website_url, agent hints).
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `slug` | No | string | "" |
| `project_dir` | No | string | "" |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "slug": {
      "type": "string",
      "title": "Slug",
      "default": ""
    },
    "project_dir": {
      "type": "string",
      "title": "Project Dir",
      "default": ""
    }
  },
  "required": [],
  "title": "resolve_project_for_ga4Arguments"
}
```

</details>

- At least one nonblank slug/project_dir required in implementation, not schema.

Source: [src/ga4_provision_mcp/server.py:475](https://github.com/HappyMonkeyAI/ai-google-analytics-mcp/blob/170ca6d97a076393f5ef530c8cc39f3ffb50951f/src/ga4_provision_mcp/server.py#L475-L478) · [src/ga4_provision_mcp/integrations.py:174](https://github.com/HappyMonkeyAI/ai-google-analytics-mcp/blob/170ca6d97a076393f5ef530c8cc39f3ffb50951f/src/ga4_provision_mcp/integrations.py#L174-L213).

## sync_ga4_to_launcher_registry

Find launcher registry project by slug; overwrite analytics.ga4 metadata with timestamp and save registry JSON updating updated_at.

<details>
<summary>Full registered description</summary>

```text
Write GA4 metadata to launcher registry project.analytics.ga4 (requires writable env).
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `slug` | Yes | string | Not declared |
| `measurement_id` | Yes | string | Not declared |
| `property_id` | Yes | string | Not declared |
| `website_url` | No | string | "" |
| `stream_name` | No | string | "" |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "slug": {
      "type": "string",
      "title": "Slug"
    },
    "measurement_id": {
      "type": "string",
      "title": "Measurement Id"
    },
    "property_id": {
      "type": "string",
      "title": "Property Id"
    },
    "website_url": {
      "type": "string",
      "title": "Website Url",
      "default": ""
    },
    "stream_name": {
      "type": "string",
      "title": "Stream Name",
      "default": ""
    }
  },
  "required": [
    "slug",
    "measurement_id",
    "property_id"
  ],
  "title": "sync_ga4_to_launcher_registryArguments"
}
```

</details>

- Tool always registered; action requires existing registry env and GA4_LAUNCHER_REGISTRY_WRITABLE set to 1,true,yes. Measurement ID must match G-[A-Z0-9]+. Property ID only trimmed, not validated.

Source: [src/ga4_provision_mcp/server.py:481](https://github.com/HappyMonkeyAI/ai-google-analytics-mcp/blob/170ca6d97a076393f5ef530c8cc39f3ffb50951f/src/ga4_provision_mcp/server.py#L481-L496) · [src/ga4_provision_mcp/integrations.py:216](https://github.com/HappyMonkeyAI/ai-google-analytics-mcp/blob/170ca6d97a076393f5ef530c8cc39f3ffb50951f/src/ga4_provision_mcp/integrations.py#L216-L260) · [src/ga4_provision_mcp/integrations.py:70](https://github.com/HappyMonkeyAI/ai-google-analytics-mcp/blob/170ca6d97a076393f5ef530c8cc39f3ffb50951f/src/ga4_provision_mcp/integrations.py#L70-L79).

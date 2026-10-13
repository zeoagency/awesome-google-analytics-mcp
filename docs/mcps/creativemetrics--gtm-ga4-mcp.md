# CreativeMetrics/gtm-ga4-mcp

[Catalog](../../README.md) · [All tool names](../tool-index.md) · [Upstream](https://github.com/CreativeMetrics/gtm-ga4-mcp) · [JSON](../../data/mcps/creativemetrics--gtm-ga4-mcp.json)

**47 tools:** 14 GA4, 33 other-service or server-support tools. Reviewed source: [`2f274468eaf7`](https://github.com/CreativeMetrics/gtm-ga4-mcp/tree/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302).

Descriptions and parameter schemas come from the registered source definitions. Generated schemas are reconstructed from annotations or validators; live `tools/list` and authenticated API calls were not run. Loose objects remain loose.

<details>
<summary>Exposure and compatibility notes</summary>

- Source review only; no tools/list or live requests and no upstream code execution.
- All registration is unconditional in index.js; imported modules provide implementation helpers rather than additional tool lists. Standalone health-check.js script and formatting helper are not MCP tools.
- OAuth client reads ~/.gtm-ga4-mcp/credentials.json and optional token.json. Authorization uses the legacy urn:ietf:wg:oauth:2.0:oob redirect; this is a setup compatibility risk, not an authenticated runtime test.
- Puppeteer/browser installation is required by browser tools; package entrypoint is index.js.
- Error responses are caught and returned as MCP isError text. No runtime input validation is implemented in the dispatcher.

</details>

## Tools

| Tool | Scope | Effect |
| --- | --- | --- |
| [`get_auth_url`](#get_auth_url) | Server support | local |
| [`exchange_auth_code`](#exchange_auth_code) | Server support | write |
| [`gtm_list_accounts`](#gtm_list_accounts) | Other service | read |
| [`gtm_list_containers`](#gtm_list_containers) | Other service | read |
| [`gtm_create_workspace`](#gtm_create_workspace) | Other service | write |
| [`gtm_copy_template`](#gtm_copy_template) | Other service | mixed |
| [`gtm_list_templates`](#gtm_list_templates) | Other service | read |
| [`gtm_list_tags`](#gtm_list_tags) | Other service | read |
| [`gtm_create_tag`](#gtm_create_tag) | Other service | write |
| [`gtm_update_tag`](#gtm_update_tag) | Other service | write |
| [`gtm_delete_tag`](#gtm_delete_tag) | Other service | write |
| [`gtm_list_triggers`](#gtm_list_triggers) | Other service | read |
| [`gtm_create_trigger`](#gtm_create_trigger) | Other service | write |
| [`gtm_update_trigger`](#gtm_update_trigger) | Other service | write |
| [`gtm_delete_trigger`](#gtm_delete_trigger) | Other service | write |
| [`gtm_list_variables`](#gtm_list_variables) | Other service | read |
| [`gtm_create_variable`](#gtm_create_variable) | Other service | write |
| [`gtm_update_variable`](#gtm_update_variable) | Other service | write |
| [`gtm_delete_variable`](#gtm_delete_variable) | Other service | write |
| [`gtm_duplicate_container`](#gtm_duplicate_container) | Other service | mixed |
| [`gtm_list_users`](#gtm_list_users) | Other service | read |
| [`gtm_add_user`](#gtm_add_user) | Other service | write |
| [`gtm_update_user`](#gtm_update_user) | Other service | write |
| [`gtm_remove_user`](#gtm_remove_user) | Other service | write |
| [`gtm_publish_container`](#gtm_publish_container) | Other service | write |
| [`scan_url`](#scan_url) | Other service | read |
| [`create_tags_from_url`](#create_tags_from_url) | Other service | mixed |
| [`compare_url_with_container`](#compare_url_with_container) | Other service | read |
| [`ga4_list_properties`](#ga4_list_properties) | GA4 | read |
| [`ga4_list_custom_dimensions`](#ga4_list_custom_dimensions) | GA4 | read |
| [`ga4_create_custom_dimension`](#ga4_create_custom_dimension) | GA4 | write |
| [`ga4_duplicate_custom_dimensions`](#ga4_duplicate_custom_dimensions) | GA4 | mixed |
| [`ga4_list_custom_metrics`](#ga4_list_custom_metrics) | GA4 | read |
| [`ga4_run_report`](#ga4_run_report) | GA4 | read |
| [`ga4_list_conversion_events`](#ga4_list_conversion_events) | GA4 | read |
| [`ga4_list_data_streams`](#ga4_list_data_streams) | GA4 | read |
| [`ga4_list_audiences`](#ga4_list_audiences) | GA4 | read |
| [`ga4_list_key_events`](#ga4_list_key_events) | GA4 | read |
| [`ga4_create_key_event`](#ga4_create_key_event) | GA4 | write |
| [`ga4_compare_properties`](#ga4_compare_properties) | GA4 | read |
| [`ga4_looker_report_url`](#ga4_looker_report_url) | GA4 | local |
| [`gtm_check_tag_health`](#gtm_check_tag_health) | GA4 | read |
| [`gsc_list_sites`](#gsc_list_sites) | Other service | read |
| [`gsc_top_queries`](#gsc_top_queries) | Other service | read |
| [`gsc_top_pages`](#gsc_top_pages) | Other service | read |
| [`gsc_compare_periods`](#gsc_compare_periods) | Other service | read |
| [`gsc_search_analytics`](#gsc_search_analytics) | Other service | read |

## get_auth_url

Reads configured OAuth client and optional saved tokens, then generates an offline Google OAuth authorization URL with the configured scopes.

<details>
<summary>Full registered description</summary>

```text
Genera il link di autorizzazione OAuth2 per Google. Da usare al primo avvio.
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

Source: [index.js:24](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L24-L28) · [index.js:646](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L646-L651) · [src/auth.js:39](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/auth.js#L39-L46).

## exchange_auth_code

Exchanges the supplied OAuth code and saves tokens to ~/.gtm-ga4-mcp/token.json.

<details>
<summary>Full registered description</summary>

```text
Completa il login scambiando il codice OAuth con un token di accesso.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `code` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "code": {
      "type": "string",
      "description": "Codice ricevuto da Google dopo il login"
    }
  },
  "required": [
    "code"
  ]
}
```

</details>

Source: [index.js:29](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L29-L37) · [index.js:652](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L652-L659) · [src/auth.js:47](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/auth.js#L47-L57).

## gtm_list_accounts

Returns API response entity list/data. Calls Tag Manager API v2 accounts.list.

<details>
<summary>Full registered description</summary>

```text
Elenca tutti gli account Google Tag Manager accessibili.
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

- Dispatcher constructs OAuth client before handling this tool, including browser-only scan and local Looker URL generation; configured credentials file is required.

Source: [index.js:40](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L40-L44) · [index.js:671](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L671-L673) · [src/gtm.js:7](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm.js#L7-L12) · [src/gtm.js:3](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm.js#L3-L6).

## gtm_list_containers

Returns API response entity list/data. Calls Tag Manager API v2 accounts.containers.list.

<details>
<summary>Full registered description</summary>

```text
Elenca i container GTM di un account.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `account_id` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "account_id": {
      "type": "string",
      "description": "ID account GTM"
    }
  },
  "required": [
    "account_id"
  ]
}
```

</details>

- Dispatcher constructs OAuth client before handling this tool, including browser-only scan and local Looker URL generation; configured credentials file is required.

Source: [index.js:45](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L45-L53) · [index.js:674](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L674-L676) · [src/gtm.js:13](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm.js#L13-L20) · [src/gtm.js:3](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm.js#L3-L6).

## gtm_create_workspace

Performs the requested API mutation and returns response data or a deletion acknowledgement. Calls Tag Manager API v2 accounts.containers.workspaces.create.

<details>
<summary>Full registered description</summary>

```text
Crea un nuovo workspace GTM. Utile dopo una pubblicazione per iniziare un nuovo set di modifiche.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `account_id` | Yes | string | Not declared |
| `container_id` | Yes | string | Not declared |
| `name` | Yes | string | Not declared |
| `description` | No | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "account_id": {
      "type": "string"
    },
    "container_id": {
      "type": "string"
    },
    "name": {
      "type": "string",
      "description": "Nome del workspace (es. \"Modifiche maggio 2025\")"
    },
    "description": {
      "type": "string",
      "description": "Descrizione opzionale"
    }
  },
  "required": [
    "account_id",
    "container_id",
    "name"
  ]
}
```

</details>

- Dispatcher constructs OAuth client before handling this tool, including browser-only scan and local Looker URL generation; configured credentials file is required.

Source: [index.js:54](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L54-L67) · [index.js:677](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L677-L679) · [src/gtm.js:83](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm.js#L83-L93) · [src/gtm.js:3](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm.js#L3-L6).

## gtm_copy_template

Resolves source and destination workspaces, matches template name case-insensitively, returns existing destination template or creates one using source templateData and optional galleryReference.

<details>
<summary>Full registered description</summary>

```text
Copia un singolo template da un container GTM a un altro per nome. Utile per installare un template specifico senza fare una duplicazione completa.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `src_account_id` | Yes | string | Not declared |
| `src_container_id` | Yes | string | Not declared |
| `src_workspace_id` | No | string | Not declared |
| `template_name` | Yes | string | Not declared |
| `dst_account_id` | Yes | string | Not declared |
| `dst_container_id` | Yes | string | Not declared |
| `dst_workspace_id` | No | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "src_account_id": {
      "type": "string"
    },
    "src_container_id": {
      "type": "string"
    },
    "src_workspace_id": {
      "type": "string",
      "description": "Opzionale"
    },
    "template_name": {
      "type": "string",
      "description": "Nome esatto del template da copiare"
    },
    "dst_account_id": {
      "type": "string"
    },
    "dst_container_id": {
      "type": "string"
    },
    "dst_workspace_id": {
      "type": "string",
      "description": "Opzionale"
    }
  },
  "required": [
    "src_account_id",
    "src_container_id",
    "template_name",
    "dst_account_id",
    "dst_container_id"
  ]
}
```

</details>

- Dispatcher constructs OAuth client before handling this tool, including browser-only scan and local Looker URL generation; configured credentials file is required.

Source: [index.js:68](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L68-L84) · [index.js:660](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L660-L667) · [src/gtm.js:42](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm.js#L42-L73) · [src/gtm.js:3](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm.js#L3-L6) · [src/gtm.js:31](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm.js#L31-L41) · [src/gtm.js:21](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm.js#L21-L30).

## gtm_list_templates

Returns API response entity list/data. Calls Tag Manager API v2 accounts.containers.workspaces.templates.list, Tag Manager API v2 accounts.containers.workspaces.list.

<details>
<summary>Full registered description</summary>

```text
Elenca i template installati in un workspace GTM, incluso il loro tipo (cvt_...) e templateId.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `account_id` | Yes | string | Not declared |
| `container_id` | Yes | string | Not declared |
| `workspace_id` | No | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "account_id": {
      "type": "string"
    },
    "container_id": {
      "type": "string"
    },
    "workspace_id": {
      "type": "string",
      "description": "Opzionale"
    }
  },
  "required": [
    "account_id",
    "container_id"
  ]
}
```

</details>

- Dispatcher constructs OAuth client before handling this tool, including browser-only scan and local Looker URL generation; configured credentials file is required.
- Omitted workspace resolves cached Default Workspace by name or first workspace; no workspace causes an error.

Source: [index.js:85](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L85-L97) · [index.js:668](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L668-L670) · [src/gtm.js:74](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm.js#L74-L82) · [src/gtm.js:3](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm.js#L3-L6) · [src/gtm.js:31](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm.js#L31-L41) · [src/gtm.js:21](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm.js#L21-L30).

## gtm_list_tags

Returns API response entity list/data. Calls Tag Manager API v2 accounts.containers.workspaces.tags.list, Tag Manager API v2 accounts.containers.workspaces.list.

<details>
<summary>Full registered description</summary>

```text
Elenca i tag in un workspace GTM.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `account_id` | Yes | string | Not declared |
| `container_id` | Yes | string | Not declared |
| `workspace_id` | No | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "account_id": {
      "type": "string"
    },
    "container_id": {
      "type": "string"
    },
    "workspace_id": {
      "type": "string",
      "description": "Opzionale"
    }
  },
  "required": [
    "account_id",
    "container_id"
  ]
}
```

</details>

- Dispatcher constructs OAuth client before handling this tool, including browser-only scan and local Looker URL generation; configured credentials file is required.
- Omitted workspace resolves cached Default Workspace by name or first workspace; no workspace causes an error.

Source: [index.js:99](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L99-L111) · [index.js:680](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L680-L682) · [src/gtm.js:94](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm.js#L94-L102) · [src/gtm.js:3](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm.js#L3-L6) · [src/gtm.js:31](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm.js#L31-L41) · [src/gtm.js:21](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm.js#L21-L30).

## gtm_create_tag

Performs the requested API mutation and returns response data or a deletion acknowledgement. Calls Tag Manager API v2 accounts.containers.workspaces.tags.create, Tag Manager API v2 accounts.containers.workspaces.list.

<details>
<summary>Full registered description</summary>

```text
Crea un nuovo tag in un workspace GTM.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `account_id` | Yes | string | Not declared |
| `container_id` | Yes | string | Not declared |
| `workspace_id` | No | string | Not declared |
| `tag` | Yes | object | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "account_id": {
      "type": "string"
    },
    "container_id": {
      "type": "string"
    },
    "workspace_id": {
      "type": "string",
      "description": "Opzionale"
    },
    "tag": {
      "type": "object",
      "description": "Oggetto tag GTM (name, type, parameter, firingTriggerId, ecc.)"
    }
  },
  "required": [
    "account_id",
    "container_id",
    "tag"
  ]
}
```

</details>

- Dispatcher constructs OAuth client before handling this tool, including browser-only scan and local Looker URL generation; configured credentials file is required.
- GTM entity request body is an intentionally loose object schema and is forwarded unchanged; no nested entity fields are exposed.
- Omitted workspace resolves cached Default Workspace by name or first workspace; no workspace causes an error.

Source: [index.js:112](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L112-L125) · [index.js:683](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L683-L685) · [src/gtm.js:103](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm.js#L103-L112) · [src/gtm.js:3](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm.js#L3-L6) · [src/gtm.js:31](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm.js#L31-L41) · [src/gtm.js:21](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm.js#L21-L30).

## gtm_update_tag

Performs the requested API mutation and returns response data or a deletion acknowledgement. Calls Tag Manager API v2 accounts.containers.workspaces.tags.update, Tag Manager API v2 accounts.containers.workspaces.list.

<details>
<summary>Full registered description</summary>

```text
Modifica un tag esistente in un workspace GTM.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `account_id` | Yes | string | Not declared |
| `container_id` | Yes | string | Not declared |
| `workspace_id` | No | string | Not declared |
| `tag_id` | Yes | string | Not declared |
| `tag` | Yes | object | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "account_id": {
      "type": "string"
    },
    "container_id": {
      "type": "string"
    },
    "workspace_id": {
      "type": "string",
      "description": "Opzionale"
    },
    "tag_id": {
      "type": "string",
      "description": "ID del tag da modificare"
    },
    "tag": {
      "type": "object",
      "description": "Oggetto tag aggiornato"
    }
  },
  "required": [
    "account_id",
    "container_id",
    "tag_id",
    "tag"
  ]
}
```

</details>

- Dispatcher constructs OAuth client before handling this tool, including browser-only scan and local Looker URL generation; configured credentials file is required.
- GTM entity request body is an intentionally loose object schema and is forwarded unchanged; no nested entity fields are exposed.
- Omitted workspace resolves cached Default Workspace by name or first workspace; no workspace causes an error.

Source: [index.js:126](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L126-L140) · [index.js:686](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L686-L688) · [src/gtm.js:113](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm.js#L113-L122) · [src/gtm.js:3](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm.js#L3-L6) · [src/gtm.js:31](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm.js#L31-L41) · [src/gtm.js:21](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm.js#L21-L30).

## gtm_delete_tag

Performs the requested API mutation and returns response data or a deletion acknowledgement. Calls Tag Manager API v2 accounts.containers.workspaces.tags.delete, Tag Manager API v2 accounts.containers.workspaces.list.

<details>
<summary>Full registered description</summary>

```text
Elimina un tag da un workspace GTM.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `account_id` | Yes | string | Not declared |
| `container_id` | Yes | string | Not declared |
| `workspace_id` | No | string | Not declared |
| `tag_id` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "account_id": {
      "type": "string"
    },
    "container_id": {
      "type": "string"
    },
    "workspace_id": {
      "type": "string",
      "description": "Opzionale"
    },
    "tag_id": {
      "type": "string",
      "description": "ID del tag da eliminare"
    }
  },
  "required": [
    "account_id",
    "container_id",
    "tag_id"
  ]
}
```

</details>

- Dispatcher constructs OAuth client before handling this tool, including browser-only scan and local Looker URL generation; configured credentials file is required.
- Omitted workspace resolves cached Default Workspace by name or first workspace; no workspace causes an error.

Source: [index.js:141](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L141-L154) · [index.js:689](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L689-L691) · [src/gtm.js:123](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm.js#L123-L133) · [src/gtm.js:3](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm.js#L3-L6) · [src/gtm.js:31](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm.js#L31-L41) · [src/gtm.js:21](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm.js#L21-L30).

## gtm_list_triggers

Returns API response entity list/data. Calls Tag Manager API v2 accounts.containers.workspaces.triggers.list, Tag Manager API v2 accounts.containers.workspaces.list.

<details>
<summary>Full registered description</summary>

```text
Elenca i trigger in un workspace GTM.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `account_id` | Yes | string | Not declared |
| `container_id` | Yes | string | Not declared |
| `workspace_id` | No | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "account_id": {
      "type": "string"
    },
    "container_id": {
      "type": "string"
    },
    "workspace_id": {
      "type": "string",
      "description": "Opzionale"
    }
  },
  "required": [
    "account_id",
    "container_id"
  ]
}
```

</details>

- Dispatcher constructs OAuth client before handling this tool, including browser-only scan and local Looker URL generation; configured credentials file is required.
- Omitted workspace resolves cached Default Workspace by name or first workspace; no workspace causes an error.

Source: [index.js:157](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L157-L169) · [index.js:692](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L692-L694) · [src/gtm.js:134](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm.js#L134-L142) · [src/gtm.js:3](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm.js#L3-L6) · [src/gtm.js:31](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm.js#L31-L41) · [src/gtm.js:21](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm.js#L21-L30).

## gtm_create_trigger

Performs the requested API mutation and returns response data or a deletion acknowledgement. Calls Tag Manager API v2 accounts.containers.workspaces.triggers.create, Tag Manager API v2 accounts.containers.workspaces.list.

<details>
<summary>Full registered description</summary>

```text
Crea un nuovo trigger in un workspace GTM.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `account_id` | Yes | string | Not declared |
| `container_id` | Yes | string | Not declared |
| `workspace_id` | No | string | Not declared |
| `trigger` | Yes | object | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "account_id": {
      "type": "string"
    },
    "container_id": {
      "type": "string"
    },
    "workspace_id": {
      "type": "string",
      "description": "Opzionale"
    },
    "trigger": {
      "type": "object",
      "description": "Oggetto trigger GTM (name, type, filter, ecc.)"
    }
  },
  "required": [
    "account_id",
    "container_id",
    "trigger"
  ]
}
```

</details>

- Dispatcher constructs OAuth client before handling this tool, including browser-only scan and local Looker URL generation; configured credentials file is required.
- GTM entity request body is an intentionally loose object schema and is forwarded unchanged; no nested entity fields are exposed.
- Omitted workspace resolves cached Default Workspace by name or first workspace; no workspace causes an error.

Source: [index.js:170](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L170-L183) · [index.js:695](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L695-L697) · [src/gtm.js:143](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm.js#L143-L152) · [src/gtm.js:3](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm.js#L3-L6) · [src/gtm.js:31](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm.js#L31-L41) · [src/gtm.js:21](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm.js#L21-L30).

## gtm_update_trigger

Performs the requested API mutation and returns response data or a deletion acknowledgement. Calls Tag Manager API v2 accounts.containers.workspaces.triggers.update, Tag Manager API v2 accounts.containers.workspaces.list.

<details>
<summary>Full registered description</summary>

```text
Modifica un trigger esistente in un workspace GTM.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `account_id` | Yes | string | Not declared |
| `container_id` | Yes | string | Not declared |
| `workspace_id` | No | string | Not declared |
| `trigger_id` | Yes | string | Not declared |
| `trigger` | Yes | object | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "account_id": {
      "type": "string"
    },
    "container_id": {
      "type": "string"
    },
    "workspace_id": {
      "type": "string",
      "description": "Opzionale"
    },
    "trigger_id": {
      "type": "string",
      "description": "ID del trigger da modificare"
    },
    "trigger": {
      "type": "object",
      "description": "Oggetto trigger aggiornato"
    }
  },
  "required": [
    "account_id",
    "container_id",
    "trigger_id",
    "trigger"
  ]
}
```

</details>

- Dispatcher constructs OAuth client before handling this tool, including browser-only scan and local Looker URL generation; configured credentials file is required.
- GTM entity request body is an intentionally loose object schema and is forwarded unchanged; no nested entity fields are exposed.
- Omitted workspace resolves cached Default Workspace by name or first workspace; no workspace causes an error.

Source: [index.js:184](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L184-L198) · [index.js:698](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L698-L700) · [src/gtm.js:153](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm.js#L153-L162) · [src/gtm.js:3](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm.js#L3-L6) · [src/gtm.js:31](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm.js#L31-L41) · [src/gtm.js:21](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm.js#L21-L30).

## gtm_delete_trigger

Performs the requested API mutation and returns response data or a deletion acknowledgement. Calls Tag Manager API v2 accounts.containers.workspaces.triggers.delete, Tag Manager API v2 accounts.containers.workspaces.list.

<details>
<summary>Full registered description</summary>

```text
Elimina un trigger da un workspace GTM.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `account_id` | Yes | string | Not declared |
| `container_id` | Yes | string | Not declared |
| `workspace_id` | No | string | Not declared |
| `trigger_id` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "account_id": {
      "type": "string"
    },
    "container_id": {
      "type": "string"
    },
    "workspace_id": {
      "type": "string",
      "description": "Opzionale"
    },
    "trigger_id": {
      "type": "string",
      "description": "ID del trigger da eliminare"
    }
  },
  "required": [
    "account_id",
    "container_id",
    "trigger_id"
  ]
}
```

</details>

- Dispatcher constructs OAuth client before handling this tool, including browser-only scan and local Looker URL generation; configured credentials file is required.
- Omitted workspace resolves cached Default Workspace by name or first workspace; no workspace causes an error.

Source: [index.js:199](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L199-L212) · [index.js:701](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L701-L703) · [src/gtm.js:163](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm.js#L163-L173) · [src/gtm.js:3](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm.js#L3-L6) · [src/gtm.js:31](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm.js#L31-L41) · [src/gtm.js:21](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm.js#L21-L30).

## gtm_list_variables

Returns API response entity list/data. Calls Tag Manager API v2 accounts.containers.workspaces.variables.list, Tag Manager API v2 accounts.containers.workspaces.list.

<details>
<summary>Full registered description</summary>

```text
Elenca le variabili in un workspace GTM.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `account_id` | Yes | string | Not declared |
| `container_id` | Yes | string | Not declared |
| `workspace_id` | No | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "account_id": {
      "type": "string"
    },
    "container_id": {
      "type": "string"
    },
    "workspace_id": {
      "type": "string",
      "description": "Opzionale"
    }
  },
  "required": [
    "account_id",
    "container_id"
  ]
}
```

</details>

- Dispatcher constructs OAuth client before handling this tool, including browser-only scan and local Looker URL generation; configured credentials file is required.
- Omitted workspace resolves cached Default Workspace by name or first workspace; no workspace causes an error.

Source: [index.js:215](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L215-L227) · [index.js:704](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L704-L706) · [src/gtm.js:174](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm.js#L174-L182) · [src/gtm.js:3](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm.js#L3-L6) · [src/gtm.js:31](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm.js#L31-L41) · [src/gtm.js:21](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm.js#L21-L30).

## gtm_create_variable

Performs the requested API mutation and returns response data or a deletion acknowledgement. Calls Tag Manager API v2 accounts.containers.workspaces.variables.create, Tag Manager API v2 accounts.containers.workspaces.list.

<details>
<summary>Full registered description</summary>

```text
Crea una nuova variabile in un workspace GTM.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `account_id` | Yes | string | Not declared |
| `container_id` | Yes | string | Not declared |
| `workspace_id` | No | string | Not declared |
| `variable` | Yes | object | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "account_id": {
      "type": "string"
    },
    "container_id": {
      "type": "string"
    },
    "workspace_id": {
      "type": "string",
      "description": "Opzionale"
    },
    "variable": {
      "type": "object",
      "description": "Oggetto variabile GTM (name, type, parameter, ecc.)"
    }
  },
  "required": [
    "account_id",
    "container_id",
    "variable"
  ]
}
```

</details>

- Dispatcher constructs OAuth client before handling this tool, including browser-only scan and local Looker URL generation; configured credentials file is required.
- GTM entity request body is an intentionally loose object schema and is forwarded unchanged; no nested entity fields are exposed.
- Omitted workspace resolves cached Default Workspace by name or first workspace; no workspace causes an error.

Source: [index.js:228](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L228-L241) · [index.js:707](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L707-L709) · [src/gtm.js:183](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm.js#L183-L192) · [src/gtm.js:3](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm.js#L3-L6) · [src/gtm.js:31](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm.js#L31-L41) · [src/gtm.js:21](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm.js#L21-L30).

## gtm_update_variable

Performs the requested API mutation and returns response data or a deletion acknowledgement. Calls Tag Manager API v2 accounts.containers.workspaces.variables.update, Tag Manager API v2 accounts.containers.workspaces.list.

<details>
<summary>Full registered description</summary>

```text
Modifica una variabile esistente in un workspace GTM.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `account_id` | Yes | string | Not declared |
| `container_id` | Yes | string | Not declared |
| `workspace_id` | No | string | Not declared |
| `variable_id` | Yes | string | Not declared |
| `variable` | Yes | object | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "account_id": {
      "type": "string"
    },
    "container_id": {
      "type": "string"
    },
    "workspace_id": {
      "type": "string",
      "description": "Opzionale"
    },
    "variable_id": {
      "type": "string",
      "description": "ID della variabile da modificare"
    },
    "variable": {
      "type": "object",
      "description": "Oggetto variabile aggiornato"
    }
  },
  "required": [
    "account_id",
    "container_id",
    "variable_id",
    "variable"
  ]
}
```

</details>

- Dispatcher constructs OAuth client before handling this tool, including browser-only scan and local Looker URL generation; configured credentials file is required.
- GTM entity request body is an intentionally loose object schema and is forwarded unchanged; no nested entity fields are exposed.
- Omitted workspace resolves cached Default Workspace by name or first workspace; no workspace causes an error.

Source: [index.js:242](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L242-L256) · [index.js:710](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L710-L712) · [src/gtm.js:193](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm.js#L193-L202) · [src/gtm.js:3](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm.js#L3-L6) · [src/gtm.js:31](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm.js#L31-L41) · [src/gtm.js:21](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm.js#L21-L30).

## gtm_delete_variable

Performs the requested API mutation and returns response data or a deletion acknowledgement. Calls Tag Manager API v2 accounts.containers.workspaces.variables.delete, Tag Manager API v2 accounts.containers.workspaces.list.

<details>
<summary>Full registered description</summary>

```text
Elimina una variabile da un workspace GTM.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `account_id` | Yes | string | Not declared |
| `container_id` | Yes | string | Not declared |
| `workspace_id` | No | string | Not declared |
| `variable_id` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "account_id": {
      "type": "string"
    },
    "container_id": {
      "type": "string"
    },
    "workspace_id": {
      "type": "string",
      "description": "Opzionale"
    },
    "variable_id": {
      "type": "string",
      "description": "ID della variabile da eliminare"
    }
  },
  "required": [
    "account_id",
    "container_id",
    "variable_id"
  ]
}
```

</details>

- Dispatcher constructs OAuth client before handling this tool, including browser-only scan and local Looker URL generation; configured credentials file is required.
- Omitted workspace resolves cached Default Workspace by name or first workspace; no workspace causes an error.

Source: [index.js:257](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L257-L270) · [index.js:713](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L713-L715) · [src/gtm.js:203](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm.js#L203-L213) · [src/gtm.js:3](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm.js#L3-L6) · [src/gtm.js:31](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm.js#L31-L41) · [src/gtm.js:21](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm.js#L21-L30).

## gtm_duplicate_container

Reads source workspace entities, creates a destination workspace, copies templates, folders, built-in variables, variables, triggers and tags with ID remapping, prefix/suffix and rate-limit retries; returns partial successes/errors.

<details>
<summary>Full registered description</summary>

```text
Duplica un intero container GTM (tag, trigger, variabili, cartelle, template) in un altro container. Gestisce rate limiting, backoff automatico sui 429, remapping ID e installazione template.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `src_account_id` | Yes | string | Not declared |
| `src_container_id` | Yes | string | Not declared |
| `dst_account_id` | Yes | string | Not declared |
| `dst_container_id` | Yes | string | Not declared |
| `prefix` | No | string | Not declared |
| `suffix` | No | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "src_account_id": {
      "type": "string",
      "description": "Account ID del container sorgente"
    },
    "src_container_id": {
      "type": "string",
      "description": "Container ID sorgente"
    },
    "dst_account_id": {
      "type": "string",
      "description": "Account ID del container destinazione"
    },
    "dst_container_id": {
      "type": "string",
      "description": "Container ID destinazione"
    },
    "prefix": {
      "type": "string",
      "description": "Prefisso opzionale da aggiungere ai nomi (es. \"[COPIA] \")"
    },
    "suffix": {
      "type": "string",
      "description": "Suffisso opzionale da aggiungere ai nomi"
    }
  },
  "required": [
    "src_account_id",
    "src_container_id",
    "dst_account_id",
    "dst_container_id"
  ]
}
```

</details>

- Dispatcher constructs OAuth client before handling this tool, including browser-only scan and local Looker URL generation; configured credentials file is required.
- Source workspace is Default Workspace or first available; raw REST list reads do not iterate pagination. Individual copy failures can leave a partially populated destination workspace.

Source: [index.js:271](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L271-L286) · [index.js:716](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L716-L723) · [src/gtm-duplicate.js:58](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm-duplicate.js#L58-L376) · [src/gtm-duplicate.js:8](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm-duplicate.js#L8-L11) · [src/gtm-duplicate.js:12](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm-duplicate.js#L12-L20) · [src/gtm-duplicate.js:21](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm-duplicate.js#L21-L28) · [src/gtm-duplicate.js:29](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm-duplicate.js#L29-L32) · [src/gtm-duplicate.js:33](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm-duplicate.js#L33-L48) · [src/gtm-duplicate.js:49](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm-duplicate.js#L49-L57).

## gtm_list_users

Returns API response entity list/data. Calls Tag Manager API v2 accounts.user_permissions.list.

<details>
<summary>Full registered description</summary>

```text
Elenca tutti gli utenti con accesso a un account GTM e i loro permessi sui container.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `account_id` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "account_id": {
      "type": "string"
    }
  },
  "required": [
    "account_id"
  ]
}
```

</details>

- Dispatcher constructs OAuth client before handling this tool, including browser-only scan and local Looker URL generation; configured credentials file is required.

Source: [index.js:288](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L288-L298) · [index.js:727](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L727-L729) · [src/gtm.js:230](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm.js#L230-L237) · [src/gtm.js:3](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm.js#L3-L6).

## gtm_add_user

Creates GTM user permission with emailAddress, accountAccess.permission (default user), and containerAccess mapped from containerId/permission inputs.

<details>
<summary>Full registered description</summary>

```text
Aggiunge un utente a un account GTM con permessi specifici sui container.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `account_id` | Yes | string | Not declared |
| `email` | Yes | string | Not declared |
| `account_permission` | No | string | Not declared |
| `container_permissions` | No | array of object | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "account_id": {
      "type": "string"
    },
    "email": {
      "type": "string",
      "description": "Email Google dell'utente"
    },
    "account_permission": {
      "type": "string",
      "enum": [
        "user",
        "admin"
      ],
      "description": "Permesso account (default: user)"
    },
    "container_permissions": {
      "type": "array",
      "description": "Lista permessi per container",
      "items": {
        "type": "object",
        "properties": {
          "containerId": {
            "type": "string"
          },
          "permission": {
            "type": "string",
            "enum": [
              "no_access",
              "read",
              "edit",
              "approve",
              "publish"
            ]
          }
        }
      }
    }
  },
  "required": [
    "account_id",
    "email"
  ]
}
```

</details>

- Dispatcher constructs OAuth client before handling this tool, including browser-only scan and local Looker URL generation; configured credentials file is required.

Source: [index.js:299](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L299-L322) · [index.js:730](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L730-L732) · [src/gtm.js:238](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm.js#L238-L256) · [src/gtm.js:3](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm.js#L3-L6).

## gtm_update_user

Updates the identified GTM user permission using accountAccess.permission and mapped containerAccess inputs; omitted values become user and empty container list.

<details>
<summary>Full registered description</summary>

```text
Modifica i permessi di un utente esistente su un account GTM.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `account_id` | Yes | string | Not declared |
| `user_permission_id` | Yes | string | Not declared |
| `account_permission` | No | string | Not declared |
| `container_permissions` | No | array of object | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "account_id": {
      "type": "string"
    },
    "user_permission_id": {
      "type": "string",
      "description": "ID permesso utente (da gtm_list_users)"
    },
    "account_permission": {
      "type": "string",
      "enum": [
        "user",
        "admin"
      ]
    },
    "container_permissions": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "containerId": {
            "type": "string"
          },
          "permission": {
            "type": "string",
            "enum": [
              "no_access",
              "read",
              "edit",
              "approve",
              "publish"
            ]
          }
        }
      }
    }
  },
  "required": [
    "account_id",
    "user_permission_id"
  ]
}
```

</details>

- Dispatcher constructs OAuth client before handling this tool, including browser-only scan and local Looker URL generation; configured credentials file is required.
- Omitted account_permission defaults to user and omitted container_permissions becomes an empty list, rather than preserving current permissions.

Source: [index.js:323](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L323-L345) · [index.js:733](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L733-L735) · [src/gtm.js:257](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm.js#L257-L271) · [src/gtm.js:3](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm.js#L3-L6).

## gtm_remove_user

Performs the requested API mutation and returns response data or a deletion acknowledgement. Calls Tag Manager API v2 accounts.user_permissions.delete.

<details>
<summary>Full registered description</summary>

```text
Rimuove completamente l'accesso di un utente a un account GTM.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `account_id` | Yes | string | Not declared |
| `user_permission_id` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "account_id": {
      "type": "string"
    },
    "user_permission_id": {
      "type": "string",
      "description": "ID permesso utente (da gtm_list_users)"
    }
  },
  "required": [
    "account_id",
    "user_permission_id"
  ]
}
```

</details>

- Dispatcher constructs OAuth client before handling this tool, including browser-only scan and local Looker URL generation; configured credentials file is required.

Source: [index.js:346](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L346-L357) · [index.js:736](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L736-L740) · [src/gtm.js:272](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm.js#L272-L279) · [src/gtm.js:3](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm.js#L3-L6).

## gtm_publish_container

Resolves workspace, creates a container version and publishes that version.

<details>
<summary>Full registered description</summary>

```text
Pubblica il workspace GTM corrente creando una nuova versione.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `account_id` | Yes | string | Not declared |
| `container_id` | Yes | string | Not declared |
| `workspace_id` | No | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "account_id": {
      "type": "string"
    },
    "container_id": {
      "type": "string"
    },
    "workspace_id": {
      "type": "string",
      "description": "Opzionale — se omesso usa il Default Workspace"
    }
  },
  "required": [
    "account_id",
    "container_id"
  ]
}
```

</details>

- Dispatcher constructs OAuth client before handling this tool, including browser-only scan and local Looker URL generation; configured credentials file is required.
- Omitted workspace resolves cached Default Workspace by name or first workspace; no workspace causes an error.

Source: [index.js:358](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L358-L370) · [index.js:724](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L724-L726) · [src/gtm.js:214](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm.js#L214-L229) · [src/gtm.js:3](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm.js#L3-L6) · [src/gtm.js:31](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm.js#L31-L41) · [src/gtm.js:21](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm.js#L21-L30).

## scan_url

Launches Puppeteer Chromium, opens the URL, automatically accepts recognized cookie banners, observes requests and rendered HTML/JavaScript, and returns detected tags, evidence and extracted tracking IDs.

<details>
<summary>Full registered description</summary>

```text
Scansiona un URL con un browser reale e rileva tutti i tag attivi (analytics, advertising, CMP, live chat, ecc.) tramite analisi di rete, HTML e variabili JavaScript. Accetta automaticamente i cookie banner.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `url` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "url": {
      "type": "string",
      "description": "URL del sito da analizzare (es. https://www.esempio.it)"
    }
  },
  "required": [
    "url"
  ]
}
```

</details>

- Dispatcher constructs OAuth client before handling this tool, including browser-only scan and local Looker URL generation; configured credentials file is required.

Source: [index.js:373](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L373-L383) · [index.js:824](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L824-L826) · [src/tag-detector.js:249](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/tag-detector.js#L249-L301) · [src/tag-detector.js:87](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/tag-detector.js#L87-L94) · [src/tag-detector.js:80](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/tag-detector.js#L80-L86) · [src/tag-detector.js:95](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/tag-detector.js#L95-L109) · [src/tag-detector.js:110](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/tag-detector.js#L110-L122) · [src/tag-detector.js:123](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/tag-detector.js#L123-L135) · [src/tag-detector.js:136](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/tag-detector.js#L136-L148) · [src/tag-detector.js:149](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/tag-detector.js#L149-L182) · [src/tag-detector.js:183](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/tag-detector.js#L183-L248).

## create_tags_from_url

Scans the URL, creates a new GTM workspace and All Pages trigger, installs downloaded gallery templates as needed, and creates supported tags using extracted IDs; returns warnings for failed or unsupported configurations.

<details>
<summary>Full registered description</summary>

```text
Scansiona un URL, rileva i tag attivi, estrae gli ID configurati e crea automaticamente i tag corrispondenti in un nuovo workspace GTM. Usa template nativi per GA4/Google Ads e template gallery ufficiali per Meta (Stape), LinkedIn, Clarity, TikTok, Pinterest.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `url` | Yes | string | Not declared |
| `account_id` | Yes | string | Not declared |
| `container_id` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "url": {
      "type": "string",
      "description": "URL del sito da analizzare"
    },
    "account_id": {
      "type": "string"
    },
    "container_id": {
      "type": "string"
    }
  },
  "required": [
    "url",
    "account_id",
    "container_id"
  ]
}
```

</details>

- Dispatcher constructs OAuth client before handling this tool, including browser-only scan and local Looker URL generation; configured credentials file is required.
- Always writes to a newly created workspace; resolved existing workspace is not used for tag creation. Supports GA4, Ads, Meta, LinkedIn, Clarity, TikTok and Pinterest; templates are downloaded from GitHub main/master.

Source: [index.js:384](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L384-L396) · [index.js:821](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L821-L823) · [src/gtm-from-scan.js:217](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm-from-scan.js#L217-L326) · [src/gtm-from-scan.js:8](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm-from-scan.js#L8-L22) · [src/gtm-from-scan.js:151](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm-from-scan.js#L151-L166) · [src/gtm-from-scan.js:167](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm-from-scan.js#L167-L183) · [src/gtm-from-scan.js:184](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm-from-scan.js#L184-L216) · [src/gtm-from-scan.js:23](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm-from-scan.js#L23-L150) · [src/tag-detector.js:242](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/tag-detector.js#L242-L300).

## compare_url_with_container

Concurrently scans a browser page and lists GTM tags; returns both inventories and counts with an approximate-comparison note.

<details>
<summary>Full registered description</summary>

```text
Scansiona un URL e confronta i tag rilevati con quelli configurati in un container GTM. Identifica tag attivi sul sito, tag in GTM non rilevati sul sito, e tag sul sito non in GTM.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `url` | Yes | string | Not declared |
| `account_id` | Yes | string | Not declared |
| `container_id` | Yes | string | Not declared |
| `workspace_id` | No | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "url": {
      "type": "string",
      "description": "URL del sito da analizzare"
    },
    "account_id": {
      "type": "string"
    },
    "container_id": {
      "type": "string"
    },
    "workspace_id": {
      "type": "string",
      "description": "Opzionale"
    }
  },
  "required": [
    "url",
    "account_id",
    "container_id"
  ]
}
```

</details>

- Dispatcher constructs OAuth client before handling this tool, including browser-only scan and local Looker URL generation; configured credentials file is required.
- Description promises mismatched-tag identification, but handler only returns inventories/counts; computed detection/type maps are unused.

Source: [index.js:397](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L397-L410) · [index.js:827](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L827-L865) · [src/tag-detector.js:249](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/tag-detector.js#L249-L301) · [src/tag-detector.js:87](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/tag-detector.js#L87-L94) · [src/tag-detector.js:80](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/tag-detector.js#L80-L86) · [src/tag-detector.js:95](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/tag-detector.js#L95-L109) · [src/tag-detector.js:110](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/tag-detector.js#L110-L122) · [src/tag-detector.js:123](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/tag-detector.js#L123-L135) · [src/tag-detector.js:136](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/tag-detector.js#L136-L148) · [src/tag-detector.js:149](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/tag-detector.js#L149-L182) · [src/tag-detector.js:183](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/tag-detector.js#L183-L248) · [src/gtm.js:94](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm.js#L94-L102) · [src/gtm.js:3](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm.js#L3-L6) · [src/gtm.js:31](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm.js#L31-L41) · [src/gtm.js:21](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm.js#L21-L30).

## ga4_list_properties

Returns API response entity list/data. Calls Analytics Admin API v1beta accountSummaries.list.

<details>
<summary>Full registered description</summary>

```text
Elenca tutte le proprietà GA4 accessibili.
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

- Dispatcher constructs OAuth client before handling this tool, including browser-only scan and local Looker URL generation; configured credentials file is required.
- List calls do not iterate nextPageToken; returned results can be incomplete.

Source: [index.js:413](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L413-L417) · [index.js:741](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L741-L743) · [src/ga4.js:11](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/ga4.js#L11-L25) · [src/ga4.js:3](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/ga4.js#L3-L6).

## ga4_list_custom_dimensions

Returns API response entity list/data. Calls Analytics Admin API v1beta properties.customDimensions.list.

<details>
<summary>Full registered description</summary>

```text
Elenca le custom dimension di una proprietà GA4.
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
      "description": "ID proprietà GA4 (solo numero)"
    }
  },
  "required": [
    "property_id"
  ]
}
```

</details>

- Dispatcher constructs OAuth client before handling this tool, including browser-only scan and local Looker URL generation; configured credentials file is required.
- List calls do not iterate nextPageToken; returned results can be incomplete.

Source: [index.js:418](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L418-L426) · [index.js:744](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L744-L746) · [src/ga4.js:26](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/ga4.js#L26-L31) · [src/ga4.js:3](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/ga4.js#L3-L6).

## ga4_create_custom_dimension

Creates a GA4 custom dimension with supplied displayName, parameterName, scope and description (default empty string) under properties/{property_id}.

<details>
<summary>Full registered description</summary>

```text
Crea una custom dimension in una proprietà GA4.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |
| `display_name` | Yes | string | Not declared |
| `parameter_name` | Yes | string | Not declared |
| `scope` | Yes | string | Not declared |
| `description` | No | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "property_id": {
      "type": "string"
    },
    "display_name": {
      "type": "string"
    },
    "parameter_name": {
      "type": "string"
    },
    "scope": {
      "type": "string",
      "enum": [
        "EVENT",
        "USER",
        "ITEM"
      ]
    },
    "description": {
      "type": "string"
    }
  },
  "required": [
    "property_id",
    "display_name",
    "parameter_name",
    "scope"
  ]
}
```

</details>

- Dispatcher constructs OAuth client before handling this tool, including browser-only scan and local Looker URL generation; configured credentials file is required.

Source: [index.js:427](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L427-L441) · [index.js:747](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L747-L754) · [src/ga4.js:32](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/ga4.js#L32-L40) · [src/ga4.js:3](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/ga4.js#L3-L6).

## ga4_duplicate_custom_dimensions

Lists source custom dimensions and creates each in the target property, returning per-dimension successes and failures.

<details>
<summary>Full registered description</summary>

```text
Duplica tutte le custom dimension da una proprietà GA4 a un'altra.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `source_property_id` | Yes | string | Not declared |
| `target_property_id` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "source_property_id": {
      "type": "string"
    },
    "target_property_id": {
      "type": "string"
    }
  },
  "required": [
    "source_property_id",
    "target_property_id"
  ]
}
```

</details>

- Dispatcher constructs OAuth client before handling this tool, including browser-only scan and local Looker URL generation; configured credentials file is required.

Source: [index.js:442](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L442-L453) · [index.js:755](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L755-L757) · [src/ga4.js:67](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/ga4.js#L67-L87) · [src/ga4.js:26](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/ga4.js#L26-L31) · [src/ga4.js:3](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/ga4.js#L3-L6) · [src/ga4.js:32](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/ga4.js#L32-L40).

## ga4_list_custom_metrics

Returns API response entity list/data. Calls Analytics Admin API v1beta properties.customMetrics.list.

<details>
<summary>Full registered description</summary>

```text
Elenca le custom metric di una proprietà GA4.
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
      "type": "string"
    }
  },
  "required": [
    "property_id"
  ]
}
```

</details>

- Dispatcher constructs OAuth client before handling this tool, including browser-only scan and local Looker URL generation; configured credentials file is required.
- List calls do not iterate nextPageToken; returned results can be incomplete.

Source: [index.js:454](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L454-L462) · [index.js:758](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L758-L760) · [src/ga4.js:41](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/ga4.js#L41-L46) · [src/ga4.js:3](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/ga4.js#L3-L6).

## ga4_run_report

Wraps metric and dimension strings as name objects, supplies one date range and limit (falsy limit becomes 10), and returns properties.runReport response data.

<details>
<summary>Full registered description</summary>

```text
Esegue un report GA4 con metriche e dimensioni personalizzate.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |
| `metrics` | Yes | array of string | Not declared |
| `dimensions` | Yes | array of string | Not declared |
| `start_date` | Yes | string | Not declared |
| `end_date` | Yes | string | Not declared |
| `limit` | No | number | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "property_id": {
      "type": "string"
    },
    "metrics": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Es. [\"sessions\", \"activeUsers\"]"
    },
    "dimensions": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Es. [\"date\", \"deviceCategory\"]"
    },
    "start_date": {
      "type": "string",
      "description": "Es. \"7daysAgo\" o \"2024-01-01\""
    },
    "end_date": {
      "type": "string",
      "description": "Es. \"today\""
    },
    "limit": {
      "type": "number",
      "description": "Numero di righe (default 10)"
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

- Dispatcher constructs OAuth client before handling this tool, including browser-only scan and local Looker URL generation; configured credentials file is required.
- Schema has no numeric limit bounds or date format validation; dispatcher replaces a zero limit with 10.

Source: [index.js:463](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L463-L478) · [index.js:761](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L761-L768) · [src/ga4.js:47](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/ga4.js#L47-L60) · [src/ga4.js:7](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/ga4.js#L7-L10).

## ga4_list_conversion_events

Returns API response entity list/data. Calls Analytics Admin API v1beta properties.conversionEvents.list.

<details>
<summary>Full registered description</summary>

```text
Elenca gli eventi di conversione configurati in una proprietà GA4.
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
      "type": "string"
    }
  },
  "required": [
    "property_id"
  ]
}
```

</details>

- Dispatcher constructs OAuth client before handling this tool, including browser-only scan and local Looker URL generation; configured credentials file is required.
- List calls do not iterate nextPageToken; returned results can be incomplete.

Source: [index.js:479](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L479-L487) · [index.js:769](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L769-L771) · [src/ga4.js:61](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/ga4.js#L61-L66) · [src/ga4.js:3](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/ga4.js#L3-L6).

## ga4_list_data_streams

Returns API response entity list/data. Calls Analytics Admin API v1beta properties.dataStreams.list.

<details>
<summary>Full registered description</summary>

```text
Elenca i data stream (web/app) di una proprietà GA4 con measurement ID.
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
      "type": "string"
    }
  },
  "required": [
    "property_id"
  ]
}
```

</details>

- Dispatcher constructs OAuth client before handling this tool, including browser-only scan and local Looker URL generation; configured credentials file is required.
- List calls do not iterate nextPageToken; returned results can be incomplete.

Source: [index.js:488](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L488-L496) · [index.js:772](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L772-L774) · [src/ga4.js:88](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/ga4.js#L88-L95) · [src/ga4.js:3](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/ga4.js#L3-L6).

## ga4_list_audiences

Returns API response entity list/data. Calls Analytics Admin API v1beta properties.audiences.list.

<details>
<summary>Full registered description</summary>

```text
Elenca le audience configurate in una proprietà GA4.
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
      "type": "string"
    }
  },
  "required": [
    "property_id"
  ]
}
```

</details>

- Dispatcher constructs OAuth client before handling this tool, including browser-only scan and local Looker URL generation; configured credentials file is required.
- List calls do not iterate nextPageToken; returned results can be incomplete.

Source: [index.js:497](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L497-L505) · [index.js:775](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L775-L777) · [src/ga4.js:96](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/ga4.js#L96-L103) · [src/ga4.js:3](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/ga4.js#L3-L6).

## ga4_list_key_events

Returns API response entity list/data. Calls Analytics Admin API v1beta properties.keyEvents.list.

<details>
<summary>Full registered description</summary>

```text
Elenca i key event (ex conversioni) di una proprietà GA4.
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
      "type": "string"
    }
  },
  "required": [
    "property_id"
  ]
}
```

</details>

- Dispatcher constructs OAuth client before handling this tool, including browser-only scan and local Looker URL generation; configured credentials file is required.
- List calls do not iterate nextPageToken; returned results can be incomplete.

Source: [index.js:506](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L506-L514) · [index.js:778](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L778-L780) · [src/ga4.js:104](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/ga4.js#L104-L109) · [src/ga4.js:3](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/ga4.js#L3-L6).

## ga4_create_key_event

Creates a GA4 key event with requestBody.eventName under properties/{property_id}.

<details>
<summary>Full registered description</summary>

```text
Crea un key event in una proprietà GA4.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |
| `event_name` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "property_id": {
      "type": "string"
    },
    "event_name": {
      "type": "string",
      "description": "Nome esatto dell'evento GA4 da marcare come key event"
    }
  },
  "required": [
    "property_id",
    "event_name"
  ]
}
```

</details>

- Dispatcher constructs OAuth client before handling this tool, including browser-only scan and local Looker URL generation; configured credentials file is required.

Source: [index.js:515](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L515-L526) · [index.js:781](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L781-L783) · [src/ga4.js:110](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/ga4.js#L110-L120) · [src/ga4.js:3](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/ga4.js#L3-L6).

## ga4_compare_properties

Reads custom dimensions, custom metrics, key events and streams for both properties concurrently; compares parameter/event names and reports stream counts and summaries.

<details>
<summary>Full registered description</summary>

```text
Confronta custom dimension, custom metric, key event e data stream tra due proprietà GA4. Mostra cosa è presente solo in una, solo nell'altra, o in entrambe.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id_a` | Yes | string | Not declared |
| `property_id_b` | Yes | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "property_id_a": {
      "type": "string"
    },
    "property_id_b": {
      "type": "string"
    }
  },
  "required": [
    "property_id_a",
    "property_id_b"
  ]
}
```

</details>

- Dispatcher constructs OAuth client before handling this tool, including browser-only scan and local Looker URL generation; configured credentials file is required.

Source: [index.js:527](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L527-L538) · [index.js:784](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L784-L786) · [src/ga4.js:121](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/ga4.js#L121-L166) · [src/ga4.js:26](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/ga4.js#L26-L31) · [src/ga4.js:3](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/ga4.js#L3-L6) · [src/ga4.js:41](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/ga4.js#L41-L46) · [src/ga4.js:88](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/ga4.js#L88-L95) · [src/ga4.js:104](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/ga4.js#L104-L109).

## ga4_looker_report_url

Locally builds a Looker Studio create-report URL using a hard-coded template ID and GA4 property ID; no report is created by the server.

<details>
<summary>Full registered description</summary>

```text
Genera un URL per creare un report Looker Studio pre-connesso a una proprietà GA4. L'utente apre il link e il report è pronto.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `property_id` | Yes | string | Not declared |
| `template` | No | string | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "property_id": {
      "type": "string"
    },
    "template": {
      "type": "string",
      "enum": [
        "ga4_overview",
        "ga4_acquisition",
        "ga4_ecommerce",
        "ga4_engagement"
      ],
      "description": "Template report (default: ga4_overview)"
    }
  },
  "required": [
    "property_id"
  ]
}
```

</details>

- Dispatcher constructs OAuth client before handling this tool, including browser-only scan and local Looker URL generation; configured credentials file is required.
- Template IDs are fixed source constants and their external validity was not verified.

Source: [index.js:539](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L539-L554) · [index.js:787](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L787-L791) · [src/ga4.js:167](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/ga4.js#L167-L172).

## gtm_check_tag_health

Runs eventCount/eventName reports for 7daysAgo..today and 14daysAgo..8daysAgo, flags stopped/dropped predefined events, lists the default/first workspace and flags paused GTM tags.

<details>
<summary>Full registered description</summary>

```text
Verifica la salute dei tag GTM confrontando gli eventi GA4 degli ultimi 7 giorni con i 7 giorni precedenti. Segnala eventi fermi o calati oltre una soglia, e tag GTM in pausa.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `gtm_account_id` | Yes | string | Not declared |
| `gtm_container_id` | Yes | string | Not declared |
| `ga4_property_id` | Yes | string | Not declared |
| `drop_threshold` | No | number | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "gtm_account_id": {
      "type": "string"
    },
    "gtm_container_id": {
      "type": "string"
    },
    "ga4_property_id": {
      "type": "string",
      "description": "ID numerico proprietà GA4 (senza \"properties/\")"
    },
    "drop_threshold": {
      "type": "number",
      "description": "Soglia calo per alert (0.0-1.0, default 0.8 = 80%)"
    }
  },
  "required": [
    "gtm_account_id",
    "gtm_container_id",
    "ga4_property_id"
  ]
}
```

</details>

- Dispatcher constructs OAuth client before handling this tool, including browser-only scan and local Looker URL generation; configured credentials file is required.
- drop_threshold is not schema-bounded; zero is replaced with 0.8 by the handler.
- Scope is adjacent because this cross-service diagnostic reads both GA4 and GTM; it does not validate each GTM tag against an event.

Source: [index.js:557](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L557-L570) · [index.js:792](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L792-L798) · [src/gtm-health.js:50](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm-health.js#L50-L129) · [src/gtm-health.js:25](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm-health.js#L25-L28) · [src/gtm-health.js:29](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm-health.js#L29-L32) · [src/gtm-health.js:33](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/gtm-health.js#L33-L49).

## gsc_list_sites

Lists accessible Search Console site entries.

<details>
<summary>Full registered description</summary>

```text
Elenca tutti i siti verificati in Google Search Console.
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

- Dispatcher constructs OAuth client before handling this tool, including browser-only scan and local Looker URL generation; configured credentials file is required.

Source: [index.js:573](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L573-L577) · [index.js:799](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L799-L801) · [src/search-console.js:7](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/search-console.js#L7-L12) · [src/search-console.js:3](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/search-console.js#L3-L6).

## gsc_top_queries

Queries Search Console for query-dimension rows from today minus days to today, with the requested row limit; formats CTR and positions.

<details>
<summary>Full registered description</summary>

```text
Mostra le query di ricerca con più click per un sito.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `site_url` | Yes | string | Not declared |
| `days` | No | number | Not declared |
| `limit` | No | number | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "site_url": {
      "type": "string",
      "description": "URL sito (es. https://www.esempio.it/)"
    },
    "days": {
      "type": "number",
      "description": "Periodo in giorni (default 28)"
    },
    "limit": {
      "type": "number",
      "description": "Numero di query (default 25)"
    }
  },
  "required": [
    "site_url"
  ]
}
```

</details>

- Dispatcher constructs OAuth client before handling this tool, including browser-only scan and local Looker URL generation; configured credentials file is required.

Source: [index.js:578](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L578-L590) · [index.js:802](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L802-L804) · [src/search-console.js:32](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/search-console.js#L32-L44) · [src/search-console.js:13](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/search-console.js#L13-L31) · [src/search-console.js:3](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/search-console.js#L3-L6).

## gsc_top_pages

Queries Search Console for page-dimension rows from today minus days to today, with the requested row limit; formats CTR and positions.

<details>
<summary>Full registered description</summary>

```text
Mostra le pagine con più click organici per un sito.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `site_url` | Yes | string | Not declared |
| `days` | No | number | Not declared |
| `limit` | No | number | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "site_url": {
      "type": "string"
    },
    "days": {
      "type": "number",
      "description": "Periodo in giorni (default 28)"
    },
    "limit": {
      "type": "number",
      "description": "Numero di pagine (default 25)"
    }
  },
  "required": [
    "site_url"
  ]
}
```

</details>

- Dispatcher constructs OAuth client before handling this tool, including browser-only scan and local Looker URL generation; configured credentials file is required.

Source: [index.js:591](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L591-L603) · [index.js:805](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L805-L807) · [src/search-console.js:45](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/search-console.js#L45-L57) · [src/search-console.js:13](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/search-console.js#L13-L31) · [src/search-console.js:3](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/search-console.js#L3-L6).

## gsc_compare_periods

Queries up to 50 query rows in each of two date periods, joins previous results to current queries and returns click deltas and positions sorted by current clicks.

<details>
<summary>Full registered description</summary>

```text
Confronta click e posizioni di ricerca tra due periodi per identificare query in crescita o calo.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `site_url` | Yes | string | Not declared |
| `days` | No | number | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "site_url": {
      "type": "string"
    },
    "days": {
      "type": "number",
      "description": "Durata di ogni periodo in giorni (default 28)"
    }
  },
  "required": [
    "site_url"
  ]
}
```

</details>

- Dispatcher constructs OAuth client before handling this tool, including browser-only scan and local Looker URL generation; configured credentials file is required.

Source: [index.js:604](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L604-L615) · [index.js:808](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L808-L810) · [src/search-console.js:58](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/search-console.js#L58-L99) · [src/search-console.js:13](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/search-console.js#L13-L31) · [src/search-console.js:3](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/search-console.js#L3-L6).

## gsc_search_analytics

Forwards supplied date strings, dimensions (default query) and row limit (default 25) to searchanalytics.query; transforms CTR to percent and rounds positions.

<details>
<summary>Full registered description</summary>

```text
Esegui una query personalizzata su Search Console con dimensioni e filtri a scelta.
```

</details>

| Parameter | Required by schema | Type | Default |
| --- | --- | --- | --- |
| `site_url` | Yes | string | Not declared |
| `start_date` | Yes | string | Not declared |
| `end_date` | Yes | string | Not declared |
| `dimensions` | No | array of string | Not declared |
| `row_limit` | No | number | Not declared |

<details>
<summary>Full input schema: nested fields, descriptions and constraints</summary>

```json
{
  "type": "object",
  "properties": {
    "site_url": {
      "type": "string"
    },
    "start_date": {
      "type": "string",
      "description": "Es. 2025-01-01"
    },
    "end_date": {
      "type": "string",
      "description": "Es. 2025-01-31"
    },
    "dimensions": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Es. [\"query\",\"page\",\"device\",\"country\"]"
    },
    "row_limit": {
      "type": "number",
      "description": "Numero di righe (default 25)"
    }
  },
  "required": [
    "site_url",
    "start_date",
    "end_date"
  ]
}
```

</details>

- Dispatcher constructs OAuth client before handling this tool, including browser-only scan and local Looker URL generation; configured credentials file is required.
- Description mentions filters, but no filter property is exposed or passed by dispatcher; module-level dimensionFilterGroups support is unreachable through this tool.

Source: [index.js:616](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L616-L630) · [index.js:811](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/index.js#L811-L820) · [src/search-console.js:13](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/search-console.js#L13-L31) · [src/search-console.js:3](https://github.com/CreativeMetrics/gtm-ga4-mcp/blob/2f274468eaf7dcf3fbb9d29e1d997a83bd88b302/src/search-console.js#L3-L6).

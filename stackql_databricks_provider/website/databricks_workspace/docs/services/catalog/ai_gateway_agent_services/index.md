---
title: ai_gateway_agent_services
hide_title: false
hide_table_of_contents: false
keywords:
  - ai_gateway_agent_services
  - catalog
  - databricks_workspace
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage databricks_workspace resources using SQL
custom_edit_url: null
image: /img/stackql-databricks_workspace-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import SchemaTable from '@site/src/components/SchemaTable/SchemaTable';

Creates, updates, deletes, gets or lists an <code>ai_gateway_agent_services</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="ai_gateway_agent_services" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.catalog.ai_gateway_agent_services" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "Resource name of the agent service. Format: ``agent-services/&#123;catalog&#125;.&#123;schema&#125;.&#123;agent_service&#125;``. Each ``&#123;...&#125;`` component is capped at 255 characters individually. Server-derived on Create from ``parent`` + ``agent_service_id``; required and immutable on Update/Get/Delete."
  },
  {
    "name": "metastore_id",
    "type": "string",
    "description": "Metastore hosting the agent service."
  },
  {
    "name": "agent_service_type",
    "type": "string",
    "description": "Type of agent service. Required on create. Immutable after creation. For future internal / genie / app kinds, determines how the backing agent surface is provisioned. (AGENT_SERVICE_TYPE_EXTERNAL)"
  },
  {
    "name": "browse_only",
    "type": "boolean",
    "description": "Whether the caller sees only metadata available through the BROWSE privilege."
  },
  {
    "name": "comment",
    "type": "string",
    "description": "User-provided description."
  },
  {
    "name": "config",
    "type": "object",
    "description": "Operational configuration: connection, base_path, system_prompt, model_service, optional inference table, optional rate limits. Required on CreateAgentService; on UpdateAgentService it is required only when ``config`` (or a ``config.*`` subpath) appears in ``update_mask``.",
    "children": [
      {
        "name": "base_path",
        "type": "string",
        "description": "Vendor base path appended to the connection url at invocation time. Bedrock example: ``/agents/AGENT123/agentAliases/ALIAS1/sessions``. Empty when the agent platform does not require a per-agent suffix."
      },
      {
        "name": "inference_table",
        "type": "object",
        "description": "Inference table config for invocation payload logging. Reuses the shared InferenceTableConfig (same as ModelServiceConfig.inference_table).",
        "children": [
          {
            "name": "parent",
            "type": "string",
            "description": "Parent UC schema where the inference table is created. Format: ``schemas/&#123;catalog&#125;.&#123;schema&#125;``. Set at create time and immutable thereafter; changing it on an existing service is rejected."
          },
          {
            "name": "disabled",
            "type": "boolean",
            "description": "Indicates whether payload logging is disabled (opt-out). Unset means that payload logging is active (the on-by-default state coincides with the proto zero-value, so the server never fills this field for a client that leaves it unset). Set ``disabled = true`` to pause runtime logging while keeping the sub-message attached (preserving ``parent`` and ``table_name_prefix`` for a later flip back to active). ``parent`` remains required either way."
          },
          {
            "name": "is_deleted",
            "type": "boolean",
            "description": "True when the bound inference TABLE has been deleted but the parent service still references it. The dangling reference is surfaced (not silently dropped) so callers can see the broken dependency. AI Gateway payload logging fails closed in this state."
          },
          {
            "name": "table",
            "type": "string",
            "description": "Resolved UC table for payload logs. Format: ``tables/&#123;catalog&#125;.&#123;schema&#125;.&#123;table&#125;``."
          },
          {
            "name": "table_name_prefix",
            "type": "string",
            "description": "Prefix for the inference-table's UC-registered name. The actual leaf name UC stores is ``&lt;table_name_prefix&gt;_payload``; the ``_payload`` suffix is appended automatically. To find the actual UC table after Create, read the ``table`` field on the response. Defaults to ``&lt;model_service_name&gt;_payload`` when unset. Set at create time and immutable thereafter; changing it on an existing service is rejected."
          }
        ]
      },
      {
        "name": "model_service",
        "type": "string",
        "description": "Resource name of the model service backing this agent. Empty when the agent platform manages its own model selection (e.g. Bedrock Agents). Format: ``model-services/&#123;catalog&#125;.&#123;schema&#125;.&#123;model_service&#125;``."
      },
      {
        "name": "rate_limits",
        "type": "array",
        "description": "Per-principal rate limits applied to invocations routed through this agent service. Repeated to support per-USER / USER_GROUP / SERVICE_PRINCIPAL / SERVICE / USER_DEFAULT scopes simultaneously, mirroring McpServiceConfig.rate_limits. Empty when no rate limit is configured.",
        "children": [
          {
            "name": "key",
            "type": "string",
            "description": "Scope key. Determines whether ``principal`` is required. (RATE_LIMIT_KEY_REQUEST_TAG, RATE_LIMIT_KEY_SERVICE, RATE_LIMIT_KEY_SERVICE_PRINCIPAL, RATE_LIMIT_KEY_USER, RATE_LIMIT_KEY_USER_DEFAULT, RATE_LIMIT_KEY_USER_GROUP)"
          },
          {
            "name": "renewal_period",
            "type": "string",
            "description": "Renewal period. (RATE_LIMIT_RENEWAL_PERIOD_HOUR, RATE_LIMIT_RENEWAL_PERIOD_MINUTE)"
          },
          {
            "name": "principal",
            "type": "string",
            "description": "Principal this limit applies to: user email, group name, or service principal application ID. Required unless ``key`` is ``RATE_LIMIT_KEY_SERVICE``, ``RATE_LIMIT_KEY_USER_DEFAULT``, or ``RATE_LIMIT_KEY_REQUEST_TAG`` (which must not set a principal)."
          },
          {
            "name": "request_tag_key",
            "type": "string",
            "description": "Request tag key this limit applies to. Required when ``key`` is ``RATE_LIMIT_KEY_REQUEST_TAG``, forbidden otherwise."
          },
          {
            "name": "request_tag_value",
            "type": "string",
            "description": "Request tag value this limit applies to. Only valid when ``key`` is ``RATE_LIMIT_KEY_REQUEST_TAG``. Leave unset to apply the limit to every value of ``request_tag_key`` (an any-value default); a set value is a specific override for that value."
          },
          {
            "name": "requests",
            "type": "integer",
            "description": "Max requests allowed within a renewal period. Leave unset for no request limit."
          },
          {
            "name": "tokens",
            "type": "integer",
            "description": "Max tokens allowed within a renewal period. Leave unset for no token limit."
          }
        ]
      },
      {
        "name": "source_connection",
        "type": "object",
        "description": "External agent referenced via a UC Connection.",
        "children": [
          {
            "name": "name",
            "type": "string",
            "description": ""
          },
          {
            "name": "is_deleted",
            "type": "boolean",
            "description": ""
          }
        ]
      },
      {
        "name": "system_prompt",
        "type": "string",
        "description": "System prompt prepended to invocations. Max 8 KB."
      }
    ]
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": "When the agent service was created."
  },
  {
    "name": "created_by",
    "type": "string",
    "description": "Creator identity."
  },
  {
    "name": "effective_owner",
    "type": "string",
    "description": "The resolved owner of the agent service. Falls back to the caller's identity when ``owner`` is not explicitly set on creation."
  },
  {
    "name": "etag",
    "type": "string",
    "description": "Optimistic concurrency control token. Server-generated from the entity's state and returned on every read. To use it as an if-match precondition on a mutation, echo the last-read value back via the dedicated ``etag`` field on the Update / Delete request; the server rejects the mutation if the stored etag differs."
  },
  {
    "name": "owner",
    "type": "string",
    "description": "The owner of the agent service. Write-only; read owner via effective_owner."
  },
  {
    "name": "update_time",
    "type": "string (date-time)",
    "description": "When the agent service was last modified."
  },
  {
    "name": "updated_by",
    "type": "string",
    "description": "Identity of the last updater."
  }
]} />
</TabItem>
</Tabs>

## Methods

The following methods are available for this resource:

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
    <th>Optional Params</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-include_browse"><code>include_browse</code></a>, <a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a>, <a href="#parameter-parent"><code>parent</code></a></td>
    <td>Lists the agent services in a Unity Catalog schema. Provide ``parent`` as</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-parent"><code>parent</code></a>, <a href="#parameter-agent_service_id"><code>agent_service_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-agent_service"><code>agent_service</code></a></td>
    <td></td>
    <td>Creates an agent service in a Unity Catalog schema. An agent service is a governed securable that</td>
</tr>
</tbody>
</table>

## Parameters

Parameters can be passed in the `WHERE` clause of a query. Check the [Methods](#methods) section to see which parameters are required or optional for each operation.

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr id="parameter-agent_service_id">
    <td><CopyableCode code="agent_service_id" /></td>
    <td><code>string</code></td>
    <td>Leaf identifier for the agent service (the unqualified name within the parent schema, e.g. "support_agent").</td>
</tr>
<tr id="parameter-deployment_name">
    <td><CopyableCode code="deployment_name" /></td>
    <td><code>string</code></td>
    <td>The Databricks Workspace Deployment Name (default: dbc-abcd0123-a1bc)</td>
</tr>
<tr id="parameter-parent">
    <td><CopyableCode code="parent" /></td>
    <td><code>string</code></td>
    <td>Resource name of the parent schema. Format: ``schemas/&#123;catalog&#125;.&#123;schema&#125;``. Each ``&#123;...&#125;`` component is capped at 255 characters individually.</td>
</tr>
<tr id="parameter-include_browse">
    <td><CopyableCode code="include_browse" /></td>
    <td><code>boolean</code></td>
    <td>Whether to include agent services for which the principal can only access selective metadata.</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of agent services to return. Defaults to 100 when unset or 0; the maximum is 1000. Use ``next_page_token`` to retrieve additional pages.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Opaque pagination token from a previous request.</td>
</tr>
<tr id="parameter-parent">
    <td><CopyableCode code="parent" /></td>
    <td><code>string</code></td>
    <td>Resource name of the parent schema to list within, as ``schemas/&#123;catalog&#125;.&#123;schema&#125;``. Each ``&#123;...&#125;`` component is capped at 255 characters individually.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

Lists the agent services in a Unity Catalog schema. Provide ``parent`` as

```sql
SELECT
name,
metastore_id,
agent_service_type,
browse_only,
comment,
config,
create_time,
created_by,
effective_owner,
etag,
owner,
update_time,
updated_by
FROM databricks_workspace.catalog.ai_gateway_agent_services
WHERE deployment_name = '{{ deployment_name }}' -- required
AND include_browse = '{{ include_browse }}'
AND page_size = '{{ page_size }}'
AND page_token = '{{ page_token }}'
AND parent = '{{ parent }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Creates an agent service in a Unity Catalog schema. An agent service is a governed securable that

```sql
INSERT INTO databricks_workspace.catalog.ai_gateway_agent_services (
agent_service,
parent,
agent_service_id,
deployment_name
)
SELECT 
'{{ agent_service }}' /* required */,
'{{ parent }}',
'{{ agent_service_id }}',
'{{ deployment_name }}'
RETURNING
name,
metastore_id,
agent_service_type,
browse_only,
comment,
config,
create_time,
created_by,
effective_owner,
etag,
owner,
update_time,
updated_by
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: ai_gateway_agent_services
  props:
    - name: parent
      value: "{{ parent }}"
      description: Required parameter for the ai_gateway_agent_services resource.
    - name: agent_service_id
      value: "{{ agent_service_id }}"
      description: Required parameter for the ai_gateway_agent_services resource.
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the ai_gateway_agent_services resource.
    - name: agent_service
      description: |
        The agent service to create. The server populates \`\`name\`\` from \`\`parent\`\` + \`\`agent_service_id\`\`; clients should leave it unset.
      value:
        agent_service_type: "{{ agent_service_type }}"
        browse_only: {{ browse_only }}
        comment: "{{ comment }}"
        config:
          base_path: "{{ base_path }}"
          inference_table:
            parent: "{{ parent }}"
            disabled: {{ disabled }}
            is_deleted: {{ is_deleted }}
            table: "{{ table }}"
            table_name_prefix: "{{ table_name_prefix }}"
          model_service: "{{ model_service }}"
          rate_limits:
            - key: "{{ key }}"
              renewal_period: "{{ renewal_period }}"
              principal: "{{ principal }}"
              request_tag_key: "{{ request_tag_key }}"
              request_tag_value: "{{ request_tag_value }}"
              requests: {{ requests }}
              tokens: {{ tokens }}
          source_connection:
            name: "{{ name }}"
            is_deleted: {{ is_deleted }}
          system_prompt: "{{ system_prompt }}"
        create_time: "{{ create_time }}"
        created_by: "{{ created_by }}"
        effective_owner: "{{ effective_owner }}"
        etag: "{{ etag }}"
        metastore_id: "{{ metastore_id }}"
        name: "{{ name }}"
        owner: "{{ owner }}"
        update_time: "{{ update_time }}"
        updated_by: "{{ updated_by }}"
`}</CodeBlock>

</TabItem>
</Tabs>

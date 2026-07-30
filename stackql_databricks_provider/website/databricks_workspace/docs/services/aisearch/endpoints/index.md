---
title: endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - endpoints
  - aisearch
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

Creates, updates, deletes, gets or lists an <code>endpoints</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="endpoints" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.aisearch.endpoints" /></td></tr>
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
    "name": "id",
    "type": "string",
    "description": "Unique identifier of the endpoint"
  },
  {
    "name": "name",
    "type": "string",
    "description": "Name of the AI Search endpoint. Server-assigned full resource path (``workspaces/&#123;workspace&#125;/endpoints/&#123;endpoint&#125;``) on output. On create, the user-supplied short name is conveyed via ``CreateEndpointRequest.endpoint_id``; the server composes the full ``name`` and returns it on the response."
  },
  {
    "name": "budget_policy_id",
    "type": "string",
    "description": "The user-selected budget policy id for the endpoint."
  },
  {
    "name": "effective_budget_policy_id",
    "type": "string",
    "description": "The budget policy id applied to the endpoint"
  },
  {
    "name": "usage_policy_id",
    "type": "string",
    "description": "The usage policy id applied to the endpoint."
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": "Time the endpoint was created."
  },
  {
    "name": "creator",
    "type": "string",
    "description": "Creator of the endpoint"
  },
  {
    "name": "custom_tags",
    "type": "array",
    "description": "The custom tags assigned to the endpoint",
    "children": [
      {
        "name": "key",
        "type": "string",
        "description": "Key field for an AI Search endpoint tag."
      },
      {
        "name": "value",
        "type": "string",
        "description": "[Optional] Value field for an AI Search endpoint tag."
      }
    ]
  },
  {
    "name": "endpoint_status",
    "type": "object",
    "description": "Current status of the endpoint",
    "children": [
      {
        "name": "message",
        "type": "string",
        "description": "Human-readable detail about the endpoint's current state or the reason for a state transition."
      },
      {
        "name": "state",
        "type": "string",
        "description": "Current lifecycle state of the endpoint. See ``State`` for the meaning of each value. (DELETED, OFFLINE, ONLINE, PROVISIONING, RED_STATE, YELLOW_STATE)"
      }
    ]
  },
  {
    "name": "endpoint_type",
    "type": "string",
    "description": "Type of endpoint. Required on create and immutable thereafter. (STANDARD, STORAGE_OPTIMIZED)"
  },
  {
    "name": "index_count",
    "type": "integer",
    "description": "Number of indexes on the endpoint"
  },
  {
    "name": "last_updated_user",
    "type": "string",
    "description": "User who last updated the endpoint"
  },
  {
    "name": "replica_count",
    "type": "integer",
    "description": "The client-supplied desired number of replicas for the endpoint, applied at create/update time. Mutually exclusive with ``target_qps``."
  },
  {
    "name": "scaling_info",
    "type": "object",
    "description": "Scaling information for the endpoint",
    "children": [
      {
        "name": "requested_target_qps",
        "type": "integer",
        "description": "The requested QPS target for the endpoint. Best-effort; the system does not guarantee this QPS will be achieved."
      },
      {
        "name": "state",
        "type": "string",
        "description": "The current state of the scaling change request. (SCALING_CHANGE_APPLIED, SCALING_CHANGE_IN_PROGRESS, SCALING_CHANGE_UNSPECIFIED)"
      }
    ]
  },
  {
    "name": "target_qps",
    "type": "integer",
    "description": "Target QPS for the endpoint. Mutually exclusive with ``replica_count``. Best-effort; the system does not guarantee this QPS will be achieved."
  },
  {
    "name": "throughput_info",
    "type": "object",
    "description": "Throughput information for the endpoint",
    "children": [
      {
        "name": "change_request_message",
        "type": "string",
        "description": "Additional information about the throughput change request"
      },
      {
        "name": "change_request_state",
        "type": "string",
        "description": "The state of the most recent throughput change request (CHANGE_ADJUSTED, CHANGE_FAILED, CHANGE_IN_PROGRESS, CHANGE_REACHED_MAXIMUM, CHANGE_REACHED_MINIMUM, CHANGE_SUCCESS)"
      },
      {
        "name": "current_concurrency",
        "type": "number",
        "description": "The current concurrency (total CPU) allocated to the endpoint"
      },
      {
        "name": "current_concurrency_utilization_percentage",
        "type": "number",
        "description": "The current utilization of concurrency as a percentage (0-100)"
      },
      {
        "name": "current_num_replicas",
        "type": "integer",
        "description": "The current number of replicas allocated to the endpoint"
      },
      {
        "name": "maximum_concurrency_allowed",
        "type": "number",
        "description": "The maximum concurrency allowed for this endpoint"
      },
      {
        "name": "minimal_concurrency_allowed",
        "type": "number",
        "description": "The minimum concurrency allowed for this endpoint"
      },
      {
        "name": "requested_concurrency",
        "type": "number",
        "description": "The requested concurrency (total CPU) for the endpoint"
      },
      {
        "name": "requested_num_replicas",
        "type": "integer",
        "description": "The requested number of replicas for the endpoint"
      }
    ]
  },
  {
    "name": "update_time",
    "type": "string (date-time)",
    "description": "Time the endpoint was last updated."
  },
  {
    "name": "warnings",
    "type": "array",
    "description": "Advisory warnings surfaced when target_qps is set on a Standard endpoint.",
    "children": [
      {
        "name": "index_names",
        "type": "array",
        "description": "Indexes affected by this warning."
      },
      {
        "name": "message",
        "type": "string",
        "description": "Human-readable detail about the warning."
      },
      {
        "name": "status_code",
        "type": "string",
        "description": "Status code categorizing the warning. (ENDPOINT_HAS_INDEX_WITHOUT_OPTIMIZED_ROUTE, ENDPOINT_HAS_MANAGED_INDEX, RERANKER_TEMPORARILY_UNAVAILABLE)"
      }
    ]
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
    <td><a href="#parameter-parent"><code>parent</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>List AI Search endpoints in a workspace.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-parent"><code>parent</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-endpoint_id"><code>endpoint_id</code></a></td>
    <td>Create a new AI Search endpoint.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-update_mask"><code>update_mask</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Update an existing AI Search endpoint. Multi-bucket masks are supported and dispatched in</td>
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
<tr id="parameter-deployment_name">
    <td><CopyableCode code="deployment_name" /></td>
    <td><code>string</code></td>
    <td>The Databricks Workspace Deployment Name (default: dbc-abcd0123-a1bc)</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the AI Search endpoint. Server-assigned full resource path (``workspaces/&#123;workspace&#125;/endpoints/&#123;endpoint&#125;``) on output. On create, the user-supplied short name is conveyed via ``CreateEndpointRequest.endpoint_id``; the server composes the full ``name`` and returns it on the response.</td>
</tr>
<tr id="parameter-parent">
    <td><CopyableCode code="parent" /></td>
    <td><code>string</code></td>
    <td>The Workspace where this Endpoint will be created. Format: ``workspaces/&#123;workspace_id&#125;``</td>
</tr>
<tr id="parameter-update_mask">
    <td><CopyableCode code="update_mask" /></td>
    <td><code>object</code></td>
    <td>The list of fields to update.</td>
</tr>
<tr id="parameter-endpoint_id">
    <td><CopyableCode code="endpoint_id" /></td>
    <td><code>string</code></td>
    <td>The user-supplied short name for the Endpoint, per AIP-133. The server composes the full ``Endpoint.name`` as ``&#123;parent&#125;/endpoints/&#123;endpoint_id&#125;``. AIP-133 does not list ``endpoint_id`` as a fields-may-be-required entry, so we annotate it OPTIONAL on the wire; the server still rejects empty values with INVALID_PARAMETER_VALUE.</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>Best-effort upper bound on the number of results to return. Honored as an upper bound by the shim: ``page_size`` only narrows the legacy backend's response, never widens it, so the practical cap is ``min(page_size, legacy_fixed_page_size)``.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Page token from a previous response. If not provided, returns the first page.</td>
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

List AI Search endpoints in a workspace.

```sql
SELECT
id,
name,
budget_policy_id,
effective_budget_policy_id,
usage_policy_id,
create_time,
creator,
custom_tags,
endpoint_status,
endpoint_type,
index_count,
last_updated_user,
replica_count,
scaling_info,
target_qps,
throughput_info,
update_time,
warnings
FROM databricks_workspace.aisearch.endpoints
WHERE parent = '{{ parent }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND page_size = '{{ page_size }}'
AND page_token = '{{ page_token }}'
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

Create a new AI Search endpoint.

```sql
INSERT INTO databricks_workspace.aisearch.endpoints (
endpoint,
parent,
deployment_name,
endpoint_id
)
SELECT 
'{{ endpoint }}' /* required */,
'{{ parent }}',
'{{ deployment_name }}',
'{{ endpoint_id }}'
RETURNING
id,
name,
budget_policy_id,
effective_budget_policy_id,
usage_policy_id,
create_time,
creator,
custom_tags,
endpoint_status,
endpoint_type,
index_count,
last_updated_user,
replica_count,
scaling_info,
target_qps,
throughput_info,
update_time,
warnings
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: endpoints
  props:
    - name: parent
      value: "{{ parent }}"
      description: Required parameter for the endpoints resource.
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the endpoints resource.
    - name: endpoint
      description: |
        The Endpoint resource to create. Fields other than \`\`endpoint.name\`\` carry the desired configuration; \`\`endpoint.name\`\` is server-assigned from \`\`parent\`\` and \`\`endpoint_id\`\`.
      value:
        endpoint_type: "{{ endpoint_type }}"
        budget_policy_id: "{{ budget_policy_id }}"
        create_time: "{{ create_time }}"
        creator: "{{ creator }}"
        custom_tags:
          - key: "{{ key }}"
            value: "{{ value }}"
        effective_budget_policy_id: "{{ effective_budget_policy_id }}"
        endpoint_status:
          message: "{{ message }}"
          state: "{{ state }}"
        id: "{{ id }}"
        index_count: {{ index_count }}
        last_updated_user: "{{ last_updated_user }}"
        name: "{{ name }}"
        replica_count: {{ replica_count }}
        scaling_info:
          requested_target_qps: {{ requested_target_qps }}
          state: "{{ state }}"
        target_qps: {{ target_qps }}
        throughput_info:
          change_request_message: "{{ change_request_message }}"
          change_request_state: "{{ change_request_state }}"
          current_concurrency: {{ current_concurrency }}
          current_concurrency_utilization_percentage: {{ current_concurrency_utilization_percentage }}
          current_num_replicas: {{ current_num_replicas }}
          maximum_concurrency_allowed: {{ maximum_concurrency_allowed }}
          minimal_concurrency_allowed: {{ minimal_concurrency_allowed }}
          requested_concurrency: {{ requested_concurrency }}
          requested_num_replicas: {{ requested_num_replicas }}
        update_time: "{{ update_time }}"
        usage_policy_id: "{{ usage_policy_id }}"
        warnings:
          - index_names: "{{ index_names }}"
            message: "{{ message }}"
            status_code: "{{ status_code }}"
    - name: endpoint_id
      value: "{{ endpoint_id }}"
      description: The user-supplied short name for the Endpoint, per AIP-133. The server composes the full \`\`Endpoint.name\`\` as \`\`{parent}/endpoints/{endpoint_id}\`\`. AIP-133 does not list \`\`endpoint_id\`\` as a fields-may-be-required entry, so we annotate it OPTIONAL on the wire; the server still rejects empty values with INVALID_PARAMETER_VALUE.
      description: The user-supplied short name for the Endpoint, per AIP-133. The server composes the full \`\`Endpoint.name\`\` as \`\`{parent}/endpoints/{endpoint_id}\`\`. AIP-133 does not list \`\`endpoint_id\`\` as a fields-may-be-required entry, so we annotate it OPTIONAL on the wire; the server still rejects empty values with INVALID_PARAMETER_VALUE.
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

Update an existing AI Search endpoint. Multi-bucket masks are supported and dispatched in

```sql
UPDATE databricks_workspace.aisearch.endpoints
SET 
endpoint = '{{ endpoint }}'
WHERE 
name = '{{ name }}' --required
AND update_mask = '{{ update_mask }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND endpoint = '{{ endpoint }}' --required
RETURNING
id,
name,
budget_policy_id,
effective_budget_policy_id,
usage_policy_id,
create_time,
creator,
custom_tags,
endpoint_status,
endpoint_type,
index_count,
last_updated_user,
replica_count,
scaling_info,
target_qps,
throughput_info,
update_time,
warnings;
```
</TabItem>
</Tabs>

---
title: endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - endpoints
  - postgres
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
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.postgres.endpoints" /></td></tr>
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
    "description": "Output only. The full resource path of the endpoint. Format: projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;/endpoints/&#123;endpoint_id&#125;"
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": ""
  },
  {
    "name": "parent",
    "type": "string",
    "description": "The branch containing this endpoint (API resource hierarchy). Format: projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;"
  },
  {
    "name": "spec",
    "type": "object",
    "description": "The spec contains the compute endpoint configuration, including autoscaling limits, suspend timeout, and disabled state.",
    "children": [
      {
        "name": "endpoint_type",
        "type": "string",
        "description": "The compute endpoint type. Either `read_write` or `read_only`. (ENDPOINT_TYPE_READ_ONLY, ENDPOINT_TYPE_READ_WRITE)"
      },
      {
        "name": "autoscaling_limit_max_cu",
        "type": "number",
        "description": "The maximum number of Compute Units. Minimum value is 0.5."
      },
      {
        "name": "autoscaling_limit_min_cu",
        "type": "number",
        "description": "The minimum number of Compute Units. Minimum value is 0.5."
      },
      {
        "name": "disabled",
        "type": "boolean",
        "description": "Whether to restrict connections to the compute endpoint. Enabling this option schedules a suspend compute operation. A disabled compute endpoint cannot be enabled by a connection or console action."
      },
      {
        "name": "group",
        "type": "object",
        "description": "Settings for optional HA configuration of the endpoint. If unspecified, the endpoint defaults to non HA settings, with a single compute backing the endpoint (and no readable secondaries for Read/Write endpoints).",
        "children": [
          {
            "name": "min",
            "type": "integer",
            "description": ""
          },
          {
            "name": "max",
            "type": "integer",
            "description": "The maximum number of computes in the endpoint group. Currently, this must be equal to min. Set to 1 for single compute endpoints, to disable HA. To manually suspend all computes in an endpoint group, set disabled to true on the EndpointSpec."
          },
          {
            "name": "enable_readable_secondaries",
            "type": "boolean",
            "description": "Whether to allow read-only connections to read-write endpoints. Only relevant for read-write endpoints where size.max &gt; 1."
          }
        ]
      },
      {
        "name": "no_suspension",
        "type": "boolean",
        "description": "When set to true, explicitly disables automatic suspension (never suspend). Should be set to true when provided."
      },
      {
        "name": "settings",
        "type": "object",
        "description": "A collection of settings for a compute endpoint.",
        "children": [
          {
            "name": "pg_settings",
            "type": "object",
            "description": "A raw representation of Postgres settings."
          }
        ]
      },
      {
        "name": "suspend_timeout_duration",
        "type": "string",
        "description": "Duration of inactivity after which the compute endpoint is automatically suspended. If specified should be between 60s and 604800s (1 minute to 1 week)."
      }
    ]
  },
  {
    "name": "status",
    "type": "object",
    "description": "Current operational status of the compute endpoint.",
    "children": [
      {
        "name": "autoscaling_limit_max_cu",
        "type": "number",
        "description": ""
      },
      {
        "name": "autoscaling_limit_min_cu",
        "type": "number",
        "description": "The minimum number of Compute Units."
      },
      {
        "name": "current_state",
        "type": "string",
        "description": "The state of the compute endpoint. (ACTIVE, DEGRADED, IDLE, INIT)"
      },
      {
        "name": "disabled",
        "type": "boolean",
        "description": "Whether to restrict connections to the compute endpoint. Enabling this option schedules a suspend compute operation. A disabled compute endpoint cannot be enabled by a connection or console action."
      },
      {
        "name": "endpoint_type",
        "type": "string",
        "description": "The compute endpoint type. Either `read_write` or `read_only`. (ENDPOINT_TYPE_READ_ONLY, ENDPOINT_TYPE_READ_WRITE)"
      },
      {
        "name": "group",
        "type": "object",
        "description": "Details on the HA configuration of the endpoint.",
        "children": [
          {
            "name": "min",
            "type": "integer",
            "description": ""
          },
          {
            "name": "max",
            "type": "integer",
            "description": "The maximum number of computes in the endpoint group. Currently, this must be equal to min. Set to 1 for single compute endpoints, to disable HA. To manually suspend all computes in an endpoint group, set disabled to true on the EndpointSpec."
          },
          {
            "name": "enable_readable_secondaries",
            "type": "boolean",
            "description": "Whether read-only connections to read-write endpoints are allowed. Only relevant if read replicas are configured by specifying size.max &gt; 1."
          }
        ]
      },
      {
        "name": "hosts",
        "type": "object",
        "description": "Contains host information for connecting to the endpoint.",
        "children": [
          {
            "name": "host",
            "type": "string",
            "description": "The hostname to connect to this endpoint. For read-write endpoints, this is a read-write hostname which connects to the primary compute. For read-only endpoints, this is a read-only hostname which allows read-only operations."
          },
          {
            "name": "read_only_host",
            "type": "string",
            "description": "An optionally defined read-only host for the endpoint, without pooling. For read-only endpoints, this attribute is always defined and is equivalent to host. For read-write endpoints, this attribute is defined if the enclosing endpoint is a group with greater than 1 computes configured, and has readable secondaries enabled."
          }
        ]
      },
      {
        "name": "pending_state",
        "type": "string",
        "description": "The state of the compute endpoint. (ACTIVE, DEGRADED, IDLE, INIT)"
      },
      {
        "name": "settings",
        "type": "object",
        "description": "A collection of settings for a compute endpoint.",
        "children": [
          {
            "name": "pg_settings",
            "type": "object",
            "description": "A raw representation of Postgres settings."
          }
        ]
      },
      {
        "name": "suspend_timeout_duration",
        "type": "string",
        "description": "Duration of inactivity after which the compute endpoint is automatically suspended."
      }
    ]
  },
  {
    "name": "uid",
    "type": "string",
    "description": "System-generated unique ID for the endpoint."
  },
  {
    "name": "update_time",
    "type": "string (date-time)",
    "description": "A timestamp indicating when the compute endpoint was last updated."
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
    <td><a href="#parameter-project_id"><code>project_id</code></a>, <a href="#parameter-branch_id"><code>branch_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Returns a paginated list of compute endpoints in the branch.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-project_id"><code>project_id</code></a>, <a href="#parameter-branch_id"><code>branch_id</code></a>, <a href="#parameter-endpoint_id"><code>endpoint_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Creates a new compute endpoint in the branch.</td>
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
<tr id="parameter-branch_id">
    <td><CopyableCode code="branch_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of the branch where this Endpoint will be created. Format: projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;</td>
</tr>
<tr id="parameter-deployment_name">
    <td><CopyableCode code="deployment_name" /></td>
    <td><code>string</code></td>
    <td>The Databricks Workspace Deployment Name (default: dbc-abcd0123-a1bc)</td>
</tr>
<tr id="parameter-endpoint_id">
    <td><CopyableCode code="endpoint_id" /></td>
    <td><code>string</code></td>
    <td>The ID to use for the Endpoint. This becomes the final component of the endpoint's resource name. The ID is required and must be 1-63 characters long, start with a lowercase letter, and contain only lowercase letters, numbers, and hyphens. For example, `primary` becomes `projects/my-app/branches/development/endpoints/primary`.</td>
</tr>
<tr id="parameter-project_id">
    <td><CopyableCode code="project_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of the Postgres project. Format: projects/&#123;project_id&#125;</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>Upper bound for items returned. Cannot be negative.</td>
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

Returns a paginated list of compute endpoints in the branch.

```sql
SELECT
name,
create_time,
parent,
spec,
status,
uid,
update_time
FROM databricks_workspace.postgres.endpoints
WHERE project_id = '{{ project_id }}' -- required
AND branch_id = '{{ branch_id }}' -- required
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

Creates a new compute endpoint in the branch.

```sql
INSERT INTO databricks_workspace.postgres.endpoints (
endpoint,
project_id,
branch_id,
endpoint_id,
deployment_name
)
SELECT 
'{{ endpoint }}' /* required */,
'{{ project_id }}',
'{{ branch_id }}',
'{{ endpoint_id }}',
'{{ deployment_name }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: endpoints
  props:
    - name: project_id
      value: "{{ project_id }}"
      description: Required parameter for the endpoints resource.
    - name: branch_id
      value: "{{ branch_id }}"
      description: Required parameter for the endpoints resource.
    - name: endpoint_id
      value: "{{ endpoint_id }}"
      description: Required parameter for the endpoints resource.
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the endpoints resource.
    - name: endpoint
      description: |
        The Endpoint to create.
      value:
        create_time: "{{ create_time }}"
        name: "{{ name }}"
        parent: "{{ parent }}"
        spec:
          endpoint_type: "{{ endpoint_type }}"
          autoscaling_limit_max_cu: {{ autoscaling_limit_max_cu }}
          autoscaling_limit_min_cu: {{ autoscaling_limit_min_cu }}
          disabled: {{ disabled }}
          group:
            min: {{ min }}
            max: {{ max }}
            enable_readable_secondaries: {{ enable_readable_secondaries }}
          no_suspension: {{ no_suspension }}
          settings:
            pg_settings: "{{ pg_settings }}"
          suspend_timeout_duration: "{{ suspend_timeout_duration }}"
        status:
          autoscaling_limit_max_cu: {{ autoscaling_limit_max_cu }}
          autoscaling_limit_min_cu: {{ autoscaling_limit_min_cu }}
          current_state: "{{ current_state }}"
          disabled: {{ disabled }}
          endpoint_type: "{{ endpoint_type }}"
          group:
            min: {{ min }}
            max: {{ max }}
            enable_readable_secondaries: {{ enable_readable_secondaries }}
          hosts:
            host: "{{ host }}"
            read_only_host: "{{ read_only_host }}"
          pending_state: "{{ pending_state }}"
          settings:
            pg_settings: "{{ pg_settings }}"
          suspend_timeout_duration: "{{ suspend_timeout_duration }}"
        uid: "{{ uid }}"
        update_time: "{{ update_time }}"
`}</CodeBlock>

</TabItem>
</Tabs>

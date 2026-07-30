---
title: postgres_replication_group_previews
hide_title: false
hide_table_of_contents: false
keywords:
  - postgres_replication_group_previews
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

Creates, updates, deletes, gets or lists a <code>postgres_replication_group_previews</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="postgres_replication_group_previews" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.postgres.postgres_replication_group_previews" /></td></tr>
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
    "description": "The resource name of the replication group. Format: projects/&#123;project_id&#125;/preview/replication-groups/&#123;replication_group_id&#125;"
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": "Server-generated timestamps."
  },
  {
    "name": "etag",
    "type": "string",
    "description": "Optional optimistic concurrency token for update and delete."
  },
  {
    "name": "observed_metrics",
    "type": "object",
    "description": "The latest observed replication metrics for this group.",
    "children": [
      {
        "name": "as_of_time",
        "type": "string (date-time)",
        "description": ""
      },
      {
        "name": "bytes_lag",
        "type": "integer",
        "description": "The most recent observed byte lag."
      },
      {
        "name": "throughput_bytes_per_second",
        "type": "integer",
        "description": "The most recent observed replication throughput."
      },
      {
        "name": "time_lag",
        "type": "string",
        "description": "The most recent observed time lag."
      }
    ]
  },
  {
    "name": "parent",
    "type": "string",
    "description": "The parent project that owns this replication group. Format: projects/&#123;project_id&#125;"
  },
  {
    "name": "primary_workspace",
    "type": "string",
    "description": "The workspace currently serving writes. Server-owned."
  },
  {
    "name": "replication_mode",
    "type": "string",
    "description": "How changes are propagated from the primary workspace to its secondaries in a replication group:<br />on a fixed schedule or continuously as they occur. (REPLICATION_MODE_PREVIEW_LIVE, REPLICATION_MODE_PREVIEW_PERIODIC)"
  },
  {
    "name": "state",
    "type": "string",
    "description": "The lifecycle state of the replication group. (REPLICATION_GROUP_PREVIEW_STATE_DEGRADED, REPLICATION_GROUP_PREVIEW_STATE_DELETING, REPLICATION_GROUP_PREVIEW_STATE_FAILING_OVER, REPLICATION_GROUP_PREVIEW_STATE_PROVISIONING, REPLICATION_GROUP_PREVIEW_STATE_READY, REPLICATION_GROUP_PREVIEW_STATE_SWITCHING_OVER)"
  },
  {
    "name": "update_time",
    "type": "string (date-time)",
    "description": ""
  },
  {
    "name": "workspaces",
    "type": "array",
    "description": "The workspaces participating in this replication group. Phase 1 requires exactly 2 entries."
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
    <td>Returns a paginated list of replication groups for the project.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-parent"><code>parent</code></a>, <a href="#parameter-replication_group_preview_id"><code>replication_group_preview_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-replication_group_preview"><code>replication_group_preview</code></a></td>
    <td><a href="#parameter-request_id"><code>request_id</code></a></td>
    <td>Creates a new replication group for the project.</td>
</tr>
<tr>
    <td><a href="#failover"><CopyableCode code="failover" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-target_workspace"><code>target_workspace</code></a></td>
    <td></td>
    <td>Fails over the replication group to a target workspace, promoting the secondary to primary.</td>
</tr>
<tr>
    <td><a href="#switchover"><CopyableCode code="switchover" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-target_workspace"><code>target_workspace</code></a></td>
    <td></td>
    <td>Switches over the replication group to a target workspace with a coordinated failover.</td>
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
    <td></td>
</tr>
<tr id="parameter-parent">
    <td><CopyableCode code="parent" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-replication_group_preview_id">
    <td><CopyableCode code="replication_group_preview_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-request_id">
    <td><CopyableCode code="request_id" /></td>
    <td><code>string</code></td>
    <td></td>
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

Returns a paginated list of replication groups for the project.

```sql
SELECT
name,
create_time,
etag,
observed_metrics,
parent,
primary_workspace,
replication_mode,
state,
update_time,
workspaces
FROM databricks_workspace.postgres.postgres_replication_group_previews
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

Creates a new replication group for the project.

```sql
INSERT INTO databricks_workspace.postgres.postgres_replication_group_previews (
replication_group_preview,
parent,
replication_group_preview_id,
deployment_name,
request_id
)
SELECT 
'{{ replication_group_preview }}' /* required */,
'{{ parent }}',
'{{ replication_group_preview_id }}',
'{{ deployment_name }}',
'{{ request_id }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: postgres_replication_group_previews
  props:
    - name: parent
      value: "{{ parent }}"
      description: Required parameter for the postgres_replication_group_previews resource.
    - name: replication_group_preview_id
      value: "{{ replication_group_preview_id }}"
      description: Required parameter for the postgres_replication_group_previews resource.
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the postgres_replication_group_previews resource.
    - name: replication_group_preview
      value:
        replication_mode: "{{ replication_mode }}"
        workspaces:
          - "{{ workspaces }}"
        create_time: "{{ create_time }}"
        etag: "{{ etag }}"
        name: "{{ name }}"
        observed_metrics:
          as_of_time: "{{ as_of_time }}"
          bytes_lag: {{ bytes_lag }}
          throughput_bytes_per_second: {{ throughput_bytes_per_second }}
          time_lag: "{{ time_lag }}"
        parent: "{{ parent }}"
        primary_workspace: "{{ primary_workspace }}"
        state: "{{ state }}"
        update_time: "{{ update_time }}"
    - name: request_id
      value: "{{ request_id }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="failover"
    values={[
        { label: 'failover', value: 'failover' },
        { label: 'switchover', value: 'switchover' }
    ]}
>
<TabItem value="failover">

Fails over the replication group to a target workspace, promoting the secondary to primary.

```sql
EXEC databricks_workspace.postgres.postgres_replication_group_previews.failover 
@name='{{ name }}' --required, 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"target_workspace": "{{ target_workspace }}", 
"etag": "{{ etag }}", 
"request_id": "{{ request_id }}"
}'
;
```
</TabItem>
<TabItem value="switchover">

Switches over the replication group to a target workspace with a coordinated failover.

```sql
EXEC databricks_workspace.postgres.postgres_replication_group_previews.switchover 
@name='{{ name }}' --required, 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"target_workspace": "{{ target_workspace }}", 
"etag": "{{ etag }}", 
"request_id": "{{ request_id }}"
}'
;
```
</TabItem>
</Tabs>

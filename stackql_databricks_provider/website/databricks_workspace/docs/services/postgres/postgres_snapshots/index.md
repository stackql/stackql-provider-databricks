---
title: postgres_snapshots
hide_title: false
hide_table_of_contents: false
keywords:
  - postgres_snapshots
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

Creates, updates, deletes, gets or lists a <code>postgres_snapshots</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="postgres_snapshots" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.postgres.postgres_snapshots" /></td></tr>
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
    "description": "The resource name of the snapshot. Format: projects/&#123;project_id&#125;/snapshots/&#123;snapshot_id&#125;"
  },
  {
    "name": "snapshot_id",
    "type": "string",
    "description": "The user-chosen ID; the final segment of ``name``."
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": "When the snapshot was created."
  },
  {
    "name": "spec",
    "type": "object",
    "description": "Client-provided configuration of the snapshot.",
    "children": [
      {
        "name": "source_branch",
        "type": "string",
        "description": "The source branch to snapshot. Format: projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;"
      },
      {
        "name": "expire_time",
        "type": "string (date-time)",
        "description": "Absolute time at which the snapshot is deleted. Mutually exclusive with ``ttl`` and ``no_expiry``."
      },
      {
        "name": "no_expiry",
        "type": "boolean",
        "description": "If true, the snapshot never expires. Mutually exclusive with ``ttl`` and ``expire_time``."
      },
      {
        "name": "source_branch_lsn",
        "type": "string",
        "description": "LSN to snapshot from, e.g. ``16/B374D848``. Mutually exclusive with ``source_branch_time``."
      },
      {
        "name": "source_branch_time",
        "type": "string (date-time)",
        "description": "Timestamp to snapshot from. Mutually exclusive with ``source_branch_lsn``."
      },
      {
        "name": "ttl",
        "type": "string",
        "description": "Time-to-live. The snapshot expires this long after it is created. Mutually exclusive with ``expire_time`` and ``no_expiry``."
      }
    ]
  },
  {
    "name": "status",
    "type": "object",
    "description": "Server-observed state of the snapshot.",
    "children": [
      {
        "name": "current_state",
        "type": "string",
        "description": "The snapshot's current state. (AVAILABLE, CREATING, DELETING, FAILED)"
      },
      {
        "name": "diff_size_bytes",
        "type": "integer",
        "description": "Incremental storage size in bytes since the previous snapshot. Unset when the snapshot is not billed on incremental usage."
      },
      {
        "name": "expire_time",
        "type": "string (date-time)",
        "description": "Absolute time at which the snapshot is deleted."
      },
      {
        "name": "full_size_bytes",
        "type": "integer",
        "description": "Full logical size of the snapshot, in bytes."
      },
      {
        "name": "no_expiry",
        "type": "boolean",
        "description": "True if the snapshot never expires."
      },
      {
        "name": "source_branch",
        "type": "string",
        "description": "The source branch the snapshot was taken from. Format: projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;"
      },
      {
        "name": "source_branch_lsn",
        "type": "string",
        "description": "The LSN at which the snapshot was taken."
      },
      {
        "name": "source_branch_time",
        "type": "string (date-time)",
        "description": "The point in time at which the snapshot was taken."
      }
    ]
  },
  {
    "name": "uid",
    "type": "string",
    "description": "Unique system-generated ID for the snapshot."
  },
  {
    "name": "update_time",
    "type": "string (date-time)",
    "description": "When the snapshot was last updated."
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
    <td>Returns a paginated list of snapshots in the project.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-parent"><code>parent</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-snapshot"><code>snapshot</code></a></td>
    <td><a href="#parameter-snapshot_id"><code>snapshot_id</code></a></td>
    <td>Creates a snapshot, an immutable point-in-time copy of a branch's data, within the project.</td>
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
<tr id="parameter-parent">
    <td><CopyableCode code="parent" /></td>
    <td><code>string</code></td>
    <td>The project in which to create the snapshot. Format: projects/&#123;project_id&#125;</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of snapshots to return per page.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Page token from a previous response; omit for the first page.</td>
</tr>
<tr id="parameter-snapshot_id">
    <td><CopyableCode code="snapshot_id" /></td>
    <td><code>string</code></td>
    <td>Client-chosen ID for the snapshot. If omitted, the server generates one.</td>
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

Returns a paginated list of snapshots in the project.

```sql
SELECT
name,
snapshot_id,
create_time,
spec,
status,
uid,
update_time
FROM databricks_workspace.postgres.postgres_snapshots
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

Creates a snapshot, an immutable point-in-time copy of a branch's data, within the project.

```sql
INSERT INTO databricks_workspace.postgres.postgres_snapshots (
snapshot,
parent,
deployment_name,
snapshot_id
)
SELECT 
'{{ snapshot }}' /* required */,
'{{ parent }}',
'{{ deployment_name }}',
'{{ snapshot_id }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: postgres_snapshots
  props:
    - name: parent
      value: "{{ parent }}"
      description: Required parameter for the postgres_snapshots resource.
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the postgres_snapshots resource.
    - name: snapshot
      description: |
        The snapshot to create.
      value:
        create_time: "{{ create_time }}"
        name: "{{ name }}"
        snapshot_id: "{{ snapshot_id }}"
        spec:
          source_branch: "{{ source_branch }}"
          expire_time: "{{ expire_time }}"
          no_expiry: {{ no_expiry }}
          source_branch_lsn: "{{ source_branch_lsn }}"
          source_branch_time: "{{ source_branch_time }}"
          ttl: "{{ ttl }}"
        status:
          current_state: "{{ current_state }}"
          diff_size_bytes: {{ diff_size_bytes }}
          expire_time: "{{ expire_time }}"
          full_size_bytes: {{ full_size_bytes }}
          no_expiry: {{ no_expiry }}
          source_branch: "{{ source_branch }}"
          source_branch_lsn: "{{ source_branch_lsn }}"
          source_branch_time: "{{ source_branch_time }}"
        uid: "{{ uid }}"
        update_time: "{{ update_time }}"
    - name: snapshot_id
      value: "{{ snapshot_id }}"
      description: Client-chosen ID for the snapshot. If omitted, the server generates one.
      description: Client-chosen ID for the snapshot. If omitted, the server generates one.
`}</CodeBlock>

</TabItem>
</Tabs>

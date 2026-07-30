---
title: postgres_recovery_branch_previews
hide_title: false
hide_table_of_contents: false
keywords:
  - postgres_recovery_branch_previews
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

Creates, updates, deletes, gets or lists a <code>postgres_recovery_branch_previews</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="postgres_recovery_branch_previews" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.postgres.postgres_recovery_branch_previews" /></td></tr>
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
    "description": "The resource name of the recovery branch. Format: projects/&#123;project_id&#125;/preview/recovery-branches/&#123;recovery_branch_id&#125;"
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": ""
  },
  {
    "name": "parent",
    "type": "string",
    "description": "The project containing this recovery branch. Format: projects/&#123;project_id&#125;"
  },
  {
    "name": "status",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "current_state",
        "type": "string",
        "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (PENDING_HOME_SYNC, READY_FOR_INSPECTION, RECONCILED)"
      },
      {
        "name": "divergent",
        "type": "boolean",
        "description": ""
      },
      {
        "name": "end_lsn",
        "type": "string",
        "description": "The Log Sequence Number (LSN) up to which the recovery branch's timeline holds data."
      },
      {
        "name": "expire_time",
        "type": "string (date-time)",
        "description": ""
      },
      {
        "name": "failover_child_lsn",
        "type": "string",
        "description": "The Log Sequence Number (LSN) at which a local child timeline was branched off this recovery branch's timeline during recovery branch creation."
      },
      {
        "name": "home_workspace",
        "type": "string",
        "description": "The workspace that owns the source branch and where reconciliation completes. Format: a workspace identifier."
      },
      {
        "name": "is_foreign",
        "type": "boolean",
        "description": ""
      },
      {
        "name": "origin_branch",
        "type": "string",
        "description": "The normal branch from which this recovery branch originated. Format: projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;"
      }
    ]
  },
  {
    "name": "uid",
    "type": "string",
    "description": ""
  },
  {
    "name": "update_time",
    "type": "string (date-time)",
    "description": ""
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
    <td>Returns a paginated list of recovery branches for the project.</td>
</tr>
<tr>
    <td><a href="#inspect"><CopyableCode code="inspect" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-branch_id"><code>branch_id</code></a></td>
    <td></td>
    <td>Materializes a temporary inspection branch from the specified recovery branch for data examination.</td>
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
    <td>The recovery branch from which to create the inspection branch.</td>
</tr>
<tr id="parameter-parent">
    <td><CopyableCode code="parent" /></td>
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

Returns a paginated list of recovery branches for the project.

```sql
SELECT
name,
create_time,
parent,
status,
uid,
update_time
FROM databricks_workspace.postgres.postgres_recovery_branch_previews
WHERE parent = '{{ parent }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND page_size = '{{ page_size }}'
AND page_token = '{{ page_token }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="inspect"
    values={[
        { label: 'inspect', value: 'inspect' }
    ]}
>
<TabItem value="inspect">

Materializes a temporary inspection branch from the specified recovery branch for data examination.

```sql
EXEC databricks_workspace.postgres.postgres_recovery_branch_previews.inspect 
@name='{{ name }}' --required, 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"branch_id": "{{ branch_id }}", 
"request_id": "{{ request_id }}"
}'
;
```
</TabItem>
</Tabs>

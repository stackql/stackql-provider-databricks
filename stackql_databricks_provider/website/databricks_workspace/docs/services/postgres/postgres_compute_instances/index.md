---
title: postgres_compute_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - postgres_compute_instances
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

Creates, updates, deletes, gets or lists a <code>postgres_compute_instances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="postgres_compute_instances" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.postgres.postgres_compute_instances" /></td></tr>
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
    "description": ""
  },
  {
    "name": "compute_instance_id",
    "type": "string",
    "description": "The unique ID for this compute."
  },
  {
    "name": "compute_host",
    "type": "string",
    "description": "A host scoped directly to the enclosing compute. This host is guaranteed to resolve to the specific compute instance."
  },
  {
    "name": "current_state",
    "type": "string",
    "description": "The current state of the compute. (ACTIVE, IDLE, INIT)"
  },
  {
    "name": "pending_state",
    "type": "string",
    "description": "The desired pending state of the compute, if a state transition is in progress. (ACTIVE, IDLE, INIT)"
  },
  {
    "name": "role",
    "type": "string",
    "description": "The role of this compute within the endpoint. (HOT_STANDBY, READ_ONLY, READ_WRITE)"
  },
  {
    "name": "start_time",
    "type": "string (date-time)",
    "description": "A timestamp indicating when the compute was last started."
  },
  {
    "name": "suspend_time",
    "type": "string (date-time)",
    "description": "A timestamp indicating when the compute was last suspended."
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
    <td>Lists all compute instances that have been created under the specified endpoint. Note:</td>
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
    <td>The parent, which owns the compute instances.</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of compute instances to return. The service may return fewer than this value. If unspecified, at most 50 compute instances will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>A page token, received from a previous ``ListInstances`` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to ``ListInstances`` must match the call that provided the page token.</td>
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

Lists all compute instances that have been created under the specified endpoint. Note:

```sql
SELECT
name,
compute_instance_id,
compute_host,
current_state,
pending_state,
role,
start_time,
suspend_time
FROM databricks_workspace.postgres.postgres_compute_instances
WHERE parent = '{{ parent }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND page_size = '{{ page_size }}'
AND page_token = '{{ page_token }}'
;
```
</TabItem>
</Tabs>

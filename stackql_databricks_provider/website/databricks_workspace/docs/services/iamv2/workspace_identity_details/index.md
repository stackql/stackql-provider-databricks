---
title: workspace_identity_details
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_identity_details
  - iamv2
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

Creates, updates, deletes, gets or lists a <code>workspace_identity_details</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="workspace_identity_details" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.iamv2.workspace_identity_details" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

<SchemaTable fields={[
  {
    "name": "principal_id",
    "type": "integer",
    "description": "The internal ID of the principal (user/sp/group) in Databricks."
  },
  {
    "name": "assignment_type",
    "type": "string",
    "description": "The type of assignment the principal has to the workspace (direct or indirect). (DIRECT, INDIRECT)"
  },
  {
    "name": "principal_type",
    "type": "string",
    "description": "The type of the principal (user/sp/group). (GROUP, SERVICE_PRINCIPAL, USER)"
  },
  {
    "name": "workspace_identity_status",
    "type": "string",
    "description": "The activity status of an identity in a Databricks workspace. (ACTIVE, INACTIVE)"
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-principal_id"><code>principal_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Returns the identity details for a principal in a workspace.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-principal_id"><code>principal_id</code></a>, <a href="#parameter-update_mask"><code>update_mask</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_identity_detail"><code>workspace_identity_detail</code></a></td>
    <td></td>
    <td>Updates a workspace identity detail for a principal.</td>
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
<tr id="parameter-principal_id">
    <td><CopyableCode code="principal_id" /></td>
    <td><code>integer</code></td>
    <td>Required. ID of the principal in Databricks.</td>
</tr>
<tr id="parameter-update_mask">
    <td><CopyableCode code="update_mask" /></td>
    <td><code>object</code></td>
    <td>Required. The list of fields to update.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Returns the identity details for a principal in a workspace.

```sql
SELECT
principal_id,
assignment_type,
principal_type,
workspace_identity_status
FROM databricks_workspace.iamv2.workspace_identity_details
WHERE principal_id = '{{ principal_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
;
```
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

Updates a workspace identity detail for a principal.

```sql
UPDATE databricks_workspace.iamv2.workspace_identity_details
SET 
workspace_identity_detail = '{{ workspace_identity_detail }}'
WHERE 
principal_id = '{{ principal_id }}' --required
AND update_mask = '{{ update_mask }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND workspace_identity_detail = '{{ workspace_identity_detail }}' --required
RETURNING
principal_id,
assignment_type,
principal_type,
workspace_identity_status;
```
</TabItem>
</Tabs>

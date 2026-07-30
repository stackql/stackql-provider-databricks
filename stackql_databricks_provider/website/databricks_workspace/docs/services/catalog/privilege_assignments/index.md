---
title: privilege_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - privilege_assignments
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

Creates, updates, deletes, gets or lists a <code>privilege_assignments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="privilege_assignments" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.catalog.privilege_assignments" /></td></tr>
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
    "name": "principal_id",
    "type": "integer",
    "description": "Unique identifier of the principal. For active principals, both ``principal`` and ``principal_id`` are present."
  },
  {
    "name": "principal",
    "type": "string",
    "description": ""
  },
  {
    "name": "privileges",
    "type": "array",
    "description": "The privileges assigned to the principal."
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
    <td><a href="#parameter-securable_type"><code>securable_type</code></a>, <a href="#parameter-full_name"><code>full_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-include_deleted_principals"><code>include_deleted_principals</code></a>, <a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a>, <a href="#parameter-principal"><code>principal</code></a></td>
    <td>Lists the privilege assignments for a securable. Does not include inherited privileges. Paginated</td>
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
<tr id="parameter-full_name">
    <td><CopyableCode code="full_name" /></td>
    <td><code>string</code></td>
    <td>Full name of securable.</td>
</tr>
<tr id="parameter-securable_type">
    <td><CopyableCode code="securable_type" /></td>
    <td><code>string</code></td>
    <td>Type of securable.</td>
</tr>
<tr id="parameter-include_deleted_principals">
    <td><CopyableCode code="include_deleted_principals" /></td>
    <td><code>boolean</code></td>
    <td>Optional. If true, also return privilege assignments whose principals have been deleted.</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>Specifies the maximum number of privilege assignments to return (page length). Every PrivilegeAssignment present in a single page response is guaranteed to contain all the privileges granted on the requested Securable for the respective principal. If not set, page length is the server configured value. If set to - lesser than 0: invalid parameter error - 0: page length is set to a server configured value - lesser than 150 but greater than 0: invalid parameter error (this is to ensure that server is able to return at least one complete PrivilegeAssignment in a single page response) - greater than (or equal to) 150: page length is the minimum of this value and a server configured value</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Opaque pagination token to go to next page based on previous query.</td>
</tr>
<tr id="parameter-principal">
    <td><CopyableCode code="principal" /></td>
    <td><code>string</code></td>
    <td>If provided, only the permissions for the specified principal (user or group) are returned.</td>
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

Lists the privilege assignments for a securable. Does not include inherited privileges. Paginated

```sql
SELECT
principal_id,
principal,
privileges
FROM databricks_workspace.catalog.privilege_assignments
WHERE securable_type = '{{ securable_type }}' -- required
AND full_name = '{{ full_name }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND include_deleted_principals = '{{ include_deleted_principals }}'
AND page_size = '{{ page_size }}'
AND page_token = '{{ page_token }}'
AND principal = '{{ principal }}'
;
```
</TabItem>
</Tabs>

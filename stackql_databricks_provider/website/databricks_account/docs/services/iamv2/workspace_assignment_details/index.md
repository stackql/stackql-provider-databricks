---
title: workspace_assignment_details
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_assignment_details
  - iamv2
  - databricks_account
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage databricks_account resources using SQL
custom_edit_url: null
image: /img/stackql-databricks_account-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import SchemaTable from '@site/src/components/SchemaTable/SchemaTable';

Creates, updates, deletes, gets or lists a <code>workspace_assignment_details</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="workspace_assignment_details" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.iamv2.workspace_assignment_details" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

<SchemaTable fields={[
  {
    "name": "account_id",
    "type": "string",
    "description": "The account ID parent of the workspace where the principal is assigned"
  },
  {
    "name": "principal_id",
    "type": "integer",
    "description": "The internal ID of the principal (user/sp/group) in Databricks."
  },
  {
    "name": "workspace_id",
    "type": "integer",
    "description": "The workspace ID where the principal is assigned"
  },
  {
    "name": "effective_entitlements",
    "type": "array",
    "description": "The principal's full effective entitlements granted in this workspace: every entitlement it holds whether granted directly or via group membership. Populated on Get; empty on List."
  },
  {
    "name": "entitlements",
    "type": "array",
    "description": "Entitlements granted directly to the principal on this workspace. The only client-settable field: create and update manage exactly this set (including entitlements the principal also holds via a group). Not populated by ListWorkspaceAssignmentDetails (omitted for scalability); call GetWorkspaceAssignmentDetail to read the entitlements for a single principal."
  },
  {
    "name": "principal_type",
    "type": "string",
    "description": "The type of the principal (user/sp/group). (GROUP, SERVICE_PRINCIPAL, USER)"
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "account_id",
    "type": "string",
    "description": "The account ID parent of the workspace where the principal is assigned"
  },
  {
    "name": "principal_id",
    "type": "integer",
    "description": "The internal ID of the principal (user/sp/group) in Databricks."
  },
  {
    "name": "workspace_id",
    "type": "integer",
    "description": "The workspace ID where the principal is assigned"
  },
  {
    "name": "effective_entitlements",
    "type": "array",
    "description": "The principal's full effective entitlements granted in this workspace: every entitlement it holds whether granted directly or via group membership. Populated on Get; empty on List."
  },
  {
    "name": "entitlements",
    "type": "array",
    "description": "Entitlements granted directly to the principal on this workspace. The only client-settable field: create and update manage exactly this set (including entitlements the principal also holds via a group). Not populated by ListWorkspaceAssignmentDetails (omitted for scalability); call GetWorkspaceAssignmentDetail to read the entitlements for a single principal."
  },
  {
    "name": "principal_type",
    "type": "string",
    "description": "The type of the principal (user/sp/group). (GROUP, SERVICE_PRINCIPAL, USER)"
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-workspace_id"><code>workspace_id</code></a>, <a href="#parameter-principal_id"><code>principal_id</code></a></td>
    <td></td>
    <td>Returns the assignment details for a principal in a workspace.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-workspace_id"><code>workspace_id</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Lists workspace assignment details for a workspace. For scalability, the response omits the</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-workspace_id"><code>workspace_id</code></a>, <a href="#parameter-workspace_assignment_detail"><code>workspace_assignment_detail</code></a></td>
    <td></td>
    <td>Creates a workspace assignment detail for a principal. Entitlement grants are applied individually and</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-workspace_id"><code>workspace_id</code></a>, <a href="#parameter-principal_id"><code>principal_id</code></a>, <a href="#parameter-update_mask"><code>update_mask</code></a>, <a href="#parameter-workspace_assignment_detail"><code>workspace_assignment_detail</code></a></td>
    <td></td>
    <td>Updates the entitlements of a directly assigned principal in a workspace. Entitlement changes are</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-workspace_id"><code>workspace_id</code></a>, <a href="#parameter-principal_id"><code>principal_id</code></a></td>
    <td></td>
    <td>Deletes a workspace assignment detail for a principal, revoking all associated entitlements.</td>
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
<tr id="parameter-account_id">
    <td><CopyableCode code="account_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-principal_id">
    <td><CopyableCode code="principal_id" /></td>
    <td><code>integer</code></td>
    <td>Required. ID of the principal in Databricks to delete workspace assignment for.</td>
</tr>
<tr id="parameter-update_mask">
    <td><CopyableCode code="update_mask" /></td>
    <td><code>object</code></td>
    <td>Required. The list of fields to update.</td>
</tr>
<tr id="parameter-workspace_id">
    <td><CopyableCode code="workspace_id" /></td>
    <td><code>integer</code></td>
    <td>The workspace ID where the principal has access.</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of workspace assignment details to return. The service may return fewer than this value.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>A page token, received from a previous ListWorkspaceAssignmentDetails call. Provide this to retrieve the subsequent page.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Returns the assignment details for a principal in a workspace.

```sql
SELECT
account_id,
principal_id,
workspace_id,
effective_entitlements,
entitlements,
principal_type
FROM databricks_account.iamv2.workspace_assignment_details
WHERE account_id = '{{ account_id }}' -- required
AND workspace_id = '{{ workspace_id }}' -- required
AND principal_id = '{{ principal_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists workspace assignment details for a workspace. For scalability, the response omits the

```sql
SELECT
account_id,
principal_id,
workspace_id,
effective_entitlements,
entitlements,
principal_type
FROM databricks_account.iamv2.workspace_assignment_details
WHERE account_id = '{{ account_id }}' -- required
AND workspace_id = '{{ workspace_id }}' -- required
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

Creates a workspace assignment detail for a principal. Entitlement grants are applied individually and

```sql
INSERT INTO databricks_account.iamv2.workspace_assignment_details (
workspace_assignment_detail,
account_id,
workspace_id
)
SELECT 
'{{ workspace_assignment_detail }}' /* required */,
'{{ account_id }}',
'{{ workspace_id }}'
RETURNING
account_id,
principal_id,
workspace_id,
effective_entitlements,
entitlements,
principal_type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: workspace_assignment_details
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the workspace_assignment_details resource.
    - name: workspace_id
      value: {{ workspace_id }}
      description: Required parameter for the workspace_assignment_details resource.
    - name: workspace_assignment_detail
      description: |
        Required. Workspace assignment detail to be created in <Databricks>.
      value:
        principal_id: {{ principal_id }}
        account_id: "{{ account_id }}"
        effective_entitlements:
          - "{{ effective_entitlements }}"
        entitlements:
          - "{{ entitlements }}"
        principal_type: "{{ principal_type }}"
        workspace_id: {{ workspace_id }}
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

Updates the entitlements of a directly assigned principal in a workspace. Entitlement changes are

```sql
UPDATE databricks_account.iamv2.workspace_assignment_details
SET 
workspace_assignment_detail = '{{ workspace_assignment_detail }}'
WHERE 
account_id = '{{ account_id }}' --required
AND workspace_id = '{{ workspace_id }}' --required
AND principal_id = '{{ principal_id }}' --required
AND update_mask = '{{ update_mask }}' --required
AND workspace_assignment_detail = '{{ workspace_assignment_detail }}' --required
RETURNING
account_id,
principal_id,
workspace_id,
effective_entitlements,
entitlements,
principal_type;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Deletes a workspace assignment detail for a principal, revoking all associated entitlements.

```sql
DELETE FROM databricks_account.iamv2.workspace_assignment_details
WHERE account_id = '{{ account_id }}' --required
AND workspace_id = '{{ workspace_id }}' --required
AND principal_id = '{{ principal_id }}' --required
;
```
</TabItem>
</Tabs>

---
title: direct_group_members
hide_title: false
hide_table_of_contents: false
keywords:
  - direct_group_members
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

Creates, updates, deletes, gets or lists a <code>direct_group_members</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="direct_group_members" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.iamv2.direct_group_members" /></td></tr>
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
    "name": "external_id",
    "type": "string",
    "description": "The external ID of the principal in Databricks."
  },
  {
    "name": "principal_id",
    "type": "integer",
    "description": "Internal ID of the principal in Databricks."
  },
  {
    "name": "display_name",
    "type": "string",
    "description": "Display name of the principal."
  },
  {
    "name": "membership_source",
    "type": "string",
    "description": "The source of group membership (internal or from identity provider). (IDENTITY_PROVIDER, INTERNAL)"
  },
  {
    "name": "principal_type",
    "type": "string",
    "description": "The type of the principal (user/service principal/group). (GROUP, SERVICE_PRINCIPAL, USER)"
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "external_id",
    "type": "string",
    "description": "The external ID of the principal in Databricks."
  },
  {
    "name": "principal_id",
    "type": "integer",
    "description": "Internal ID of the principal in Databricks."
  },
  {
    "name": "display_name",
    "type": "string",
    "description": "Display name of the principal."
  },
  {
    "name": "membership_source",
    "type": "string",
    "description": "The source of group membership (internal or from identity provider). (IDENTITY_PROVIDER, INTERNAL)"
  },
  {
    "name": "principal_type",
    "type": "string",
    "description": "The type of the principal (user/service principal/group). (GROUP, SERVICE_PRINCIPAL, USER)"
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-group_id"><code>group_id</code></a>, <a href="#parameter-principal_id"><code>principal_id</code></a></td>
    <td></td>
    <td>Gets a provisioned direct member of a group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-group_id"><code>group_id</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Lists provisioned direct members of a group with their membership source (internal or from identity</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-group_id"><code>group_id</code></a>, <a href="#parameter-direct_group_member"><code>direct_group_member</code></a></td>
    <td></td>
    <td>Creates a group membership (assigns a principal to a group).</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-group_id"><code>group_id</code></a>, <a href="#parameter-principal_id"><code>principal_id</code></a></td>
    <td></td>
    <td>Deletes a group membership (unassigns a principal from a group).</td>
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
<tr id="parameter-group_id">
    <td><CopyableCode code="group_id" /></td>
    <td><code>integer</code></td>
    <td>Required. Internal ID of the group in Databricks.</td>
</tr>
<tr id="parameter-principal_id">
    <td><CopyableCode code="principal_id" /></td>
    <td><code>integer</code></td>
    <td>Required. Internal ID of the principal to be unassigned from the group.</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of members to return. The service may return fewer than this value. If not provided, defaults to 1000 (also the maximum allowed).</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>A page token, received from a previous ListDirectGroupMembers call. Provide this to retrieve the subsequent page.</td>
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

Gets a provisioned direct member of a group.

```sql
SELECT
external_id,
principal_id,
display_name,
membership_source,
principal_type
FROM databricks_account.iamv2.direct_group_members
WHERE account_id = '{{ account_id }}' -- required
AND group_id = '{{ group_id }}' -- required
AND principal_id = '{{ principal_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists provisioned direct members of a group with their membership source (internal or from identity

```sql
SELECT
external_id,
principal_id,
display_name,
membership_source,
principal_type
FROM databricks_account.iamv2.direct_group_members
WHERE account_id = '{{ account_id }}' -- required
AND group_id = '{{ group_id }}' -- required
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

Creates a group membership (assigns a principal to a group).

```sql
INSERT INTO databricks_account.iamv2.direct_group_members (
direct_group_member,
account_id,
group_id
)
SELECT 
'{{ direct_group_member }}' /* required */,
'{{ account_id }}',
'{{ group_id }}'
RETURNING
external_id,
principal_id,
display_name,
membership_source,
principal_type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: direct_group_members
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the direct_group_members resource.
    - name: group_id
      value: {{ group_id }}
      description: Required parameter for the direct_group_members resource.
    - name: direct_group_member
      description: |
        Required. The direct group member to be added to the group.
      value:
        principal_id: {{ principal_id }}
        display_name: "{{ display_name }}"
        external_id: "{{ external_id }}"
        membership_source: "{{ membership_source }}"
        principal_type: "{{ principal_type }}"
`}</CodeBlock>

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

Deletes a group membership (unassigns a principal from a group).

```sql
DELETE FROM databricks_account.iamv2.direct_group_members
WHERE account_id = '{{ account_id }}' --required
AND group_id = '{{ group_id }}' --required
AND principal_id = '{{ principal_id }}' --required
;
```
</TabItem>
</Tabs>

---
title: attribute_control_entries
hide_title: false
hide_table_of_contents: false
keywords:
  - attribute_control_entries
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

Creates, updates, deletes, gets or lists an <code>attribute_control_entries</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="attribute_control_entries" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.iamv2.attribute_control_entries" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' },
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "The resource name of the entry. Format: accounts/&#123;account_id&#125;/attribute-control-entries/&#123;attribute_name&#125; where &#123;attribute_name&#125; is the IdP attribute being governed (e.g. \"department\")."
  },
  {
    "name": "is_allowed",
    "type": "boolean",
    "description": "Whether the attribute is permitted. Always true in the Identity Attributes PrPr."
  }
]} />
</TabItem>
<TabItem value="get">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "The resource name of the entry. Format: accounts/&#123;account_id&#125;/attribute-control-entries/&#123;attribute_name&#125; where &#123;attribute_name&#125; is the IdP attribute being governed (e.g. \"department\")."
  },
  {
    "name": "is_allowed",
    "type": "boolean",
    "description": "Whether the attribute is permitted. Always true in the Identity Attributes PrPr."
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
    <td><a href="#parameter-parent"><code>parent</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Lists the identity attribute control-list entries for an account.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-name"><code>name</code></a></td>
    <td></td>
    <td>Gets an identity attribute control-list entry.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-parent"><code>parent</code></a>, <a href="#parameter-attribute_control_entry"><code>attribute_control_entry</code></a></td>
    <td><a href="#parameter-attribute_control_entry_id"><code>attribute_control_entry_id</code></a></td>
    <td>Creates (allows) an identity attribute control-list entry for an account.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-update_mask"><code>update_mask</code></a>, <a href="#parameter-attribute_control_entry"><code>attribute_control_entry</code></a></td>
    <td></td>
    <td>Updates an identity attribute control-list entry for an account.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-name"><code>name</code></a></td>
    <td></td>
    <td>Deletes an identity attribute control-list entry.</td>
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
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Required. The resource name of the entry to delete. Format: accounts/&#123;account_id&#125;/attribute-control-entries/&#123;attribute_name&#125;</td>
</tr>
<tr id="parameter-parent">
    <td><CopyableCode code="parent" /></td>
    <td><code>string</code></td>
    <td>Required. The account under which to create the entry. Format: accounts/&#123;account_id&#125;</td>
</tr>
<tr id="parameter-update_mask">
    <td><CopyableCode code="update_mask" /></td>
    <td><code>object</code></td>
    <td>Required. The fields to update. For the PrPr only is_allowed is mutable, so the backend currently applies the full entry regardless of the mask.</td>
</tr>
<tr id="parameter-attribute_control_entry_id">
    <td><CopyableCode code="attribute_control_entry_id" /></td>
    <td><code>string</code></td>
    <td>Optional. The ID to use for the entry, which becomes the last segment of its resource name: the IdP attribute being governed (e.g. "department").</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>Optional. The maximum number of entries to return.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Optional. A page token from a previous call, to retrieve the next page.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' },
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="list">

Lists the identity attribute control-list entries for an account.

```sql
SELECT
name,
is_allowed
FROM databricks_account.iamv2.attribute_control_entries
WHERE parent = '{{ parent }}' -- required
AND page_size = '{{ page_size }}'
AND page_token = '{{ page_token }}'
;
```
</TabItem>
<TabItem value="get">

Gets an identity attribute control-list entry.

```sql
SELECT
name,
is_allowed
FROM databricks_account.iamv2.attribute_control_entries
WHERE name = '{{ name }}' -- required
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

Creates (allows) an identity attribute control-list entry for an account.

```sql
INSERT INTO databricks_account.iamv2.attribute_control_entries (
attribute_control_entry,
parent,
attribute_control_entry_id
)
SELECT 
'{{ attribute_control_entry }}' /* required */,
'{{ parent }}',
'{{ attribute_control_entry_id }}'
RETURNING
name,
is_allowed
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: attribute_control_entries
  props:
    - name: parent
      value: "{{ parent }}"
      description: Required parameter for the attribute_control_entries resource.
    - name: attribute_control_entry
      description: |
        Required. The entry to create.
      value:
        is_allowed: {{ is_allowed }}
        name: "{{ name }}"
    - name: attribute_control_entry_id
      value: "{{ attribute_control_entry_id }}"
      description: Optional. The ID to use for the entry, which becomes the last segment of its resource name: the IdP attribute being governed (e.g. "department").
      description: Optional. The ID to use for the entry, which becomes the last segment of its resource name: the IdP attribute being governed (e.g. "department").
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

Updates an identity attribute control-list entry for an account.

```sql
UPDATE databricks_account.iamv2.attribute_control_entries
SET 
attribute_control_entry = '{{ attribute_control_entry }}'
WHERE 
name = '{{ name }}' --required
AND update_mask = '{{ update_mask }}' --required
AND attribute_control_entry = '{{ attribute_control_entry }}' --required
RETURNING
name,
is_allowed;
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

Deletes an identity attribute control-list entry.

```sql
DELETE FROM databricks_account.iamv2.attribute_control_entries
WHERE name = '{{ name }}' --required
;
```
</TabItem>
</Tabs>

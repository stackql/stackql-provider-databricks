---
title: users
hide_title: false
hide_table_of_contents: false
keywords:
  - users
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

Creates, updates, deletes, gets or lists a <code>users</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="users" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.iamv2.users" /></td></tr>
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
    "description": "The accountId parent of the user in Databricks."
  },
  {
    "name": "external_id",
    "type": "string",
    "description": "ExternalId of the user in the customer's IdP."
  },
  {
    "name": "internal_id",
    "type": "string",
    "description": "Internal userId of the user in Databricks."
  },
  {
    "name": "full_name",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "family_name",
        "type": "string",
        "description": ""
      },
      {
        "name": "given_name",
        "type": "string",
        "description": ""
      }
    ]
  },
  {
    "name": "account_user_status",
    "type": "string",
    "description": "The activity status of a user in a Databricks account. (ACTIVE, INACTIVE)"
  },
  {
    "name": "username",
    "type": "string",
    "description": "Username/email of the user."
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "account_id",
    "type": "string",
    "description": "The accountId parent of the user in Databricks."
  },
  {
    "name": "external_id",
    "type": "string",
    "description": "ExternalId of the user in the customer's IdP."
  },
  {
    "name": "internal_id",
    "type": "string",
    "description": "Internal userId of the user in Databricks."
  },
  {
    "name": "full_name",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "family_name",
        "type": "string",
        "description": ""
      },
      {
        "name": "given_name",
        "type": "string",
        "description": ""
      }
    ]
  },
  {
    "name": "account_user_status",
    "type": "string",
    "description": "The activity status of a user in a Databricks account. (ACTIVE, INACTIVE)"
  },
  {
    "name": "username",
    "type": "string",
    "description": "Username/email of the user."
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-internal_id"><code>internal_id</code></a></td>
    <td></td>
    <td>Fetches a user from the Databricks account by its internal ID.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-filter"><code>filter</code></a>, <a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Lists the users in the Databricks account, returning one page per call. Supports filtering by username</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-user"><code>user</code></a></td>
    <td></td>
    <td>Creates a user in the Databricks account and returns the resulting User resource. Behavior depends on</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-internal_id"><code>internal_id</code></a>, <a href="#parameter-update_mask"><code>update_mask</code></a>, <a href="#parameter-user"><code>user</code></a></td>
    <td></td>
    <td>Updates an existing user in the Databricks account, returning the updated User resource. The behavior</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-internal_id"><code>internal_id</code></a></td>
    <td></td>
    <td>Deletes a user from the Databricks account by its internal ID.</td>
</tr>
<tr>
    <td><a href="#resolve"><CopyableCode code="resolve" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-external_id"><code>external_id</code></a></td>
    <td></td>
    <td>Resolves a user with the given external ID from the customer's IdP. If the user does not exist, it</td>
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
<tr id="parameter-internal_id">
    <td><CopyableCode code="internal_id" /></td>
    <td><code>string</code></td>
    <td>Required. Internal ID of the user in Databricks.</td>
</tr>
<tr id="parameter-update_mask">
    <td><CopyableCode code="update_mask" /></td>
    <td><code>string</code></td>
    <td>Optional. The list of fields to update.</td>
</tr>
<tr id="parameter-filter">
    <td><CopyableCode code="filter" /></td>
    <td><code>string</code></td>
    <td>Optional. Allows filtering users by username or external id.</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of users to return. The service may return fewer than this value.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>A page token, received from a previous ListUsers call. Provide this to retrieve the subsequent page.</td>
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

Fetches a user from the Databricks account by its internal ID.

```sql
SELECT
account_id,
external_id,
internal_id,
full_name,
account_user_status,
username
FROM databricks_account.iamv2.users
WHERE account_id = '{{ account_id }}' -- required
AND internal_id = '{{ internal_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists the users in the Databricks account, returning one page per call. Supports filtering by username

```sql
SELECT
account_id,
external_id,
internal_id,
full_name,
account_user_status,
username
FROM databricks_account.iamv2.users
WHERE account_id = '{{ account_id }}' -- required
AND filter = '{{ filter }}'
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

Creates a user in the Databricks account and returns the resulting User resource. Behavior depends on

```sql
INSERT INTO databricks_account.iamv2.users (
user,
account_id
)
SELECT 
'{{ user }}' /* required */,
'{{ account_id }}'
RETURNING
account_id,
external_id,
internal_id,
full_name,
account_user_status,
username
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: users
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the users resource.
    - name: user
      description: |
        Required. User to be created in <Databricks>
      value:
        account_id: "{{ account_id }}"
        account_user_status: "{{ account_user_status }}"
        external_id: "{{ external_id }}"
        full_name:
          family_name: "{{ family_name }}"
          given_name: "{{ given_name }}"
        internal_id: "{{ internal_id }}"
        username: "{{ username }}"
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

Updates an existing user in the Databricks account, returning the updated User resource. The behavior

```sql
UPDATE databricks_account.iamv2.users
SET 
user = '{{ user }}'
WHERE 
account_id = '{{ account_id }}' --required
AND internal_id = '{{ internal_id }}' --required
AND update_mask = '{{ update_mask }}' --required
AND user = '{{ user }}' --required
RETURNING
account_id,
external_id,
internal_id,
full_name,
account_user_status,
username;
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

Deletes a user from the Databricks account by its internal ID.

```sql
DELETE FROM databricks_account.iamv2.users
WHERE account_id = '{{ account_id }}' --required
AND internal_id = '{{ internal_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="resolve"
    values={[
        { label: 'resolve', value: 'resolve' }
    ]}
>
<TabItem value="resolve">

Resolves a user with the given external ID from the customer's IdP. If the user does not exist, it

```sql
EXEC databricks_account.iamv2.users.resolve 
@account_id='{{ account_id }}' --required 
@@json=
'{
"external_id": "{{ external_id }}"
}'
;
```
</TabItem>
</Tabs>

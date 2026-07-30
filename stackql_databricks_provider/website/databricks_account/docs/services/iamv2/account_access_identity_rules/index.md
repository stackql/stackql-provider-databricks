---
title: account_access_identity_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - account_access_identity_rules
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

Creates, updates, deletes, gets or lists an <code>account_access_identity_rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="account_access_identity_rules" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.iamv2.account_access_identity_rules" /></td></tr>
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
    "name": "name",
    "type": "string",
    "description": "Fully qualified name for the rule. Format: accounts/&#123;account_id&#125;/account-access-identity-rules/&#123;external_principal_id&#125;"
  },
  {
    "name": "external_principal_id",
    "type": "string",
    "description": "External ID of the principal in the customer's IdP."
  },
  {
    "name": "display_name",
    "type": "string",
    "description": "Display name of the principal."
  },
  {
    "name": "action",
    "type": "string",
    "description": "Currently, only DENY action is supported. (DENY)"
  },
  {
    "name": "principal_type",
    "type": "string",
    "description": "The type of the principal (user/service principal/group). This field is populated by the server based on the external_principal_id. (GROUP, SERVICE_PRINCIPAL, USER)"
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "Fully qualified name for the rule. Format: accounts/&#123;account_id&#125;/account-access-identity-rules/&#123;external_principal_id&#125;"
  },
  {
    "name": "external_principal_id",
    "type": "string",
    "description": "External ID of the principal in the customer's IdP."
  },
  {
    "name": "display_name",
    "type": "string",
    "description": "Display name of the principal."
  },
  {
    "name": "action",
    "type": "string",
    "description": "Currently, only DENY action is supported. (DENY)"
  },
  {
    "name": "principal_type",
    "type": "string",
    "description": "The type of the principal (user/service principal/group). This field is populated by the server based on the external_principal_id. (GROUP, SERVICE_PRINCIPAL, USER)"
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
    <td><a href="#parameter-parent"><code>parent</code></a>, <a href="#parameter-external_principal_id"><code>external_principal_id</code></a></td>
    <td></td>
    <td>Gets an account access identity rule for a given principal.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-parent"><code>parent</code></a></td>
    <td><a href="#parameter-filter"><code>filter</code></a>, <a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Lists all account access identity rules for a given account. These rules control which principals</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-parent"><code>parent</code></a>, <a href="#parameter-external_principal_id"><code>external_principal_id</code></a>, <a href="#parameter-account_access_identity_rule"><code>account_access_identity_rule</code></a></td>
    <td></td>
    <td>Creates a new account access identity rule for a given account. This allows administrators to</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-parent"><code>parent</code></a>, <a href="#parameter-external_principal_id"><code>external_principal_id</code></a></td>
    <td></td>
    <td>Deletes an account access identity rule for a given principal.</td>
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
<tr id="parameter-external_principal_id">
    <td><CopyableCode code="external_principal_id" /></td>
    <td><code>string</code></td>
    <td>Required. The external ID of the principal whose rule should be deleted.</td>
</tr>
<tr id="parameter-parent">
    <td><CopyableCode code="parent" /></td>
    <td><code>string</code></td>
    <td>Required. The account for which to delete the rule. Format: accounts/&#123;account_id&#125;</td>
</tr>
<tr id="parameter-filter">
    <td><CopyableCode code="filter" /></td>
    <td><code>string</code></td>
    <td>Optional. Filter to apply to the list. Supports filtering by displayName.</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>Optional. The maximum number of rules to return. The service may return fewer than this value.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Optional. A page token, received from a previous call. Provide this to retrieve the subsequent page.</td>
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

Gets an account access identity rule for a given principal.

```sql
SELECT
name,
external_principal_id,
display_name,
action,
principal_type
FROM databricks_account.iamv2.account_access_identity_rules
WHERE parent = '{{ parent }}' -- required
AND external_principal_id = '{{ external_principal_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all account access identity rules for a given account. These rules control which principals

```sql
SELECT
name,
external_principal_id,
display_name,
action,
principal_type
FROM databricks_account.iamv2.account_access_identity_rules
WHERE parent = '{{ parent }}' -- required
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

Creates a new account access identity rule for a given account. This allows administrators to

```sql
INSERT INTO databricks_account.iamv2.account_access_identity_rules (
account_access_identity_rule,
parent,
external_principal_id
)
SELECT 
'{{ account_access_identity_rule }}' /* required */,
'{{ parent }}',
'{{ external_principal_id }}'
RETURNING
name,
external_principal_id,
display_name,
action,
principal_type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: account_access_identity_rules
  props:
    - name: parent
      value: "{{ parent }}"
      description: Required parameter for the account_access_identity_rules resource.
    - name: external_principal_id
      value: "{{ external_principal_id }}"
      description: Required parameter for the account_access_identity_rules resource.
    - name: account_access_identity_rule
      description: |
        Required. The rule to create.
      value:
        action: "{{ action }}"
        display_name: "{{ display_name }}"
        external_principal_id: "{{ external_principal_id }}"
        name: "{{ name }}"
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

Deletes an account access identity rule for a given principal.

```sql
DELETE FROM databricks_account.iamv2.account_access_identity_rules
WHERE parent = '{{ parent }}' --required
AND external_principal_id = '{{ external_principal_id }}' --required
;
```
</TabItem>
</Tabs>

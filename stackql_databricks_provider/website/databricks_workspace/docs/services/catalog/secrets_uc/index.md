---
title: secrets_uc
hide_title: false
hide_table_of_contents: false
keywords:
  - secrets_uc
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

Creates, updates, deletes, gets or lists a <code>secrets_uc</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="secrets_uc" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.catalog.secrets_uc" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="secrets_uc_get_secret"
    values={[
        { label: 'secrets_uc_get_secret', value: 'secrets_uc_get_secret' },
        { label: 'secrets_uc_list_secrets', value: 'secrets_uc_list_secrets' }
    ]}
>
<TabItem value="secrets_uc_get_secret">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "The name of the secret, relative to its parent schema."
  },
  {
    "name": "metastore_id",
    "type": "string",
    "description": "Unique identifier of the metastore hosting the secret."
  },
  {
    "name": "catalog_name",
    "type": "string",
    "description": "The name of the catalog where the schema and the secret reside."
  },
  {
    "name": "full_name",
    "type": "string",
    "description": "The three-level (fully qualified) name of the secret, in the form of **catalog_name.schema_name.secret_name**."
  },
  {
    "name": "schema_name",
    "type": "string",
    "description": "The name of the schema where the secret resides."
  },
  {
    "name": "comment",
    "type": "string",
    "description": "User-provided free-form text description of the secret."
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": "The time at which this secret was created."
  },
  {
    "name": "created_by",
    "type": "string",
    "description": "The principal that created the secret."
  },
  {
    "name": "effective_owner",
    "type": "string",
    "description": "The effective owner of the secret, which may differ from the directly-set **owner** due to inheritance."
  },
  {
    "name": "effective_value",
    "type": "string",
    "description": "The secret value. Only populated in responses when you have the **READ_SECRET** privilege and **include_value** is set to true in the request. The maximum size is 60 KiB."
  },
  {
    "name": "expire_time",
    "type": "string (date-time)",
    "description": "User-provided expiration time of the secret. This field indicates when the secret should no longer be used and may be displayed as a warning in the UI. It is purely informational and does not trigger any automatic actions or affect the secret's lifecycle."
  },
  {
    "name": "owner",
    "type": "string",
    "description": "The owner of the secret. Defaults to the creating principal on creation. Can be updated to transfer ownership of the secret to another principal."
  },
  {
    "name": "update_time",
    "type": "string (date-time)",
    "description": "The time at which this secret was last updated."
  },
  {
    "name": "updated_by",
    "type": "string",
    "description": "The principal that last updated the secret."
  },
  {
    "name": "value",
    "type": "string",
    "description": "The secret value to store. This field is input-only and is not returned in responses — use the **effective_value** field (via GetSecret with **include_value** set to true) to read the secret value. The maximum size is 60 KiB (pre-encryption). Accepted content includes passwords, tokens, keys, and other sensitive credential data."
  }
]} />
</TabItem>
<TabItem value="secrets_uc_list_secrets">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "The name of the secret, relative to its parent schema."
  },
  {
    "name": "metastore_id",
    "type": "string",
    "description": "Unique identifier of the metastore hosting the secret."
  },
  {
    "name": "catalog_name",
    "type": "string",
    "description": "The name of the catalog where the schema and the secret reside."
  },
  {
    "name": "full_name",
    "type": "string",
    "description": "The three-level (fully qualified) name of the secret, in the form of **catalog_name.schema_name.secret_name**."
  },
  {
    "name": "schema_name",
    "type": "string",
    "description": "The name of the schema where the secret resides."
  },
  {
    "name": "comment",
    "type": "string",
    "description": "User-provided free-form text description of the secret."
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": "The time at which this secret was created."
  },
  {
    "name": "created_by",
    "type": "string",
    "description": "The principal that created the secret."
  },
  {
    "name": "effective_owner",
    "type": "string",
    "description": "The effective owner of the secret, which may differ from the directly-set **owner** due to inheritance."
  },
  {
    "name": "effective_value",
    "type": "string",
    "description": "The secret value. Only populated in responses when you have the **READ_SECRET** privilege and **include_value** is set to true in the request. The maximum size is 60 KiB."
  },
  {
    "name": "expire_time",
    "type": "string (date-time)",
    "description": "User-provided expiration time of the secret. This field indicates when the secret should no longer be used and may be displayed as a warning in the UI. It is purely informational and does not trigger any automatic actions or affect the secret's lifecycle."
  },
  {
    "name": "owner",
    "type": "string",
    "description": "The owner of the secret. Defaults to the creating principal on creation. Can be updated to transfer ownership of the secret to another principal."
  },
  {
    "name": "update_time",
    "type": "string (date-time)",
    "description": "The time at which this secret was last updated."
  },
  {
    "name": "updated_by",
    "type": "string",
    "description": "The principal that last updated the secret."
  },
  {
    "name": "value",
    "type": "string",
    "description": "The secret value to store. This field is input-only and is not returned in responses — use the **effective_value** field (via GetSecret with **include_value** set to true) to read the secret value. The maximum size is 60 KiB (pre-encryption). Accepted content includes passwords, tokens, keys, and other sensitive credential data."
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
    <td><a href="#secrets_uc_get_secret"><CopyableCode code="secrets_uc_get_secret" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-full_name"><code>full_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Gets a secret by its three-level (fully qualified) name.</td>
</tr>
<tr>
    <td><a href="#secrets_uc_list_secrets"><CopyableCode code="secrets_uc_list_secrets" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-catalog_name"><code>catalog_name</code></a>, <a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a></td>
    <td>Lists secrets in Unity Catalog.</td>
</tr>
<tr>
    <td><a href="#secrets_uc_create_secret"><CopyableCode code="secrets_uc_create_secret" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-secret"><code>secret</code></a></td>
    <td></td>
    <td>Creates a new secret in Unity Catalog.</td>
</tr>
<tr>
    <td><a href="#secrets_uc_update_secret"><CopyableCode code="secrets_uc_update_secret" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-full_name"><code>full_name</code></a>, <a href="#parameter-update_mask"><code>update_mask</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-secret"><code>secret</code></a></td>
    <td></td>
    <td>Updates an existing secret in Unity Catalog.</td>
</tr>
<tr>
    <td><a href="#secrets_uc_delete_secret"><CopyableCode code="secrets_uc_delete_secret" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-full_name"><code>full_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Deletes a secret by its three-level (fully qualified) name.</td>
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
    <td>The three-level (fully qualified) name of the secret (for example, **catalog_name.schema_name.secret_name**).</td>
</tr>
<tr id="parameter-update_mask">
    <td><CopyableCode code="update_mask" /></td>
    <td><code>object</code></td>
    <td>The field mask specifying which fields of the secret to update. - If **update_mask** is **"*"**, all fields specified in **secret** are updated. - If **update_mask** specifies one or more fields, only those fields are updated. Each specified field must be set in **secret**. Supported fields: **value**, **comment**, **owner**, **expire_time**. To change the secret name, delete and recreate the secret.</td>
</tr>
<tr id="parameter-catalog_name">
    <td><CopyableCode code="catalog_name" /></td>
    <td><code>string</code></td>
    <td>The name of the catalog under which to list secrets. Both **catalog_name** and **schema_name** must be specified together.</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of secrets to return. - If not specified, at most 1000 secrets are returned. - If set to a value greater than 0, the page length is the minimum of this value and 1000. - If set to 0, the page length is set to 1000. - If set to a value less than 0, an invalid parameter error is returned.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Opaque pagination token to go to the next page based on previous query. The maximum page length is determined by a server configured value.</td>
</tr>
<tr id="parameter-schema_name">
    <td><CopyableCode code="schema_name" /></td>
    <td><code>string</code></td>
    <td>The name of the schema under which to list secrets. Both **catalog_name** and **schema_name** must be specified together.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="secrets_uc_get_secret"
    values={[
        { label: 'secrets_uc_get_secret', value: 'secrets_uc_get_secret' },
        { label: 'secrets_uc_list_secrets', value: 'secrets_uc_list_secrets' }
    ]}
>
<TabItem value="secrets_uc_get_secret">

Gets a secret by its three-level (fully qualified) name.

```sql
SELECT
name,
metastore_id,
catalog_name,
full_name,
schema_name,
comment,
create_time,
created_by,
effective_owner,
effective_value,
expire_time,
owner,
update_time,
updated_by,
value
FROM databricks_workspace.catalog.secrets_uc
WHERE full_name = '{{ full_name }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
<TabItem value="secrets_uc_list_secrets">

Lists secrets in Unity Catalog.

```sql
SELECT
name,
metastore_id,
catalog_name,
full_name,
schema_name,
comment,
create_time,
created_by,
effective_owner,
effective_value,
expire_time,
owner,
update_time,
updated_by,
value
FROM databricks_workspace.catalog.secrets_uc
WHERE deployment_name = '{{ deployment_name }}' -- required
AND catalog_name = '{{ catalog_name }}'
AND page_size = '{{ page_size }}'
AND page_token = '{{ page_token }}'
AND schema_name = '{{ schema_name }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="secrets_uc_create_secret"
    values={[
        { label: 'secrets_uc_create_secret', value: 'secrets_uc_create_secret' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="secrets_uc_create_secret">

Creates a new secret in Unity Catalog.

```sql
INSERT INTO databricks_workspace.catalog.secrets_uc (
secret,
deployment_name
)
SELECT 
'{{ secret }}' /* required */,
'{{ deployment_name }}'
RETURNING
name,
metastore_id,
catalog_name,
full_name,
schema_name,
comment,
create_time,
created_by,
effective_owner,
effective_value,
expire_time,
owner,
update_time,
updated_by,
value
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: secrets_uc
  props:
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the secrets_uc resource.
    - name: secret
      description: |
        The secret object to create. The **name**, **catalog_name**, **schema_name**, and **value** fields are required.
      value:
        name: "{{ name }}"
        catalog_name: "{{ catalog_name }}"
        schema_name: "{{ schema_name }}"
        value: "{{ value }}"
        comment: "{{ comment }}"
        create_time: "{{ create_time }}"
        created_by: "{{ created_by }}"
        effective_owner: "{{ effective_owner }}"
        effective_value: "{{ effective_value }}"
        expire_time: "{{ expire_time }}"
        full_name: "{{ full_name }}"
        metastore_id: "{{ metastore_id }}"
        owner: "{{ owner }}"
        update_time: "{{ update_time }}"
        updated_by: "{{ updated_by }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="secrets_uc_update_secret"
    values={[
        { label: 'secrets_uc_update_secret', value: 'secrets_uc_update_secret' }
    ]}
>
<TabItem value="secrets_uc_update_secret">

Updates an existing secret in Unity Catalog.

```sql
UPDATE databricks_workspace.catalog.secrets_uc
SET 
secret = '{{ secret }}'
WHERE 
full_name = '{{ full_name }}' --required
AND update_mask = '{{ update_mask }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND secret = '{{ secret }}' --required
RETURNING
name,
metastore_id,
catalog_name,
full_name,
schema_name,
comment,
create_time,
created_by,
effective_owner,
effective_value,
expire_time,
owner,
update_time,
updated_by,
value;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="secrets_uc_delete_secret"
    values={[
        { label: 'secrets_uc_delete_secret', value: 'secrets_uc_delete_secret' }
    ]}
>
<TabItem value="secrets_uc_delete_secret">

Deletes a secret by its three-level (fully qualified) name.

```sql
DELETE FROM databricks_workspace.catalog.secrets_uc
WHERE full_name = '{{ full_name }}' --required
AND deployment_name = '{{ deployment_name }}' --required
;
```
</TabItem>
</Tabs>

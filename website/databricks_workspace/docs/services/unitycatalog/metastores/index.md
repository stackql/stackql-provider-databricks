--- 
title: metastores
hide_title: false
hide_table_of_contents: false
keywords:
  - metastores
  - unitycatalog
  - databricks_workspace
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage databricks_workspace resources using SQL
custom_edit_url: null
image: /img/stackql-databricks_workspace-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>metastores</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>metastores</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.unitycatalog.metastores" /></td></tr>
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

The metastore was successfully retrieved.

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="default_data_access_config_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="global_metastore_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="metastore_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="storage_root_credential_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="delta_sharing_organization_name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="storage_root_credential_name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="cloud" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="created_by" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="delta_sharing_recipient_token_lifetime_in_seconds" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="delta_sharing_scope" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="external_access_enabled" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="owner" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="privilege_model_version" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="region" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="storage_root" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="updated_at" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="updated_by" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

The metastore list was successfully retrieved.

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="default_data_access_config_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="global_metastore_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="metastore_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="storage_root_credential_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="delta_sharing_organization_name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="storage_root_credential_name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="cloud" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="created_by" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="delta_sharing_recipient_token_lifetime_in_seconds" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="delta_sharing_scope" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="external_access_enabled" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="owner" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="privilege_model_version" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="region" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="storage_root" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="updated_at" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="updated_by" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>
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
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Gets a metastore that matches the supplied ID. The caller must be a metastore admin to retrieve this info.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Gets an array of the available metastores (as</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Creates a new metastore based on a provided name and optional storage root path. By default (if the</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Updates information for a specific metastore. The caller must be a metastore admin. If the</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Deletes a metastore. The caller must be a metastore admin.</td>
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

Gets a metastore that matches the supplied ID. The caller must be a metastore admin to retrieve this info.

```sql
SELECT
name,
default_data_access_config_id,
global_metastore_id,
metastore_id,
storage_root_credential_id,
delta_sharing_organization_name,
storage_root_credential_name,
cloud,
created_at,
created_by,
delta_sharing_recipient_token_lifetime_in_seconds,
delta_sharing_scope,
external_access_enabled,
owner,
privilege_model_version,
region,
storage_root,
updated_at,
updated_by
FROM databricks_workspace.unitycatalog.metastores
WHERE deployment_name = '{{ deployment_name }}' -- required;
```
</TabItem>
<TabItem value="list">

Gets an array of the available metastores (as

```sql
SELECT
name,
default_data_access_config_id,
global_metastore_id,
metastore_id,
storage_root_credential_id,
delta_sharing_organization_name,
storage_root_credential_name,
cloud,
created_at,
created_by,
delta_sharing_recipient_token_lifetime_in_seconds,
delta_sharing_scope,
external_access_enabled,
owner,
privilege_model_version,
region,
storage_root,
updated_at,
updated_by
FROM databricks_workspace.unitycatalog.metastores
WHERE deployment_name = '{{ deployment_name }}' -- required;
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

Creates a new metastore based on a provided name and optional storage root path. By default (if the

```sql
INSERT INTO databricks_workspace.unitycatalog.metastores (
data__name,
data__storage_root,
data__region,
deployment_name
)
SELECT 
'{{ name }}',
'{{ storage_root }}',
'{{ region }}',
'{{ deployment_name }}'
RETURNING
name,
default_data_access_config_id,
global_metastore_id,
metastore_id,
storage_root_credential_id,
delta_sharing_organization_name,
storage_root_credential_name,
cloud,
created_at,
created_by,
delta_sharing_recipient_token_lifetime_in_seconds,
delta_sharing_scope,
external_access_enabled,
owner,
privilege_model_version,
region,
storage_root,
updated_at,
updated_by
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: metastores
  props:
    - name: deployment_name
      value: string
      description: Required parameter for the metastores resource.
    - name: name
      value: required
    - name: storage_root
      value: string
    - name: region
      value: string
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

Updates information for a specific metastore. The caller must be a metastore admin. If the

```sql
UPDATE databricks_workspace.unitycatalog.metastores
SET 
data__storage_root_credential_id = '{{ storage_root_credential_id }}',
data__delta_sharing_recipient_token_lifetime_in_seconds = {{ delta_sharing_recipient_token_lifetime_in_seconds }},
data__delta_sharing_organization_name = '{{ delta_sharing_organization_name }}',
data__owner = '{{ owner }}',
data__privilege_model_version = '{{ privilege_model_version }}',
data__new_name = '{{ new_name }}',
data__delta_sharing_scope = '{{ delta_sharing_scope }}'
WHERE 
deployment_name = '{{ deployment_name }}' --required
RETURNING
name,
default_data_access_config_id,
global_metastore_id,
metastore_id,
storage_root_credential_id,
delta_sharing_organization_name,
storage_root_credential_name,
cloud,
created_at,
created_by,
delta_sharing_recipient_token_lifetime_in_seconds,
delta_sharing_scope,
external_access_enabled,
owner,
privilege_model_version,
region,
storage_root,
updated_at,
updated_by;
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

Deletes a metastore. The caller must be a metastore admin.

```sql
DELETE FROM databricks_workspace.unitycatalog.metastores
WHERE deployment_name = '{{ deployment_name }}' --required;
```
</TabItem>
</Tabs>

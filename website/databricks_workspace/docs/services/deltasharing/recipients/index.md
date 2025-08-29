--- 
title: recipients
hide_title: false
hide_table_of_contents: false
keywords:
  - recipients
  - deltasharing
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

Creates, updates, deletes, gets or lists a <code>recipients</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>recipients</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.deltasharing.recipients" /></td></tr>
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

The recipient was successfully retrieved.

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
    <td><CopyableCode code="data_recipient_global_metastore_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="metastore_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="activated" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="activation_url" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="authentication_type" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="cloud" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="comment" /></td>
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
    <td><CopyableCode code="ip_access_list" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="owner" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="properties_kvpairs" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="region" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="sharing_code" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="tokens" /></td>
    <td><code>array</code></td>
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

The list of recipients was successfully retrieved.

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
    <td><CopyableCode code="data_recipient_global_metastore_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="metastore_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="activated" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="activation_url" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="authentication_type" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="cloud" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="comment" /></td>
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
    <td><CopyableCode code="ip_access_list" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="owner" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="properties_kvpairs" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="region" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="sharing_code" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="tokens" /></td>
    <td><code>array</code></td>
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
    <td>Gets a share recipient from the metastore if:</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Gets an array of all share recipients within the current metastore where:</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Creates a new recipient with the delta sharing authentication type in the metastore. The caller must be a metastore admin or has the</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Updates an existing recipient in the metastore. The caller must be a metastore admin or the owner of the recipient. If the recipient name will be updated, the user must be both a metastore admin and the owner of the recipient.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Deletes the specified recipient from the metastore. The caller must be the owner of the recipient.</td>
</tr>
<tr>
    <td><a href="#rotatetoken"><CopyableCode code="rotatetoken" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Refreshes the specified recipient's delta sharing authentication token with the provided token info. The caller must be the owner of the recipient.</td>
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

Gets a share recipient from the metastore if:

```sql
SELECT
name,
data_recipient_global_metastore_id,
metastore_id,
activated,
activation_url,
authentication_type,
cloud,
comment,
created_at,
created_by,
ip_access_list,
owner,
properties_kvpairs,
region,
sharing_code,
tokens,
updated_at,
updated_by
FROM databricks_workspace.deltasharing.recipients
WHERE deployment_name = '{{ deployment_name }}' -- required;
```
</TabItem>
<TabItem value="list">

Gets an array of all share recipients within the current metastore where:

```sql
SELECT
name,
data_recipient_global_metastore_id,
metastore_id,
activated,
activation_url,
authentication_type,
cloud,
comment,
created_at,
created_by,
ip_access_list,
owner,
properties_kvpairs,
region,
sharing_code,
tokens,
updated_at,
updated_by
FROM databricks_workspace.deltasharing.recipients
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

Creates a new recipient with the delta sharing authentication type in the metastore. The caller must be a metastore admin or has the

```sql
INSERT INTO databricks_workspace.deltasharing.recipients (
data__name,
data__authentication_type,
data__owner,
data__comment,
data__data_recipient_global_metastore_id,
data__sharing_code,
data__expiration_time,
data__ip_access_list,
data__properties_kvpairs,
deployment_name
)
SELECT 
'{{ name }}',
'{{ authentication_type }}',
'{{ owner }}',
'{{ comment }}',
'{{ data_recipient_global_metastore_id }}',
'{{ sharing_code }}',
'{{ expiration_time }}',
'{{ ip_access_list }}',
'{{ properties_kvpairs }}',
'{{ deployment_name }}'
RETURNING
name,
data_recipient_global_metastore_id,
metastore_id,
activated,
activation_url,
authentication_type,
cloud,
comment,
created_at,
created_by,
ip_access_list,
owner,
properties_kvpairs,
region,
sharing_code,
tokens,
updated_at,
updated_by
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: recipients
  props:
    - name: deployment_name
      value: string
      description: Required parameter for the recipients resource.
    - name: name
      value: required
    - name: authentication_type
      value: string
    - name: owner
      value: required
    - name: comment
      value: string
    - name: data_recipient_global_metastore_id
      value: string
    - name: sharing_code
      value: string
    - name: expiration_time
      value: string
    - name: ip_access_list
      value: object
    - name: properties_kvpairs
      value: object
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

Updates an existing recipient in the metastore. The caller must be a metastore admin or the owner of the recipient. If the recipient name will be updated, the user must be both a metastore admin and the owner of the recipient.

```sql
UPDATE databricks_workspace.deltasharing.recipients
SET 
data__owner = '{{ owner }}',
data__comment = '{{ comment }}',
data__new_name = '{{ new_name }}',
data__expiration_time = {{ expiration_time }},
data__ip_access_list = '{{ ip_access_list }}',
data__properties_kvpairs = '{{ properties_kvpairs }}'
WHERE 
deployment_name = '{{ deployment_name }}' --required;
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

Deletes the specified recipient from the metastore. The caller must be the owner of the recipient.

```sql
DELETE FROM databricks_workspace.deltasharing.recipients
WHERE deployment_name = '{{ deployment_name }}' --required;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="rotatetoken"
    values={[
        { label: 'rotatetoken', value: 'rotatetoken' }
    ]}
>
<TabItem value="rotatetoken">

Refreshes the specified recipient's delta sharing authentication token with the provided token info. The caller must be the owner of the recipient.

```sql
EXEC databricks_workspace.deltasharing.recipients.rotatetoken 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"existing_token_expire_in_seconds": "{{ existing_token_expire_in_seconds }}"
}';
```
</TabItem>
</Tabs>

--- 
title: credentials
hide_title: false
hide_table_of_contents: false
keywords:
  - credentials
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

Creates, updates, deletes, gets or lists a <code>credentials</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>credentials</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.unitycatalog.credentials" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="generatetemporaryservicecredential"
    values={[
        { label: 'generatetemporaryservicecredential', value: 'generatetemporaryservicecredential' },
        { label: 'getcredential', value: 'getcredential' },
        { label: 'listcredentials', value: 'listcredentials' }
    ]}
>
<TabItem value="generatetemporaryservicecredential">

Request completed successfully.

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
    <td><CopyableCode code="aws_temp_credentials" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="expiration_time" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="getcredential">

Request completed successfully.

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
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="metastore_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="full_name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="aws_iam_role" /></td>
    <td><code>object</code></td>
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
    <td><CopyableCode code="isolation_mode" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="owner" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="purpose" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="read_only" /></td>
    <td><code>boolean</code></td>
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
<tr>
    <td><CopyableCode code="used_for_managed_storage" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="listcredentials">

Request completed successfully.

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
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="metastore_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="full_name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="aws_iam_role" /></td>
    <td><code>object</code></td>
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
    <td><CopyableCode code="isolation_mode" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="owner" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="purpose" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="read_only" /></td>
    <td><code>boolean</code></td>
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
<tr>
    <td><CopyableCode code="used_for_managed_storage" /></td>
    <td><code>boolean</code></td>
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
    <td><a href="#generatetemporaryservicecredential"><CopyableCode code="generatetemporaryservicecredential" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Returns a set of temporary credentials generated using the specified service credential. The caller must be a metastore admin or have the metastore privilege</td>
</tr>
<tr>
    <td><a href="#getcredential"><CopyableCode code="getcredential" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Gets a service or storage credential from the metastore. The caller must be a metastore admin, the owner of the credential, or have any permission on the credential.</td>
</tr>
<tr>
    <td><a href="#listcredentials"><CopyableCode code="listcredentials" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Gets an array of credentials (as</td>
</tr>
<tr>
    <td><a href="#createcredential"><CopyableCode code="createcredential" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Creates a new credential. The type of credential to be created is determined by the</td>
</tr>
<tr>
    <td><a href="#updatecredential"><CopyableCode code="updatecredential" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Updates a service or storage credential on the metastore.</td>
</tr>
<tr>
    <td><a href="#deletecredential"><CopyableCode code="deletecredential" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Deletes a service or storage credential from the metastore. The caller must be an owner of the credential.</td>
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
    defaultValue="generatetemporaryservicecredential"
    values={[
        { label: 'generatetemporaryservicecredential', value: 'generatetemporaryservicecredential' },
        { label: 'getcredential', value: 'getcredential' },
        { label: 'listcredentials', value: 'listcredentials' }
    ]}
>
<TabItem value="generatetemporaryservicecredential">

Returns a set of temporary credentials generated using the specified service credential. The caller must be a metastore admin or have the metastore privilege

```sql
SELECT
aws_temp_credentials,
expiration_time
FROM databricks_workspace.unitycatalog.credentials
WHERE deployment_name = '{{ deployment_name }}' -- required;
```
</TabItem>
<TabItem value="getcredential">

Gets a service or storage credential from the metastore. The caller must be a metastore admin, the owner of the credential, or have any permission on the credential.

```sql
SELECT
id,
name,
metastore_id,
full_name,
aws_iam_role,
comment,
created_at,
created_by,
isolation_mode,
owner,
purpose,
read_only,
updated_at,
updated_by,
used_for_managed_storage
FROM databricks_workspace.unitycatalog.credentials
WHERE deployment_name = '{{ deployment_name }}' -- required;
```
</TabItem>
<TabItem value="listcredentials">

Gets an array of credentials (as

```sql
SELECT
id,
name,
metastore_id,
full_name,
aws_iam_role,
comment,
created_at,
created_by,
isolation_mode,
owner,
purpose,
read_only,
updated_at,
updated_by,
used_for_managed_storage
FROM databricks_workspace.unitycatalog.credentials
WHERE deployment_name = '{{ deployment_name }}' -- required;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="createcredential"
    values={[
        { label: 'createcredential', value: 'createcredential' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="createcredential">

Creates a new credential. The type of credential to be created is determined by the

```sql
INSERT INTO databricks_workspace.unitycatalog.credentials (
data__name,
data__comment,
data__read_only,
data__purpose,
data__skip_validation,
data__aws_iam_role,
deployment_name
)
SELECT 
'{{ name }}',
'{{ comment }}',
'{{ read_only }}',
{{ purpose }},
'{{ skip_validation }}',
'{{ aws_iam_role }}',
'{{ deployment_name }}'
RETURNING
id,
name,
metastore_id,
full_name,
aws_iam_role,
comment,
created_at,
created_by,
isolation_mode,
owner,
purpose,
read_only,
updated_at,
updated_by,
used_for_managed_storage
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: credentials
  props:
    - name: deployment_name
      value: string
      description: Required parameter for the credentials resource.
    - name: name
      value: required
    - name: comment
      value: string
    - name: read_only
      value: string
    - name: purpose
      value: boolean
    - name: skip_validation
      value: string
    - name: aws_iam_role
      value: object
```
</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="updatecredential"
    values={[
        { label: 'updatecredential', value: 'updatecredential' }
    ]}
>
<TabItem value="updatecredential">

Updates a service or storage credential on the metastore.

```sql
UPDATE databricks_workspace.unitycatalog.credentials
SET 
data__new_name = '{{ new_name }}',
data__comment = '{{ comment }}',
data__read_only = {{ read_only }},
data__owner = '{{ owner }}',
data__isolation_mode = '{{ isolation_mode }}',
data__skip_validation = {{ skip_validation }},
data__force = {{ force }},
data__aws_iam_role = '{{ aws_iam_role }}'
WHERE 
deployment_name = '{{ deployment_name }}' --required
RETURNING
id,
name,
metastore_id,
full_name,
aws_iam_role,
comment,
created_at,
created_by,
isolation_mode,
owner,
purpose,
read_only,
updated_at,
updated_by,
used_for_managed_storage;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="deletecredential"
    values={[
        { label: 'deletecredential', value: 'deletecredential' }
    ]}
>
<TabItem value="deletecredential">

Deletes a service or storage credential from the metastore. The caller must be an owner of the credential.

```sql
DELETE FROM databricks_workspace.unitycatalog.credentials
WHERE deployment_name = '{{ deployment_name }}' --required;
```
</TabItem>
</Tabs>

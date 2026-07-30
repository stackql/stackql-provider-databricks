---
title: service_principals
hide_title: false
hide_table_of_contents: false
keywords:
  - service_principals
  - iamv2
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

Creates, updates, deletes, gets or lists a <code>service_principals</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="service_principals" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.iamv2.service_principals" /></td></tr>
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
    "description": "The parent account ID for the service principal in Databricks."
  },
  {
    "name": "application_id",
    "type": "string",
    "description": "Application ID of the service principal."
  },
  {
    "name": "external_id",
    "type": "string",
    "description": "ExternalId of the service principal in the customer's IdP."
  },
  {
    "name": "internal_id",
    "type": "string",
    "description": "Internal service principal ID of the service principal in Databricks."
  },
  {
    "name": "display_name",
    "type": "string",
    "description": "Display name of the service principal."
  },
  {
    "name": "account_sp_status",
    "type": "string",
    "description": "The activity status of a service principal in a Databricks account. (ACTIVE, INACTIVE)"
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "account_id",
    "type": "string",
    "description": "The parent account ID for the service principal in Databricks."
  },
  {
    "name": "application_id",
    "type": "string",
    "description": "Application ID of the service principal."
  },
  {
    "name": "external_id",
    "type": "string",
    "description": "ExternalId of the service principal in the customer's IdP."
  },
  {
    "name": "internal_id",
    "type": "string",
    "description": "Internal service principal ID of the service principal in Databricks."
  },
  {
    "name": "display_name",
    "type": "string",
    "description": "Display name of the service principal."
  },
  {
    "name": "account_sp_status",
    "type": "string",
    "description": "The activity status of a service principal in a Databricks account. (ACTIVE, INACTIVE)"
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
    <td><a href="#parameter-internal_id"><code>internal_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Fetches a service principal by its internal ID from the Databricks account that parents the calling</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-filter"><code>filter</code></a>, <a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Lists the service principals in the Databricks account that parents the calling workspace, returning</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-service_principal"><code>service_principal</code></a></td>
    <td></td>
    <td>Creates a service principal in the Databricks account that parents the calling workspace and returns</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-internal_id"><code>internal_id</code></a>, <a href="#parameter-update_mask"><code>update_mask</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-service_principal"><code>service_principal</code></a></td>
    <td></td>
    <td>Updates an existing service principal in the Databricks account that parents the calling workspace.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-internal_id"><code>internal_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Deletes a service principal by its internal ID from the Databricks account that parents the calling</td>
</tr>
<tr>
    <td><a href="#resolve"><CopyableCode code="resolve" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-external_id"><code>external_id</code></a></td>
    <td></td>
    <td>Resolves an SP with the given external ID from the customer's IdP. If the SP does not exist, it will</td>
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
<tr id="parameter-internal_id">
    <td><CopyableCode code="internal_id" /></td>
    <td><code>string</code></td>
    <td>Required. Internal ID of the service principal in Databricks.</td>
</tr>
<tr id="parameter-update_mask">
    <td><CopyableCode code="update_mask" /></td>
    <td><code>string</code></td>
    <td>Optional. The list of fields to update.</td>
</tr>
<tr id="parameter-filter">
    <td><CopyableCode code="filter" /></td>
    <td><code>string</code></td>
    <td>Optional. Allows filtering service principals by application id or external id.</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of SPs to return. The service may return fewer than this value.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>A page token, received from a previous ListServicePrincipals call. Provide this to retrieve the subsequent page.</td>
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

Fetches a service principal by its internal ID from the Databricks account that parents the calling

```sql
SELECT
account_id,
application_id,
external_id,
internal_id,
display_name,
account_sp_status
FROM databricks_workspace.iamv2.service_principals
WHERE internal_id = '{{ internal_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists the service principals in the Databricks account that parents the calling workspace, returning

```sql
SELECT
account_id,
application_id,
external_id,
internal_id,
display_name,
account_sp_status
FROM databricks_workspace.iamv2.service_principals
WHERE deployment_name = '{{ deployment_name }}' -- required
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

Creates a service principal in the Databricks account that parents the calling workspace and returns

```sql
INSERT INTO databricks_workspace.iamv2.service_principals (
service_principal,
deployment_name
)
SELECT 
'{{ service_principal }}' /* required */,
'{{ deployment_name }}'
RETURNING
account_id,
application_id,
external_id,
internal_id,
display_name,
account_sp_status
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: service_principals
  props:
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the service_principals resource.
    - name: service_principal
      description: |
        Required. Service principal to be created in <Databricks>
      value:
        account_id: "{{ account_id }}"
        account_sp_status: "{{ account_sp_status }}"
        application_id: "{{ application_id }}"
        display_name: "{{ display_name }}"
        external_id: "{{ external_id }}"
        internal_id: "{{ internal_id }}"
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

Updates an existing service principal in the Databricks account that parents the calling workspace.

```sql
UPDATE databricks_workspace.iamv2.service_principals
SET 
service_principal = '{{ service_principal }}'
WHERE 
internal_id = '{{ internal_id }}' --required
AND update_mask = '{{ update_mask }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND service_principal = '{{ service_principal }}' --required
RETURNING
account_id,
application_id,
external_id,
internal_id,
display_name,
account_sp_status;
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

Deletes a service principal by its internal ID from the Databricks account that parents the calling

```sql
DELETE FROM databricks_workspace.iamv2.service_principals
WHERE internal_id = '{{ internal_id }}' --required
AND deployment_name = '{{ deployment_name }}' --required
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

Resolves an SP with the given external ID from the customer's IdP. If the SP does not exist, it will

```sql
EXEC databricks_workspace.iamv2.service_principals.resolve 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"external_id": "{{ external_id }}"
}'
;
```
</TabItem>
</Tabs>

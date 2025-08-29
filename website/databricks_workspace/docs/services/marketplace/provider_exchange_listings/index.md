--- 
title: provider_exchange_listings
hide_title: false
hide_table_of_contents: false
keywords:
  - provider_exchange_listings
  - marketplace
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

Creates, updates, deletes, gets or lists a <code>provider_exchange_listings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>provider_exchange_listings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.marketplace.provider_exchange_listings" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="listlistingsforexchange"
    values={[
        { label: 'listlistingsforexchange', value: 'listlistingsforexchange' },
        { label: 'listexchangesforlisting', value: 'listexchangesforlisting' }
    ]}
>
<TabItem value="listlistingsforexchange">

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
    <td><CopyableCode code="exchange_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="listing_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="exchange_name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="listing_name" /></td>
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
</tbody>
</table>
</TabItem>
<TabItem value="listexchangesforlisting">

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
    <td><CopyableCode code="exchange_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="listing_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="exchange_name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="listing_name" /></td>
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
    <td><a href="#listlistingsforexchange"><CopyableCode code="listlistingsforexchange" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>List listings associated with an exchange</td>
</tr>
<tr>
    <td><a href="#listexchangesforlisting"><CopyableCode code="listexchangesforlisting" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>List exchanges associated with a listing</td>
</tr>
<tr>
    <td><a href="#addlistingtoexchange"><CopyableCode code="addlistingtoexchange" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Associate an exchange with a listing</td>
</tr>
<tr>
    <td><a href="#deletelistingfromexchange"><CopyableCode code="deletelistingfromexchange" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Disassociate an exchange with a listing</td>
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
    defaultValue="listlistingsforexchange"
    values={[
        { label: 'listlistingsforexchange', value: 'listlistingsforexchange' },
        { label: 'listexchangesforlisting', value: 'listexchangesforlisting' }
    ]}
>
<TabItem value="listlistingsforexchange">

List listings associated with an exchange

```sql
SELECT
id,
exchange_id,
listing_id,
exchange_name,
listing_name,
created_at,
created_by
FROM databricks_workspace.marketplace.provider_exchange_listings
WHERE deployment_name = '{{ deployment_name }}' -- required;
```
</TabItem>
<TabItem value="listexchangesforlisting">

List exchanges associated with a listing

```sql
SELECT
id,
exchange_id,
listing_id,
exchange_name,
listing_name,
created_at,
created_by
FROM databricks_workspace.marketplace.provider_exchange_listings
WHERE deployment_name = '{{ deployment_name }}' -- required;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="addlistingtoexchange"
    values={[
        { label: 'addlistingtoexchange', value: 'addlistingtoexchange' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="addlistingtoexchange">

Associate an exchange with a listing

```sql
INSERT INTO databricks_workspace.marketplace.provider_exchange_listings (
data__listing_id,
data__exchange_id,
deployment_name
)
SELECT 
'{{ listing_id }}',
'{{ exchange_id }}',
'{{ deployment_name }}'
RETURNING
exchange_for_listing
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: provider_exchange_listings
  props:
    - name: deployment_name
      value: string
      description: Required parameter for the provider_exchange_listings resource.
    - name: listing_id
      value: required
    - name: exchange_id
      value: string
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="deletelistingfromexchange"
    values={[
        { label: 'deletelistingfromexchange', value: 'deletelistingfromexchange' }
    ]}
>
<TabItem value="deletelistingfromexchange">

Disassociate an exchange with a listing

```sql
DELETE FROM databricks_workspace.marketplace.provider_exchange_listings
WHERE deployment_name = '{{ deployment_name }}' --required;
```
</TabItem>
</Tabs>

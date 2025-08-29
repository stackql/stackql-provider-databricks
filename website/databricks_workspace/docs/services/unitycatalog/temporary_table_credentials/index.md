--- 
title: temporary_table_credentials
hide_title: false
hide_table_of_contents: false
keywords:
  - temporary_table_credentials
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

Creates, updates, deletes, gets or lists a <code>temporary_table_credentials</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>temporary_table_credentials</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.unitycatalog.temporary_table_credentials" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="generatetemporarytablecredentials"
    values={[
        { label: 'generatetemporarytablecredentials', value: 'generatetemporarytablecredentials' }
    ]}
>
<TabItem value="generatetemporarytablecredentials">

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
    <td><CopyableCode code="azure_user_delegation_sas" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="expiration_time" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="gcp_oauth_token" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="r2_temp_credentials" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="url" /></td>
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
    <td><a href="#generatetemporarytablecredentials"><CopyableCode code="generatetemporarytablecredentials" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Get a short-lived credential for directly accessing the table data on cloud storage. The metastore must have external_access_enabled flag set to true (default false). The caller must have EXTERNAL_USE_SCHEMA privilege on the parent schema and this privilege can only be granted by catalog owners.</td>
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
    defaultValue="generatetemporarytablecredentials"
    values={[
        { label: 'generatetemporarytablecredentials', value: 'generatetemporarytablecredentials' }
    ]}
>
<TabItem value="generatetemporarytablecredentials">

Get a short-lived credential for directly accessing the table data on cloud storage. The metastore must have external_access_enabled flag set to true (default false). The caller must have EXTERNAL_USE_SCHEMA privilege on the parent schema and this privilege can only be granted by catalog owners.

```sql
SELECT
aws_temp_credentials,
azure_user_delegation_sas,
expiration_time,
gcp_oauth_token,
r2_temp_credentials,
url
FROM databricks_workspace.unitycatalog.temporary_table_credentials
WHERE deployment_name = '{{ deployment_name }}' -- required;
```
</TabItem>
</Tabs>

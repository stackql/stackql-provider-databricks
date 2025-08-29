--- 
title: libraries
hide_title: false
hide_table_of_contents: false
keywords:
  - libraries
  - compute
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

Creates, updates, deletes, gets or lists a <code>libraries</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>libraries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.compute.libraries" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="clusterstatus"
    values={[
        { label: 'clusterstatus', value: 'clusterstatus' },
        { label: 'allclusterlibrarystatuses', value: 'allclusterlibrarystatuses' }
    ]}
>
<TabItem value="clusterstatus">

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
    <td><CopyableCode code="cluster_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="library_statuses" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="allclusterlibrarystatuses">

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
    <td><CopyableCode code="cluster_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="library_statuses" /></td>
    <td><code>array</code></td>
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
    <td><a href="#clusterstatus"><CopyableCode code="clusterstatus" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Get the status of libraries on a cluster. A status is returned for all libraries installed on this cluster via the API or the libraries UI. The order of returned libraries is as follows:</td>
</tr>
<tr>
    <td><a href="#allclusterlibrarystatuses"><CopyableCode code="allclusterlibrarystatuses" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Get the status of all libraries on all clusters. A status is returned for all libraries installed on this cluster via the API or the libraries UI.</td>
</tr>
<tr>
    <td><a href="#install"><CopyableCode code="install" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Add libraries to install on a cluster. The installation is asynchronous; it happens in the background after the completion of this request.</td>
</tr>
<tr>
    <td><a href="#uninstall"><CopyableCode code="uninstall" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Set libraries to uninstall from a cluster. The libraries won't be uninstalled until the cluster is restarted. A request to uninstall a library that is not currently installed is ignored.</td>
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
    defaultValue="clusterstatus"
    values={[
        { label: 'clusterstatus', value: 'clusterstatus' },
        { label: 'allclusterlibrarystatuses', value: 'allclusterlibrarystatuses' }
    ]}
>
<TabItem value="clusterstatus">

Get the status of libraries on a cluster. A status is returned for all libraries installed on this cluster via the API or the libraries UI. The order of returned libraries is as follows:

```sql
SELECT
cluster_id,
library_statuses
FROM databricks_workspace.compute.libraries
WHERE deployment_name = '{{ deployment_name }}' -- required;
```
</TabItem>
<TabItem value="allclusterlibrarystatuses">

Get the status of all libraries on all clusters. A status is returned for all libraries installed on this cluster via the API or the libraries UI.

```sql
SELECT
cluster_id,
library_statuses
FROM databricks_workspace.compute.libraries
WHERE deployment_name = '{{ deployment_name }}' -- required;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="install"
    values={[
        { label: 'install', value: 'install' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="install">

Add libraries to install on a cluster. The installation is asynchronous; it happens in the background after the completion of this request.

```sql
INSERT INTO databricks_workspace.compute.libraries (
data__cluster_id,
data__libraries,
deployment_name
)
SELECT 
'{{ cluster_id }}',
'{{ libraries }}',
'{{ deployment_name }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: libraries
  props:
    - name: deployment_name
      value: string
      description: Required parameter for the libraries resource.
    - name: cluster_id
      value: required
    - name: libraries
      value: required
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="uninstall"
    values={[
        { label: 'uninstall', value: 'uninstall' }
    ]}
>
<TabItem value="uninstall">

Set libraries to uninstall from a cluster. The libraries won't be uninstalled until the cluster is restarted. A request to uninstall a library that is not currently installed is ignored.

```sql
DELETE FROM databricks_workspace.compute.libraries
WHERE deployment_name = '{{ deployment_name }}' --required;
```
</TabItem>
</Tabs>

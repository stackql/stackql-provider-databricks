--- 
title: pipelines
hide_title: false
hide_table_of_contents: false
keywords:
  - pipelines
  - deltalivetables
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

Creates, updates, deletes, gets or lists a <code>pipelines</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pipelines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.deltalivetables.pipelines" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'listpipelines', value: 'listpipelines' }
    ]}
>
<TabItem value="get">

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
    <td><CopyableCode code="cluster_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="pipeline_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="creator_user_name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="run_as_user_name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="latest_updates" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="spec" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="listpipelines">

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
    <td><CopyableCode code="pipeline_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="creator_user_name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="latest_updates" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
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
    <td></td>
</tr>
<tr>
    <td><a href="#listpipelines"><CopyableCode code="listpipelines" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Lists pipelines defined in the Delta Live Tables system.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Creates a new data processing pipeline based on the requested configuration. If successful, this method returns the ID of the new pipeline.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Updates a pipeline with the supplied configuration.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Deletes a pipeline.</td>
</tr>
<tr>
    <td><a href="#stop"><CopyableCode code="stop" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Stops the pipeline by canceling the active update. If there is no active update for the pipeline, this request is a no-op.</td>
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
        { label: 'listpipelines', value: 'listpipelines' }
    ]}
>
<TabItem value="get">

No description available.

```sql
SELECT
name,
cluster_id,
pipeline_id,
creator_user_name,
run_as_user_name,
latest_updates,
spec,
state
FROM databricks_workspace.deltalivetables.pipelines
WHERE deployment_name = '{{ deployment_name }}' -- required;
```
</TabItem>
<TabItem value="listpipelines">

Lists pipelines defined in the Delta Live Tables system.

```sql
SELECT
name,
pipeline_id,
creator_user_name,
latest_updates,
state
FROM databricks_workspace.deltalivetables.pipelines
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

Creates a new data processing pipeline based on the requested configuration. If successful, this method returns the ID of the new pipeline.

```sql
INSERT INTO databricks_workspace.deltalivetables.pipelines (
data__id,
data__name,
data__storage,
data__target,
data__schema,
data__continuous,
data__development,
data__photon,
data__edition,
data__channel,
data__catalog,
data__serverless,
data__allow_duplicate_names,
data__dry_run,
data__configuration,
data__clusters,
data__libraries,
data__trigger,
data__filters,
data__notifications,
data__deployment,
data__ingestion_definition,
deployment_name
)
SELECT 
'{{ id }}',
'{{ name }}',
'{{ storage }}',
'{{ target }}',
'{{ schema }}',
{{ continuous }},
{{ development }},
{{ photon }},
'{{ edition }}',
'{{ channel }}',
'{{ catalog }}',
{{ serverless }},
{{ allow_duplicate_names }},
{{ dry_run }},
'{{ configuration }}',
'{{ clusters }}',
'{{ libraries }}',
'{{ trigger }}',
'{{ filters }}',
'{{ notifications }}',
'{{ deployment }}',
'{{ ingestion_definition }}',
'{{ deployment_name }}'
RETURNING
pipeline_id
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: pipelines
  props:
    - name: deployment_name
      value: string
      description: Required parameter for the pipelines resource.
    - name: id
      value: string
    - name: name
      value: string
    - name: storage
      value: string
    - name: target
      value: string
    - name: schema
      value: string
    - name: continuous
      value: boolean
    - name: development
      value: boolean
    - name: photon
      value: boolean
    - name: edition
      value: string
    - name: channel
      value: string
    - name: catalog
      value: string
    - name: serverless
      value: boolean
    - name: allow_duplicate_names
      value: boolean
    - name: dry_run
      value: boolean
    - name: configuration
      value: object
    - name: clusters
      value: Array of object
    - name: libraries
      value: Array of object
    - name: trigger
      value: object
    - name: filters
      value: object
    - name: notifications
      value: Array of object
    - name: deployment
      value: object
    - name: ingestion_definition
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

Updates a pipeline with the supplied configuration.

```sql
UPDATE databricks_workspace.deltalivetables.pipelines
SET 
data__id = '{{ id }}',
data__name = '{{ name }}',
data__storage = '{{ storage }}',
data__target = '{{ target }}',
data__schema = '{{ schema }}',
data__continuous = {{ continuous }},
data__development = {{ development }},
data__photon = {{ photon }},
data__edition = '{{ edition }}',
data__channel = '{{ channel }}',
data__catalog = '{{ catalog }}',
data__serverless = {{ serverless }},
data__pipeline_id = '{{ pipeline_id }}',
data__allow_duplicate_names = {{ allow_duplicate_names }},
data__expected_last_modified = {{ expected_last_modified }},
data__configuration = '{{ configuration }}',
data__clusters = '{{ clusters }}',
data__libraries = '{{ libraries }}',
data__trigger = '{{ trigger }}',
data__filters = '{{ filters }}',
data__notifications = '{{ notifications }}',
data__deployment = '{{ deployment }}',
data__ingestion_definition = '{{ ingestion_definition }}'
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

Deletes a pipeline.

```sql
DELETE FROM databricks_workspace.deltalivetables.pipelines
WHERE deployment_name = '{{ deployment_name }}' --required;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="stop"
    values={[
        { label: 'stop', value: 'stop' }
    ]}
>
<TabItem value="stop">

Stops the pipeline by canceling the active update. If there is no active update for the pipeline, this request is a no-op.

```sql
EXEC databricks_workspace.deltalivetables.pipelines.stop 
@deployment_name='{{ deployment_name }}' --required;
```
</TabItem>
</Tabs>

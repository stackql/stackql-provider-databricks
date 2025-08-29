--- 
title: model_transition_requests
hide_title: false
hide_table_of_contents: false
keywords:
  - model_transition_requests
  - machinelearning
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

Creates, updates, deletes, gets or lists a <code>model_transition_requests</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>model_transition_requests</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.machinelearning.model_transition_requests" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="listtransitionrequests"
    values={[
        { label: 'listtransitionrequests', value: 'listtransitionrequests' }
    ]}
>
<TabItem value="listtransitionrequests">

Fetched all open requests successfully.

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
    <td><CopyableCode code="user_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="activity_type" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="comment" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="creation_timestamp" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="from_stage" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="last_updated_timestamp" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="system_comment" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="to_stage" /></td>
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
    <td><a href="#listtransitionrequests"><CopyableCode code="listtransitionrequests" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Gets a list of all open stage transition requests for the model version.</td>
</tr>
<tr>
    <td><a href="#createtransitionrequest"><CopyableCode code="createtransitionrequest" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Creates a model version stage transition request.</td>
</tr>
<tr>
    <td><a href="#deletetransitionrequest"><CopyableCode code="deletetransitionrequest" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Cancels a model version stage transition request.</td>
</tr>
<tr>
    <td><a href="#approvetransitionrequest"><CopyableCode code="approvetransitionrequest" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Approves a model version stage transition request.</td>
</tr>
<tr>
    <td><a href="#rejecttransitionrequest"><CopyableCode code="rejecttransitionrequest" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Rejects a model version stage transition request.</td>
</tr>
<tr>
    <td><a href="#transitionstage"><CopyableCode code="transitionstage" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Transition a model version's stage. This is a Databricks workspace version of the</td>
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
    defaultValue="listtransitionrequests"
    values={[
        { label: 'listtransitionrequests', value: 'listtransitionrequests' }
    ]}
>
<TabItem value="listtransitionrequests">

Gets a list of all open stage transition requests for the model version.

```sql
SELECT
id,
user_id,
activity_type,
comment,
creation_timestamp,
from_stage,
last_updated_timestamp,
system_comment,
to_stage
FROM databricks_workspace.machinelearning.model_transition_requests
WHERE deployment_name = '{{ deployment_name }}' -- required;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="createtransitionrequest"
    values={[
        { label: 'createtransitionrequest', value: 'createtransitionrequest' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="createtransitionrequest">

Creates a model version stage transition request.

```sql
INSERT INTO databricks_workspace.machinelearning.model_transition_requests (
data__name,
data__version,
data__stage,
data__comment,
deployment_name
)
SELECT 
'{{ name }}',
'{{ version }}',
'{{ stage }}',
'{{ comment }}',
'{{ deployment_name }}'
RETURNING
request
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: model_transition_requests
  props:
    - name: deployment_name
      value: string
      description: Required parameter for the model_transition_requests resource.
    - name: name
      value: required
    - name: version
      value: string
    - name: stage
      value: required
    - name: comment
      value: string
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="deletetransitionrequest"
    values={[
        { label: 'deletetransitionrequest', value: 'deletetransitionrequest' }
    ]}
>
<TabItem value="deletetransitionrequest">

Cancels a model version stage transition request.

```sql
DELETE FROM databricks_workspace.machinelearning.model_transition_requests
WHERE deployment_name = '{{ deployment_name }}' --required;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="approvetransitionrequest"
    values={[
        { label: 'approvetransitionrequest', value: 'approvetransitionrequest' },
        { label: 'rejecttransitionrequest', value: 'rejecttransitionrequest' },
        { label: 'transitionstage', value: 'transitionstage' }
    ]}
>
<TabItem value="approvetransitionrequest">

Approves a model version stage transition request.

```sql
EXEC databricks_workspace.machinelearning.model_transition_requests.approvetransitionrequest 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"name": "{{ name }}", 
"version": "{{ version }}", 
"stage": "{{ stage }}", 
"archive_existing_versions": "{{ archive_existing_versions }}", 
"comment": "{{ comment }}"
}';
```
</TabItem>
<TabItem value="rejecttransitionrequest">

Rejects a model version stage transition request.

```sql
EXEC databricks_workspace.machinelearning.model_transition_requests.rejecttransitionrequest 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"name": "{{ name }}", 
"version": "{{ version }}", 
"stage": "{{ stage }}", 
"comment": "{{ comment }}"
}';
```
</TabItem>
<TabItem value="transitionstage">

Transition a model version's stage. This is a Databricks workspace version of the

```sql
EXEC databricks_workspace.machinelearning.model_transition_requests.transitionstage 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"name": "{{ name }}", 
"version": "{{ version }}", 
"stage": "{{ stage }}", 
"archive_existing_versions": "{{ archive_existing_versions }}", 
"comment": "{{ comment }}"
}';
```
</TabItem>
</Tabs>

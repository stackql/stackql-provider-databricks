--- 
title: model_web_hooks
hide_title: false
hide_table_of_contents: false
keywords:
  - model_web_hooks
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

Creates, updates, deletes, gets or lists a <code>model_web_hooks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>model_web_hooks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.machinelearning.model_web_hooks" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="listwebhooks"
    values={[
        { label: 'listwebhooks', value: 'listwebhooks' }
    ]}
>
<TabItem value="listwebhooks">

Registry webhooks listed successfully.

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
    <td><CopyableCode code="model_name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="creation_timestamp" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="events" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="http_url_spec" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="last_updated_timestamp" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
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
    <td><a href="#listwebhooks"><CopyableCode code="listwebhooks" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>This endpoint is in Public Preview.</td>
</tr>
<tr>
    <td><a href="#createwebhook"><CopyableCode code="createwebhook" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>: This endpoint is in Public Preview.</td>
</tr>
<tr>
    <td><a href="#updatewebhook"><CopyableCode code="updatewebhook" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>This endpoint is in Public Preview.</td>
</tr>
<tr>
    <td><a href="#deletewebhook"><CopyableCode code="deletewebhook" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>This endpoint is in Public Preview.</td>
</tr>
<tr>
    <td><a href="#testregistrywebhook"><CopyableCode code="testregistrywebhook" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>This endpoint is in Public Preview.</td>
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
    defaultValue="listwebhooks"
    values={[
        { label: 'listwebhooks', value: 'listwebhooks' }
    ]}
>
<TabItem value="listwebhooks">

This endpoint is in Public Preview.

```sql
SELECT
id,
model_name,
creation_timestamp,
description,
events,
http_url_spec,
last_updated_timestamp,
status
FROM databricks_workspace.machinelearning.model_web_hooks
WHERE deployment_name = '{{ deployment_name }}' -- required;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="createwebhook"
    values={[
        { label: 'createwebhook', value: 'createwebhook' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="createwebhook">

: This endpoint is in Public Preview.

```sql
INSERT INTO databricks_workspace.machinelearning.model_web_hooks (
data__events,
data__model_name,
data__description,
data__status,
data__job_spec,
data__http_url_spec,
deployment_name
)
SELECT 
'{{ events }}',
'{{ model_name }}',
'{{ description }}',
'{{ status }}',
'{{ job_spec }}',
'{{ http_url_spec }}',
'{{ deployment_name }}'
RETURNING
webhook
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: model_web_hooks
  props:
    - name: deployment_name
      value: string
      description: Required parameter for the model_web_hooks resource.
    - name: events
      value: required
    - name: model_name
      value: Array of string
    - name: description
      value: string
    - name: status
      value: string
    - name: job_spec
      value: object
    - name: http_url_spec
      value: object
```
</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="updatewebhook"
    values={[
        { label: 'updatewebhook', value: 'updatewebhook' }
    ]}
>
<TabItem value="updatewebhook">

This endpoint is in Public Preview.

```sql
UPDATE databricks_workspace.machinelearning.model_web_hooks
SET 
data__id = '{{ id }}',
data__events = '{{ events }}',
data__description = '{{ description }}',
data__status = '{{ status }}',
data__http_url_spec = '{{ http_url_spec }}',
data__job_spec = '{{ job_spec }}'
WHERE 
deployment_name = '{{ deployment_name }}' --required
RETURNING
webhook;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="deletewebhook"
    values={[
        { label: 'deletewebhook', value: 'deletewebhook' }
    ]}
>
<TabItem value="deletewebhook">

This endpoint is in Public Preview.

```sql
DELETE FROM databricks_workspace.machinelearning.model_web_hooks
WHERE deployment_name = '{{ deployment_name }}' --required;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="testregistrywebhook"
    values={[
        { label: 'testregistrywebhook', value: 'testregistrywebhook' }
    ]}
>
<TabItem value="testregistrywebhook">

This endpoint is in Public Preview.

```sql
EXEC databricks_workspace.machinelearning.model_web_hooks.testregistrywebhook 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"id": "{{ id }}", 
"event": "{{ event }}"
}';
```
</TabItem>
</Tabs>

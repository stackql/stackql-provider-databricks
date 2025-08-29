--- 
title: commands
hide_title: false
hide_table_of_contents: false
keywords:
  - commands
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

Creates, updates, deletes, gets or lists a <code>commands</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>commands</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.compute.commands" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="commandstatus"
    values={[
        { label: 'commandstatus', value: 'commandstatus' }
    ]}
>
<TabItem value="commandstatus">

Status was returned successfully.

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
    <td><CopyableCode code="results" /></td>
    <td><code>object</code></td>
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
    <td><a href="#commandstatus"><CopyableCode code="commandstatus" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Gets the status of and, if available, the results from a currently executing command.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Creates an execution context for running cluster commands.</td>
</tr>
<tr>
    <td><a href="#cancel"><CopyableCode code="cancel" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Cancels a currently running command within an execution context.</td>
</tr>
<tr>
    <td><a href="#destroy"><CopyableCode code="destroy" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Deletes an execution context.</td>
</tr>
<tr>
    <td><a href="#execute"><CopyableCode code="execute" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Runs a cluster command in the given execution context, using the provided language.</td>
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
    defaultValue="commandstatus"
    values={[
        { label: 'commandstatus', value: 'commandstatus' }
    ]}
>
<TabItem value="commandstatus">

Gets the status of and, if available, the results from a currently executing command.

```sql
SELECT
id,
results,
status
FROM databricks_workspace.compute.commands
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

Creates an execution context for running cluster commands.

```sql
INSERT INTO databricks_workspace.compute.commands (
data__clusterId,
data__language,
deployment_name
)
SELECT 
'{{ clusterId }}',
'{{ language }}',
'{{ deployment_name }}'
RETURNING
id
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: commands
  props:
    - name: deployment_name
      value: string
      description: Required parameter for the commands resource.
    - name: clusterId
      value: string
    - name: language
      value: string
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="cancel"
    values={[
        { label: 'cancel', value: 'cancel' },
        { label: 'destroy', value: 'destroy' },
        { label: 'execute', value: 'execute' }
    ]}
>
<TabItem value="cancel">

Cancels a currently running command within an execution context.

```sql
EXEC databricks_workspace.compute.commands.cancel 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"clusterId": "{{ clusterId }}", 
"contextId": "{{ contextId }}", 
"commandId": "{{ commandId }}"
}';
```
</TabItem>
<TabItem value="destroy">

Deletes an execution context.

```sql
EXEC databricks_workspace.compute.commands.destroy 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"clusterId": "{{ clusterId }}", 
"contextId": "{{ contextId }}"
}';
```
</TabItem>
<TabItem value="execute">

Runs a cluster command in the given execution context, using the provided language.

```sql
EXEC databricks_workspace.compute.commands.execute 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"clusterId": "{{ clusterId }}", 
"contextId": "{{ contextId }}", 
"language": "{{ language }}", 
"command": "{{ command }}"
}';
```
</TabItem>
</Tabs>

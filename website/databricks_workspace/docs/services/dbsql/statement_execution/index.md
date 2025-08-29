--- 
title: statement_execution
hide_title: false
hide_table_of_contents: false
keywords:
  - statement_execution
  - dbsql
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

Creates, updates, deletes, gets or lists a <code>statement_execution</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>statement_execution</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.dbsql.statement_execution" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="getstatement"
    values={[
        { label: 'getstatement', value: 'getstatement' }
    ]}
>
<TabItem value="getstatement">

StatementResponse contains `statement_id` and `status`; other fields might be absent or present depending on context. In case of an error during execution of the SQL statement -- as opposed to an error while processing the request -- a 200 response is returned with error details in the `status` field.

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
    <td><CopyableCode code="statement_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="manifest" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="result" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>object</code></td>
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
    <td><a href="#getstatement"><CopyableCode code="getstatement" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>This request can be used to poll for the statement's status. When the</td>
</tr>
<tr>
    <td><a href="#cancelexecution"><CopyableCode code="cancelexecution" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Requests that an executing statement be canceled. Callers must poll for status to see the terminal state.</td>
</tr>
<tr>
    <td><a href="#executestatement"><CopyableCode code="executestatement" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Execute a SQL statement and optionally await its results for a specified time.</td>
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
    defaultValue="getstatement"
    values={[
        { label: 'getstatement', value: 'getstatement' }
    ]}
>
<TabItem value="getstatement">

This request can be used to poll for the statement's status. When the

```sql
SELECT
statement_id,
manifest,
result,
status
FROM databricks_workspace.dbsql.statement_execution
WHERE deployment_name = '{{ deployment_name }}' -- required;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="cancelexecution"
    values={[
        { label: 'cancelexecution', value: 'cancelexecution' },
        { label: 'executestatement', value: 'executestatement' }
    ]}
>
<TabItem value="cancelexecution">

Requests that an executing statement be canceled. Callers must poll for status to see the terminal state.

```sql
EXEC databricks_workspace.dbsql.statement_execution.cancelexecution 
@deployment_name='{{ deployment_name }}' --required;
```
</TabItem>
<TabItem value="executestatement">

Execute a SQL statement and optionally await its results for a specified time.

```sql
EXEC databricks_workspace.dbsql.statement_execution.executestatement 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"statement": "{{ statement }}", 
"warehouse_id": "{{ warehouse_id }}", 
"catalog": "{{ catalog }}", 
"schema": "{{ schema }}", 
"row_limit": "{{ row_limit }}", 
"byte_limit": "{{ byte_limit }}", 
"disposition": {{ disposition }}, 
"format": {{ format }}, 
"wait_timeout": "{{ wait_timeout }}", 
"on_wait_timeout": "{{ on_wait_timeout }}", 
"parameters": "{{ parameters }}"
}';
```
</TabItem>
</Tabs>

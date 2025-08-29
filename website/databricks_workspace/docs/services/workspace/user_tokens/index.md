--- 
title: user_tokens
hide_title: false
hide_table_of_contents: false
keywords:
  - user_tokens
  - workspace
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

Creates, updates, deletes, gets or lists a <code>user_tokens</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_tokens</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.workspace.user_tokens" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="listtokens"
    values={[
        { label: 'listtokens', value: 'listtokens' }
    ]}
>
<TabItem value="listtokens">

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
    <td><CopyableCode code="token_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="comment" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="creation_time" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="expiry_time" /></td>
    <td><code>integer</code></td>
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
    <td><a href="#listtokens"><CopyableCode code="listtokens" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Lists all the valid tokens for a user-workspace pair.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Creates and returns a token for a user. If this call is made through token authentication, it creates a token with the same client ID as the authenticated token. If the user's token quota is exceeded, this call returns an error</td>
</tr>
<tr>
    <td><a href="#revoketoken"><CopyableCode code="revoketoken" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Revokes an access token.</td>
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
    defaultValue="listtokens"
    values={[
        { label: 'listtokens', value: 'listtokens' }
    ]}
>
<TabItem value="listtokens">

Lists all the valid tokens for a user-workspace pair.

```sql
SELECT
token_id,
comment,
creation_time,
expiry_time
FROM databricks_workspace.workspace.user_tokens
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

Creates and returns a token for a user. If this call is made through token authentication, it creates a token with the same client ID as the authenticated token. If the user's token quota is exceeded, this call returns an error

```sql
INSERT INTO databricks_workspace.workspace.user_tokens (
data__lifetime_seconds,
data__comment,
deployment_name
)
SELECT 
{{ lifetime_seconds }},
'{{ comment }}',
'{{ deployment_name }}'
RETURNING
token_info,
token_value
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: user_tokens
  props:
    - name: deployment_name
      value: string
      description: Required parameter for the user_tokens resource.
    - name: lifetime_seconds
      value: integer
    - name: comment
      value: string
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="revoketoken"
    values={[
        { label: 'revoketoken', value: 'revoketoken' }
    ]}
>
<TabItem value="revoketoken">

Revokes an access token.

```sql
EXEC databricks_workspace.workspace.user_tokens.revoketoken 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"token_id": "{{ token_id }}"
}';
```
</TabItem>
</Tabs>

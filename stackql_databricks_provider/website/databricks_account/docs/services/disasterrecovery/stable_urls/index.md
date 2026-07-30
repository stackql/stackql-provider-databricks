---
title: stable_urls
hide_title: false
hide_table_of_contents: false
keywords:
  - stable_urls
  - disasterrecovery
  - databricks_account
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage databricks_account resources using SQL
custom_edit_url: null
image: /img/stackql-databricks_account-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import SchemaTable from '@site/src/components/SchemaTable/SchemaTable';

Creates, updates, deletes, gets or lists a <code>stable_urls</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="stable_urls" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.disasterrecovery.stable_urls" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' },
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "Fully qualified resource name. Format: accounts/&#123;account_id&#125;/stable-urls/&#123;stable_url_id&#125;."
  },
  {
    "name": "effective_workspace_id",
    "type": "string",
    "description": "The workspace this stable URL currently routes to. Set to ``initial_workspace_id`` at creation, advanced to the failover group's primary while attached (including across a failover), and preserved when the stable URL is detached from its failover group. Read this to see where an unattached stable URL points: after a failover followed by a detach it reflects the post-failover primary, not ``initial_workspace_id``."
  },
  {
    "name": "initial_workspace_id",
    "type": "string",
    "description": "The workspace this stable URL is initially bound to. Used only in Create requests to associate the stable URL with a workspace. Not returned in responses."
  },
  {
    "name": "stable_workspace_id",
    "type": "string",
    "description": "The stable workspace ID for this stable URL. Generated on creation and immutable thereafter; identifies the URL across failovers and is the same value embedded in the ``url`` (as the ``w=`` query parameter for SPOG URLs, or in the ``conn-&lt;id&gt;`` hostname for Private-Link URLs)."
  },
  {
    "name": "failover_group_name",
    "type": "string",
    "description": "Fully qualified resource name of the FailoverGroup this stable URL is currently linked to, in the format ``accounts/&#123;account_id&#125;/failover-groups/&#123;failover_group_id&#125;``. Empty when the stable URL is not attached to any failover group."
  },
  {
    "name": "url",
    "type": "string",
    "description": "The stable URL endpoint. Generated on creation and immutable thereafter. For non-Private-Link workspaces this is ``https://&lt;spog_host&gt;/?w=&lt;connection_id&gt;``. For Private-Link workspaces this is the per-connection hostname."
  }
]} />
</TabItem>
<TabItem value="get">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "Fully qualified resource name. Format: accounts/&#123;account_id&#125;/stable-urls/&#123;stable_url_id&#125;."
  },
  {
    "name": "effective_workspace_id",
    "type": "string",
    "description": "The workspace this stable URL currently routes to. Set to ``initial_workspace_id`` at creation, advanced to the failover group's primary while attached (including across a failover), and preserved when the stable URL is detached from its failover group. Read this to see where an unattached stable URL points: after a failover followed by a detach it reflects the post-failover primary, not ``initial_workspace_id``."
  },
  {
    "name": "initial_workspace_id",
    "type": "string",
    "description": "The workspace this stable URL is initially bound to. Used only in Create requests to associate the stable URL with a workspace. Not returned in responses."
  },
  {
    "name": "stable_workspace_id",
    "type": "string",
    "description": "The stable workspace ID for this stable URL. Generated on creation and immutable thereafter; identifies the URL across failovers and is the same value embedded in the ``url`` (as the ``w=`` query parameter for SPOG URLs, or in the ``conn-&lt;id&gt;`` hostname for Private-Link URLs)."
  },
  {
    "name": "failover_group_name",
    "type": "string",
    "description": "Fully qualified resource name of the FailoverGroup this stable URL is currently linked to, in the format ``accounts/&#123;account_id&#125;/failover-groups/&#123;failover_group_id&#125;``. Empty when the stable URL is not attached to any failover group."
  },
  {
    "name": "url",
    "type": "string",
    "description": "The stable URL endpoint. Generated on creation and immutable thereafter. For non-Private-Link workspaces this is ``https://&lt;spog_host&gt;/?w=&lt;connection_id&gt;``. For Private-Link workspaces this is the per-connection hostname."
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
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-parent"><code>parent</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>List stable URLs for an account.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-name"><code>name</code></a></td>
    <td></td>
    <td>Get a stable URL.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-parent"><code>parent</code></a>, <a href="#parameter-stable_url_id"><code>stable_url_id</code></a>, <a href="#parameter-stable_url"><code>stable_url</code></a></td>
    <td><a href="#parameter-validate_only"><code>validate_only</code></a></td>
    <td>Create a new stable URL.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-name"><code>name</code></a></td>
    <td></td>
    <td>Delete a stable URL.</td>
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
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The fully qualified resource name. Format: accounts/&#123;account_id&#125;/stable-urls/&#123;stable_url_id&#125;.</td>
</tr>
<tr id="parameter-parent">
    <td><CopyableCode code="parent" /></td>
    <td><code>string</code></td>
    <td>The parent resource. Format: accounts/&#123;account_id&#125;.</td>
</tr>
<tr id="parameter-stable_url_id">
    <td><CopyableCode code="stable_url_id" /></td>
    <td><code>string</code></td>
    <td>Client-provided identifier for the stable URL. Used to construct the resource name as &#123;parent&#125;/stable-urls/&#123;stable_url_id&#125;.</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of stable URLs to return per page: - when set to a value greater than 0, the page length is the minimum of this value and a server configured value; - when set to 0 or unset, the page length is set to a server configured value (recommended); - when set to a value less than 0, an invalid parameter error is returned.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Page token received from a previous ListStableUrls call. Provide this to retrieve the subsequent page.</td>
</tr>
<tr id="parameter-validate_only">
    <td><CopyableCode code="validate_only" /></td>
    <td><code>boolean</code></td>
    <td>When true, validates the request without creating the stable URL.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' },
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="list">

List stable URLs for an account.

```sql
SELECT
name,
effective_workspace_id,
initial_workspace_id,
stable_workspace_id,
failover_group_name,
url
FROM databricks_account.disasterrecovery.stable_urls
WHERE parent = '{{ parent }}' -- required
AND page_size = '{{ page_size }}'
AND page_token = '{{ page_token }}'
;
```
</TabItem>
<TabItem value="get">

Get a stable URL.

```sql
SELECT
name,
effective_workspace_id,
initial_workspace_id,
stable_workspace_id,
failover_group_name,
url
FROM databricks_account.disasterrecovery.stable_urls
WHERE name = '{{ name }}' -- required
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

Create a new stable URL.

```sql
INSERT INTO databricks_account.disasterrecovery.stable_urls (
stable_url,
parent,
stable_url_id,
validate_only
)
SELECT 
'{{ stable_url }}' /* required */,
'{{ parent }}',
'{{ stable_url_id }}',
'{{ validate_only }}'
RETURNING
name,
effective_workspace_id,
initial_workspace_id,
stable_workspace_id,
failover_group_name,
url
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: stable_urls
  props:
    - name: parent
      value: "{{ parent }}"
      description: Required parameter for the stable_urls resource.
    - name: stable_url_id
      value: "{{ stable_url_id }}"
      description: Required parameter for the stable_urls resource.
    - name: stable_url
      description: |
        The stable URL to create.
      value:
        initial_workspace_id: "{{ initial_workspace_id }}"
        effective_workspace_id: "{{ effective_workspace_id }}"
        failover_group_name: "{{ failover_group_name }}"
        name: "{{ name }}"
        stable_workspace_id: "{{ stable_workspace_id }}"
        url: "{{ url }}"
    - name: validate_only
      value: {{ validate_only }}
      description: When true, validates the request without creating the stable URL.
      description: When true, validates the request without creating the stable URL.
`}</CodeBlock>

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

Delete a stable URL.

```sql
DELETE FROM databricks_account.disasterrecovery.stable_urls
WHERE name = '{{ name }}' --required
;
```
</TabItem>
</Tabs>

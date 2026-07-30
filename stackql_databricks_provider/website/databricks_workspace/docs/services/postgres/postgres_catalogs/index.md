---
title: postgres_catalogs
hide_title: false
hide_table_of_contents: false
keywords:
  - postgres_catalogs
  - postgres
  - databricks_workspace
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage databricks_workspace resources using SQL
custom_edit_url: null
image: /img/stackql-databricks_workspace-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import SchemaTable from '@site/src/components/SchemaTable/SchemaTable';

Creates, updates, deletes, gets or lists a <code>postgres_catalogs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="postgres_catalogs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.postgres.postgres_catalogs" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


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
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-catalog_id"><code>catalog_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-catalog"><code>catalog</code></a></td>
    <td></td>
    <td>Register a Postgres database in the Unity Catalog.</td>
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
<tr id="parameter-catalog_id">
    <td><CopyableCode code="catalog_id" /></td>
    <td><code>string</code></td>
    <td>The ID in the Unity Catalog. It becomes the full resource name, for example "my_catalog" becomes "catalogs/my_catalog".</td>
</tr>
<tr id="parameter-deployment_name">
    <td><CopyableCode code="deployment_name" /></td>
    <td><code>string</code></td>
    <td>The Databricks Workspace Deployment Name (default: dbc-abcd0123-a1bc)</td>
</tr>
</tbody>
</table>

## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Register a Postgres database in the Unity Catalog.

```sql
INSERT INTO databricks_workspace.postgres.postgres_catalogs (
catalog,
catalog_id,
deployment_name
)
SELECT 
'{{ catalog }}' /* required */,
'{{ catalog_id }}',
'{{ deployment_name }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: postgres_catalogs
  props:
    - name: catalog_id
      value: "{{ catalog_id }}"
      description: Required parameter for the postgres_catalogs resource.
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the postgres_catalogs resource.
    - name: catalog
      value:
        catalog_id: "{{ catalog_id }}"
        create_time: "{{ create_time }}"
        name: "{{ name }}"
        spec:
          postgres_database: "{{ postgres_database }}"
          branch: "{{ branch }}"
          create_database_if_missing: {{ create_database_if_missing }}
        status:
          branch: "{{ branch }}"
          postgres_database: "{{ postgres_database }}"
          project: "{{ project }}"
        uid: "{{ uid }}"
        update_time: "{{ update_time }}"
`}</CodeBlock>

</TabItem>
</Tabs>

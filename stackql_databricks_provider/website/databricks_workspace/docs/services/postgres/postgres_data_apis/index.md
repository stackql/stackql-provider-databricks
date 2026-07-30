---
title: postgres_data_apis
hide_title: false
hide_table_of_contents: false
keywords:
  - postgres_data_apis
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

Creates, updates, deletes, gets or lists a <code>postgres_data_apis</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="postgres_data_apis" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.postgres.postgres_data_apis" /></td></tr>
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
    <td><a href="#parameter-parent"><code>parent</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-data_api"><code>data_api</code></a></td>
    <td></td>
    <td>Enable Data API for a database.</td>
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
<tr id="parameter-parent">
    <td><CopyableCode code="parent" /></td>
    <td><code>string</code></td>
    <td>Parent database: projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;/databases/&#123;database_id&#125;</td>
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

Enable Data API for a database.

```sql
INSERT INTO databricks_workspace.postgres.postgres_data_apis (
data_api,
parent,
deployment_name
)
SELECT 
'{{ data_api }}' /* required */,
'{{ parent }}',
'{{ deployment_name }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: postgres_data_apis
  props:
    - name: parent
      value: "{{ parent }}"
      description: Required parameter for the postgres_data_apis resource.
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the postgres_data_apis resource.
    - name: data_api
      description: |
        The Data API configuration to create.
      value:
        create_time: "{{ create_time }}"
        name: "{{ name }}"
        parent: "{{ parent }}"
        spec:
          db_aggregates_enabled: {{ db_aggregates_enabled }}
          db_anon_role: "{{ db_anon_role }}"
          db_extra_search_path:
            - "{{ db_extra_search_path }}"
          db_max_rows: {{ db_max_rows }}
          db_schemas:
            - "{{ db_schemas }}"
          jwt_cache_max_lifetime: "{{ jwt_cache_max_lifetime }}"
          jwt_role_claim_key: "{{ jwt_role_claim_key }}"
          openapi_mode: "{{ openapi_mode }}"
          server_cors_allowed_origins:
            - "{{ server_cors_allowed_origins }}"
          server_timing_enabled: {{ server_timing_enabled }}
        status:
          available_schemas:
            - "{{ available_schemas }}"
          db_aggregates_enabled: {{ db_aggregates_enabled }}
          db_anon_role: "{{ db_anon_role }}"
          db_extra_search_path:
            - "{{ db_extra_search_path }}"
          db_max_rows: {{ db_max_rows }}
          db_schemas:
            - "{{ db_schemas }}"
          jwt_cache_max_lifetime: "{{ jwt_cache_max_lifetime }}"
          jwt_role_claim_key: "{{ jwt_role_claim_key }}"
          openapi_mode: "{{ openapi_mode }}"
          server_cors_allowed_origins:
            - "{{ server_cors_allowed_origins }}"
          server_timing_enabled: {{ server_timing_enabled }}
          url: "{{ url }}"
        update_time: "{{ update_time }}"
`}</CodeBlock>

</TabItem>
</Tabs>

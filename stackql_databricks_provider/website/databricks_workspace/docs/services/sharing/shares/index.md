---
title: shares
hide_title: false
hide_table_of_contents: false
keywords:
  - shares
  - sharing
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

Creates, updates, deletes, gets or lists a <code>shares</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="shares" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.sharing.shares" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "Name of the share."
  },
  {
    "name": "serverless_budget_policy_id",
    "type": "string",
    "description": "Serverless budget policy id (can only be created/updated when calling data-sharing service) [Create,Update:IGN]"
  },
  {
    "name": "comment",
    "type": "string",
    "description": ""
  },
  {
    "name": "created_at",
    "type": "integer",
    "description": "Time at which this share was created, in epoch milliseconds."
  },
  {
    "name": "created_by",
    "type": "string",
    "description": "Username of share creator."
  },
  {
    "name": "objects",
    "type": "array",
    "description": "A list of shared data objects within the share.",
    "children": [
      {
        "name": "name",
        "type": "string",
        "description": ""
      },
      {
        "name": "added_at",
        "type": "integer",
        "description": "The time when this data object is added to the share, in epoch milliseconds."
      },
      {
        "name": "added_by",
        "type": "string",
        "description": "Username of the sharer."
      },
      {
        "name": "cdf_enabled",
        "type": "boolean",
        "description": "Whether to enable cdf or indicate if cdf is enabled on the shared object."
      },
      {
        "name": "comment",
        "type": "string",
        "description": "A user-provided comment when adding the data object to the share."
      },
      {
        "name": "content",
        "type": "string",
        "description": "The content of the notebook file when the data object type is NOTEBOOK_FILE. This should be base64 encoded. Required for adding a NOTEBOOK_FILE, optional for updating, ignored for other types."
      },
      {
        "name": "data_object_type",
        "type": "string",
        "description": "The type of the data object. (FEATURE_SPEC, FOREIGN_TABLE, FUNCTION, MATERIALIZED_VIEW, MODEL, NOTEBOOK_FILE, SCHEMA, STREAMING_TABLE, TABLE, VIEW, VOLUME)"
      },
      {
        "name": "global_distribution_status",
        "type": "object",
        "description": "Global Distribution status for the shared asset. Output only. Only set for TABLE objects; absent for all other data object types.",
        "children": [
          {
            "name": "eligible",
            "type": "boolean",
            "description": "Whether this asset meets the structural requirements for global distribution (e.g. asset type, history sharing mode, storage scheme)."
          },
          {
            "name": "status",
            "type": "string",
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (DISABLED, ENABLED)"
          }
        ]
      },
      {
        "name": "history_data_sharing_status",
        "type": "string",
        "description": "Whether to enable or disable sharing of data history. If not specified, the default is **DISABLED**. (DISABLED, ENABLED)"
      },
      {
        "name": "partitions",
        "type": "array",
        "description": "Array of partitions for the shared data.",
        "children": [
          {
            "name": "values",
            "type": "array",
            "description": "",
            "children": [
              {
                "name": "name",
                "type": "string",
                "description": ""
              },
              {
                "name": "op",
                "type": "string",
                "description": "The operator to apply for the value. (EQUAL, LIKE)"
              },
              {
                "name": "recipient_property_key",
                "type": "string",
                "description": "The key of a Delta Sharing recipient's property. For example \"databricks-account-id\". When this field is set, field ``value`` can not be set."
              },
              {
                "name": "value",
                "type": "string",
                "description": "The value of the partition column. When this value is not set, it means ``null`` value. When this field is set, field ``recipient_property_key`` can not be set."
              }
            ]
          }
        ]
      },
      {
        "name": "shared_as",
        "type": "string",
        "description": "A user-provided alias name for table-like data objects within the share. Use this field for table-like objects (for example: TABLE, VIEW, MATERIALIZED_VIEW, STREAMING_TABLE, FOREIGN_TABLE). For non-table objects (for example: VOLUME, MODEL, NOTEBOOK_FILE, FUNCTION), use ``string_shared_as`` instead. Important: For non-table objects, this field must be omitted entirely. Format: Must be a 2-part name ``&lt;schema_name&gt;.&lt;table_name&gt;`` (e.g., \"sales_schema.orders_table\") - Both schema and table names must contain only alphanumeric characters and underscores - No periods, spaces, forward slashes, or control characters are allowed within each part - Do not include the catalog name (use 2 parts, not 3) Behavior: - If not provided, the service automatically generates the alias as ``&lt;schema&gt;.&lt;table&gt;`` from the object's original name - If you don't want to specify this field, omit it entirely from the request (do not pass an empty string) - The ``shared_as`` name must be unique within the share Examples: - Valid: \"analytics_schema.customer_view\" - Invalid: \"catalog.analytics_schema.customer_view\" (3 parts not allowed) - Invalid: \"analytics-schema.customer-view\" (hyphens not allowed)"
      },
      {
        "name": "start_version",
        "type": "integer",
        "description": "The start version associated with the object. This allows data providers to control the lowest object version that is accessible by clients. If specified, clients can query snapshots or changes for versions &gt;= start_version. If not specified, clients can only query starting from the version of the object at the time it was added to the share. NOTE: The start_version should be &lt;= the ``current`` version of the object."
      },
      {
        "name": "status",
        "type": "string",
        "description": "One of: **ACTIVE**, **PERMISSION_DENIED**. (ACTIVE, PERMISSION_DENIED)"
      },
      {
        "name": "string_shared_as",
        "type": "string",
        "description": "A user-provided alias name for non-table data objects within the share. Use this field for non-table objects (for example: VOLUME, MODEL, NOTEBOOK_FILE, FUNCTION). For table-like objects (for example: TABLE, VIEW, MATERIALIZED_VIEW, STREAMING_TABLE, FOREIGN_TABLE), use ``shared_as`` instead. Important: For table-like objects, this field must be omitted entirely. Format: - For VOLUME: Must be a 2-part name ``&lt;schema_name&gt;.&lt;volume_name&gt;`` (e.g., \"data_schema.ml_models\") - For FUNCTION: Must be a 2-part name ``&lt;schema_name&gt;.&lt;function_name&gt;`` (e.g., \"udf_schema.calculate_tax\") - For MODEL: Must be a 2-part name ``&lt;schema_name&gt;.&lt;model_name&gt;`` (e.g., \"models.prediction_model\") - For NOTEBOOK_FILE: Should be the notebook file name (e.g., \"analysis_notebook.py\") - All names must contain only alphanumeric characters and underscores - No periods, spaces, forward slashes, or control characters are allowed within each part Behavior: - If not provided, the service automatically generates the alias from the object's original name - If you don't want to specify this field, omit it entirely from the request (do not pass an empty string) - The ``string_shared_as`` name must be unique for objects of the same type within the share Examples: - Valid for VOLUME: \"data_schema.training_data\" - Valid for FUNCTION: \"analytics.calculate_revenue\" - Invalid: \"catalog.data_schema.training_data\" (3 parts not allowed for volumes) - Invalid: \"data-schema.training-data\" (hyphens not allowed)"
      }
    ]
  },
  {
    "name": "owner",
    "type": "string",
    "description": "Username of current owner of share."
  },
  {
    "name": "replication_config",
    "type": "object",
    "description": "Configuration for share replication.",
    "children": [
      {
        "name": "enabled",
        "type": "boolean",
        "description": "Whether replication is enabled for the share."
      },
      {
        "name": "schedule",
        "type": "object",
        "description": "Optional schedule describing how often replication runs for this share. When unset, replication runs on a service-default schedule.",
        "children": [
          {
            "name": "interval",
            "type": "object",
            "description": "Fixed-interval replication schedule.",
            "children": [
              {
                "name": "duration",
                "type": "string",
                "description": "How often the share's data should be replicated."
              }
            ]
          }
        ]
      }
    ]
  },
  {
    "name": "storage_location",
    "type": "string",
    "description": "Storage Location URL (full path) for the share."
  },
  {
    "name": "storage_root",
    "type": "string",
    "description": "Storage root URL for the share."
  },
  {
    "name": "updated_at",
    "type": "integer",
    "description": "Time at which this share was updated, in epoch milliseconds."
  },
  {
    "name": "updated_by",
    "type": "string",
    "description": "Username of share updater."
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "Name of the share."
  },
  {
    "name": "serverless_budget_policy_id",
    "type": "string",
    "description": "Serverless budget policy id (can only be created/updated when calling data-sharing service) [Create,Update:IGN]"
  },
  {
    "name": "comment",
    "type": "string",
    "description": ""
  },
  {
    "name": "created_at",
    "type": "integer",
    "description": "Time at which this share was created, in epoch milliseconds."
  },
  {
    "name": "created_by",
    "type": "string",
    "description": "Username of share creator."
  },
  {
    "name": "objects",
    "type": "array",
    "description": "A list of shared data objects within the share.",
    "children": [
      {
        "name": "name",
        "type": "string",
        "description": ""
      },
      {
        "name": "added_at",
        "type": "integer",
        "description": "The time when this data object is added to the share, in epoch milliseconds."
      },
      {
        "name": "added_by",
        "type": "string",
        "description": "Username of the sharer."
      },
      {
        "name": "cdf_enabled",
        "type": "boolean",
        "description": "Whether to enable cdf or indicate if cdf is enabled on the shared object."
      },
      {
        "name": "comment",
        "type": "string",
        "description": "A user-provided comment when adding the data object to the share."
      },
      {
        "name": "content",
        "type": "string",
        "description": "The content of the notebook file when the data object type is NOTEBOOK_FILE. This should be base64 encoded. Required for adding a NOTEBOOK_FILE, optional for updating, ignored for other types."
      },
      {
        "name": "data_object_type",
        "type": "string",
        "description": "The type of the data object. (FEATURE_SPEC, FOREIGN_TABLE, FUNCTION, MATERIALIZED_VIEW, MODEL, NOTEBOOK_FILE, SCHEMA, STREAMING_TABLE, TABLE, VIEW, VOLUME)"
      },
      {
        "name": "global_distribution_status",
        "type": "object",
        "description": "Global Distribution status for the shared asset. Output only. Only set for TABLE objects; absent for all other data object types.",
        "children": [
          {
            "name": "eligible",
            "type": "boolean",
            "description": "Whether this asset meets the structural requirements for global distribution (e.g. asset type, history sharing mode, storage scheme)."
          },
          {
            "name": "status",
            "type": "string",
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (DISABLED, ENABLED)"
          }
        ]
      },
      {
        "name": "history_data_sharing_status",
        "type": "string",
        "description": "Whether to enable or disable sharing of data history. If not specified, the default is **DISABLED**. (DISABLED, ENABLED)"
      },
      {
        "name": "partitions",
        "type": "array",
        "description": "Array of partitions for the shared data.",
        "children": [
          {
            "name": "values",
            "type": "array",
            "description": "",
            "children": [
              {
                "name": "name",
                "type": "string",
                "description": ""
              },
              {
                "name": "op",
                "type": "string",
                "description": "The operator to apply for the value. (EQUAL, LIKE)"
              },
              {
                "name": "recipient_property_key",
                "type": "string",
                "description": "The key of a Delta Sharing recipient's property. For example \"databricks-account-id\". When this field is set, field ``value`` can not be set."
              },
              {
                "name": "value",
                "type": "string",
                "description": "The value of the partition column. When this value is not set, it means ``null`` value. When this field is set, field ``recipient_property_key`` can not be set."
              }
            ]
          }
        ]
      },
      {
        "name": "shared_as",
        "type": "string",
        "description": "A user-provided alias name for table-like data objects within the share. Use this field for table-like objects (for example: TABLE, VIEW, MATERIALIZED_VIEW, STREAMING_TABLE, FOREIGN_TABLE). For non-table objects (for example: VOLUME, MODEL, NOTEBOOK_FILE, FUNCTION), use ``string_shared_as`` instead. Important: For non-table objects, this field must be omitted entirely. Format: Must be a 2-part name ``&lt;schema_name&gt;.&lt;table_name&gt;`` (e.g., \"sales_schema.orders_table\") - Both schema and table names must contain only alphanumeric characters and underscores - No periods, spaces, forward slashes, or control characters are allowed within each part - Do not include the catalog name (use 2 parts, not 3) Behavior: - If not provided, the service automatically generates the alias as ``&lt;schema&gt;.&lt;table&gt;`` from the object's original name - If you don't want to specify this field, omit it entirely from the request (do not pass an empty string) - The ``shared_as`` name must be unique within the share Examples: - Valid: \"analytics_schema.customer_view\" - Invalid: \"catalog.analytics_schema.customer_view\" (3 parts not allowed) - Invalid: \"analytics-schema.customer-view\" (hyphens not allowed)"
      },
      {
        "name": "start_version",
        "type": "integer",
        "description": "The start version associated with the object. This allows data providers to control the lowest object version that is accessible by clients. If specified, clients can query snapshots or changes for versions &gt;= start_version. If not specified, clients can only query starting from the version of the object at the time it was added to the share. NOTE: The start_version should be &lt;= the ``current`` version of the object."
      },
      {
        "name": "status",
        "type": "string",
        "description": "One of: **ACTIVE**, **PERMISSION_DENIED**. (ACTIVE, PERMISSION_DENIED)"
      },
      {
        "name": "string_shared_as",
        "type": "string",
        "description": "A user-provided alias name for non-table data objects within the share. Use this field for non-table objects (for example: VOLUME, MODEL, NOTEBOOK_FILE, FUNCTION). For table-like objects (for example: TABLE, VIEW, MATERIALIZED_VIEW, STREAMING_TABLE, FOREIGN_TABLE), use ``shared_as`` instead. Important: For table-like objects, this field must be omitted entirely. Format: - For VOLUME: Must be a 2-part name ``&lt;schema_name&gt;.&lt;volume_name&gt;`` (e.g., \"data_schema.ml_models\") - For FUNCTION: Must be a 2-part name ``&lt;schema_name&gt;.&lt;function_name&gt;`` (e.g., \"udf_schema.calculate_tax\") - For MODEL: Must be a 2-part name ``&lt;schema_name&gt;.&lt;model_name&gt;`` (e.g., \"models.prediction_model\") - For NOTEBOOK_FILE: Should be the notebook file name (e.g., \"analysis_notebook.py\") - All names must contain only alphanumeric characters and underscores - No periods, spaces, forward slashes, or control characters are allowed within each part Behavior: - If not provided, the service automatically generates the alias from the object's original name - If you don't want to specify this field, omit it entirely from the request (do not pass an empty string) - The ``string_shared_as`` name must be unique for objects of the same type within the share Examples: - Valid for VOLUME: \"data_schema.training_data\" - Valid for FUNCTION: \"analytics.calculate_revenue\" - Invalid: \"catalog.data_schema.training_data\" (3 parts not allowed for volumes) - Invalid: \"data-schema.training-data\" (hyphens not allowed)"
      }
    ]
  },
  {
    "name": "owner",
    "type": "string",
    "description": "Username of current owner of share."
  },
  {
    "name": "replication_config",
    "type": "object",
    "description": "Configuration for share replication.",
    "children": [
      {
        "name": "enabled",
        "type": "boolean",
        "description": "Whether replication is enabled for the share."
      },
      {
        "name": "schedule",
        "type": "object",
        "description": "Optional schedule describing how often replication runs for this share. When unset, replication runs on a service-default schedule.",
        "children": [
          {
            "name": "interval",
            "type": "object",
            "description": "Fixed-interval replication schedule.",
            "children": [
              {
                "name": "duration",
                "type": "string",
                "description": "How often the share's data should be replicated."
              }
            ]
          }
        ]
      }
    ]
  },
  {
    "name": "storage_location",
    "type": "string",
    "description": "Storage Location URL (full path) for the share."
  },
  {
    "name": "storage_root",
    "type": "string",
    "description": "Storage root URL for the share."
  },
  {
    "name": "updated_at",
    "type": "integer",
    "description": "Time at which this share was updated, in epoch milliseconds."
  },
  {
    "name": "updated_by",
    "type": "string",
    "description": "Username of share updater."
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-include_shared_data"><code>include_shared_data</code></a></td>
    <td>Gets a data object share from the metastore. The caller must have the USE_SHARE privilege on the</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-filter_by_genie_space_id"><code>filter_by_genie_space_id</code></a>, <a href="#parameter-max_results"><code>max_results</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Gets an array of data object shares from the metastore. If the caller has the USE_SHARE privilege on</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-name"><code>name</code></a></td>
    <td></td>
    <td>Creates a new share for data objects. Data objects can be added after creation with **update**. The</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Updates the share with the changes and data objects in the request. The caller must be the owner of</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Deletes a data object share from the metastore. The caller must be an owner of the share.</td>
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
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the share.</td>
</tr>
<tr id="parameter-filter_by_genie_space_id">
    <td><CopyableCode code="filter_by_genie_space_id" /></td>
    <td><code>string</code></td>
    <td>When set, only shares that contain the Genie space with this id are returned. The filter is applied at the data-sharing layer after MC returns the page, so the resulting page may be smaller than ``max_results``. Intended for the provider Genie space page's "Shared with N recipients" lookup; not optimized for providers with many shares.</td>
</tr>
<tr id="parameter-include_shared_data">
    <td><CopyableCode code="include_shared_data" /></td>
    <td><code>boolean</code></td>
    <td>Query for data to include in the share.</td>
</tr>
<tr id="parameter-max_results">
    <td><CopyableCode code="max_results" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of shares to return. - when set to 0, the page length is set to a server configured value (recommended); - when set to a value greater than 0, the page length is the minimum of this value and a server configured value; - when set to a value less than 0, an invalid parameter error is returned; - If not set, all valid shares are returned (not recommended). - Note: The number of returned shares might be less than the specified max_results size, even zero. The only definitive indication that no further shares can be fetched is when the next_page_token is unset from the response.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Opaque pagination token to go to next page based on previous query.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Gets a data object share from the metastore. The caller must have the USE_SHARE privilege on the

```sql
SELECT
name,
serverless_budget_policy_id,
comment,
created_at,
created_by,
objects,
owner,
replication_config,
storage_location,
storage_root,
updated_at,
updated_by
FROM databricks_workspace.sharing.shares
WHERE name = '{{ name }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND include_shared_data = '{{ include_shared_data }}'
;
```
</TabItem>
<TabItem value="list">

Gets an array of data object shares from the metastore. If the caller has the USE_SHARE privilege on

```sql
SELECT
name,
serverless_budget_policy_id,
comment,
created_at,
created_by,
objects,
owner,
replication_config,
storage_location,
storage_root,
updated_at,
updated_by
FROM databricks_workspace.sharing.shares
WHERE deployment_name = '{{ deployment_name }}' -- required
AND filter_by_genie_space_id = '{{ filter_by_genie_space_id }}'
AND max_results = '{{ max_results }}'
AND page_token = '{{ page_token }}'
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

Creates a new share for data objects. Data objects can be added after creation with **update**. The

```sql
INSERT INTO databricks_workspace.sharing.shares (
name,
comment,
replication_config,
serverless_budget_policy_id,
storage_root,
deployment_name
)
SELECT 
'{{ name }}' /* required */,
'{{ comment }}',
'{{ replication_config }}',
'{{ serverless_budget_policy_id }}',
'{{ storage_root }}',
'{{ deployment_name }}'
RETURNING
name,
serverless_budget_policy_id,
comment,
created_at,
created_by,
objects,
owner,
replication_config,
storage_location,
storage_root,
updated_at,
updated_by
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: shares
  props:
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the shares resource.
    - name: name
      value: "{{ name }}"
      description: |
        Name of the share.
    - name: comment
      value: "{{ comment }}"
      description: |
        User-provided free-form text description.
    - name: replication_config
      description: |
        Configuration for share replication.
      value:
        enabled: {{ enabled }}
        schedule:
          interval:
            duration: "{{ duration }}"
    - name: serverless_budget_policy_id
      value: "{{ serverless_budget_policy_id }}"
      description: |
        Serverless budget policy id (can only be created/updated when calling data-sharing service) [Create,Update:IGN]
    - name: storage_root
      value: "{{ storage_root }}"
      description: |
        Storage root URL for the share.
`}</CodeBlock>

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

Updates the share with the changes and data objects in the request. The caller must be the owner of

```sql
UPDATE databricks_workspace.sharing.shares
SET 
comment = '{{ comment }}',
new_name = '{{ new_name }}',
owner = '{{ owner }}',
serverless_budget_policy_id = '{{ serverless_budget_policy_id }}',
storage_root = '{{ storage_root }}',
updates = '{{ updates }}'
WHERE 
name = '{{ name }}' --required
AND deployment_name = '{{ deployment_name }}' --required
RETURNING
name,
serverless_budget_policy_id,
comment,
created_at,
created_by,
objects,
owner,
replication_config,
storage_location,
storage_root,
updated_at,
updated_by;
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

Deletes a data object share from the metastore. The caller must be an owner of the share.

```sql
DELETE FROM databricks_workspace.sharing.shares
WHERE name = '{{ name }}' --required
AND deployment_name = '{{ deployment_name }}' --required
;
```
</TabItem>
</Tabs>

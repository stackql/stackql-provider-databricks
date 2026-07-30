---
title: genie
hide_title: false
hide_table_of_contents: false
keywords:
  - genie
  - dashboards
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

Creates, updates, deletes, gets or lists a <code>genie</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="genie" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.dashboards.genie" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="genie_list_message_comments"
    values={[
        { label: 'genie_list_message_comments', value: 'genie_list_message_comments' },
        { label: 'genie_list_conversation_comments', value: 'genie_list_conversation_comments' },
        { label: 'genie_download_message_attachment_visualization', value: 'genie_download_message_attachment_visualization' },
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="genie_list_message_comments">

<SchemaTable fields={[
  {
    "name": "comments",
    "type": "array",
    "description": "",
    "children": [
      {
        "name": "space_id",
        "type": "string",
        "description": "Genie space ID"
      },
      {
        "name": "conversation_id",
        "type": "string",
        "description": "Conversation ID"
      },
      {
        "name": "message_id",
        "type": "string",
        "description": "Message ID"
      },
      {
        "name": "message_comment_id",
        "type": "string",
        "description": "Comment ID"
      },
      {
        "name": "content",
        "type": "string",
        "description": "Comment text content"
      },
      {
        "name": "created_timestamp",
        "type": "integer",
        "description": "Timestamp when the comment was created"
      },
      {
        "name": "user_id",
        "type": "integer",
        "description": "ID of the user who created the comment"
      }
    ]
  },
  {
    "name": "next_page_token",
    "type": "string",
    "description": "Token to get the next page of results."
  }
]} />
</TabItem>
<TabItem value="genie_list_conversation_comments">

<SchemaTable fields={[
  {
    "name": "comments",
    "type": "array",
    "description": "",
    "children": [
      {
        "name": "space_id",
        "type": "string",
        "description": "Genie space ID"
      },
      {
        "name": "conversation_id",
        "type": "string",
        "description": "Conversation ID"
      },
      {
        "name": "message_id",
        "type": "string",
        "description": "Message ID"
      },
      {
        "name": "message_comment_id",
        "type": "string",
        "description": "Comment ID"
      },
      {
        "name": "content",
        "type": "string",
        "description": "Comment text content"
      },
      {
        "name": "created_timestamp",
        "type": "integer",
        "description": "Timestamp when the comment was created"
      },
      {
        "name": "user_id",
        "type": "integer",
        "description": "ID of the user who created the comment"
      }
    ]
  },
  {
    "name": "next_page_token",
    "type": "string",
    "description": "Token to get the next page of results."
  }
]} />
</TabItem>
<TabItem value="genie_download_message_attachment_visualization">

<SchemaTable fields={[]} />
</TabItem>
<TabItem value="get">

<SchemaTable fields={[
  {
    "name": "space_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "warehouse_id",
    "type": "string",
    "description": "Warehouse associated with the Genie Space"
  },
  {
    "name": "description",
    "type": "string",
    "description": "Description of the Genie Space"
  },
  {
    "name": "etag",
    "type": "string",
    "description": "ETag for this space. Pass this value back in the update request to prevent overwriting concurrent changes."
  },
  {
    "name": "parent_path",
    "type": "string",
    "description": "Parent folder path of the Genie Space"
  },
  {
    "name": "serialized_space",
    "type": "string",
    "description": "The contents of the Genie Space in serialized string form. This field is excluded in List Genie spaces responses. Use the [Get Genie Space](:method:genie/getspace) API to retrieve an example response, which includes the ``serialized_space`` field. This field provides the structure of the JSON string that represents the space's layout and components."
  },
  {
    "name": "title",
    "type": "string",
    "description": "Title of the Genie Space"
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "next_page_token",
    "type": "string",
    "description": ""
  },
  {
    "name": "spaces",
    "type": "array",
    "description": "List of Genie spaces",
    "children": [
      {
        "name": "space_id",
        "type": "string",
        "description": ""
      },
      {
        "name": "title",
        "type": "string",
        "description": "Title of the Genie Space"
      },
      {
        "name": "description",
        "type": "string",
        "description": "Description of the Genie Space"
      },
      {
        "name": "etag",
        "type": "string",
        "description": "ETag for this space. Pass this value back in the update request to prevent overwriting concurrent changes."
      },
      {
        "name": "parent_path",
        "type": "string",
        "description": "Parent folder path of the Genie Space"
      },
      {
        "name": "serialized_space",
        "type": "string",
        "description": "The contents of the Genie Space in serialized string form. This field is excluded in List Genie spaces responses. Use the [Get Genie Space](:method:genie/getspace) API to retrieve an example response, which includes the ``serialized_space`` field. This field provides the structure of the JSON string that represents the space's layout and components."
      },
      {
        "name": "warehouse_id",
        "type": "string",
        "description": "Warehouse associated with the Genie Space"
      }
    ]
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
    <td><a href="#genie_list_message_comments"><CopyableCode code="genie_list_message_comments" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-space_id"><code>space_id</code></a>, <a href="#parameter-conversation_id"><code>conversation_id</code></a>, <a href="#parameter-message_id"><code>message_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>List comments on a specific conversation message.</td>
</tr>
<tr>
    <td><a href="#genie_list_conversation_comments"><CopyableCode code="genie_list_conversation_comments" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-space_id"><code>space_id</code></a>, <a href="#parameter-conversation_id"><code>conversation_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>List all comments across all messages in a conversation.</td>
</tr>
<tr>
    <td><a href="#genie_download_message_attachment_visualization"><CopyableCode code="genie_download_message_attachment_visualization" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Download a rendered image of a message visualization attachment. The response body is the raw PNG</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-space_id"><code>space_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-include_serialized_space"><code>include_serialized_space</code></a></td>
    <td>Get details of a Genie Space.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Get list of Genie Spaces.</td>
</tr>
<tr>
    <td><a href="#genie_create_message_comment"><CopyableCode code="genie_create_message_comment" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-space_id"><code>space_id</code></a>, <a href="#parameter-conversation_id"><code>conversation_id</code></a>, <a href="#parameter-message_id"><code>message_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-content"><code>content</code></a></td>
    <td></td>
    <td>Create a comment on a conversation message.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-warehouse_id"><code>warehouse_id</code></a>, <a href="#parameter-serialized_space"><code>serialized_space</code></a></td>
    <td></td>
    <td>Creates a Genie space from a serialized payload.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-space_id"><code>space_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Updates a Genie space with a serialized payload.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-space_id"><code>space_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Move a Genie Space to the trash.</td>
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
<tr id="parameter-conversation_id">
    <td><CopyableCode code="conversation_id" /></td>
    <td><code>string</code></td>
    <td>The ID associated with the conversation.</td>
</tr>
<tr id="parameter-deployment_name">
    <td><CopyableCode code="deployment_name" /></td>
    <td><code>string</code></td>
    <td>The Databricks Workspace Deployment Name (default: dbc-abcd0123-a1bc)</td>
</tr>
<tr id="parameter-message_id">
    <td><CopyableCode code="message_id" /></td>
    <td><code>string</code></td>
    <td>The ID associated with the message.</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The resource name of the attachment to render, in the format ``spaces/&#123;space_id&#125;/conversations/&#123;conversation_id&#125;/messages/&#123;message_id&#125;/attachments/&#123;attachment_id&#125;``.</td>
</tr>
<tr id="parameter-space_id">
    <td><CopyableCode code="space_id" /></td>
    <td><code>string</code></td>
    <td>The ID associated with the Genie space to be sent to the trash.</td>
</tr>
<tr id="parameter-include_serialized_space">
    <td><CopyableCode code="include_serialized_space" /></td>
    <td><code>boolean</code></td>
    <td>Whether to include the serialized space export in the response. Requires at least CAN EDIT permission on the space.</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of spaces to return per page</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Pagination token for getting the next page of results</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="genie_list_message_comments"
    values={[
        { label: 'genie_list_message_comments', value: 'genie_list_message_comments' },
        { label: 'genie_list_conversation_comments', value: 'genie_list_conversation_comments' },
        { label: 'genie_download_message_attachment_visualization', value: 'genie_download_message_attachment_visualization' },
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="genie_list_message_comments">

List comments on a specific conversation message.

```sql
SELECT
comments,
next_page_token
FROM databricks_workspace.dashboards.genie
WHERE space_id = '{{ space_id }}' -- required
AND conversation_id = '{{ conversation_id }}' -- required
AND message_id = '{{ message_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND page_size = '{{ page_size }}'
AND page_token = '{{ page_token }}'
;
```
</TabItem>
<TabItem value="genie_list_conversation_comments">

List all comments across all messages in a conversation.

```sql
SELECT
comments,
next_page_token
FROM databricks_workspace.dashboards.genie
WHERE space_id = '{{ space_id }}' -- required
AND conversation_id = '{{ conversation_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND page_size = '{{ page_size }}'
AND page_token = '{{ page_token }}'
;
```
</TabItem>
<TabItem value="genie_download_message_attachment_visualization">

Download a rendered image of a message visualization attachment. The response body is the raw PNG

```sql
SELECT
*
FROM databricks_workspace.dashboards.genie
WHERE name = '{{ name }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
<TabItem value="get">

Get details of a Genie Space.

```sql
SELECT
space_id,
warehouse_id,
description,
etag,
parent_path,
serialized_space,
title
FROM databricks_workspace.dashboards.genie
WHERE space_id = '{{ space_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND include_serialized_space = '{{ include_serialized_space }}'
;
```
</TabItem>
<TabItem value="list">

Get list of Genie Spaces.

```sql
SELECT
next_page_token,
spaces
FROM databricks_workspace.dashboards.genie
WHERE deployment_name = '{{ deployment_name }}' -- required
AND page_size = '{{ page_size }}'
AND page_token = '{{ page_token }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="genie_create_message_comment"
    values={[
        { label: 'genie_create_message_comment', value: 'genie_create_message_comment' },
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="genie_create_message_comment">

Create a comment on a conversation message.

```sql
INSERT INTO databricks_workspace.dashboards.genie (
content,
space_id,
conversation_id,
message_id,
deployment_name
)
SELECT 
'{{ content }}' /* required */,
'{{ space_id }}',
'{{ conversation_id }}',
'{{ message_id }}',
'{{ deployment_name }}'
RETURNING
conversation_id,
message_comment_id,
message_id,
space_id,
user_id,
content,
created_timestamp
;
```
</TabItem>
<TabItem value="create">

Creates a Genie space from a serialized payload.

```sql
INSERT INTO databricks_workspace.dashboards.genie (
warehouse_id,
serialized_space,
description,
parent_path,
title,
deployment_name
)
SELECT 
'{{ warehouse_id }}' /* required */,
'{{ serialized_space }}' /* required */,
'{{ description }}',
'{{ parent_path }}',
'{{ title }}',
'{{ deployment_name }}'
RETURNING
space_id,
warehouse_id,
description,
etag,
parent_path,
serialized_space,
title
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: genie
  props:
    - name: space_id
      value: "{{ space_id }}"
      description: Required parameter for the genie resource.
    - name: conversation_id
      value: "{{ conversation_id }}"
      description: Required parameter for the genie resource.
    - name: message_id
      value: "{{ message_id }}"
      description: Required parameter for the genie resource.
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the genie resource.
    - name: content
      value: "{{ content }}"
      description: |
        Comment text content.
    - name: warehouse_id
      value: "{{ warehouse_id }}"
      description: |
        Warehouse to associate with the new space
    - name: serialized_space
      value: "{{ serialized_space }}"
      description: |
        The contents of the Genie Space in serialized string form. Use the [Get Genie Space](:method:genie/getspace) API to retrieve an example response, which includes the \`\`serialized_space\`\` field. This field provides the structure of the JSON string that represents the space's layout and components.
    - name: description
      value: "{{ description }}"
      description: |
        Optional description
    - name: parent_path
      value: "{{ parent_path }}"
      description: |
        Parent folder path where the space will be registered
    - name: title
      value: "{{ title }}"
      description: |
        Optional title override
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

Updates a Genie space with a serialized payload.

```sql
UPDATE databricks_workspace.dashboards.genie
SET 
description = '{{ description }}',
etag = '{{ etag }}',
parent_path = '{{ parent_path }}',
serialized_space = '{{ serialized_space }}',
title = '{{ title }}',
warehouse_id = '{{ warehouse_id }}'
WHERE 
space_id = '{{ space_id }}' --required
AND deployment_name = '{{ deployment_name }}' --required
RETURNING
space_id,
warehouse_id,
description,
etag,
parent_path,
serialized_space,
title;
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

Move a Genie Space to the trash.

```sql
DELETE FROM databricks_workspace.dashboards.genie
WHERE space_id = '{{ space_id }}' --required
AND deployment_name = '{{ deployment_name }}' --required
;
```
</TabItem>
</Tabs>

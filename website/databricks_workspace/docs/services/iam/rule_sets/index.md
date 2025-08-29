--- 
title: rule_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - rule_sets
  - iam
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

Creates, updates, deletes, gets or lists a <code>rule_sets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>rule_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.iam.rule_sets" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="getruleset"
    values={[
        { label: 'getruleset', value: 'getruleset' }
    ]}
>
<TabItem value="getruleset">

The rule set was returned successfully.

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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="grant_rules" /></td>
    <td><code>array</code></td>
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
    <td><a href="#getruleset"><CopyableCode code="getruleset" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Get a rule set by its name. A rule set is always attached to a resource and contains a list of access rules on the said resource. Currently only a default rule set for each resource is supported.</td>
</tr>
<tr>
    <td><a href="#updateruleset"><CopyableCode code="updateruleset" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Replace the rules of a rule set. First, use a GET rule set request to read the current version of the rule set before modifying it. This pattern helps prevent conflicts between concurrent updates.</td>
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
    defaultValue="getruleset"
    values={[
        { label: 'getruleset', value: 'getruleset' }
    ]}
>
<TabItem value="getruleset">

Get a rule set by its name. A rule set is always attached to a resource and contains a list of access rules on the said resource. Currently only a default rule set for each resource is supported.

```sql
SELECT
name,
etag,
grant_rules
FROM databricks_workspace.iam.rule_sets
WHERE deployment_name = '{{ deployment_name }}' -- required;
```
</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="updateruleset"
    values={[
        { label: 'updateruleset', value: 'updateruleset' }
    ]}
>
<TabItem value="updateruleset">

Replace the rules of a rule set. First, use a GET rule set request to read the current version of the rule set before modifying it. This pattern helps prevent conflicts between concurrent updates.

```sql
UPDATE databricks_workspace.iam.rule_sets
SET 
data__name = '{{ name }}',
data__rule_set = '{{ rule_set }}'
WHERE 
deployment_name = '{{ deployment_name }}' --required
RETURNING
name,
etag,
grant_rules;
```
</TabItem>
</Tabs>

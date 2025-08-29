--- 
title: job_compliance
hide_title: false
hide_table_of_contents: false
keywords:
  - job_compliance
  - workflows
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

Creates, updates, deletes, gets or lists a <code>job_compliance</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>job_compliance</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.workflows.job_compliance" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="listcompliance"
    values={[
        { label: 'listcompliance', value: 'listcompliance' },
        { label: 'getcompliance', value: 'getcompliance' }
    ]}
>
<TabItem value="listcompliance">

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
    <td><CopyableCode code="job_id" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="is_compliant" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="violations" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="getcompliance">

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
    <td><CopyableCode code="is_compliant" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="violations" /></td>
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
    <td><a href="#listcompliance"><CopyableCode code="listcompliance" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Returns the policy compliance status of all jobs that use a given policy. Jobs could be out of compliance if a cluster policy they use was updated after the job was last edited and its job clusters no longer comply with the updated policy.</td>
</tr>
<tr>
    <td><a href="#getcompliance"><CopyableCode code="getcompliance" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Returns the policy compliance status of a job. Jobs could be out of compliance if a cluster policy they use was updated after the job was last edited and some of its job clusters no longer comply with their updated policies.</td>
</tr>
<tr>
    <td><a href="#enforcecompliance"><CopyableCode code="enforcecompliance" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Updates a job so the job clusters that are created when running the job (specified in</td>
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
    defaultValue="listcompliance"
    values={[
        { label: 'listcompliance', value: 'listcompliance' },
        { label: 'getcompliance', value: 'getcompliance' }
    ]}
>
<TabItem value="listcompliance">

Returns the policy compliance status of all jobs that use a given policy. Jobs could be out of compliance if a cluster policy they use was updated after the job was last edited and its job clusters no longer comply with the updated policy.

```sql
SELECT
job_id,
is_compliant,
violations
FROM databricks_workspace.workflows.job_compliance
WHERE deployment_name = '{{ deployment_name }}' -- required;
```
</TabItem>
<TabItem value="getcompliance">

Returns the policy compliance status of a job. Jobs could be out of compliance if a cluster policy they use was updated after the job was last edited and some of its job clusters no longer comply with their updated policies.

```sql
SELECT
is_compliant,
violations
FROM databricks_workspace.workflows.job_compliance
WHERE deployment_name = '{{ deployment_name }}' -- required;
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="enforcecompliance"
    values={[
        { label: 'enforcecompliance', value: 'enforcecompliance' }
    ]}
>
<TabItem value="enforcecompliance">

Updates a job so the job clusters that are created when running the job (specified in

```sql
REPLACE databricks_workspace.workflows.job_compliance
SET 
data__job_id = '{{ job_id }}',
data__validate_only = {{ validate_only }}
WHERE 
deployment_name = '{{ deployment_name }}' --required
RETURNING
has_changes,
job_cluster_changes,
settings;
```
</TabItem>
</Tabs>

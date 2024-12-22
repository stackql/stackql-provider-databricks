---
title: workspace_permission_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - workspace_permission_assignments
  - iam
  - databricks_account
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Databricks resources using SQL
custom_edit_url: null
image: /img/providers/databricks_account/stackql-databricks-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Operations on a <code>workspace_permission_assignments</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workspace_permission_assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.iam.workspace_permission_assignments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="error" /> | `string` |  |
| <CopyableCode code="permissions" /> | `array` |  |
| <CopyableCode code="principal" /> | `object` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="account_id, workspace_id" /> | Get the permission assignments for the specified Databricks account and Databricks workspace. |
| <CopyableCode code="createorupdate" /> | `INSERT` | <CopyableCode code="account_id, principal_id, workspace_id" /> | Creates or updates the workspace permissions assignment in a given account and workspace for the specified principal. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="account_id, principal_id, workspace_id" /> | Deletes the workspace permissions assignment in a given account and workspace for the specified principal. |

---
title: groups
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - groups
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

Operations on a <code>groups</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.iam.groups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` |  |
| <CopyableCode code="displayName" /> | `string` |  |
| <CopyableCode code="externalId" /> | `string` |  |
| <CopyableCode code="members" /> | `array` |  |
| <CopyableCode code="roles" /> | `array` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="account_id, id" /> | Gets the information for a specific group in the Databricks account. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="account_id" /> | Gets all details of the groups associated with the Databricks account. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="account_id" /> | Creates a group in the Databricks account with a unique name, using the supplied group details. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="account_id, id" /> | Deletes a group from the Databricks account. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="account_id, id" /> | Partially updates the details of a group. |
| <CopyableCode code="update" /> | `REPLACE` | <CopyableCode code="account_id, id" /> | Updates the details of a group by replacing the entire group entity. |

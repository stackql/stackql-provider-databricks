---
title: budgets
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - budgets
  - billing
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

Operations on a <code>budgets</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>budgets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.billing.budgets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="account_id" /> | `string` |  |
| <CopyableCode code="alert_configurations" /> | `array` |  |
| <CopyableCode code="budget_configuration_id" /> | `string` |  |
| <CopyableCode code="create_time" /> | `integer` |  |
| <CopyableCode code="display_name" /> | `string` |  |
| <CopyableCode code="filter" /> | `object` |  |
| <CopyableCode code="update_time" /> | `integer` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="account_id, budget_id" /> | Gets a budget configuration for an account. Both account and budget configuration are specified by ID. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="account_id" /> | Gets all budgets associated with this account. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="account_id" /> | Create a new budget configuration for an account. For full details, see |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="account_id, budget_id" /> | Deletes a budget configuration for an account. Both account and budget configuration are specified by ID. This cannot be undone. |
| <CopyableCode code="update" /> | `REPLACE` | <CopyableCode code="account_id, budget_id" /> | Updates a budget configuration for an account. Both account and budget configuration are specified by ID. |

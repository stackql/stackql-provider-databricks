---
title: usage_dashboards
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - usage_dashboards
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

Operations on a <code>usage_dashboards</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>usage_dashboards</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.billing.usage_dashboards" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="dashboard_id" /> | `string` |  |
| <CopyableCode code="dashboard_url" /> | `string` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="account_id" /> | Get a usage dashboard specified by workspaceId, accountId, and dashboard type. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="account_id" /> | Create a usage dashboard specified by workspaceId, accountId, and dashboard type. |

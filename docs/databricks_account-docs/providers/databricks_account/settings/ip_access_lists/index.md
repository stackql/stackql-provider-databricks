---
title: ip_access_lists
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - ip_access_lists
  - settings
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

Operations on a <code>ip_access_lists</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ip_access_lists</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.settings.ip_access_lists" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="address_count" /> | `integer` |  |
| <CopyableCode code="created_at" /> | `integer` |  |
| <CopyableCode code="created_by" /> | `integer` |  |
| <CopyableCode code="enabled" /> | `boolean` |  |
| <CopyableCode code="ip_addresses" /> | `array` |  |
| <CopyableCode code="label" /> | `string` |  |
| <CopyableCode code="list_id" /> | `string` |  |
| <CopyableCode code="list_type" /> | `string` |  |
| <CopyableCode code="updated_at" /> | `integer` |  |
| <CopyableCode code="updated_by" /> | `integer` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="account_id, ip_access_list_id" /> | Gets an IP access list, specified by its list ID. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="account_id" /> | Gets all IP access lists for the specified account. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="account_id" /> | Creates an IP access list for the account. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="account_id, ip_access_list_id" /> | Deletes an IP access list, specified by its list ID. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="account_id, ip_access_list_id" /> | Updates an existing IP access list, specified by its ID. |
| <CopyableCode code="replace" /> | `REPLACE` | <CopyableCode code="account_id, ip_access_list_id" /> | Replaces an IP access list, specified by its ID. |

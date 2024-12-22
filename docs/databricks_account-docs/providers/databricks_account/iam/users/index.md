---
title: users
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - users
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

Operations on a <code>users</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.iam.users" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` |  |
| <CopyableCode code="name" /> | `object` |  |
| <CopyableCode code="active" /> | `boolean` |  |
| <CopyableCode code="displayName" /> | `string` |  |
| <CopyableCode code="emails" /> | `array` |  |
| <CopyableCode code="externalId" /> | `string` |  |
| <CopyableCode code="roles" /> | `array` |  |
| <CopyableCode code="userName" /> | `string` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="account_id, id" /> | Gets information for a specific user in Databricks account. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="account_id" /> | Gets details for all the users associated with a Databricks account. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="account_id" /> | Creates a new user in the Databricks account. This new user will also be added to the Databricks account. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="account_id, id" /> | Deletes a user. Deleting a user from a Databricks account also removes objects associated with the user. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="account_id, id" /> | Partially updates a user resource by applying the supplied operations on specific user attributes. |
| <CopyableCode code="update" /> | `REPLACE` | <CopyableCode code="account_id, id" /> | Replaces a user's information with the data supplied in request. |

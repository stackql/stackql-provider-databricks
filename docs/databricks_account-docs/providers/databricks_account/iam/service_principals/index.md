---
title: service_principals
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - service_principals
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

Operations on a <code>service_principals</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_principals</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.iam.service_principals" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` |  |
| <CopyableCode code="active" /> | `boolean` |  |
| <CopyableCode code="applicationId" /> | `string` |  |
| <CopyableCode code="displayName" /> | `string` |  |
| <CopyableCode code="externalId" /> | `string` |  |
| <CopyableCode code="roles" /> | `array` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="account_id, id" /> | Gets the details for a single service principal define in the Databricks account. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="account_id" /> | Gets the set of service principals associated with a Databricks account. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="account_id" /> | Creates a new service principal in the Databricks account. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="account_id, id" /> | Delete a single service principal in the Databricks account. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="account_id, id" /> | Partially updates the details of a single service principal in the Databricks account. |
| <CopyableCode code="update" /> | `REPLACE` | <CopyableCode code="account_id, id" /> | Updates the details of a single service principal. |

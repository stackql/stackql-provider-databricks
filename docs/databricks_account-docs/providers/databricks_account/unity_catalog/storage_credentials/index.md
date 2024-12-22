---
title: storage_credentials
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - storage_credentials
  - unity_catalog
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

Operations on a <code>storage_credentials</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>storage_credentials</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.unity_catalog.storage_credentials" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` |  |
| <CopyableCode code="name" /> | `string` |  |
| <CopyableCode code="aws_iam_role" /> | `object` |  |
| <CopyableCode code="comment" /> | `string` |  |
| <CopyableCode code="created_at" /> | `integer` |  |
| <CopyableCode code="created_by" /> | `string` |  |
| <CopyableCode code="full_name" /> | `string` |  |
| <CopyableCode code="isolation_mode" /> | `string` |  |
| <CopyableCode code="metastore_id" /> | `string` |  |
| <CopyableCode code="owner" /> | `string` |  |
| <CopyableCode code="read_only" /> | `boolean` |  |
| <CopyableCode code="updated_at" /> | `integer` |  |
| <CopyableCode code="updated_by" /> | `string` |  |
| <CopyableCode code="used_for_managed_storage" /> | `boolean` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="account_id, metastore_id, storage_credential_name" /> | Gets a storage credential from the metastore. The caller must be a metastore admin, the owner of the storage credential, or have a level of privilege on the storage credential. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="account_id, metastore_id" /> | Gets a list of all storage credentials that have been assigned to given metastore. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="account_id, metastore_id" /> | Creates a new storage credential. The request object is specific to the cloud: |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="account_id, metastore_id, storage_credential_name" /> | Deletes a storage credential from the metastore. The caller must be an owner of the storage credential. |
| <CopyableCode code="update" /> | `REPLACE` | <CopyableCode code="account_id, metastore_id, storage_credential_name" /> | Updates a storage credential on the metastore. The caller must be the owner of the storage credential. If the caller is a metastore admin, only the |

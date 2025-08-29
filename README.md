# stackql-databricks-openapi

Build `databricks_account` and `databricks_workspace` providers for `stackql` using the databricks web documentation:  

- [api/workspace](https://docs.databricks.com/api/workspace/introduction)
- [api/account](https://docs.databricks.com/api/account/introduction)

## usage

The program requires `selenium` and the `chromedriver` for windows, use PowerShell to run the following code to extract web doc data into machine readable staging documents, the staging documents are then converted into tagged OpenAPI specification documents organized by service:

```powershell
python -m venv venv
.\venv\Scripts\Activate
pip install -r requirements.txt
pip freeze
# scrape web docs
python .\process_web_docs.py account --clean --debug 
python .\process_web_docs.py workspace --clean --debug
# generate openapi specs
python .\generate_openapi_specs.py account --clean --debug
python .\generate_openapi_specs.py workspace --clean --debug

deactivate
Remove-Item -Recurse -Force ./venv
```

## tests

To run tests locally, clone [stackql-provider-tests](https://github.com/stackql/stackql-provider-tests), and run locally:

```bash
# run from the directory you cloned into
cd /mnt/c/LocalGitRepos/stackql/core/stackql-provider-tests
# test account
bash test-provider.sh \
databricks_account \
false \
/mnt/c/LocalGitRepos/stackql/openapi-conversion/stackql-databricks-openapi/openapi_providers \
true

# test workspace
bash test-provider.sh \
databricks_workspace \
false \
/mnt/c/LocalGitRepos/stackql/openapi-conversion/stackql-databricks-openapi/openapi_providers \
true
# back to starting dir
cd /mnt/c/LocalGitRepos/stackql/openapi-conversion/stackql-databricks-openapi
```

## inspect

```bash
curl -L https://bit.ly/stackql-zip -O && unzip stackql-zip
```

```bash
PROVIDER_REGISTRY_ROOT_DIR="$(pwd)/openapi_providers"
REG_STR='{"url": "file://'${PROVIDER_REGISTRY_ROOT_DIR}'", "localDocRoot": "'${PROVIDER_REGISTRY_ROOT_DIR}'", "verifyConfig": {"nopVerify": true}}'
./stackql shell --registry="${REG_STR}"
```

some test queries...

```sql
SELECT 
u.id,
displayName, 
userName, 
active 
FROM databricks_account.iam.users u, JSON_EACH(roles)
WHERE account_id = 'ebfcc5a9-9d49-4c93-b651-b3ee6cf1c9ce'
AND JSON_EXTRACT(json_each.value, '$.value') = 'account_admin';
```

```sql
select 
gr.id, 
displayName, 
json_extract(json_each.value, '$.value') as entitlement 
from databricks_workspace.iam.groups gr, JSON_EACH(entitlements) 
where deployment_name = 'dbc-ddbc0f51-c9cf';
```

```sql
SELECT 
sp.id,
active,
applicationId,
displayName,
externalId
FROM databricks_account.iam.service_principals sp, JSON_EACH(roles)
WHERE account_id = 'ebfcc5a9-9d49-4c93-b651-b3ee6cf1c9ce'
AND JSON_EXTRACT(json_each.value, '$.value') = 'account_admin';
```

```sql
select 
workspace_id,
workspace_name,
deployment_name,
workspace_status,
pricing_tier, 
aws_region, 
credentials_id, 
storage_configuration_id
from
databricks_account.provisioning.workspaces where account_id = 'ebfcc5a9-9d49-4c93-b651-b3ee6cf1c9ce';
```

```sql
select 
cluster_id,
aws_attributes,
node_type_id,
state
from  
databricks_workspace.compute.clusters 
where deployment_name = 'dbc-ddbc0f51-c9cf';
```

```sql
select
*
from databricks_account.provisioning.vw_workspaces 
where account_id = 'ebfcc5a9-9d49-4c93-b651-b3ee6cf1c9ce' 
```

## check for new routes

```powershell
python .\find_new_routes.py workspace
# or
python3 .\find_new_routes.py account
```

## debugging with `curl`

```bash
DATABRICKS_TOKEN=$(curl --request POST "https://accounts.cloud.databricks.com/oidc/accounts/${DATABRICKS_ACCOUNT_ID}/v1/token" \
  --header "Content-Type: application/x-www-form-urlencoded" \
  --data-urlencode "grant_type=client_credentials" \
  --data-urlencode "client_id=${DATABRICKS_CLIENT_ID}" \
  --data-urlencode "client_secret=${DATABRICKS_CLIENT_SECRET}" \
  --data-urlencode "scope=all-apis" | jq -r .access_token)

curl --request GET "https://accounts.cloud.databricks.com/api/2.0/accounts/${DATABRICKS_ACCOUNT_ID}/workspaces" \
  --header "Authorization: Bearer ${DATABRICKS_TOKEN}" \
  -vvv \
  --header "Accept: application/json"
  ```

## generate user (web) docs

```bash
npm i

# databricks_account
rm -rf ./website/databricks_account/docs/*
npm run generate-docs -- \
  --provider-name databricks_account \
  --provider-dir ./openapi_providers/src/databricks_account/v00.00.00000 \
  --output-dir ./website/databricks_account \
  --provider-data-dir ./docgen/provider-data/databricks_account \
  --dereferenced

# databricks_workspace
rm -rf ./website/databricks_workspace/docs/*
npm run generate-docs -- \
  --provider-name databricks_workspace \
  --provider-dir ./openapi_providers/src/databricks_workspace/v00.00.00000 \
  --output-dir ./website/databricks_workspace \
  --provider-data-dir ./docgen/provider-data/databricks_workspace \
  --dereferenced  
```  

### test web docs locally

```bash
# google
cd website/databricks_account
yarn start

# googleadmin
cd website/databricks_workspace
yarn start
```

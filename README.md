# stackql-databricks-openapi

Build `databricks_account` and `databricks_workspace` providers for `stackql` using the databricks web documentation:  

- [api/workspace](https://docs.databricks.com/api/workspace/introduction)
- [api/account](https://docs.databricks.com/api/account/introduction)

# usage

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
```

## tests

To run tests locally, clone [stackql-provider-tests](https://github.com/stackql/stackql-provider-tests), and run locally:

```bash
# run from the directory you cloned into
cd /mnt/c/LocalGitRepos/stackql/core/stackql-provider-tests
bash test-provider.sh \
databricks_account \
false \
/mnt/c/LocalGitRepos/stackql/openapi-conversion/stackql-databricks-openapi/openapi_providers \
true
# stop the server
sh stop.sh
cd /mnt/c/LocalGitRepos/stackql/openapi-conversion/stackql-databricks-openapi
```

# inspect

```bash
curl -L https://bit.ly/stackql-zip -O && unzip stackql-zip
```

```bash
PROVIDER_REGISTRY_ROOT_DIR="$(pwd)/openapi_providers"
REG_STR='{"url": "file://'${PROVIDER_REGISTRY_ROOT_DIR}'", "localDocRoot": "'${PROVIDER_REGISTRY_ROOT_DIR}'", "verifyConfig": {"nopVerify": true}}'
./stackql shell --registry="${REG_STR}"
```




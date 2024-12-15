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
python .\process-web-docs.py account --debug
python .\process-web-docs.py workspace --debug
# generate openapi specs

deactivate
```



# testing

```bash
curl -L https://bit.ly/stackql-zip -O && unzip stackql-zip
```

## Inspect

```bash
PROVIDER_REGISTRY_ROOT_DIR="$(pwd)/openapi_providers"
REG_STR='{"url": "file://'${PROVIDER_REGISTRY_ROOT_DIR}'", "localDocRoot": "'${PROVIDER_REGISTRY_ROOT_DIR}'", "verifyConfig": {"nopVerify": true}}'
./stackql shell --registry="${REG_STR}"
```
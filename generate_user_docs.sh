#!/bin/bash

provider=$1

if [ -z "$provider" ]; then
    echo "provider (arg 1) must be set"
    exit 1
fi

# Validate provider value
if [ "$provider" != "account" ] && [ "$provider" != "workspace" ]; then
    echo "Error: provider must be either 'account' or 'workspace'"
    exit 1
fi

echo "testing provider: $provider"

if [ -z "$regpath" ]; then
    regpath=$(pwd)/openapi_providers
fi

echo "registry path: $regpath"

# Create and activate virtual environment

python3 -m venv .venv
source .venv/bin/activate

# install packages

pip install pandas
pip install psycopg[binary]

chmod +x stackql

# show version
./stackql --version

# do checks

# set registry path
if [ "$SIGNED" = "true" ]; then
    REG='{"url": "file://'${regpath}'", "localDocRoot": "'${regpath}'", "verifyConfig": {"nopVerify": false}}'
else
    REG='{"url": "file://'${regpath}'", "localDocRoot": "'${regpath}'", "verifyConfig": {"nopVerify": true}}'
fi

# start the server if not running
echo "checking if server is running"
if ! pgrep -f "stackql --registry=" > /dev/null; then
    echo "starting server with registry: $REG"
    nohup ./stackql --registry="${REG}" --pgsrv.port=5444 srv &> stackql.log &
    STACKQL_PID=$!  # Capture the server process ID
    echo "stackql server started with PID: $STACKQL_PID"
    sleep 5
else
    echo "server is already running"
    STACKQL_PID=$(pgrep -f "stackql --registry=")
    echo "existing stackql server PID: $STACKQL_PID"
fi

python3 generate_user_docs.py databricks_${provider}

# Deactivate virtual environment
# deactivate

echo "stopping server with PID: $STACKQL_PID"
kill -9 $STACKQL_PID
echo "stackql server stopped"
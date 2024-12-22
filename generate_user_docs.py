import sys, datetime, shutil, psycopg
from pathlib import Path
from psycopg.rows import dict_row
import pandas as pd

from lib.documentation.provider import generate_provider_doc
from lib.documentation.service import generate_service_doc
from lib.documentation.resource import generate_resource_doc

provider = sys.argv[1]

start_time = datetime.datetime.now()

pd.set_option('display.max_columns', None)

# Setup and cleanup documentation directories
docs_dir = Path("docs")
base_path = docs_dir / f"{provider}-docs" # provider index and mdx file goes here
if (base_path / "index.md").exists():
    (base_path / "index.md").unlink()
providers_path = base_path / f"providers/{provider}" # service dirs go here
if providers_path.exists():
    shutil.rmtree(providers_path)

providers_path.mkdir(parents=True, exist_ok=True)

conn = psycopg.connect(
      host="localhost", port=5444,
      autocommit = True,
      row_factory=dict_row
)

def run_query(query):
      print("running %s..." % query)
      try:
            r = conn.execute(query)
            data = r.fetchall()
            return pd.DataFrame([i.copy() for i in data])
      except Exception as e:
            if str(e) == "the last operation didn't produce a result":
                  return None
            print("ERROR [%s]" % str(e))
            sys.exit(1)

# SHOW SERVICES
iql_services_query = "SHOW SERVICES IN %s" % provider
services = run_query(iql_services_query)
if services is None:
      print("ERROR [no services found for %s]" % provider)
      sys.exit(1)
num_services = len(services)

total_resources = 0
total_methods = 0

# SHOW RESOURCES
for serviceIx, serviceRow in services.iterrows():
      service = serviceRow['name']
      iql_resources_query = "SHOW RESOURCES IN %s.%s" % (provider, service)
      resources = run_query(iql_resources_query)
      if resources is None:
            print("ERROR [no resources found for %s.%s]" % (provider, service))
            sys.exit(1)
      num_resources = len(resources)
      print("processing %s resources in %s" % (num_resources, service))
      total_resources = total_resources + num_resources

      # Generate service documentation after getting resources
      generate_service_doc(provider, service, resources, providers_path)
      
      for resIx, resRow in resources.iterrows():
            resource = resRow['name']
            fields = None 
            fqrn_len = len("%s.%s.%s" % (provider, service, resource))

            print("-------------------------------------------------")
            print("%s.%s.%s (length: %s)" % (provider, service, resource, fqrn_len))
            print("-------------------------------------------------")

            # test methods
            iql_methods_query = "SHOW EXTENDED METHODS IN %s.%s.%s" % (provider, service, resource)
            methods = run_query(iql_methods_query)
            print(methods)
            if methods is None:
                  # check if its a view
                  iql_desc_query = "DESCRIBE EXTENDED %s.%s.%s" % (provider, service, resource)
                  fields = run_query(iql_desc_query)
                  if fields is None:
                        print("ERROR [no methods found for %s.%s.%s]" % (provider, service, resource))
                        sys.exit(1)
                  else:
                        total_methods += 1                        
            else:
                  num_methods = len(methods)
                  total_methods = total_methods + num_methods
                  print("%s methods in %s.%s.%s" % (num_methods, provider, service, resource))
                  print(methods)
                  # get fields
                  if 'SELECT' in methods['SQLVerb'].values:
                        # Get fields for the resource
                        iql_desc_query = "DESCRIBE EXTENDED %s.%s.%s" % (provider, service, resource)
                        fields = run_query(iql_desc_query)
                        
            if fields is not None and not fields.empty:
                  print("Fields in %s.%s.%s:" % (provider, service, resource))
                  print(fields)
            else:
                  print("No fields found for %s.%s.%s" % (provider, service, resource))

            # Generate resource documentation
            generate_resource_doc(provider, service, resource, methods, fields, providers_path, resources)

print("%s services processed" % (num_services))
print("%s total resources processed" % (total_resources))
print("%s total methods available" % (total_methods))

# Generate provider documentation at the end
generate_provider_doc(provider, services, total_resources, total_methods, base_path)

print(datetime.datetime.now() - start_time)
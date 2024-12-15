#!/usr/bin/env python3
import yaml, json, os, sys,argparse, time
from pathlib import Path

def read_manifest(provider):

    """Process the API manifest file based on provider type."""
    # Determine which manifest file to read
    manifest_file = f"manifests/{provider}_api_manifest.yml"
    
    try:
        with open(manifest_file, 'r') as f:
            manifest = yaml.safe_load(f)
        return manifest            
    except FileNotFoundError:
        print(f"Error: {manifest_file} not found")
        sys.exit(1)
    except yaml.YAMLError as e:
        print(f"Error parsing {manifest_file}: {e}")
        sys.exit(1)

def create_base_openapi_spec():
    """Create the base OpenAPI specification structure"""
    return {
        "openapi": "3.0.0",
        "info": {
            "title": "Databricks API",
            "version": "v00.00.00000"
        },
        "paths": {},
        "components": {}
    }

def merge_operation_into_paths(paths, operation_spec):
    """Merge an operation spec into the paths dict, handling shared paths"""
    for path, verbs in operation_spec.items():
        if path not in paths:
            # New path, add it with all its verbs
            paths[path] = verbs
        else:
            # Existing path, merge in new verbs
            paths[path].update(verbs)

def load_operation_specs(service_dir, debug):
    """Load all operation specs from a service directory and merge shared paths"""
    paths = {}
    
    # Walk through all resource directories in the service
    for resource_dir in os.scandir(service_dir):
        if resource_dir.is_dir():
            if debug:
                print(f"Processing resource: {resource_dir.name}")
            
            # Process each operation file in the resource directory
            for operation_file in os.scandir(resource_dir.path):
                if operation_file.name.endswith('.json'):
                    if debug:
                        print(f"  Processing operation: {operation_file.name}")
                    
                    with open(operation_file.path) as f:
                        operation_spec = json.load(f)
                        # Merge this operation's paths into our collection
                        merge_operation_into_paths(paths, operation_spec)
    
    return paths

def generate_openapi_docs(provider, debug):
    """Generate OpenAPI specs for each service"""
    staging_dir = f"staging/databricks_{provider}"
    target_dir = f"openapi_providers/src/databricks_{provider}/v00.00.00000/services"
    
    # Create target directory if it doesn't exist
    os.makedirs(target_dir, exist_ok=True)
    
    # Process each service directory
    for service_dir in os.scandir(staging_dir):
        if service_dir.is_dir():
            service_name = service_dir.name
            if debug:
                print(f"\nProcessing service: {service_name}")
            
            # Create base OpenAPI spec for this service
            openapi_spec = create_base_openapi_spec()
            openapi_spec["info"]["title"] = f"Databricks {service_name.capitalize()} API"
            openapi_spec["info"]["description"] = read_manifest(provider)["services"][service_name]["description"]
            
            # Load and merge all operations for this service
            paths = load_operation_specs(service_dir.path, debug)
            openapi_spec["paths"] = paths
            
            # Write the OpenAPI spec to a YAML file
            output_path = os.path.join(target_dir, f"{service_name}.yaml")
            with open(output_path, 'w') as f:
                yaml.dump(openapi_spec, f, sort_keys=False)
            
            if debug:
                print(f"Generated OpenAPI spec: {output_path}")    

def clean_target_dir(provider):
    """Clean the target directory and all subdirectories"""
    target_dir = f"openapi/databricks_{provider}"
    if os.path.exists(target_dir):
        print(f"Cleaning directory: {target_dir}\n")
        print(f"========\n")
        for root, dirs, files in os.walk(target_dir, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir(target_dir)

def build_resource_entry(provider, service_name, resource_name):
    """Build the basic structure for a resource entry"""
    return {
        "id": f"databricks_{provider}.{service_name}.{resource_name}",
        "name": resource_name,
        "title": resource_name.capitalize(),
        "methods": {},
        "sqlVerbs": {
            "select": [],
            "insert": [],
            "update": [],
            "replace": [],
            "delete": [],
            "exec": []
        }
    }

def add_method_to_resource(resource, method_name, path, verb, response_code="200"):
    """Add a method to a resource's methods collection"""
    # Create the path reference, replacing / with ~1 per OpenAPI spec
    path_ref = path.replace("/", "~1")
    resource["methods"][method_name] = {
        "operation": {
            "$ref": f"#/paths/{path_ref}/{verb}"
        },
        "response": {
            "mediaType": "application/json",
            "openAPIDocKey": response_code
        }
    }

def generate_stackql_resources(provider, debug):
    """Generate x-stackQL-resources components for each service"""
    services_dir = f"openapi_providers/src/databricks_{provider}/v00.00.00000/services"
    
    # Process each service YAML file
    for service_file in os.scandir(services_dir):
        if service_file.name.endswith('.yaml'):
            if debug:
                print(f"\nProcessing service file: {service_file.name}")
            
            service_name = service_file.name[:-5]  # Remove .yaml extension
            
            with open(service_file.path, 'r') as f:
                spec = yaml.safe_load(f)
            
            # Create resources dictionary
            resources = {}
            
            # Process each path and its operations
            for path, path_obj in spec['paths'].items():
                for verb, operation in path_obj.items():
                    if 'x-stackQL-resource' not in operation:
                        if debug:
                            print(f"Warning: Missing x-stackQL-resource in {path} {verb}")
                        continue
                    
                    resource_name = operation['x-stackQL-resource']
                    method_name = operation['x-stackQL-method']
                    sql_verb = operation['x-stackQL-verb']
                    num_params = operation.get('x-numReqParams', 0)
                    response_code = operation.get('x-stackQL-responseCode', '200')
                    
                    # Create resource if it doesn't exist
                    if resource_name not in resources:
                        resources[resource_name] = build_resource_entry(provider, service_name, resource_name)
                    
                    # Add method to resource
                    add_method_to_resource(resources[resource_name], method_name, path, verb, response_code)
                    
                    # Add method reference to appropriate sqlVerb list
                    method_ref = f"#/components/x-stackQL-resources/{resource_name}/methods/{method_name}"
                    
                    # Find insertion point based on x-numReqParams
                    sql_verb_list = resources[resource_name]["sqlVerbs"][sql_verb]
                    insert_index = 0
                    for i, existing_ref in enumerate(sql_verb_list):
                        existing_path = existing_ref["$ref"].split("/methods/")[1]
                        existing_op = spec["paths"][path][verb]
                        if existing_op.get('x-numReqParams', 0) <= num_params:
                            insert_index = i
                            break
                        insert_index = i + 1
                    
                    sql_verb_list.insert(insert_index, {"$ref": method_ref})
            
            # Add resources to spec and write back
            if not 'components' in spec:
                spec['components'] = {}
            spec['components']['x-stackQL-resources'] = resources
            
            with open(service_file.path, 'w') as f:
                yaml.dump(spec, f, sort_keys=False)
            
            if debug:
                print(f"Updated {service_file.name} with x-stackQL-resources")

def generate_provider_yaml(provider):
    """Generate the provider.yaml file that indexes all service specs"""
    services_dir = f"openapi_providers/src/databricks_{provider}/v00.00.00000/services"
    provider_dir = f"openapi_providers/src/databricks_{provider}/v00.00.00000"
    version = "v00.00.00000"
    
    # Read the manifest to get service descriptions
    manifest = read_manifest(provider)
    
    # Create base provider structure
    provider_spec = {
        "id": f"databricks_{provider}",
        "name": f"databricks_{provider}",
        "version": version,
        "providerServices": {},
        "config": {
            "auth": {
                "credentialsenvvar": "DATABRICKS_CREDENTIALS",
                "type": "service_account"
            }
        }
    }
    
    # Process each service YAML file
    for service_file in os.scandir(services_dir):
        if service_file.name.endswith('.yaml'):
            service_name = service_file.name[:-5]  # Remove .yaml extension
            
            # Add service to provider spec
            provider_spec["providerServices"][service_name] = {
                "id": f"{service_name}:{version}",
                "name": service_name,
                "preferred": True,
                "service": {
                    "$ref": f"databricks_{provider}/{version}/services/{service_name}.yaml"
                },
                "title": manifest["services"][service_name]["description"].split('.')[0],  # First sentence
                "version": version,
                "description": manifest["services"][service_name]["description"]
            }
    
    # Write provider.yaml
    output_path = os.path.join(provider_dir, "provider.yaml")
    with open(output_path, 'w') as f:
        yaml.dump(provider_spec, f, sort_keys=False)

def main():
    start_time = time.time()

    parser = argparse.ArgumentParser(description='Process Databricks API documentation')
    parser.add_argument('provider', choices=['account', 'workspace'],
                      help='The provider type to process (account or workspace)')
    parser.add_argument('--debug', action='store_true',
                      help='Save raw text files alongside JSON for debugging')
    parser.add_argument('--clean', action='store_true',
                      help='Clean the entire target directory before processing')    

    args = parser.parse_args()
    
    if args.clean:
        # Clean target directory before processing
        clean_target_dir(args.provider)    

    #
    # step 1 - generate OpenAPI specs
    #
    generate_openapi_docs(args.provider, args.debug)    

    #
    # step 2 - generate components/x-stackQL-resources
    #    
    generate_stackql_resources(args.provider, args.debug)

    #
    # step 3 - generate provider.yaml
    # 
    generate_provider_yaml(args.provider)

    elapsed_time = time.time() - start_time
    print(f"Elapsed time: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    main()
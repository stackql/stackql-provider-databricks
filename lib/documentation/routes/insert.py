from pathlib import Path
import re, yaml
import sys
import pandas as pd

#
# main routine
#

def generate_insert_example(provider, service, resource, methods_df, fields_df, spec_root_path):
    """Generate INSERT example documentation."""
    # Get all INSERT operations
    insert_methods = methods_df[methods_df['SQLVerb'] == 'INSERT'].copy()
    if insert_methods.empty:
        return ""
    
    # Add parameter count for sorting
    insert_methods['param_count'] = insert_methods['RequiredParams'].apply(
        lambda x: len(x.split(', ')) if pd.notna(x) else 0
    )
    # Sort by parameter count
    insert_methods = insert_methods.sort_values('param_count')
    
    def create_insert_statement(method):
        """Creates an INSERT statement for the given method"""
        required_params = method['RequiredParams'].split(', ') if pd.notna(method['RequiredParams']) else []
        
        # Get the request body fields from the manifest
        manifest = get_manifest_fields(provider, service, resource, method['MethodName'], spec_root_path)
        req_body_params = []
        if manifest != "# TODO: Resource not found in spec":
            try:
                manifest_yaml = yaml.safe_load(manifest)
                if manifest_yaml and 'props' in manifest_yaml[0]:
                    req_body_params = [p['name'] for p in manifest_yaml[0]['props']]
            except:
                pass
        
        # Create column and value lists
        columns = []
        values = []
        
        # Add path params (required params without data__ prefix)
        for param in required_params:
            if not param.startswith('data__'):
                template_param = param
                columns.append(param)
                values.append(f"'{{{{ {template_param} }}}}'")
        
        # Add request body params (with data__ prefix)
        for param in req_body_params:
            if param != 'id':  # Skip id field
                columns.append(f"data__{param}")
                values.append(f"'{{{{ {param} }}}}'")
        
        query = f"""/*+ create */
INSERT INTO {provider}.{service}.{resource} (
{',\\n'.join(columns)}
)
SELECT 
{',\\n'.join(values)}
;"""
        return query

    # If only one INSERT method, don't use tabs for methods
    if len(insert_methods) == 1:
        method = insert_methods.iloc[0]
        manifest = get_manifest_fields(provider, service, resource, method['MethodName'], spec_root_path)
        
        return """
## INSERT example

Use the following StackQL query and manifest file to create a new <code>%s</code> resource.

<Tabs
    defaultValue="create"
    values={[
        {{ label: '%s', value: 'create', }},
        {{ label: 'Manifest', value: 'manifest', }},
    ]}
>
<TabItem value="create">
""" % (resource, resource) + f"""```sql
{create_insert_statement(method)}
```

</TabItem>
<TabItem value="manifest">

```yaml
{manifest}
```

</TabItem>
</Tabs>
"""
    
    # For multiple INSERT methods, use additional tabs
    content = """
## INSERT example

Use the following StackQL query and manifest file to create a new <code>%s</code> resource.

<Tabs
    defaultValue="%s"
    values={[
""" % (resource, insert_methods.iloc[0]['MethodName'])
    
    # Add tab definitions for each method
    tab_values = []
    for _, method in insert_methods.iterrows():
        tab_values.append(
            f"""        {{ label: '{resource} ({method["MethodName"]})', value: '{method["MethodName"]}' }}"""
        )
    tab_values.append("""        { label: 'Manifest', value: 'manifest' }""")
    
    content += ',\n'.join(tab_values)
    content += """
    ]
}>
"""
    
    # Add tab for each INSERT method
    for _, method in insert_methods.iterrows():
        content += f"""<TabItem value="{method['MethodName']}">

```sql
{create_insert_statement(method)}
```

</TabItem>
"""
    
    # Add manifest tab using the first method as reference
    manifest = get_manifest_fields(provider, service, resource, insert_methods.iloc[0]['MethodName'], spec_root_path)
    content += f"""<TabItem value="manifest">

```yaml
{manifest}
```

</TabItem>
</Tabs>
"""
    
    return content

#
# manifest
#

def get_manifest_fields(provider, service, resource, method, spec_root_path):
    """Get manifest fields for a resource from its OpenAPI spec."""
    spec = load_service_spec(spec_root_path, provider, service)
    
    # Find the resource in x-stackQL-resources
    resource_spec = None
    for res_name, res_spec in spec['components']['x-stackQL-resources'].items():
        if res_spec['name'] == resource:
            resource_spec = res_spec
            break
    
    if not resource_spec:
        print(f"ERROR [resource {resource} not found in spec for {provider}]")
        sys.exit(1)
    
    # Get the operation ref and extract path
    operation_ref = resource_spec['methods'][method]['operation']['$ref']
    path_match = re.search(r'#/paths/(.+?)/(post|put)', operation_ref)
    if not path_match:
        print(f"ERROR [could not parse operation reference for {provider}.{service}.{resource}]")
        sys.exit(1)
    
    path = path_match.group(1).replace('~1', '/')
    verb = path_match.group(2)  # will be either 'post' or 'put'
    operation = spec['paths'][path][verb]
    
    # Check if request body exists
    if 'requestBody' not in operation:
        return """- name: your_resource_model_name
  props: []  # No request body parameters required"""
    
    # Get example structure from request body
    request_body = operation['requestBody']
    json_content = request_body.get('content', {}).get('application/json', {})
    example = json_content.get('schema', {}).get('example', {})
    
    # Build manifest structure
    manifest_obj = {
        'name': 'your_resource_model_name',
        'props': []
    }
    
    # Process each property from the example
    for prop_name, prop_value in example.items():
        if prop_name == 'id':
            continue
            
        if isinstance(prop_value, list):
            # Handle array type (using first item as template)
            if prop_value:
                manifest_obj['props'].append({
                    'name': prop_name,
                    'value': prop_value
                })
        elif isinstance(prop_value, dict):
            # Handle object type
            manifest_obj['props'].append({
                'name': prop_name,
                'value': prop_value
            })
        else:
            # Handle simple types
            manifest_obj['props'].append({
                'name': prop_name,
                'value': 'string' if prop_value == 'string' else prop_value
            })
    
    # Convert to YAML
    return yaml.dump([manifest_obj], default_flow_style=False, sort_keys=False)

def load_service_spec(spec_root_path, provider, service):
    """Load the OpenAPI spec for a service."""
    # Find the version directory (most recent one)
    provider_path = Path(spec_root_path) / "src" / f"{provider}"
    version_dirs = [d for d in provider_path.iterdir() if d.is_dir() and d.name.startswith('v')]
    if not version_dirs:
        raise Exception(f"No version directory found in {provider_path}")
    latest_version = sorted(version_dirs)[-1]
    
    # Load the service spec
    spec_path = latest_version / "services" / f"{service}.yaml"
    if not spec_path.exists():
        raise Exception(f"Service spec not found: {spec_path}")
    
    with open(spec_path) as f:
        return yaml.safe_load(f)
    

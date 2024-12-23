import pandas as pd

def generate_replace_example(provider, service, resource, methods_df, fields_df):
    """Generate REPLACE example documentation."""
    # Get all REPLACE operations
    replace_methods = methods_df[methods_df['SQLVerb'] == 'REPLACE'].copy()
    if replace_methods.empty:
        return ""
    
    # Add parameter count for sorting
    replace_methods['param_count'] = replace_methods['RequiredParams'].apply(
        lambda x: len(x.split(', ')) if pd.notna(x) else 0
    )
    # Sort by parameter count (least specific to most)
    replace_methods = replace_methods.sort_values('param_count')

    def create_replace_statement(method):
        """Creates an REPLACE statement for the given method"""
        required_params = method['RequiredParams'].split(', ') if pd.notna(method['RequiredParams']) else []
        where_clause = []
        for param in required_params:
            template_param = param.replace('data__', '')
            where_clause.append(f"{param} = '{{{{ {template_param} }}}}'")
        where_str = ' AND\n'.join(where_clause)
        
        return f"""/*+ update */
-- replace field1, field2, etc. with the fields you want to update
REPLACE %s.%s.%s
SET field1 = '{{ value1 }}',
field2 = '{{ value2 }}', ...
WHERE %s;""" % (provider, service, resource, where_str)

    # If only one REPLACE method, don't use tabs
    if len(replace_methods) == 1:
        method = replace_methods.iloc[0]
        content = f"""
## `REPLACE` example

Replaces a <code>{resource}</code> resource.

```sql
{create_replace_statement(method)}
```
"""
    else:
        # For multiple REPLACE methods, use tabs
        content = """
## `REPLACE` example

Replaces a <code>%s</code> resource.

<Tabs
    defaultValue="%s"
    values={[
""" % (resource, replace_methods.iloc[0]['MethodName'])
    
        # Add tab definitions
        tab_values = []
        for _, method in replace_methods.iterrows():
            tab_values.append(
                """        { label: '%s', value: '%s' }""" % (method["MethodName"], method["MethodName"])
            )
        
        content += ',\n'.join(tab_values)
        content += """
    ]
}>
"""
   
        # Add tab for each REPLACE method
        for _, method in replace_methods.iterrows():
            content += f"""<TabItem value="{method['MethodName']}">

```sql
{create_replace_statement(method)}
```
</TabItem>
"""
    
        content += "</Tabs>\n"
    return content

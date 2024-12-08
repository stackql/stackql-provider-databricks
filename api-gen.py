import json
import re

def cleanup_dict(d):
    """Remove null values from dictionary recursively"""
    if not isinstance(d, dict):
        return d
    
    return {
        k: cleanup_dict(v)
        for k, v in d.items()
        if v is not None and v != {} and v != []
    }

def parse_doc_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
    
    # Split into sections using the known anchors
    sections = {
        'verb_path': content.split('Path parameters')[0].strip(),
        'path_params': content.split('Path parameters')[1].split('Request body')[0].strip() if 'Request body' in content else content.split('Path parameters')[1].split('Responses')[0].strip(),
        'request_body': content.split('Request body')[1].split('Responses')[0].strip() if 'Request body' in content else None,
        'responses': content.split('Responses')[1].split('This method might return')[0].strip() if 'This method might return' in content else content.split('Responses')[1].strip(),
        'error_codes': content.split('Possible error codes:')[1].strip() if 'Possible error codes:' in content else None
    }
    
    # Parse verb and path
    lines = sections['verb_path'].split('\n')
    verb = lines[0].strip().lower()
    path = lines[1].strip()
    op_desc = lines[2].strip()
    
    # Parse path parameters
    path_parameters = {}
    if sections['path_params']:
        current_param = None
        for line in sections['path_params'].split('\n'):
            line = line.strip()
            if line.startswith('code:'):
                current_param = line.replace('code:', '').strip()
                path_parameters[current_param] = {
                    'required': False,
                    'type': None
                }
            elif line == 'required':
                path_parameters[current_param]['required'] = True
            elif line in ['string', 'integer', 'boolean', 'array']:
                path_parameters[current_param]['type'] = line
            elif line and not line.startswith('code:'):
                path_parameters[current_param]['description'] = line

    def parse_array_structure(lines, start_idx):
        """Parse array structure and return the array item properties and the ending index"""
        array_props = {'type': 'array', 'items': {'type': 'object', 'properties': {}}}
        current_prop = None
        in_enum = False
        enum_values = []
        i = start_idx
        
        while i < len(lines):
            line = lines[i].strip()
            
            if line == ']':
                return array_props, i
                
            if line.startswith('code:'):
                if in_enum and current_prop:
                    # Handle enum values from previous property
                    parts = line.replace('code:', '').strip().split('|')
                    enum_values.extend([p.strip() for p in parts])
                    array_props['items']['properties'][current_prop]['enum'] = enum_values
                    in_enum = False
                else:
                    current_prop = line.replace('code:', '').strip()
                    array_props['items']['properties'][current_prop] = {
                        'type': None
                    }
            elif line in ['string', 'integer', 'boolean', 'array']:
                if current_prop:
                    array_props['items']['properties'][current_prop]['type'] = line
            elif line == 'Enum:':
                in_enum = True
                enum_values = []
                array_props['items']['properties'][current_prop]['type'] = 'string'
            elif '|' in line and not line.startswith('code:'):
                parts = line.split('|')
                enum_values.extend([p.strip() for p in parts])
                array_props['items']['properties'][current_prop]['enum'] = enum_values
            elif line and not line.startswith('Array') and not line.startswith('code:'):
                if current_prop and not in_enum:
                    array_props['items']['properties'][current_prop]['description'] = line
            
            i += 1
        
        return array_props, i

    # Parse request body
    request_body = None
    if sections['request_body']:
        request_body = {'properties': {}}
        lines = sections['request_body'].split('\n')
        i = 0
        current_prop = None
        in_enum = False
        enum_values = []
        
        while i < len(lines):
            line = lines[i].strip()
            
            if line.startswith('code:'):
                if in_enum and current_prop:
                    # Handle enum values from previous property
                    parts = line.replace('code:', '').strip().split('|')
                    enum_values.extend([p.strip() for p in parts])
                    request_body['properties'][current_prop]['enum'] = enum_values
                    in_enum = False
                else:
                    current_prop = line.replace('code:', '').strip()
                    request_body['properties'][current_prop] = {
                        'type': None
                    }
            elif line == 'Array [':
                if current_prop and request_body['properties'][current_prop].get('type') == 'Array of object':
                    array_props, new_idx = parse_array_structure(lines, i + 1)
                    request_body['properties'][current_prop].update(array_props)
                    i = new_idx
            elif line in ['string', 'integer', 'boolean', 'array', 'Array of object']:
                if current_prop:
                    request_body['properties'][current_prop]['type'] = line
            elif line == 'Enum:':
                in_enum = True
                enum_values = []
                request_body['properties'][current_prop]['type'] = 'string'
            elif line and not line.startswith('code:') and not line == 'Array [' and not line == ']':
                if current_prop and not in_enum:
                    request_body['properties'][current_prop]['description'] = line
                    
            i += 1

    # Parse responses (similar updates for response parsing...)
    responses = {}
    if sections['responses']:
        current_code = None
        current_prop = None
        in_enum = False
        enum_values = []
        lines = sections['responses'].split('\n')
        i = 0
        
        while i < len(lines):
            line = lines[i].strip()
            
            if line and line.isdigit():
                current_code = line
                responses[current_code] = {}
                current_prop = None
            elif line.startswith('code:'):
                if in_enum and current_prop:
                    parts = line.replace('code:', '').strip().split('|')
                    enum_values.extend([p.strip() for p in parts])
                    responses[current_code][current_prop]['enum'] = enum_values
                    in_enum = False
                else:
                    current_prop = line.replace('code:', '').strip()
                    if current_code:
                        responses[current_code][current_prop] = {
                            'type': None
                        }
            elif line == 'Array [' and current_prop:
                if responses[current_code][current_prop].get('type') == 'Array of object':
                    array_props, new_idx = parse_array_structure(lines, i + 1)
                    responses[current_code][current_prop].update(array_props)
                    i = new_idx
            elif current_prop and line in ['string', 'integer', 'boolean', 'array', 'Array of object']:
                if current_code:
                    responses[current_code][current_prop]['type'] = line
            elif line == 'Enum:':
                in_enum = True
                enum_values = []
                responses[current_code][current_prop]['type'] = 'string'
            elif current_prop and line and not line.startswith('code:'):
                if current_code and not in_enum:
                    responses[current_code][current_prop]['description'] = line
                    
            i += 1
    
    # Parse error codes
    if sections['error_codes']:
        error_lines = sections['error_codes'].split('\n')
        current_code = None
        for line in error_lines:
            line = line.strip()
            if line.isdigit():
                current_code = line
                if current_code not in responses:
                    responses[current_code] = {}
            elif current_code and line and not line.startswith('HTTP code'):
                if 'error_code' not in responses[current_code]:
                    responses[current_code]['error_code'] = line
                elif 'description' not in responses[current_code]:
                    responses[current_code]['description'] = line
    
    # Construct final output
    output = {
        'verb': verb,
        'path': path,
        'description': op_desc,
        'pathParameters': path_parameters,
    }
    
    if request_body:
        output['requestBody'] = request_body
        
    if responses:
        output['responses'] = responses
    
    # Clean up null values
    output = cleanup_dict(output)
    
    return output

def main():
    # Parse the document
    result = parse_doc_file('http_section_content.txt')
    
    # Write to output file with pretty printing
    with open('api_spec.json', 'w') as f:
        json.dump(result, f, indent=2)

if __name__ == "__main__":
    main()
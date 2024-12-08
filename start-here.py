#!/usr/bin/env python3
import yaml
import argparse
import subprocess
import sys
import json
import re
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

def process_manifest(provider, debug):
    """Process the API manifest file based on provider type."""
    # Determine which manifest file to read
    manifest_file = f"{provider}_api_manifest.yml"
    
    try:
        with open(manifest_file, 'r') as f:
            manifest = yaml.safe_load(f)
    except FileNotFoundError:
        print(f"Error: {manifest_file} not found")
        sys.exit(1)
    except yaml.YAMLError as e:
        print(f"Error parsing {manifest_file}: {e}")
        sys.exit(1)

    # Process each service in the manifest
    for service_name, service_data in manifest['services'].items():
        for resource in service_data['resources']:
            resource_name = resource['name']
            for method in resource['methods']:
                process_endpoint(provider, service_name, resource_name, method['name'], method['docPath'], method['verb'], debug)

def scrape_dynamic_content(url):
    # Configure Selenium WebDriver with headless Chrome
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Specify the path to the downloaded ChromeDriver
    driver = webdriver.Chrome(
        service=Service("inc/chromedriver.exe"),
        options=chrome_options
    )

    try:
        # Open the page
        driver.get(url)

        # Wait for a specific element to load
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "root"))
        )

        # Extract the full rendered HTML
        page_source = driver.page_source

        # Parse the content using BeautifulSoup
        soup = BeautifulSoup(page_source, "html.parser")

        # Remove unwanted elements
        for tag in soup(["head", "script", "meta", "title", "style", "svg", "input", "iframe"]):
            tag.decompose()

        return soup

    finally:
        # Close the browser
        driver.quit()

def extract_http_section(soup):
    """Extract HTTP verb and everything below it, adding preamble for `code` tags, and truncate at samples."""
    all_text = []

    # Find all text content
    capturing = False
    http_verbs = {"GET", "POST", "PUT", "PATCH", "DELETE"}
    stop_keywords = {"Request samples", "Response samples"}

    for element in soup.find_all(string=True):
        text = element.strip()
        if not text:
            continue

        # Check if the text contains an HTTP verb
        if any(verb in text for verb in http_verbs):
            capturing = True

        # Stop capturing if a stop keyword is encountered
        if any(keyword in text for keyword in stop_keywords):
            capturing = False
            break

        # If capturing, append the text
        if capturing:
            # Handle `code` tags with a preamble
            if element.parent and element.parent.name == "code":
                all_text.append(f"code: {text}")
            else:
                all_text.append(text)

    return all_text

def cleanup_dict(d):
    """Remove null values from dictionary recursively"""
    if not isinstance(d, dict):
        return d
    
    return {
        k: cleanup_dict(v)
        for k, v in d.items()
        if v is not None and v != {} and v != []
    }

def parse_doc_content(content):
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

    # Parse responses
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

def process_endpoint(provider, service, resource, method, docPath, verb, debug):
    # Scrape the documentation page
    soup = scrape_dynamic_content(docPath)
    
    # Extract the HTTP section
    http_section = extract_http_section(soup)
    http_content = "\n".join(http_section)

    # Parse the content into structured format
    api_spec = parse_doc_content(http_content)

    # Create output directory structure
    output_dir = f"staging/databricks_{provider}/{service}/{resource}"
    os.makedirs(output_dir, exist_ok=True)

    # Write the output
    output_file = f"{output_dir}/{method}.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(api_spec, f, indent=2)

    if debug:
        # Write the raw text content
        text_file = f"{output_dir}/{method}.txt"
        with open(text_file, 'w', encoding='utf-8') as f:
            f.write(http_content)

    print(f"""Parsed {docPath}
Provider: {provider}
Service: {service}
Resource: {resource}
Method: {method}
Verb: {verb}
Output: {output_file}
""")

def clean_target_dir(provider):
    """Clean the target directory and all subdirectories"""
    target_dir = f"staging/databricks_{provider}"
    if os.path.exists(target_dir):
        print(f"Cleaning directory: {target_dir}")
        for root, dirs, files in os.walk(target_dir, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir(target_dir)

def main():
    parser = argparse.ArgumentParser(description='Process Databricks API documentation')
    parser.add_argument('provider', choices=['account', 'workspace'],
                      help='The provider type to process (account or workspace)')
    parser.add_argument('--debug', action='store_true',
                      help='Save raw text files alongside JSON for debugging')

    args = parser.parse_args()
    
    # Clean target directory before processing
    clean_target_dir(args.provider)
    
    # Process the manifest for the specified provider
    process_manifest(args.provider, args.debug)

if __name__ == "__main__":
    main()
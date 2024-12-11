#!/usr/bin/env python3
import yaml, argparse , sys, json, os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import bs4

def process_manifest(provider, debug):
    """Process the API manifest file based on provider type."""
    # Determine which manifest file to read
    manifest_file = f"manifests/{provider}_api_manifest.yml"
    
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
        soup = bs4.BeautifulSoup(page_source, "html.parser")

        # Remove unwanted elements
        for tag in soup(["head", "script", "meta", "title", "style", "svg", "input", "iframe"]):
            tag.decompose()

        return soup

    finally:
        # Close the browser
        driver.quit()

def process_endpoint(provider, service, resource, method, docPath, sqlVerb, debug):
    print(f"""processing docPath: {docPath}
provider: {provider}
service: {service}
resource: {resource}
method: {method}
sqlVerb: {sqlVerb}
""")

    # Create output directory structure
    output_dir = f"staging/databricks_{provider}/{service}/{resource}"
    os.makedirs(output_dir, exist_ok=True)

    # Scrape the documentation page
    soup = scrape_dynamic_content(docPath)
    
    main_article = soup.find("article", role="main")
    if main_article is None:
        print("Could not find <article role='main'>")
        return

    result = []
    start_processing = False  # To skip everything before 'GET'

    for element in main_article.descendants:
        # Only process elements that contain text
        if isinstance(element, bs4.element.Tag) and element.string:
            text = element.string.strip()  # Get and clean the text
            if not text:  # Skip empty text
                continue

            # Rule 1: Start processing at the first instance of http verb
            if not start_processing:
                if text in ('GET', 'POST', 'PUT', 'PATCH', 'DELETE'):
                    start_processing = True
                else:
                    continue

            # Create the current tuple
            current_item = (element.name, text)

            # Rule 2: Take only the last tuple if consecutive values are the same
            if len(result) > 0 and result[-1][1] == text:
                result[-1] = current_item  # Replace the last tuple
            else:
                result.append(current_item)

    process_main_article_data(result, output_dir, resource, method, sqlVerb, docPath)

def process_main_article_data(main_article_data, output_dir, resource, method, sqlVerb, docPath):

    write_output(output_dir, f"{method}-raw", main_article_data)

    #
    # helper functions
    #
    def process_params(param_data, param_type, params):
        current_param = None
        i = 0
        
        while i < len(param_data):
            element_type, value = param_data[i]
            
            if element_type == 'code':
                # If we have a current parameter, add it to params
                if current_param:
                    params.append(current_param)
                
                # Start new parameter
                current_param = {
                    'name': value,
                    'in': param_type,
                    'description': '',
                    'required': False
                }
                
                # Look ahead for required and app_type
                j = i + 1
                while j < len(param_data):
                    next_type, next_value = param_data[j]
                    
                    if next_type == 'code':  # Stop if we hit another parameter
                        break
                        
                    if next_type == 'span' and next_value == 'required':
                        current_param['required'] = True
                    elif next_type == 'span':  # This is the app_type
                        app_type = next_value
                        # Look for description in next element
                        if j + 1 < len(param_data) and param_data[j + 1][0] == 'div':
                            description = param_data[j + 1][1]
                            current_param['description'] = f"{description} ({app_type})"
                    
                    j += 1
                    
            i += 1
        
        if current_param:
            params.append(current_param)
            
        return params    

    #
    # main processing
    #
    verb = (main_article_data[0][1]).lower()
    path = main_article_data[1][1]
    description = main_article_data[2][1]
    operationId = f"{resource.replace('_', '-')}-{method.replace('_', '-')}"
    externalDocs = { "url": docPath }

    #
    # find anchor points
    #
    path_parameter_index = -1
    query_parameter_index = -1
    request_body_index = -1
    responses_index = -1
    error_codes_index = -1

    # start from 3rd element
    for i, item in enumerate(main_article_data[3:]):
        if item[0] in ('h1','h2','h3', 'h4'):
            if item[1] == 'Path parameters':
                path_parameter_index = i + 1
            elif item[1] == 'Query parameters':
                query_parameter_index = i + 1
            elif item[1] == 'Request body':
                request_body_index = i + 1
            elif item[1] == 'Responses':
                responses_index =  i + 1
            elif item[1] == 'Possible error codes:':
                error_codes_index = i + 1

    parameters = []

    path_param_stop = len(main_article_data)
    query_param_stop = len(main_article_data)

    if query_parameter_index > 0:
        path_param_stop = query_parameter_index-1
    elif request_body_index > 0:
        path_param_stop = request_body_index-1
        query_param_stop = request_body_index-1
    elif responses_index > 0:
        path_param_stop = responses_index-1
        query_param_stop = responses_index-1
    elif error_codes_index > 0:
        path_param_stop = error_codes_index-1
        query_param_stop = error_codes_index-1

    #
    # path parameters
    #
    if path_parameter_index > 0:
        parameters = process_params(main_article_data[path_parameter_index:path_param_stop], 'path', parameters)

    #
    # query parameters
    #
    if query_parameter_index > 0:
        parameters = process_params(main_article_data[query_parameter_index:query_param_stop], 'query', parameters)


    operation_object = {}
    operation_object['path'] = path
    operation_object['verb'] = verb
    operation_object['operationId'] = operationId
    operation_object['description'] = description
    operation_object['externalDocs'] = externalDocs
    operation_object['parameters'] = parameters

    write_output(output_dir, method, operation_object)


def write_output(output_dir, method, result):
    print(f"\nWriting output to {output_dir}/{method}.json\n")
    # Write the output
    output_file = f"{output_dir}/{method}.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=1)

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
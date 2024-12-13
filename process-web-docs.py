#!/usr/bin/env python3
import yaml, argparse , sys, json, os, re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import bs4
from parsel import Selector

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
sqlVerb: {sqlVerb}""")

    # Create output directory structure
    output_dir = f"staging/databricks_{provider}/{service}/{resource}"
    os.makedirs(output_dir, exist_ok=True)

    # Scrape the documentation page
    soup = scrape_dynamic_content(docPath)
    
    selector = Selector(text=str(soup))

    doc_base_path = "/html/body/div[1]/div/div[2]/div/div[2]/div[3]/article/div/div[1]"

    http_verb = selector.xpath(f"{doc_base_path}/article/span/code/div/div/text()").get().lower()
    print(f"\nhttp_verb: {http_verb}")
    if http_verb not in ["get", "post", "put", "delete", "patch"]:
        raise ValueError(f"Invalid HTTP verb: {http_verb}")

    http_path = selector.xpath(f"{doc_base_path}/article/span/code/span/text()").get()
    print(f"http_path: {http_path}")
    if not http_path.startswith('/api/2.0/'):
        raise ValueError(f"Invalid HTTP path: {http_path}")
    
    op_desc = selector.xpath(f"{doc_base_path}/div[3]/div[2]/text()").get().replace("\n", " ").strip()
    print(f"op_desc: {op_desc}")
    if op_desc is None:
        raise ValueError(f"Invalid operation description: {http_path}")

    params = []

    # default index values
    path_params_ix = 0
    query_params_ix = 0
    request_body_desc_ix = 0
    request_body_props_ix = 0
    responses_ix = 0

    #
    # path params
    #

    # Find the index of the <div> containing the <h3> with text "Path parameters"
    path_params_ix = int(float(selector.xpath(
        f"count({doc_base_path}/*[self::div and .//h3[text()='Path parameters']]/preceding-sibling::div)"
    ).get()))
    if path_params_ix > 0:
        path_params_ix += 1

    # has path params?
    if path_params_ix > 0:
        direct_divs = selector.xpath(f"{doc_base_path}/div[{path_params_ix}]/div/*[name()=\"div\"]")
        for idx, div in enumerate(direct_divs):
            param = {}
            param["name"] = selector.xpath(f"{doc_base_path}/div[{path_params_ix}]/div/div[{idx+1}]/div[1]/a/span[2]/code/text()").get()
            if selector.xpath(f"{doc_base_path}/div[{path_params_ix}]/div/div[{idx+1}]/div[1]/span[1]/text()").get() == "required":
                param["required"] = True
            type_desc = selector.xpath(f"{doc_base_path}/div[{path_params_ix}]/div/div[{idx+1}]/div[1]/span[2]/text()").get()
            param_desc = selector.xpath(f"{doc_base_path}/div[{path_params_ix}]/div/div[{idx+1}]/div[3]/div/text()").get().replace("\n", " ").strip()
            param["description"] = f"({type_desc}) {param_desc}" if type_desc else param_desc
            param["in"] = "path"
            params.append(param)

    #
    # query params
    #
    
    query_params_ix = int(float(selector.xpath(
        f"count({doc_base_path}/*[self::div and .//h3[text()='Query parameters']]/preceding-sibling::div)"
    ).get()))
    if query_params_ix > 0:
        query_params_ix += 1

    if query_params_ix > 0:
        direct_divs = selector.xpath(f"{doc_base_path}/div[{query_params_ix}]/div/*[name()=\"div\"]")
        for idx, div in enumerate(direct_divs):
            param = {}
            param["name"] = selector.xpath(f"{doc_base_path}/div[{query_params_ix}]/div/div[{idx+1}]/div[1]/a/span[2]/code/text()").get()
            if selector.xpath(f"{doc_base_path}/div[{query_params_ix}]/div/div[{idx+1}]/div[1]/span[1]/text()").get() == "required":
                param["required"] = True
            type_desc = selector.xpath(f"{doc_base_path}/div[{query_params_ix}]/div/div[{idx+1}]/div[1]/span[2]/text()").get()
            param_desc = selector.xpath(f"{doc_base_path}/div[{query_params_ix}]/div/div[{idx+1}]/div[3]/div/text()").get().replace("\n", " ").strip()
            param["description"] = f"({type_desc}) {param_desc}" if type_desc else param_desc
            param["in"] = "query"
            params.append(param)
        
    print(f"params: {params}")

    #
    # req body params
    #

    if selector.xpath(f"{doc_base_path}/h3[1]/text()").get() == "Request body":
        request_body_desc_ix = max(path_params_ix, query_params_ix) + 1
        request_body_props_ix = request_body_desc_ix + 1
        request_body_desc = selector.xpath(f"{doc_base_path}/div[{request_body_desc_ix}]/text()").get().replace("\n", " ").strip()
        print(f"request body description: {request_body_desc}")
        direct_divs = selector.xpath(f"{doc_base_path}/div[{request_body_props_ix}]/*[name()=\"div\"]")
        print(f"number of req body params: {len(direct_divs)}")    

    #
    # responses
    #

    responses_ix = max(path_params_ix, query_params_ix, request_body_props_ix) + 1
    resp_code = selector.xpath(f"{doc_base_path}/div[{responses_ix}]/div[1]/div/strong/text()").get()
    resp_code_desc = selector.xpath(f"{doc_base_path}/div[{responses_ix}]/div[1]/div/span[2]/text()").get()
    print(f"resp_code: {resp_code}")
    print(f"resp_code_desc: {resp_code_desc}")
    direct_divs = selector.xpath(f"{doc_base_path}/div[{responses_ix}]/div[2]/div/div[2]/*[name()=\"div\"]")
    print(f"number of response fields: {len(direct_divs)}")    

    error_responses_raw_str = selector.xpath(f"{doc_base_path}/div[{responses_ix+2}]/div[1]/div/text()").get()
    error_responses = list(re.findall(r'\b\d{3}\b', error_responses_raw_str))
    print(f"error_responses: {error_responses}")

    print(f"\n========\n")


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
        print(f"Cleaning directory: {target_dir}\n")
        print(f"========\n")
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
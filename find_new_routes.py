#!/usr/bin/env python3
import yaml
import argparse
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException, TimeoutException
from urllib3.exceptions import MaxRetryError
import ssl
import time

def get_existing_routes(provider):
    """Extract existing routes from the manifest file."""
    manifest_file = f"manifests/{provider}_api_manifest.yml"
    existing_routes = set()
    
    try:
        with open(manifest_file, 'r') as f:
            manifest = yaml.safe_load(f)
    except FileNotFoundError:
        print(f"Error: {manifest_file} not found")
        sys.exit(1)
    except yaml.YAMLError as e:
        print(f"Error parsing {manifest_file}: {e}")
        sys.exit(1)

    # Extract all docPaths from the manifest
    for service_data in manifest['services'].values():
        for resource in service_data['resources']:
            for method in resource['methods']:
                existing_routes.add(method['docPath'])
    
    return existing_routes

def scrape_documentation_links(provider, max_retries=5, retry_delay=5):
    """Scrape all API documentation links from the introduction page."""
    url = f"https://docs.databricks.com/api/{provider}/introduction"
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    driver = None
    discovered_links = set()

    for attempt in range(max_retries):
        try:
            driver = webdriver.Chrome(
                service=Service("inc/chromedriver.exe"),
                options=chrome_options
            )

            driver.get(url)

            # Wait for the navigation element to load
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div/div[1]/div[2]"))
            )

            # Find all links in the navigation
            nav_element = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[1]/div[2]")
            links = nav_element.find_elements(By.TAG_NAME, "a")

            # Process each link
            base_url = f"https://docs.databricks.com/api/{provider}/"
            for link in links:
                href = link.get_attribute('href')
                if href and href.startswith(base_url):
                    # Exclude introduction page and root service links
                    if (not href.endswith('/introduction') and 
                        len(href.split('/')) > 6):  # This ensures we're beyond root service level
                        discovered_links.add(href)

            return discovered_links

        except (ssl.SSLError, MaxRetryError, TimeoutException, WebDriverException) as e:
            print(f"Known error occurred on attempt {attempt + 1}/{max_retries}: {e}")
            if attempt + 1 == max_retries:
                print("Max retries reached. Failing program.")
                raise
            else:
                print(f"Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)

        except Exception as e:
            print(f"Unexpected error: {e}")
            raise

        finally:
            if driver:
                driver.quit()

def main():
    parser = argparse.ArgumentParser(description='Find new API routes not in manifest')
    parser.add_argument('provider', choices=['account', 'workspace'],
                      help='The provider type to process (account or workspace)')
    
    args = parser.parse_args()
    
    # Get existing routes from manifest
    existing_routes = get_existing_routes(args.provider)
    
    # Get current routes from documentation
    current_routes = scrape_documentation_links(args.provider)
    
    # Find new routes
    new_routes = current_routes - existing_routes
    
    # Print results
    if new_routes:
        print("\nnew routes discovered:")
        for route in sorted(new_routes):
            print(route)
    else:
        print("\nno new routes discovered")

if __name__ == "__main__":
    main()
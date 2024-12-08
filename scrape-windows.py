from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import json
import re

# URL of the page to scrape
url = 'https://docs.databricks.com/api/workspace/clusters/setpermissions'

def scrape_dynamic_content(url):
    # Configure Selenium WebDriver with headless Chrome
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Specify the path to the downloaded ChromeDriver
    driver = webdriver.Chrome(
        service=Service("inc/chromedriver.exe"),  # Replace with your actual path
        options=chrome_options
    )

    try:
        # Open the page
        driver.get(url)

        # Wait for a specific element (e.g., the main content) to load
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "root"))  # Adjust the selector to a visible element
        )

        # Extract the full rendered HTML
        page_source = driver.page_source

        # Parse the content using BeautifulSoup
        soup = BeautifulSoup(page_source, "html.parser")

        # Remove unwanted elements
        for tag in soup(["head", "script", "meta", "title", "style", "svg", "input", "iframe"]):
            tag.decompose()  # Remove these tags and their contents

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
    stop_keywords = {"Request samples", "Response samples"}  # Keywords to stop capturing

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

if __name__ == "__main__":
    # Scrape the page content
    soup = scrape_dynamic_content(url)

    # Extract HTTP verb section
    http_section = extract_http_section(soup)

    # Save the HTTP section to a text file
    with open("http_section_content.txt", "w", encoding="utf-8") as file:
        file.write("\n".join(http_section))
    print("HTTP section content saved as http_section_content.txt.")
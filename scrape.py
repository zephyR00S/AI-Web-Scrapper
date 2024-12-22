from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

AUTH = 'brd-customer-hl_449d7b07-zone-ai_web_scraper:z716jrjxzoa3'
SBR_WEBDRIVER = f'https://{AUTH}@brd.superproxy.io:9515'

def scrape_site(website):
    print('Launching Chrome browser')
    
    sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, 'goog', 'chrome')
    with Remote(sbr_connection, options=ChromeOptions()) as driver:
        
        driver.get(website)
        print('Taking page screenshot to file page.png')
        driver.get_screenshot_as_file('./page.png')
        print('Navigated! Scraping page content...')
        html = driver.page_source
        
        if not html or html.strip() == "":
            print("Error: Failed to retrieve page source.")
            return None
        
        return html

def extract_body_content(html_content):
    if not html_content:
        print("Error: No HTML content provided.")
        return None
    
    soup = BeautifulSoup(html_content, 'html.parser')
    body_content = soup.body
    
    if body_content:
        return str(body_content)
    print("Error: No body tag found in HTML content.")
    return None

def cleaned_content(body_content):
    if not body_content:
        print("Error: No body content to clean.")
        return ""
    
    soup = BeautifulSoup(body_content, 'html.parser')
    
    # Remove script and style tags
    for script_or_style in soup(['script', 'style']):
        script_or_style.extract()
        
    clean_content = soup.get_text(separator='\n')
    clean_content = '\n'.join(
        line.strip() for line in clean_content.splitlines() if line.strip()
    )
    
    return clean_content

def split_dom_content(dom_content, max_len=6000):
    if not dom_content or len(dom_content.strip()) == 0:
        print("Error: DOM content is empty or None.")
        return []  # Return an empty list to prevent further issues
    
    # Safely split the content into chunks of `max_len`
    return [dom_content[i:i+max_len] for i in range(0, len(dom_content), max_len)]
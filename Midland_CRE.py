from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from datetime import date, datetime, timedelta
import time as sys_time

# Set webdriver options
chrome_options = webdriver.chrome.options.Options()

prefs = {
    'download.extensions_to_open': 'xml',
    'safebrowsing.enabled': True
}
## Uncomment the below to let the program run in the background
options = webdriver.ChromeOptions()
options.add_experimental_option('prefs', prefs)
options.add_argument("start-maximized")
options.add_argument("--headless")
# options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument("--safebrowsing-disable-download-protection")
options.add_argument("safebrowsing-disable-extension-blacklist")
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

def scrape_data():
    def wait_for_page_load(driver):
        sys_time.sleep(10)  # Wait for 10 seconds for the page to load

    # Retail
    # Lease
    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://www.midlandici.com.hk/ics/property/find/shops/lease'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    retail_lease = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/div[1]/span').text
    
    # Sales
    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://www.midlandici.com.hk/ics/property/find/shops/sale'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    retail_sales = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/div[1]/span').text
    
    # Office
    # Lease
    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://www.midlandici.com.hk/ics/property/find/office/lease'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    office_lease = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/div[1]/span').text
    
    # Sales
    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://www.midlandici.com.hk/ics/property/find/office/sale'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    office_sales = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/div[1]/span').text
    
    # Factory
    # Lease
    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://www.midlandici.com.hk/ics/property/find/industrial/lease'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    factory_lease = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/div[1]/span').text
    
    # Sales
    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://www.midlandici.com.hk/ics/property/find/industrial/sale'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    factory_sales = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/div[1]/span').text
    
    d = date.today() + timedelta(days=1)
    
    driver.quit()  # Quit the webdriver to release resources
    
    return [d, retail_sales, retail_lease, office_sales, office_lease, factory_sales, factory_lease]

# Scrape data
data = [scrape_data()]

# Load existing data from file
try:
    df = pd.read_excel("Mid_CRE.xlsx")
except FileNotFoundError:
    df = pd.DataFrame(columns=["Date", "Retail Sales", "Retail Lease", "Office Sales", "Office Lease", "Industrial Sales", "Industrial Lease"])

# Convert the "Date" column to the desired format
df["Date"] = pd.to_datetime(df["Date"]).dt.strftime("%Y-%m-%d")

# Append new data to the dataframe
df = pd.concat([df, pd.DataFrame(data, columns=df.columns)], ignore_index=True)

# Save dataframe to file
df.to_excel("Mid_CRE.xlsx", sheet_name="sheet1", index=False)

print("Data appended successfully.")

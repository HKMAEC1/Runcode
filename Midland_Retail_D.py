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

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://www.midlandici.com.hk/ics/property/find/shops/lease?districts=CEN&lang=english'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    CEN = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/div[1]/span').text
    
    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://www.midlandici.com.hk/ics/property/find/shops/lease?districts=WES&lang=english'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    WES = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/div[1]/span').text

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://www.midlandici.com.hk/ics/property/find/shops/lease?districts=SHW&lang=english'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    SHW = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/div[1]/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://www.midlandici.com.hk/ics/property/find/shops/lease?districts=WAC&lang=english'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    WAC = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/div[1]/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://www.midlandici.com.hk/ics/property/find/shops/lease?districts=CAB&lang=english'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    CAB = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/div[1]/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://www.midlandici.com.hk/ics/property/find/shops/lease?districts=TIH&lang=english'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    TIH = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/div[1]/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://www.midlandici.com.hk/ics/property/find/shops/lease?districts=HAV&lang=english'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    HAV = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/div[1]/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://www.midlandici.com.hk/ics/property/find/shops/lease?districts=TAH&lang=english'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    TAH = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/div[1]/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://www.midlandici.com.hk/ics/property/find/shops/lease?districts=NOP&lang=english'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    NOP = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/div[1]/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://www.midlandici.com.hk/ics/property/find/shops/lease?districts=SKW&lang=english'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    SKW = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/div[1]/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://www.midlandici.com.hk/ics/property/find/shops/lease?districts=QUB&lang=english'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    QUB = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/div[1]/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://www.midlandici.com.hk/ics/property/find/shops/lease?districts=CHW&lang=english'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    CHW = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/div[1]/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://www.midlandici.com.hk/ics/property/find/shops/lease?districts=SOU&lang=english'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    SOU = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/div[1]/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://www.midlandici.com.hk/ics/property/find/shops/lease?districts=ABE&lang=english'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    ABE = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/div[1]/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://www.midlandici.com.hk/ics/property/find/shops/lease?districts=MOK&lang=english'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    MOK = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/div[1]/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://www.midlandici.com.hk/ics/property/find/shops/lease?districts=TST&lang=english'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    TST = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/div[1]/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://www.midlandici.com.hk/ics/property/find/shops/lease?districts=JOR&lang=english'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    JOR = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/div[1]/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://www.midlandici.com.hk/ics/property/find/shops/lease?districts=YMT&lang=english'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    YMT = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/div[1]/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://www.midlandici.com.hk/ics/property/find/shops/lease?districts=TKT&lang=english'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    TKT = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/div[1]/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://www.midlandici.com.hk/ics/property/find/shops/lease?districts=TSE&lang=english'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    TSE = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/div[1]/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://www.midlandici.com.hk/ics/property/find/shops/lease?districts=SSP&lang=english'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    SSP = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/div[1]/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://www.midlandici.com.hk/ics/property/find/shops/lease?districts=CSW&lang=english'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    CSW = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/div[1]/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://www.midlandici.com.hk/ics/property/find/shops/lease?districts=MEF&lang=english'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    MEF = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/div[1]/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://www.midlandici.com.hk/ics/property/find/shops/lease?districts=KOC&lang=english'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    KOC = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/div[1]/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://www.midlandici.com.hk/ics/property/find/shops/lease?districts=TKW&lang=english'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    TKW = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/div[1]/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://www.midlandici.com.hk/ics/property/find/shops/lease?districts=HUH&lang=english'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    HUH = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/div[1]/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://www.midlandici.com.hk/ics/property/find/shops/lease?districts=KAT&lang=english'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    KAT = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/div[1]/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://www.midlandici.com.hk/ics/property/find/shops/lease?districts=SPK&lang=english'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    SPK = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/div[1]/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://www.midlandici.com.hk/ics/property/find/shops/lease?districts=WTS&lang=english'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    WTS = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/div[1]/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://www.midlandici.com.hk/ics/property/find/shops/lease?districts=KWT&lang=english'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    KWT = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/div[1]/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://www.midlandici.com.hk/ics/property/find/shops/lease?districts=NTK&lang=english'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    NTK = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/div[1]/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://www.midlandici.com.hk/ics/property/find/shops/lease?districts=KOB&lang=english'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    KOB = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/div[1]/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://www.midlandici.com.hk/ics/property/find/shops/lease?districts=YAT&lang=english'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    YAT = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/div[1]/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://www.midlandici.com.hk/ics/property/find/shops/lease?districts=KWC&lang=english'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    KWC = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/div[1]/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://www.midlandici.com.hk/ics/property/find/shops/lease?districts=TSY&lang=english'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    TSY = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/div[1]/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://www.midlandici.com.hk/ics/property/find/shops/lease?districts=TSW&lang=english'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    TSW = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/div[1]/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://www.midlandici.com.hk/ics/property/find/shops/lease?districts=TUM&lang=english'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    TUM = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/div[1]/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://www.midlandici.com.hk/ics/property/find/shops/lease?districts=YUL&lang=english'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    YUL = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/div[1]/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://www.midlandici.com.hk/ics/property/find/shops/lease?districts=TIS&lang=english'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    TIS = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/div[1]/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://www.midlandici.com.hk/ics/property/find/shops/lease?districts=HSK&lang=english'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    HSK = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/div[1]/span').text

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://www.midlandici.com.hk/ics/property/find/shops/lease?districts=SHS&lang=english'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    SHS = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/div[1]/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://www.midlandici.com.hk/ics/property/find/shops/lease?districts=FAN&lang=english'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    FAN = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/div[1]/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://www.midlandici.com.hk/ics/property/find/shops/lease?districts=TAP&lang=english'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    TAP = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/div[1]/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://www.midlandici.com.hk/ics/property/find/shops/lease?districts=SHT&lang=english'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    SHT = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/div[1]/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://www.midlandici.com.hk/ics/property/find/shops/lease?districts=TAW&lang=english'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    TAW = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/div[1]/span').text

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://www.midlandici.com.hk/ics/property/find/shops/lease?districts=MOS&lang=english'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    MOS = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/div[1]/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://www.midlandici.com.hk/ics/property/find/shops/lease?districts=TKO&lang=english'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    TKO = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/div[1]/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://www.midlandici.com.hk/ics/property/find/shops/lease?districts=SAK&lang=english'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    SAK = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/div[1]/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://www.midlandici.com.hk/ics/property/find/shops/lease?districts=ISI&lang=english'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    ISI = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/div[1]/span').text 

    d = date.today() + timedelta(days=1)
    
    driver.quit()  # Quit the webdriver to release resources
    
    return [d, retail_lease, CEN, WES, SHW, WAC, CAB, TIH, HAV, TAH, NOP, SKW, QUB, CHW, SOU, ABE, MOK, TST, JOR, YMT, TKT, TSE, SSP, CSW, MEF, KOC, TKW, HUH, KAT, SPK, WTS, KWT, NTK, KOB, YAT, KWC, TSY, TSW, TUM, YUL, TIS, HSK, SHS, FAN, TAP, SHT, TAW, MOS, TKO, SAK, ISI]

# Scrape data
data = [scrape_data()]

# Load existing data from file
try:
    df = pd.read_excel("Mid_Retail_district.xlsx")
except FileNotFoundError:
    df = pd.DataFrame(columns=["Date", "Retail Sales", "Central", "Western District", "Sheung Wan", "Wan Chai", "Causeway Bay", "Tin Hau", "Happy Valley", "Tai Hang", "North Point", "Shau Kei Wan", "Quarry Bay", "Chai Wan", "Island South", "Aberdeen", "Mongkok", "Tsim Sha Tsui", "Jordan", "Yau Ma Tei", "Tai Kok Tsui", "Tsim Sha Tsui East", "Sham Shui Po", "Cheung Sha Wan", "Mei Foo", "Kowloon City", "To KWa Wan", "Hung Hom", "Kai Tak", "San Po Kong", "Wong Tai Sin", "Kwun Tong", "Ngau Tau Kok", "Kowloon Bay", "Yau Tong", "Kwai Chung", "Tsing Yi", "Tsuen Wan", "Tuen Man", "Yuen Long", "Tin Shui Wai", "Hung Shui Kiu", "Sheung Shui", "Fanling", "Tai Po", "Sha Tin", "Tai Wai", "Ma On Shan", "Tseung Kwan O", "Sai Kung", "Island"])

# Convert the "Date" column to the desired format
df["Date"] = pd.to_datetime(df["Date"]).dt.strftime("%Y-%m-%d")

# Append new data to the dataframe
df = pd.concat([df, pd.DataFrame(data, columns=df.columns)], ignore_index=True)

# Save dataframe to file
df.to_excel("Mid_Retail_district.xlsx", sheet_name="sheet1", index=False)

print("Data appended successfully.")

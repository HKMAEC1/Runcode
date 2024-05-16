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
        sys_time.sleep(5)  # Wait for 10 seconds for the page to load

    # Retail
    # Lease
    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/lease/retail/'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    retail_lease = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div/div[1]/h1/span').text

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS004&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    CEN = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div/div[1]/h1/span').text
    
    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS001&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    WES = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div/div[1]/h1/span').text

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS003&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    SHW = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/h1/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS006&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    WAC = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div/div[1]/h1/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS012&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    CAB = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div/div[1]/h1/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS046&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    TIH = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div/div[1]/h1/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS048&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    HAV = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div/div[1]/h1/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS049&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    TAS = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div/div[1]/h1/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS008&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    NOP = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div/div[1]/h1/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS011&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    SKW = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div/div[1]/h1/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS009&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    QUB = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div/div[1]/h1/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS007&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    CHW = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div/div[1]/h1/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS002&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    SOU = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div/div[1]/h1/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS005&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    ADM = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div/div[1]/h1/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS013&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    SSW = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div/div[1]/h1/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS010&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    SWH = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div/div[1]/h1/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS047&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    ABE = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div/div[1]/h1/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS020&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    MOK = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div/div[1]/h1/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS023&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    TST = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div/div[1]/h1/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS022&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    JOR = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div/div[1]/h1/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS021&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    YMT = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div/div[1]/h1/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS018&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    TKT = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div/div[1]/h1/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS016&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    SSP = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div/div[1]/h1/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS015&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    CSW = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div/div[1]/h1/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS014&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    MEF = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div/div[1]/h1/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS025&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    KOC = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div/div[1]/h1/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS026&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    TKW = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div/div[1]/h1/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS027&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    HUH = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div/div[1]/h1/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS030&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    SPK = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div/div[1]/h1/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS029&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    WTS = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div/div[1]/h1/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS024&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    KWT = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div/div[1]/h1/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS031&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    KOB = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div/div[1]/h1/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS021&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    YMT = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div/div[1]/h1/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS019&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    PRI = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div/div[1]/h1/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS045&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    HMT = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div/div[1]/h1/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS042&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    KWC = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div/div[1]/h1/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS041&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    TSY = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div/div[1]/h1/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS040&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    TSW = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div/div[1]/h1/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS039&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    TUM = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div/div[1]/h1/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS038&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    YUL = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div/div[1]/h1/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS050&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    TIS = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div/div[1]/h1/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS051&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    SHS = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div/div[1]/h1/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS052&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    FAN = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div/div[1]/h1/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS034&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    TAP = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div/div[1]/h1/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS035&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    SHT = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div/div[1]/h1/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS053&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    TAW = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div/div[1]/h1/span').text

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS054&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    MOS = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div/div[1]/h1/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS037&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    TKO = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div/div[1]/h1/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS036&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    SAK = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div/div[1]/h1/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS044&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    ISI = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div/div[1]/h1/span').text 

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS043&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    LAK = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div/div[1]/h1/span').text 

    d = date.today() + timedelta(days=1)
    
    driver.quit()  # Quit the webdriver to release resources
    
    return [d, retail_lease, CEN, WES, SHW, WAC, CAB, TIH, HAV, TAS, NOP, SKW, QUB, CHW, SOU, ADM, SSW, SWH, ABE, MOK, TST, JOR, YMT, TKT, SSP, CSW, MEF, KOC, TKW, HUH, SPK, WTS, KWT, KOB, YMT, PRI, HMT, KWC, TSY, TSW, TUM, YUL, TIS, SHS, FAN, TAP, SHT, TAW, MOS, TKO, SAK, ISI, LAK]

# Scrape data
data = [scrape_data()]

# Load existing data from file
try:
    df = pd.read_excel("Cen_Retail_district.xlsx")
except FileNotFoundError:
    df = pd.DataFrame(columns=["Date", "Retail lease", "Central", "Western District", "Sheung Wan", "Wan Chai", "Causeway Bay", "Tin Hau", "Happy Valley", "TaiKoo Shing", "North Point", "Shau Kei Wan", "Quarry Bay", "Chai Wan", "Island South", "Admiralty", "Siu Sai Wan", "Sai Wan Ho", "Aberdeen", "Mongkok", "Tsim Sha Tsui", "Jordan", "Yau Ma Tei", "Tai Kok Tsui", "Sham Shui Po", "Cheung Sha Wan", "Mei Foo", "Kowloon City", "To Kwa Wan", "Hung Hom", "San Po Kong", "Wong Tai Sin", "Kwun Tong", "Kowloon Bay", "Yau Ma Tei", "Prince Edward", "Ho Man Tin", "Kwai Chung", "Tsing Yi", "Tsuen Wan", "Tuen Man", "Yuen Long", "Tin Shui Wai", "Sheung Shui", "Fanling", "Tai Po", "Sha Tin", "Tai Wai", "Ma On Shan", "Tseung Kwan O", "Sai Kung", "Island", "Lai King"])

# Convert the "Date" column to the desired format
df["Date"] = pd.to_datetime(df["Date"]).dt.strftime("%Y-%m-%d")

# Append new data to the dataframe
df = pd.concat([df, pd.DataFrame(data, columns=df.columns)], ignore_index=True)

# Save dataframe to file
df.to_excel("Cen_Retail_district.xlsx", sheet_name="sheet1", index=False)

print("Data appended successfully.")

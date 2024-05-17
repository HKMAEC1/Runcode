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
    xpath1 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/h1/span'
    xpath2 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div[1]/section/div/h1/span'
    try:
        CEN = driver.find_element_by_xpath(xpath1).text
    except Exception as e:
        if 'no such element' in str(e).lower():
            CEN = driver.find_element_by_xpath(xpath2).text
        else:
            raise  
    
    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS001&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    xpath1 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/h1/span'
    xpath2 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div[1]/section/div/h1/span'
    try:
        WES = driver.find_element_by_xpath(xpath1).text
    except Exception as e:
        if 'no such element' in str(e).lower():
            WES = driver.find_element_by_xpath(xpath2).text
        else:
            raise  

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS003&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    xpath1 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/h1/span'
    xpath2 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div[1]/section/div/h1/span'
    try:
        SHW = driver.find_element_by_xpath(xpath1).text
    except Exception as e:
        if 'no such element' in str(e).lower():
            SHW = driver.find_element_by_xpath(xpath2).text
        else:
            raise    

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS006&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    xpath1 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/h1/span'
    xpath2 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div[1]/section/div/h1/span'
    try:
        WAC = driver.find_element_by_xpath(xpath1).text
    except Exception as e:
        if 'no such element' in str(e).lower():
            WAC = driver.find_element_by_xpath(xpath2).text
        else:
            raise  

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS012&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    xpath1 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/h1/span'
    xpath2 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div[1]/section/div/h1/span'
    try:
        CAB = driver.find_element_by_xpath(xpath1).text
    except Exception as e:
        if 'no such element' in str(e).lower():
            CAB = driver.find_element_by_xpath(xpath2).text
        else:
            raise  

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS046&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    xpath1 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/h1/span'
    xpath2 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div[1]/section/div/h1/span'
    try:
        TIH = driver.find_element_by_xpath(xpath1).text
    except Exception as e:
        if 'no such element' in str(e).lower():
            TIH = driver.find_element_by_xpath(xpath2).text
        else:
            raise   

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS048&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    xpath1 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/h1/span'
    xpath2 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div[1]/section/div/h1/span'
    try:
        HAV = driver.find_element_by_xpath(xpath1).text
    except Exception as e:
        if 'no such element' in str(e).lower():
            HAV = driver.find_element_by_xpath(xpath2).text
        else:
            raise  

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS049&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    xpath1 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/h1/span'
    xpath2 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div[1]/section/div/h1/span'
    try:
        TAS = driver.find_element_by_xpath(xpath1).text
    except Exception as e:
        if 'no such element' in str(e).lower():
            TAS = driver.find_element_by_xpath(xpath2).text
        else:
            raise

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS008&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    xpath1 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/h1/span'
    xpath2 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div[1]/section/div/h1/span'
    try:
        NOP = driver.find_element_by_xpath(xpath1).text
    except Exception as e:
        if 'no such element' in str(e).lower():
            NOP = driver.find_element_by_xpath(xpath2).text
        else:
            raise  

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS011&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    xpath1 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/h1/span'
    xpath2 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div[1]/section/div/h1/span'
    try:
        SKW = driver.find_element_by_xpath(xpath1).text
    except Exception as e:
        if 'no such element' in str(e).lower():
            SKW = driver.find_element_by_xpath(xpath2).text
        else:
            raise  

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS009&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    xpath1 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/h1/span'
    xpath2 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div[1]/section/div/h1/span'
    try:
        QUB = driver.find_element_by_xpath(xpath1).text
    except Exception as e:
        if 'no such element' in str(e).lower():
            QUB = driver.find_element_by_xpath(xpath2).text
        else:
            raise  

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS007&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    xpath1 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/h1/span'
    xpath2 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div[1]/section/div/h1/span'
    try:
        CHW = driver.find_element_by_xpath(xpath1).text
    except Exception as e:
        if 'no such element' in str(e).lower():
            CHW = driver.find_element_by_xpath(xpath2).text
        else:
            raise  

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS002&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    xpath1 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/h1/span'
    xpath2 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div[1]/section/div/h1/span'
    try:
        SOU = driver.find_element_by_xpath(xpath1).text
    except Exception as e:
        if 'no such element' in str(e).lower():
            SOU = driver.find_element_by_xpath(xpath2).text
        else:
            raise  

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS005&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    xpath1 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/h1/span'
    xpath2 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div[1]/section/div/h1/span'
    try:
        ADM = driver.find_element_by_xpath(xpath1).text
    except Exception as e:
        if 'no such element' in str(e).lower():
            ADM = driver.find_element_by_xpath(xpath2).text
        else:
            raise  

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS013&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    xpath1 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/h1/span'
    xpath2 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div[1]/section/div/h1/span'
    try:
        SSW = driver.find_element_by_xpath(xpath1).text
    except Exception as e:
        if 'no such element' in str(e).lower():
            SSW = driver.find_element_by_xpath(xpath2).text
        else:
            raise  

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS010&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    xpath1 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/h1/span'
    xpath2 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div[1]/section/div/h1/span'
    try:
        SWH = driver.find_element_by_xpath(xpath1).text
    except Exception as e:
        if 'no such element' in str(e).lower():
            SWH = driver.find_element_by_xpath(xpath2).text
        else:
            raise  

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS047&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    xpath1 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/h1/span'
    xpath2 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div[1]/section/div/h1/span'
    try:
        ABE = driver.find_element_by_xpath(xpath1).text
    except Exception as e:
        if 'no such element' in str(e).lower():
            ABE = driver.find_element_by_xpath(xpath2).text
        else:
            raise  

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS020&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    xpath1 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/h1/span'
    xpath2 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div[1]/section/div/h1/span'
    try:
        MOK = driver.find_element_by_xpath(xpath1).text
    except Exception as e:
        if 'no such element' in str(e).lower():
            MOK = driver.find_element_by_xpath(xpath2).text
        else:
            raise  

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS023&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    xpath1 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/h1/span'
    xpath2 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div[1]/section/div/h1/span'
    try:
        TST = driver.find_element_by_xpath(xpath1).text
    except Exception as e:
        if 'no such element' in str(e).lower():
            TST = driver.find_element_by_xpath(xpath2).text
        else:
            raise  

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS022&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    xpath1 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/h1/span'
    xpath2 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div[1]/section/div/h1/span'
    try:
        JOR = driver.find_element_by_xpath(xpath1).text
    except Exception as e:
        if 'no such element' in str(e).lower():
            JOR = driver.find_element_by_xpath(xpath2).text
        else:
            raise  

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS021&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    xpath1 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/h1/span'
    xpath2 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div[1]/section/div/h1/span'
    try:
        YMT = driver.find_element_by_xpath(xpath1).text
    except Exception as e:
        if 'no such element' in str(e).lower():
            YMT = driver.find_element_by_xpath(xpath2).text
        else:
            raise  

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS018&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    xpath1 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/h1/span'
    xpath2 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div[1]/section/div/h1/span'
    try:
        TKT = driver.find_element_by_xpath(xpath1).text
    except Exception as e:
        if 'no such element' in str(e).lower():
            TKT = driver.find_element_by_xpath(xpath2).text
        else:
            raise  

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS016&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    xpath1 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/h1/span'
    xpath2 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div[1]/section/div/h1/span'
    try:
        SSP = driver.find_element_by_xpath(xpath1).text
    except Exception as e:
        if 'no such element' in str(e).lower():
            SSP = driver.find_element_by_xpath(xpath2).text
        else:
            raise

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS015&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    xpath1 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/h1/span'
    xpath2 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div[1]/section/div/h1/span'
    try:
        CSW = driver.find_element_by_xpath(xpath1).text
    except Exception as e:
        if 'no such element' in str(e).lower():
            CSW = driver.find_element_by_xpath(xpath2).text
        else:
            raise  

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS014&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    xpath1 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/h1/span'
    xpath2 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div[1]/section/div/h1/span'
    try:
        MEF = driver.find_element_by_xpath(xpath1).text
    except Exception as e:
        if 'no such element' in str(e).lower():
            MEF = driver.find_element_by_xpath(xpath2).text
        else:
            raise  

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS025&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    xpath1 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/h1/span'
    xpath2 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div[1]/section/div/h1/span'
    try:
        KOC = driver.find_element_by_xpath(xpath1).text
    except Exception as e:
        if 'no such element' in str(e).lower():
            KOC = driver.find_element_by_xpath(xpath2).text
        else:
            raise   

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS026&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    xpath1 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/h1/span'
    xpath2 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div[1]/section/div/h1/span'
    try:
        TKW = driver.find_element_by_xpath(xpath1).text
    except Exception as e:
        if 'no such element' in str(e).lower():
            TKW = driver.find_element_by_xpath(xpath2).text
        else:
            raise  

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS027&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    xpath1 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/h1/span'
    xpath2 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div[1]/section/div/h1/span'
    try:
        HUH = driver.find_element_by_xpath(xpath1).text
    except Exception as e:
        if 'no such element' in str(e).lower():
            HUH = driver.find_element_by_xpath(xpath2).text
        else:
            raise  

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS030&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    xpath1 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/h1/span'
    xpath2 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div[1]/section/div/h1/span'
    try:
        SPK = driver.find_element_by_xpath(xpath1).text
    except Exception as e:
        if 'no such element' in str(e).lower():
            SPK = driver.find_element_by_xpath(xpath2).text
        else:
            raise  

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS029&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    xpath1 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/h1/span'
    xpath2 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div[1]/section/div/h1/span'
    try:
        WTS = driver.find_element_by_xpath(xpath1).text
    except Exception as e:
        if 'no such element' in str(e).lower():
            WTS = driver.find_element_by_xpath(xpath2).text
        else:
            raise  

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS024&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    xpath1 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/h1/span'
    xpath2 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div[1]/section/div/h1/span'
    try:
        KWT = driver.find_element_by_xpath(xpath1).text
    except Exception as e:
        if 'no such element' in str(e).lower():
            KWT = driver.find_element_by_xpath(xpath2).text
        else:
            raise  

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS031&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    xpath1 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/h1/span'
    xpath2 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div[1]/section/div/h1/span'
    try:
        KOB = driver.find_element_by_xpath(xpath1).text
    except Exception as e:
        if 'no such element' in str(e).lower():
            KOB = driver.find_element_by_xpath(xpath2).text
        else:
            raise  

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS021&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    xpath1 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/h1/span'
    xpath2 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div[1]/section/div/h1/span'
    try:
        YMT = driver.find_element_by_xpath(xpath1).text
    except Exception as e:
        if 'no such element' in str(e).lower():
            YMT = driver.find_element_by_xpath(xpath2).text
        else:
            raise  

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS019&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    xpath1 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/h1/span'
    xpath2 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div[1]/section/div/h1/span'
    try:
        PRI = driver.find_element_by_xpath(xpath1).text
    except Exception as e:
        if 'no such element' in str(e).lower():
            PRI = driver.find_element_by_xpath(xpath2).text
        else:
            raise  

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS045&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    xpath1 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/h1/span'
    xpath2 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div[1]/section/div/h1/span'
    try:
        HMT = driver.find_element_by_xpath(xpath1).text
    except Exception as e:
        if 'no such element' in str(e).lower():
            HMT = driver.find_element_by_xpath(xpath2).text
        else:
            raise  

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS042&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    xpath1 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/h1/span'
    xpath2 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div[1]/section/div/h1/span'
    try:
        KWC = driver.find_element_by_xpath(xpath1).text
    except Exception as e:
        if 'no such element' in str(e).lower():
            KWC = driver.find_element_by_xpath(xpath2).text
        else:
            raise  

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS041&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    xpath1 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/h1/span'
    xpath2 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div[1]/section/div/h1/span'
    try:
        TSY = driver.find_element_by_xpath(xpath1).text
    except Exception as e:
        if 'no such element' in str(e).lower():
            TSY = driver.find_element_by_xpath(xpath2).text
        else:
            raise  

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS040&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    xpath1 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/h1/span'
    xpath2 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div[1]/section/div/h1/span'
    try:
        TSW = driver.find_element_by_xpath(xpath1).text
    except Exception as e:
        if 'no such element' in str(e).lower():
            TSW = driver.find_element_by_xpath(xpath2).text
        else:
            raise  

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS039&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    xpath1 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/h1/span'
    xpath2 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div[1]/section/div/h1/span'
    try:
        TUM = driver.find_element_by_xpath(xpath1).text
    except Exception as e:
        if 'no such element' in str(e).lower():
            TUM = driver.find_element_by_xpath(xpath2).text
        else:
            raise  

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS038&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    xpath1 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/h1/span'
    xpath2 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div[1]/section/div/h1/span'
    try:
        YUL = driver.find_element_by_xpath(xpath1).text
    except Exception as e:
        if 'no such element' in str(e).lower():
            YUL = driver.find_element_by_xpath(xpath2).text
        else:
            raise  

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS050&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    xpath1 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/h1/span'
    xpath2 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div[1]/section/div/h1/span'
    try:
        TIS = driver.find_element_by_xpath(xpath1).text
    except Exception as e:
        if 'no such element' in str(e).lower():
            TIS = driver.find_element_by_xpath(xpath2).text
        else:
            raise  

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS051&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    xpath1 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/h1/span'
    xpath2 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div[1]/section/div/h1/span'
    try:
        SHS = driver.find_element_by_xpath(xpath1).text
    except Exception as e:
        if 'no such element' in str(e).lower():
            SHS = driver.find_element_by_xpath(xpath2).text
        else:
            raise  

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS052&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    xpath1 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/h1/span'
    xpath2 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div[1]/section/div/h1/span'
    try:
        FAN = driver.find_element_by_xpath(xpath1).text
    except Exception as e:
        if 'no such element' in str(e).lower():
            FAN = driver.find_element_by_xpath(xpath2).text
        else:
            raise  

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS034&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    xpath1 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/h1/span'
    xpath2 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div[1]/section/div/h1/span'
    try:
        TAP = driver.find_element_by_xpath(xpath1).text
    except Exception as e:
        if 'no such element' in str(e).lower():
            TAP = driver.find_element_by_xpath(xpath2).text
        else:
            raise  

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS035&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    xpath1 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/h1/span'
    xpath2 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div[1]/section/div/h1/span'
    try:
        SHT = driver.find_element_by_xpath(xpath1).text
    except Exception as e:
        if 'no such element' in str(e).lower():
            SHT = driver.find_element_by_xpath(xpath2).text
        else:
            raise  

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS053&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    xpath1 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/h1/span'
    xpath2 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div[1]/section/div/h1/span'
    try:
        TAW = driver.find_element_by_xpath(xpath1).text
    except Exception as e:
        if 'no such element' in str(e).lower():
            TAW = driver.find_element_by_xpath(xpath2).text
        else:
            raise  

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS054&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    xpath1 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/h1/span'
    xpath2 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div[1]/section/div/h1/span'
    try:
        MOS = driver.find_element_by_xpath(xpath1).text
    except Exception as e:
        if 'no such element' in str(e).lower():
            MOS = driver.find_element_by_xpath(xpath2).text
        else:
            raise  

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS037&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    xpath1 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/h1/span'
    xpath2 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div[1]/section/div/h1/span'
    try:
        TKO = driver.find_element_by_xpath(xpath1).text
    except Exception as e:
        if 'no such element' in str(e).lower():
            TKO = driver.find_element_by_xpath(xpath2).text
        else:
            raise  

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS036&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    xpath1 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/h1/span'
    xpath2 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div[1]/section/div/h1/span'
    try:
        SAK = driver.find_element_by_xpath(xpath1).text
    except Exception as e:
        if 'no such element' in str(e).lower():
            SAK = driver.find_element_by_xpath(xpath2).text
        else:
            raise  

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS044&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    xpath1 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/h1/span'
    xpath2 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div[1]/section/div/h1/span'
    try:
        ISI = driver.find_element_by_xpath(xpath1).text
    except Exception as e:
        if 'no such element' in str(e).lower():
            ISI = driver.find_element_by_xpath(xpath2).text
        else:
            raise

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
    url = 'https://oir.centanet.com/en/lease/search/?districts=WS043&usages=Retail'
    driver.get(url)
    wait_for_page_load(driver)  # Wait for the page to load
    xpath1 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/h1/span'
    xpath2 = '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div[1]/section/div/h1/span'
    try:
        LAK = driver.find_element_by_xpath(xpath1).text
    except Exception as e:
        if 'no such element' in str(e).lower():
            LAK = driver.find_element_by_xpath(xpath2).text
        else:
            raise  

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

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
from datetime import date, datetime, timedelta
import time

def get_data(url):
    driver.get(url)
    time.sleep(5)
    
    xpath1 = '//*[@id="__next"]/main/div[2]/div/div[2]/div[1]/div[2]/div/div[1]/div/div/div[2]/div/h2/span'
    xpath2 = '//*[@id="__next"]/main/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div[2]/div/h2/span'
    
    try:
        data = driver.find_element_by_xpath(xpath1).text
    except Exception as e:
        if 'no such element' in str(e).lower():
            data = driver.find_element_by_xpath(xpath2).text
        else:
            raise  


def store_sale(data):
    if data is not None:  # Check if data is not None
        if "," in data:
            data = data.replace(",", "")
        new_data_sale.append(int(data))

def store_lease(data):  # Store scrapped lease data to the list as int
  if "," in data:
    data = data.replace(",","")
  else:
    pass
  new_data_lease.append(int(data))

#set webdriver
chrome_options = webdriver.chrome.options.Options()

prefs = {
'download.extensions_to_open': 'xml',
'safebrowsing.enabled': True
}
## Uncomment the below to let the program to run in background
options = webdriver.ChromeOptions()
options.add_experimental_option('prefs',prefs)
options.add_argument("--headless")
options.add_argument("--disable-extensions")
options.add_argument("--safebrowsing-disable-download-protection")
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

df_sale = pd.read_excel("美聯放盤.xlsx", sheet_name="賣盤")
df_lease = pd.read_excel("美聯放盤.xlsx", sheet_name="租盤")
new_data_sale = []
new_data_lease = []

d = date.today() + timedelta(days=1)
print(d)
new_data_sale.append(d)
new_data_lease.append(d)

#Sequence: All sale, sale_3m, ..., sale_30m, sale_200ft, ..., sale_500ft)
driver = webdriver.Chrome('/usr/bin/chromedriver', options = options)

sale_links = ["https://www.midland.com.hk/zh-hk/list/buy", "https://www.midland.com.hk/zh-hk/list/buy/%E6%90%9C%E5%B0%8B-H-9f94ee16",
"https://www.midland.com.hk/zh-hk/list/buy/%E6%90%9C%E5%B0%8B-H-f1f7c295", "https://www.midland.com.hk/zh-hk/list/buy/%E6%90%9C%E5%B0%8B-H-9466ad7",
"https://www.midland.com.hk/zh-hk/list/buy/%E6%90%9C%E5%B0%8B-H-e071f291", "https://www.midland.com.hk/zh-hk/list/buy/%E6%90%9C%E5%B0%8B-H-4a1fabd7",
"https://www.midland.com.hk/zh-hk/list/buy/%E6%90%9C%E5%B0%8B-H-89cc6595", "https://www.midland.com.hk/zh-hk/list/buy/%E6%90%9C%E5%B0%8B-H-a11b0dd7",
"https://www.midland.com.hk/zh-hk/list/buy/%E6%90%9C%E5%B0%8B-H-34b3e799", "https://www.midland.com.hk/zh-hk/list/buy/%E6%90%9C%E5%B0%8B-H-82a1c2d7",
"https://www.midland.com.hk/zh-hk/list/buy/%E6%90%9C%E5%B0%8B-H-3958edae", "https://www.midland.com.hk/zh-hk/list/buy/%E6%90%9C%E5%B0%8B-H-9825f977",
"https://www.midland.com.hk/zh-hk/list/buy/%E6%90%9C%E5%B0%8B-H-4b628795", "https://www.midland.com.hk/zh-hk/list/buy/%E6%90%9C%E5%B0%8B-H-88cfd3b7",
"https://www.midland.com.hk/zh-hk/list/buy/%E6%90%9C%E5%B0%8B-H-3ad35bf0", "https://www.midland.com.hk/zh-hk/list/buy/%E6%90%9C%E5%B0%8B-H-16f7cbf7",
"https://www.midland.com.hk/zh-hk/list/buy/%E6%90%9C%E5%B0%8B-H-ca345a15", "https://www.midland.com.hk/zh-hk/list/buy/%E6%90%9C%E5%B0%8B-H-efdb0b14",
"https://www.midland.com.hk/zh-hk/list/buy/%E6%90%9C%E5%B0%8B-H-7d688178", "https://www.midland.com.hk/zh-hk/list/buy/%E6%90%9C%E5%B0%8B-H-9a825477",
"https://www.midland.com.hk/zh-hk/list/buy/%E6%90%9C%E5%B0%8B-H-74877fbc", "https://www.midland.com.hk/zh-hk/list/buy/%E6%90%9C%E5%B0%8B-H-3da07f75",              
"https://www.midland.com.hk/zh-hk/list/buy/%E6%90%9C%E5%B0%8B-H-215e6eef", "https://www.midland.com.hk/zh-hk/list/buy/%E6%90%9C%E5%B0%8B-H-6dbf926d",              
"https://www.midland.com.hk/zh-hk/list/buy/%E6%90%9C%E5%B0%8B-H-d1d84feb", "https://www.midland.com.hk/zh-hk/list/buy/%E6%90%9C%E5%B0%8B-H-f989626d",
"https://www.midland.com.hk/zh-hk/list/buy/%E6%90%9C%E5%B0%8B-H-dc4a006f", "https://www.midland.com.hk/zh-hk/list/buy/%E6%90%9C%E5%B0%8B-H-5f35336d",
"https://www.midland.com.hk/zh-hk/list/buy/%E6%90%9C%E5%B0%8B-H-d592fe3", "https://www.midland.com.hk/zh-hk/list/buy/%E6%90%9C%E5%B0%8B-H-25287f6d",
"https://www.midland.com.hk/zh-hk/list/buy/%E6%90%9C%E5%B0%8B-H-d811f3f4", "https://www.midland.com.hk/zh-hk/list/buy/%E6%90%9C%E5%B0%8B-H-23c3ec1f",
"https://www.midland.com.hk/zh-hk/list/buy/%E6%90%9C%E5%B0%8B-H-fff8fe1b", "https://www.midland.com.hk/zh-hk/list/buy/%E6%90%9C%E5%B0%8B-H-548ddd9a",
"https://www.midland.com.hk/zh-hk/list/buy/%E6%90%9C%E5%B0%8B-H-1ae02d19", "https://www.midland.com.hk/zh-hk/list/buy/%E6%90%9C%E5%B0%8B-H-6f750c98",
"https://www.midland.com.hk/zh-hk/list/buy/%E6%90%9C%E5%B0%8B-H-a197d854"]

for link in sale_links:
  sale = get_data(link)
  print(sale)
  store_sale(sale)


lease_links = ["https://www.midland.com.hk/zh-hk/list/rent", "https://www.midland.com.hk/zh-hk/list/rent/%E6%90%9C%E5%B0%8B-H-d2994d0",
"https://www.midland.com.hk/zh-hk/list/rent/%E6%90%9C%E5%B0%8B-H-b60a7652", "https://www.midland.com.hk/zh-hk/list/rent/%E6%90%9C%E5%B0%8B-H-101cd7d4",
"https://www.midland.com.hk/zh-hk/list/rent/%E6%90%9C%E5%B0%8B-H-2a40a652", "https://www.midland.com.hk/zh-hk/list/rent/%E6%90%9C%E5%B0%8B-H-3b47a071",
"https://www.midland.com.hk/zh-hk/list/rent/%E6%90%9C%E5%B0%8B-H-c494d552", "https://www.midland.com.hk/zh-hk/list/rent/%E6%90%9C%E5%B0%8B-H-d49bf7dc",
"https://www.midland.com.hk/zh-hk/list/rent/%E6%90%9C%E5%B0%8B-H-fea18952", "https://www.midland.com.hk/zh-hk/list/rent/%E6%90%9C%E5%B0%8B-H-af7bca2b",
"https://www.midland.com.hk/zh-hk/list/rent/%E6%90%9C%E5%B0%8B-H-57cebad9", "https://www.midland.com.hk/zh-hk/list/rent/%E6%90%9C%E5%B0%8B-H-90e05084",
"https://www.midland.com.hk/zh-hk/list/rent/%E6%90%9C%E5%B0%8B-H-3c4b7105", "https://www.midland.com.hk/zh-hk/list/rent/%E6%90%9C%E5%B0%8B-H-75f92186",
"https://www.midland.com.hk/zh-hk/list/rent/%E6%90%9C%E5%B0%8B-H-21644207", "https://www.midland.com.hk/zh-hk/list/rent/%E6%90%9C%E5%B0%8B-H-5af2b2b"]             
               
for link in lease_links:
  sale = get_data(link)
  print(sale)
  store_sale(sale)

driver.quit()

df_sale.loc[len(df_sale)] = new_data_sale
df_lease.loc[len(df_lease)] = new_data_lease
df_sale['日期'] = pd.to_datetime(df_sale['日期'])
df_sale['日期'] = df_sale['日期'].dt.strftime('%Y-%m-%d')
df_lease['日期'] = pd.to_datetime(df_lease['日期'])
df_lease['日期'] = df_lease['日期'].dt.strftime('%Y-%m-%d')
print(df_sale)

with pd.ExcelWriter("美聯放盤.xlsx") as writer:
  df_sale.to_excel(writer, sheet_name="賣盤", index=False)
  df_lease.to_excel(writer, sheet_name="租盤", index=False)

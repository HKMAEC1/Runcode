# -*- coding: utf-8 -*-
"""
Created on Tue May 14 23:16:00 2024

@author: kayt
"""

#%% Import neccessary packages
#import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from datetime import datetime, date, timedelta
import pandas as pd
import schedule
import time

#%% Set webdriver
chrome_options = webdriver.chrome.options.Options()

prefs = {
'download.extensions_to_open': 'xml',
'safebrowsing.enabled': True
}
## Uncomment the below to let the program to run in background
options = webdriver.ChromeOptions()
options.add_experimental_option('prefs',prefs)
options.add_argument("start-maximized")
#options.add_argument("--headless")  
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument("--safebrowsing-disable-download-protection")
options.add_argument("safebrowsing-disable-extension-blacklist")


#%% Web scraping
driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
driver.get('https://oir.centanet.com/lease/retail/')

Data = []

#Total
data = driver.find_element('xpath', '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div/div[1]/h1/span').text
print(data)
Data.append(data)

#HK Island
driver.find_element('xpath', '//*[@id="mapIcon"]').click()
time.sleep(1)
driver.find_element('xpath', '//*[contains(@id, "el-popover")]/div[1]/div[2]/label/span[1]').click()
time.sleep(1)
driver.find_element('xpath', '//*[@id="__layout"]/div/div[1]/div[1]/div[1]/div[2]').click()
time.sleep(3)
data = driver.find_element('xpath', '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/h1/span').text
print(data)
Data.append(data)

#Sheung Wan
driver.find_element('xpath', '//*[@id="mapIcon"]').click()
time.sleep(1)
driver.find_element('xpath', '//*[contains(@id, "el-popover")]/div[1]/div[2]/label/span[1]').click()
time.sleep(1)
driver.find_element('xpath', '//*[contains(@id, "el-popover")]/div[1]/div[2]/div/label[1]/span[1]').click()
time.sleep(1)
driver.find_element('xpath', '//*[contains(@id, "layout")]/div/div[1]/div[1]/div[1]/div[2]').click()
time.sleep(3)
data = driver.find_element('xpath', '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/h1/span').text
print(data)
Data.append(data)

#Other HK Island districts
for x in range(1,17):
    i = x
    j = x + 1
    driver.find_element('xpath', '//*[@id="mapIcon"]').click()
    time.sleep(1)
    driver.find_element('xpath', '//*[contains(@id, "el-popover")]/div[1]/div[2]/div/label[' + str(i) + ']/span[1]').click()
    time.sleep(2)
    driver.find_element('xpath', '//*[contains(@id, "el-popover")]/div[1]/div[2]/div/label[' + str(j) + ']/span[1]').click()
    time.sleep(2)
    driver.find_element('xpath', '//*[@id="__layout"]/div/div[1]/div[1]/div[1]/div[2]').click()
    time.sleep(3)
    try:
        data = driver.find_element('xpath', '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/h1/span').text
        print(data)
        Data.append(data)
    except:
        data = 0
        print(data)
        Data.append(data)
        pass
        
    
#Kowloon 
driver.find_element('xpath', '//*[@id="mapIcon"]').click()
time.sleep(1)
driver.find_element('xpath', '//*[contains(@id, "el-popover")]/div[1]/div[2]/div/label[17]/span[1]').click()
time.sleep(2)
driver.find_element('xpath', '//*[@id="tab-KL"]/h2/span').click()
time.sleep(1)
driver.find_element('xpath', '//*[contains(@id, "el-popover")]/div[1]/div[2]/label/span[1]').click()
time.sleep(1)
driver.find_element('xpath', '//*[@id="__layout"]/div/div[1]/div[1]/div[1]/div[2]').click()
time.sleep(3)
data = driver.find_element('xpath', '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/h1/span').text
print(data)
Data.append(data)

#Kowloon City
driver.find_element('xpath', '//*[@id="mapIcon"]').click()
time.sleep(1)
driver.find_element('xpath', '//*[contains(@id, "el-popover")]/div[1]/div[2]/label/span[1]').click()
time.sleep(1)
driver.find_element('xpath', '//*[contains(@id, "el-popover")]/div[1]/div[2]/div/label[1]/span[1]').click()
time.sleep(1)
driver.find_element('xpath', '//*[contains(@id, "layout")]/div/div[1]/div[1]/div[1]/div[2]').click()
time.sleep(3)
data = driver.find_element('xpath', '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/h1/span').text
print(data)
Data.append(data)

#Other Kowloon districts
for x in range(1,18):
    i = x
    j = x + 1
    driver.find_element('xpath', '//*[@id="mapIcon"]').click()
    time.sleep(1)
    driver.find_element('xpath', '//*[contains(@id, "el-popover")]/div[1]/div[2]/div/label[' + str(i) + ']/span[1]').click()
    time.sleep(2)
    driver.find_element('xpath', '//*[contains(@id, "el-popover")]/div[1]/div[2]/div/label[' + str(j) + ']/span[1]').click()
    time.sleep(2)
    driver.find_element('xpath', '//*[@id="__layout"]/div/div[1]/div[1]/div[1]/div[2]').click()
    time.sleep(3)
    try:
        data = driver.find_element('xpath', '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/h1/span').text
        print(data)
        Data.append(data)
    except:
        data = 0
        print(data)
        Data.append(data)
        pass


#NT 
driver.find_element('xpath', '//*[@id="mapIcon"]').click()
time.sleep(1)
driver.find_element('xpath', '//*[contains(@id, "el-popover")]/div[1]/div[2]/div/label[18]/span[1]').click()
time.sleep(2)
driver.find_element('xpath', '//*[@id="tab-NT"]/h2/span').click()
time.sleep(1)
driver.find_element('xpath', '//*[contains(@id, "el-popover")]/div[1]/div[2]/label/span[1]').click()
time.sleep(1)
driver.find_element('xpath', '//*[@id="__layout"]/div/div[1]/div[1]/div[1]/div[2]').click()
time.sleep(3)
data = driver.find_element('xpath', '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/h1/span').text
print(data)
Data.append(data)

#Tai Po
driver.find_element('xpath', '//*[@id="mapIcon"]').click()
time.sleep(1)
driver.find_element('xpath', '//*[contains(@id, "el-popover")]/div[1]/div[2]/label/span[1]').click()
time.sleep(1)
driver.find_element('xpath', '//*[contains(@id, "el-popover")]/div[1]/div[2]/div/label[1]/span[1]').click()
time.sleep(1)
driver.find_element('xpath', '//*[contains(@id, "layout")]/div/div[1]/div[1]/div[1]/div[2]').click()
time.sleep(3)
data = driver.find_element('xpath', '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/h1/span').text
print(data)
Data.append(data)

#Other NT districts
for x in range(1,16):
    i = x
    j = x + 1
    driver.find_element('xpath', '//*[@id="mapIcon"]').click()
    time.sleep(1)
    driver.find_element('xpath', '//*[contains(@id, "el-popover")]/div[1]/div[2]/div/label[' + str(i) + ']/span[1]').click()
    time.sleep(2)
    driver.find_element('xpath', '//*[contains(@id, "el-popover")]/div[1]/div[2]/div/label[' + str(j) + ']/span[1]').click()
    time.sleep(2)
    driver.find_element('xpath', '//*[@id="__layout"]/div/div[1]/div[1]/div[1]/div[2]').click()
    time.sleep(3)
    try:
        data = driver.find_element('xpath', '//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/h1/span').text
        print(data)
        Data.append(data)
    except:
        data = 0
        print(data)
        Data.append(data)
        pass

driver.quit()


#%%
Date = []
d = date.today()
print(d)
Date.append(d)

Total = Data[::55]
HK = Data[1::55]
SW = Data[2::55]
SSW = Data[3::55]
Central = Data[4::55]
NP = Data[5::55]
TH = Data[6::55]
Western = Data[7::55]
SWH = Data[8::55]
Admiralty = Data[9::55]
Southern = Data[10::55]
ABD = Data[11::55]
CW = Data[12::55]
SKW = Data[13::55]
CWB = Data[14::55]
HV = Data[15::55]
WC = Data[16::55]
QB = Data[17::55]
TKS = Data[18::55]
KL = Data[19::55]
KLC = Data[20::55]
KLT = Data[21::55]
KLB = Data[22::55]
TKW = Data[23::55]
TKT = Data[24::55]
PE = Data[25::55]
TST = Data[26::55]
JD = Data[27::55]
MK = Data[28::55]
HMT = Data[29::55]
YMT = Data[30::55]
CSW = Data[31::55]
HH = Data[32::55]
MF = Data[33::55]
SSP = Data[34::55]
WTS = Data[35::55]
SPK = Data[36::55]
KT = Data[37::55]
NT = Data[38::55]
TP = Data[39::55]
YL = Data[40::55]
TSW = Data[41::55]
TM = Data[42::55]
SS = Data[43::55]
FL = Data[44::55]
SK = Data[45::55]
ST = Data[46::55]
TaiWai = Data[47::55]
MOS = Data[48::55]
TY = Data[49::55]
LK = Data[50::55]
TsuenWan = Data[51::55]
TKO = Data[52::55]
KC = Data[53::55]
Islands = Data[54::55]


#%%
df = pd.DataFrame()
df["日期"] = Date
df["商鋪租盤"] = Total
df["港島"] = HK
df["九龍"] = KL
df["新界"] = NT

df["上環"] = SW
df["小西灣"] = SSW
df["中環"] = Central
df["北角"] = NP
df["天后"] = TH
df["西區"] = Western
df["西灣河"] = SWH
df["金鐘"] = Admiralty
df["南區"] = Southern
df["香港仔"] = ABD
df["柴灣"] = CW
df["筲箕灣"] = SKW
df["銅鑼灣"] = CWB
df["跑馬地"] = HV
df["灣仔"] = WC
df["鰂魚涌"] = QB
df["太古城"] = TKS

df["九龍城"] = KLC
df["九龍塘"] = KLT
df["九龍灣"] = KLB
df["土瓜灣"] = TKW
df["大角咀"] = TKT
df["太子"] = PE
df["尖沙咀"] = TST
df["佐敦"] = JD
df["旺角"] = MK
df["何文田"] = HMT
df["油麻地"] = YMT
df["長沙灣"] = CSW
df["紅磡"] = HH
df["美孚"] = MF
df["深水埗"] = SSP
df["黃大仙"] = WTS
df["新蒲崗"] = SPK
df["觀塘"] = KT

df["大埔"] = TP
df["元朗"] = YL
df["天水圍"] = TSW
df["屯門"] = TM
df["上水"] = SS
df["粉嶺"] = FL
df["西貢"] = SK
df["沙田"] = ST
df["大圍"] = TaiWai
df["馬鞍山"] = MOS
df["青衣"] = TY
df["荔景"] = LK
df["荃灣"] = TsuenWan
df["將軍澳"] = TKO
df["葵涌"] = KC
df["離島"] = Islands

df.to_excel("Centaline_retail.xlsx",sheet_name="sheet1", index=False)



import requests
from bs4 import BeautifulSoup
from datetime import date, datetime, timedelta
import time
import pandas as pd

def scrape_data():

    max_retries = 5
    
    #Retail lease
    url = 'https://oir.centanet.com/lease/retail/'
    retail_lease = retry_scrape(url, max_retries, 'h1', 'list_res_num')

    #CEN
    url004 = 'https://oir.centanet.com/en/lease/search/?districts=WS004&usages=Retail'
    CEN = retry_scrape(url004, max_retries, 'h1', 'list_res_num')

    #WES
    url001 = 'https://oir.centanet.com/en/lease/search/?districts=WS001&usages=Retail'
    WES = retry_scrape(url001, max_retries, 'h1', 'list_res_num')

    #SHW
    url003 = 'https://oir.centanet.com/en/lease/search/?districts=WS003&usages=Retail'
    SHW = retry_scrape(url003, max_retries, 'h1', 'list_res_num')

    #WAC
    url006 = 'https://oir.centanet.com/en/lease/search/?districts=WS006&usages=Retail'
    WAC = retry_scrape(url006, max_retries, 'h1', 'list_res_num')

    #CHW
    url012 = 'https://oir.centanet.com/en/lease/search/?districts=WS012&usages=Retail'
    CHW = retry_scrape(url012, max_retries, 'h1', 'list_res_num')

    #TIH
    url046 = 'https://oir.centanet.com/en/lease/search/?districts=WS046&usages=Retail'
    TIH = retry_scrape(url046, max_retries, 'h1', 'list_res_num')


    #HAV
    url048 = 'https://oir.centanet.com/en/lease/search/?districts=WS048&usages=Retail'
    HAV = retry_scrape(url046, max_retries, 'h1', 'list_res_num')

    #TAS
    url049 = 'https://oir.centanet.com/en/lease/search/?districts=WS049&usages=Retail'
    TAS = retry_scrape(url049, max_retries, 'h1', 'list_res_num')

    #NOP
    url008 = 'https://oir.centanet.com/en/lease/search/?districts=WS008&usages=Retail'
    NOP = retry_scrape(url008, max_retries, 'h1', 'list_res_num')

    #SKW
    url011 = 'https://oir.centanet.com/en/lease/search/?districts=WS011&usages=Retail'
    SKW = retry_scrape(url011, max_retries, 'h1', 'list_res_num')

    #QUB
    url009 = 'https://oir.centanet.com/en/lease/search/?districts=WS009&usages=Retail'
    QUB = = retry_scrape(url009, max_retries, 'h1', 'list_res_num')

    #CAB
    url007 = 'https://oir.centanet.com/en/lease/search/?districts=WS007&usages=Retail'
    CAB = retry_scrape(url007, max_retries, 'h1', 'list_res_num')

    #SOU
    url002 = 'https://oir.centanet.com/en/lease/search/?districts=WS002&usages=Retail'
    SOU = retry_scrape(url002, max_retries, 'h1', 'list_res_num')


    #ADM
    url005 = 'https://oir.centanet.com/en/lease/search/?districts=WS005&usages=Retail'
    ADM = retry_scrape(url005, max_retries, 'h1', 'list_res_num')


    #SSW
    url013 = 'https://oir.centanet.com/en/lease/search/?districts=WS013&usages=Retail'
    SSW = retry_scrape(url013, max_retries, 'h1', 'list_res_num')

    #SWH
    url010 = 'https://oir.centanet.com/en/lease/search/?districts=WS010&usages=Retail'
    SWH = retry_scrape(url010, max_retries, 'h1', 'list_res_num')

    #ABE
    url047 = 'https://oir.centanet.com/en/lease/search/?districts=WS047&usages=Retail'
    ABE = retry_scrape(url047, max_retries, 'h1', 'list_res_num')

    #MOK
    url020 = 'https://oir.centanet.com/en/lease/search/?districts=WS020&usages=Retail'
    MOK = retry_scrape(url020, max_retries, 'h1', 'list_res_num')

    #TST
    url023 = 'https://oir.centanet.com/en/lease/search/?districts=WS023&usages=Retail'
    TST = retry_scrape(url023, max_retries, 'h1', 'list_res_num')

    #JOR
    url022 = 'https://oir.centanet.com/en/lease/search/?districts=WS022&usages=Retail'
    JOR = retry_scrape(url022, max_retries, 'h1', 'list_res_num')

    #YMT
    url021 = 'https://oir.centanet.com/en/lease/search/?districts=WS021&usages=Retail'
    YMT = retry_scrape(url021, max_retries, 'h1', 'list_res_num')

    #TKT
    url018 = 'https://oir.centanet.com/en/lease/search/?districts=WS018&usages=Retail'
    TKT = retry_scrape(url018, max_retries, 'h1', 'list_res_num')

    #SSP
    url016 = 'https://oir.centanet.com/en/lease/search/?districts=WS016&usages=Retail'
    SSP = retry_scrape(url016, max_retries, 'h1', 'list_res_num')

    #CSW
    url015 = 'https://oir.centanet.com/en/lease/search/?districts=WS015&usages=Retail'
    CSW = retry_scrape(url015, max_retries, 'h1', 'list_res_num')

    #MEF
    url014 = 'https://oir.centanet.com/en/lease/search/?districts=WS014&usages=Retail'
    MEF = retry_scrape(url014, max_retries, 'h1', 'list_res_num')

    #KOC
    url025 = 'https://oir.centanet.com/en/lease/search/?districts=WS025&usages=Retail'
    KOC = retry_scrape(url025, max_retries, 'h1', 'list_res_num')

    #TKW
    url026 = 'https://oir.centanet.com/en/lease/search/?districts=WS026&usages=Retail'
    TKW = retry_scrape(url026, max_retries, 'h1', 'list_res_num')

    #HUH
    url027 = 'https://oir.centanet.com/en/lease/search/?districts=WS027&usages=Retail'
    HUH = retry_scrape(url027, max_retries, 'h1', 'list_res_num')

    #SPK
    url030 = 'https://oir.centanet.com/en/lease/search/?districts=WS030&usages=Retail'
    SPK = retry_scrape(url030, max_retries, 'h1', 'list_res_num')

    #WTS
    url029 = 'https://oir.centanet.com/en/lease/search/?districts=WS029&usages=Retail'
    WTS = retry_scrape(url029, max_retries, 'h1', 'list_res_num')

    #KWT
    url032 = 'https://oir.centanet.com/en/lease/search/?districts=WS032&usages=Retail'
    KWT = retry_scrape(url032, max_retries, 'h1', 'list_res_num')

    #KOB
    url031 = 'https://oir.centanet.com/en/lease/search/?districts=WS031&usages=Retail'
    KOB = retry_scrape(url031, max_retries, 'h1', 'list_res_num')

    #YMT
    url021 = 'https://oir.centanet.com/en/lease/search/?districts=WS021&usages=Retail'
    YMT = retry_scrape(url021, max_retries, 'h1', 'list_res_num')

    #PRI
    url019 = 'https://oir.centanet.com/en/lease/search/?districts=WS019&usages=Retail'
    PRI = retry_scrape(url019, max_retries, 'h1', 'list_res_num')

    #HMT
    url045 = 'https://oir.centanet.com/en/lease/search/?districts=WS045&usages=Retail'
    HMT = retry_scrape(url045, max_retries, 'h1', 'list_res_num')

    #KWC
    url042 = 'https://oir.centanet.com/en/lease/search/?districts=WS042&usages=Retail'
    KWC = retry_scrape(url042, max_retries, 'h1', 'list_res_num')

    #TSY
    url041 = 'https://oir.centanet.com/en/lease/search/?districts=WS041&usages=Retail'
    TSY = retry_scrape(url041, max_retries, 'h1', 'list_res_num')

    #TSW
    url040 = 'https://oir.centanet.com/en/lease/search/?districts=WS040&usages=Retail'
    TSW = retry_scrape(url040, max_retries, 'h1', 'list_res_num')

    #TUM
    url039 = 'https://oir.centanet.com/en/lease/search/?districts=WS039&usages=Retail'
    TUM = retry_scrape(url039, max_retries, 'h1', 'list_res_num')

    #YUL
    url038 = 'https://oir.centanet.com/en/lease/search/?districts=WS038&usages=Retail'
    YUL = retry_scrape(url038, max_retries, 'h1', 'list_res_num')

    #TIS
    url050 = 'https://oir.centanet.com/en/lease/search/?districts=WS050&usages=Retail'
    TIS = retry_scrape(url050, max_retries, 'h1', 'list_res_num')

    #SHS
    url051 = 'https://oir.centanet.com/en/lease/search/?districts=WS051&usages=Retail'
    SHS = retry_scrape(url051, max_retries, 'h1', 'list_res_num')

    #FAN
    url052 = 'https://oir.centanet.com/en/lease/search/?districts=WS052&usages=Retail'
    FAN = retry_scrape(url052, max_retries, 'h1', 'list_res_num')

    #TAP
    url034 = 'https://oir.centanet.com/en/lease/search/?districts=WS034&usages=Retail'
    TAP = retry_scrape(url034, max_retries, 'h1', 'list_res_num')

    #SHT
    url035 = 'https://oir.centanet.com/en/lease/search/?districts=WS035&usages=Retail'
    SHT = retry_scrape(url035, max_retries, 'h1', 'list_res_num')

    #TAW
    url053 = 'https://oir.centanet.com/en/lease/search/?districts=WS053&usages=Retail'
    TAW = retry_scrape(url053, max_retries, 'h1', 'list_res_num')

    #MOS
    url054 = 'https://oir.centanet.com/en/lease/search/?districts=WS054&usages=Retail'
    MOS = retry_scrape(url054, max_retries, 'h1', 'list_res_num')

    #TKO
    url037 = 'https://oir.centanet.com/en/lease/search/?districts=WS037&usages=Retail'
    TKO = retry_scrape(url037, max_retries, 'h1', 'list_res_num')

    #SAK
    url036 = 'https://oir.centanet.com/en/lease/search/?districts=WS036&usages=Retail'
    SAK = retry_scrape(url036, max_retries, 'h1', 'list_res_num')

    #ISI
    url044 = 'https://oir.centanet.com/en/lease/search/?districts=WS044&usages=Retail'
    ISI = retry_scrape(url044, max_retries, 'h1', 'list_res_num')

    #LAK
    url043 = 'https://oir.centanet.com/en/lease/search/?districts=WS043&usages=Retail'
    LAK = retry_scrape(url043, max_retries, 'h1', 'list_res_num')
    
    d = date.today() + timedelta(days=1)
    
    return [d, retail_lease, CEN, WES, SHW, WAC, CAB, TIH, HAV, TAS, NOP, SKW, QUB, CHW, SOU, ADM, SSW, SWH, ABE, MOK, TST, JOR, YMT, TKT, SSP, CSW, MEF, KOC, TKW, HUH, SPK, WTS, KWT, KOB, YMT, PRI, HMT, KWC, TSY, TSW, TUM, YUL, TIS, SHS, FAN, TAP, SHT, TAW, MOS, TKO, SAK, ISI, LAK]

def retry_scrape(url, max_retries, tag, class_name):
        retries = 0
    while retries < max_retries:
        time.sleep(10)  # Add a delay to avoid overwhelming the server
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        span_element = soup.find(tag, class_=class_name)
        if span_element:
            return span_element.find('span').text.replace(',', '')
        retries += 1
    return 'NA'

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

    # Mapping of district codes to district names
    #district_mapping = {
        #'WS004': 'CEN',
        #'WS001': 'WES',
        #'WS003': 'SHW',
        #'WS002': 'SOU',
        #'WS006': 'WAC',
        #'WS007': 'CAB',
        #'WS008': 'NOP',
        #'WS009': 'QUB',
        #'WS010': 'SWH',
        #'WS011': 'SKW',
        #'WS012': 'CHW',
        #'WS013': 'SSW',
        #'WS014': 'MEF',
        #'WS015': 'CSW',
        #'WS016': 'SSP',
        #'WS018': 'TKT',
        #'WS019': 'PRI',
        #'WS020': 'MOK',
        #'WS021': 'YMT',
        #'WS022': 'JOR',
        #'WS023': 'TST',
        #'WS025': 'KWC',
        #'WS026': 'TKW',
        #'WS027': 'HUH',
        #'WS029': 'WTS',
        #'WS030': 'SPK',
        #'WS031': 'KOB',
        #'WS032': 'KWT',
        #'WS034': 'TAP',
        #'WS035': 'SHT',
        #'WS036': 'SAK',
        #'WS037': 'TKO',
        #'WS038': 'YUL',
        #'WS039': 'TUM',
        #'WS040': 'TSW',
        #'WS041': 'TSY',
        #'WS042': 'KWC',
        #'WS005': 'ADM',
        #'WS048': 'HAV',
        #'WS043': 'LAK',
        #'WS044': 'ISI',
        #'WS045': 'HMT',
        #'WS046': 'TIH',
        #'WS049': 'TAS',
        #'WS047': 'ABE',
        #'WS050': 'TIS',
        #'WS051': 'SHS',
        #'WS052': 'FAN',
        #'WS053': 'TAW',
        #'WS054': 'MOS'
    

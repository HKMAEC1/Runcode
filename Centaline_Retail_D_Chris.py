import requests
from bs4 import BeautifulSoup
import time

def scrape_data():
    #Retail lease
    url = 'https://oir.centanet.com/lease/retail/'
    time.sleep(5)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    span_element = soup.find('h1', class_='list_res_num').find('span')
    retail_lease = span_element.text.replace(',', '')

    #CEN
    url004 = 'https://oir.centanet.com/en/lease/search/?districts=WS004&usages=Retail'
    time.sleep(5)
    response = requests.get(url004)
    soup = BeautifulSoup(response.content, 'html.parser')
    span_element = soup.find('h1', class_='list_res_num').find('span')
    CEN = span_element.text.replace(',', '')

    #WES
    url001 = 'https://oir.centanet.com/en/lease/search/?districts=WS001&usages=Retail'
    time.sleep(5)
    response = requests.get(url001)
    soup = BeautifulSoup(response.content, 'html.parser')
    span_element = soup.find('h1', class_='list_res_num').find('span')
    WES = span_element.text.replace(',', '')

    #SHW
    url003 = 'https://oir.centanet.com/en/lease/search/?districts=WS003&usages=Retail'
    time.sleep(5)
    response = requests.get(url003)
    soup = BeautifulSoup(response.content, 'html.parser')
    span_element = soup.find('h1', class_='list_res_num').find('span')
    SHW = span_element.text.replace(',', '')

    #WAC
    url006 = 'https://oir.centanet.com/en/lease/search/?districts=WS006&usages=Retail'
    time.sleep(5)
    response = requests.get(url006)
    soup = BeautifulSoup(response.content, 'html.parser')
    span_element = soup.find('h1', class_='list_res_num').find('span')
    WAC = span_element.text.replace(',', '')

    #CHW
    url012 = 'https://oir.centanet.com/en/lease/search/?districts=WS012&usages=Retail'
    time.sleep(5)
    response = requests.get(url012)
    soup = BeautifulSoup(response.content, 'html.parser')
    span_element = soup.find('h1', class_='list_res_num').find('span')
    CHW = span_element.text.replace(',', '')

    #TIH
    url046 = 'https://oir.centanet.com/en/lease/search/?districts=WS046&usages=Retail'
    time.sleep(5)
    response = requests.get(url046)
    soup = BeautifulSoup(response.content, 'html.parser')
    span_element = soup.find('h1', class_='list_res_num').find('span')
    TIH = span_element.text.replace(',', '')


    #HAV
    url048 = 'https://oir.centanet.com/en/lease/search/?districts=WS048&usages=Retail'
    time.sleep(5)
    response = requests.get(url048)
    soup = BeautifulSoup(response.content, 'html.parser')
    span_element = soup.find('h1', class_='list_res_num').find('span')
    HAV = span_element.text.replace(',', '')


    #TAS
    url049 = 'https://oir.centanet.com/en/lease/search/?districts=WS049&usages=Retail'
    time.sleep(5)
    response = requests.get(url049)
    soup = BeautifulSoup(response.content, 'html.parser')
    span_element = soup.find('h1', class_='list_res_num').find('span')
    TAS = span_element.text.replace(',', '')


    #NOP
    url008 = 'https://oir.centanet.com/en/lease/search/?districts=WS008&usages=Retail'
    time.sleep(5)
    response = requests.get(url008)
    soup = BeautifulSoup(response.content, 'html.parser')
    span_element = soup.find('h1', class_='list_res_num').find('span')
    NOP = span_element.text.replace(',', '')

    #SKW
    url011 = 'https://oir.centanet.com/en/lease/search/?districts=WS011&usages=Retail'
    time.sleep(5)
    response = requests.get(url011)
    soup = BeautifulSoup(response.content, 'html.parser')
    span_element = soup.find('h1', class_='list_res_num').find('span')
    SKW = span_element.text.replace(',', '')

    #QUB
    url009 = 'https://oir.centanet.com/en/lease/search/?districts=WS009&usages=Retail'
    time.sleep(5)
    response = requests.get(url009)
    soup = BeautifulSoup(response.content, 'html.parser')
    span_element = soup.find('h1', class_='list_res_num').find('span')
    QUB = span_element.text.replace(',', '')

    #CAB
    url007 = 'https://oir.centanet.com/en/lease/search/?districts=WS007&usages=Retail'
    time.sleep(5)
    response = requests.get(url007)
    soup = BeautifulSoup(response.content, 'html.parser')
    span_element = soup.find('h1', class_='list_res_num').find('span')
    CAB = span_element.text.replace(',', '')

    #SOU
    url002 = 'https://oir.centanet.com/en/lease/search/?districts=WS002&usages=Retail'
    time.sleep(5)
    response = requests.get(url002)
    soup = BeautifulSoup(response.content, 'html.parser')
    span_element = soup.find('h1', class_='list_res_num').find('span')
    SOU = span_element.text.replace(',', '')


    #ADM
    url005 = 'https://oir.centanet.com/en/lease/search/?districts=WS005&usages=Retail'
    time.sleep(5)
    response = requests.get(url005)
    soup = BeautifulSoup(response.content, 'html.parser')
    span_element = soup.find('h1', class_='list_res_num').find('span')
    ADM = span_element.text.replace(',', '')


    #SSW
    url013 = 'https://oir.centanet.com/en/lease/search/?districts=WS013&usages=Retail'
    time.sleep(5)
    response = requests.get(url013)
    soup = BeautifulSoup(response.content, 'html.parser')
    span_element = soup.find('h1', class_='list_res_num').find('span')
    SSW = span_element.text.replace(',', '')

    #SWH
    url010 = 'https://oir.centanet.com/en/lease/search/?districts=WS010&usages=Retail'
    time.sleep(5)
    response = requests.get(url010)
    soup = BeautifulSoup(response.content, 'html.parser')
    span_element = soup.find('h1', class_='list_res_num').find('span')
    SWH = span_element.text.replace(',', '')

    #ABE
    url047 = 'https://oir.centanet.com/en/lease/search/?districts=WS047&usages=Retail'
    time.sleep(5)
    response = requests.get(url047)
    soup = BeautifulSoup(response.content, 'html.parser')
    span_element = soup.find('h1', class_='list_res_num').find('span')
    ABE = span_element.text.replace(',', '')

    #MOK
    url020 = 'https://oir.centanet.com/en/lease/search/?districts=WS020&usages=Retail'
    time.sleep(5)
    response = requests.get(url020)
    soup = BeautifulSoup(response.content, 'html.parser')
    span_element = soup.find('h1', class_='list_res_num').find('span')
    MOK = span_element.text.replace(',', '')

    #TST
    url023 = 'https://oir.centanet.com/en/lease/search/?districts=WS023&usages=Retail'
    time.sleep(5)
    response = requests.get(url023)
    soup = BeautifulSoup(response.content, 'html.parser')
    span_element = soup.find('h1', class_='list_res_num').find('span')
    TST = span_element.text.replace(',', '')

    #JOR
    url022 = 'https://oir.centanet.com/en/lease/search/?districts=WS022&usages=Retail'
    time.sleep(5)
    response = requests.get(url022)
    soup = BeautifulSoup(response.content, 'html.parser')
    span_element = soup.find('h1', class_='list_res_num').find('span')
    JOR = span_element.text.replace(',', '')

    #YMT
    url021 = 'https://oir.centanet.com/en/lease/search/?districts=WS021&usages=Retail'
    time.sleep(5)
    response = requests.get(url021)
    soup = BeautifulSoup(response.content, 'html.parser')
    span_element = soup.find('h1', class_='list_res_num').find('span')
    YMT = span_element.text.replace(',', '')

    #TKT
    url018 = 'https://oir.centanet.com/en/lease/search/?districts=WS018&usages=Retail'
    time.sleep(5)
    response = requests.get(url018)
    soup = BeautifulSoup(response.content, 'html.parser')
    span_element = soup.find('h1', class_='list_res_num').find('span')
    TKT = span_element.text.replace(',', '')

    #SSP
    url016 = 'https://oir.centanet.com/en/lease/search/?districts=WS016&usages=Retail'
    time.sleep(5)
    response = requests.get(url016)
    soup = BeautifulSoup(response.content, 'html.parser')
    span_element = soup.find('h1', class_='list_res_num').find('span')
    SSP = span_element.text.replace(',', '')

    #CSW
    url015 = 'https://oir.centanet.com/en/lease/search/?districts=WS015&usages=Retail'
    time.sleep(5)
    response = requests.get(url015)
    soup = BeautifulSoup(response.content, 'html.parser')
    span_element = soup.find('h1', class_='list_res_num').find('span')
    CSW = span_element.text.replace(',', '')

    #MEF
    url014 = 'https://oir.centanet.com/en/lease/search/?districts=WS014&usages=Retail'
    time.sleep(5)
    response = requests.get(url014)
    soup = BeautifulSoup(response.content, 'html.parser')
    span_element = soup.find('h1', class_='list_res_num').find('span')
    MEF = span_element.text.replace(',', '')

    #KWC
    url025 = 'https://oir.centanet.com/en/lease/search/?districts=WS025&usages=Retail'
    time.sleep(5)
    response = requests.get(url025)
    soup = BeautifulSoup(response.content, 'html.parser')
    span_element = soup.find('h1', class_='list_res_num').find('span')
    KWC = span_element.text.replace(',', '')

    #TKW
    url026 = 'https://oir.centanet.com/en/lease/search/?districts=WS026&usages=Retail'
    time.sleep(5)
    response = requests.get(url026)
    soup = BeautifulSoup(response.content, 'html.parser')
    span_element = soup.find('h1', class_='list_res_num').find('span')
    TKW = span_element.text.replace(',', '')

    #HUH
    url027 = 'https://oir.centanet.com/en/lease/search/?districts=WS027&usages=Retail'
    time.sleep(5)
    response = requests.get(url027)
    soup = BeautifulSoup(response.content, 'html.parser')
    span_element = soup.find('h1', class_='list_res_num').find('span')
    HUH = span_element.text.replace(',', '')

    #SPK
    url030 = 'https://oir.centanet.com/en/lease/search/?districts=WS030&usages=Retail'
    time.sleep(5)
    response = requests.get(url030)
    soup = BeautifulSoup(response.content, 'html.parser')
    span_element = soup.find('h1', class_='list_res_num').find('span')
    SPK = span_element.text.replace(',', '')

    #WTS
    url029 = 'https://oir.centanet.com/en/lease/search/?districts=WS029&usages=Retail'
    time.sleep(5)
    response = requests.get(url029)
    soup = BeautifulSoup(response.content, 'html.parser')
    span_element = soup.find('h1', class_='list_res_num').find('span')
    WTS = span_element.text.replace(',', '')

    #KWT
    url024 = 'https://oir.centanet.com/en/lease/search/?districts=WS024&usages=Retail'
    time.sleep(5)
    response = requests.get(url024)
    soup = BeautifulSoup(response.content, 'html.parser')
    span_element = soup.find('h1', class_='list_res_num').find('span')
    KWT = span_element.text.replace(',', '')

    #KOB
    url031 = 'https://oir.centanet.com/en/lease/search/?districts=WS031&usages=Retail'
    time.sleep(5)
    response = requests.get(url031)
    soup = BeautifulSoup(response.content, 'html.parser')
    span_element = soup.find('h1', class_='list_res_num').find('span')
    KOB = span_element.text.replace(',', '')

    #YMT
    url021 = 'https://oir.centanet.com/en/lease/search/?districts=WS021&usages=Retail'
    time.sleep(5)
    response = requests.get(url021)
    soup = BeautifulSoup(response.content, 'html.parser')
    span_element = soup.find('h1', class_='list_res_num').find('span')
    YMT = span_element.text.replace(',', '')

    #PRI
    url019 = 'https://oir.centanet.com/en/lease/search/?districts=WS019&usages=Retail'
    time.sleep(5)
    response = requests.get(url019)
    soup = BeautifulSoup(response.content, 'html.parser')
    span_element = soup.find('h1', class_='list_res_num').find('span')
    PRI = span_element.text.replace(',', '')

    #HMT
    url045 = 'https://oir.centanet.com/en/lease/search/?districts=WS045&usages=Retail'
    time.sleep(5)
    response = requests.get(url045)
    soup = BeautifulSoup(response.content, 'html.parser')
    span_element = soup.find('h1', class_='list_res_num').find('span')
    HMT = span_element.text.replace(',', '')

    #KWC
    url042 = 'https://oir.centanet.com/en/lease/search/?districts=WS042&usages=Retail'
    time.sleep(5)
    response = requests.get(url042)
    soup = BeautifulSoup(response.content, 'html.parser')
    span_element = soup.find('h1', class_='list_res_num').find('span')
    KWC = span_element.text.replace(',', '')

    #TSY
    url041 = 'https://oir.centanet.com/en/lease/search/?districts=WS041&usages=Retail'
    time.sleep(5)
    response = requests.get(url041)
    soup = BeautifulSoup(response.content, 'html.parser')
    span_element = soup.find('h1', class_='list_res_num').find('span')
    TSY = span_element.text.replace(',', '')

    #TSW
    url040 = 'https://oir.centanet.com/en/lease/search/?districts=WS040&usages=Retail'
    time.sleep(5)
    response = requests.get(url040)
    soup = BeautifulSoup(response.content, 'html.parser')
    span_element = soup.find('h1', class_='list_res_num').find('span')
    TSW = span_element.text.replace(',', '')

    #TUM
    url039 = 'https://oir.centanet.com/en/lease/search/?districts=WS039&usages=Retail'
    time.sleep(5)
    response = requests.get(url039)
    soup = BeautifulSoup(response.content, 'html.parser')
    span_element = soup.find('h1', class_='list_res_num').find('span')
    TUM = span_element.text.replace(',', '')

    #YUL
    url038 = 'https://oir.centanet.com/en/lease/search/?districts=WS038&usages=Retail'
    time.sleep(5)
    response = requests.get(url038)
    soup = BeautifulSoup(response.content, 'html.parser')
    span_element = soup.find('h1', class_='list_res_num').find('span')
    YUL = span_element.text.replace(',', '')

    #TIS
    url050 = 'https://oir.centanet.com/en/lease/search/?districts=WS050&usages=Retail'
    time.sleep(5)
    response = requests.get(url050)
    soup = BeautifulSoup(response.content, 'html.parser')
    span_element = soup.find('h1', class_='list_res_num').find('span')
    TIS = span_element.text.replace(',', '')

    #SHS
    url051 = 'https://oir.centanet.com/en/lease/search/?districts=WS051&usages=Retail'
    time.sleep(5)
    response = requests.get(url051)
    soup = BeautifulSoup(response.content, 'html.parser')
    span_element = soup.find('h1', class_='list_res_num').find('span')
    SHS = span_element.text.replace(',', '')

    #FAN
    url052 = 'https://oir.centanet.com/en/lease/search/?districts=WS052&usages=Retail'
    time.sleep(5)
    response = requests.get(url052)
    soup = BeautifulSoup(response.content, 'html.parser')
    span_element = soup.find('h1', class_='list_res_num').find('span')
    FAN = span_element.text.replace(',', '')

    #TAP
    url034 = 'https://oir.centanet.com/en/lease/search/?districts=WS034&usages=Retail'
    time.sleep(5)
    response = requests.get(url034)
    soup = BeautifulSoup(response.content, 'html.parser')
    span_element = soup.find('h1', class_='list_res_num').find('span')
    TAP = span_element.text.replace(',', '')

    #SHT
    url035 = 'https://oir.centanet.com/en/lease/search/?districts=WS035&usages=Retail'
    time.sleep(5)
    response = requests.get(url035)
    soup = BeautifulSoup(response.content, 'html.parser')
    span_element = soup.find('h1', class_='list_res_num').find('span')
    SHT = span_element.text.replace(',', '')

    #TAW
    url053 = 'https://oir.centanet.com/en/lease/search/?districts=WS053&usages=Retail'
    time.sleep(5)
    response = requests.get(url053)
    soup = BeautifulSoup(response.content, 'html.parser')
    span_element = soup.find('h1', class_='list_res_num').find('span')
    TAW = span_element.text.replace(',', '')

    #MOS
    url054 = 'https://oir.centanet.com/en/lease/search/?districts=WS054&usages=Retail'
    time.sleep(5)
    response = requests.get(url054)
    soup = BeautifulSoup(response.content, 'html.parser')
    span_element = soup.find('h1', class_='list_res_num').find('span')
    MOS = span_element.text.replace(',', '')

    #TKO
    url037 = 'https://oir.centanet.com/en/lease/search/?districts=WS037&usages=Retail'
    time.sleep(5)
    response = requests.get(url037)
    soup = BeautifulSoup(response.content, 'html.parser')
    span_element = soup.find('h1', class_='list_res_num').find('span')
    TKO = span_element.text.replace(',', '')

    #SAK
    url036 = 'https://oir.centanet.com/en/lease/search/?districts=WS036&usages=Retail'
    time.sleep(5)
    response = requests.get(url036)
    soup = BeautifulSoup(response.content, 'html.parser')
    span_element = soup.find('h1', class_='list_res_num').find('span')
    SAK = span_element.text.replace(',', '')

    #ISI
    url044 = 'https://oir.centanet.com/en/lease/search/?districts=WS044&usages=Retail'
    time.sleep(5)
    response = requests.get(url044)
    soup = BeautifulSoup(response.content, 'html.parser')
    span_element = soup.find('h1', class_='list_res_num').find('span')
    ISI = span_element.text.replace(',', '')

    #LAK
    url043 = 'https://oir.centanet.com/en/lease/search/?districts=WS043&usages=Retail'
    time.sleep(5)
    response = requests.get(url043)
    soup = BeautifulSoup(response.content, 'html.parser')
    span_element = soup.find('h1', class_='list_res_num').find('span')
    LAK = span_element.text.replace(',', '')
    
    d = date.today() + timedelta(days=1)
    
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
        #'WS024': 'KWT',
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
    

from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
from datetime import datetime
import time
from google.colab import files
import pickle

import warnings
warnings.filterwarnings("ignore")

from datetime import date
today = date.today()
print("Today's date:", today)

hse28_master = pd.read_csv("hse28_resmaster.csv")
hse28_data = pd.DataFrame()

# Find the largest number in the "ad_id" column
largest_ad_id = hse28_master["ad_id"].max()

ad_id_start = int(largest_ad_id) + 1
ad_id_end = ad_id_start + 10000

# Take the first 20 rows from the 'ad_id' column
#ad_ids_column = hse28_master['ad_id'].iloc[:10]

#for index, ad_id in enumerate(ad_ids_column):
hse28_master['read'] = hse28_master.loc[hse28_master['latest_date_filter'] == 'Y', 'ad_id']
for index, read in enumerate(hse28_master['read']):
    if pd.notnull(read):  # Check if the value is not NaN
        print(int(read))
        try:
            url_get = "https://www.28hse.com/en/buy/residential/property-" + str(int(read))
            
            ####################################
            ## Web scraping with Beautiful Soup##
            ####################################
            source = requests.get(url_get).text
            webpage = BeautifulSoup(source, 'lxml')

            if 'Error' in webpage.find('div', class_="header").text:
                print("Property listing is not found")
                continue

            # Extract segment (Residential, Office, etc)
            segment = webpage.find('div', class_="ui small basic label").text

            # Extract created date and updated date
            propertyDate = webpage.find('div', class_="propertyDate").text.strip()

            # Reg Ex
            created_date = re.search("Created\:(.+?) \|", propertyDate).group(1)
            updated_date = re.search("Updated\:(.+)", propertyDate).group(1)

            # Convert to date variable
            created_date_d = datetime.strptime(created_date, '%Y-%m-%d').date()
            updated_date_d = datetime.strptime(updated_date, '%Y-%m-%d').date()

            # Convert to pd dataframe
            prop_ad_df1 = dict(
                ad_id=read,
                segment=segment,
                scrape_date=today,
                created_date=created_date_d,
                updated_date=updated_date_d
            )

            prop_ad_df1 = pd.DataFrame([prop_ad_df1])

            ######################################
            # Web scraping with Pandas' read_html #
            #######################################
            pd_table = pd.read_html(url_get, skiprows=1)

            prop_ad_df2 = pd_table[0].transpose()
            prop_ad_df2.columns = prop_ad_df2.iloc[0]
            prop_ad_df2 = prop_ad_df2.drop(0, axis=0).reset_index(drop=True)

            ######################################
            # Combine two tables into one df ##
            #######################################
            prop_ad_df3 = pd.concat([prop_ad_df1, prop_ad_df2], axis=1)
            hse28_data = hse28_data.append(prop_ad_df3)

            # Time pause for every 100 iterations
            if (index + 1) % 100 == 0:
                print("Pausing for 5 seconds...")
                time.sleep(5)

        except Exception as e:
            print("Error during Web Scraping:", e)
            pass

for index, ad_id in enumerate(range(ad_id_start, ad_id_end + 1)):
    print(ad_id)
    try:
        url_get = "https://www.28hse.com/en/buy/residential/property-" + str(ad_id)

        ####################################
        ## Web scrapping by Beautiful Soup##
        ####################################
        source = requests.get(url_get).text
        webpage = BeautifulSoup(source, 'lxml')

        if 'Error' in webpage.find('div', class_="header").text:
            print("Property listing is not found")
            continue

        # Extract segment (Residential, Office, etc)
        segment = webpage.find('div', class_="ui small basic label").text

        # Extract created date and updated date
        propertyDate = webpage.find('div', class_="propertyDate").text.strip()

        # Reg Ex
        created_date = re.search("Created\:(.+?) \|", propertyDate).group(1)
        updated_date = re.search("Updated\:(.+)", propertyDate).group(1)

        # Convert to date variable
        created_date_d = datetime.strptime(created_date, '%Y-%m-%d').date()
        updated_date_d = datetime.strptime(updated_date, '%Y-%m-%d').date()

        # Convert to pd dataframe
        prop_ad_df1 = dict(
            ad_id=ad_id,
            segment=segment,
            scrape_date=today,
            created_date=created_date_d,
            updated_date=updated_date_d
        )

        prop_ad_df1 = pd.DataFrame([prop_ad_df1])

        ######################################
        # Web scraping by Pandas' read_html #
        #######################################
        pd_table = pd.read_html(url_get, skiprows=1)

        prop_ad_df2 = pd_table[0].transpose()
        prop_ad_df2.columns = prop_ad_df2.iloc[0]
        prop_ad_df2 = prop_ad_df2.drop(0, axis=0).reset_index(drop=True)

        ######################################
        # Combine two tables into one df ##
        #######################################
        prop_ad_df3 = pd.concat([prop_ad_df1, prop_ad_df2], axis=1)
        hse28_data = hse28_data.append(prop_ad_df3)

        # Time pause for every 100 iterations
        if (index + 1) % 100 == 0:
            print("Pausing for 5 seconds...")
            time.sleep(5)

    except:
        print("Error during Web Scraping")
        pass
        
  # Sub set of variables
hse28_sub = hse28_data[['ad_id', 'scrape_date', 'segment', 'created_date', 'updated_date', 'Estate','Saleable Area', 'Gross Area', 'Sell Price', 'Monthly Rental']]

# Date type
hse28_sub['scrape_date']=pd.to_datetime(hse28_sub['scrape_date'])
hse28_sub['created_date']=pd.to_datetime(hse28_sub['created_date'])
hse28_sub['updated_date']=pd.to_datetime(hse28_sub['updated_date'])

# Reg Ex to extract numbers
hse28_sub['saleable_area_ft2']=hse28_sub['Saleable Area'].str.extract(r'^([^ft]+)')
hse28_sub['saleable_area_ft2'] = hse28_sub['saleable_area_ft2'].str.replace(',','')
hse28_sub['saleable_area_ft2']=pd.to_numeric(hse28_sub['saleable_area_ft2'])

hse28_sub['gross_area_ft2']=hse28_sub['Gross Area'].str.extract(r'^([^ft]+)')
hse28_sub['gross_area_ft2'] = hse28_sub['gross_area_ft2'].str.replace(',','')
hse28_sub['gross_area_ft2']=pd.to_numeric(hse28_sub['gross_area_ft2'])

#hse28_rental = hse28_sub.dropna(subset=['Monthly Rental'])
#hse28_sell = hse28_sub.dropna(subset=['Sell Price'])

try:
    hse28_sub['price_hkdm'] = hse28_sub['Sell Price'].str.extract(r'(\$.*(?= Millions))')
except:
    hse28_sub['price_hkdm'] = "error"

try:
    hse28_sub['price_hkdm'] = hse28_sub['price_hkdm'].str.replace('$', '', regex=True)
except:
    hse28_sub['price_hkdm'] = "error"

try:
    hse28_sub['price_hkdm'] = pd.to_numeric(hse28_sub['price_hkdm'], errors='coerce')
except:
    hse28_sub['price_hkdm'] = "error"

try:
    hse28_sub['rent_hkd'] = hse28_sub['Monthly Rental'].str.replace(',', '', regex=True)
except:
    hse28_sub['rent_hkd'] = "error"

try:
    hse28_sub['rent_hkd'] = hse28_sub['rent_hkd'].str.extract('(\d+)')
except:
    hse28_sub['rent_hkd'] = "error"

try:
    hse28_sub['rent_hkd'] = pd.to_numeric(hse28_sub['rent_hkd'], errors='coerce')
except:
    hse28_sub['rent_hkd'] = "error"

hse28_sub = hse28_sub.reset_index(drop=True)
#hse28_sub

# Format the date as a string in the desired format
date_string = today.strftime("%Y%m%d")  # Change the format as per your preference

# Generate the file name using the formatted date
file_name = f"hse28_{date_string}.csv"

# Save DataFrame as CSV
hse28_sub.to_csv(file_name, index=False)

# Print confirmation message
print(f"DataFrame saved as {file_name}")

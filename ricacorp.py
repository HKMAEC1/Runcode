import requests
import json
import numpy as np
import pandas as pd
import datetime
import time
import os  

os.chdir('/Users/asmalltang/Desktop')

#from PIL import Image
#from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
#import matplotlib.pyplot as plt


#Get the total no. of jobs for each search
temp = requests.get('https://property.ricacorp.com/rcAPI/rcPost?language=hk&page=1&paymentPeriod=30&mortgageInterestRate=2.5').content
total=json.loads(temp)['results']


fnews=[]  
for i in range(0,total,90):
    offset=str(i)
    url = "https://property.ricacorp.com/rcAPI/rcPost?language=hk&page=1&limit=&paymentPeriod=30&mortgageInterestRate=2.5"
    print("1")
# grab the data in json format
    while True:
        try:
             wbdata = requests.get(url,timeout=360).content
             print("2")
             data = json.loads(wbdata)
             print(data)
             news = data['results']
             for n in range(len(news)):
                 del news[n]['attachments']
                 del news[n]['publicationIds']
                 del news[n]['postTagItems']
                 del news[n]['mortgagePayment']
                 flat=flatten(news[n])
                 fnews.append(flat)
        except:
            print (i)
            print("error: try again in 210s")
            time.sleep(210)
            continue
        break

print("4")
    # decode the json format data

df = pd.DataFrame(fnews)
df.to_excel(r'C:\Users\asmalltang\Desktop\export_dataframe2.xlsx', index = False, header=True)
# Database update I/O 
print("end")


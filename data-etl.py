import pandas as pd
import numpy as np
from datetime import timedelta, datetime as dt
import os
import sys
import requests
import json
from bs4 import BeautifulSoup
from urllib import request
import time
from selenium import webdriver


# Set up Chrome options
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run in headless mode
driver = webdriver.Chrome(options=options)

# url of intended website
page_url1 = "http://www.amlc.gov.ph/images/PDFs/Main/SEC31Jan25.pdf"
page_url2 = "https://checkwithsec.sec.gov.ph/check-with-sec/suspended"

response1 = requests.get(page_url1)
response2 = requests.get(page_url2)

soup1 = BeautifulSoup(response1.content, 'html5lib')
soup2 = BeautifulSoup(response2.content, 'html5lib')

text_only1 = soup1.text
text_only2 = soup2.text

# print(text_only1)
print(text_only1)


# general data cleaning, manipulation and aggregation scripts here 
data = pd.DataFrame(text_only1) 
num = data.count().sort_index(ascending=False).tail()
pctchange = ((curr - prev) / prev) * 100

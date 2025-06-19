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


# url of intended website
page_url1 = "https://cars.mitula.ph/searchC/level1-Camarines+Sur/sort-0/q-naga-city-bicol?req_sgmt=REVTS1RPUDtTRU87U0VSUDs="
page_url2 = "https://www.fazwaz.ph/house-for-sale/philippines/bicol"

response1 = requests.get(page_url1)
response2 = requests.get(page_url2)

soup1 = BeautifulSoup(response1.content, 'html5lib')
soup2 = BeautifulSoup(response2.content, 'html5lib')

text_only1 = soup1.text
text_only2 = soup2.text

print(text_only1)
print(soup2)


# general data cleaning, manipulation and aggregation scripts here 
data = pd.DataFrame(text_only1)
num = data.count().sort_index(ascending=False).tail()
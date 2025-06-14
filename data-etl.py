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
page_url = "https://finance.yahoo.com/markets/world-indices/"


for i in range(10):
    response = requests.get(page_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
    elif response.status_code == 429:
        print(f"Received 429 error. Waiting before retrying")
        time.sleep(10)
        continue
    else:
        print(f"Error: {response.status_code}")
    
    time.sleep(5)


print(soup)


# general data cleaning, manipulation and aggregation scripts here 
# data = pd.DataFrame()
# num = data.count().sort_index(ascending=False).tail()
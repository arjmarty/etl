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
page_url = "https://finance.yahoo.com/markets/stocks/most-active/"

def get_url(page_url):
    for attempt in range(5):
        response = requests.get(page_url)

        if response.status_code == 200:
            return BeautifulSoup(response.content, 'html.parser')
        elif response == 429:
            wait_time = 2 ** attempt
            print(f"Received 429 error. Waiting for {wait_time} seconds before retrying...")
            time.sleep(wait_time)
        else:
            print(f"Error: {response.status_code}")
            break
    
    return None



#open the page
soup = get_url(page_url)

print(soup)


# general data cleaning, manipulation and aggregation scripts here 
# data = pd.DataFrame()
# num = data.count().sort_index(ascending=False).tail()
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
page_url = "https://finance.yahoo.com/quote/PSEI.PS/history/"


def make_request(page_url):
    retries = 5
    for i in range(retries):
        response = requests.get(page_url)
        if response.status_code == 429:
            wait_time = 2 ** i  # Exponential backoff
            print(f"Received 429, waiting for {wait_time} seconds...")
            time.sleep(wait_time)
        else:
            return response
    return None

# soup = BeautifulSoup(response.content, 'html5lib')

response = make_request()

print(response)


# general data cleaning, manipulation and aggregation scripts here 
# data = pd.DataFrame()
# num = data.count().sort_index(ascending=False).tail()
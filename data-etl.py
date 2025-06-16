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
page_url = "https://cars.mitula.ph/searchC/level1-Camarines+Sur/sort-0/q-naga-city-bicol?req_sgmt=REVTS1RPUDtTRU87U0VSUDs="

response = requests.get(page_url)

soup = BeautifulSoup(response.content, 'html5lib')

print(soup)


# general data cleaning, manipulation and aggregation scripts here 
# data = pd.DataFrame()
# num = data.count().sort_index(ascending=False).tail()
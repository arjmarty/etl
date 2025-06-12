import pandas as pd
import numpy as np
from datetime import timedelta, datetime as dt
import os
import sys
import requests
import json
from urllib3 import request

data_url = "https://www.klook.com/search/result/?query=philippines&needQueryIdentification=true&spm=Home.SearchSuggest_LIST&clickId=3573313ca4"

#access from other portal
site = requests.post(data_url, verify=True)

site_data = site.json()


# general data cleaning, manipulation and aggregation scripts here 
# data = pd.DataFrame()
# num = data.count().sort_index(ascending=False).tail()

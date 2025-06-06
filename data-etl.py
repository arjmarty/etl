import pandas as pd
import numpy as np
from datetime import timedelta, datetime as dt
import os
import sys
import requests

#access from other portal
DATA_URL = os.getenv("URL_HERE")

r = requests.post(DATA_URL, verify=False)

# general data cleaning, manipulation and aggregation scripts here 
data = pd.DataFrame()
num = data.count().sort_index(ascending=False).tail()

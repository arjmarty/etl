import pandas as pd
import numpy as np
from datetime import timedelta, datetime as dt
import os
import sys
import requests
import json
from bs4 import BeautifulSoup
from urllib import request


# url of intended website
page_url = "https://www.booking.com/"

#open the page
raw_page = request.urlopen(page_url)

#create object from the page
soup = BeautifulSoup(raw_page, 'html5lib')



# general data cleaning, manipulation and aggregation scripts here 
# data = pd.DataFrame()
# num = data.count().sort_index(ascending=False).tail()
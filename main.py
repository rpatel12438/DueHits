import pandas as pd
import numpy as np
import bs4 
import requests
from clean_data import clean_data
from filters import filter_stat

clean_data()
filter_stat('cleaned_batters.csv')

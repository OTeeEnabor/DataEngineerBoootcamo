# 1 scrape first link
# load dynamic links and scrape those
# add all to the same csv
import time
import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
import os
from selenium import webdriver
DRIVER_PATH = r"C:/SeleniumDrivers/chromedriver.exe"
os.environ['PATH'] += DRIVER_PATH

driver = webdriver.Chrome(DRIVER_PATH)

start_url = "https://www.forbes.com/sites/billybambrough/?sh=272453c56a89"
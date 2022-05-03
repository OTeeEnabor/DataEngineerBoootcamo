import time
import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

DRIVER_PATH = r"C:/Users/user/Documents/EdenAI/Data_Engineer/Web_Scrape_Project/chromedriver.exe"
serv_obj = Service(DRIVER_PATH)
driver = webdriver.Chrome(service=serv_obj)
# implicit wait
driver.implicitly_wait(0.5)
driver.maximize_window()
start_url = "https://www.coinbureau.com/blog/"
driver.get(start_url)
time.sleep(5)
# use selenium to scroll through the pages
# scroll till gif appears
# wait
# scroll again till gif appears
# if gif does not appear - no more content to load - parse the page source using bs4 or scrappy
# parse the content (driver.page_source -> parse with beautiful) html.parser? lxml?

#get titles and urls
get_titles = driver.find_elements(By.CLASS_NAME,'stream-item__title')
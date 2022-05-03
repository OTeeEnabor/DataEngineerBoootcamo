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
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

DRIVER_PATH = r"C:/Users/user/Documents/EdenAI/Data_Engineer/Web_Scrape_Project/chromedriver.exe"
serv_obj = Service(DRIVER_PATH)
driver = webdriver.Chrome(service=serv_obj)
# implicit wait
driver.implicitly_wait(0.5)
driver.maximize_window()
start_url = "https://www.forbes.com/sites/billybambrough/?sh=272453c56a89"
driver.get(start_url)
time.sleep(50)
# identify the more articles element
more_articles = driver.find_element(By.CLASS_NAME,"load-more")

# check if the button is displayed
button_displayed = more_articles.is_displayed()

# if the button is displayed click on it
if button_displayed:
    counter = 1
    while button_displayed:
        # if displayed
        try:
            click_more_articles = more_articles.click()
            print(f'button clicked: {counter} times')
            time.sleep(2)
            button_displayed = more_articles.is_displayed()
            time.sleep(2)
            counter += 1
        except:
            print("Finished - no more articles to load!!")
            button_displayed = False # exit while loop
        # print(driver.page_source)
driver.implicitly_wait(2)
# Get all the titles
blog_titles = driver.find_elements(By.CLASS_NAME,'stream-item__title')
blog_titles_list = [elem.text for elem in blog_titles]
# Get all views
blog_views = driver.find_elements(By.CLASS_NAME,'stream-item__views')
blog_views_list = [elem.text for elem in blog_views]
# Get all publish date
blog_publish_date = driver.find_elements(By.CLASS_NAME,'stream-item__date')
blog_publish_date_list = [elem.text for elem in blog_publish_date]
# Get all excerpt
blog_exceprt = driver.find_elements(By.CLASS_NAME,'stream-item__description')
blog_exceprt_list =[elem.text.strip() for elem in blog_exceprt]
# Get all Links to
blog_links_list = [blog_title.get_attribute('href') for blog_title in blog_titles]
#use beautiful soup to parse through the links
author = driver.title

output_dict_list = []

for i in range(len(blog_titles_list)):
    blog_dict ={}
    blog_dict['id'] = i
    blog_dict['author'] = author
    blog_dict['title'] = blog_titles_list[i]
    blog_dict['link'] = blog_links_list[i]
    blog_dict['publish_date'] = blog_publish_date_list[i]
    blog_dict['views'] = blog_views_list[i]
    blog_dict['excerpt'] = blog_exceprt_list[i]

    output_dict_list.append(blog_dict)
    # click the more articles
    #print(more_articles)
def output_csv(bloglist):
    blogs_df = pd.DataFrame(bloglist)
    # change the name to reflect forbes
    blogs_df.to_csv('forbes_selenium.csv', index=False)
    print('Done. Saved to CSV')
    return
output_csv(output_dict_list)
#.print(driver.title)

driver.close()

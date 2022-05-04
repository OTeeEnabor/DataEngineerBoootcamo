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

load_more_button = driver.find_element(By.CLASS_NAME,"feed__load-more-button")
button_displayed = load_more_button.is_displayed()
if button_displayed:
    counter = 1
    while button_displayed:

        try:
            # scroll to desired y position
            print('Got here')
            driver.execute_script('arguments[0].scrollIntoView(true);', load_more_button)
            print(f'scrolled: {counter} times')
            time.sleep(2)
            button_displayed = load_more_button.is_displayed()
            time.sleep(2)
            counter += 1
        except:
            print("Finished - no more articles to load")
            button_displayed = False

driver.implicitly_wait(2)
# Get all the titles
blog_titles = driver.find_elements(By.CLASS_NAME,'feed__title')
blog_titles_list = [elem.text for elem in blog_titles]
# Get all dates
blog_category = driver.find_elements(By.CLASS_NAME,'post-categories')
blog_category_list = [elem.text for elem in blog_category]
# Get all publish date
blog_publish_date = driver.find_elements(By.CLASS_NAME,'feed_date')
blog_publish_date_list = [elem.text for elem in blog_publish_date]
# Get all Links to
blog_links = driver.find_elements(By.CLASS_NAME,'feed__clickable')
blog_links_list = [blog_links.get_attribute('href') for blog_link in blog_links]
#use beautiful soup to parse through the links

output_dict_list = []

for i in range(len(blog_titles_list)):
    blog_dict ={}
    blog_dict['id'] = i
    blog_dict['title'] = blog_titles_list[i]
    blog_dict['link'] = blog_links_list[i]
    blog_dict['publish_date'] = blog_publish_date_list[i]
    blog_dict['Category'] = blog_category_list[i]

    output_dict_list.append(blog_dict)
    # click the more articles
    #print(more_articles)
def output_csv(bloglist):
    blogs_df = pd.DataFrame(bloglist)
    # change the name to reflect forbes
    blogs_df.to_csv('coinbureau_selenium.csv', index=False)
    print('Done. Saved to CSV')
    return
output_csv(output_dict_list)
#.print(driver.title)

driver.close()
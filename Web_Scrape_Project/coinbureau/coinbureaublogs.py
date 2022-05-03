import time
import requests
from bs4 import BeautifulSoup
import json
import pandas as pd

url = "https://www.coinbureau.com/wp-json/wp/v2/posts/?_embed=true&page=1&per_page=100&orderby=date&order=desc"

def get_data(url):
    r = requests.get(url).json()
    return r
def html_parse(data):
    soup = BeautifulSoup(data, 'html.parser')
    # article = soup.find('div',{'class':'article single__content'})
    #class ="article single__content"
    text = soup.find_all('p')
    remove_anchor = [i.decompose('a') for i in text]
    text_list = [item.get_text().strip() for item in remove_anchor]
    print(text_list)
    return text_list

def parse_data(dict):
    blog_dict = {}
    #what do I want
    # blog title, author, exceprt, publish date, blog url
    blog_dict['blog_id'] = dict['id']
    blog_dict['blog_date'] = dict['date_gmt']
    blog_dict['blog_title'] = dict['title']['rendered']
    blog_dict['blog_author'] = dict['yoast_head_json']['twitter_misc']['Written by']
    blog_dict['blog_excerpt'] = dict['excerpt']['rendered']
    # html content
    # use beautifulSoup to parse this content?
    blog_dict['blog_content'] = html_parse(dict['content']['rendered'])
    # print(blog_dict['blog_content'])
    blog_dict['blog_url'] = dict['link']
    return blog_dict

def output_csv(bloglist):
    blogs_df = pd.DataFrame(bloglist)
    blogs_df.to_csv('coinbureau.csv', index=False)
    print('Done. Saved to CSV')
    return

# for item in get_data(url):
#     print(item['title']['rendered'])

# print(len(get_data(url)))
# print(get_data(url))
# blog_dict_test_list = [parse_data(item) for item in get_data(url)]
# for item in blog_dict_test_list:
#     print(item['blog_content'])

results = []
for x in range(1,17):
    data = get_data(f'https://www.coinbureau.com/wp-json/wp/v2/posts/?_embed=true&page={x}&per_page=100&orderby=date&order=desc')
    for item in data:
        results.append(parse_data(item))
    print(f'Scraped page {x}')
    time.sleep(1.5)


output_csv(results)




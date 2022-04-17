import requests
import pandas as pd
import json
from bs4 import BeautifulSoup
import time

# get URL for main page
main_url = "https://www.forbes.com/sites/billybambrough/?sh=272453c56a89"
more_article1 = "https://www.forbes.com/simple-data/more-stream?date=1649644828330&start=6&ids=content_625be8c5a7f10500017f4e32,content_62596dccf69f28000164a448,content_6259436da7f1050001af92bc,content_6254cd35897b0800019d8f25,content_62538df09023e80001002b54&sourceType=author&sourceValue=blogstream-blogAuthorId/blog/author/blog-5660_all&limit=&source=stream&isBlog="
more_article2 = "https://www.forbes.com/simple-data/more-stream?date=1648163716000&start=16&ids=content_625be8c5a7f10500017f4e32,content_62596dccf69f28000164a448,content_6259436da7f1050001af92bc,content_6254cd35897b0800019d8f25,content_62538df09023e80001002b54,content_624e806ad09ee00001afd857,content_624bf0fb542e2e0001d0f28f,content_624ab695a1f3a400019ea3f8,content_6246cd6644424900015891e5,content_6244241cd510970001ee5ee1,content_6242d5b53e5b540001523c91,content_62431c3195eae10001b1c27a,content_624183645e1a5600014b7ce3,content_623d85dd12aab400014e6bd5,content_623af38afa60540001776077&sourceType=author&sourceValue=blogstream-blogAuthorId/blog/author/blog-5660_all&limit=&source=stream&isBlog="
more_articles3 = "https://www.forbes.com/simple-data/more-stream?date=1647239430000&start=26&ids=content_625be8c5a7f10500017f4e32,content_62596dccf69f28000164a448,content_6259436da7f1050001af92bc,content_6254cd35897b0800019d8f25,content_62538df09023e80001002b54,content_624e806ad09ee00001afd857,content_624bf0fb542e2e0001d0f28f,content_624ab695a1f3a400019ea3f8,content_6246cd6644424900015891e5,content_6244241cd510970001ee5ee1,content_6242d5b53e5b540001523c91,content_62431c3195eae10001b1c27a,content_624183645e1a5600014b7ce3,content_623d85dd12aab400014e6bd5,content_623af38afa60540001776077,content_623c9da82be974000185d6f3,content_6239a6342be97400010118f2,content_6238af069c15b200017dd629,content_62385a309c15b20001235d53,content_6236d5f874d6b8000110fd05,content_6235af60c43f3f0001f81c42,content_6231bddd9f51ad0001b7a5d0,content_623064873c435800012eabe7,content_622f1e7fb8ae06000131dba7,content_622ed143b8ae060001146402&sourceType=author&sourceValue=blogstream-blogAuthorId/blog/author/blog-5660_all&limit=&source=stream&isBlog="
more_articles4 = "https://www.forbes.com/simple-data/more-stream?date=1646267412000&start=36&ids=content_625be8c5a7f10500017f4e32,content_62596dccf69f28000164a448,content_6259436da7f1050001af92bc,content_6254cd35897b0800019d8f25,content_62538df09023e80001002b54,content_624e806ad09ee00001afd857,content_624bf0fb542e2e0001d0f28f,content_624ab695a1f3a400019ea3f8,content_6246cd6644424900015891e5,content_6244241cd510970001ee5ee1,content_6242d5b53e5b540001523c91,content_62431c3195eae10001b1c27a,content_624183645e1a5600014b7ce3,content_623d85dd12aab400014e6bd5,content_623af38afa60540001776077,content_623c9da82be974000185d6f3,content_6239a6342be97400010118f2,content_6238af069c15b200017dd629,content_62385a309c15b20001235d53,content_6236d5f874d6b8000110fd05,content_6235af60c43f3f0001f81c42,content_6231bddd9f51ad0001b7a5d0,content_623064873c435800012eabe7,content_622f1e7fb8ae06000131dba7,content_622ed143b8ae060001146402,content_622cbe89267eee0001d2db70,content_622892e8dcc7870001e56863,content_6228738d8f0ee5000188c3c6,content_6227927c56eadc00019ebd00,content_62248ca2f3a59700013d059d,content_622476faeb74330001312a95,content_6223361ef3a5970001f17091,content_62209f4469b0da00014760b5,content_621b768cc5cac3000183c0c9,content_621b7ab3e5fd6500017bdfce&sourceType=author&sourceValue=blogstream-blogAuthorId/blog/author/blog-5660_all&limit=&source=stream&isBlog="

# get data using beautifulSoup
def get_data(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text,'html.parser')
    return soup
def get_data_json(url):
    r = requests.get(url).json()
    return r['streamItems']
def html_parse(soup):
    # get author name - span class="contributor-details__name-span" css selector
    blog_author = soup.find('span',{'class':'contributor-details__name-span'}).get_text()
    # get all blog titles
    blog_title = soup.find_all('a',{'class':'stream-item__title'},href=True)
    blog_title_list = [item.get_text() for item in blog_title]
    # get blog link
    blog_link_list = [item['href'] for item in blog_title]
    # get blog excerpt
    blog_excerpt = soup.find_all('div',{'class':'stream-item__description'})
    blog_excerpt_list = [item.get_text() for item in blog_excerpt]
    # get blog publish date
    blog_date = soup.find_all('div',{'class':'stream-item__date'})
    blog_date_list = [item.get_text() for item in blog_date]
    # get blog views
    blog_views = soup.find_all('div',{'class':'stream-item__views'})
    blog_views_list = [item.get_text() for item in blog_views]

    blog_dict_list =[]
    for x in range(len(blog_title_list)):
        blog_dict={}
        blog_dict['Author'] = blog_author
        blog_dict['Title']  = blog_title_list[x]
        blog_dict['Excerpt'] = blog_excerpt_list[x]
        blog_dict['Views'] = blog_views_list[x]
        blog_dict['Publish_Date'] = blog_date_list[x]
        blog_dict['Link'] = blog_link_list[x]
        blog_dict_list.append(blog_dict)

    return blog_dict_list
    # print(len(blog_title_list))
    # print(len(blog_link_list))
    # print(len(blog_excerpt_list))
    # print(len(blog_date_list))
    # print(len(blog_views_list))
def parse_data(dict):
    blog_dict = {}
    # blog title, author, exceprt, publish date, blog url
    blog_dict['Author'] = dict['author']['name']
    blog_dict['Publish_Date'] = dict['timestamp']
    blog_dict['Title'] = dict['title']
    blog_dict['Excerpt'] = dict['description']
    blog_dict['Link'] = dict['url']
    blog_dict['Views'] = dict['pageViews']
    return blog_dict

def output_csv(bloglist):
    blogs_df = pd.DataFrame(bloglist)
    blogs_df.to_csv('coinbureau.csv', index=False)
    print('Done. Saved to CSV')
    return
# create list to store the urls to pull json-stream
more_articles_list = [more_article1, more_article2, more_articles3, more_articles4]
# create a list of dictionaries from the content pulled from the main blog url
main_url_blog_dict_list = html_parse(get_data("https://www.forbes.com/sites/billybambrough/?sh=272453c56a89"))
# create a list to store the dictionaries created from the json-stream
blog_json_dict_list =[]
# get each json-stream url
for url in more_articles_list:
    # get the data from each json-stream url
    for item in get_data_json(url):
        # add the data to json dictionary list creaeted aboe
        blog_json_dict_list.append(parse_data(item))
        time.sleep(1.5)

# add the dictionaries to the main_url list
for item in blog_json_dict_list:
    main_url_blog_dict_list.append(item)
# output URL List to CSV
output_csv(main_url_blog_dict_list)




#     # do something
# for item in get_data_json(more_article1):
#     print(item.keys())
# # print(get_data_json(more_article1))
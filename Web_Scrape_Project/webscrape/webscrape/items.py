# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import Join,TakeFirst,MapCompose
from w3lib.html import remove_tags
import datetime

def remove_characters(value):
    return value.strip()
class WebscrapeItem(scrapy.Item):
    # define the fields for your item here like:
    blog_url= scrapy.Field()
    blog_title = scrapy.Field(input_processor = MapCompose(remove_tags),output_processor=TakeFirst())
    blog_excerpt = scrapy.Field(input_processor = MapCompose(remove_tags),output_processor=TakeFirst())
    blog_text = scrapy.Field(input_processor = MapCompose(remove_tags),output_processor=Join('\n'))
    blog_author = scrapy.Field(input_processor = MapCompose(remove_tags),output_processor=TakeFirst())
    blog_publish_date = scrapy.Field(input_processor = MapCompose(remove_tags,remove_characters),output_processor=TakeFirst())
    blog_pull_timestamp = datetime.datetime.now()
    # name = scrapy.Field()
    pass

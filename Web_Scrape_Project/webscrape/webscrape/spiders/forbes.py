#import scrappy
import scrapy
from ..items import WebscrapeItem
from scrapy.loader import ItemLoader
# Import the CrawlerProcess: for running the spider
from scrapy.crawler import CrawlerProcess

class OpenDeltaCrawler(scrapy.Spider):
    name = "openDeltaCrawler"

    def start_requests(self):
        url = "https://www.moneyweb.co.za/moneyweb-crypto/"
        #headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
        yield scrapy.Request(url, callback = self.parse_blog)

    def parse_blog(self,response):
        # Go to the blocks that contain blog posts
        blog_posts = response.xpath('//h3[contains(@class,"title list-title m0005")]')
        # Go to the blog links
        blog_links = blog_posts.xpath('./a/@href')
        print(blog_links)
        # Extract the links (as a list of strings)
        links_to_follow = blog_links.extract()
        print(links_to_follow)
        # Follow the links in the next parser


        for url in links_to_follow:
            #headers = {'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}
            yield response.follow(url=url, callback=self.parse_pages)

    def parse_pages(self, response):
        i = ItemLoader(item=WebscrapeItem(), selector=response)
        i.add_css('blog_title','h1.article-headline')
        i.add_css('blog_excerpt','div.article-excerpt')
        i.add_xpath('blog_author','//div[@class="article-meta grey-text"]/span[1]/span')
        i.add_xpath('blog_publish_date','//div[@class="article-meta grey-text"]/span[2]')
        i.add_xpath('blog_text','//p')
        i.add_value('blog_url',response.url)
        yield i.load_item()


        # item = WebscrapeItem()
        # # Direct to the blog title text
        # blog_title = response.css('h1.article-headline::text')
        # # Exctract and clean the blog title text
        # blog_title_clean = blog_title.extract_first().strip()
        # # Direct to the Exceprt
        # blog_excerpt = response.css('div.article-excerpt::text')
        # # Extract and clean the blog exceprt
        # blog_excerpt_clean = blog_excerpt.extract_first().strip()
        # # Direct to Blog Author
        # blog_author = response.xpath('//div[@class="article-meta grey-text"]/span[1]/span/text()')
        # # Extract and clean the author
        # blog_author_clean = blog_author.extract_first().strip()
        # # Direct to publish
        # blog_publish_date = response.xpath('text()')
        # # Extract and clean the publish date
        # blog_publish_date_clean = blog_publish_date.extract_first().strip()
        # print(blog_publish_date_clean)
        # print(blog_author_clean)
        # # code to parse blog posts



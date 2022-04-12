#import scrappy
import scrapy

# Import the CrawlerProcess: for running the spider
from scrapy.crawler import CrawlerProcess

class OpenDeltaCrawler(scrapy.Spider):
    name = "openDeltaCrawler"

    def start_requests(self):
        url = "https://www.moneyweb.co.za/moneyweb-crypto/"
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
        yield scrapy.Request(url, headers=headers, callback = self.parse_blog)

    def parse_blog(self,response):
        # Go to the blocks that contain blog posts
        blog_posts = response.css('row m1000')
        # Go to the blog links
        blog_links = blog_posts.xpath('./a/@href')
        # Extract the links (as a list of strings)
        links_to_follow = blog_links.extract()
        # Follow the links in the next parser
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}

        for url in links_to_follow:
            yield response.follow(url=url,headers=headers, callback=self.parse_pages)

    def parse_pages(self, response):
        # Direct to the blog title text
        blog_title = response.css('h1.article-headline::text')
        # Exctract and clean the blog title text
        blog_title_clean = blog_title.extract_first().strip()
        # Direct to the Exceprt
        blog_excerpt = response.css('div.article-excerpt::text')
        # Extract and clean the blog exceprt
        blog_excerpt_clean = blog_excerpt.extract_first().strip()
        # Direct to Blog Author
        blog_author = response.xpath('//div[@class="article-meta grey-text"]/span[1]/span/text()')
        # Extract and clean the author
        blog_author_clean = blog_author.extract_first().strip()
        # Direct to publish
        blog_publish_date = response.xpath('//div[@class="article-meta grey-text"]/span[2]/span/text()')
        # Extract and clean the publish date
        blog_publish_date_clean = blog_publish_date.extract_fisrt().strip()
        print(blog_publish_date_clean)
        print(blog_author_clean)
        # code to parse blog posts



blog_dic = dict()

process= CrawlerProcess()
process.crawl(OpenDeltaCrawler)
process.start()
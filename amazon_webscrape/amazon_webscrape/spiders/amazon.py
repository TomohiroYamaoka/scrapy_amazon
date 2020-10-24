import scrapy


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['amazon.co.jp']
    start_urls = ['http://amazon.co.jp/']

    def parse(self, response):
        pass

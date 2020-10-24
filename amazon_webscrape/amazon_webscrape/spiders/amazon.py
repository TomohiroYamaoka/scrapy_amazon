import scrapy
from  ..items import AmazonItem

class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['amazon.co.jp']
    start_urls = ['https://www.amazon.co.jp/']

    def parse(self, response):
        item_name = response.css(".product-title>h1.a-size-large>a.a-link-normal::text").get()
        for amazon_item in response.css(".review>.a-row>.celwidget"):
            yield AmazonItem(
                name=post.css("span.a-profile-name::text").get(),
                title = post.css(".review-title>span::text").get(),
                star = int(post.css(".a-icon-star>span::text").get()[-3:-2]),
                date = post.css(".review-date::text").get()[0:10],
                quote_text = ','.join(post.css(".review-text-content>span::text").getall()),
                item_name=item_name
            )
            older_post_link = response.css("li.a-last>a::attr(href)").extract_first()
            if older_post_link is None:
                return
                
            older_post_link = response.urljoin(older_post_link)
            yield scrapy.Request(older_post_link, callback=self.parse)


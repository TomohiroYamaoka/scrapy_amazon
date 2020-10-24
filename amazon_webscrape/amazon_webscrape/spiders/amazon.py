import scrapy
from  ..items import AmazonItem

class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['amazon.co.jp']
    start_urls = ['https://www.amazon.co.jp/dp/B00IMEA9CU#customerReviews']

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
            
            next_page = response.css("li.a-last>a::attr(href)").extract_first()
            if next_page is None:
                return
                
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)



#https://qiita.com/ritukiii/items/272d485e8a249d0d1bd7
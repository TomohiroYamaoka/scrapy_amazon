# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Post(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    title = scrapy.Field()
    star = scrapy.Field()
    date = scrapy.Field()
    quote_text = scrapy.Field()
    item_name = scrapy.Field()
    
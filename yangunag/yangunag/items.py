# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class YangunagItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    href = scrapy.Field()
    publish_date = scrapy.Field()
    content_img = scrapy.Field()
    content = scrapy.Field()

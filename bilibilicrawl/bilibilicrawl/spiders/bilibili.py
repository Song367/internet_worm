import scrapy
from ..items import BilibilicrawlItem


class BilibiliSpider(scrapy.Spider):
    name = 'bilibili'
    allowed_domains = ['bilibili.com']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        a = response.xpath('//ul[@class="clears"]/li')[4:-4]
        item = BilibilicrawlItem()
        for div in a:
             li = div.xpath('./div[@class="main_bot"]//h2')
             item["username"] = li.xpath('./text()').extract_first()
             item["work"] = li.xpath('./span/text()').extract_first()

             yield item

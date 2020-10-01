import scrapy
import logging

logger = logging.getLogger(__name__)

class Douban1Spider(scrapy.Spider):
    name = 'douban1'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        #print(response)
        x = {'key':'value'}
        for _ in range(5):
            logger.warning(x)
            yield x


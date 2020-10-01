import scrapy

import re
from scrapy.settings.default_settings import USER_AGENT
from scrapy.http import Request
from scrapy.selector import Selector
from ..items import MyscrapysItem
from urllib.parse import urljoin


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        print(self.settings.get('USER_AGENT'))        # 获取settings中的元素
        # ret = response.xpath("//div[@class='tea_con']//h3/text()").extract()    # 获取Selector中的中文

        ret = response.xpath("//div[@class='tea_con']//li[last()]")     # //相对路径下  /绝对路径  @标签属性 text()显示内容 last()最后一个
        res = {}
        for li in ret:
            res['name'] = li.xpath(".//h3/text()").extract_first()      # extract_first是获取第一个值当拿不到值时，就返回None
            res['title'] = li.xpath(".//h4/text()").extract_first()

            # Request, Baseitem ,dict,None   #返回值类型只能是这四种
            yield res   # yield 是将数据传到pipelines


        # item = MyscrapysItem()
        # selector = Selector(response)
        # Movies = selector.xpath('//div[@class="info"]')
        # for eachMovie in Movies:
        #     title = eachMovie.xpath('div[@class="hd"]/a/span/text()').extract()  # 多个span标签
        #     fullTitle = "".join(title)  # 将多个字符串无缝连接起来
        #     movieInfo = eachMovie.xpath('div[@class="bd"]/p/text()').extract()
        #     star = eachMovie.xpath('div[@class="bd"]/div[@class="star"]/span/text()').extract()[0]
        #     quote = eachMovie.xpath('div[@class="bd"]/p[@class="quote"]/span/text()').extract()
        #     # quote可能为空，因此需要先进行判断
        #     if quote:
        #         quote = quote[0]
        #     else:
        #         quote = ''
        #     item['title'] = fullTitle
        #     item['movieInfo'] = ';'.join(movieInfo)
        #     item['star'] = star
        #     item['quote'] = quote
        #     yield item
        # nextLink = selector.xpath('//span[@class="next"]/link/@href').extract()
        # # 第10页是最后一页，没有下一页的链接
        # if nextLink:
        #     nextLink = nextLink[0]
        #     yield Request(urljoin(response.url, nextLink), callback=self.parse)


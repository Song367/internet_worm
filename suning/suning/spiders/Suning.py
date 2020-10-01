import scrapy
from ..items import SuningItem


class SuningSpider(scrapy.Spider):
    name = 'Suning'
    allowed_domains = ['suning.com']
    start_urls = ['https://book.suning.com/?safp=d488778a.homepagev8.126605238627.43&safpn=10001']

    def parse(self, response):
        item = SuningItem()
        lists = response.xpath('//div[@class="menu-list"]/div')[6]       # 这是获取三个类别的书籍   科普，医学，互联网
        smallcate = lists.xpath('.//dd/a')
        for a in smallcate:
            item['name'] = a.xpath('text()').extract_first()             # 获取这三个类别的名字和ip
            item['href'] = a.xpath('@href').extract_first()

            yield scrapy.Request(                                        # 返回每一个类别的到parseAll中进行处理
                item['href'],
                meta={'href': item['href'],
                      'name': item['name'],
                      'res': item.copy()     # 深拷贝
                      },
                callback=self.parseAll,
            )

    def parseAll(self, response):
        # print(response.meta['res'])
        lists = response.xpath('//div[@id="filter-results"]/ul/li')
        # print(lists)
        res = {}
        item1 = response.meta['res']

        res['price'] = lists.xpath('//div[@class="res-info"]/p[@class="prive-tag"]/em/@datasku').extract()
        res['state'] = lists.xpath('//div[@class="res-info"]/p[@class="sell-point"]/a/text()').extract()
        for i in res['state']:
            if '\n' == i:
                res['state'].remove(i)

        for i in range(len(res['price'])):
            item1['price'] = res['price'][i]
            item1['state'] = res['state'][i]
            yield item1

        next_url = response.xpath('//div[@id="bottom_pager"]/a/@href')[:-1].extract()    # 下一页
        #next_url = 'https://list.suning.com/' + next_url
        for i in next_url:
            i = 'https://list.suning.com/' + i          # 组装完整url

            if i:
                yield scrapy.Request(
                    i,
                    callback=self.parseAll,
                    meta={'res':item1.copy()}
                )

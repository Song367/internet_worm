import scrapy


class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['tencent.com']
    start_urls = ['http://hr.tencent.com/position.php']

    def parse(self, response):
        print(response)
        tr_list = response.xpath("//table[@class='tablelist']/tr")[1:-1]
        for tr in tr_list:
            item={}
            item["title"] = tr.xpath("./td[1]/a/text()").extract_first()
            yield item

        # 下一页的url
        # while len(next_url)>0:
        # yield scrapy.Request(url,callback=self.parse,meta={'item':item},dont_filter=False)
        # callback就是执行函数  meta在不同解析函数中传输数据  parse就是一个解析函数 dont_filter=False不过滤url

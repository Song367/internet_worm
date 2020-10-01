import scrapy
from ..items import YangunagItem


class YgSpider(scrapy.Spider):
    name = 'yg'
    allowed_domains = ['sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=0']

    def parse(self, response):
        tr_list = response.xpath("//div/[@class='greyframe']/table/tr/td/table/tr")
        for tr in tr_list:
            item = YangunagItem()
            item['title'] = tr.xpath("./td[2]/a[@class='news14']/@title").extract_first()
            item['href'] = tr.xpath("./td[2]/a[@class='news14']/@href").extract_first()
            item['publish_data'] = tr.xpath("./td[last()]/text()").extract_first()
            yield scrapy.Request(
                item["href"],   # url
                callback=self.parse_detail,
                meta={"res": item}
            )

        next_url = response.xpath("//a[text()='>']/@href").extract_first()
        if next_url:
            yield scrapy.Request(
                next_url,
                callback=self.parse
            )

    # 详情页
    def parse_detail(self,response):
        item = response.meta['res']
        print(item)
        item["content"] = response.xpath("//div[@class='cl text14_2']//text()").extract()
        item["content_img"] = response.xpath("//div[@class='c1 text14_2']//img/@src").extract()
        item["content_img"] = ["http://wz.sun0769.com" + i for i in item["content_img"]]

        yield item
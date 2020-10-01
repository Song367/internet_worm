# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import logging

class MyscrapysPipeline:
    # item是douban.py文件传来的数据  spider是douban.py的类
    def process_item(self, item, spider):
        #print(item)
        #print(spider.name=='douban')
        print(item)
        return item

class MyscrapysPipeline1:
    # item是douban.py文件传来的数据  spider是douban.py的类
    def open_spider(self,spider):     # 当开始爬虫时要进行的操作
        spider.hello = 'world'

    def close_spider(self,spider):    # 当结束爬虫时进行的操作
        print(spider.hello)

    def process_item(self, item, spider):
        print(spider.settings.get('USER_AGENT'))
        #print(item)
        if spider.name=='douban1':

            print(spider.name)
        return item
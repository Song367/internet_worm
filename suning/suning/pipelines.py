# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import xlwt
import pymysql


# 将数据存为excel文件
class SuningPipeline:
    def open_spider(self,spider):
        self.book = xlwt.Workbook(encoding='utf-8')
        self.sheet = self.book.add_sheet('suning__book')
        col = ['name','href','price','state']
        for i in range(len(col)):
            self.sheet.write(0,i,col[i])
        self.j = 0

    def process_item(self, item, spider):

        self.j+=1
        arr = [item['name'],item['href'],item['price'],item['state']]
        if self.j >= 65536:
            return item
        for i in range(len(arr)):
            self.sheet.write(self.j,i,arr[i])
        return item

    def close_spider(self,spider):
        self.book.save('./suning.xls')


# 将数据存入mysql
class SuningPipeline2:
    def open_spider(self,spider):
        self.conn = pymysql.connect(db='test1', user='root', passwd='admin123', host='localhost', port=3306, charset='utf8')
        self.cur = self.conn.cursor()
        self.j = 0

    def process_item(self,item,spider):
        sql = '''insert into suning(name,state,href,price) values(%s,%s,%s,%s)'''
        if self.j >= 65536:
            return item
        self.cur.execute(sql,[item['name'],item['state'],item['href'],item['price']])
        self.j += 1

        return item

    def close_spider(self,spider):
        self.conn.commit()
        self.conn.close()


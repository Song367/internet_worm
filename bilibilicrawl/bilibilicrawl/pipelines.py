# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import xlwt


class BilibilicrawlPipeline:
    # 打开时执行的操作
    def open_spider(self,spider):
        self.book = xlwt.Workbook(encoding="utf-8")   # 创建对象
        self.sheet = self.book.add_sheet('名字')      # 创建表
        self.j=0
        col = ['老师名', '老师职位']
        for i in range(len(col)):  # 写入列名
            self.sheet.write(0, i, col[i])

    def process_item(self, item, spider):

        self.sheet.write(self.j+1, 0, item['username'])
        self.sheet.write(self.j+1, 1, item['work'])
        self.j += 1
        print(item)
        return item

    def close_spider(self,spider):
        self.book.save('test.xls')      # 保存数据到excel中


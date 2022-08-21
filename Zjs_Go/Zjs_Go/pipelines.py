# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

from itemadapter import ItemAdapter
from scrapy.exporters import CsvItemExporter
import json
from collections import OrderedDict


class ZjsGoPipeline:

    def __init__(self):
        self.file = open('Zjs.csv', 'wb')
        self.exporter = CsvItemExporter(self.file, encoding='utf-8')
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        # print('默认的字段数据：{}\n'.format(item))
        item = OrderedDict(item)
        item = json.dumps(item, ensure_ascii=False)
        print('调整后的字段数据：{}\n'.format(item))
        self.exporter.export_item(eval(item))
        return item

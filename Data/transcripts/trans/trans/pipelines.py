# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exporters import CsvItemExporter
from scrapy.exporters import JsonItemExporter

class WriteItemPipeline(object):
    def __init__(self):
        self.file = open("trans.json", 'wb')
        self.exporter = JsonItemExporter(self.file ) # json is  by definition an unordered collection thus you need to order cols in python later
        self.exporter.start_exporting()
 
    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()
 
    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

   
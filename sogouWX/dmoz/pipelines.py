# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import signals
from scrapy.contrib.exporter import CsvItemExporter
# from dmoz.spiders.ganji import *

class DmozPipeline(object):
    def process_item(self, item, spider):
        pass
class WechatPipeline(object):
##	@classmethod
##	def from_scrawl(cls,crawler):
##		pipeine=cls()
##		crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
##        	crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
##		return pipeline
	def open_spider(self,spider):
		self.file=open('wechat.csv','w+b')
		self.file.write('\xEF\xBB\xBF')
		self.exporter=CsvItemExporter(self.file)
		self.exporter.fields_to_export = ['page','wID','wtitle','wsub','Link']
		# self.exporter.fields_to_export = ['jobTitle','salary','education','ex','age','num','contact','location','updatetime','url','Requirement','comInfo','delivery_num']
		self.exporter.start_exporting()

	def close_spider(self,spider):
		self.exporter.finish_exporting()
		self.file.close()
	def process_item(self,item,spider):
		self.exporter.export_item(item)
		return item




# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import signals
from scrapy.contrib.exporter import CsvItemExporter
import sys
import MySQLdb
import hashlib
from scrapy.exceptions import DropItem
from scrapy.http import Request
class MySQLStorePipeline(object):
	host='localhost'
	user='Jason'
	password='520205'
	db='jason'
	def __init__(self):
		self.connection=MySQLdb.connect(host=self.host,user=self.user,passwd=self.password,db=self.db,charset='utf8')
		self.cursor=self.connection.cursor()

	def process_item(self,item,spider):
		try:
			self.cursor.execute("""INSERT INTO wechat (page,wID,wTitle,wSub) 
				VALUES (%s,%s,%s,%s)""",
				(item['page'][0],item['wID'][0],item['wtitle'],item['wsub']))
			self.connection.commit()
                except MySQLdb.Error,e:
                        print "Error %d: %s" % (e.args[0], e.args[1])
                return item




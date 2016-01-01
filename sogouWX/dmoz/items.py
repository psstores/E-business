# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
from scrapy.item import Item, Field 
class DmozItem(Item):
    name = Field()                # 职位名称
    catalog = Field()             # 职位类别
    workLocation = Field()        # 工作地点
    recruitNumber = Field()       # 招聘人数
    detailLink = Field()          # 职位详情页链接
    publishTime = Field()         # 发布时间
class GanjiItem(Item):
	page=Field()
	title=Field()
	add=Field()
	time=Field()
	url=Field()
class GanjidetailItem(Item):
	jobTitle=Field()
	salary=Field()
	education=Field()
	ex=Field()
	age=Field()
	num=Field()
	contact=Field()
	location=Field()
	Requirement=Field()
	comInfo=Field()
	url=Field()
	delivery_num=Field()
	updatetime=Field()
class WxItem(Item):
	wtitle=Field()
	wsub=Field()
	# Link=Field()
	wID=Field()
	# date=Field()
	page=Field()



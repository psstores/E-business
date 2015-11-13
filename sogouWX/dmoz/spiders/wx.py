# #encoding=utf-8
import scrapy
from scrapy import log
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.http import Request,FormRequest
from dmoz.settings import *
from dmoz.items import *
import codecs
import chardet
import re
from scrapy import Selector
class DmozSpider(CrawlSpider):
    name = "wx"
    allowed_domains = ["weixin.sogou.com"]
    start_urls = [
        # "http://www.baidu.com",  
        ]
    querystring=u'三七用法'
    type=2
    for i in range(1,11,1):
		start_urls.append("http://weixin.sogou.com/weixin?type=%d&query=%s&page=%d"%(type,querystring,i))
##    rules = [
##           # 提取匹配 'category.php' (但不匹配 'subsection.php') 的链接并跟进链接(没有callback意味着follow默认为True)
##           Rule(LinkExtractor(allow=("http://weixin.sogou.com/weixin\?query=37&type=2&page=\d*&ie=utf8")),callback='parse_item',follow=True)
##           # Rule(LinkExtractor(allow=('/[a-zA-Z]*/\d*x\.htm')),callback='parse_object',follow=True) 
##           ]
##            
#    def parse_item(self, response):
#        self.log('HI,this is an item page!%s'% response.url)
#        filename = response.url.split("/")[-2]
#        with open(filename, 'wb') as f:
#            f.write(response.body)
    # def __init__(self):

    #      self.headers=HEADER
    #      self.cookies=COOKIES
        
    # def start_requests(self):
    #      for i,url in enumerate(self.start_urls):
    #          yield FormRequest(url,
    #                            meta={'cookiejar':i},
    #                            headers=self.headers,
    #                            # cookies=self.cookies,
    #                            callback=self.parse_item)
##    def parse(self,response):
##        f=open('t.html','w')
##        f.write(response.body)
##        f.close()
##        print 'done'

    def parse(self,response):
        self.log(response.url+'************************************************************')
        filename = 'ganji_url.txt'
        f=open('test.html','w')
        f.write(response.body)
        f.close()
        response=response.replace(body=response.body.replace('<em>',''))
        sel=Selector(response)
        sites=sel.xpath('//div[contains(@id,"sogou_vr_")]')
        p=re.compile(r'page=(\d*)')
        print len(sites)
        print sites[0].extract()
        print sites[0].xpath('div[@class="txt-box"]/h4/a/text()').extract()
        for site in sites:
            item=WxItem()
            item['page']=p.findall(response.url)
            item['wtitle']=''.join(site.xpath('div[@class="txt-box"]/h4/a/text()').extract())
            item['wsub']=''.join(site.xpath('div[@class="txt-box"]/p[contains(@id,"sogou_vr_")]/text()').extract())
            # item['Link']=''.join(list(list('http://weixin.sogou.com')+site.xpath('div[@class="txt-box"]/div[@class="s-p"]/a/@href').extract()))
            item['wID']=site.xpath('div[@class="txt-box"]/div[@class="s-p"]/a[@id="weixin_account"]/@title').extract()
            # item['date']=site.xpath('div[@class="txt-box"]/div[@class="s-p"]/text()').extract()
            yield item

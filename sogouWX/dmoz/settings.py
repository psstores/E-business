# -*- coding: utf-8 -*-

# Scrapy settings for dmoz project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#
import json
BOT_NAME = 'dmoz'
# DOWNLOAD_DELAY = 0.25
SPIDER_MODULES = ['dmoz.spiders']
NEWSPIDER_MODULE = 'dmoz.spiders'
DOWNLOAD_DELAY=2
COOKIES={
 	'CXID':r'0254A816144F030B91385E0F74F035AF',
        'IPLOC':r'CN5300',
        'ppinf':r'5|1446953493|1448163093|Y2xpZW50aWQ6NDoyMDE3fGNydDoxMDoxNDQ2OTUzNDkzfHJlZm5pY2s6Mjpxd3x0cnVzdDoxOjF8dXNlcmlkOjQ0OjAxQUVCNTYwNDIyNDEwRTg0OTRCNUZGRjU0N0MxOTJFQHFxLnNvaHUuY29tfHVuaXFuYW1lOjI6cXd8',
        'pprdig':r'GPCuM0zRIrVCvhuiDThj6suVbT-RPMTO-dDL9J4lZyaQSi9OWBF6PY6ASSXBSC6_UCKLtn3vF_UQGIPhXaf21F3ZchKZnQ521s32XJFJ3SdU8P3fo38IIf-VJZbcE1huZBa6Q6SYL7JPl96O_QFYHtwsBFyCF-aEpB4jWgmBKJw',
        'sct':r'2',
        'SNUID':r'8B394513A5A1874D2EC9FDDBA5346845',

        'SUID':r'ED09AE7C791C900A5518001C000C8392',
        'SUV':r'00ED7C9A715135E955FE050CDE805945',
        'wapsogou_qq_nickname':r'',
        'ABTEST':r'0|1446860790|v1',
        'ppmdig':r'14469534930000001350d64badf621c5d9d9d567eb62ad52',
        'weixinIndexVisited':r'1'
        
 }
HEADER={
     # "Host": "www.baidu.com",
     "Connection": "keep-alive",
     "Cache-Control": "max-age=0",
     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
     "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36",
     "Accept-Encoding": "gzip,deflate,sdch",
     "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4,zh-TW;q=0.2",
     }

##Crawl responsibly by identifying yourself (and your website) on the user-agent
##USER_AGENT = 'dmoz (+http://www.yourdomain.com)'
# DOWNLOADER_MIDDLEWARES={
# 	'scrapy.contrib.downloadermiddleware.CasperjsMiddleware.CasperjsMiddleware':542
# }
ITEM_PIPELINES={
	# 'dmoz.pipelines.WechatPipeline':301
    'dmoz.MysqlPipelines.MySQLStorePipeline':300
}
EXPORT_FIELDS=['page','title','add','time','url']
FEED_EXPORTERS = {
    'csv': 'dmoz.feedexport.CSVkwItemExporter',
    
}

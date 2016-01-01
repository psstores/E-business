# encoding=utf-8
#提取阿里巴巴详情页图片
import urllib2
import urllib
import re
import pdb
from os import getcwd,listdir
import os
import time
from bs4 import BeautifulSoup
#'re='window.runParams.descUrl="(.*?)"'匹配详情页地址
url=raw_input('Please input your alibaba url in here: ')
##fp=open('html.html','w')
#url='http://www.aliexpress.com/item/Luxury-Universal-Selfie-Stick-Monopod-for-Iphone-6-Plus-5s-Wired-Palo-Selfie-For-SAMSUNG-Android/32372569056.html'
##url='http://www.aliexpress.com/store/product/Hot-Sale-2015-New-Summer-Girl-Dress-Fashion-Printed-Dress-Baby-Girls-Dress-Cotton-Children-s/1328152_32315365720.html'
req=urllib2.Request(url)
res=urllib2.urlopen(req)
re1=r'data-tfs-url="(.*?)"'
html=res.read()
url1=re.findall(re1,html)
print url1

try:
    url1=url1[0]
    req1=urllib2.Request(url1)
    res1=urllib2.urlopen(req1)
    con=res1.read()
##    fw=fp.write(html)
    #print con
    re2=r'src=\\"(.*?)\\"'
    con1=re.findall(re2,con)
    i=0
    fn='.jpg'
    fn1='0.jpg'
    fn2='0.jpg'
    print u'匹配网址并下载'
    
    for x in con1:
        if os.path.exists(getcwd()+'\Images') :
            print u'写入图片到Image'
            mypath=getcwd()+'\images'
            #改变目录
            os.chdir(mypath)
            urllib.urlretrieve(x,fn1)
            i=i+1
            fn1=str(i)+fn
            print x
        else:
            os.mkdir(getcwd()+'\images')
            mypath=getcwd()+'\images'
            os.chdir(mypath)
            urllib.urlretrieve(x,fn1)
            i=i+1
            fn1=str(i)+fn
            print x
        os.chdir(os.path.pardir)
    print u'下载完成'
except IndexError:
    print u'请确保该网址为阿里巴巴产品详情页地址！！！'

#下载nav_item图片
soup=BeautifulSoup(html,'html.parser',from_encoding='utf-8')
nav_ul=soup.find_all('ul',{'class':'nav nav-tabs fd-clr'})[0]
nav_lis=nav_ul.find_all('li')
if os.path.exists(getcwd()+'\nav_item'):
    mypath=getcwd()+'\nav_item'
    os.chdir(mypath)
    for nav_li in nav_lis:
        y=nav_li.find_all('img')[0].get('src')[:-9]+'jpg'
        urllib.urlretrieve(y,fn2)
        i=i+1
        fn2=str(i)+fn
    os.chdir(os.path.pardir)
else:
    print u'Creating a new folder and downloading images'
    os.mkdir(getcwd()+r'\nav_item')
    mypath=getcwd()+r'\nav_item'
    os.chdir(mypath)
    for nav_li in nav_lis:
        y=nav_li.find_all('img')[0].get('src')[:-9]+'jpg'
        urllib.urlretrieve(y,fn2)
        i=i+1
        fn2=str(i)+fn
    os.chdir(os.path.pardir)
    
##fp.close()


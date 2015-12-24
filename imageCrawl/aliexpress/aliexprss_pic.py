#encoding=utf-8
#提取速卖通主页图片
##import sys
##reload(sys)
##sys.setdefaultencoding( "utf-8")
import urllib2,urllib
import os,re
from bs4 import BeautifulSoup
import subprocess
from os import getcwd,listdir
##调用casperjs来获取AJax内容
rawURL=raw_input('Pls input your aliexpress item url:  ')
# cmd= r'casperjs alpic.js --url='+url
##print cmd
#不用casperjs方式，渲染页面太慢。
# stdout,stderr=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
#改用正则获取回调地址
resp=urllib2.urlopen(rawURL)
html=resp.read()
soup1=BeautifulSoup(html,'html.parser',from_encoding='utf-8')
regr=re.compile(r'descUrl="(.*?)"')
url=re.findall(regr,html)[0]
#获取ajax回调内容
body=urllib2.urlopen(url).read()
soup=BeautifulSoup(body,'html.parser',from_encoding='utf-8')
#获取图片结果集
# g_data=soup.find_all('div',{'id':'custom-description'})
p_lists=soup.find_all('img')
# p_lists=filter(lambda x:x.has_attr('alt'),lists)
##创建文件存放位置

t_path='\\images'
#文件名
f_ex=r'.jpg'
f_init='0.jpg'
i=0
##下载图片

if os.path.exists(getcwd()+t_path):
    print u'原目录下载>>>>>>>>>>>>>>>>.'
    pass
else:
    print u'创建目录路径'
    os.mkdir(getcwd()+t_path)
    mypath=getcwd()+t_path
    os.chdir(mypath)
    for p_list in p_lists:
        x=p_list.get('src')
        urllib.urlretrieve(x,f_init)
        i=i+1
        print u'正在下载第'+str(i)+u'张图片'
        f_init=str(i)+f_ex
    os.chdir(os.path.pardir)

    
##下载文件头图片
nav_items=soup1.find_all('li',{'class':'image-nav-item'})
if os.path.exists(getcwd()+'\nav_pic'):
    pass
else:
    print u'创建nav_pic目录'
    os.mkdir(getcwd()+r'\nav_pic')
    mypath=getcwd()+r'\nav_pic'
    os.chdir(mypath)
    for nav_item in nav_items:
        y=nav_item.find_all('img')[0].get('src')[:-10]
        urllib.urlretrieve(y,f_init)
        i=i+1
        print u'正在下载第'+str(i)+u'张图片'
        f_init=str(i)+f_ex
os.chdir(os.path.pardir)

# #详情页介绍
# f=open('detail.html','w')
# f.write(str(g_data[0]))
# f.close()















# fp=open('html.txt','w')
# url='http://www.aliexpress.com/item/Luxury-Universal-Selfie-Stick-Monopod-for-Iphone-6-Plus-5s-Wired-Palo-Selfie-For-SAMSUNG-Android/32372569056.html'
# ##url='http://www.aliexpress.com/store/product/Hot-Sale-2015-New-Summer-Girl-Dress-Fashion-Printed-Dress-Baby-Girls-Dress-Cotton-Children-s/1328152_32315365720.html'
# req=urllib2.Request(url)
# res=urllib2.urlopen(req)
# re1=r'window.runParams.descUrl="(.*?)"'

# html=res.read()
# url1=re.findall(re1,html)
# url1=url1[0]
# req1=urllib2.Request(url1)
# res1=urllib2.urlopen(req1)
# con=res1.read()
# fw=fp.write(html)
# #print con
# re2=r'src="(.*?)"'
# con1=re.findall(re2,con)
# i=0
# fn='.jpg'
# fn1='0.jpg'
# for x in con1:
#     urllib.urlretrieve(x,'/dd/'+fn1)
#     i=i+1
#     fn1=str(i)+fn

# fp.close()

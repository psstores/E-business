#encoding=utf-8
import re
import os
from os import getcwd
import urllib
from bs4 import BeautifulSoup
import time
# url='https://www.wish.com/search/scooter#cid=55ff8599e768aa10f8c45af7'
f=open('temp.html','r')
html=f.read()
soup=BeautifulSoup(html,'html.parser',from_encoding='utf-8')
g_data=soup.find_all('div',{'class':re.compile("picture-wrapper")})
# tupianxiazai
f_ex=r'.jpg'	
f_init='0.jpg'
i=0
t_path=r'\images'
##for item in g_data:
##    link=item.find('img').get('src')
##    image_url=link.replace('-small.jpg','.jpg').replace('-tiny','.jpg')
##    print image_url
if os.path.exists(getcwd()+t_path):
    print u'此目录已经存在>>>>>>>>>>>>>>>>.'
    pass
else:
    print u'创建目录路径'
    os.mkdir(getcwd()+t_path)
    mypath=getcwd()+t_path
    os.chdir(mypath)
    for item in g_data:
        link=item.find('img').get('src')
        image_url=link.replace('small.jpg','').replace('tiny','')
        print image_url
        urllib.urlretrieve(image_url,f_init)
        i=i+1
        print u'正在下载第'+str(i)+u'张图片'
##        time.sleep()
        print 'time sleep for 3 sec'
        f_init=str(i)+f_ex
    os.chdir(os.path.pardir)
    print 'Download finished'
 

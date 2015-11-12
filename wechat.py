#encoding=utf-8
import csv
from bs4 import BeautifulSoup
import subprocess
import re
import chardet
import codecs
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
####def getContent():
cmd=r'casperjs D:\git\wechat.js'
print "cmd:",cmd
stdout,stderr=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
con=stdout.decode('gbk').encode('utf-8')
soup=BeautifulSoup(con,'html.parser',from_encoding='utf-8')
g_data=soup.find_all("div",{"class":"txt-box"})
print len(g_data)
for item in g_data:
    if item!=g_data[0]:
        try:
            title=((item.find("a",{"class":"news_lst_tab zhz"}).text).strip()).replace(',','，')
        except: 
            title='title'
        try:
            para=(item.find("p").text).strip()
        except:
            para='para'
        try:
             date=(item.find("div",{"class":"s-p"}).text).strip()
        except:
            date='date'
        try:
            link='http://weixin.sogou.com'+item.find("a",{"class":re.compile("tab")}).get('href')
        except:
            link='link'
        d=[title,para,date,link]
        with codecs.open('test.csv','a+','utf-8') as fd:
                           fd.write('\xEF\xBB\xBF')
                           write=csv.writer(fd,dialect='excel')
##                           write=csv.writer(fd,delimiter=' ')
                           write.writerow(d)
                           fd.close()
    else:
        pass
        
    
##    link=item.find("a",{"class":re.compile("tab")}).get('href')
    

	# for item in g_data:
# if __name__=='__main__':
# 	# url=raw_input('Pls input your weixinSogou URL:')
# 	getContent()

#encoding=utf-8
import csv
import sys
import MySQLdb
reload(sys)
sys.setdefaultencoding( "utf-8")
import codecs
import subprocess
import chardet
import time
import re
from bs4 import BeautifulSoup
def getDom(page):
            cmd=r'casperjs D:\ajax_render.js'+' --page='+page
            print "cmd",cmd
            stdout,stderr=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
            print stderr
            fp=open('html.txt','w')
            print u'第'+page+u'页'
            fp=open('html.txt','w')
            
            soup=BeautifulSoup(stdout,'html.parser',from_encoding="gb18030")
            g_data=soup.find_all("li",{"class":re.compile("^list-item")})
            
        
            print len(g_data)
            fp.write(stdout)
            fp.close()
            ##变量写入字典
            for item in g_data:
                     try:
                            title=(item.find('h3').text).strip()
                     except:
                            title='请检查'
                            
                    ##销量
                     try:
                            order=(item.find('span',{'class':'order-num'}).text).strip()
                     except:
                            order= '0'
                    ## price
                     try:
                            price=(item.find('span',{'class':'value notranslate'}).text).strip()
                     except:
                            price= '0'
                    ## unit
                     try:
                            unit=(item.find('span',{'class':'unit'}).text).strip()
                     except:
                            unit= '0'
                    ## unit
                     try:
                            storeId=(item.find('a',{'class':'store  notranslate'}).get('title')).strip()
                     except:
                            storeId= '请检查'
                    ## feedback
                     try:
                            feedback=(item.find('span',{'id':re.compile('score')}).get('feedbackscore')).strip()
                     except:
                            feedback= '0'
                    ## url
                     try:
                            url=(item.find('a').get('href')).strip()
                     except:
                            url= '0'
                   
                     d=[page,title,order,price+'/'+unit,storeId,feedback,url]
                     #write to csv
                     with codecs.open('aliexpress.csv','a+','utf-8') as fd:
                           fd.write('\xEF\xBB\xBF')
                           write=csv.writer(fd,dialect='excel')
                           write.writerow(d)
                           fd.close()
                     #write to mysql
        ##             conn=MySQLdb.connect(host='localhost',user='Jason',passwd='520205',db='jason',charset='utf8')
        ##             cursor=conn.cursor()
        ##             sql='insert into ali(com,deal,title,year,url) values(%s,%s,%s,%s,%s)'
        ##             param=d
        ##             n=cursor.execute(sql,param)
        ##             conn.commit()
        ##             print 'insert',n

##            cursor.close()
##            conn.close()
            print u'delay 2 second'
            time.sleep(2)
            
for page in range(1,21):
    page=str(page)                               
    getDom(page)  
    
##    order=(item.find('span',{'class':'order-num'}).text).strip()
##	price=(item.find('span',{'class':'value notranslate'}).text).strip()
##	unit=(item.find('span',{'class':'unit'}).text).strip()
##	storeId=(item.find('a',{'class':'store  notranslate'}).get('title'))
##	feedback=(item.find('span',{'id':re.compile('score')}).get('feedbackscore')).strip()
##	url=(item.find('a').get('href')).strip()

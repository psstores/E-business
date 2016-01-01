#encoding=utf-8
import urllib2
import requests
import re,codecs
import csv
from bs4 import BeautifulSoup
import sys
reload (sys)
sys.setdefaultencoding("utf-8")
rawURL=raw_input('pls input your url here: ')
# url=r'http://feedback.aliexpress.com/display/productEvaluation.htm?productId=32490750607&ownerMemberId=204960703&companyId=217397603&memberType=seller&startValidDate='
#POST方式获取拼了评论，所以这里要写入postdata
def getURL(rawURL=rawURL):
	res=urllib2.urlopen(rawURL)
	content=res.read()
	regr=re.compile(r'thesrc="(.*?)">')
	url1=re.findall(regr,content)[0]
	return url1
url=getURL(rawURL=rawURL)
def getFeedback(url=url,page=1):
	postdata={'page':str(page)}
	headers = {  
	    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'  
	} 
	# url=r'http://feedback.aliexpress.com/display/productEvaluation.htm?productId=32490750607&ownerMemberId=204960703&companyId=217397603&memberType=seller&startValidDate='
	r=requests.post(url=url,data=postdata,headers=headers)
	#BeautifulSoup 包提出评论
	soup=BeautifulSoup(r.text,'xml',from_encoding='utf-8')
	#定位要用获取数据的table
	soup_content=soup.find('table',{'class':re.compile('^rating-table')}).find('tbody')
	#获取table里面的数据集
	g_data=soup_content.find_all('tr')
	f=open('t.html','a')
	f.write(r.text)
	f.close()
	for item in g_data:
		print len(g_data)
		buyer=(item.find('td',{'class':'td3'}).find('span').text).strip()
		print buyer
		buyer_cou=re.split('_',(item.find('td',{'class':'td3'}).find('span').find('b').get('class')))[2].strip()
		print item.find('td',{'class':'td3'}).find('span').find('b').get('class')
		buyer_stat=re.split('-',(item.find('td',{'class':'td3'}).find_all('span')[1].find('i').get('class')))[4].strip()
		print buyer_stat
		product=(item.find('td',{'class':'td4'}).find('span').text).strip()
		print product
		unit=(item.find('td',{'class':'td4'}).find('div').text).strip()
		print unit
		star=re.split(':',(item.find('td',{'class':'td2'}).find('span').get('style')).strip())[1]
		print star
		time=(item.find('td',{'class':'td2'}).find('div',{'class':'feedback-date'}).text).strip()
		print time
		feedback=((item.find('td',{'class':'td2'}).find('div',{'class':'right feedback'}).text).strip()).encode('utf-8')
		# helpful=(item.find('td',{'class':'td2'}).find('div',{'class':'thf-digg'}).find('span',{'class':'thf-digg-useful'}).text).strip()
		data=[buyer,buyer_cou,buyer_stat,product,unit,star,time,feedback]
		with codecs.open('feedback.csv','a','utf-8') as csvfile:
			csvfile.write('\xEF\xBB\xBF')
			writer=csv.writer(csvfile,dialect='excel')
			writer.writerow(data)
		
def pgnum(url=url):
	postdata={}
	headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'} 
	r=requests.post(url=url,data=postdata,headers=headers)
	soup=BeautifulSoup(r.text,'xml',from_encoding='utf-8')
	g_content=int(soup.find('div',{'id':'pagination-top'}).find_all('a',{'href':re.compile('javascript:gotoPage')})[1].text)
	return g_content

if __name__=='__main__':
	print 
	num=pgnum(url=url)
	for i in range(num):
		getFeedback(url=url,page=i)
	print u'finished'

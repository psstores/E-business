#encoding=utf-8
import urllib,urllib2
import re
import json
from fixJson import fixLazyJsonWithComments
import csv
import codecs
import chardet
import sys
reload(sys)
sys.setdefaultencoding( "utf-8")
kw='python'
alibabaURL="http://connectkeyword.alibaba.com/lenoIframeJson.htm?iframe_delete=true&varname=intelSearchData&keyword="+kw+"&searchType=product_en&cateId=&cookieId=183.224.156.42.1445046104738.749831.1&buckettest=&callback=jQuery18305847417997301511_1450020260912&_=1450020340406"
aliexURL="http://connectkeyword.aliexpress.com/lenoIframeJson.htm?iframe_delete=true&varname=intelSearchData&__number=1&keyword="+kw+""
amazonURL="http://completion.amazon.com/search/complete?method=completion&mkt=1&client=amazon-search-ui&x=String&search-alias=aps&q="+kw+"&qs=&cf=1&noCacheIE=1450021966460&fb=1&sc=1&"
ebayURL="http://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw=scooter&_sacat=0"
googleURL="https://www.google.com.hk/complete/search?client=hp&hl=zh-CN&gs_rn=64&gs_ri=hp&tok=xzIOZZnQIDpu6XEDT3j1TA&cp=6&gs_id=22s&q="+kw+"&xhr=t"
urls=[
alibabaURL,
aliexURL,
amazonURL,
ebayURL,
googleURL
]
fieldnames = ['alibaba', 'aliexpress','amazon','google']
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'# 将user_agent写入头信息
headers={'User-Agent' : user_agent}
values = {}
def alibabaDropdown(url=urls[0],headers=headers,values=values):
	data = urllib.urlencode(values)
	req=urllib2.Request(urls[0],data,headers)
	response=urllib2.urlopen(req)
	content=response.read()
	#正则查找所要处理部分
	encodeJson=re.findall(re.compile('window.intelSearchData=(.*)'),content)[0][:-1]
	# j=encodeJson.replace('(','[').replace(')',']').replace('\'','"')
	#处理成符合json格式的数据
	j=fixLazyJsonWithComments(encodeJson)
	#还原数据为列表类型
	js_list=json.loads(j)
	return js_list
	#Json格式化输出
	# js_json=json.dumps(js_list,indent=4)
	# print js_json

def aliExDropdown(url=urls[1],headers=headers,values=values):
	data = urllib.urlencode(values)
	req=urllib2.Request(urls[1],data,headers)
	response=urllib2.urlopen(req)
	content=response.read()
	#去除多余的行\n,空格\t
	content=content.replace('\n','').replace('\t','')
	encodeJson=re.findall(re.compile('window.intelSearchData = (.*)'),content)[0][:-1]
	j=fixLazyJsonWithComments(encodeJson)
	js_list=json.loads(j)
	return js_list

def amazonDropdown(url=urls[2],headers=headers,values=values):
	data = urllib.urlencode(values)
	req=urllib2.Request(urls[2],data,headers)
	response=urllib2.urlopen(req)
	content=response.read()
	encodeJson=re.findall(re.compile('completion = (.*);String\(\);'),content)[0]
	# j=fixLazyJsonWithComments(encodeJson)
	js_list=json.loads(encodeJson)
	return js_list

def googleDropdown(url=urls[4],headers=headers,values=values):
	res=urllib2.urlopen(urls[4])
	content=res.read()
	# encodeJson=re.findall(re.compile('completion = (.*);String\(\);'),content)[0]
	j=fixLazyJsonWithComments(content)
	#check the encoding of j and decode it to unicode
	k=chardet.detect(j)
	j=j.decode(k['encoding'])
	js_list=json.loads(j)
	return js_list

def formatOnelist(a,b,c,d):
	aa=[i['keywords'] for i in a]
	bb=[i['keywords'] for i in b]
	cc=c[1]
	dd=[i[0] for i in d[1]]
	aaa=[{'alibaba':i} for i in aa]
	bbb=[{'aliexpress':i} for i in bb]
	ccc=[{'amazon':i} for i in cc]
	ddd=[{'google':i} for i in dd]
# 将4个列表字典合并为一个字典列表aaa。
	for i in range(len(ddd)):
			# ddd[i].update(aaa[i])
			ddd[i].update(bbb[i])
			ddd[i].update(ccc[i])
	return ddd
# 将结果写入csv文档中
def toCSV(data,fieldnames):
	with open('test.csv','ab+') as fd:
		fd.write('\xEF\xBB\xBF')
		writer=csv.DictWriter(fd,dialect='excel',fieldnames=fieldnames)
		writer.writeheader()
		for k in data:
			writer.writerow(k)
		fd.close()

if __name__=='__main__':

	a=alibabaDropdown()
	b=aliExDropdown()
	c=amazonDropdown()
	d=googleDropdown()
	allInOne=formatOnelist(a=a,b=b,c=c,d=d)
	toCSV(data=allInOne,fieldnames=fieldnames)




	
#encoding=utf-8
import csv
import json
import subprocess
import os 
import sys
import time
import sys
import re
reload(sys)
sys.setdefaultencoding( "utf-8")
from urllib import urlencode
from multiprocessing import Pool
curPath=os.path.abspath(sys.path[0])
q='%D7%D4%C5%C4%C9%F1%C6%F7'
base_url='http://s.1688.com/selloffer/offer_search.htm?'
t=time.strftime('%Y%m%d',time.localtime(time.time()))
urls=map(lambda num:base_url+urlencode({
 "keywords": q,
 "sug": "1_0", 
 "n": "y", 
 "filterP4pIds": "1201122244,521279035344,44905301557,44632737573,523778196750,524414222456,45304569184,523080670148", 
 "offset": "9", 
 "spm": "a260k.635.1998096057.d1#beginPage="+str(num)
}),[x for x in xrange(0,101)])
urls=map(lambda x:re.sub(r'%23',r'#',x),urls)
urls=map(lambda x:re.sub(r'%3D',r'=',x),urls)
urls=map(lambda x:re.sub(r'%25',r'%',x),urls)
# urls=['http://s.1688.com/selloffer/offer_search.htm?keywords=%D7%D4%C5%C4%C9%F1%C6%F7&sug=1_0&n=y&spm=a260k.635.1998096057.d1#beginPage=8&offset=9&filterP4pIds=1201122244,521279035344,44905301557,44632737573,523778196750,524414222456,45304569184,523080670148']
#代理
PROXY='--proxy=123.126.108.190:3128 '
def FUN(url):
	cmd=r'casperjs '+PROXY+curPath+'\\JS.js'+' --URL='+'"'+url+'"'
	# cmd=r'casperjs '+PROXY+curPath+'\\JS.js'
	print url
	stdout=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE).communicate()[0]
	# print stdout
	#这里转码输出为python识别的dict数据类型
	l=json.loads(stdout.decode('GBK',errors='ignore'))
	li=json.loads(l)
	print(li[0]['li_num'])
	with open('1688.csv','ab+') as f:
		fieldnames = ['page','title','price','deal','store_name','year','store_url','item_url','li_num']
		f.write('\xEF\xBB\xBF')
		writer = csv.DictWriter(f, fieldnames=fieldnames,dialect='excel')
		# writer.writeheader()
		map(lambda x:writer.writerow(x),li)
		f.close()
	# 	print 'closing f.csv'
def main():
	pool=Pool(processes=10)
	pool.map(FUN,urls)
	pool.close()
	pool.join()
	print('finished')

if __name__=="__main__":
	main()
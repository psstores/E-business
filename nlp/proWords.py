#encoding=utf-8
import nltk
import json
from nltk import FreqDist
import csv
import re
with open('keywords.csv','rb') as csvfile:
	reader=csv.reader(csvfile)
	#读取标题列
	rows=[row[1] for row in reader]
	csvfile.close()
#标题组合
t=str(rows).replace('[','').replace(']','').replace("'",'').replace("'",'').replace(",",'').replace("\\n",' ')
t2=nltk.word_tokenize(t)
f1=FreqDist(t2)
f2=sorted(f1)
#pair出关键词
f3=[{i:f1[i]} for i in f1.keys() if len(i)>1]
#排序
f3=sorted(f3,key=lambda x:x.values()[0],reverse=True)
f_out=[i.items()[0] for i in f3]
#写入txt
f=open('test.txt','w')
for i in f_out:
	f.write(i[0]+'\t'+str(i[1])+'\n')
f.close()

# ss=n_gram(keyword='which',text=content,direction=0,num=2)
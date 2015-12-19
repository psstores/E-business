#encoding=utf-8
import nltk
import json
from nltk import FreqDist
import csv
import re
def n_gram(keyword,text,direction=1,num=2):
	keyword=keyword
	num=num
	direction=direction

	if direction==1:
		reg=keyword+'\s.*?'*num
	elif direction==0:
		reg='\S*\W*'*num+keyword
	text=str(text).replace('[','').replace(']','').replace("'",'').replace("'",'').replace(",",'').replace("\\n",' ')
	s=re.findall(reg,text)
	ss=FreqDist(s)
	f3=[{i:ss[i]} for i in ss.keys() if len(i)>1]
	f3=sorted(f3,key=lambda x:x.values()[0],reverse=True) 
	f_out=[i.items()[0] for i in f3]
	#写入txt
	f=open('n_gram.txt','a+')
	for i in f_out:
		f.write(i[0]+'\t'+str(i[1])+'\n')
	f.close()
	return ss
def readCSV():
	with open('keywords.csv','rb+') as csvfile:
		reader=csv.reader(csvfile)
		rows=[row[1] for row in reader]
		csvfile.close()
	return rows

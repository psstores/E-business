#encoding=utf-8
from nlp import n_gram,readCSV
import csv
text=readCSV()
keyword=raw_input('please input your keywords:')
direction=int(raw_input('1+,0-:'))
num=int(raw_input('number:'))
n_gram(keyword=keyword,text=text,direction=direction,num=num)
print 'finished'
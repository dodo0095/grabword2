import csv
with open('在家自學全資料.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    column = [row[1] for row in reader]
print (column)
import json
import requests
column=str(column)
from snownlp import SnowNLP
s = SnowNLP(column)
import jieba
dic={}
for ele in jieba.cut(column):
    if ele not in dic:
        dic[ele]=1
    else:
        dic[ele]=dic[ele]+1
        import operator
sorted_word = sorted(dic.items(),key=operator.itemgetter(1),reverse=True)
for ele in sorted_word:
    if len(ele[0])>=2:
        print (ele[0],ele[1])
# -*- coding: utf-8 -*-

import pymysql
import xlwt

from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

book = xlwt.Workbook(encoding='utf-8', style_compression=0)
conn=pymysql.connect(host="localhost",port=3306,user="root",passwd="scholar@2016",db="test",charset='utf8')
cur=conn.cursor()
years=['07','08','09','10','11','12','13','14','15','16','17']
jnums=['J01','J02','J03','J04','J05','J06','J07','J08','J09','J10','J11','J12']
for yr in years:
	ats=[]
	year="20"+yr
	print year +"--------------"
	sheet = book.add_sheet(year, cell_overwrite_ok=True)
	for jn in jnums:
		sqlstr='select text from jtext where j_num=%s and year=%s'
		print sqlstr
		cur.execute(sqlstr,(jn,year))
		at=cur.fetchall()
		jat=''
		for tt in at:
			#print "tt=------"
			#print tt
			jat=jat+ tt[0] +" "
		#print jat
		ats.append(jat)
	rs=ats
	print "---------len(rs)= " + str(len(rs))
	vectorizer = CountVectorizer()  # 该类会将文本中的词语转换为词频矩阵，矩阵元素a[i][j] 表示j词在i类文本下的词频
	transformer = TfidfTransformer()  # 该类会统计每个词语的tf-idf权值
	tfidf = transformer.fit_transform(
		vectorizer.fit_transform(rs))  # 第一个fit_transform是计算tf-idf，第二个fit_transform是将文本转为词频矩阵
	word = vectorizer.get_feature_names()  # 获取词袋模型中的所有词语
	weight = tfidf.toarray()  # 将tf-idf矩阵抽取出来，元素a[i][j]表示j词在i类文本中的tf-idf权重
	p=1
	for i in range(len(weight)):  # 打印每类文本的tf-idf词语权重，第一个for遍历所有文本，第二个for便利某一类文本下的词语权重
		sheet.write(0,p,"J"+str(i))
		sheet.write(0,p,'tfidf')
		k=1
		dict={}
		for j in range(len(word)):
			if weight[i][j]>0:
				dict[word[j]]=weight[i][j] #将结果放在一个字典中
				#print word[j],weight[i][j]
		sortres = sorted(dict.items(), key=lambda item: item[1], reverse=True) # sort the dict
		for key in sortres:
			sheet.write(k, p, key[0])
			sheet.write(k, p+1, key[1])
			k=k+1
		p=p+3

# 最后，将以上操作保存到指定的Excel文件中
book.save("./data/tfidf-byyear.xls")
#book.save(r"E:\edu_data\datatfidf-total.xls")
#f02.close()
print "done!------------------------"
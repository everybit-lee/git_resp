# -*- coding: utf-8 -*-

'''
Created on 20171115
将作者信息提取出来。
原始数据中，作者是混杂在一起的
@author: Liyuyao
'''

#import nltk
import pymysql
import xlsxwriter   #xlwt
import pandas as pd
import collections

conn=pymysql.connect(host="localhost",port=3306,user="root",passwd="123456",db="bibanalyse",charset='utf8')
cur=conn.cursor()

sqlstr='select a_num,j_num,author from bib'
cur.execute(sqlstr)
rs=cur.fetchall()
if rs:
    auths=[]
    for res in rs:
        aa=res[2].split('and') #先将最后一个取出来
        for k in aa:
            k=k.strip()  #消去前后空格
            auths.append(k)
    na=[]
    pre=auths[0]
    nw=''
    for n in range(0,len(auths)):
        if n>0:
            nw=auths[n]

# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 09:33:58 2016

@author: Administrator
"""
import pymysql
conn=pymysql.connect(host='localhost',port=3306,user='root',passwd='123456',db='paper3',charset='utf8')
cur=conn.cursor()
cur.executemany("insert into authors(aname) values(%s)",["test01","test02"])
conn.commit()
conn.close()
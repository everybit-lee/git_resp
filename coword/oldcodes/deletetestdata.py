# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 15:29:48 2016

@author: Administrator
"""
# 删除数据库中的测试数据
import pymysql  
import json
import urllib.request
from builtins import int  
import os
  
#将MysqlHelper的几个函数写出来  
  
def  connDB():                              #连接数据库  
    conn=pymysql.connect(host="localhost",port=3306,user="root",passwd="123456",db="paper3",charset='utf8');  
    cur=conn.cursor();  
    return (conn,cur);  
  
def exeUpdate(conn,cur,sql):                #更新或插入操作  
    sta=cur.execute(sql);  
    conn.commit();  
    return (sta);  
  
def exeDelete(conn,cur,IDs):                #删除操作  
    sta=0;  
    for eachID in IDs.split(' '):  
        sta+=cur.execute("delete from students where Id=%d"%(int(eachID)));  
    conn.commit();  
    return (sta);  
          
def exeQuery(cur,sql):                      #查找操作  
    cur.execute(sql);  
    return (cur);  
      
def connClose(conn,cur):                    #关闭连接，释放资源  
    cur.close();  
    conn.close();  

#########################下面开始事务操作##############

conn,cur=connDB()

sqlstr='DELETE FROM paper'
cur.execute(sqlstr)
conn.commit()
print('DELETE * from paper')

sqlstr='DELETE FROM authors'
cur.execute(sqlstr)
conn.commit()
print('DELETE * from authors')

sqlstr='DELETE FROM p_a'
cur.execute(sqlstr)
conn.commit()
print('DELETE * from p_a')

sqlstr='DELETE FROM keywords'
cur.execute(sqlstr)
conn.commit()
print('DELETE * from keywords')

sqlstr='DELETE FROM p_kw'
cur.execute(sqlstr)
conn.commit()
print('DELETE * from p_kw')


connClose(conn,cur)

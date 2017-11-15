# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 10:17:58 2017

@author: Administrator
"""
import pymysql 
import igraph 
#将MysqlHelper的几个函数写出来  
  
def  connDB():                              #连接数据库  
    conn=pymysql.connect(host="localhost",port=3306,user="root",passwd="123456",db="wf",charset='utf8');  
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
g=Graph()


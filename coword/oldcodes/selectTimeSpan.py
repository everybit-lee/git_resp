# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 14:53:04 2016

@author: Administrator
"""
import pymysql

conn=pymysql.connect(host="localhost",port=3306,user="root",passwd="123456",db="paper2",charset='utf8');  
cur=conn.cursor();  
f=open('aulog.txt','w+')
cur.execute('SELECT * FROM team_auth')
rs=cur.fetchall()

getT={
      '1997_1999':'T1',
      '2000_2002':'T2',
      '2003_2005':'T3',
      '2006_2008':'T4',
      '2009_2011':'T5',
      '2012_2014':'T6'
      }
        

for r in rs:
    if r[0] in getT:
        #print(getT.get(r[0]))
        Ts=getT.get(r[0])
        if (r[1]=='-' and r[2] is not None):
            tmp=r[5] + r[0] + '_' + r[2]
            t='state1'
        elif (r[1]!='-' and r[2] is not None):
            tmp=r[5] + r[0] + r[1] + r[2] + '_' 
            t='state2'
        elif (r[1]=='-' and r[2] is None):
            tmp=r[5] + r[0] + '_'
            t='state3'
        tid=r[3][len(tmp):len(r[3])]
        #print(tid)
        sqlstr='INSERT INTO TeamByTime(Tspan,rank,field,team_id,a_id,lang) VALUES(%s,%s,%s,%s,%s,%s)'
        cur.execute(sqlstr,(Ts,r[1],r[2],tid,r[4],r[5]))
        conn.commit()
        f.write(Ts + '--' + tid + '--' + r[4] + '----- ' + t +'  ---------' + tmp + '\n')
    #print(t1,t2)
    #print(r[0])
    #break
    
conn.close()
f.close()
print('Done!')
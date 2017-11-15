# -*- coding: utf-8 -*-
"""
Created on 20170616
  重新计算KR
数据来源：
mb_dg_nr_membercount： 从中获得团队个数
mb_dg_nr_order6 从中获得每个团队的详细情况
目标数据库：
rate1_kr_nr

@author: Administrator
"""
from __future__ import division
import pymysql

conn=pymysql.connect(host="localhost",port=3306,user="lyy",passwd="123456",db="paper2",charset='utf8');
cur=conn.cursor();
f=open("compuKR.txt","w+")
re_k=0.36
re_t1=14
re_t2=73
#从mb_dg_nr_membercount中获得时间片对中，两两进行比对。
for i in range(1,3):
    ts1="T"+str(i)
    ts2 = "T" + str(i+1)
    for j in range(2,11):
        area = "A"
        if len(str(j)) < 2:
            area = area + "0" + str(j)
        else:
            area = area + str(j)
        cur.execute("select * from mb_dg_nr_membercount where ts=%s and field=%s order by ts,field,membership",(ts1,area))
        t1teams=cur.fetchall()
        for t1team in t1teams: #对每个t1team，循环，查找t2team 中的数据，其中t2team 是只用ts而不管field的，即跨field查找
            cur.execute("select * from mb_dg_nr_membercount where ts=%s and field=%s order by ts, field, membership", (ts2,area)) #对所有ts2 的团队进行查找
            t2teams = cur.fetchall() # 获得每一个t2team ，在每一个比例下比较
            if re_t1 > 0:
                if t1team[2] < re_t1 - 1:  #
                    print("t1team[2]&re_tl=" + str(t1team[2]) + "<--->" + str(re_t1))
                    continue
                else:
                    re_t1 = 0
            else:
                if re_k>0:
                    k=re_k
                else:
                    re_k=0
                    k=0.1
                list = []
                while k<=0.41:
                    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++k="+str(k))
                    rr = "r" + str(int(k * 100))
                    #RR="R"+str(k)
                    sqlstr="select count(author_id) from mb_dg_nr_order6 where ts=%s and field=%s and membership=%s and "+rr+">0"

                    cur.execute(sqlstr, (ts1,area,t1team[2])) #计算特定t1团队中人数
                    countt1t=cur.fetchall()
                    if countt1t[0][0]>0:
                        for t2team in t2teams:
                            print("ts1="+str(ts1)+"--area="+area+"---Mbs="+str(t1team[2])+"---ts2="+str(ts2)+"--area="+area+"---Mbs="+str(t2team[2])+"\t")
                            sqlstr="select id,author_id from mb_dg_nr_order6 as a where a.ts=%s and a.field=%s and a.membership=%s and a."+rr+">0 and a.author_id in (select author_id from mb_dg_nr_order6 as b where b.ts=%s and b.field=%s and b.membership=%s and b."+rr+">0)"
                            if re_t2>0:
                                if t2team[2]<re_t2-1:
                                    print("t2team[2]&re_t2=" + str(t2team[2]) +"<===>" + str(re_t2))
                                    continue
                                else:
                                    re_t2=0
                            else:
                                cur.execute(sqlstr,(ts1,area,t1team[2],ts2,area,t2team[2]))
                                res=cur.fetchall() #接下来对res进行判断。如果不为空，则将对应的信息进行拆分，装入rate_kr_nr表中
                                print("len(res)="+str(len(res)))
                                if len(res)>0:
                                    rfloat = len(res) / countt1t[0][0]
                                    if t2team[2] in list:
                                        sqlstr = "update rate1_kr_nr set " + rr + "=%s where Tspan=%s and Area=%s and T1=%s and T2=%s"
                                        cur.execute(sqlstr, (rfloat,ts2, area, t1team[2], t2team[2]))
                                        conn.commit()
                                        #list.append(t2team[2])
                                        print("update----Tspan=" + ts2 + "---area=" + area + "---T1=" + str(t1team[2]) + "---T2=" + str(
                                            t2team[2]) + "---rfloat=" + str(rfloat))
                                        f.write("update----Tspan=" + ts2 + "---area=" + area + "---T1=" + str(t1team[2]).decode(
                                            "utf-8") + "---T2=" + str(t2team[2]).decode("utf-8") + "---rfloat=" + str(
                                            rfloat).decode("utf-8") + "\n")
                                    else:
                                        sqlstr="insert into rate1_kr_nr(Tspan,Area,T1,T2," + rr + ") values(%s,%s,%s,%s,%s)"
                                        cur.execute(sqlstr,(ts2,area,t1team[2],t2team[2],rfloat))
                                        conn.commit()
                                        list.append(t2team[2])
                                        print("insert----Tspan="+ts2+"---area="+area+"---T1="+str(t1team[2])+"---T2="+str(t2team[2])+"---rfloat="+str(rfloat))
                                        f.write("insert----Tspan="+ts2+"---area="+area+"---T1="+str(t1team[2]).decode("utf-8")+"---T2="+str(t2team[2]).decode("utf-8")+"---rfloat="+str(rfloat).decode("utf-8")+"\n")
                    k=k+0.01



conn.close()
f.close()
print("=================Done!======================")
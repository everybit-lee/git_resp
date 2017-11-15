# -*- coding: utf-8 -*-

'''
Created on 20171115
将作者信息提取出来。
原始数据中，作者是混杂在一起的
@author: Liyuyao
'''

#import nltk
import pymysql
#import xlsxwriter   #xlwt
#import pandas as pd
#import collections

conn=pymysql.connect(host="localhost",port=3306,user="root",passwd="123456",db="bibanalyse",charset='utf8')
cur=conn.cursor()
#f01=open('tmp.txt','w')
sqlstr='select a_num,j_num,author from bib'#' where a_num=%s'
cur.execute(sqlstr)#,'A_5858')
rs=cur.fetchall()
if rs:

    for res in rs:
        #f01.write('\n')
        #f01.write('原始值=')
        #f01.write(str(res))
        #print '原始值========================================================='
        #print res
        aa=res[2].split(' and ') #先将最后一个取出来
        #print '分离and=========='
        #print aa
        auths = []
        for k in aa:
            k=k.strip()  #消去前后空格
            print k
            auths.append(k)
        na = []#
        if len(auths)>1:  #大于2个元素才需要做特殊处理
            #print "=======手术中。。。消去空格后============"
            #print auths
            ka=auths[0].split(',')  #对第一个元素进行分离,kk是一个列表
            kk=[]
            for kb in ka:
                tk=kb.strip()
                kk.append(tk)
            #print '需要处理的列表kk======'
            #print(kk)
            pre=''
            nw=''
            for n in range(0,len(kk)):   #将结尾是句号的字符跟前一个字符串合并为一个
                #print '进入循环了：--->'+str(n)
                na.append(kk[n])#print auths[n]
                #print '当前--->' + str(kk[n])
                if n>0 and ((len(kk[n])<3 and kk[n][-1]=='.') or (kk[n][-4]=='.')):
                    nw=pre + ', ' + kk[n]
                    del na[len(na)-1]
                    del na[len(na) - 1]
                    na.append(nw)
                    #print(nw)
                elif n==0:
                    pre=kk[0]
                else:
                    pre=kk[n-1]
            na.append(auths[len(auths) - 1])
            #print '对比一下------'
            #print kk

        else:
            na=auths
        #f01.write('\n')
        #f01.write('结果----------------------')
        #f01.write(str(na))

        sqlstr='insert into authors(an,jn,name) VALUES(%s,%s,%s)'
        for name in na:
            cur.execute(sqlstr,(res[0],res[1],name))
            conn.commit()
print 'done!'
#f01.close()
conn.close()
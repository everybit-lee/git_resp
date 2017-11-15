# -*- coding: utf-8 -*-
'''
Created on 20171108
从数据库读取数据，统计词频并计算高频词同现矩阵
@author: Liyuyao
'''

#import nltk
import pymysql
import xlsxwriter   #xlwt
import pandas as pd
import collections

conn=pymysql.connect(host="localhost",port=3306,user="root",passwd="scholar@2016",db="test",charset='utf8')
cur=conn.cursor()
writer=pd.ExcelWriter('./data/comat4_6_50.xlsx',engine='xlsxwriter')
#book = xlwt.Workbook(encoding='utf-8', style_compression=0)
wfreq=50 #高频词频率
for a in ("04","05","06"):
    jnum="J" + a  #获得期刊编号    
    sqlstr="select text from jtext where j_num=%s"# and year=%s"    
    cur.execute(sqlstr,jnum)#,yr))
    rs=cur.fetchall()
    if rs:
        txts=''
        for res in rs:
            txts=txts + res[0] + ' '  #获得该期刊的所有数据
        #print txts
        kd=collections.Counter(txts.split()) #计词频
        countres=sorted(kd.items(), key=lambda item:item[1],reverse=True) #得到排序后的词频结果
        df=pd.DataFrame(countres,columns=['words','freq']) #数据源：字典countres,行标记
        df.to_excel(writer,sheet_name=jnum) # jnum是这张表的名字
        writer.save()
        print "写入词频xlsx..."+ jnum
#---------------计算高频词矩阵,词频高于wfreq的词		
        highfreqwd=[]
        for items in countres:  #将词频写入文件
            #print items+ "-->" + str(countres[items])
            #sheet.write(i,1, items[0])
            #sheet.write(i,2, items[1])
            if items[1]>wfreq: #获得词频高于100的词
                highfreqwd.append(items[0])
            #i=i+1
        #p=p+3 #原来用来控制第几列，跟j一起的
		
#---------------计算高频词矩阵
        wcl=len(highfreqwd)
        print jnum + "-----计算高频词矩阵，共有高频词个数：" + str(wcl)
        comat=[[0 for col in range(wcl)] for row in range(wcl)] #定义一个全零的二维列表
        tlist=txts.split()
        for colindex in range(wcl):
            for rowindex in range(wcl):
                conum=0
                for tt in tlist:                    
                    if highfreqwd[colindex] in tt and highfreqwd[rowindex] in tt and highfreqwd[colindex]!=highfreqwd[rowindex]:
                        conum=conum+1
                comat[colindex][rowindex]=conum
                if conum>20:
                    print highfreqwd[colindex] + "--" + str(colindex) + "--" + highfreqwd[rowindex]+"--" +str(rowindex) + "-----" +str(conum)        
        df=pd.DataFrame(comat,columns=highfreqwd)
        df.to_excel(writer,sheet_name=jnum+"_highreqmat") #写入高频词矩阵		
        writer.save()
        print "写入高频词矩阵xlsx..."+ jnum+"_highreqmat"
		
conn.close()


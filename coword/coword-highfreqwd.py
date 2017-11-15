# -*- coding: utf-8 -*-
'''
Created on 20171108
从数据库读取数据，统计词频并计算高频词同现矩阵
@author: Liyuyao
'''

# import nltk
import pymysql
import xlsxwriter  # xlwt
import pandas as pd
import collections

conn = pymysql.connect(host="localhost", port=3306, user="root", passwd="scholar@2016", db="test", charset='utf8')
cur = conn.cursor()
writer = pd.ExcelWriter('./data/comat_highfreqwd.xlsx', engine='xlsxwriter')
# book = xlwt.Workbook(encoding='utf-8', style_compression=0)
wfreq = 100  # 高频词频率
for a in ('01', '02', '03', "04", "05", "06", "07", "08", "09", "10", "11", "12"):
    jnum = "J" + a  # 获得期刊编号
    sqlstr = "select text from jtext where j_num=%s"  # and year=%s"
    cur.execute(sqlstr, jnum)  # ,yr))
    rs = cur.fetchall()
    if rs:
        txts = ''
        for res in rs:
            txts = txts + res[0] + ' '  # 获得该期刊的所有数据
        # print txts
        kd = collections.Counter(txts.split())  # 计词频
        countres = sorted(kd.items(), key=lambda item: item[1], reverse=True)  # 得到排序后的词频结果
        #df = pd.DataFrame(countres, columns=['words', 'freq'])  # 数据源：字典countres,行标记
        #df.to_excel(writer, sheet_name=jnum)  # jnum是这张表的名字
        print "写入词频xlsx..." + jnum
# ---------------计算高频词矩阵,词频高于wfreq的词
        orihighfreqwd = []
        for items in countres:  # 将词频写入文件
            # print items+ "-->" + str(countres[items])
            # sheet.write(i,1, items[0])
            # sheet.write(i,2, items[1])
            if items[1] > wfreq:  # 获得词频高于100的词
                orihighfreqwd.append(items[0])
        sbwd=orihighfreqwd
# ---------------压缩高频词矩阵
        for tmpi in range(0, len(orihighfreqwd) - 1):
            for tmpj in range(tmpi + 1, len(orihighfreqwd)):
                if len(orihighfreqwd[tmpi]) > len(orihighfreqwd[tmpj]):
                    if orihighfreqwd[tmpi][0:len(orihighfreqwd[tmpj]) - 1] == orihighfreqwd[tmpj][0:-1]:
                        orihighfreqwd[tmpi] = "****"  # 将长的字符串设为****，以便过滤
                else:
                    if orihighfreqwd[tmpj][0:len(orihighfreqwd[tmpi]) - 1] == orihighfreqwd[tmpi][0:-1]:
                        orihighfreqwd[tmpj] = "****"  # 将长的字符串设为****，以便过滤

        highfreqwd=[]		
        highfreqwd = [orihighfreqwd,sbwd]

        df = pd.DataFrame(highfreqwd)
        df.to_excel(writer, sheet_name=jnum + "_highreqmat")  # 写入高频词矩阵
        #writer.save()
        print "写入高频词矩阵xlsx..." + jnum + "_highreqmat"
writer.save()
conn.close()


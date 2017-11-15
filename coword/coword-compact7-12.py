# -*- coding: utf-8 -*-
'''
Created on 20171108
从数据库读取数据，统计词频并计算高频词同现矩阵;
对高频词矩阵进行了压缩：将相同词根的高频词视为同一个词，比如learn和learner
for i in range(0,高频词矩阵长度-1)
	for j in range(i,高频词矩阵长度)
		if len(highfreqwd[i])>len(highfreqwd[j]): #如果i词的长度比j词的要大, 
			if i词与j词同根   #将同根的长词设为****;这里用字符串匹配方法
				将i词设为"***"
		else #如果j词的长度比i词的要大
@author: Liyuyao
'''

# import nltk
import pymysql
import xlsxwriter  # xlwt
import pandas as pd
import collections

conn = pymysql.connect(host="localhost", port=3306, user="root", passwd="scholar@2016", db="test", charset='utf8')
cur = conn.cursor()
writer = pd.ExcelWriter('./data/real_comat7_12_50.xlsx', engine='xlsxwriter')
# book = xlwt.Workbook(encoding='utf-8', style_compression=0)
wfreq = 50  # 高频词频率
for a in ("07", "08", "09", "10", "11", "12"):
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
        df = pd.DataFrame(countres, columns=['words', 'freq'])  # 数据源：字典countres,行标记
        df.to_excel(writer, sheet_name=jnum)  # jnum是这张表的名字
        # writer.save()
        print "写入词频xlsx..." + jnum
        # ---------------计算高频词矩阵,词频高于wfreq的词
        orihighfreqwd = []
        for items in countres:  # 将词频写入文件
            if items[1] > wfreq:  # 获得词频高于100的词
                orihighfreqwd.append(items[0])
                
# ---------------压缩高频词矩阵        
        for tmpi in range(0, len(orihighfreqwd) - 1):
            for tmpj in range(tmpi + 1, len(orihighfreqwd)):
                if len(orihighfreqwd[tmpi]) > len(orihighfreqwd[tmpj]):
                    if orihighfreqwd[tmpi][0:len(orihighfreqwd[tmpj]) - 1] == orihighfreqwd[tmpj][0:-1]:
                        orihighfreqwd[tmpi] = "****"  # 将长的字符串设为****，以便过滤
                else:
                    if orihighfreqwd[tmpj][0:len(orihighfreqwd[tmpi]) - 1] == orihighfreqwd[tmpi][0:-1]:
                        orihighfreqwd[tmpj] = "****"  # 将长的字符串设为****，以便过滤
        highfreqwd = []
        for tt in orihighfreqwd:
            if tt <> "****":
                highfreqwd.append(tt)

        print "highfreq-word / Compacted highfreq words =" + str(len(orihighfreqwd)) + "<--->" + str(
            len(highfreqwd))
# ---------------压缩高频词矩阵

# ---------------计算高频词矩阵
        wcl = len(highfreqwd)
        print jnum + "-----计算高频词矩阵，共有高频词个数：" + str(wcl)
        comat = [[0 for col in range(wcl)] for row in range(wcl)]  # 定义一个全零的二维列表
        tlist = txts.split()
        for colindex in range(wcl):
            for rowindex in range(wcl):
                conum = 0
                for tt in tlist:
                    if highfreqwd[colindex] in tt and highfreqwd[rowindex] in tt and highfreqwd[colindex] != highfreqwd[
                        rowindex]:
                        conum = conum + 1
                comat[colindex][rowindex] = conum
                if conum > 20:
                    print highfreqwd[colindex] + "--" + str(colindex) + "--" + highfreqwd[rowindex] + "--" + str(
                        rowindex) + "-----" + str(conum)
        df = pd.DataFrame(comat, columns=highfreqwd)
        df.to_excel(writer, sheet_name=jnum + "_highreqmat")  # 写入高频词矩阵
        # writer.save()
        print "写入高频词矩阵xlsx..." + jnum + "_highreqmat"
writer.save()
conn.close()


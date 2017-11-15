# -*- coding: utf-8 -*-
"""
Created on 20171009
  将computer and education中的引用数据提取出来制作词云
@author: Administrator
"""


f01=open("E://tmp//education and trends.txt","r")
f02=open("E://tmp//e-t-ti-ab.txt","w+")


ti=False
ab=False
wr=False
st=""
for line in f01.readlines():
    print line[0:2]
    print line[3:-1]
    if len(line)==0:   #空行，打印，并在文本中输出一个空行
        print("A new record...............")
        f02.write("\n")
        ti = False
        ab = False
    elif line[0:2]=="TI" or line[0:2]=="AB":#否则判断是标题还是摘要，注意换行问题
        if line[0:2]=="TI":
            ti=True
        if line[0:2]=="AB":
            ab=True
        st = line[3:len(line)-1]
    elif line[0:2]=='  ':
        st=st + " " + line[3:len(line)-1]
        wr=True
    elif wr and (line[0:2]!='  ' or line[0:2]!="TI" or line[0:2]!="AB"):
        ti=False
        ab=False
        wr=False
        f02.write(st)
        f02.write("\n")
        f02.write("\n")



f01.close()
f02.close()
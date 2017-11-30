# -*- coding: utf-8 -*-
"""
Created on 20171120 用pandas读取excel中的矩阵数据

@author: Administrator
"""
import pandas as pd
import numpy as np
import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist
from sklearn import metrics

font = FontProperties(fname="/usr/share/fonts/truetype/droid/DroidSansFallbackFull.ttf", size=10)
xlsx = pd.ExcelFile('./data/selectdata.xlsx')
pngfile = "./data/"
# filerange=[100,200,500,1000,1500,2000]
filerange = [1000]
for st in filerange:
    sheetname = "n3-" + str(st)  # 1586个kw
    df = pd.read_excel(xlsx, sheetname, index_col=0)
    # 1 = np.array([1, 2, 3, 1, 5, 6, 5, 5, 6, 7, 8, 9, 7, 9])
    # x2 = np.array([1, 3, 2, 2, 8, 6, 7, 6, 7, 1, 2, 1, 1, 3])
    # X=np.array(list(zip(x1,x2))).reshape(len(x1),2)  #转置为14行2列
    kw = []
    for wd in df.index:
        kw.append(wd)  # 用kw接收所有词
    nf = df.values  # 转换为numpy adarray
    print "length of kw=" + str(len(kw))
    print kw
    plt.figure()
    plt.axis([0, nf.shape[0], 0, 1])  # 用最大行数，即最大词数，作为数轴横轴
    plt.grid(True)
    plt.title(u'Determining the best K value with the elbow rule', fontproperties=font)
    # plt.plot(nf,'k.')
    ax1 = plt.subplot(122, projection='polar')
    ax2 = plt.subplot(121)
    ax1.plot(nf, '.', lw=2)
    plt.title(u'polar coordinates', fontproperties=font)
    ax2.plot(nf, '.', lw=2)
    plt.title(u'Cartesian coordinates', fontproperties=font)
    svgfile = pngfile + "polar01" + str(st) + ".svg"
    plt.savefig(svgfile)
    pngfile = "./data/"

# ===============肘部法确定
# font = FontProperties(fname=r"c:\windows\fonts\msyh.ttc", size=10)

K = range(2, 20)
meandistortions = []
for k in K:
    # print "k=" + str(k)
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(nf)
    # print kmeans.cluster_centers_
    meandistortions.append(sum(np.min(cdist(
        nf, kmeans.cluster_centers_, "euclidean"), axis=1)) / nf.shape[0])
# tmpb = np.zeros((11,len(meandistortions)), dtype=nf.dtype)  # 生成(11,n) 矩阵
# tmpb=np.vstack((meandistortions,tmpb)).T  #向下扩展，然后转置为（n，12）的矩阵
# tmpa=np.zeros((nf.shape[0]-len(meandistortions),12),dtype=nf.dtype) #生成缺少的剩余数据
# tmpb=np.vstack((tmpb,tmpa)) #向下扩展，得到需要的尺寸的矩阵
    plt.figure()
    plt.plot(K, meandistortions, 'bx-')
    plt.xlabel('k')
    plt.ylabel(u'The average degree of distortion', fontproperties=font)  # 平均畸变程度
    plt.title(u'Determining the best K value with the elbow rule', fontproperties=font)  # 用肘部法则来确定最佳的K值
    svgfile = pngfile + "polar02" + str(st) + ".svg"
    plt.savefig(svgfile)
    # plt.show()
    pngfile = "./data/"

f01 = open("./data/kmeans_models.txt", "w+")
# ========肘部附近几个值展示
# plt.figure(figsize=(8, 10))
plt.subplot(431, polar=True)
plt.xlim([0, nf.shape[0]])
plt.ylim([0, 1])
# plt.scatter(nf)
plt.plot(nf, 'k.')
plt.title(u'Sample', fontproperties=font)
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'b']
markers = ['o', 's', 'D', 'v', '^', 'p', '*', '+']
tests = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]  # 肘部附近的值
subplot_counter = 1
for t in tests:
    f01.write("t=" + str(t) + "\n")
    subplot_counter += 1
    tmp = 430 + subplot_counter
    plt.subplot(tmp, polar=True)
    kmeans_model = KMeans(n_clusters=t).fit(nf)
    # print kmeans_model.labels_
    for m in range(0, len(kw)):
        print kw[m]
        print kmeans_model.labels_[m]
        if not isinstance(kw[m], float):
            f01.write(kw[m] + "," + str(kmeans_model.labels_[m]) + "\n")  # 每行输出单词及分类号
            # 每个点对应的标签值
    for i, l in enumerate(kmeans_model.labels_):
        print "--->  i=" + str(i) + "---> l= " + str(l) + "  <---"
        l = l % 8
        plt.plot(nf, color=colors[l],  # 这里x1[i],x2[i] 是分系列的值？如何跟nf对应？
                 marker=markers[l], ls='None')
        plt.xlim([0, nf.shape[0]])
        plt.ylim([0, 1])
        plt.title(u'K = %s, Silhouette_Score = %.03f' %
                  (t, metrics.silhouette_score
                  (nf, kmeans_model.labels_, metric='euclidean'))
                  , fontproperties=font)
svgfile = pngfile + "polar03" + str(st) + ".svg"
plt.savefig(svgfile)
# plt.show()

print "---------------Done!-------------"

f01.close()

# ====================================
'''
import pymysql
import json
import pandas as pd
import numpy as np
import xlrd
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.cluster import KMeans
import sklearn as sk

#%matplotlib inline
xlsx=pd.ExcelFile('..\\data\\journals\\comats.xlsx')

df=pd.read_excel(xlsx,'J12_highreqmat',index_col=0)
print type(df)
#print df
#print "df.mean()=" + str(df.mean())
nf=df.values
print type(nf)
#print nf
#nfs=preprocessing.scale(nf)
#nfs=preprocessing.normalize(nf,norm="l2")
#print str(nfs)
knf=KMeans(n_clusters=2,random_state=0).fit(nf)
print knf.labels_
print knf.cluster_centers_
print "numpy array : df.ndim,df.shape,df.size....."
print str(nf.ndim)
print str(nf.size)
print str(nf.shape)
coums=nf.shape[0]
print "coums="+str(coums)
rows=nf.shape[1]
print "rows="+str(rows)
print str(np.amax(nf))

#print "df.idmax()=" + str(df.max)
#print df.head(0)
kws=df.columns
kwl=[]
for kw in kws:
#print "keywords.."
    kwl.append(kw)
    #print kw
print "kwl=......."
print kwl

plt.figure()
plt.axis([0,rows,0,np.amax(nf)])
plt.grid(True)
plt.plot(nf,'k.')
plt.show()
#df=pd.read_excel(xlsx,['J11_highreqmat','J12_highreqmat'],index_col=0)
for k in df.items():
    print k
#print df[1]
import numpy as np
from sklearn.cluster import KMeans
from sklearn import metrics
import matplotlib.pyplot as plt
plt.figure(figsize=(8, 10))
plt.subplot(3, 2, 1)
x1 = np.array([1, 2, 3, 1, 5, 6, 5, 5, 6, 7, 8, 9, 7, 9])
x2 = np.array([1, 3, 2, 2, 8, 6, 7, 6, 7, 1, 2, 1, 1, 3])
X = np.array(list(zip(x1, x2))).reshape(len(x1), 2)
plt.xlim([0, 10])
plt.ylim([0, 10])
plt.title('样本',fontproperties=font)
plt.scatter(x1, x2)
'''

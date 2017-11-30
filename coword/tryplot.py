# -*- coding: utf-8 -*-
"""
Created on 20171122 非常好的案例
https://www.cnblogs.com/wuchuanying/p/6264025.html

@author: Administrator
"""
'''
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline
#随机生成一个实数，范围在（0.5,1.5）之间
cluster1=np.random.uniform(0.5,1.5,(2,10))
cluster2=np.random.uniform(3.5,4.5,(2,10))
#hstack拼接操作
X=np.hstack((cluster1,cluster2)).T
plt.figure()
plt.axis([0,5,0,5])
plt.grid(True)
plt.plot(X[:,0],X[:,1],'k.')
plt.show()

from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"c:\windows\fonts\msyh.ttc", size=10)
#我们计算K值从1到10对应的平均畸变程度：
from sklearn.cluster import KMeans
#用scipy求解距离
from scipy.spatial.distance import cdist
K=range(1,10)
meandistortions=[]
for k in K:
    kmeans=KMeans(n_clusters=k)
    kmeans.fit(X)
    meandistortions.append(sum(np.min(
            cdist(X,kmeans.cluster_centers_,
                 'euclidean'),axis=1))/X.shape[0])
plt.plot(K,meandistortions,'bx-')
plt.xlabel('k')
plt.ylabel(u'平均畸变程度',fontproperties=font)
plt.title(u'用肘部法则来确定最佳的K值',fontproperties=font)
plt.show()
'''
#尝试用极坐标来画图
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist
from sklearn import metrics
import math
font = FontProperties(fname="c:\windows\\fonts\msyh.ttc", size=10)
xlsx=pd.ExcelFile('../data/journals/selectdata.xlsx')
pngfile="../data/journals/results/"
#filerange=[100,200,500,1000,1500,2000]
filerange=[1000]
for st in filerange:
    sheetname="n3-"+str(st)
    df=pd.read_excel(xlsx,sheetname,index_col=0)
    #1 = np.array([1, 2, 3, 1, 5, 6, 5, 5, 6, 7, 8, 9, 7, 9])
    #x2 = np.array([1, 3, 2, 2, 8, 6, 7, 6, 7, 1, 2, 1, 1, 3])
    #X=np.array(list(zip(x1,x2))).reshape(len(x1),2)  #转置为14行2列
    kw=[]
    for wd in df.index:
        kw.append(wd) #用kw接收所有词
    nf=df.values #转换为numpy adarray
    #print nf
    plt.figure()
    plt.axis([0,nf.shape[0],0,1])  #用最大行数，即最大词数，作为数轴横轴
    plt.grid(True)
    ax1 = plt.subplot(121, projection='polar')
    plt.title(u'polar coordinates', fontproperties=font)
    ax2 = plt.subplot(221)
    plt.title(u'Cartesian coordinates', fontproperties=font)
    #ax3 = plt.subplot(223, projection='polar')
    #ax4 = plt.subplot(224, projection='polar')
    ax1.plot(nf, '.', lw=3)
    #ax2.plot(nf, '.', lw=3)
    #ax3.plot(nf, '.', lw=3)
    #ax4.plot(nf, '.', lw=3)
    #ax1.set_rscale('linear')
    #ax3.set_rlim(math.pow(10, -1), math.pow(10, 0))
    #ax3.set_rscale('symlog')
    #ax4.set_rlim(math.pow(2, -1), math.pow(2, 0))
    #ax4.set_rscale('log')
    #foo_fig=plt.gcf()
    #foo_fig.savefig('f00.eps',format='eps',dpi=1000)
    #figfile=pngfile+ "polar8-"+ str(st) +".png"
    figfile = pngfile + "polar6" + str(st) + ".svg"
    plt.savefig(figfile)
    #pngfile = "..\\data\\journals\\results\\"

'''
#画出原图
import numpy as np
import matplotlib.pyplot as plt
x1 = np.array([1, 2, 3, 1, 5, 6, 5, 5, 6, 7, 8, 9, 7, 9])
x2 = np.array([1, 3, 2, 2, 8, 6, 7, 6, 7, 1, 2, 1, 1, 3])
X=np.array(list(zip(x1,x2))).reshape(len(x1),2)  #转置为14行2列
print X
print '---------------'
print X[:,0]
print '---------------'
print X[:,1]
plt.figure()
plt.axis([0,10,0,10])  #用最大值作为数轴
plt.grid(True)
#plt.plot(X[:,0],X[:,1],'k.')
ax1=plt.subplot(121,projection='polar')
ax2=plt.subplot(122)
ax1.plot(X[:,0],X[:,1],'--',lw=2)
ax2.plot(X[:,0],X[:,1],'--',lw=2)
plt.show()
'''
'''
#肘部法则确定肘部位置
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist
from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"c:\windows\fonts\msyh.ttc", size=10)
K=range(1,10)
meandistortions=[]
for k in K:
    kmeans=KMeans(n_clusters=k)
    kmeans.fit(X)
    meandistortions.append(sum(np.min(cdist(
            X,kmeans.cluster_centers_,"euclidean"),axis=1))/X.shape[0])
plt.plot(K,meandistortions,'bx-')
plt.xlabel('k')
plt.ylabel(u'平均畸变程度',fontproperties=font)
plt.title(u'用肘部法则来确定最佳的K值',fontproperties=font)
plt.show()

#肘部附近几个K值得对比==
import numpy as np
from sklearn.cluster import KMeans
from sklearn import metrics
f01=open("tt.txt","w+")
plt.figure(figsize=(8,10))
plt.subplot(3,2,1)
x1 = np.array([1, 2, 3, 1, 5, 6, 5, 5, 6, 7, 8, 9, 7, 9])
x2 = np.array([1, 3, 2, 2, 8, 6, 7, 6, 7, 1, 2, 1, 1, 3])
X = np.array(list(zip(x1, x2))).reshape(len(x1), 2)
plt.xlim([0,10])
plt.ylim([0,10])
plt.title(u'样本',fontproperties=font)
plt.scatter(x1, x2)
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'b']
markers = ['o', 's', 'D', 'v', '^', 'p', '*', '+']
tests=[2,3,4,5,8]
subplot_counter=1
for t in tests:
    print "t="+ str(t) + "-------------"
    f01.write("t="+ str(t) + "-------------  " + "\n")
    subplot_counter+=1
    plt.subplot(3,2,subplot_counter)
    kmeans_model=KMeans(n_clusters=t).fit(X)
    #print X
    #print X.shape
    for i in range(0,X.shape[0]):
        print kmeans_model.labels_[i]#:每个点对应的标签值
        f01.write(str(kmeans_model.labels_[i]))
    f01.write('\n')
    for i,l in enumerate(kmeans_model.labels_):
        plt.plot(x1[i],x2[i],color=colors[l],
             marker=markers[l],ls='None')
        plt.xlim([0,10])
        plt.ylim([0,10])
        plt.title(u'K = %s, 轮廓系数 = %.03f' %
                  (t, metrics.silhouette_score
                   (X, kmeans_model.labels_,metric='euclidean'))
                  ,fontproperties=font)
plt.show()
f01.close()
'''
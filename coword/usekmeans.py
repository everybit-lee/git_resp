# -*- coding: utf-8 -*-
"""
Created on 20171120 尝试使用Kmeans进行聚类

@author: Administrator
"""

from sklearn.cluster import KMeans
import pandas as pd

xlsx=pd.ExcelFile('..\\data\\journals\\comats.xlsx')

df=pd.read_excel(xlsx,'J12_highreqmat',index_col=0)  #这里得到一个pandas dataframe
#print type(df)

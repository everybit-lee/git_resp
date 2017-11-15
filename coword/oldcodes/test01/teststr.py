# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 15:38:59 2016

@author: Administrator
"""

str='This (is) a string'
print(len(str))
pstr=str[0:9]
print(len(pstr))
i=len(str)-len(pstr)
print(i)
nstr=str[9:9+i]
print(pstr)
print(nstr)
smstr=pstr.replace('(','')
rstr=smstr + nstr
print(rstr)
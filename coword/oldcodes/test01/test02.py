# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 15:16:43 2016

@author: Administrator
"""

import urllib.request
#urllib.request.urljoin('http://paper.scholat.com/paper/select?callback=jQuery171024074964099705132_1479691582727&indent=on&version=2.2&json.wrf=searchHomePageResult&q=source:自动化学报&fl=*&sort=score%20desc,year%20desc&wt=json&facet=true&facet.field=type&facet.field=year&facet.sort=index&f.year.facet.mincount=1&facet.limit=-1&_=1479691582812')
response=urllib.request.urlopen('http://paper.scholat.com/paper/select?callback=jQuery171024074964099705132_1479691582727&indent=on&version=2.2&json.wrf=searchHomePageResult&q=source:%e8%87%aa%e5%8a%a8%e5%8c%96%e5%ad%a6%e6%8a%a5&fl=*&sort=score%20desc,year%20desc&wt=json&facet=true&facet.field=type&facet.field=year&facet.sort=index&f.year.facet.mincount=1&facet.limit=-1&_=1479691582812&start=0&rows=1')
#print(response.info())
#print(response.read().decode('UTF8'))
str=response.read().decode('UTF8')

pstr=str[0:str.find('"response"')+11]
j=len(str)-(str.find('"response"')+11)
nstr=str[str.find('"response"')+11:str.find('"response"')+11+j]
#print(nstr)
mstr=nstr[0:nstr.find('"facet_counts"')-4]  #mstr是符合json格式的字符串
print(mstr)
i=len(str)-len(pstr)-2
nstr=str[22:22+i]
sstr=pstr.replace('(','')
rstr=sstr+nstr  #rstr才是正确的json结构
#print(rstr)
#if rstr.find('"response"')>0:
    #print(rstr.find('"response"'))
#else:
    #print('notfound')

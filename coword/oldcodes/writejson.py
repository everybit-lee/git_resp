# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 13:50:46 2016

@author: Administrator
"""

#import pymysql  
import json
import urllib.request
#from builtins import int  


response=urllib.request.urlopen('http://paper.scholat.com/paper/select?callback=jQuery171024074964099705132_1479691582727&indent=on&version=2.2&json.wrf=searchHomePageResult&q=source:%e8%87%aa%e5%8a%a8%e5%8c%96%e5%ad%a6%e6%8a%a5+OR+source%3a%e6%8e%a7%e5%88%b6%e4%b8%8e%e5%86%b3%e7%ad%96+OR+source%3a%e8%ae%a1%e7%ae%97%e6%9c%ba%e9%9b%86%e6%88%90%e5%88%b6%e9%80%a0%e7%b3%bb%e7%bb%9f+OR+source%3a%e9%81%a5%e6%84%9f%e6%8a%80%e6%9c%af%e4%b8%8e%e5%ba%94%e7%94%a8+OR+source%3a%e6%8e%a7%e5%88%b6%e7%90%86%e8%ae%ba%e4%b8%8e%e5%ba%94%e7%94%a8+OR+source%3a%e4%b8%ad%e5%9b%bd%e5%9b%be%e8%b1%a1%e5%9b%be%e5%bd%a2%e5%ad%a6%e6%8a%a5+OR+source%3a%e5%9b%bd%e5%9c%9f%e8%b5%84%e6%ba%90%e9%81%a5%e6%84%9f+OR+source%3a%e8%ae%a1%e7%ae%97%e6%9c%ba%e5%b7%a5%e7%a8%8b%e4%b8%8e%e8%ae%be%e8%ae%a1+OR+source%3a%e7%b3%bb%e7%bb%9f%e4%bb%bf%e7%9c%9f%e5%ad%a6%e6%8a%a5+OR+source%3a%e5%be%ae%e7%94%b5%e5%ad%90%e5%ad%a6%e4%b8%8e%e8%ae%a1%e7%ae%97%e6%9c%ba+OR+source%3a%e5%b0%8f%e5%9e%8b%e5%be%ae%e5%9e%8b%e8%ae%a1%e7%ae%97%e6%9c%ba%e7%b3%bb%e7%bb%9f+OR+source%3a%e6%8e%a7%e5%88%b6%e5%b7%a5%e7%a8%8b+OR+source%3a%e8%bd%af%e4%bb%b6%e5%ad%a6%e6%8a%a5+OR+source%3a%e8%ae%a1%e7%ae%97%e6%9c%ba%e5%ad%a6%e6%8a%a5+OR+source%3a%e8%ae%a1%e7%ae%97%e6%9c%ba%e7%a0%94%e7%a9%b6%e4%b8%8e%e5%8f%91%e5%b1%95+OR+source%3a%e4%b8%ad%e6%96%87%e4%bf%a1%e6%81%af%e5%ad%a6%e6%8a%a5+OR+source%3a%e6%9c%ba%e5%99%a8%e4%ba%ba+OR+source%3a%e8%ae%a1%e7%ae%97%e6%9c%ba%e8%be%85%e5%8a%a9%e8%ae%be%e8%ae%a1%e4%b8%8e%e5%9b%be%e5%bd%a2%e5%ad%a6%e5%ad%a6%e6%8a%a5+OR+source%3a%e4%bc%a0%e6%84%9f%e6%8a%80%e6%9c%af%e5%ad%a6%e6%8a%a5+OR+source%3a%e8%ae%a1%e7%ae%97%e6%9c%ba%e5%ba%94%e7%94%a8+OR+source%3a%e9%81%a5%e6%84%9f%e4%bf%a1%e6%81%af+OR+source%3a%e8%ae%a1%e7%ae%97%e6%9c%ba%e5%b7%a5%e7%a8%8b+OR+source%3a%e8%ae%a1%e7%ae%97%e6%9c%ba%e7%a7%91%e5%ad%a6+OR+source%3a%e8%ae%a1%e7%ae%97%e6%9c%ba%e7%a7%91%e5%ad%a6%e4%b8%8e%e6%8e%a2%e7%b4%a2+OR+source%3a%e8%ae%a1%e7%ae%97%e6%9c%ba%e5%ba%94%e7%94%a8%e7%a0%94%e7%a9%b6+OR+source%3a%e6%a8%a1%e5%bc%8f%e8%af%86%e5%88%ab%e4%b8%8e%e4%ba%ba%e5%b7%a5%e6%99%ba%e8%83%bd+OR+source%3a%e6%99%ba%e8%83%bd%e7%b3%bb%e7%bb%9f%e5%ad%a6%e6%8a%a5+OR+source%3a%e8%ae%a1%e7%ae%97%e6%9c%ba%e5%b7%a5%e7%a8%8b%e4%b8%8e%e5%ba%94%e7%94%a8+OR+source%3a%e4%bf%a1%e6%81%af%e4%b8%8e%e6%8e%a7%e5%88%b6+OR+source%3a%e8%ae%a1%e7%ae%97%e6%9c%ba%e5%b7%a5%e7%a8%8b%e4%b8%8e%e7%a7%91%e5%ad%a6+OR+source%3a%e8%ae%a1%e7%ae%97%e6%9c%ba%e4%bb%bf%e7%9c%9f&fl=*&sort=score%20desc,year%20desc&wt=json&facet=true&facet.field=type&facet.field=year&facet.sort=index&f.year.facet.mincount=1&facet.limit=-1&_=1479691582812&start=0&rows=360648')
readstr=response.read().decode('UTF-8','ignore')
pstr=readstr[0:readstr.find('"response"')+11]
j=len(readstr)-(readstr.find('"response"')+11)
nstr=readstr[readstr.find('"response"')+11:readstr.find('"response"')+11+j]
#print(nstr)
mstr=nstr[0:nstr.find('"facet_counts"')-4]

myjs=json.loads(mstr)

f=open('mstr.json','w+')

f.write(json.dumps(myjs))
    
f.close()

print('写入json文件结束！')
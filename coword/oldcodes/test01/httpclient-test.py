# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 14:16:59 2016

@author: Administrator
"""
#!/usr/bin/env python
#coding=utf8

import http.client
#import sys
#import imp
#imp.reload(sys)                        
#sys.setdefaultencoding('utf-8')

# str='/paper/select?callback=jQuery171024074964099705132_1479691582727&indent=on&version=2.2&json.wrf=searchHomePageResult&q=source:%e8%87%aa%e5%8a%a8%e5%8c%96%e5%ad%a6%e6%8a%a5&fl=*&sort=score%20desc,year%20desc&wt=json&facet=true&facet.field=type&facet.field=year&facet.sort=index&f.year.facet.mincount=1&facet.limit=-1&_=1479691582812'
str='/paper/select?callback=jQuery171024074964099705132_1479691582727&indent=on&version=2.2&json.wrf=searchHomePageResult&q=source:自动化学报&fl=*&sort=score%20desc,year%20desc&wt=json&facet=true&facet.field=type&facet.field=year&facet.sort=index&f.year.facet.mincount=1&facet.limit=-1&_=1479691582812'
#str.encode('utf-8')
httpclient=None
httpclient=http.client.HTTPConnection('paper.scholat.com')
#httpclient.request('GET',str)
httpclient.request('GET',str.encode('utf-8'))
res=httpclient.getresponse()
print(res.status,res.reason)
print(res.msg)
print(res.read().decode('utf-8'))

if httpclient:
    httpclient.close()


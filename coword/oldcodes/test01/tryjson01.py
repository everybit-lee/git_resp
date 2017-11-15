# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 14:25:09 2016

@author: Administrator
"""

import json 
json_string = '{"success": "1","info": "成功","data": {"list": [{"word": "淘宝seo","total": 239},{"word": "哪里学seo","total": 0}]}}' 
#先将json解析成python字典类型，然后就跟操作字典一样取值 
json_dict = json.loads(json_string) 
for i in json_dict.get('data').get('list'): 
    print(i.get('word') )

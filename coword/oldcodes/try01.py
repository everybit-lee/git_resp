# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 13:45:35 2016

@author: Administrator
"""
import pymysql  
import json
#import urllib.request
#from builtins import int
#import os
  
#将MysqlHelper的几个函数写出来  
  
def  connDB():                              #连接数据库  
    conn=pymysql.connect(host="localhost",port=3306,user="root",passwd="123456",db="paper3",charset='utf8');  
    cur=conn.cursor();  
    return (conn,cur);  
  
def exeUpdate(conn,cur,sql):                #更新或插入操作  
    sta=cur.execute(sql);  
    conn.commit();  
    return (sta);  
  
def exeDelete(conn,cur,IDs):                #删除操作  
    sta=0;  
    for eachID in IDs.split(' '):  
        sta+=cur.execute("delete from students where Id=%d"%(int(eachID)));  
    conn.commit();  
    return (sta);  
          
def exeQuery(cur,sql):                      #查找操作  
    cur.execute(sql);  
    return (cur);  
      
def connClose(conn,cur):                    #关闭连接，释放资源  
    cur.close();  
    conn.close();  

#########################下面开始事务操作##############
#connDB():连接数据库/ exeUpdate(conn,cur,sql)更新或插入操作 
#exeDelete(conn,cur,IDs)删除操作  / exeQuery(cur,sql)查找操作  /connClose(conn,cur)关闭连接，释放资源
#response=urllib.request.urlopen('http://paper.scholat.com/paper/select?callback=jQuery171024074964099705132_1479691582727&indent=on&version=2.2&json.wrf=searchHomePageResult&q=source:%e8%87%aa%e5%8a%a8%e5%8c%96%e5%ad%a6%e6%8a%a5&fl=*&sort=score%20desc,year%20desc&wt=json&facet=true&facet.field=type&facet.field=year&facet.sort=index&f.year.facet.mincount=1&facet.limit=-1&_=1479691582812&start=0&rows=360648')
response=urllib.request.urlopen('http://paper.scholat.com/paper/select?callback=jQuery171024074964099705132_1479691582727&indent=on&version=2.2&json.wrf=searchHomePageResult&q=source:%e8%87%aa%e5%8a%a8%e5%8c%96%e5%ad%a6%e6%8a%a5+OR+source%3a%e6%8e%a7%e5%88%b6%e4%b8%8e%e5%86%b3%e7%ad%96+OR+source%3a%e8%ae%a1%e7%ae%97%e6%9c%ba%e9%9b%86%e6%88%90%e5%88%b6%e9%80%a0%e7%b3%bb%e7%bb%9f+OR+source%3a%e9%81%a5%e6%84%9f%e6%8a%80%e6%9c%af%e4%b8%8e%e5%ba%94%e7%94%a8+OR+source%3a%e6%8e%a7%e5%88%b6%e7%90%86%e8%ae%ba%e4%b8%8e%e5%ba%94%e7%94%a8+OR+source%3a%e4%b8%ad%e5%9b%bd%e5%9b%be%e8%b1%a1%e5%9b%be%e5%bd%a2%e5%ad%a6%e6%8a%a5+OR+source%3a%e5%9b%bd%e5%9c%9f%e8%b5%84%e6%ba%90%e9%81%a5%e6%84%9f+OR+source%3a%e8%ae%a1%e7%ae%97%e6%9c%ba%e5%b7%a5%e7%a8%8b%e4%b8%8e%e8%ae%be%e8%ae%a1+OR+source%3a%e7%b3%bb%e7%bb%9f%e4%bb%bf%e7%9c%9f%e5%ad%a6%e6%8a%a5+OR+source%3a%e5%be%ae%e7%94%b5%e5%ad%90%e5%ad%a6%e4%b8%8e%e8%ae%a1%e7%ae%97%e6%9c%ba+OR+source%3a%e5%b0%8f%e5%9e%8b%e5%be%ae%e5%9e%8b%e8%ae%a1%e7%ae%97%e6%9c%ba%e7%b3%bb%e7%bb%9f+OR+source%3a%e6%8e%a7%e5%88%b6%e5%b7%a5%e7%a8%8b+OR+source%3a%e8%bd%af%e4%bb%b6%e5%ad%a6%e6%8a%a5+OR+source%3a%e8%ae%a1%e7%ae%97%e6%9c%ba%e5%ad%a6%e6%8a%a5+OR+source%3a%e8%ae%a1%e7%ae%97%e6%9c%ba%e7%a0%94%e7%a9%b6%e4%b8%8e%e5%8f%91%e5%b1%95+OR+source%3a%e4%b8%ad%e6%96%87%e4%bf%a1%e6%81%af%e5%ad%a6%e6%8a%a5+OR+source%3a%e6%9c%ba%e5%99%a8%e4%ba%ba+OR+source%3a%e8%ae%a1%e7%ae%97%e6%9c%ba%e8%be%85%e5%8a%a9%e8%ae%be%e8%ae%a1%e4%b8%8e%e5%9b%be%e5%bd%a2%e5%ad%a6%e5%ad%a6%e6%8a%a5+OR+source%3a%e4%bc%a0%e6%84%9f%e6%8a%80%e6%9c%af%e5%ad%a6%e6%8a%a5+OR+source%3a%e8%ae%a1%e7%ae%97%e6%9c%ba%e5%ba%94%e7%94%a8+OR+source%3a%e9%81%a5%e6%84%9f%e4%bf%a1%e6%81%af+OR+source%3a%e8%ae%a1%e7%ae%97%e6%9c%ba%e5%b7%a5%e7%a8%8b+OR+source%3a%e8%ae%a1%e7%ae%97%e6%9c%ba%e7%a7%91%e5%ad%a6+OR+source%3a%e8%ae%a1%e7%ae%97%e6%9c%ba%e7%a7%91%e5%ad%a6%e4%b8%8e%e6%8e%a2%e7%b4%a2+OR+source%3a%e8%ae%a1%e7%ae%97%e6%9c%ba%e5%ba%94%e7%94%a8%e7%a0%94%e7%a9%b6+OR+source%3a%e6%a8%a1%e5%bc%8f%e8%af%86%e5%88%ab%e4%b8%8e%e4%ba%ba%e5%b7%a5%e6%99%ba%e8%83%bd+OR+source%3a%e6%99%ba%e8%83%bd%e7%b3%bb%e7%bb%9f%e5%ad%a6%e6%8a%a5+OR+source%3a%e8%ae%a1%e7%ae%97%e6%9c%ba%e5%b7%a5%e7%a8%8b%e4%b8%8e%e5%ba%94%e7%94%a8+OR+source%3a%e4%bf%a1%e6%81%af%e4%b8%8e%e6%8e%a7%e5%88%b6+OR+source%3a%e8%ae%a1%e7%ae%97%e6%9c%ba%e5%b7%a5%e7%a8%8b%e4%b8%8e%e7%a7%91%e5%ad%a6+OR+source%3a%e8%ae%a1%e7%ae%97%e6%9c%ba%e4%bb%bf%e7%9c%9f&fl=*&sort=score%20desc,year%20desc&wt=json&facet=true&facet.field=type&facet.field=year&facet.sort=index&f.year.facet.mincount=1&facet.limit=-1&_=1479691582812&start=0&rows=360648')
readstr=response.read().decode('UTF-8','ignore')
pstr=readstr[0:readstr.find('"response"')+11]
j=len(readstr)-(readstr.find('"response"')+11)
nstr=readstr[readstr.find('"response"')+11:readstr.find('"response"')+11+j]
#print(nstr)
mstr=nstr[0:nstr.find('"facet_counts"')-4]  #mstr是符合json格式的字符串
#print(mstr)
#######################上面获得文献的json数据#####################
'''
f=open('papers.txt','w+')
f.write(mstr)
f.close()
'''
##################
myjs=json.loads(mstr)
conn,cur=connDB()

log_file=open('log.txt','w+')
i=0
for p in myjs.get('docs'):  #循环处理每一个文献信息
    #插入之前先检查有没有重复文献数据   
    sqlstr='SELECT pid FROM paper WHERE pid=%s'
    cur.execute(sqlstr,p.get('id'))
    #cur.scroll(0)
    getpid=cur.fetchall()
    #print(getpid)
    if not getpid:
        log_file.write('\n' + '####################插入第' + str(i) +'个文献#######################:' + '\n')
        #print('插入文献')        
        try:
            #exeUpdate(cur,sqlstr)            
            if ('author' in p.keys()) :
                sqlstr= 'INSERT INTO paper(oriid,ptitle,ptype,plang,abstract,eng_abstract,source,year,issue,doi) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                cur.execute(sqlstr,(p.get('id'),p.get('title'),p.get('type'),p.get('lang'),p.get('abstract'),p.get('english_abstract'),p.get('source'),p.get('year'),p.get('issue'),p.get('doi')))
            else:
                sqlstr= 'INSERT INTO paper(oriid,ptitle,ptype,plang,abstract,eng_abstract,source,year,issue,doi,noauthor) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                cur.execute(sqlstr,(p.get('id'),p.get('title'),p.get('type'),p.get('lang'),p.get('abstract'),p.get('english_abstract'),p.get('source'),p.get('year'),p.get('issue'),p.get('doi'),1))
            conn.commit()   
            ptitle=p.get('title')
            try:
                log_file.write('插入文献信息成功:' + p.get('title') + '\n')
            except:
                print('发生解码错误，不能写入文件')
                    
            #print('插入文献信息成功'+ptitle)
            pSucc=True
        except Exception as e:
            #log_file.write('&&&&&&&  插入文献信息失败 可能存在重复 &&&&&&&&7&&：'+ p.get('title'))
            print('插入文献信息失败',e)
            raise
        if pSucc: #获得当前
            cur.execute('SELECT pid FROM paper WHERE oriid=%s',p.get('id'))
            pidstr=cur.fetchall()
            
        if pSucc and ('author' in p.keys()) :        
            auths=p.get('author')
            for a in auths:  
                #这里应该有一个作者姓名消岐的过程（暂无，先只是唯一化）
                sqlstr='SELECT aname FROM authors WHERE aname=%s'
                cur.execute(sqlstr,a)
                ns=cur.fetchall()
                #print(ns)
                if not ns:  #若还没有该作者，插入该作者信息
                    log_file.write('@@@@@@@@@@@@@插入作者@@@@@@@@@@@@@@'+ '\n')
                    #print('插入作者')
                    ##### ns为空，则插入新的姓名
                    sqlstr='INSERT INTO authors(aname) VALUES(%s)'
                    aSucc=False
                    #sqlstr=sqlstr +'"'+ a +'"' +')'
                    try:
                        #exeUpdatecur,sqlstr)
                        #conn,cur=connDB()
                        cur.execute(sqlstr,a)  #插入author
                        conn.commit()
                        xingm=a
                        #connClose(conn,cur)
                        log_file.write('插入作者信息成功:')
                        #print('插入作者信息成功:'+xingm)
                        aSucc=True
                    except Exception as e:
                        #log_file.write('插入作者信息失败' +a)
                        print('插入作者信息失败',e)
                        raise
                        
                #有可能作者表已经有该作者，但仍需处理该作者与文献的关联。                
                log_file.write('当前文献与作者关联：' + str(pidstr[0][0]) + '---')                
                cur.execute('SELECT aid FROM authors WHERE aname=%s',a)
                aidstr=cur.fetchall()
                log_file.write(str(aidstr[0][0]))
                #print(str(aidstr[0][0]) + '  ' + xingm)                        
                
                sqlstr='SELECT pid,aid FROM p_a WHERE pid=%s AND aid=%s'
                cur.execute(sqlstr,(pidstr[0][0],aidstr[0][0]))
                rs=cur.fetchall()
                if not rs: #结果集合为空，才插入关联
                    log_file.write('---------插入此关联----')
                    #print('插入关联')
                    sqlstr='INSERT INTO p_a(pid,aid) VALUES(%s,%s)'                
                    try:
                        cur.execute(sqlstr,(pidstr[0][0],aidstr[0][0]))  #插入文献与作者关系表
                        conn.commit()
                        log_file.write('插入文献和作者关联成功:' + str(pidstr[0][0]) + ' -- ' + str(aidstr[0][0]) )
                        #print('插入文献和作者关联成功:' + str(pidstr[0][0]) + ptitle + ' -- ' + str(aidstr[0][0]) + xingm)
                    except Exception as e:
                        log_file.write('插入文献和作者关联失败' + str(pidstr[0][0]) + ' -- ' + str(aidstr[0][0]))
                        #print('插入文献和作者关联失败',e)
                        raise
                else:
                    log_file.write('插入文献和作者关联成功:' + str(pidstr[0][0]) + ' -- ' + str(aidstr[0][0]))
                    #print('出现重复的文献和作者关联:'+ str(pidstr[0][0]) + ' -- ' + str(aidstr[0][0]))
        else:
            log_file.write('!!!!!!!!!!!!!  No Authors! !!!!!!!!!!!!!!' + '  in ' + p.get('source') + '\n')
                            #处理关键词
        if pSucc and ('keyword' in p.keys()):
            kws=p.get('keyword')
            for kw in kws:
                cur.execute('SELECT keyword FROM keywords WHERE keyword=%s', kw)
                ks=cur.fetchall()
                if not ks:
                    log_file.write('……………………插入关键字……………………')
                    #print('……………………插入关键字……………………')
                    sqlstr='INSERT INTO keywords(keyword) VALUES(%s)'   
                    kSucc=False
                    try:
                        cur.execute(sqlstr,kw)  #插入author
                        conn.commit()
                        gjz=kw
                        #connClose(conn,cur)
                        try:
                            log_file.write('插入关键字信息成功:'+gjz)                        
                        except:
                            print('发生解码错误，不能写入文件')   
                        kSucc=True
                    except Exception as e:
                        #log_file.write(e)
                        print('插入关键字信息失败')                        
                        raise
                    if kSucc:
                        #cur.execute('SELECT pid FROM paper WHERE oriid=%s',p.get('id'))
                        #pidstr=cur.fetchall()    
                        #log_file.write(str(pidstr[0][0]))
                        #print(str(pidstr[0][0]) + '  ' + ptitle)
                        cur.execute('SELECT kwid FROM keywords WHERE keyword=%s',kw)
                        kwstr=cur.fetchall()
                        try:
                            log_file.write(str(kwstr[0][0]) + '  ' + gjz + '\n')
                        except:
                            print('发生解码错误，不能写入文件')
                        
                        sqlstr='SELECT pid,kwid FROM p_kw WHERE pid=%s AND kwid=%s'
                        cur.execute(sqlstr,(pidstr[0][0],kwstr[0][0]))
                        kws=cur.fetchall()
                        if not kws: #结果集合为空，才插入关联
                            log_file.write('-----插入文献与关键字关联------'+ '\n')
                            
                            sqlstr='INSERT INTO p_kw(pid,kwid) VALUES(%s,%s)'                
                            try:
                                cur.execute(sqlstr,(pidstr[0][0],kwstr[0][0]))  #插入文献与作者关系表
                                conn.commit()
                                log_file.write('插入文献与关键字关联成功:' + str(pidstr[0][0]) + ' -- ' + str(kwstr[0][0]))
                                #print('插入文献和作者关联成功:' + str(pidstr[0][0]) + ptitle + ' -- ' + str(aidstr[0][0]) + xingm)
                            except Exception as e:
                                #log_file.write('插入文献与关键字关联失败'+ e)
                                print('插入文献和作者关联失败' + str(pidstr[0][0]) + ' -- ' + str(kwstr[0][0]))
                                raise
                        else:
                            try:
                                log_file.write('可能存在重复的文献与关键字关联：'+ str(pidstr[0][0]) + ' -- ' + str(kwstr[0][0]) + gjz)
                            except:
                                print('发生解码错误，不能写入文件')
        else:
            try:
                log_file.write('!!!!!!!!!!!!!!No keywords!!!!!!!!!!!  in ' + p.get('title') + '\n')       
            except:
                print('发生解码错误，不能写入文件')
    i=i+1
    if (i % 1000)==0:
        print('######  第 ' + str(i) + ' 个值处理完...继续干活...#######')
                
connClose(conn,cur)
log_file.write('所有操作结束')
print('所有操作结束')
log_file.close()


    















#-*-coding:utf-8-*-
'''
Created on 2014-10-15

@author: BONFY
'''
import MySQLdb
from dbTools import dbTools

if __name__ == '__main__':
    conn=MySQLdb.connect(host='localhost',user='****',passwd='****',port=3306,db='****',charset='utf8')
    #conn.select_db('test')
    
    sqlTools = dbTools(conn)
    
    sqlTools.insert('workers_info',username = 'bonfy',password='fwfwfw')  
    sqlTools.update('workers_info', username='ddfd',condition="password = 'hello'")
    
    sqlTools.close()
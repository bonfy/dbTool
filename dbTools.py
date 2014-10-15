#-*-coding:utf-8-*-
'''
Created on 2014-10-15

@author: BONFY
'''

class dbTools(object):

    def __init__(self,conn):
        self.conn = conn
        self.cursor=conn.cursor()
    
    def truncate(self,tablename):
        sql = "truncate table %s" % tablename
        self.cursor.execute(sql)
        self.conn.commit()
        
    def select(self,tablename,topN=None,condition=None):
        sql = "select "
        if topN:
            sql += "TOP %d " % topN
        sql += " * from %s" % tablename 
        if condition:
            sql += " where %s" % condition
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        return results
    
    def delete(self,tablename,condition=None):
        if condition:
            sql = "DELETE FROM %s WHERE %s" % (tablename,condition)
            self.cursor.execute(sql)
            self.conn.commit()
        else:
            print 'no condition not support,please use truncate'
    
    def insert(self,tablename,**kwags):
        if len(kwags):
            keys=""
            values = ""
            sql = "insert into %s(" % tablename
            for key in kwags:
                keys += "%s,"%key
                if type(kwags.get(key))==int:
                    values += "%s,"%kwags.get(key)
                else:
                    values += "'%s',"%kwags.get(key)

            sql = sql+ keys[:-1]+') values ('+values[:-1]+')'
            self.cursor.execute(sql)
            self.conn.commit() 
        else:
            print 'no arguments here'
    
    def update(self,tablename,condition=None,**kwags):
        if len(kwags):
            values = ""
            sql = "UPDATE %s SET " % tablename
            for key in kwags:
                
                if type(kwags.get(key))==int:
                    values += "%s = %s," % (key,kwags.get(key))
                else:
                    values += "%s = '%s'," % (key,kwags.get(key))
            sql = sql + values[:-1]     
            if condition:
                sql = sql + " where %s" % condition   
            self.cursor.execute(sql)
            self.conn.commit() 
        else:
            print 'no arguments here'
        
    
    def close(self):
        self.conn.close()

            
    
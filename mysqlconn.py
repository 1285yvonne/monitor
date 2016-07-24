#! /usr/bin/env python

import MySQLdb as mysqldb
import string

class Mysqlconn(object):
    
    def __init__(self):
        self.db = mysqldb.connect(user='cyf',passwd='password',db='practice',host='localhost')
        self.db.autocommit(True)
        self.cur = self.db.cursor()
        print 'the connect is established'
    
    def commitsql(self,sql,args=None):
        if args != None:
            self.cur.executemany(sql,args)
            print 'oks'
        else:
            self.cur.execute(sql)
            print 'ok'
            res = self.cur.fetchall()
            if res != None:
                return res
    
    def clear(self):
        sql = "delete from mem;delete from cpu; delete from disk;"
        self.cur.executemany(sql,args=None)
        # just for test

if __name__=='__main__':
    m = Mysqlconn()

import linecache
import time
import mysqlconn

DB = mysqlconn.Mysqlconn()
#import MySQLdb as mysqldb

#db = mysqldb.connect(user="cyf",passwd="64770118",db="practice",host="localhost")
#db.autocommit(True)
#cur = db.cursor()

def getMem():
    with open('/proc/meminfo') as f:
        linecache.clearcache()
        #linecount = len(f.readlines())
        mem_total = int(linecache.getline(f.name,1).split()[1])
	mem_avail = int(linecache.getline(f.name,3).split()[1])
    mem_used = mem_total - mem_avail
    #print mem_used/1024
    t = int(time.time())
    sql = 'insert into mem_prac values (%s,%s)'%(mem_used/1024,t)
    #cur.execute(sql)
    DB.commitsql(sql)
    #print 'ok'

while True:
    time.sleep(1)
    getMem()

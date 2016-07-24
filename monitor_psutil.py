#! /usr/bin/env python

import psutil
import mysqlconn
import time

class Monitor(object):

    def __init__(self):
        self.DB = mysqlconn.Mysqlconn() #connect to the sql

    def mem_monitor(self,status=True):
        if status:
            mem = psutil.virtual_memory()
            mem_total = int(mem.total)/ (1024.0*1024.0)
            mem_used = int(mem.total - mem.free - mem.buffers- mem.cached) / (1024.0*1024.0) 
            mem_ration = mem.percent
            mem_sql = "insert into mem values(%s,%s,%s);" % (time.time(),mem_used,mem_ration)
            self.DB.commitsql(mem_sql)
            #return mem_sql
        else:
            return

    def cpu_monitor(self,status=True):
        if status:
            cpu_status = psutil.cpu_times()
            cpu_user_time = cpu_status.user / 100.0
            cpu_sql = "insert into cpu values(%s,%s);" % (time.time(),cpu_user_time)
            self.DB.commitsql(cpu_sql)
            #return cpu_sql
        else:
            return

    def disk_monitor(self,status=True):
        if status:
            disk_status = psutil.disk_usage('/') #the usage of the partion
            disk_ration = float(disk_status.used) / float(disk_status.total)
            disk_sql = "insert into disk values(%s,%s);" % (time.time(),disk_ration)
            self.DB.commitsql(disk_sql)
            #return disk_sql
        else:
            return

    def web_monitor(self,status=True):
        pass
        
    def monitor(self,mem_status=True,cpu_status=True,disk_status=True,web_status=True):
        # just for test
        self.DB.clear()

        while True:
            time.sleep(2)
            self.mem_monitor(mem_status)
            self.cpu_monitor(cpu_status)
            self.disk_monitor(disk_status)
            self.web_monitor(web_status)
            #sql = str(mem_sql1 + cpu_sql2 + disk_sql3 + web_sql4)
            #print sql
            #self.DB.commitsql(sql,items)

if __name__=='__main__':
    print 'test'
    

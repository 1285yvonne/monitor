#! /usr/bin/env python
# coding=utf-8
from flask import Flask,render_template
import mysqlconn
import json
from subprocess import call
import os
import socket

app = Flask(__name__)
timestamp = 0;
DB = mysqlconn.Mysqlconn()
hostname = socket.gethostname()

@app.route('/')
def hello_world():
    call("sh start_monitor.sh",shell=True)
    return render_template('main.html')

@app.route('/mem')
def mem_status():
    global timestamp
    timestamp = 0
    return render_template('mem.html')

@app.route('/cpu')
def cpu_status():
    global timestamp
    timestamp = 0
    return render_template('cpu.html')

@app.route('/disk')
def disk_status():
    global timestamp
    timestamp = 0
    return render_template('disk.html')

@app.route('/data/mem',methods=['GET','POST'])
def data_mem():
    global timestamp
    global hostname
    if timestamp > 0:
	    sql = 'select * from mem where time >%s'% (timestamp/1000)
    else:
	    sql = 'select * from mem'
    res = DB.commitsql(sql)
    arr = []
    #temp = [{'name':hostname, 'marker':{'symbol':"'square'"},'data':[]}]
    for i in res:
        arr.append((i[0]*1000,i[-1]))
    #temp[0]['data'] = arr
    if len(arr)>0:
        timestamp = arr[0][0]
	return json.dumps(arr)

@app.route('/data/cpu',methods=['GET','POST'])
def data_cpu():
    pass

@app.route('/data/disk',methods=['GET','POST'])
def data_disk():
    pass

if __name__=='__main__':
    app.run(host='0.0.0.0',port=9999,debug=True)

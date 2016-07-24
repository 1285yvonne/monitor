# coding=utf-8
from flask import Flask,render_template
import MySQLdb as mysql
import json
app = Flask(__name__)

con = mysql.connect(user='cyf',passwd='64770118',host='localhost',db='practice')
con.autocommit(True)
cur = con.cursor()

timestamp = 0;

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/data')
def data():
    global timestamp
    if timestamp > 0:
	    sql = 'select * from mem_prac where time >%s'% (timestamp/1000)
    else:
	    sql = 'select * from mem_prac'
    cur.execute(sql)
    arr = []
    for i in cur.fetchall():
        arr.append([i[1]*1000,i[0]])
    if len(arr)>0:
        timestamp = arr[-1][0]
	return json.dumps(arr)

if __name__=='__main__':
    app.run(host='0.0.0.0',port=9999,debug=True)

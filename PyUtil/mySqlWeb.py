#! /usr/env/bin python3

from flask import Flask, render_template, request
from flaskext.mysql import MySQL
import mysql.connector
from mySqlConn import sqlConn

app = Flask(__name__)



'''
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'ashish_mysql'
app.config['MYSQL_DB'] = 'sakila'
'''

#sconn = sqlConn
#sconn.mySQLData(sconn)



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':        
        return render_template('login_form.html')        
    elif request.method == 'POST':
        sconn = sqlConn
        sconn.mySQLData(sconn)
        valOut =  "Conn Successfull %s"%sconn.mySQLData(sconn)
        text = request.form['username']
        return "submitted! %s and mySql: %s"%(text,valOut)
        
    

if __name__ == '__main__':
    app.run()
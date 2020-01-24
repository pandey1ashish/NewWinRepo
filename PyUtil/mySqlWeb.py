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
        return render_template('login_form.html', content="Python Example Registration Form")        
    elif request.method == 'POST':
        #text = request.form['username']
        uid = request.form['userid']
        sconn = sqlConn
        #sconn.mySQLData(sconn)
        valOut =  sconn.mySQLData(sconn, uid)
        #return "submitted! %s and mySql: %s"%(text,valOut)
        return render_template('login_form.html', content="Python Example Registration Form POST!", firstname=valOut, lastname="Last Name") 
        
    

if __name__ == '__main__':
    app.run()
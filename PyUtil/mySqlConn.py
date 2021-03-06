#! /usr/env/bin python3 

import flask
from flaskext.mysql import MySQL
import mysql.connector

db_connection = mysql.connector.connect(host="localhost", user="root", passwd="ashish_mysql", database="sakila", auth_plugin='mysql_native_password')

class sqlConn():
    def mySQLData(self, act_id):
        try:
            #print(db_connection)
            db_cursor = db_connection.cursor(buffered=True)
            sql_select_query = """select Concat(first_name) from actor where actor_id = %s"""
            #db_cursor.execute("select Concat(first_name,' ', last_name) from actor where actor_id = %s",act_id)
            db_cursor.execute(sql_select_query, (act_id,))
            mysql = MySQL()
            msgReturn = 'DbCon: ',mysql
            #print(msgReturn)

            for db in db_cursor:
                actor_name = db
                return actor_name
        
        except Exception as e:
            print('catch/except block')
            print(e)
        
        finally:
            print('finally')

scon = sqlConn()
print(scon.mySQLData(201))
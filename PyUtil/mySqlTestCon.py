import flask
from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse
#from flask.ext.mysql import MySQL
from flaskext.mysql import MySQL
import mysql.connector

db_connection = mysql.connector.connect(host="localhost", user="root", passwd="ashish_mysql", database="sakila", auth_plugin='mysql_native_password')
print(db_connection)
db_cursor = db_connection.cursor()
# executing cursor with execute method and pass SQL query
#db_cursor.execute("CREATE DATABASE my_first_db")
# get list of all databases

#db_cursor.execute("SHOW DATABASES")
db_cursor.execute("select Concat(first_name,' ', last_name) from actor where actor_id = 2")

#print all databases
mysql = MySQL()
msgReturn = 'DbCon: ',mysql

print(msgReturn)

for db in db_cursor:
    print(db)
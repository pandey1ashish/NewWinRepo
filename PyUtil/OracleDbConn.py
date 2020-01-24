#! /usr/env/bin python3

import cx_Oracle

connStr = 'test_local_db/ashish_db@localhost:1521/xe'
conn = cx_Oracle.connect(connStr)

'''
username = 'test_local_db'
password = 'ashish_db'
dsn = 'localhost/xe'
port = 1521
encoding = 'UTF-8'

connection = None
try:
    print('test_oracle_db')
    connection = cx_Oracle.connect(
        username,
        password,
        dsn,
        encoding=encoding)
 
    # show the version of the Oracle Database
    print(connection.version)
except cx_Oracle.Error as error:
    print(error)
finally:
    # release the connection
    if connection:
        connection.close()
'''
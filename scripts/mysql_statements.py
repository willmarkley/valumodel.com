#!/usr/bin/python

import mysql.connector

def mysql_statements():
    cnx = mysql.connector.connect(user='root', password='$$Jasper19',host='127.0.0.1',database='valumodel')
    cnx.close()
    return enterprise_value



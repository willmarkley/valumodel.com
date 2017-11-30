#!/usr/bin/python

import mysql.connector

def mysql_statements(ticker, value):
    cnx = mysql.connector.connect(user='root', password='$Dcfr$ck1', host='127.0.0.1', database='valumodel')
    cursor = cnx.cursor()
    
    ## INSERT into database
    cursor.execute('INSERT INTO avg VALUES (\''+ticker+'\',\''+str(value)+'\');')
    
    ## Make sure data is committed
    cnx.commit()
    
    cursor.close()
    cnx.close()



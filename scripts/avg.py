#!/usr/bin/python

import mysql.connector
from jinja2 import Environment, FileSystemLoader

def avg(req):
	cnx = mysql.connector.connect(user='root', password='$$Jasper19', host='127.0.0.1', database='valumodel')
	cursor = cnx.cursor()
    
	## SELECT from database
	cursor.execute('SELECT * FROM avg')
    
	totals = {}
	times = {}
	for (ticker, enterprise_val) in cursor:
		totals[ticker] += enterprise_val
		times[ticker] = times[ticker]+1
    	
	results = {}
	for ticker in totals.keys():
		results[ticker] = totals[ticker] / times[ticker]
    
	sorted_tickers = sorted(results.keys())
    
	cursor.close()
	cnx.close()

	env = Environment(loader = FileSystemLoader('/var/www/html/valumodel.com/html/templates'))
	template = env.get_template('avg.html')
	return template.render(results=results, tickers=sorted_tickers)

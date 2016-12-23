#!/usr/bin/python

import subprocess
import yaml
import sys

def calc_database(ticker):
	fcf = {}
	output = subprocess.check_output(['python', '/var/www/html/valumodel.com/scripts/calc_quandl.py', ticker])
	
	curr_year = int(output.split("^^")[0])
	
	if curr_year is '-1':
		print output.split("^^")[1]
		sys.exit()
	else:
		output = output.split("^^")[1]
		for key, value in yaml.load(output).iteritems():
			fcf[key] = value
			
	return (curr_year, fcf)

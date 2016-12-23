#!/usr/bin/python

import subprocess
import yaml
import sys

def calc_database(ticker):
	output = subprocess.check_output(['python', '/var/www/html/t.py', ticker])
	
	curr_year = output.split("^^")[0]
	
	if curr_year is '-1':
		print output.split("^^")[1]
		sys.exit()
	else:
		output = output.split("^^")[1]
		for key, value in yaml.load(output).iteritems():
			fcf[key] = value
			
	return (curr_year, fcf)

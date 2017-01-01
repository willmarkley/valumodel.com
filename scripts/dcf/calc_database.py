#!/usr/bin/python

import subprocess
import yaml
import sys

def calc_database(ticker):
	fcf = {}
	wacc = {}
        output = subprocess.check_output(['python', '/var/www/html/valumodel.com/scripts/calc_quandl.py', ticker])
	
	curr_year = int(output.split('^^')[0])
	output_fcf = output.split('^^')[1]
	output_wacc = output.split('^^')[2]
	
	if curr_year == -1:
		fcf=output_fcf
	else:
		for key, value in yaml.load(output_fcf).iteritems():
			fcf[key] = value
		for key, value in yaml.load(output_wacc).iteritems():
			wacc[key] = value
			
	return (curr_year, fcf, wacc)

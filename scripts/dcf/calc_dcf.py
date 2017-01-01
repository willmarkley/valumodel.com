#!/usr/bin/python

import sys
sys.path.append('/var/www/html/valumodel.com/scripts/dcf')

from calc_fcf import calc_fcf
from calc_wacc import calc_wacc
from calc_enter_val import calc_enter_val
from calc_database import calc_database
from mysql_statements import mysql_statements
from output import output

def calc_dcf(assumptions, ticker):
	##### Global Variables
	
	### Tuple, Value Dictionaries (field, year) = value
	fcf = {}

	### Key, Value Dictionaries [field] = value
	wacc = {}
	enterprise_value = {}
	implied_equity_value = {}
	
	### Gather Data from Quandl databases
	tuple_data       = calc_database(ticker)
	curr_year        = tuple_data[0]
	fcf              = tuple_data[1]
	wacc             = tuple_data[2]
	if curr_year==-1:
		return fcf
	
	### Years
	historical_years = [curr_year-3, curr_year-2, curr_year-1, curr_year]
	projected_years  = [curr_year+1, curr_year+2, curr_year+3, curr_year+4, curr_year+5]

	##### Main Execution
	fcf                  = calc_fcf(fcf, assumptions, curr_year, historical_years, projected_years)
	wacc                 = calc_wacc(wacc, assumptions)
	enterprise_value     = calc_enter_val(enterprise_value, assumptions, fcf, wacc, curr_year, projected_years)
	
	### Add Result to database
	mysql_statements(ticker, enterprise_value['Enterprise Value'])

	return output(fcf, curr_year, historical_years, projected_years, wacc, enterprise_value, assumptions, ticker)

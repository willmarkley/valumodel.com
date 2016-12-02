#!/usr/bin/python

import datetime
import sys
sys.path.append('/var/www/html/valumodel.com/scripts')

from calc_fcf import calc_fcf
from calc_wacc import calc_wacc
from calc_enter_val import calc_enter_val
from user_assumptions import user_assumptions
from calc_database import calc_database
from output import output

def calc_dcf(assumptions):
	##### Global Variables

	name = 'General Electric'
	ticker = 'GE'

	### Tuple, Value Dictionaries (field, year) = value
	fcf = {}

	### Key, Value Dictionaries [field] = value
	wacc = {}
	enterprise_value = {}
	implied_equity_value = {}

	### Years
	curr_year = 2008   #curr_year = datetime.datetime.now().year
	historical_years = [curr_year-3, curr_year-2, curr_year-1, curr_year]
	projected_years  = [curr_year+1, curr_year+2, curr_year+3, curr_year+4, curr_year+5]


	##### Main Execution

	fcf                  = calc_database(fcf, historical_years)
	fcf                  = calc_fcf(fcf, assumptions, curr_year, historical_years, projected_years)
	wacc                 = calc_wacc(wacc, assumptions)
	enterprise_value     = calc_enter_val(enterprise_value, assumptions, fcf, wacc, curr_year, projected_years)

	return output(fcf, curr_year, historical_years, projected_years, wacc, enterprise_value, assumptions, name, ticker)
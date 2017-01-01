#!/usr/bin/python

import sys
sys.path.append('/var/www/html/valumodel.com/scripts/dcf')
from calc_dcf import calc_dcf

def create_dcf(req, tax_rate, growth_rate_1_year_out, sga_of_sales, da_of_sales, capex_of_sales, nwc_of_sales, levered_beta, current_yield, exit_multiple, ticker):
	assumptions = {}
	try:
		assumptions['Tax Rate']               = float(tax_rate)/100.0
		assumptions['Growth Rate 1 year out'] = float(growth_rate_1_year_out)/100.0
		assumptions['SGA % of sales']         = float(sga_of_sales)/100.0
		assumptions['D&A % of sales']         = float(da_of_sales)/100.0
		assumptions['CAPEX % of sales']       = float(capex_of_sales)/100.0
		assumptions['NWC % of sales']         = float(nwc_of_sales)/100.0
		assumptions['Levered Beta']           = float(levered_beta)
		assumptions['Current Yield']          = float(current_yield)/100.0
		assumptions['Exit Multiple']          = float(exit_multiple)
	except ValueError:
		return '<!doctype html><html><body><h1>Invalid DCF Input.  Please try again.</h1></body></html>'
        ticker = ticker.split(' ')[0]
        if not ticker.isalnum():
            return '<!doctype html><html><body><h1>Invalid Ticker.  Please try again.</h1></body></html>'

	return calc_dcf(assumptions, ticker.upper())

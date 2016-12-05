#!/usr/bin/python

import sys
sys.path.append('/var/www/html/valumodel.com/scripts')
from calc_dcf import calc_dcf

def create_dcf(req, tax_rate, growth_rate_1_year_out, sga_of_sales, da_of_sales, capex_of_sales, nwc_of_sales, exit_multiple):
	ticker = 'AAPL'
	assumptions = {}
	assumptions['Tax Rate']               = float(tax_rate)/100.0
	assumptions['Growth Rate 1 year out'] = float(growth_rate_1_year_out)/100.0
	assumptions['SGA % of sales']         = float(sga_of_sales)/100.0
	assumptions['D&A % of sales']         = float(da_of_sales)/100.0
	assumptions['CAPEX % of sales']       = float(capex_of_sales)/100.0
	assumptions['NWC % of sales']         = float(nwc_of_sales)/100.0
	assumptions['Exit Multiple']          = float(exit_multiple)

	return calc_dcf(assumptions, ticker)

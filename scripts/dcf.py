#!/usr/bin/python

import sys
sys.path.append('/var/www/html/valumodel.com/scripts')
from calc_dcf import calc_dcf

def create_dcf(req, tax_rate, growth_rate_1_year_out, sga_%_of_sales, d&a_%_of_sales, capex_%_of_sales, nwc_%_of_sales, exit_multiple):
	assumptions = {}
	assumptions['Tax Rate'] = tax_rate
	assumptions['Growth Rate 1 year out'] = growth_rate_1_year_out
	assumptions['SGA % of sales'] = sga_%_of_sales
	assumptions['D&A % of sales'] = d&a_%_of_sales
	assumptions['CAPEX % of sales'] = capex_%_of_sales
	assumptions['NWC % of sales'] = nwc_%_of_sales
	assumptions['Exit Multiple'] = exit_multiple

	return calc_dcf()

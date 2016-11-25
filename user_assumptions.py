#!/usr/bin/python

def user_assumptions(assumptions):
	assumptions['Tax Rate'] = 0.38
	assumptions['Growth Rate 1 year out'] = 0.08
	assumptions['sga % of sales'] = 0.25
	assumptions['d&a % of sales'] = 0.02
	assumptions['capex % of sales'] = 0.02
	assumptions['nwc % of sales'] = 0.07

	return assumptions

## ensure that terminal year d&a = capex
## consider more granular approach for inwc
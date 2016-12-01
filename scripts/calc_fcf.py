#!/usr/bin/python

def calc_fcf(fcf, assumptions, curr_year, historical_years, projected_years):

	### Initialize Earliest year
	fcf[('Growth Rate',(curr_year-3))] = 0
	fcf[('Increase in Net Working Capital',(curr_year-3))] = 0
	
	### Calculate Revenue Growth Rate & Initialize Average Gross Margin
	growth_rate_step_down = (0.03-assumptions['Growth Rate 1 year out'])/4  ## step down until year 5 is between 2% & 4%
	avg_gross_margin = 0.0

	### Calculate Historical Years
	for year in historical_years:
		# REVENUE
		fcf[('Net Working Capital',year)] = assumptions['nwc % of sales']*fcf[('Revenue',year)]
		if year != (curr_year-3):
			fcf[('Growth Rate',year)]  = ((fcf[('Revenue',year)]/fcf[('Revenue',year-1)]) - 1)*100
			fcf[('Increase in Net Working Capital',year)] = fcf[('Net Working Capital',year)] - fcf[('Net Working Capital',year-1)]
		# COGS
		fcf[('Gross Profit',year)]   = fcf[('Revenue',year)]      - fcf[('Cost of Goods Sold',year)]
		fcf[('Gross Margin', year)]  = (fcf[('Gross Profit',year)] / fcf[('Revenue',year)])*100
		# SGA
		fcf[('EBITDA',year)]         = fcf[('Gross Profit',year)] - fcf[('Selling, General, & Administrative',year)]
		# D&A
		fcf[('EBIT',year)]           = fcf[('EBITDA',year)]       - fcf[('Depreciation & Amortization',year)]
		fcf[('Taxes',year)]          = assumptions['Tax Rate'] * fcf[('EBIT',year)]
		fcf[('EBIAT',year)]          = fcf[('EBIT',year)]         - fcf[('Taxes',year)]
		# D&A
		# CAPEX
		fcf[('Free Cash Flow',year)] = fcf[('EBIAT',year)]        + fcf[('Depreciation & Amortization',year)] - fcf[('Increase in Net Working Capital',year)] - fcf[('Capital Expenditures',year)]
		avg_gross_margin += fcf[('Gross Margin', year)]

	### Calculate Average Gross Margin
	avg_gross_margin = avg_gross_margin/4

	### Calculate Projected Years
	for year in projected_years:
		fcf[('Growth Rate',year)]  = (assumptions['Growth Rate 1 year out'] + ( growth_rate_step_down*(year-curr_year-1) ))*100
		fcf[('Revenue',year)]      = fcf[('Revenue',year-1)] * ((fcf[('Growth Rate',year)]/100)+1)

		fcf[('Gross Margin',year)] = avg_gross_margin
		fcf[('Gross Profit',year)] = (fcf[('Gross Margin',year)]/100)*fcf[('Revenue',year)]
		fcf[('Cost of Goods Sold',year)] = fcf[('Revenue',year)] - fcf[('Gross Profit',year)]
	
		fcf[('Selling, General, & Administrative',year)] = assumptions['sga % of sales']*fcf[('Revenue',year)]
		fcf[('EBITDA',year)] = fcf[('Gross Profit',year)] - fcf[('Selling, General, & Administrative',year)]
	
		fcf[('Depreciation & Amortization',year)] = assumptions['d&a % of sales']*fcf[('Revenue',year)]
		fcf[('EBIT',year)] = fcf[('EBITDA',year)]       - fcf[('Depreciation & Amortization',year)]
		fcf[('Taxes',year)] = assumptions['Tax Rate'] * fcf[('EBIT',year)]
		fcf[('EBIAT',year)] = fcf[('EBIT',year)]         - fcf[('Taxes',year)]
		# D&A
		fcf[('Capital Expenditures',year)] = assumptions['capex % of sales']*fcf[('Revenue',year)]
		fcf[('Net Working Capital',year)] = assumptions['nwc % of sales']*fcf[('Revenue',year)]
		fcf[('Increase in Net Working Capital',year)] = fcf[('Net Working Capital',year)] - fcf[('Net Working Capital',year-1)]
		fcf[('Free Cash Flow',year)] = fcf[('EBIAT',year)]        + fcf[('Depreciation & Amortization',year)] - fcf[('Increase in Net Working Capital',year)] - fcf[('Capital Expenditures',year)]

	return fcf
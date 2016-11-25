#!/usr/bin/python

from jinja2 import Environment, FileSystemLoader

def output(fcf, curr_year, historical_years, projected_years):
	data_fields = ['Revenue', 'Cost of Goods Sold', 'Selling, General, & Administrative', 'Depreciation & Amortization', 'Capital Expenditures']
	user_fields = ['Growth Rate', 'Selling, General, & Administrative', 'Depreciation & Amortization', 'Capital Expenditures']
	important_fields = ['Revenue','Gross Profit', 'EBITDA', 'EBIT', 'EBIAT', 'Free Cash Flow']
	
	years = historical_years + projected_years
	rows = ['Revenue', 'Growth Rate', 'Cost of Goods Sold', 'Gross Profit', 'Gross Margin', 'Selling, General, & Administrative', 'EBITDA', 'Depreciation & Amortization', 'EBIT', 'Taxes', 'EBIAT', 'Depreciation & Amortization', 'Increase in Net Working Capital', 'Capital Expenditures', 'Free Cash Flow']

	for row in rows:
		for year in years:
			if row is 'Growth Rate' or row is 'Gross Margin':
				fcf[(row,year)] = str( round( fcf[(row, year)],1) )+"%"
			else:
				fcf[(row,year)] = round( fcf[(row,year)],1)
			
	for row in rows:
		for year in years:
			if fcf[(row,year)]==0:
				fcf[(row,year)] = '-'
				
	fcf[('Growth Rate',(curr_year-3))] = ""
	fcf[('Increase in Net Working Capital',(curr_year-3))] = ""

	env = Environment(loader = FileSystemLoader('/Users/willjmarkley/Desktop/valumodel.com'))
	template = env.get_template('dcf.html')
	print template.render(rows=rows, historical_years=historical_years, fcf=fcf, projected_years=projected_years, years=years, data_fields=data_fields, user_fields=user_fields, important_fields=important_fields)

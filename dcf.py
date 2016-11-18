#!/usr/bin/python

import datetime
from jinja2 import Environment, FileSystemLoader

##### Global Variables (Dictionaries)

### Tuple, Value Dictionaries (field, year) = value
fcf = {}

### Key, Value Dictionaries [field] = value
enterprise_value = {}
implied_equity_value = {}
implied_perpetuity_growth_rate = {}
implied_EV_EBITA = {}
assumptions = {}



##### Acquire Data from Database / Update Database

data_fields = ['Revenue', 'Cost of Goods Sold', 'Selling, General, & Administrative', 'Depreciation & Amortization', 'Capital Expenditures']
user_fields = ['Growth Rate', 'Selling, General, & Administrative', 'Depreciation & Amortization', 'Capital Expenditures']
important_fields = ['Revenue','Gross Profit', 'EBITDA', 'EBIT', 'EBIAT', 'Free Cash Flow']

#curr_year = datetime.datetime.now().year
curr_year = 2008
historical_years = [2005, 2006, 2007, 2008]
projected_years = [2009, 2010, 2011, 2012, 2013]
years = historical_years + projected_years
data_revenue = [780.0, 850.0, 925.0, 1000.0, 1080.0, 1144.8, 1190.6, 1226.3, 1263.1]
#data_ebita = [109.2, 123.3, 138.8, 150.0, 162.0, 171.1, 178.6, 183.9, 189.5]
data_cogs = [471.9, 512.1, 555.0, 600.0, 0,0,0,0,0]
#48.0, 686.9, 714.4, 735.8, 757.9]
data_sga = [198.9, 214.6, 231.3, 250.0, 0,0,0,0,0]
#270.0, 286.2, 297.6, 306.6, 315.8]
data_d_a = [15.6, 17.0, 18.5, 20.0, 0,0,0,0,0]
#21.6, 22.9, 23.8, 24.5, 25.3]
data_capex = [15.0, 18.0, 18.5, 20.0, 0,0,0,0,0]
#21.6, 22.9, 23.8, 24.5, 25.3]
data_inwc = [0.0, 0.0, 0.0, 0.0, 0,0,0,0,0]
#8, 6.5, 4.6, 3.6, 3.7]
data_wacc = 0.11

i=0
for year in years:
	key = ('Revenue',year) 
	fcf[key] = data_revenue[i]
	key = ('Cost of Goods Sold',year)
	fcf[key] = data_cogs[i]
	key = ('Selling, General, & Administrative',year)
	fcf[key] = data_sga[i]
	key = ('Depreciation & Amortization',year)
	fcf[key] = data_d_a[i]
	key = ('Capital Expenditures',year)
	fcf[key] = data_capex[i]
	key = ('Increase in Net Working Capital',year)
	fcf[key] = data_inwc[i]
	i = i+1


##### Acquire Assumptions from User

tax_rate = 0.38
growth_rate_1_year_out = 0.08
sga_percentage_of_sales = 0.25
d_a_percentage_of_sales = 0.02
capex_percentage_of_sales = 0.02
## ensure that terminal year d&a = capex

## have user input capex projections or project as % of sales

## project NWC as percentage of sales or have user input data
## calc YoY changes
##### May NEED a lot of Calculations for this

##### Calculate formulae of DCF

fcf[('Growth Rate',(curr_year-3))] = 0
## step down until year 5 is between 2% & 4%
growth_rate_step_down = (0.03-growth_rate_1_year_out)/4
avg_gross_margin = 0.0

for year in historical_years:
	# REVENUE
	if year != (curr_year-3):
		fcf[('Growth Rate',year)]  = ((fcf[('Revenue',year)]/fcf[('Revenue',year-1)]) - 1)*100
	# COGS
	fcf[('Gross Profit',year)]   = fcf[('Revenue',year)]      - fcf[('Cost of Goods Sold',year)]
	fcf[('Gross Margin', year)]  = (fcf[('Gross Profit',year)] / fcf[('Revenue',year)])*100
	# SGA
	fcf[('EBITDA',year)]         = fcf[('Gross Profit',year)] - fcf[('Selling, General, & Administrative',year)]
	# D&A
	fcf[('EBIT',year)]           = fcf[('EBITDA',year)]       - fcf[('Depreciation & Amortization',year)]
	fcf[('Taxes',year)]          = tax_rate * fcf[('EBIT',year)]
	fcf[('EBIAT',year)]          = fcf[('EBIT',year)]         - fcf[('Taxes',year)]
	# D&A
	# CAPEX
	fcf[('Free Cash Flow',year)] = fcf[('EBIAT',year)]        + fcf[('Depreciation & Amortization',year)] - fcf[('Increase in Net Working Capital',year)] - fcf[('Capital Expenditures',year)]
	avg_gross_margin += fcf[('Gross Margin', year)]

avg_gross_margin = avg_gross_margin/4

for year in projected_years:
	fcf[('Growth Rate',year)]  = (growth_rate_1_year_out+ ( growth_rate_step_down*(year-curr_year-1) ))*100
	fcf[('Revenue',year)]      = fcf[('Revenue',year-1)] * ((fcf[('Growth Rate',year)]/100)+1)

	fcf[('Gross Margin',year)] = avg_gross_margin
	fcf[('Gross Profit',year)] = (fcf[('Gross Margin',year)]/100)*fcf[('Revenue',year)]
	fcf[('Cost of Goods Sold',year)] = fcf[('Revenue',year)] - fcf[('Gross Profit',year)]
	
	fcf[('Selling, General, & Administrative',year)] = sga_percentage_of_sales*fcf[('Revenue',year)]
	fcf[('EBITDA',year)] = fcf[('Gross Profit',year)] - fcf[('Selling, General, & Administrative',year)]
	
	fcf[('Depreciation & Amortization',year)] = d_a_percentage_of_sales*fcf[('Revenue',year)]
	fcf[('EBIT',year)] = fcf[('EBITDA',year)]       - fcf[('Depreciation & Amortization',year)]
	fcf[('Taxes',year)] = tax_rate * fcf[('EBIT',year)]
	fcf[('EBIAT',year)] = fcf[('EBIT',year)]         - fcf[('Taxes',year)]
	# D&A
	fcf[('Capital Expenditures',year)] = capex_percentage_of_sales*fcf[('Revenue',year)]
	fcf[('Free Cash Flow',year)] = fcf[('EBIAT',year)]        + fcf[('Depreciation & Amortization',year)] - fcf[('Increase in Net Working Capital',year)] - fcf[('Capital Expenditures',year)]

##### Create HTML/XML output of DCF
	


## JUST PRINT


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

env = Environment(loader = FileSystemLoader('/Users/willjmarkley/Desktop/valumodel.com'))
template = env.get_template('dcf.html')
print template.render(rows=rows, historical_years=historical_years, fcf=fcf, projected_years=projected_years, years=years, data_fields=data_fields, user_fields=user_fields, important_fields=important_fields)


'''
print '\n\n'
print '\t\t\t\t\t\t\t',
for year in years:
	print str(year)+'\t',

print
for field in lines:
	print '{:34s} \t\t\t'.format(field),
	for year in years:
		print str(fcf[(field,year)]) + '\t',
	print
	
print 'Unlevered Free Cash Flow'
lines = ['WACC', 'Discount Period', 'Discount Factor', 'Present Value of Free Cash Flow']
for field in lines:
	print '\t'+field

print '\n\n'

'''


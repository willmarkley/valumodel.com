#!/usr/bin/python

import datetime

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

curr_year = datetime.datetime.now().year

historical_years = [2005, 2006, 2007, 2008]
projected_years = [2009, 2010, 2011, 2012, 2013]
years = historical_years + projected_years
data_revenue = [780.0, 850.0, 925.0, 1000.0, 1080.0, 1144.8, 1190.6, 1226.3, 1263.1]
#data_ebita = [109.2, 123.3, 138.8, 150.0, 162.0, 171.1, 178.6, 183.9, 189.5]
data_cogs = [471.9, 512.1, 555.0, 600.0, 648.0, 686.9, 714.4, 735.8, 757.9]
data_sga = [198.9, 214.6, 231.3, 250.0, 270.0, 286.2, 297.6, 306.6, 315.8]
data_d_a = [15.6, 17.0, 18.5, 20.0, 21.6, 22.9, 23.8, 24.5, 25.3]
data_capex = [15.0, 18.0, 18.5, 20.0, 21.6, 22.9, 23.8, 24.5, 25.3]
data_inwc = [0, 0, 0, 0, 0, 0, 0, 0, 0]
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



##### Calculate formulae of DCF


for year in historical_years:
	fcf[('Gross Profit',year)]   = fcf[('Revenue',year)]      - fcf[('Cost of Goods Sold',year)]
	fcf[('EBITDA',year)]         = fcf[('Gross Profit',year)] - fcf[('Selling, General, & Administrative',year)]
	fcf[('EBIT',year)]           = fcf[('EBITDA',year)]       - fcf[('Depreciation & Amortization',year)]
	fcf[('Taxes',year)]          = tax_rate * fcf[('EBIT',year)]
	fcf[('EBIAT',year)]          = fcf[('EBIT',year)]         - fcf[('Taxes',year)]
	fcf[('Free Cash Flow',year)] = fcf[('EBIAT',year)]        + fcf[('Depreciation & Amortization',year)] - fcf[('Increase in Net Working Capital',year)] - fcf[('Capital Expenditures',year)]

for year in projected_years:
	fcf[('Gross Profit',year)] = 7777
	fcf[('EBITDA',year)] = 7777
	fcf[('EBIT',year)] = 7777
	fcf[('Taxes',year)] = 7777
	fcf[('EBIAT',year)] = 7777
	fcf[('Free Cash Flow',year)] = 7777

##### Create HTML/XML output of DCF




## JUST PRINT

print '\n\n'

lines = ['Revenue', 'Cost of Goods Sold', 'Gross Profit', 'Selling, General, & Administrative', 'EBITDA', 'Depreciation & Amortization', 'EBIT', 'Taxes', 'EBIAT', 'Depreciation & Amortization', 'Increase in Net Working Capital', 'Capital Expenditures', 'Free Cash Flow']

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

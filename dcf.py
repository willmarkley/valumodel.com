#!/usr/bin/python


##### Global Variables (Dictionaries)

### Tuple, Value Dictionaries (field, year) = value
fcf_historical = {}
fcf_projected = {}

### Key, Value Dictionaries [field] = value
enterprise_value = {}
implied_equity_value = {}
implied_perpetuity_growth_rate = {}
implied_EV_EBITA = {}
assumptions = {}



##### Acquire Data from Database / Update Database

historical_years = [2005, 2006, 2007, 2008]
projected_years = [2009, 2010, 2011, 2012, 2013]
data_sales_h = [780.0, 850.0, 925.0, 1000.0]
data_sales_p = [1080.0, 1144.8, 1190.6, 1226.3, 1263.1]

data_ebita_h = [109.2, 123.3, 138.8, 150.0]
data_ebita_p = [162.0, 171.1, 178.6, 183.9, 189.5]


i=0
for year in historical_years:
	key = ('Sales',year) 
	fcf_historical[key] = data_sales_h[i]
	key = ('EBITA',year)
	fcf_historical[key] = data_ebita_h[i]
	i = i+1
	
i=0
for year in projected_years:
	key = ('Sales',year) 
	fcf_projected[key] = data_sales_p[i]
	key = ('EBITA',year)
	fcf_projected[key] = data_ebita_p[i]
	i = i+1


##### Acquire Assumptions from User





##### Calculate formulae of DCF





##### Create HTML/XML output of DCF




## JUST PRINT

lines = ["Sales", "EBITA"]

for field in lines:
	print field + '\t',
	for year in historical_years:
		print str(fcf_historical[(field,year)]) + '\t',
	for year in projected_years:
		print str(fcf_projected[(field,year)]) + '\t',
	print

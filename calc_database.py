#!/usr/bin/python

def calc_database(fcf, historical_years):
	data_revenue = [780.0, 850.0, 925.0, 1000.0]
	#, 1080.0, 1144.8, 1190.6, 1226.3, 1263.1]
	data_cogs = [471.9, 512.1, 555.0, 600.0, 0,0,0,0,0]
	data_sga = [198.9, 214.6, 231.3, 250.0, 0,0,0,0,0]
	data_d_a = [15.6, 17.0, 18.5, 20.0, 0,0,0,0,0]
	data_capex = [15.0, 18.0, 18.5, 20.0, 0,0,0,0,0]

	i=0
	for year in historical_years:
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
		i = i+1
		
	return fcf
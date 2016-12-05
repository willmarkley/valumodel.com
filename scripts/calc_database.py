#!/usr/bin/python

import sys
sys.path.append('/home/ec2-user/apache_httpd_server')
#import quandl
from quandlapikey import quandlapikey

def calc_database(ticker, fcf):
	data_revenue = [780.0, 850.0, 925.0, 1000.0]
	#, 1080.0, 1144.8, 1190.6, 1226.3, 1263.1]
	data_cogs = [471.9, 512.1, 555.0, 600.0, 0,0,0,0,0]
	data_sga = [198.9, 214.6, 231.3, 250.0, 0,0,0,0,0]
	data_d_a = [15.6, 17.0, 18.5, 20.0, 0,0,0,0,0]
	data_capex = [15.0, 18.0, 18.5, 20.0, 0,0,0,0,0]

	i=0
	curr_year=2016
	historical_years = [curr_year-3, curr_year-2, curr_year-1, curr_year]
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
		
	return (2016, fcf)

'''
	quandl.ApiConfig.api_key = quandlapikey
	indicators = [('REVENUE','Revenue'), ('GP','Cost of Goods Sold'), ('SGNA','Selling, General, & Administrative'), ('DEPAMOR','Depreciation & Amortization'), ('CAPEX','Capital Expenditures')]

	for indicator in indicators:
		code = 'SF0/'+ticker+'_'+indicator[0]+'_MRY'    ### generate database call
		try:
                    mydata = quandl.get(code, rows=4, returns="numpy")   ### return most recent 4 years as numpy array
		except:
                    print '<!doctype html><html><body><h1>Ticker not supported.  Please try another company.</h1></body></html>'
                    sys.exit()
                if indicator[0] is 'REVENUE':
			curr_year = mydata[-1][0].year   ### access last array's (most recent) datetime object's year attribute

		i=0
		start_year=curr_year-3
		for i in range(4):
			if indicator[0] is 'GP':    ### Revenue - Gross Profit = COGS
				fcf[(indicator[1],start_year+i)] = (fcf[('Revenue',start_year+i)] - mydata[i][1]/1000000)
			elif indicator[0] is 'CAPEX':  ### make capex positive
				fcf[(indicator[1],start_year+i)] = -1*mydata[i][1]/1000000   ### access value of indicator in a year
			else:
				fcf[(indicator[1],start_year+i)] = mydata[i][1]/1000000   ### access value of indicator in a year

	return (curr_year, fcf)

'''

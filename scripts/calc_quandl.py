#!/usr/bin/python

import sys
sys.path.append('/home/ec2-user/apache_httpd_server')
import quandl
from quandlapikey import quandlapikey
import yaml
import getopt

ticker = sys.argv[1]

quandl.ApiConfig.api_key = quandlapikey
indicators = [('REVENUE','Revenue'), ('GP','Cost of Goods Sold'), ('SGNA','Selling, General, & Administrative'), ('DEPAMOR','Depreciation & Amortization'), ('CAPEX','Capital Expenditures')]

for indicator in indicators:
	code = 'SF0/'+ticker+'_'+indicator[0]+'_MRY'    ### generate database call
	try:
		mydata = quandl.get(code, rows=4, returns="numpy")   ### return most recent 4 years as numpy array
	except:
		print '-1^^',
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
			

print curr_year,
print yaml.dump(fcf)
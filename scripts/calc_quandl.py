#!/usr/bin/python

import sys
sys.path.append('/home/ec2-user/apache_httpd_server')
import quandl
#from quandlapikey import quandlapikey
import yaml

ticker = sys.argv[1]

#quandl.ApiConfig.api_key = quandlapikey
quandl.ApiConfig.api_key = 'PVS8XsdfoZhuSS34A__o'
indicators = [('REVENUE','Revenue'), ('GP','Cost of Goods Sold'), ('SGNA','Selling, General, & Administrative'), ('DEPAMOR','Depreciation & Amortization'), ('CAPEX','Capital Expenditures')]
fcf = {}
wacc = {}

### Balance Sheet Items
for indicator in indicators:
	code = 'SF0/'+ticker+'_'+indicator[0]+'_MRY'    ### generate database call
	try:
		mydata = quandl.get(code, rows=4, returns="numpy")   ### return most recent 4 years as numpy array
	except:
		print '-1^^'
		print '<!doctype html><html><body><h1>Ticker not supported.  Please try another company.</h1></body></html>'
		sys.exit(0)
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

### Total Debt & Equity
for indicator in [('DEBT','Total Debt'), ('EQUITY','Total Equity')]:
	code = 'SF0/'+ticker+'_'+indicator[0]+'_MRY'    ### generate database call
	try:
		mydata = quandl.get(code, rows=1, returns="numpy")   ### return most recent 4 years as numpy array
	except:
		print '-1^^'
		print '<!doctype html><html><body><h1>Ticker not supported.  Please try another company.</h1></body></html>'
		sys.exit(0)
	
	wacc[indicator[1]] = mydata[0][1]


### Risk Free Rate (10 year Treasury)
code = 'FRED/DGS10'    ### generate database call
try:
		mydata = quandl.get(code, rows=1, returns="numpy")   ### return most recent 4 years as numpy array
except:
	print '-1^^'
	print '<!doctype html><html><body><h1>Ticker not supported.  Please try another company.</h1></body></html>'
	sys.exit(0)

wacc['Risk Free Rate'] = mydata[0][1]/100  ## convert percentage to fraction

print str(curr_year)+'^^'
print yaml.dump(fcf)+'^^'

sys.exit(0)

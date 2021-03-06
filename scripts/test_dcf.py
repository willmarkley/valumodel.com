#!/usr/bin/python

import sys
sys.path.append('/var/www/html/valumodel.com/scripts/dcf')
from calc_dcf import calc_dcf


ticker = 'NFLX'
assumptions = {}
assumptions['Tax Rate']               = 0.07
assumptions['Growth Rate 1 year out'] = 0.07
assumptions['SGA % of sales']         = 0.07
assumptions['D&A % of sales']         = 0.07
assumptions['CAPEX % of sales']       = 0.07
assumptions['NWC % of sales']         = 0.07
assumptions['Levered Beta']           = 1.2
assumptions['Current Yield']          = 0.07
assumptions['Exit Multiple']          = 0.07

print calc_dcf(assumptions, ticker)

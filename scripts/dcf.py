#!/usr/bin/python

import sys
sys.path.append('/var/www/html/valumodel.com/scripts')
from calc_dcf import calc_dcf

def create_dcf(req):
	return calc_dcf()

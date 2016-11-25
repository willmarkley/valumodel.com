#!/usr/bin/python

import datetime
from calc_fcf import calc_fcf
from user_assumptions import user_assumptions
from calc_database import calc_database
from output import output

##### Global Variables (Dictionaries)

### Tuple, Value Dictionaries (field, year) = value
fcf = {}

### Key, Value Dictionaries [field] = value
wacc = {}
enterprise_value = {}
implied_equity_value = {}
implied_perpetuity_growth_rate = {}
implied_EV_EBITA = {}
assumptions = {}


#curr_year = datetime.datetime.now().year
curr_year = 2008
### Initialize years
historical_years = [curr_year-3, curr_year-2, curr_year-1, curr_year]
projected_years  = [curr_year+1, curr_year+2, curr_year+3, curr_year+4, curr_year+5]

total_debt = 40
debt_coupon_rate = 0.06
debt_par_value = 1000
debt_market_price = 900
total_equity = 100


fcf = calc_database(fcf, historical_years)
assumptions = user_assumptions(assumptions)
fcf         = calc_fcf(fcf, assumptions, curr_year, historical_years, projected_years)
output(fcf, curr_year, historical_years, projected_years)


###### Calculate WACC

percent_debt = total_debt / (total_debt + total_equity)
percent_equity = 1 - percent_debt

debt_cash_inflows = debt_coupon_rate * debt_par_value
current_yield = debt_cash_inflows/debt_market_price
cost_of_debt = current_yield*(1-assumptions['Tax Rate'])

#!/usr/bin/python

def calc_wacc(wacc, assumptions):
	### Get from Database	
	total_debt = 40.0
	debt_coupon_rate = 0.06
	debt_par_value = 3000.0
	debt_market_price = 900.0
	total_equity = 60.0
	risk_free_rate = 1.83/100 ## US 10 year Treasury Yield
	market_risk_premium = 0.071
	levered_beta = 1.2   ### have user enter
		
	wacc['% Debt']   = total_debt / (total_debt + total_equity)
	wacc['% Equity'] = 1 - wacc['% Debt']
	wacc['% Debt']   = wacc['% Debt']*100
	wacc['% Equity'] = wacc['% Equity']*100

	debt_cash_inflows = (float)(debt_coupon_rate * debt_par_value)
	current_yield = (debt_cash_inflows)/debt_market_price
	wacc['Cost of Debt'] = (current_yield*(1-assumptions['Tax Rate']))*100
	
	## Capital Asset Pricing Model
	
	wacc['Cost of Equity'] = (risk_free_rate + (levered_beta*market_risk_premium))*100
	wacc['WACC']           = (wacc['Cost of Debt']*wacc['% Debt'] + wacc['Cost of Equity']*wacc['% Equity'])/100
	
	return wacc

### should probably create sensitivity table
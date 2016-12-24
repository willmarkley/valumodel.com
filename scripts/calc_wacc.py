#!/usr/bin/python

def calc_wacc(wacc, assumptions):
	### Get from Database	
	debt_coupon_rate = 0.06
	debt_par_value = 3000.0
	debt_market_price = 900.0
	assumptions['Levered Beta'] = 1.2   ### have user enter
	
	market_risk_premium = 0.071  ### Constant
		
	wacc['% Debt']   = wacc['Total Debt'] / float(wacc['Total Debt'] + wacc['Total Equity'])
	wacc['% Equity'] = 1 - wacc['% Debt']
	wacc['% Debt']   = wacc['% Debt']*100
	wacc['% Equity'] = wacc['% Equity']*100

	debt_cash_inflows = (float)(debt_coupon_rate * debt_par_value)
	current_yield = (debt_cash_inflows)/debt_market_price
	wacc['Cost of Debt'] = (current_yield*(1-assumptions['Tax Rate']))*100
	
	## Capital Asset Pricing Model
	
	wacc['Cost of Equity'] = (wacc['Risk Free Rate'] + (assumptions['Levered Beta']*market_risk_premium))*100
	wacc['WACC']           = (wacc['Cost of Debt']*wacc['% Debt'] + wacc['Cost of Equity']*wacc['% Equity'])/100
	
	return wacc

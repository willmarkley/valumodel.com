#!/usr/bin/python

def calc_wacc(wacc, assumptions):
	market_risk_premium = 0.071  ### Constant
		
	wacc['% Debt']   = wacc['Total Debt'] / float(wacc['Total Debt'] + wacc['Total Equity'])
	wacc['% Equity'] = 1 - wacc['% Debt']
	wacc['% Debt']   = wacc['% Debt']*100
	wacc['% Equity'] = wacc['% Equity']*100

	#debt_cash_inflows = (float)(debt_coupon_rate * debt_par_value)
	#current_yield = (debt_cash_inflows)/debt_market_price
	wacc['Cost of Debt'] = (assumptions['Current Yield']*(1-assumptions['Tax Rate']))*100
	
	## Capital Asset Pricing Model
	
	wacc['Cost of Equity'] = (wacc['Risk Free Rate'] + (assumptions['Levered Beta']*market_risk_premium))*100
	wacc['WACC']           = (wacc['Cost of Debt']*wacc['% Debt'] + wacc['Cost of Equity']*wacc['% Equity'])/100
	
	return wacc

#!/usr/bin/python

def calc_enter_val(enterprise_value, assumptions, fcf, wacc, curr_year, projected_years):

	enterprise_value['Cumulative Present Value of FCF'] = 0
	for year in projected_years:
		fcf[('Discount Factor',year)]                        = 1/((1+(wacc['WACC'])/100)**(year-curr_year))
		fcf[('Present Value of Free Cash Flow',year)]        = fcf[('Free Cash Flow',year)]*fcf[('Discount Factor',year)]
		enterprise_value['Cumulative Present Value of FCF'] += fcf[('Present Value of Free Cash Flow',year)]

	
	enterprise_value['Terminal Year EBITDA'] = fcf[('EBITDA',projected_years[4])]
	enterprise_value['Exit Multiple'] = assumptions['Exit Multiple']
	
	enterprise_value['Terminal Value'] = enterprise_value['Exit Multiple']*enterprise_value['Terminal Year EBITDA']
	enterprise_value['Discount Factor'] = fcf[('Discount Factor',projected_years[4])]
	enterprise_value['Present Value of Terminal Value'] = enterprise_value['Terminal Value']*enterprise_value['Discount Factor']
	
	enterprise_value['Enterprise Value'] = enterprise_value['Cumulative Present Value of FCF']+enterprise_value['Present Value of Terminal Value']
	
	return enterprise_value
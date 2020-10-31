#!/usr/bin/python3

import pandas as pd
from os import listdir
from optparse import OptionParser

payments = {
		"01" : [],
		"02" : [],
		"03" : [],
		"04" : [],
		"05" : [],
		"06" : [],
		"07" : [],
		"08" : [],
		"09" : [],
		"10" : [],
		"11" : [],
		"12" : [],
	}

months = {
		"01":"January",
		"02":"February",
		"03":"March",
		"04":"April",
		"05":"May",
		"06":"June",
		"07":"July",
		"08":"August",
		"09":"September",
		"10":"October",
		"11":"November",
		"12":"December",
	}

quarters = {
		"1" : ["01", "02", "03"],
		"2" : ["04", "05", "06"],
		"3" : ["07", "08", "09"],
		"4" : ["10", "11", "12"]
}

def compute_monthly_total():
	for stat in listdir('../pay_statements'):
		file = str('../pay_statements/'+stat)
		month = stat[-14:-12]
		read = pd.read_csv(file)
		payments[month].extend(read['Total'].values)
		if(payments[month] == None):
			payments[month].extend(read['Totaal'].values)

def print_summary_month(index):
	#print(payments[index])
	print('Following is the total of all payments occurred in '+months[index])
	print('namely the sum, delivered to your Uber account, of each delivery')
	print('TIPS ARE NOT INCLUDED')
	tmp = []
	for x in payments[index]:
		tmp.append(float(x[1:]))
	total = sum(tmp)
	print('\tomzet is: '+str(total)+' euro')
	print('\tof which 21% are taxes (omzetbelasting): '+str('%.2f' % (total/100*21))+ ' euro')
	print('\tnetto: '+str('%.2f' % (total - total/100*21))+' euro')

def print_summary_quarter(index):
	#print(payments[index])
	print('Following is the total of all payments occurred in quarter '+ index
			+ ', namely for the months of ' + months[quarters[index][0]] + ", "
									  	  + months[quarters[index][1]] + " and "
									      + months[quarters[index][2]] + ", "
										  "to your Uber account for each delivery")
	print('TIPS ARE NOT INCLUDED')
	tmp = []
	for month in quarters[index]:
		for x in payments[month]:
			tmp.append(float(x[1:]))
	total = sum(tmp)
	print('\tomzet is: '+str(total)+' euro')
	print('\tof which 21% are taxes (omzetbelasting): '+str('%.2f' % (total/100*21))+ ' euro')
	print('\tnetto: '+str('%.2f' % (total - total/100*21))+' euro')

def print_summary_year(index):
	#print(payments[index])
	print('Following is the total of all payments occurred in '+index)
	print('namely the sum of money delivered to your Uber account for each delivery during this period')
	print('TIPS ARE NOT INCLUDED')
	tmp = []
	for x in payments[index]:
		tmp.append(float(x[1:]))
	total = sum(tmp)
	print('\tomzet is: '+str(total)+' euro')
	print('\tof which 21% are taxes (omzetbelasting): '+str('%.2f' % (total/100*21))+ ' euro')
	print('\tnetto: '+str('%.2f' % (total - total/100*21))+' euro')


if __name__ == '__main__':
	try:
		parse = OptionParser()
		parse.add_option("-m", "--month", dest="month",
                  help="specify a month as a 2 digit value")
		parse.add_option("-y", "--year", dest="year",
                  help="specify an year as a 4 digit value")
		parse.add_option("-q", "--quarter", dest="quarter",
                  help="specify a quarter as a number from 1 to 4")
		(options, args) = parse.parse_args()
		if options.month:
			compute_monthly_total()
			print_summary_month(options.month)
		elif options.quarter:
			compute_monthly_total()
			print_summary_quarter(options.quarter)
		elif options.year:
			compute_monthly_total()
			print_summary_year(options.year)
		else:
			parse.print_help()
			parse.error('an option must be specified')
	except Exception as e:
		print(e)

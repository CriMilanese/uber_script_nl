#!/usr/bin/python3

import pandas as pd
from os import listdir
from optparse import OptionParser
from unit_test.validation import Validator
from datetime import datetime

this_year = datetime.now().strftime("%Y")

string_format = {
    "01": "January",
    "02": "February",
    "03": "March",
    "04": "April",
    "05": "May",
    "06": "June",
    "07": "July",
    "08": "August",
    "09": "September",
    "10": "October",
    "11": "November",
    "12": "December"
}

payments = {
    "2019" : {},
    "2020" : {},
    "2021" : {},
    "2022" : {},
    "2023" : {}
}

quarters = {
    "1": ["01", "02", "03"],
    "2": ["04", "05", "06"],
    "3": ["07", "08", "09"],
    "4": ["10", "11", "12"]
}

def init_dict():
    for year in payments:
        payments[year] = {
            "01": [],
            "02": [],
            "03": [],
            "04": [],
            "05": [],
            "06": [],
            "07": [],
            "08": [],
            "09": [],
            "10": [],
            "11": [],
            "12": []
        }


def compute_monthly_total():
    for stat in listdir('../pay_statements'):
        file = str('../pay_statements/' + stat)
        month = stat[-14:-12]
        year = stat[-8:-4]
        read = pd.read_csv(file)
        if(read.get('Total') is not None):
            payments[year][month].extend(read['Total'].values)
        elif (read.get('Totaal') is not None):
            payments[year][month].extend(read['Totaal'].values)
        else:
            raise KeyError('column name not found')


def print_summary_month(index, year = this_year):
    # print(string_format[index])
    year_string = year if year != this_year else "this year"
    print('Following is the total of all payments occurred in ' +
          string_format[index] + " of "+year_string)
    print('namely the sum, transferred to your Uber account, of all deliveries')
    print('TIPS ARE NOT INCLUDED')
    tmp = []
    for x in payments[year][index]:
        tmp.append(float(x[1:]))
    total = sum(tmp)
    print('\tomzet is: ' + str('%.2f' % total) + ' euro')
    print('\tof which 21% are taxes (omzetbelasting): ' +
          str('%.2f' % (total / 100 * 21)) + ' euro')
    print('\tnetto: ' + str('%.2f' % (total - total / 100 * 21)) + ' euro')


def print_summary_quarter(index, year = this_year):
    year_string = year if year != this_year else "this year"
    print('Following is the total of all payments, occurred in quarter ' + index
          + ', namely for the months of ' + string_format[quarters[index][0]] + ", "
          + string_format[quarters[index][1]] + " and "
          + string_format[quarters[index][2]] + " of "+ year_string + ", "
          "to your Uber account for each delivery")
    print('TIPS ARE NOT INCLUDED')
    tmp = []
    for month in quarters[index]:
        for x in payments[year][month]:
            tmp.append(float(x[1:]))
    total = sum(tmp)
    print('\tomzet is: ' + str('%.2f' % total) + ' euro')
    print('\tof which 21% are taxes (omzetbelasting): ' +
          str('%.2f' % (total / 100 * 21)) + ' euro')
    print('\tnetto: ' + str('%.2f' % (total - total / 100 * 21)) + ' euro')


def print_summary_year(index, year = this_year):
    year_string = year if year != this_year else "this year"
    print('Following is the total of all payments occurred in ' + index)
    print('namely the sum of money transferred to your Uber account \n for each delivery during this period')
    print('TIPS ARE NOT INCLUDED')
    tmp = []
    for x in payments[year].keys():
        for y in payments[year][x]:
            tmp.append(float(y[1:]))
    total = sum(tmp)
    print('\tomzet is: ' + str('%.2f' % total) + ' euro')
    print('\tof which 21% are taxes (omzetbelasting): ' +
          str('%.2f' % (total / 100 * 21)) + ' euro')
    print('\tnetto: ' + str('%.2f' % (total - total / 100 * 21)) + ' euro')


if __name__ == '__main__':
    try:
        init_dict()
        check = Validator()
        parse = OptionParser()
        parse.add_option("-m", "--month", dest="month",
                         help="specify a month as a value between 1 and 12")
        parse.add_option("-y", "--year", dest="year",
                         help="specify an year as a 4 digit value")
        parse.add_option("-q", "--quarter", dest="quarter",
                         help="specify a quarter as a number from 1 to 4")
        (options, args) = parse.parse_args()
        if options.month:
            if(check.month_is_valid(options.month)):
                compute_monthly_total()
                print_summary_month(options.month, options.year) if options.year else print_summary_month(options.month)
            else:
                raise ValueError('month value is invalid')
        elif options.quarter:
            if(options.month):
                raise ValueError("months are already specified")
            if(check.quarter_is_valid(options.quarter)):
                compute_monthly_total()
                print_summary_quarter(options.quarter, options.year) if options.year else print_summary_quarter(options.quarter)
            else:
                raise ValueError('incorrect quarter value')
        elif options.year:
            compute_monthly_total()
            print_summary_year(options.year)
        else:
            parse.error('an options error occurred')
            parse.print_help()
    except KeyError as e:
        print("You need to use two digits, so if you need month 8 then you type \"-m 08\"")
    except Exception as e:
        print(e)
        parse.print_help()

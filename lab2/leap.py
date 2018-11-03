# -*- coding: utf-8 -*-
import calendar

def check_leap_year_using_lib(year):
    if calendar.isleap(year):
        print(year,"is a leap year")
    else:
        print(year,"is not a leap year")

def check_leap_year_using_algo(year):
    if year % 400 == 0:
        print(year, "is a leap year")
    elif year % 100 == 0:
        print(year, "is not a leap year")
    elif year % 4 == 0:
        print(year, "is a leap year")
    else:
        print(year, "is not a leap year")

if __name__ == '__main__':
    year = int(input("Enter a year A.D.: "))
    check_leap_year_using_lib(year)
    #check_leap_year_using_algo(year)


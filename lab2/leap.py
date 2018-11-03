# -*- coding: utf-8 -*-
import calendar

def check_leap_year_using_lib(year):
    return calendar.isleap(year)

def check_leap_year_using_algo(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    year = int(input("Enter a year A.D.: "))
    if check_leap_year_using_lib(year):  # check_leap_year_using_algo(year) for
        print(year, "is a leap year")
    else:
        print(year, "is not a leap year")

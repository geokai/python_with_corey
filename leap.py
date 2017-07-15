
# This file was created on 15/07/17
# Author: George Kaimakis - https://github.com/geokai

# this code taken from Corey Schafer's 'generator' tutorial:

# Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    """ Return True for leap years, False for non-leap years. """

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """ Return number of days in that month in that year. """

    # year 2017
    # month 2
    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]


#print(is_leap(2020))
print(days_in_month(2017, 2))

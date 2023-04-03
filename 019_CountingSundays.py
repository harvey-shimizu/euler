'''
Problem #19
Counting Sundays

You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September, April, June and November.
All the rest have thirty-one,
Saving February alone, Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

'''
import math
import datetime

def isSunday_ref(y, m, d):
    if datetime.datetime(y,m,d).weekday() == 6:
        return True
    else:
        return False

def findEndDay(year, month):
    if month in [4, 6, 9, 11]:
        end_day = 30
    elif month in [2]:
        if year % 4 == 0:
            end_day = 29
        else:
            end_day = 28
    else:
        end_day = 31
    return end_day

def isSunday(y, m, d):
    #Adjust year and month for Zeller's congruence
    if m <= 2:
        y -= 1
        m += 12

    C = math.floor(y/100)
    Y = y%100
    # Available for Gregorian calendar after AD.1582.
    if year:
        # Gregorian calendar
        h = ((d+math.floor(13*(m+1)/5)+Y+math.floor(Y/4)+5*C+math.floor(C/4)) % 7)

    if h == 1:
        return True
    else:
        return False

count = 0
for year in range(1901, 2001):
    for month in range(1, 13):
        for day in range(1, findEndDay(year, month)+1):
            if day == 1 and isSunday(year, month, day):
                count += 1
print(count)

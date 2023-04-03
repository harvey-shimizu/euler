'''
Reciprocal cycles
Problem #26

A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
'''
from decimal import *

def checkCycleNumber(l):
    cyclePattern = []
    PreambleLength = PRESICE
    PreamblePattern = l[3:PreambleLength+2]

    if len(PreamblePattern) < 4:
        return False

    cnt = 0
    idx = 0
    p = PreamblePattern
    while len(l[3:-4]) > idx:
        if  l[idx]   == p[0] and l[idx+1] == p[1] and\
            l[idx+2] == p[2] and l[idx+3] == p[3]:
            cnt += 1
            if cnt == 1:
                preidx = idx
        if cnt == 2:
            diff_idx = idx - preidx
            break
        idx += 1
    if cnt == 2:
        cyclePattern = PreamblePattern[:diff_idx]
        return cyclePattern
    return False

def findMaxReciprocalCycle(n):
    PRESICE = 2500
    getcontext().prec = PRESICE
    max = 1
    maxN = 0
    for n in range(1,1000):
        p = Decimal(1)/Decimal(n)
        l = checkCycleNumber(list(str(p)))
        if l:
            if len(l) > max:
                max = len(l)
                maxN = n
    return maxN

# Another solutions
# 24
#import myprime as p
#pl = p.g(1000)
#print(pl[-1])

max_round = 0
divider = 2

while divider < 1000:
    dividend = 1
    remainders = list()

    while True:
        remainder = dividend % divider
        if remainder in remainders:
            first_index = remainders.index(remainder)
            last_index = len(remainders)
            if last_index - first_index > max_round:
                max_round = last_index - first_index
                number = divider
            break
        dividend = 10 * remainder
        remainders.append(remainder)

    divider += 1

print(number)

# Another solutions
'''
Python - String solution
I treated the problem as a string/substring problem. First I generated strings of the decimal of d to 5000 decimal places then did a brute force for substrings of increasing length. It runs in just a few seconds and could be optimized if required.
'''

from decimal import *
# precision of decimal
getcontext().prec = 5000

# [integer d, length of recurrence]
d = [7, 6]
# max integer to test
limit = 1000
# start point for the initial substring
start = 3

# the range of integers to test e.g., 1/i
for i in range(2, limit):
    found = False
    s = str(Decimal(1) / Decimal(i)).split('.')[1]

    ss_len = 6
    while (not found) and (ss_len < len(s)/2):
        end = start + ss_len
        found = False

        if (not found) and (len(s) > end + ss_len):
            ss = s[start: end]
            if ss == s[end: end + ss_len]:
                found = True
                if ss_len > d[1]:
                    d = [i, ss_len]
                    print(d)

        ss_len += 1

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

def getDegitRecurringCycle(n):
    l = list(str(n))
    cyclePattern = {}
    for cnt, digit in zip(range(1, len(l)+1),l[2:-2]):
        cyclePattern[cnt] = digit
#    print(n, cyclePattern)
    if checkCycleNumber(cyclePattern):
        return [x for x in cyclePattern.values()]
    return None

def checkCycleNumber(p):
    preseq = 0
    prevalue = True
    count = 0
    for seq, digit in p.items():
        if seq - presq == 1 and digit ==  prevalue:
            count += 1
        else:
            count = 0
        if count > 10:
            return False
    return True

getcontext().prec = 100
max = 1
for n in range(1,30):
    p = Decimal(1)/Decimal(n)
    l = getDegitRecurringCycle(p)
    if l:
        if len(l) > max:
            max = len(l)
            maxDigit = l
            maxP = n

print(f"1/{maxP}, {max}, {maxDigit}")

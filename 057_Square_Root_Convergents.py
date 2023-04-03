'''
It is possible to show that the square root of two can be expressed as an infinite continued fraction.
By expanding this for the first four iterations, we get:

The next three expansions are , and , but the eighth expansion, , is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator with more digits than the denominator?

'''

import sys
from fractions import Fraction

def getRootSquare(num, depth):
    if depth > 1:
        return 1/(num + getRootSquare(num, depth-1))
    else:
        return 1/num

def getConvergents(num, depth):
    return 1 + getRootSquare(num, depth)

def getRS(num, depth):
    if depth > 1:
        return Fraction(1, num + getRS(num, depth-1))
    else:
        return Fraction(1, num)

def getConv(num, depth):
    return 1 + getRS(num, depth)

#sys.setrecursionlimit(2000)
#print(sys.getrecursionlimit())
# 2000
sys.setrecursionlimit(10 ** 4)
#print(sys.getrecursionlimit())
# 10000

count = 0
for d in range(1,100):
    f = Fraction(getConv(2, d))
    #print(len(str(f.numerator)), len(str(f.denominator)))
    if len(str(f.numerator)) > len(str(f.denominator)):
        count += 1
        print(d, Fraction(getConv(2, d)))
print(count)


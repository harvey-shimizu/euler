'''
Amicable numbers
Problem #21

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''

import myprime as p
import math as m

N = 10000
prime = p.g(N*10)

def sum_of_dividers(num):
    nn = num
    pdict = {}
    n = 0

    # Here is to find primes of the dividers.
    while num > 1:
        pcount = 0
        while num % prime[n] == 0:
            num /= prime[n]
            pcount += 1
            pdict[prime[n]] = pcount
        n += 1

    # Here is a summation of all devisors.
    p = 1
    for k, v in pdict.items():
        s = 0
        for y in range(v+1):
            s += k**y
        p *= s

    return p - nn

def sum_of_amicableDivider(N):
    apair = []
    s = 0
    for n in range(N,1,-1):
        any = sum_of_dividers(n)
        if n == sum_of_dividers(any):
            apair.append((n, any))

    for a, b in apair:
        if a != b:
            s += a

    return s

if __name__ == '__main__':
    print(sum_of_amicableDivider(N))

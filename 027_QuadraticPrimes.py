'''
Quadratic Primes
Problem #27

Euler discovered the remarkable quadratic formula:
    n^2 + n + 41
It turns out that the formula will produce 40 primes for the consecutive integer values .
However, when  is divisible by 41, and certainly when  is clearly divisible by 41.

The incredible formula  was discovered, which produces 80 primes for the consecutive values . The product of the coefficients, −79 and 1601, is −126479.
Considering quadratics of the form:
, where  and

where  is the modulus/absolute value of
e.g.  and
Find the product of the coefficients,  and , for the quadratic expression that produces the maximum number of primes for consecutive values of , starting with .

'''

import math
import myprime as p

prime = list()
maxPrimeList = list()
pl =  p.g(1000)
maxLength = 0
pl = [-1 * x for x in pl][::-1] + pl
ab = (0, 0)

#for b in range(1000,-1000, -1):
#    for a in range(-1000,1000, 1):
for b in pl:
    for a in pl[::-1]:
        prime = list()
        for n in range(1000):
            x = n**2 + a*n + b
            if not p.isPrime(x):
                break
            prime.append(x)
        if len(prime) > maxLength:
            ab = (a, b)
            maxLength = len(prime)
            maxPrimeList = prime

print(f'{ab[0]=}, {ab[1]=}, {maxLength=}')
print(maxPrimeList)
print(f'{ab[0]*ab[1]=}')



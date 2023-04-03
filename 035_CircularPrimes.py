'''
Circular primes
Problem #35

The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
How many circular primes are there below one million?
'''

import myprime as p
import time
import sys

start = time.time()
primeList = p.g(1_000_000)

'''
I tried two different implimentations to make a circular number list,
getting the result that the first is about 1sec faster than 2nd on my PC,
which mean that the list operation costs me more time.
'''
def circularNumList(n):
    cnList = []
    cnt = d = len(str(n))
    while cnt >= 1:
        denominator = 10**(d-1)
        left = n//denominator
        n = (n-left*denominator)*10 + left
        cnt -= 1
        cnList.append(n)
    return cnList

def circularNumList2(n):
    number = list(str(n))
    cnList = []
    for n in range(len(number)):
        cnList.append(number[n:] + number[:n])
    return [int(''.join(n)) for n in cnList]

circularPrimeList = []
for prime in primeList:
    notPrime = False
    tmp = []
    for cP in circularNumList(prime):
#    for cP in circularNumList2(prime):
        if p.isPrime(cP):
            tmp.append(cP)
        else:
            notPrime = True
            break
    if not notPrime:
        circularPrimeList.append(tmp)

print(circularPrimeList)
print(len(circularPrimeList))
end = time.time()
print(end-start)


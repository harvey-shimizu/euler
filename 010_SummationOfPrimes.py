"""
Summation of Primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.

"""
import time
import math
import sys
import myprime as mp

N = 2_000_000
t1 = time.time()
print(f"{sum(mp.g(N)):10,d}")
t2 = time.time()
elapse = (t2 - t1)
print (f"{elapse=:,.2f}sec")

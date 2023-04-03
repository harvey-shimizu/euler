'''
Pandigital Prime
Problem #41
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
'''
import myprime as p
import time
from tqdm import trange


start = time.time()
for n in trange(10**7-1, 1, -2):
    if not p.isPrime(n):
        continue
    sp = set([int(i) for i in str(n)])
    if sp == set(range(1,len(str(n))+1)):
        print(sp, n)
        break
end = time.time() - start
print(end)

# Another Solutions

import numpy as np
from itertools import permutations
from sympy import isprime

start = time.time()
perm_gen = (int(''.join(u)) for u in permutations('1234567'))

max_prime = 0
for i in perm_gen:
  if isprime(i):
    if i > max_prime: max_prime = i

print(max_prime)
end = time.time() - start
print(end)

# Another Solutions

def odd_is_prime(n):
    d = 3
    while d * d <= n:
        if n % d == 0: return False
        d += 2
    return True

start = time.time()
for n in range(7654321, 1234566, -2):
    if set(str(n)) == set("1234567") and odd_is_prime(n):
        print(n)
        break
end = time.time() - start
print(end)


# Another Solutions
def main():
    from eulertools import primes, PermN
    from itertools import count

    p = primes(int(7654321**.5))
    for j in count():
        i = int("".join(PermN("7654321", j)))
        for d in p:
            if i % d == 0:
                break
        else:
            print(i)
            return
start = time.time()
main()
end = time.time() - start
print(end)

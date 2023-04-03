'''
Prime pair sets
-------------------
Problem #60

The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

'''

import myprime as mp
from itertools import combinations, permutations
from tqdm import tqdm

#primeList = mp.g(792);  N = 4
primeList = mp.g(1000); N = 5
primeList = mp.g(100_000_000); N = 5

for p in tqdm(combinations(primeList, N)):
    count = 0
    for p0, p1 in permutations(p, 2):
        num = int(str(p0)+str(p1))
        if num in primeList:
            count += 1
        elif mp.isPrime(num):
            primeList.append(num)
            count += 1
            print(num)
        else:
            break
    if count == N*(N-1):
        break

print(p)
print(sum(p))


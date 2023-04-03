'''
Truncatable Primes
Problem #37

The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''

import myprime as p
import tqdm
import time

start = time.time()
primeList = p.g(1_000_000)
truncablePrime = []
for prime in primeList[4:]:
    notTruncablePrime = False
    for cnt in range(len(str(prime))):
        if not p.isPrime(int(str(prime)[cnt:])) or not p.isPrime(int(str(prime)[:len(str(prime))-cnt])):
            notTruncablePrime = True
            break
#        print(int(str(prime)[cnt:]), int(str(prime)[:len(str(prime))-cnt]))
    if not notTruncablePrime:
        truncablePrime.append(prime)
end = time.time() - start
print("Runtime =", end)
print(sum(truncablePrime))
print(len(truncablePrime))
print(truncablePrime)

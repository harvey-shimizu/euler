"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""
import time
import math
import prime_gen

def findPrimeFactor(n):
    prime = []
    for p in prime_gen.g(int(math.sqrt(n))):
        if p*p > n : break
        while n%p == 0:
            prime.append(p)
            n //= p
    if n > 1:
        prime.append(n)
    return max(prime)

# 474.6sec (7.91min)
n = 600851475143
n = 13195
t1 = time.time()
print(findPrimeFactor(n))
t2 = time.time()
elapse = (t2 - t1)
print (f"{elapse=:.2f}sec")

#--------------------------------------
# Another Solution
#--------------------------------------

n = 13195
n = 600851475143
factor = 2
lastfactor = 1
t1 = time.time()
while n > 1:
    if n % factor == 0:
        lastfactor = factor
        n /= factor
        while n % factor == 0:
            n /= factor
            print(n)
    factor = factor + 1
t2 = time.time()
print(lastfactor)
elapse = (t2 - t1)*10**3
print (f"{elapse=:.2f}msec")

#--------------------------------------
# Another Solution
#--------------------------------------

n = 13195
n = 600851475143
t1 = time.time()
if n % 2 == 0:
    n /= 2
    lastfactor = 2
    while n % 2 == 0:
        n /= 2
else:
    lastfactor = 1
factor = 3
while n > 1:
    if n % factor == 0:
        n /= factor
        lastfactor = factor
        while n % factor == 0:
            n /= factor
    factor += 2
t2 = time.time()
print(lastfactor)
elapse = (t2 - t1)*10**3
print (f"{elapse=:.2f}msec")

#--------------------------------------
# Another Solution
#--------------------------------------

n = 13195
n = 6008514751430329
n = 600851475143
t1 = time.time()
if n % 2 == 0:
    lastfactor = 2
    n /= 2
    while n % 2 == 0:
        n /= 2
else:
    lastfactor = 1
factor = 3
maxfactor = math.sqrt(n)
while n > 1 and factor <= maxfactor:
    if n % factor == 0:
        n /= factor
        while n % factor == 0:
            n /= factor
        maxfactor = math.sqrt(n)
    factor += 2
t2 = time.time()
if n == 1:
    print(lastfactor)
else:
    print(int(n))
elapse = (t2 - t1)*10**3
print (f"{elapse=:.2f}msec")

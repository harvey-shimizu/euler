
"""
Smallest Multiple

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""
import time
import math
import prime_gen as pr
import sys
import myprime as mp

# this algorizm takes an elapsed time about 43s.
#prime_list = list(range(2,20))
t1 = time.time()
prime_list = []
m = 1
#for p in pr.g(20):
for p in mp.g(20):
#for p in mp.g(10):
    m *= p
prime_list.append(m)
prime_list.reverse()
prime_list.extend([16,9,8])
smallest_multiple = 0
found_flag = 0
#prime_list = list(range(2,11))
print(prime_list)

while found_flag == 0:
    smallest_multiple += 1
    for p in prime_list:
        if not smallest_multiple % p == 0:
            found_flag = 0
            break
        else:
            found_flag = 1
            t2 = time.time()
            elapse = (t2 - t1)
            sys.stdout.write(f"sm:{smallest_multiple:15,d}:{p:10,d} {elapse=:.2f}sec\r")
            sys.stdout.flush()
print("\n")
print(f"{smallest_multiple:,d}")
t2 = time.time()
elapse = (t2 - t1)*10**3
print (f"{elapse=:.2f}msec")

#--------------------------------------
# Answer
#--------------------------------------

N = 1
K = 20
check = True
t1 = time.time()

limit = math.sqrt(K)
k = math.log(K)
#PrimeList = pr.g(K)
PrimeList = mp.g(K)
#print(PrimeList)
alist = {}
for p in PrimeList:
    a = 1
    if check :
        if p <= limit:
            a = math.floor(k/math.log(p))
        else:
            check = False
#    alist[p] = a
    N = N * p ** a
#print(alist)
print(f"{N:,d}")

t2 = time.time()
elapse = (t2 - t1)*10**3
print (f"{elapse=:.2f}msec")


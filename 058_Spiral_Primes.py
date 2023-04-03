'''
Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?

'''

import myprime as m
import math
import time

def IsPrime(n):
    Counter = 0
    for x in range(2, 1 + math.ceil(math.sqrt(n))):
        if n % x == 0:
            Counter = Counter+1
            break
    if Counter == 0:
        return(True)
    if n == 2:
        return(True)
    else:
        return(False)

def IsPrime2(n):
    if n == 1 or n != 2 and n % 2 == 0 or n != 3 and n % 3 == 0:
        return False
    for i in range(1, int(n ** 0.5)//3 + 1):
        i = 3 * i + 1 | 1
        if n % i == 0:
            return False
    return True

def getDiagonalNum(l):
    dp = [1]
    for i in range(2, l+2):
        dp += genSpiralList(i)
    return dp

def genSpiralList(l):
    return [n for n in range(1,(2*l-1)**2+1)][::(l-1)*2][-4:]

def genSpiralList2(l):
    t0 = (2*l-1)**2
    t1 = t0 - (l-1)*2
    t2 = t1 - (l-1)*2
    t3 = t2 - (l-1)*2
    return [t3, t2, t1, t0]

def p058_1():
    inc = 1
    pCnt = 0
    percent = 1.0
    while percent >= 0.1:
        inc += 1
        #print(genSpiralList2(inc))
        pCnt += sum(map(m.isPrime, genSpiralList2(inc)))
        percent = pCnt/((inc-1)*4+1)
        #print(inc, pCnt, (inc-1)*4+1, percent)
        #print(percent)
    return (inc)*2-1

def p058_2():
    inc = 1
    pCnt = 0
    percent = 1.0
    while percent >= 0.1:
        inc += 1
        #print(genSpiralList2(inc))
        pCnt += sum(map(IsPrime, genSpiralList2(inc)))
        percent = pCnt/((inc-1)*4+1)
        #print(inc, pCnt, (inc-1)*4+1, percent)
        #print(percent)
    return (inc)*2-1

def p058_3():
    inc = 1
    pCnt = 0
    percent = 1.0
    while percent >= 0.1:
        inc += 1
        #print(genSpiralList2(inc))
        pCnt += sum(map(IsPrime2, genSpiralList2(inc)))
        percent = pCnt/((inc-1)*4+1)
        #print(inc, pCnt, (inc-1)*4+1, percent)
        #print(percent)
    return (inc)*2-1

t1 = time.time()
print(p058_1())
t2 = time.time()
elapse = (t2 - t1)*10**3
print (f"{elapse=:.2f}msec")

t1 = time.time()
print(p058_2())
t2 = time.time()
elapse = (t2 - t1)*10**3
print (f"{elapse=:.2f}msec")

t1 = time.time()
print(p058_3())
t2 = time.time()
elapse = (t2 - t1)*10**3
print (f"{elapse=:.2f}msec")

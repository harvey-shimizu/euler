"""
10001st Prime

By listing the first six prime numbers: 2, 3, 5, 7, 11 and 13, we can see that the 6th prime is 15. What is the 10001st prime number?

"""
import time
import math
import prime_gen as pg
import sys

def prime(num):
    if   num <= 0: return []
    elif num == 1: return []
    elif num == 2: return [2]
    elif num == 3: return [2,3]
    else: pass
    p = [2,3]
    for x in range(3,num):
        if x % 2 == 0:
            continue
        prime_check = True
        for y in p:
            if x % y == 0:
                prime_check = False
                break
        if prime_check == True:
            p.append(x)
    return p

def st_prime(num):
    if   num <= 0: return []
    elif num == 1: return [2]
    elif num == 2: return [2,3]
    else: pass
    p = [2,3]
    x = 3
    while len(p) < num:
        x += 1
        if x % 2 == 0:
            continue
        prime_check = True
        for y in p:
            if x % y == 0:
                prime_check = False
                break
        if prime_check == True:
            p.append(x)
    return p

if __name__ == '__main__':

    t1 = time.time()
    sp = st_prime(10001)
    print(sp[-1])
    t2 = time.time()
    elapse = (t2 - t1)*10**3
    print (f"{elapse=:.2f}msec")

    t1 = time.time()
    myp = prime(10001)
    print("len:", len(myp))
#print("my_prime[", 10001, "]:", myp[10001])
#print(myp)
    t2 = time.time()
    elapse = (t2 - t1)*10**3
    print (f"{elapse=:.2f}msec")

    t1 = time.time()
    mp = pg.g(10001)
    t2 = time.time()
    elapse = (t2 - t1)*10**3
    print (f"{elapse=:.2f}msec")

    if mp == myp:
        print("Correct")
    else:
        print("Wrong!")

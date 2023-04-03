"""
10001st Prime

By listing the first six prime numbers: 2, 3, 5, 7, 11 and 13, we can see that the 6th prime is 15. What is the 10001st prime number?

"""
import time
import math
#import prime_gen as pg
import sys

def old_g(num):
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
    elif num == 1: return []
    elif num == 2: return [2]
    elif num == 3: return [2,3]
    else: pass
    p = [2,3]
    x = 3
    while len(p) < num:
        x += 2
#        if x % 2 == 0:
#            continue
        prime_check = True
        for y in p:
            if x % y == 0:
                prime_check = False
                break
        if prime_check == True:
            p.append(x)
    return p

# Imporved version after seeing the answer.
def st_prime2(num):
    if   num <= 0: return []
    elif num == 1: return []
    elif num == 2: return [2]
    elif num == 3: return [2,3]
    else: pass
    p = [2,3]
    x = 3
    while len(p) < num:
        x += 2
        if isPrime(x):
            p.append(x)
    return p

def g(num):
    if   num <= 1: return []
    elif num == 2: return [2]
    elif num == 3: return [2,3]
    else: pass
    p = [2]
    candidate = 1
    if num % 2 == 0 : num -= 1
    while candidate < num:
        candidate += 2
        if isPrime(candidate):
            p.append(candidate)
    return p

def isPrime(num):
    if   num <= 1: return False
    elif num <  4: return True # 2 or 3
    elif num %  2 == 0 : return False
    elif num <  9: return True # Aleady excluded 4,6 and 8.
    elif num %  3 == 0 : return False
    else:
        r = math.floor(math.sqrt(num))
        f = 5
        # All primes greater than 5 can be written in the form 6k+/-1.(k:Z)
        while f <= r:
            if num % f == 0: return False
            if num % (f+2) == 0: return False
            f += 6
    return True

def countPrime(limit):
    count = 1 # We know that 2 is prime.
    candidate = 1
    while count != limit:
        candidate += 2
        if isPrime(candidate):
            count += 1
    return candidate

if __name__ == '__main__':

    print("1:", g(1))
    print("2:", g(2))
    print("3:", g(3))
    print("4:", g(4))
    print("5:", g(5))
    print("6:", g(6))
    print("7:", g(7))
    print("8:", g(8))
    print("100:", g(100))
    print("100:",len(g(100)))

    print("1:", pg.g(1))
    print("2:", pg.g(2))
    print("3:", pg.g(3))
    print("4:", pg.g(4))
    print("5:", pg.g(5))
    print("6:", pg.g(6))
    print("7:", pg.g(7))
    print("8:", pg.g(8))
    print("100:", pg.g(100))
    print("100:",len(pg.g(100)))

    Limit = 10001
    t1 = time.time()
    print(countPrime(Limit))
    t2 = time.time()
    elapse = (t2 - t1)*10**3
    print (f"{elapse=:.2f}msec")

    t1 = time.time()
    sp = st_prime2(Limit)
#    sp = st_prime(100)
#    print(sp)
    print(sp[-1])
    t2 = time.time()
    elapse = (t2 - t1)*10**3
    print (f"{elapse=:.2f}msec")

    t1 = time.time()
    myp = g(Limit)
#    print("len:", len(myp))
#print("my_prime[", 10001, "]:", myp[10001])
#print(myp)
    t2 = time.time()
    elapse = (t2 - t1)*10**3
    print (f"{elapse=:.2f}msec")

    t1 = time.time()
    mp = pg.g(Limit)
    t2 = time.time()
    elapse = (t2 - t1)*10**3
    print (f"{elapse=:.2f}msec")

    if mp == myp:
        print("Correct")
    else:
        print("Wrong!")


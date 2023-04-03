'''

By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values:
13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family:
56003, 56113, 56333, 56443, 56663, 56773, and 56993.

Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.

---------------------

Answers
[121313, 222323, 323333, 424343, 525353, 626363, 828383, 929393]

'''

import myprime as p
import itertools as i
import tqdm as t

def paddingNum(num):
    digit = len(str(num))
    if digit == 5: return str(num)
    if digit < 5:
        strNum = (5-digit)*"0" + str(num)
        return strNum
    else: # digitNum > 5
        print("Overflow! : ", num)
        exti()

def primeDigitReplacements(strNum):
    primes = []
    d = 0
    while d < 10:
        num = int(strNum.replace('*', str(d)))
        if p.isPrime(num):
            primes.append(num)
        d += 1
    return primes

#if __name__ == '__main__':
def main2():

    astarisk = ["**", "***", "****"]
    astarisk = ["***", "****"]
    lengthCnt = 8
    for a in range(len(astarisk)):
        for k in t.tqdm(range(100000, 1000000)):
            for kk in i.permutations(astarisk[a]+str(k)[:6-len(astarisk[a])], 6):
                #print(''.join(kk))
                strNum = ''.join(kk)
                primes = primeDigitReplacements(strNum);
                if len(primes) == lengthCnt:
                    if len(str(primes[0])) == 6:
                        print(primes)
                        exit()

# Another answers from Euler Project

def isprime(N):
    if N < 2:
        return 0
    if N % 2 == 0 and not N == 2:
        return 0
    for i in range(3, int(N ** .5)+1, 2):
        if N % i == 0:
            return 0
    return 1

def checkpattern(N, mx=7):
    N = str(N)
    n = tuple(_ for _ in N[:-1] if int(_) <= (10 - mx))
    #print(N, n, N[:-1])

    for _ in n:
        #print(_)
        count = 10 - int(_)
        for z in range(int(_), 9+1):
            if not isprime(vu := int(N[:-1].replace(_, str(z)) + N[-1])):
                count -= 1
            if count < mx:
                break
        if count >= mx:
            return _, count

def main():
    i = 1
    #while 1:
    while i < 200:
        if isprime(i) and checkpattern(i, 8):
            return i
        i += 2

if __name__ == '__main__':
    print(main2())

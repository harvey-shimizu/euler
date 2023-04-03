'''
Goldbach's other conjecture
Problem #46

It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
'''

def solution(limit):
    sieve = [0]*(limit + 1)
    sieve[0] = 1
    sieve[1] = 1

    for k in range(2,limit+1, 2):
        sieve[k] = 1

    for n in range(3, limit+1, 2):
        if sieve[n] == 0: # is prime?
            for k in range(n*n, limit+1, n):
                sieve[k] = 1
        elif n % 2 == 1: # is odd composite
            hasWitness = False
            for k in range(1, 2*k*k):
                if sieve[n - 2*k*k] == 0:
                    hasWitness = True
                    break
            if not hasWitness : return n
    return False

print(solution(20000))

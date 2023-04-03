'''
Distinct Primes Factors
Problem #47

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
'''

def solution(horizon, numFactors, seqLength):
    count = 0
    # The Sieve of Eratosthenes
    primeCount = [0]*(horizon+1)
    for i in range(2,horizon+1):
        if primeCount[i] == numFactors:
            count += 1
            if count == seqLength:
                return i - seqLength + 1
        else:
            count = 0
            if primeCount[i] == 0:
                for j in range(i, horizon+1, i):
                    primeCount[j] += 1
    return False

print(solution(150000, 4, 4))

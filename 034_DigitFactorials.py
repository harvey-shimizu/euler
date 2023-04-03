'''
Digit Factorials
Problem #34

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.
'''
import math
import tqdm
import time

factorial_list = [math.factorial(n) for n in range(0,11)]
found_list = list()
# Max bound must be logically over 7-digits.
for n in tqdm.trange(3,1499999):
    s = 0
    num = n
    while num >= 1:
        s += factorial_list[num % 10]
        num //= 10
    if s == n:
        found_list.append(n)
print(sum(found_list))

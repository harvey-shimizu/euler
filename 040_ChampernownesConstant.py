'''
Champernowne's constant
Problem #40

An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.
If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

'''

import time

start = time.time()
products = 1
cc = ''.join([str(c) for c in range(1_000_000)])
for i in range(0,7):
    products *= int(cc[10**i])
print(products)
end = time.time() - start
print(end)


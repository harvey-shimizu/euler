
"""
Special Pythagorean Triplet

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

"""
import sys
import time
import math

# a^2 + b^2 = c^2 and a + b + c = 1000

N = 1000
if N%2 :
    print("Please input even number.")
    sys.exit()

N2 = N*N/2
c = N
result = []
found = 0

while c > N/2:
    for b in range(c):
        for a in range(b):
            sys.stdout.write(f"{a:4,d}:{b:4,d} {c=:4,d}\r")
            sys.stdout.flush()
            if a+b+c ==1000 and a**2 + b**2 == c**2:
                found = 1
                break
        if found == 1:
            break
    if found == 1:
        break
    c -= 1

print('\nfound:', found)
print(f"ans {a=:4,d}:{b=:4,d} {c=:4,d}")
resutl = a*b*c
print("\n", resutl)


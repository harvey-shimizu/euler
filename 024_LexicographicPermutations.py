'''
Lexicographic Permutations
Problem #24

A permutation is an ordered arrangement of objects.
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''

import time
import math
import string as s

T = 3000000
T = 1000000
def genLexiconPattern(pattern, target):
    out = []
    target -= 1
    plist = list(pattern)
    length = len(pattern) - 1
    while length >= 1:
        g = target // math.factorial(length)
        out.append(plist.pop(g))
        target %= math.factorial(length)
        length -= 1
    out.append(plist.pop())
    return out

t1 = time.time()
print(genLexiconPattern('0123456789', T))
t2 = time.time()
elapse = (t2 - t1)
print (f"{elapse=:.6f}")

# Another solutions

from operator import add

def getPermutations(a):
   if len(a)==1:
      yield a
   else:
      for i in range(len(a)):
         this = a[i]
         rest = a[:i] + a[i+1:]
         for p in getPermutations(rest):
            yield [this] + p

index = 0
t1 = time.time()
for k in getPermutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]):
    index += 1
    if index == T:
        print(k)
        break
t2 = time.time()
elapse = (t2 - t1)*10**3
print(f"{elapse=:.2f}msec")
#
import itertools

t1 = time.time()

per = itertools.permutations('0123456789')

a = [''.join(i) for i in per]
b = [int(i) for i in a]

print(b[T-1])
t2 = time.time()

elapse = (t2 - t1)*10**3
print(f"{elapse=:.2f}msec")

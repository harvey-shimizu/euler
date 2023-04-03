
'''
A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?
'''

import time

t1 = time.time()
print(max(sum(map(int, str(a**b))) for a in range(100) for b in range(100)))
t2 = time.time()
elapse = (t2 - t1)*10**3
print (f"{elapse=:.2f}msec")

t1 = time.time()
print(max(sum(map(int, str(a**b))) for a in range(90, 100) for b in range(90, 100)))
t2 = time.time()
elapse = (t2 - t1)*10**3
print (f"{elapse=:.2f}msec")

import math
def L(a, b):
      return 1 + math.floor(b * math.log(a, 10))
maxi = 0
t1 = time.time()
for b in range(99, 1, -1):
    if 9 * L(99, b) < maxi:
        break
    for a in range(99, 90, -1):
        maxi = max(maxi, sum(map(int, str(a**b))))
t2 = time.time()
print(maxi)
elapse = (t2 - t1)*10**3
print (f"{elapse=:.2f}msec")

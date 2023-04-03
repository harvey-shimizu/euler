'''
Pandigital multiples
Problem #38

Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
'''

import tqdm
import time
from pprint import pprint

LIMIT = 200
panDigitalList = {}
start = time.time()
for num in tqdm.trange(1, 10000):
    panSpace = []
    digitCnt = 0
    for seq in range(1,10):
        product = num * seq
        digitCnt += len(str(product))
        if digitCnt <= 9:
            for pan in str(product):
                if pan != '0' and not pan in panSpace:
                    panSpace += pan
        else:
            break
    if len(panSpace) == 9:
        panDigitalList[num]=panSpace
pprint(panDigitalList)
end = time.time() - start
print(end)

# Another solutions

# Pandigital multiples
from time import time
import itertools

start = time()

def e38():
    for p in itertools.permutations('987654321', 4):
#    for p in itertools.permutations('123456789', 4):
        s = ''
        for d in p:
            s += d

        if len(set(s + str(int(s) * 2) + '0')) == 10:
            return s + str(int(s) * 2)

print('The largest pandigital =', e38())  # 932718654
print("Runtime =", time() - start)

from time import time
import itertools

start = time()

for p in itertools.permutations('987654321', 4):
    if int(p[0]) < 6:
        break
    s = ''
    for d in p:
        s += d
    if len(set(s + str(int(s) * 2) + '0')) == 10:
        print(s + ' ' + str(int(s) * 2))

for p in itertools.permutations('321987654', 3):
    if int(p[0]) > 3:
        break
    s = ''
    for d in p:
        s += d
    if len(set(s + str(int(s) * 2) + str(int(s) * 3) + '0')) == 10:
        print(s + ' ' + str(int(s) * 2) + ' ' + str(int(s) * 3))

s9 = s1 = ''
for n in range(1, 10):
    if n < 6:
        s9 += str(9 * n) + ' '
    s1 += str(n) + ' '
print(s9[:-1])
print(s1[:-1])
print("Runtime =", time() - start)


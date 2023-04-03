'''
Digit fifth powers
Problem #30

Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
'''

from rich import print
import time

s = 0
start = time.time()
for a in range(0,10):
    for b in range(0,10):
        for c in range(0,10):
            for d in range(0,10):
                for e in range(0,10):
                    for f in range(0,10):
                        x = a**5 + b**5 + c**5 + d**5 + e**5 + f**5
                        if x == (100000*a + 10000*b + 1000*c + 100*d + 10*e + f):
                            s += x
                            print(x)
s -= 1
print(f'{s=}')
end = time.time()
print(start - end)

import tqdm

numbers = []

start = time.time()
#for i in tqdm.tqdm(range(10, 1000000)):
for i in tqdm.tqdm(range(10, 9**5*6)):
    sum_of_numbers = 0
    for j in str(i):
        sum_of_numbers += int(j) ** 5
    if sum_of_numbers == i:
        numbers.append(i)

print(sum(numbers))
end = time.time()
print(start - end)

start = time.time()
def digpownumsum(pow, max):
    return sum(map(lambda i: i * (i == sum(map(lambda x: x ** pow, map(int, list(str(i)))))), tqdm.trange(2, max)))
print(digpownumsum(5, 9**5*6))
#print(digpownumsum(5, 1000000))
end = time.time()
print(start - end)

start = time.time()
c=0
for q in range (0,10):
  for w in range (0,q+1):
    for e in range (0,w+1):
      for r in range (0,e+1):
         for t in range (0,r+1):
            for y in range (0,t+1):
                v= (q**5+w**5+e**5+r**5+t**5+y**5)
                b=0
                n=str(v)
                m=0
                while m < len(n) and b <= v:
                       b+=int(n[m])**5
                       m+=1
                if b == v :
                      c += v
print(c-1)
end = time.time()
print(start - end)

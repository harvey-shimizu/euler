"""
Special Pythagorean Triplet

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
import math
import sys
import time

N = 1000
c = int(N/2)
b = 10
a = 1
found = 0

print("N =", N)
t1 = time.time()
while c > 0:
   ab = N/2*(N - 2*c)
   b = 5
   while c > b:
#       print('c>b', c,'>', b)
       if ab % b == 0:
           a = 1
           while b > a:
#               print('b>a', b,'>', a)
               if ab % a == 0:
                   if ((a**2 + b**2) == c**2) and a+b+c == 1000:
                       found = 1
                       break
               a += 1
       if found == 1:
           break
       b += 5
   if found == 1:
       break
   c -= 1

t2 = time.time()
print(found)
print(a, b, c)
print(a*b*c)
elapse = (t2 - t1)*10**3
print (f"{elapse=:.2f}msec")

#--------------------------------------
# Answer
#--------------------------------------

N = 1000
print("N =", N)
t1 = time.time()
for a in range(3, int((N-3)/3)):
    for b in range(a+1, int((N-1-a)/2)):
        c = N-a-b
        if c*c == a*a + b*b :
            print(f"{a=:4,d}, {b=:4,d}, {c=:4,d}")
t2 = time.time()
elapse = (t2 - t1)*10**3
print (f"{elapse=:.2f}msec")

#--------------------------------------
# Answer
#--------------------------------------
N = 170500020500010
N = 100000000000000
N = 1000
print(f"{N=:20,d}")
t1 = time.time()
s2 = int(N/2)
mlimit = math.ceil(math.sqrt(s2)) - 1
for m in range(2, mlimit):
    if s2 % m == 0:
        sm = s2 / m
        while sm % 2 == 0:
            sm /= 2
        if m % 2 == 1:
            k = m+2
        else:
            k = m+1
        while k < 2*m and k <= sm:
            if sm % k == 0 and math.gcd(k, m) == 1:
                d = s2 / (k*m)
                n = k - m
                a = d*(m*m - n*n)
                b = 2*d*m*n
                c = d*(m*m+n*n)
                print(f"{a=:>20,.0f}, {b=:>20,.0f}, {c=:>20,.0f}")
            k += 2
t2 = time.time()
elapse = (t2 - t1)*10**3
print (f"{elapse=:.2f}msec")

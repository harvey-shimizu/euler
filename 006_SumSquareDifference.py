
"""
Sum square difference

The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + .... + 10^2 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + 3 +...+ 10)^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is, 3025 - 385 = 2640

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
import time
import math

N = 100
t1 = time.time()

s1 = 0
for n in range(1, N+1):
    s1 += n**2
s2 = (((N+1)*N)//2)**2

print(f"{s2-s1:,d}")
t2 = time.time()
elapse = (t2 - t1)*10**3
print (f"{elapse=:.2f}msec")

#--------------------------------------
# Another Solution
#--------------------------------------

N = 100
t1 = time.time()

s2 = (((N+1)*N)//2)**2
s1 = N*(N+1)*(2*N+1)//6

print(f"{s2-s1:,d}")
t2 = time.time()
elapse = (t2 - t1)*10**3
print (f"{elapse=:.2f}msec")


"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.#
"""
import time

target = 1_000_000

t1 = time.time()
l = []
for x in range(1,target):
    if not x % 3 or not x % 5:
        l.append(x)

print(sum(l))
t2 = time.time()

#lap = (t2 - t1)*10**6
lap = (t2 - t1)
print (f"{lap=:.2f}sec")

t1 = time.time()
print(sum([x for x in range(1,target) if not x%3 or not x%5]))
t2 = time.time()

#lap = (t2 - t1)*10**6
lap = (t2 - t1)
print (f"{lap=:.2f}sec")

# Another Solution

t1 = time.time()
def sumDivisibleBy(x):
    n = target // x
    return x*(n*(n+1))//2

print(sumDivisibleBy(3) + sumDivisibleBy(5) - sumDivisibleBy(15))
t2 = time.time()
lap = (t2 - t1)*10**6
print (f"{lap=:.2f}us")

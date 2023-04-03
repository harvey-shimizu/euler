'''
Longest Collatz Sequence

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
Which starting number, under one million, produces the longest chain?
NOTE: Once the chain starts the terms are allowed to go above one million.
'''

import time
import sys

def collatz_process(num):
    if num % 2 == 0:
        return int(num / 2)
    else:
        return 3*num + 1

def collatz_process2(num):
    if num in ca.keys():
        return ca[num]
    if num % 2 == 0:
        ca[num] = collatz_process2(num/2) + 1
    else:
        ca[num] = collatz_process2((3*num + 1)/2) + 2
    return ca[num]

def findSteps_of_collatz(num):
    steps = 1
    while num > 1:
#        print(num, '->', end=' ')
        num = collatz_process(num)
        steps += 1
        if num == 1:
#            print(num)
            break
    return steps

# (  837,799, 525 steps) below 1,000,000
# (8,400,511, 686 steps) below 10,000,000

UPPER = 1_000_0000
maxStep = (0, 0)
ca = {1:1}
t1 = time.time()
for n in range(int(UPPER/2),UPPER,1):
#    step = findSteps_of_collatz(n)
    step = collatz_process2(n)
    if step > maxStep[1]:
        maxStep = n, step
        print(f"{n=:<20,d} Current Maxstep:{step:>7,d}")
#        sys.stdout.write(f"{n=:<20,d} Current Maxstep:{step:>7,d}\r")
#        sys.stdout.flush()
print(maxStep)
t2 = time.time()
elapse = (t2 - t1)*10**3
print (f"{elapse=:.2f}msec")



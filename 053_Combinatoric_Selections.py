'''

There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation,
.

In general,

, where , , and .

It is not until , that a value exceeds one-million:
.

How many, not necessarily distinct, values of
 for , are greater than one-million?


'''
import math as m

def combinations(n, r):
    return m.factorial(n) // (m.factorial(n-r) * m.factorial(r))


count = 0
for n in range(1, 101):
    for r in range(1, n+1):
        if len(str(combinations(n, r))) > 6:
            #print(n, '{:,}'.format(combinations(n, r)))
            count += 1
print(count)

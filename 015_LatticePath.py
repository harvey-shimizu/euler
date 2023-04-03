'''
Problem #15
Lattice paths

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?
'''

import sys
import time
import math

# Another solution
def countRoutes(m, n):
    if n == 0 or m == 0:
        return 1
    return countRoutes(m, n-1) + countRoutes(m-1, n)

t1 = time.time()
print(countRoutes(10,10))
t2 = time.time()
elapse = (t2 - t1)*10**3
print (f"{elapse=:.2f}msec")

N = 100

# Another solution

lattice ={}
def countRoutes2(m ,n):
    if n == 0 or m == 0:
        return 1

    if (m, n) in lattice.keys():
        return lattice[(m, n)]

    lattice[(m, n)] = countRoutes2(m, n-1) + countRoutes2(m-1, n)
    return lattice[(m, n)]

t1 = time.time()
if N <= 100:
    print(countRoutes2(N,N))
t2 = time.time()
elapse = (t2 - t1)*10**3
print (f"{elapse=:.2f}msec")

# Another solution

def countRoutes3(m, n):
    # 2-d array initialization of being all setted to 1.
    grid = [[1]*m for i in range(n)]
    for x in range(0,m):
        for y in range(0,n):
            grid[x][y] = grid[x-1][y] + grid[x][y-1]

    return grid[m-1][n-1]

t1 = time.time()
if N <= 1000:
    print(countRoutes3(N,N))
t2 = time.time()
elapse = (t2 - t1)*10**3
print (f"{elapse=:.2f}msec")

def countRoutes4(n):
    result = 1
    result *= [n+i for i in range(1,n+1)]
    return math.prod(result)//math.prod(range(1,n+1))

t1 = time.time()
print(countRoutes4(N))
t2 = time.time()
elapse = (t2 - t1)*10**3
print (f"{elapse=:.2f}msec")

def countRoutes5(n):
    result = 1
    return math.factorial(2*n)//(math.factorial(n)*math.factorial(n))

t1 = time.time()
print(countRoutes5(N))
t2 = time.time()
elapse = (t2 - t1)*10**3
print (f"{elapse=:.2f}msec")

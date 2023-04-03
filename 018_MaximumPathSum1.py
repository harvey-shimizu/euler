'''
Problem #18
Maximum path sum 1

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)
'''
import time

t=[]
t.append([75,])
t.append([95, 64,])
t.append([17, 47, 82,])
t.append([18, 35, 87, 10,])
t.append([20,  4, 82, 47, 65,])
t.append([19,  1, 23, 75,  3, 34,])
t.append([88,  2, 77, 73,  7, 63, 67,])
t.append([99, 65,  4, 28,  6, 16, 70, 92,])
t.append([41, 41, 26, 56, 83, 40, 80, 70, 33,])
t.append([41, 48, 72, 33, 47, 32, 37, 16, 94, 29,])
t.append([53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14,])
t.append([70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57,])
t.append([91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48,])
t.append([63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31,])
t.append([ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23,])

def getMaxsum(l, i):
    if l < -2:
        return t[l][i] + max(getMaxsum(l+1, i), getMaxsum(l+1, i+1))
    else:
        return t[l][i] + max(t[-1][i], t[-1][i+1])

t1 = time.time()
print(getMaxsum(-len(t), 0))
t2 = time.time()
ela = (t2 - t1)*10**3
print(f'{ela=:,.2f}ms')


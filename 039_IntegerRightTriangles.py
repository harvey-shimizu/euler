'''
Integer right triangles
Problem #39

If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
'''
import math
import tqdm
from pprint import pprint

triangleLengthList = {}
for p in tqdm.trange(500, 1001):
    perimeter = {}
    found = 0
    for a in range(100,1000):
        for b in range(a,1000):
            if a+b > 1000:
                continue
            c = p - a - b
            if c > 0 and c*c == a*a + b*b and a+b+c <= 1000:
                found += 1
                perimeter[p] = [a,b,c, a+b+c]
    triangleLengthList[found] = [perimeter.keys(), perimeter.values()]

pprint(triangleLengthList)
print(max(triangleLengthList.keys()))
print(triangleLengthList[max(triangleLengthList.keys())])

#Another solutions

# Integer right triangles
from time import time
import math

start = time()

def e39():
    sin45 = math.sin(math.pi / 4)
    hm = 2 * sin45 + 1  # the hypotenuse is min when the angles = 45deg and the legs are equal
    maxs = 0            # p = 2 * leg + hmin; leg = hmin * sin45; hmin = p / (2 * sin45 + 1)
    maxp = 0
    for p in range(100, 1001, 2):  # perimeter is always even
        sol = 0
        for h in range(int(p / hm) + 1, p // 2):  # here is hypotenuse, from min to max
            bsq = (p - h) ** 2  # for the square equasion: leg**2-(p-h)*leg+((p-h)**2-h**2)/2 = 0
            dis = bsq - 2 * (bsq - h ** 2)  # discriminant: b**2-4*a*c
            leg = (p - h + dis ** 0.5) / 2
            if leg == int(leg):
                sol += 1
                print(p, h, leg, p - h - leg)
        if sol > maxs:
            maxs = sol
            maxp = p
    return f'For p = {maxp}, the number of solutions = {maxs}'

print(e39())  # 840
print("Runtime =", time() - start)

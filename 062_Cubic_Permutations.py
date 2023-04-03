'''

The cube, 41063625 (3453), can be permuted to produce two other cubes: 56623104 (3843) and 66430125 (4053). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.

'''


def p062():
    i = 1; si = '1';
    L = 5
    found = 0
    for n in range(1,10000):
        sn = str(n**3)
        pool=[]
        count = 0
        for i in range(n, 10000):
            m = str(i**3)
            if len(sn) == len(m) and sorted(sn) == sorted(m):
                count += 1
                pool.append((i, m))
            if count == L:
                found = 1
                break
        if found == 1:
            print(found, n, pool)
            break

p062()

#------Another solutions

def p062_1():
    cubic = [''.join(sorted(str(i**3))) for i in range(10000)]
    cubic_cnt = []

    for i in cubic:
        cnt = 0
        for j in cubic:
            if i == j: cnt += 1
        cubic_cnt.append(cnt)

    print(cubic_cnt)
    print(cubic_cnt.index(5)**3)

#------Another solutions

import itertools

def cubic_permutations(N):
    sorted_cubes={}
    possible_answers=[]
    for c in (x**3 for x in itertools.count(1)):
        s = ''.join(sorted(str(c)))
        if possible_answers and len(s) > digits:
            # Can now rely on last digit result being complete
            # Need to check no more permuations were added.
            possible_answers = [l for l in possible_answers if len(l)==N]

        if possible_answers:
            return min(map(min, possible_answers))

        l = sorted_cubes.setdefault(s,[])
        l.append(c)
        if len(l)==N:
            possible_answers.append(l)
            digits=len(s)

print (cubic_permutations(5))

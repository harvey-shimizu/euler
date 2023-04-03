'''
Prime pair sets
-------------------
Problem #60

The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

'''
import myprime as mp
from itertools import combinations, permutations, repeat
from tqdm import tqdm
import time
from sympy import isprime, sieve

def findPrimePairSets2(pLimit, N):
    primeList = mp.g(pLimit)
    #p1 = [x for x in primeList if (len(str(x)) % 3) == 1]
    #p2 = [x for x in primeList if (len(str(x)) % 3) == 2]
    #primeDict = set(zip(mp.g(1_000_000), repeat(True)))
    #print(primeDict)
    #exit()
    for p in combinations(primeList, N):
    #for p in combinations(p1+p2, N):
        ap = map(int, [str(x)+str(y) for x, y in permutations(p, 2)])
        #if ap.issubset(primeDict):
        #if all(mp.isPrime(x) for x in ap):
        if all(isprime(x) for x in ap):
        #if all(primeDict.get(x, False) for x in ap):
        #if all(x in primeDict.keys() for x in ap):
        #if all(primeDict.get(x) for x in ap):
            return p
    return None


def findPrimePairSets(pLimit, N):
#primeList = mp.g(1_000_000); N = 5
    primeList = mp.g(pLimit)
    #primeList.reverse()
    for p in combinations(primeList, N):
        count = 0
        for p0, p1 in permutations(p, 2):
            num = int(str(p0)+str(p1))
            if num in set(primeList):
                count += 1
            elif mp.isPrime(num):
                primeList.append(num)
                count += 1
            else:
                break
        if count == N*(N-1):
            return p

# process time : about 5sec
#t1 = time.time()
#p = findPrimePairSets(1000, 4)
#print(p, sum(p))
#t2 = time.time()
#elapse = (t2 - t1)*10**3
#print (f"{elapse=:.2f}msec")

#t1 = time.time()
#p = findPrimePairSets2(10000, 5)
#p = findPrimePairSets2(1000, 4)
#print(p, sum(p))
#t2 = time.time()
#elapse = (t2 - t1)*10**3
#print (f"{elapse=:.2f}msec")



'''
It was fun to realize that this problem has a natural connection whith graph theory.

I first computed the set S of pairs of prime (p, q) with p < q and concat(p, q) is a prime and concat(q, p) is a prime and p < 10**8 and q < 10**8. This computation took 45 seconds in python. The size of S is 133135. Then using the awesome python package NetworkX, i built the graph G, whose edges are the elements of S and found the 5-cliques of G. To see a definition :

https://en.wikipedia.org/wiki/Clique_(graph_theory).

The result is the sum of this 5-clique : [13, 8389, 5197, 5701, 6733] because it has the lowest sum. The graph part of the algorithm takes only 5 seconds and looks like this (with S described above and pre-computed in the code) :


import networkx
from networkx.algorithms.clique import find_cliques
G = networkx.Graph()
G.add_edges_from(list(S))
five_cliques=[clique for clique in find_cliques(G) if len(clique)==5]
print(sorted(five_cliques, key=lambda clique: sum(clique))[0])
'''


'''
I seperated the primes by the sum of their digits mod 3.  It might be a slight optimization, or it may make the program slower, but:
For each prime (except 3), the sum of its digits mod three must be either 1 or 2.  If you concatenate a 1-prime with a 2-prime, you'll get a prime that is divisible by three.  So I created 2 arrays -- one for the 1-primes and one for the 2-primes.  3 went into both arrays, since no matter what you concatenate 3 with, it will never be divisible by 3.  All the numbers in the solution must be either in the 1-array or the 2-array, so you have to search through less primes.



17 codelines running 1.5s for primes up to 10000 on my i5-6500 from 2015:

First: create a dict of prime pairs using the mod 3 trick - this takes 99% of the runtime
Second: iterate through the pairs to delete all but Quintuplets
Third: identify minimum sum
Fourth: start with primes up to 10000 which yields 26033.
        To verify this is lowest sum, rerun up to 26030 (which runs nearly 10s)

'''

def p060_1():
    from sympy import isprime, sieve
    #limit=10**4 # limit was try and error
    limit=10**2 # limit was try and error

# initialize dict and find pairs:
    d={p:{p} for p in sieve.primerange(3,limit) }

    for p in d.keys():
        for q in (q for q in d.keys() if q>p and p%3==q%3 and isprime(int(str(p)+str(q))) and isprime(int(str(q)+str(p)))):
                d[p] |= {q}; d[q] |= {p}

    print(d)

# delete all but Quintuplets
    tupel = 5
    l=0
    while l != len(d):
        l=len(d)
        rm=set()
        for k in d.keys():
            d[k] -= {i for i in d[k] if len(d.get(i,set()) & d[k]) < tupel}
            if len(d[k])<tupel:  rm |= {k}
        for r in rm: d.pop(r)

    print(d)

# identify minimum sum
    print(min(map(sum,(s for s in d.values()))))
    print('len: ', len(d))

t1 = time.time()
p060_1()
t2 = time.time()
elapse = (t2 - t1)*10**3
print (f"{elapse=:.2f}msec")

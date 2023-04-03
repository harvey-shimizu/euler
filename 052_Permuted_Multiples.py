'''
Permuted multiples

Problem 52

It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.
Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

'''
import time

def isPermutedMultiples(length, num):
    n1 = str(num); n2 = str(num*2); n3 = str(num*3); n4 = str(num*4); n5 = str(num*5); n6 = str(num*6)
    l = len(n1);    l2 = len(n2);   l3 = len(n3);    l4 = len(n4);    l5 = len(n5);    l6 = len(n6)
    s1 = set(n1);  s2 = set(n2);    s3 = set(n3);    s4 = set(n4);    s5 = set(n6);    s6 = set(n6)

    if s1 == s2 == s3 == s4 == s5 == s6 and length == l == l2 == l3 == l4 == l5 == l6 \
          == len(s1) == len(s2) == len(s3) == len(s4) == len(s5) == len(s6):
        return True
    else:
        return False

def isPermutedMultiples2(length, num):
    n1 = str(num); l = len(n1);
    n2 = str(num*2); l2 = len(n2);
    s1 = set(n1); s2 = set(n2)

    if s1 == s2 and length == l == l2 == len(s1) == len(s2):
        print(length, l, l2, n1, n2)
        return True
    else:
        return False

t1 = time.time()
for countUp in range(1, 100000000):
    if isPermutedMultiples(len(str(countUp)), countUp):
        print(countUp)
        break
t2 = time.time()
elapse = (t2 - t1)*10**3
print (f"{elapse=:.2f}msec")

#------

lim=6

def containssamedigit(x,y):
    n,m=list(str(x)),list(str(y))
    if len(n)!=len(m):
        return(False)
    for i in n:
        if i not in m:
            return(False)
        m.remove(i)
    return(True)

i=1
t1 = time.time()
while True:
    j=2
    while containssamedigit(i,j*i) and j<=lim:
        j+=1
    if j>lim:
        print(i)
        break
    i+=1
t2 = time.time()
elapse = (t2 - t1)*10**3
print (f"{elapse=:.2f}msec")

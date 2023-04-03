'''

Powerful digit counts
---------------------
Problem #63

The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit number, 134217728=89, is a ninth power.
How many n-digit positive integers exist which are also an nth power?

'''


count = 0
pList = []
for d in range(1,100):
    for p in range(1,1000):
        if p == len(str(d**p)):
            count += 1
            pList.append((d,p))

print(count)
print(pList)


'''
Names Scores
Problem #22

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
'''

import string
import time

def read_name(path):
    with open(path, 'rt') as f:
        return f.read().strip("\n").strip('"').split('","')

def compute(names):
    alpha = [ss for ss in string.ascii_uppercase]
    ad = {k:v for k,v in zip(alpha, range(1,len(alpha)+1))}
    names.sort()

    total = 0
    for n in names:
        _sum = 0
        for s in n:
            _sum += ad[s]
#            _sum += ord(s)-64
        _sum *= (names.index(n)+1)
        total += _sum

    return total

t1 = time.time()
print(compute(read_name("name.txt")))
t2 = time.time()
ela = (t2 - t1)*10**3
print(f'{ela=:,.2f}ms')

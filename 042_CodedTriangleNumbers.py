'''
Coded triangle numbers
Problem #42

The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
'''

import time
import string as s
from pprint import pprint

def isTriangleNum(s):
    cnt = 1
    while True:
        tn = cnt*(cnt+1)*(1/2)
        if s > tn:
            cnt += 1
        else:
            return s == tn

start = time.time()
with open('words.txt') as f:
    line = f.read().split(',')
tw = []
for w in line[:-1]:
    s = 0
    for a in w.strip('"'):
        s += ord(a) - 64
    if isTriangleNum(s):
        tw.append([s,w])
pprint(len(tw))
end = time.time() - start
#pprint(tw)
print(end)

#Another solutions


def is_triangular_number(a):
    counter = 1
    while True:
        t = int(0.5 * counter * (counter + 1))
        if a > t:
            counter += 1
        else:
            return a == t

start = time.time()
list_of_numbers = []
with open('words.txt') as f:
    text = ''.join(list(f)).replace('"', '').split(',')

for word in text:
    number = 0
    for letter in word:
        number += ord(letter) - 64
    if is_triangular_number(number):
        list_of_numbers.append(number)

print(len(list_of_numbers))
end = time.time() - start
print(end)



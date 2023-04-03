"""
Largest palindrome product

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
import time
import math

#palindrome_list = []
palindrome_list = {}
t1 = time.time()
for abc in range(100, 999):
    for xyz in range(100, 999):
        n = list(str(abc * xyz))
#        if len(n) == 6 and n[0] == n[5] and n[1] == n[4] and n[2] == n[3]:
        n2 = n.copy()
        n.reverse()
        if n2 == n:
#            print('find:', n)
#            palindrome_list.append(abc*xyz)
            key = str(abc)+"*"+str(xyz)
            palindrome_list[key] = abc*xyz
m = max(palindrome_list.values())
print('max:', m, "=", list(palindrome_list.keys())[list(palindrome_list.values()).index(m)])
#print(palindrome_list, " ", len(palindrome_list))
print('min:', min(palindrome_list.values()), " =" ,list(palindrome_list.keys())[list(palindrome_list.values()).index(min(palindrome_list.values()))])
t2 = time.time()
elapse = (t2 - t1)*10**3
print (f"{elapse=:.2f}msec")

#--------------------------------------
# Another Solution
#--------------------------------------

palindrome_list = {}
t1 = time.time()
for abc in range(100, 999):
    for xyz in range(abc, 999): # <--- Min is changed to 'abc'
        n = list(str(abc * xyz))
        n2 = n.copy()
        n.reverse()
        if n2 == n:
            key = str(abc)+"*"+str(xyz)
            palindrome_list[key] = abc*xyz
m = max(palindrome_list.values())
print('max:', m, "=", list(palindrome_list.keys())[list(palindrome_list.values()).index(m)])
t2 = time.time()
elapse = (t2 - t1)*10**3
print (f"{elapse=:.2f}msec")

#--------------------------------------
# Another Solution
#--------------------------------------

def isPalindrome(n):
    n1 = list(str(n))
    n2 = n1.copy()
    n1.reverse()
    if n2 == n1:
        return True
    else:
        return False

a = 999
largePalindrome = 0
t1 = time.time()
while a >= 100:
    b = 999
    while b >= a:
        if a*b <= largePalindrome:
            break
        elif isPalindrome(a*b):
            largePalindrome = a*b
        b -= 1
    a -= 1
print("max:",largePalindrome)
t2 = time.time()
elapse = (t2 - t1)*10**3
print (f"{elapse=:.2f}msec")

#--------------------------------------
# Another Solution
#--------------------------------------

a = 999
largePalindrome = 0
t1 = time.time()
while a >= 100:
    if a % 11 == 0:
        b = 999
        db = 1
    else:
        b = 990 # The largest number less than or equal 999
                # and divisible by 11
        db = 11

    while b >= a:
        if a*b <= largePalindrome:
            break
        elif isPalindrome(a*b):
            largePalindrome = a*b
        b = b-db
    a -= 1
print("max:",largePalindrome)
t2 = time.time()
elapse = (t2 - t1)*10**3
print (f"{elapse=:.2f}msec")

#--------------------------------------
# Another Solution
#--------------------------------------

t1 = time.time()
for abc in range(100, 999):
    for xyz in range(abc, 999): # <--- Min is changed to 'abc'
        p = xyz * abc
        if not p % 11 == 0 or p < largePalindrome:
            break
        elif isPalindrome(p):
            largePalindrome = p
print("max:",largePalindrome)
t2 = time.time()
elapse = (t2 - t1)*10**3
print (f"{elapse=:.2f}msec")


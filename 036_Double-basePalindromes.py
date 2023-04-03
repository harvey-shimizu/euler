'''
Double-base palindromes
Problem #36

The decimal number, 585 = 1001001001(2) (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
'''

import tqdm
import time

def isPalindromic(num, base):
    if base == 10:
        n1 = list(str(num))
    elif base == 2:
        n1 = list(str(bin(num)))[2:]
    else:
        return None
    n2 = n1.copy()
    n1.reverse()
    if n2 == n1:
        return True
    else:
        return False

#LIMIT = 1_000_000_000
LIMIT = 1_000_000
palindromeList = []
for n in tqdm.trange(1,LIMIT):
    if isPalindromic(n, 10) and isPalindromic(n, 2):
        palindromeList.append(n)
print(sum(palindromeList))

'''
Pandigital Products
Problem #32

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
'''

from rich.console import Console
from tqdm import trange
from rich.progress import track

console = Console()

def checkPandigited(d1, d2):
    product = d1 * d2
    check = [s for s in str(product) + str(d1) + str(d2)]
    if '0' in check:
        return False
    i = 0
    digit = ['1','2','3','4','5','6','7','8','9']
    isPandigit = True
    while len(digit) > 0:
        if len(check) <= i:
            isPandigit = False
            break
        if check[i] in digit:
            digit.pop(digit.index(check[i]))
            i += 1
        else:
            isPandigit = False
            break
    if isPandigit and len(check) < 10:
        return True
    return False

total = list()
for d1 in track(range(1,987)):
    for d2 in range(d1,9876):
        if checkPandigited(d1, d2):
            if len(str(d1)) <= 2 and not d1*d2 in total:
#                print(f'{d1} x {d2} = {d1*d2}')
                total.append(d1*d2)
console.print(sum(total))


'''
Digit cancelling fractions
Problem #33

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
'''

from fractions import Fraction
from tqdm import trange
import time

start = time.time()
product = 1
for b in trange(2,10):
    for a in range(1,b):
        x = 9*a*b // (10*a - b)
        if len(str(x)) == 1 and (10*a+x)/(10*x+b) == a/b:
            print(f'{a}{x}/{x}{b} = {a}/{b}')
            product *= a/b
print(Fraction(product).limit_denominator())
end = time.time()
print(end-start)

'''
Problem #17
Number letter counts

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
'''
import time

wd = {0:'', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen', 20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety', 100:'hundred', 1000:'thousand'}

def num2word(n):
    word = ''
    if n == 1000:
        word = 'one ' + wd[n]
        return word
    elif 1000 > n >= 100:
        word  = wd[n//100] + ' ' + wd[100]
        if n%100:
            word += " and " + num2word(n%100)
    elif 99 >= n >= 20:
        word += wd[(n//10)*10]
        if n%10:
            word += '-' + num2word(n%10)
    elif 20 > n >= 1:
        word += wd[n]
    return word

s = ''
#for n in range(1,1001):
#    print(num2word(n))
t1 = time.time()
for n in range(1,1001):
    s += num2word(n)
print(len(s.replace(' ', '').replace('-', '')))
t2 = time.time()
elapse = (t2 - t1)*10**3
print (f"{elapse=:.2f}msec")

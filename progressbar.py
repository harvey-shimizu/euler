
import tqdm as t
from collections import OrderedDict
from time import sleep

text = 'abcdefgadkbd'

#with t.tqdm(text, ncols=80, bar_format="{bar} {percentage:3.0f}% {elapsed}/{remaining}") as pbar:
with t.tqdm(text, ncols=80) as pbar:
    for i, ch in enumerate(pbar):
        sleep(1)

with t.tqdm(text, ncols=80, bar_format="{bar} {percentage:3.0f}% {elapsed}/{remaining}", desc="{elapsed}/{remaining}") as pbar:
    for i, ch in enumerate(pbar):
        pbar.set_description("[train] Epoch %d" % i)
        pbar.set_postfix(OrderedDict(loss=1-i/5, acc=i/10))
        sleep(0.1)
#
#
#for i in t.trange(10, desc='1st loop', ncols=100):
#    for j in t.trange(5, desc='2nd loop', leave=False, ncols=90):
#        for k in t.trange(100, desc='3nd loop', ncols=80):
#            sleep(0.01)

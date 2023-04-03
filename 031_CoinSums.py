'''
Coin Sums
Problem #31

In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
'''

from tqdm import trange, tnrange, tqdm_notebook
import time

result = list()
CSUM = 200
start = time.time()
for p100 in range(0,CSUM//100+1):
    for p50 in range(0,(CSUM-100*p100)//50+1):
        for p20 in range(0,(CSUM-100*p100-50*p50)//20+1):
            for p10 in range(0,(CSUM-100*p100-50*p50-20*p20)//10+1):
                for p5 in range(0,(CSUM-100*p100-50*p50-20*p20-10*p10)//5+1):
                    for p2 in range(0,(CSUM-100*p100-50*p50-20*p20-10*p10-5*p5)//2+1):
                        for p1 in range(0,(CSUM-100*p100-50*p50-20*p20-10*p10-5*p5-2*p2)+1):
                            s = 100*p100 + 50*p50 + 20*p20 + 10*p10 + 5*p5 + 2*p2 + 1*p1
                            if s == 200:
                                result.append({100:p100, 50:p50, 20:p20, 10:p10, 5:p5, 2:p2, 1:p1})
print(len(result)+1)
end= time.time()
print(f'{(end-start):,.5f}sec')

start = time.time()
count = 0
for p100 in range(CSUM, -1 ,-CSUM):
    for p50 in range(p100, -1, -100):
        for p20 in range(p50, -1, -50):
            for p10 in range(p20, -1, -20):
                for p5 in range(p10, -1, -10):
                    for p2 in range(p5, -1, -5):
                        for p1 in range(p2, -1, -2):
                            count += 1
print(count)
end= time.time()
print(f'{(end-start)*10**3:,.5f}msec')

# Another solutions

import logging

#logging.basicConfig(level=logging.DEBUG, stream=TqdmStream)
#log = logging.getLogger(__name__)
#log.info("loop")

logger = logging.getLogger('LoggingTest')
logger.setLevel(10)
sh = logging.StreamHandler()
logger.addHandler(sh)
fh = logging.FileHandler('test.log')
logger.addHandler(fh)
logger.log(20,'info')
logger.log(30,'waring')
logger.log(100,'test')


#target = CSUM
target = 10
#coinSize = [1,2,5,10,20,50,100,200]
coinSize = [1,2,5,10]
ways = [0] * (target+1)
ways[0] = 1

start = time.time()
for i in range(len(coinSize)):
   for j in range(coinSize[i], target+1):
        ways[j] += ways[j - coinSize[i]]
#        print(f'ways[{j:3d}]= ways[{j:3d}] + ways[{ways[j-coinSize[i]]:5,d}]')
        logger.info(f'ways[{j}]= ways[{j}] + ways[{ways[j-coinSize[i]]}]')
        logger.info(f'coinSize[{i}]={coinSize[i]:3,d} {j=:3,d}, ways[{j}]={ways[j]}')
#print(ways)
print(ways[-1])
end= time.time()
print(f'{(end-start)*10**3:,.5f}msec')

import logging

import tqdm
import tqdm_logging_wrapper

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

items = [1, 2, 3]
items_iter = tqdm.tqdm(items)
logger.info(f"Items: {items}")
with tqdm_logging_wrapper.wrap_logging_for_tqdm(items_iter), items_iter:
    for item in items_iter:
        logger.info(f"Item: {item}")
logger.info(f"Items: {items}")



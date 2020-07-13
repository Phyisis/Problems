# It can be verified that there are 23 positive integers less than 1000 that are divisible 
# by at least four distinct primes less than 100.
# Find how many positive integers less than 10^16 are divisible 
# by at least four distinct primes less than 100.

from helpers import analytics,primes
analytics.monitor()
import math, bisect, random
from itertools import combinations
import functools

def naive(limit):
    total = 0
    for i in range(1,limit):
        unique = 0
        for p in pu100:
            if i % p == 0:
                unique += 1
            if unique == 4:
                total += 1
                break
    return total

def main(limit):
    total = 0
    for i in range(4,len(pu100)):
        minlcm = float("inf")
        for s in combinations(pu100,i):
            p = math.prod(s)
            if p < minlcm:
                minlcm = p
            if p < limit:
                f = math.comb(i-1,3)
                if i%2==0:
                    total += f*(limit//p)
                else:
                    total -= f*(limit//p)
        if minlcm > limit:
            break
    return total

limit = int(1e16)
pu100 = list(primes.primes(100))
print(main(limit), analytics.lap(), analytics.maxMem())
#result = naive(limit); print("naive:",result,"    time:",lap())

# exact:
# 1e3 : 23     ; 0.004 sec
# 1e4 : 811    ; 0.05 sec
# 1e5 : 9280   ; 0.5 sec
# 1e6 : 77579  ; 5.5 sec
# 1e7 : 768778 ; 64 sec

# 1e16: 785478606870985 ; 28.2 sec
# approx:
# 1e16 ~ 7.85e14


"""
(elements,duplicates) = extra count
(5,0) = 5
(5,1) = 0
(6,0) = 6c4 =
(6,1) = (2,3,5,7,11,11) = (5,0)


(2,3,5,7,11)
(2,3,5,7)
n*(1-,2-,3-,(2,2)-,5-,(2,3)-,7-,(2,2,2)-,(3,3)-,(2,5)-,11,(2,2,3)...)

"""
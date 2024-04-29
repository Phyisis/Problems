from helpers import analytics
analytics.monitor()
from math import prod,log
from itertools import combinations_with_replacement,chain
"""
2 <= k <= 12000
s = l + m
k == len(s) == len(m) + len(l)
m = [a0+a1+a2+..+an]
l = [1]*(k-len(m))
prod(s) == sum(s) == prod(m) == sum(m) + (k-len(m))
"""

limit = 12000
v_min = {k:2*k for k in range(1,limit+1)}

def prodsum(n=2, p=1, s=1, c=1):
    k = p - s + c
    if k < limit:
        v_min[k] = min(p,v_min[k])
        for i in range(n, limit//p*2 + 1):
            prodsum(i, p*i, s+i, c+1)

def main(limit):
    prodsum()
    return sum(set(v_min[k] for k in range(2,limit)))

print(main(limit), analytics.lap(), analytics.maxMem())
"""
7587457 
time: 0.251497387 
max memory: 10.5MB
"""
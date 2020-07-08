import numpy as np
import random
from fractions import gcd
from functools import reduce
import math
import _Utility_ as U

def ways(r,n,s): #to roll r with n, s-sided dice
    m = math.floor((r-n)/s)
    w = 0
    for k in range(0,m+1):
        w += ((-1)**k)*U.binomial(n,k)*U.binomial(r-s*k-1,n-1)
    return w

def P(r,n,s):
    m = math.floor((r-n)/s)
    w = 0
    for k in range(0,m+1):
        w += ((-1)**k)*U.binomial(n,k)*U.binomial(r-s*k-1,n-1)
    return w/s**n

p = []
c = []

def populate(table,n,s):
    for i in range(0,n*s+1):
        table.append(ways(i,n,s))

populate(p,9,4)
populate(c,6,6)

print(p)
print(c)

w = 0
t = (4**9) * (6**6)
for C in range(0, 37):
    for P in range (C+1, 37):
        w += p[P]*c[C]

print(round(w/t,7))

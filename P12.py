import numpy as np
import random
from fractions import gcd
from functools import reduce
import math


min = 2
max = 500
nt = 1
tnum = 0
maxDivisors = 0

def GetNumDivisors(num):
    divisors = 0
    rootn = math.floor(num**(.5))
    for i in range(2,rootn):
        if (num % i == 0):
            divisors += 2
        if rootn**2 == num:
            divisors -= 1
    return divisors

while (GetNumDivisors(tnum) < max):
    tnum += nt
    nt += 1

print(tnum)








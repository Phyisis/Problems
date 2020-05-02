import numpy as np
import random
from fractions import gcd
from functools import reduce
import math


min = 1
max = 20

def gcd(a, b):
    while b:      
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def lcmm(*args):  
    return reduce(lcm, args)

out = lcmm(*range(min,max))
print(out)





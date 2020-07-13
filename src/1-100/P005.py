from helpers import analytics
analytics.monitor()
from functools import reduce
import math

def lcm(a, b):
    return a * b // math.gcd(a, b)

def lcmm(*args):  
    return reduce(lcm, args)

def main():
    return lcmm(*range(1,20))

print(main(), analytics.lap(), analytics.maxMem())
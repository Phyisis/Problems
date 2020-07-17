from helpers import analytics
analytics.monitor()
from functools import reduce
from math import gcd

def lcm(a, b):
    return (a * b) // gcd(a, b)

def main():
    return reduce(lcm,range(1,20))

print(main(), analytics.lap(), analytics.maxMem())
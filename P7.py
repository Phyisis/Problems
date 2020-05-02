import numpy as np
import random
from fractions import gcd
from functools import reduce
import math


min = 2
max = 10001
n = 3
primes = [2]

def CheckPrime(num):
    rootn = math.floor(num**(.5))
    for i in primes:
        if i > rootn:
            return True
        if num % i == 0:
            return False
    return True

while (len(primes) < max):
    if CheckPrime(n):
        primes.append(n)
    n += 2

print(primes)








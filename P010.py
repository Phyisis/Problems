import numpy as np
import random
from fractions import gcd
from functools import reduce
import math


min = 2
max = 2000000
sum = 0
n = 3
primes = [2]
lastprime = 0

def gcd(a, b):
    while b:      
        a, b = b, a % b
    return a

def CheckPrime(num):
    rootn = math.floor(num**(.5))
    for i in primes:
        if i > rootn:
            return True
        if num % i == 0:
            return False
    return True

while (lastprime < max):
    if CheckPrime(n):
        lastprime = n
        primes.append(n)
    n += 2

for i in range(0,len(primes)-1):
    sum += primes[i]

print(sum)
'print(primes)'








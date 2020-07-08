"""
Consider the divisors of 30: 1,2,3,5,6,10,15,30.
It can be seen that for every divisor d of 30, d+30/d is prime.

Find the sum of all positive integers n not exceeding 100 000 000
such that for every divisor d of n, d+n/d is prime.
"""

""" Notes:
n must be square free, and 1 less than a prime
"""
import repackage; repackage.up()
import math
from itertools import compress
from helpers import analytics, primes
analytics.monitor()

limit = int(1e8)
primesList = primes.primes(limit)
primesHash = set(primesList)

def main(limit):
    total = 1
    for p in primesList:
        i = p-1
        if valid(i,squareFree(i)):
            total += i
    return total

def squareFree(n): #if sqr free, return factorization, else return false
    pf = []
    for p in primesList:
      if p*p > n : break
      count = 0
      while not n % p:
        n //= p
        count += 1
        if count > 1: return False
      if count > 0: pf.append(p)
    if n > 1: pf.append(n)
    return pf

def valid(i,pa):
    if not pa: return False
    for d in divisors(pa):
        if not (d+i//d in primesHash):
            return False
    return True

def divisors(pa): #where pa is a list of primes representing a square-free integer's factorization
    divs = [1]
    for p in pa:
        divs += [x*p for x in divs]
    return divs

print(main(limit), analytics.lap(), analytics.maxMem())

# 1739023853137 time: 66.54
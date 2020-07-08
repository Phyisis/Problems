from Problems.helpers import analytics, primes
analytics.monitor()
from math import prod

limit = int(1e5)
primes.initialize(limit)

def rad(n):
    return prod([i for i,_ in primes.factorization(n)])

def main(limit):
    E = [(rad(n),n) for n in range(1,limit+1)]
    E.sort()
    return E[10000-1]

print(main(limit), analytics.lap(), analytics.maxMem())
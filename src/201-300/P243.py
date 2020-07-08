import repackage; repackage.up()
from helpers import analytics, primes
analytics.monitor()
from math import prod
from itertools import combinations_with_replacement, chain

limit = int(27)
target = 15499/94744
primesList = primes.primes(limit)

def R(A):
    if len(A) == 1:
        return 1
    return prod(A)*prod([1-1/p for p in set(A)])/(prod(A)-1)

def main():
    primorials = [[2]]
    for p in primesList[1:]:
        primorials.append(primorials[-1]+[p])
    for r in range(3,5):
        for c in combinations_with_replacement(primorials,r):
            if R(list(chain.from_iterable(c))) < target:
                return prod(chain.from_iterable(c))


print(main(), analytics.lap(), analytics.maxMem())
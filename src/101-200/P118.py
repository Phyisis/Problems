import repackage; repackage.up()
from helpers import analytics, primes, iterators
analytics.monitor()
from itertools import permutations,combinations
from math import prod

digits = "123456789"
noRepeatPrimes = {}

def main():
    total = 0
    for k in range(1,len(digits)):
        for c in combinations(digits,k):
            noRepeatPrimes[c] = 0
            for p in permutations(c):
                if primes.millerRabin(int(''.join(p))):
                    noRepeatPrimes[c] += 1
    for p in iterators.set_partitions(map(str,range(1,10))):
        if len(p) < 2: continue
        q = prod(noRepeatPrimes[tuple(k)] for k in p)
        total += q
    return total

print(main(), analytics.lap(), analytics.maxMem())
# 44680
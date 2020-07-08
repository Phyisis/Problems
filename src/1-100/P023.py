import repackage; repackage.up()
from helpers import analytics, primes
analytics.monitor()

limit = 28123
primes.initialize(limit)

def genAbundants():
    abundants = []
    for i in range(12,limit):
        if sum(primes.divisors(i)) > 2*i:
            abundants.append(i)
    return abundants

def main():
    abundants = genAbundants()
    v = {k:False for k in range(1,limit)}
    for i in range(len(abundants)-1):
        for j in range(i,len(abundants)):
            v[abundants[i]+abundants[j]] = True
    return sum(k for k in range(1,limit) if not v[k])

print(main(), analytics.lap(), analytics.maxMem())

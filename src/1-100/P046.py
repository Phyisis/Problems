import repackage; repackage.up()
from helpers import analytics, primes
analytics.monitor()

limit = int(1e4)
pu = primes.primes(limit)
sq = [i**2 for i in range(1,int(limit**(1/2)+1))]
ns = set(range(3,limit,2))

def main(limit):
    for p in pu:
        for s in sq:
            ns.discard(p)
            ns.discard(p+2*s)
    return min(ns)

print(main(limit), analytics.lap(), analytics.maxMem())
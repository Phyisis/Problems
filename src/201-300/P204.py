import repackage; repackage.up()
from helpers import analytics,primes
analytics.monitor()
from math import prod

def main(maxp,limit):
    primesList = primes.primes(maxp)
    total = 1
    p = [0]*len(primesList)
    v = prod(primesList[i]**p[i] for i in range(len(p)))
    while True:
        while v < limit:
            v *= 2
            p[0] += 1
            total += 1
        i = 0
        while v >= limit:
            v //= primesList[i]**p[i]
            p[i] = 0
            i += 1
            try: 
                p[i] += 1
                v *= primesList[i]
            except: return total
    return 

print(main(100,10**9), analytics.lap(), analytics.maxMem())
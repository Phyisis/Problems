from helpers import analytics,primes
analytics.monitor()
from math import prod

def hamming(maxp,limit):
    primesList = primes.primes(maxp)
    p = [0]*len(primesList)
    v,go = 1,True
    while go:
        while True:
            v *= 2
            p[0] += 1
            if v < limit: yield v
            else: break
        i = 0
        while v > limit:
            v //= primesList[i]**(p[i]-1)
            p[i] = 1
            i += 1
            if i < len(p):
                p[i] += 1
                v *= primesList[i]
                if v < limit: yield v
            else: 
                go = False
                break

def main(N):
    pfn = set()
    for n in hamming(30,N):
        m = primes.nextPrime(n+1)
        #print(n,m,m-n)
        pfn.add(m-n)
    return sum(pfn)

print(main(10**9), analytics.lap(), analytics.maxMem())
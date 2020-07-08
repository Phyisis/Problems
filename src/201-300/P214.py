import repackage; repackage.up()
from helpers import analytics, primes
analytics.monitor()
from fractions import Fraction

n = int(4e7)
t = 25
primesList = primes.primes(n)
phi = primes.totients(n)

def main(n,t):
    total = 0
    for p in primesList:
        if chain(p)==t:
            total += p
    return total

def chain(p,c=0):
    if p==1: return c+1
    return chain(phi[p],c+1)

print(main(n,t), analytics.lap(), analytics.maxMem())
# 1677366278943 time: 55.27
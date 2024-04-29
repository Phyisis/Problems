from helpers import analytics, primes
from math import prod
analytics.monitor()
primes.initialize(1000)

"""
every number can be written as the product of two coprime numbers.
let sigma(n) = sum of divisors of n
for n = i*j, gcd(i,j)==1, sigma(n) = sigma(i)*sigma(j) 
n can be written as the product of coprime i and j, in 2**(r-1) different ways.
where r is the number of distinct prime factors of n
and n can be written as the product of unrestricted i and j in prod(k+1) for exponents k, of each prime factor

"""

mod = 10**9

def divisorSum(pfa,power=1):
    return prod((p**(power*k+1)-1)//(p-1) for p,k in pfa.items())

def divisorSum2(pfa,pfb):
    pf = pfa.copy()
    for p,k in pfb.items():
        if p in pf: pf[p] += k
        else: pf[p] = k
    return prod((p**(k+1)-1)//(p-1) for p,k in pf.items())

def main(N):
    t1,t2 = 0,0
    for i in range(1,N+1):
        pfi = primes.factorization(i)
        t1 += divisorSum(pfi,2)
        for j in range(1,i):
            pfj = primes.factorization(j)
            t2 += divisorSum2(pfi,pfj)
    return 2*t2 + t1    

print(main(1000), analytics.lap(), analytics.maxMem())
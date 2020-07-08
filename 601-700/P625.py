from Problems.helpers import analytics, primes
analytics.monitor()
from math import gcd,comb

#Find G(10^11). Give your answer modulo 998244353
limit = int(1e5)
mod = 998244353
phi = primes.totients(limit)
primes.initialize(limit)

def g(j): #2*j-1 for prime j
    total = 0
    for d in primes.divisors(j):
        total += phi[d]/d
    return round(j*total)

def G(N):
    total = 0
    for j in range(1,N+1):
        total += g(j)
    return total

def main(limit):
    return G(limit) % mod

print(main(limit), analytics.lap(), analytics.maxMem())
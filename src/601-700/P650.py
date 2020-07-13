from helpers import analytics, primes
analytics.monitor()
from math import prod,comb,factorial

limit = int(1e4)
primes.initialize(limit)
mod = 1000000007

# find sum of the sum of the divisors of the products of the rows in pascal's triangle
# comb(n,k) == n!/k!(n-k)!

def P(A):
    return [1] + [A[i]+A[i+1] for i in range(len(A)-1)] + [1]

def Pfac(A):
    f = {}
    for q in A:
        for p,i in primes.factorization(q):
            if p in f:
                f[p] += i
            else:
                f[p] = i
    return f

def Psum(A):
    divs = [1]
    f = Pfac(A)
    for p in f:
        divs += [x*pow(p,k,mod) for k in range(1,f[p]+1) for x in divs]
    return sum(divs)

def main(row):
    A = [1]
    total = -1
    for _ in range(row+1):
        total += Psum(A)%mod
        A = P(A)
    return total%mod

def divisors(n):
    divs = [1]
    for p, e in primes.factorization(n):
        divs += [x*p**k for k in range(1,e+1) for x in divs]
    return divs

def main2(row):
    n = 1
    total = -1
    for r in range(row+1):
        total += sum(primes.divisors(n))
        n = (n*((r+1)**r))//factorial(r)
    return total%mod

#print(main(10), analytics.lap(), analytics.maxMem())
print(main2(20), analytics.lap(), analytics.maxMem())
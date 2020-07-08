from Problems.helpers import analytics, primes
analytics.monitor()
import math
from functools import lru_cache
from itertools import compress, combinations
from fractions import Fraction

def primes(n):
    """ Returns  a list of primes < n for n > 2 """
    sieve = bytearray([True]) * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = bytearray((n-i*i-1)//(2*i)+1)
    return [2,*compress(range(3,n,2), sieve[1:])]

def factorization(n):
    """ Returns a list of the prime factorization of n """
    pf = []
    for p in primeslist:
      if p*p > n : break
      count = 0
      while not n % p:
        n //= p
        count += 1
      if count > 0 and p != 2: pf.append(p)
    if n > 2: pf.append(n)
    return tuple(pf)

def sumOfCubes(n):
    return int((n*(n+1)/2)**2)

def decomposeCube(n):
    s = int(math.copysign(1,n))
    n = abs(n)
    cubes = [i for i in range(1,round(n**(1/3))+2)]
    neg = [-c for c in cubes]
    cubes += neg
    for r in range(1,len(cubes)):
        for c in combinations(cubes,r):
            if sum(i**3 for i in c) == n:
                return ",".join([str(s*i) for i in c])
    return 0

@lru_cache(maxsize=10000000)
def f(n):
    pf = factorization(n)
    return n**3 * math.prod(m(p) for p in pf)

def f2(n):
    pf = factorization(n)
    return math.prod(m2(p) for p in pf)
    # f(n) = (prod(duplicateFactors)*prod(uniquefactors(+/-)1))**3
    # find n=q*p, p>2
    # if q%p==0: f(n)=f(q)*p**3
    # if q%p!=0: f(n)=f(q)*m(p)**3 #(in new version of m() that doesn't divide by n**3)
    

@lru_cache(maxsize=100000)
def m(p):
    if p%4 == 3:
        return Fraction(p**3+1,p**3)
    elif p%4 == 1:
        return Fraction(p**3-1,p**3)
    else: return 1

def m2(p):
    if p%4 == 3:
        return p**3+1
    elif p%4 == 1:
        return p**3-1
    else: return 8
        
def main(limit):
    total = 0
    for n in range(1,limit+1):
        pf = factorization(n)
        pp = math.prod(m(p) for p in pf)
        total += n**3 * pp
    return int(total)

def main2(limit):
    total = 1
    for p in primeslist:
        total *= g(6,p,1)
    return int(total)

def main3(limit):
    for p in primeslist:
        print(f(p))
    return

def G(k,s):
    total = 1 - 1/2**(s-k+1)
    for p in primeslist[1:10000]:
        if p % 4 == 1:
            total *= 1-(1/p**(s-k+1))-((p-1)/p**(s-k/2+1))
        else:            
            total *= 1-(1/p**(s-k+1))-((1-p)/p**(s-k/2+1))
    return total

def g(k,p,i):
    if i == 1:
        if p == 2: 
            return (-2)**(k-1)
        else: 
            return -p**(k-1)-(-1)**(k*(p-1)/4)*p**(k/2-1)*(p-1)
    return 0

## PHI(k,p,i)/(p**2*phi(p)) == p**(k-2) * g(k,p,i)/(p-1)


def P(k,p,s):
    #return 1/(1-PHI(k,p,1,s))
    total = 1
    for i in range(1,2):
        total += PHI(k,p,i,s)
    return total

def PHI2(k,p,i,s):
    return p**(k-s)*g(k,p,i)/(p-1)

def phi(p,i):
    return p**i-p**(i-1)

def PHI(k,p,i,s):
    x1 = p**(i*(k-1-s))
    if p%4==1:
        x1 *= 1-Fraction(1,p**((i*k)//2))
    else:
        x1 *= 1+Fraction(1,p**((i*k)//2))
    return x1

def zeta(x,n):
    return sum(k**(-x) for k in range(n))

mod = 1000000007
limit = int(1e5)
analytics.lap()
primeslist = primes(int(limit**0.5)+1)
print(len(primeslist),"primes generated in:" ,analytics.lap(), " seconds")

analytics.lap()
print(main(limit)%mod,analytics.lap(),analytics.maxMem()) # correct but slow
#print(sumOfCubes(limit)%mod,"time soc:",lap()) # lower bound
#print(main2(limit)%mod,"time main2:",lap()) # why the fuck doesn't this work
#print((main2(limit)*sumOfCubes(limit))%mod,"time G:",lap()) # wrong track with this
#main3(limit)

"""
sum(PHI_k(n)/(n**2*phi(n))) for n < limit = 
prod(P(p,s)) for prime < limit,?
P(p,s)=1+sum(PHI_k(p**i)/(n**2i*phi(p**i))) for i in ??? 

if n is prime, f(n) == m(n)
n**3 * prod(m(pu)) == prod(pr)**3 * prod(m2(pu))
n**3 * prod(m(pu)) == prod(pr)**3 * prod(pu1**3 - 1) * prod(pu3**3 + 1)
n**3 * prod(pu1**3 - 1) * prod(pu3**3+1) * prod(1/pu1**3) * prod(1/pu3**3) == prod(pr)**3 * prod(pu1**3 - 1) * prod(pu3**3 + 1)
n**3 * prod(m(pu)) == PR**3 * (pu1a**3-1)*(pu1b**3-1)...() * (pu3a**3+1)*(pu3b**3+1)...()
== (PR**3*pu1a**3*pu1b**3*pu1c**3-PR**3*pu1b**3*pu1c**3) - (PR**3*pu1a**3*pu1c**3-PR**3*pu1c**3)-(PR**3*pu1a**3*pu1b**3-PR**3*pu1b**3) - (PR**3*pu1a**3-PR**3)


1 + 2**3 + 3**3 * m(3) + 4**3 + 5**3 * m(5) + 6**3 * m(3) + 7**3 * m(7)

(1) + (2**3) + (3**3+1) + (4**3) + (5**3-1) + (2**3 * (3**3+1)) + (7**3+1) + (8**3) + (3**3 * (3**3+1)) + (2**3 * (5**3-1))
+ (11**3+1) + (4**3 * (3**3+1)) + (13**3-1) + (2**3 * (7**3+1)) + ((3**3+1)*(5**3-1)) + (16**3) + (17**3-1) + (6**3 * (3**3+1))
+ (19**3+1) + (4**3 * (5**3-1)) + ((3**3+1) * (7**3+1)) + (2**3 * (11**3+1)) + (23**3-1) + (8**3 *(3**3+1)) + (5**3 * (5**3-1))
+ (2**3 * (13**3-1)) + (9**3 * (3**3+1)) 

1 + 2**3 + 3**3+1 + 4**3 + 5**3-1 + 6**3 + 2**3 + 7**3+1 + 8**3 + 9**3 + 3**3 + 10**3 - 2**3 + 11**3+1 + 12**3 + 4**3
+ 13**3-1 + 14**3 + 2**3 + 15**3 + 5**3 - 3**3 - 1

5**3 - 1 + 7**3 + 1 + 3**3 + 11**3 + 1 + 4**3 + 13**3 - 1 + 5**3

35 => (5**3-1) * (7**3+1) = 35**3 + 5**3 - 7**3 - 1
"""

#print(f(4))
#print(1 + 2**3 + 3**3+1 + 4**3 + 5**3-1 + 6**3 + 7**3+1 + 8**3 + 9**3 + 3**3 + 10**3)

"""
[2,3,5,7,11,13]
[1,0,0,0,0,0] [1,0,0,0,0,0]~~
[0,1,0,0,0,0] [1,1,0,0,0,0]~~
[2,0,0,0,0,0] [3,1,0,0,0,0]~~
[0,0,1,0,0,0] [3,1,1,0,0,0]
[1,1,0,0,0,0] [4,2,1,0,0,0]
[0,0,0,1,0,0] [4,2,1,1,0,0]
[3,0,0,0,0,0] [7,2,1,1,0,0]
[0,2,0,0,0,0] [7,4,1,1,0,0]
[1,0,1,0,0,0] [8,4,2,1,0,0]~
[0,0,0,0,1,0] [8,4,2,1,1,0]
[2,1,0,0,0,0] [10,5,2,1,1,0]
[0,0,0,0,0,1] [10,5,2,1,1,1]
[1,0,0,1,0,0] [11,5,2,2,1,1]
[0,1,1,0,0,0] [11,6,3,2,1,1]
[4,0,0,0,0,0] [15,6,3,2,1,1]
"""
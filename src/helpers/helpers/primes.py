from itertools import compress
from functools import lru_cache
from math import log, gcd, prod
from random import randint
from bisect import bisect
from time import perf_counter
from helpers import integers
from helpers import analytics
import gmpy2
import heapq
analytics.monitor()

def initialize(limit):
    """ Initialize prime list from other modules """
    global primeslist
    primeslist = dynamicPrimes(int(limit**0.5)+1)
    return primeslist

def primes(n):
    '''Returns a generator that yields the prime numbers up to n'''
    bitmap = gmpy2.xmpz(3)
    bitmap[4:n:2] = -1
    for p in bitmap.iter_clear(3, gmpy2.isqrt(n) + 1):
        bitmap[p*p:n:p+p] = -1
    return list(bitmap.iter_clear(2,n))

def primesInRange(a,b):
    a = a-1+a%2
    if a < 2: return primes(b)
    sieve = bytearray([True]) * (b//2)
    for i in range(3,int(b**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = bytearray((b-i*i-1)//(2*i)+1)
    return [*compress(range(a,b,2), sieve[a//2:])]

def ballieExtend(a,b):
    a = (int(a)+1) | 1 #next odd int
    return list(filter(baillie_psw,range(a,b,2)))

class dynamicPrimes():
    def __init__(self,n=2):
        self.n = n 
        self.primes = primes(n)
    
    def __iter__(self):
        return iter(self.primes)
    
    def __len__(self):
        return len(self.primes)
    
    def expect(self,n):
        if n > self.n:
            self.primes += ballieExtend(self.n,n)
            self.n = n
            return self.primes
        return self.primes

primeslist = dynamicPrimes()

def isPrime(n):
    """ Test if single number is prime by trial division """
    if n < 2:
        return False
    for p in primeslist.expect(int(n**0.5)+1):
        if p*p > n:
            return True
        if n % p == 0:
            return False
    return True

def factorization(n):
    """ Returns a dict of the prime factorization of n """
    pf = {}
    for p in primeslist.expect(int(n**0.5)+1):
      if p*p > n : break
      count = 0
      while not n % p:
        n //= p
        count += 1
      if count > 0: pf[p] = count
    if n > 1: pf[n] = 1
    return pf

def divisors(n,power=1):
    """ Returns an unsorted list of the divisors of n**power """
    divs = [1]
    f = factorization(n)
    for p in f:
        divs += [x*p**k for k in range(1,power*f[p]+1) for x in divs]
    return divs

def divisorsSorted(n,power=1,facs={}):
    """ Generator in increasing order of the divisors of n**power """
    divs = [1]
    if not facs: facs = factorization(n)
    for p in facs:
        for d in [x*p**k for k in range(1,power*facs[p]+1) for x in divs]:
            heapq.heappush(divs,d)
    while divs:
        yield heapq.heappop(divs)

def totients(n):
    """ returns complete list of totients from 0 to n inclusive """
    phi = list(range(n+1))
    for p in range(2, n+1, 2):
        phi[p] >>= 1
    for p in range(3, n+1, 2):
        if phi[p] != p: continue
        phi[p] -= 1
        for j in range(2*p, n+1, p):
            phi[j] -= phi[j] // p
    return phi

def millerRabin(n, T=None):
    """ miller rabin primality test, performed with bases a in T. \n
    minimal bases for definite output used if T = None and n < 3317044064679887385961980
    """
    if n%2==0 or n<3: return n==2
    d = n-1
    r = (d-(d&d-1)).bit_length()-1
    d >>= r
    if T == None: T = testSet(n)
    for a in T:
        x = pow(a,d,n)
        if x == 1 or x == n - 1:
            continue
        c = True
        for _ in range(r-1):
            x = pow(x,2,n)
            if x == n - 1:
                c = False
                break
        if c:
            return False
    return True

def testSet(n):
    if n < testKeys[-1]:
        return testSets[testKeys[bisect(testKeys,n)]]
    t = log(n)*log(log(log(n)))
    t = max(t,3)
    return primes(int(t))

testSets = {
    2046:[2],
    1373652:[2,3],
    9080190:[31,73],
    25326000:[2,3,5],
    3215031750:[2,3,5,7],
    4759123140:[2,7,61],
    1122004669632:[2,13,23,1662803],
    2152302898746:[2,3,5,7,11],
    3474749660382:[2,3,5,7,11,13],
    341550071728320:[2,3,5,7,11,13,17],
    3825123056546413050:[2,3,5,7,11,13,17,19,23],
    318665857834031151167460:[2,3,5,7,11,13,17,19,23,29,31,37],
    3317044064679887385961980:[2,3,5,7,11,13,17,19,23,29,31,37,41]
    }
testKeys = sorted(testSets.keys())

def brentRho(n, maxIter = 15): 
    """ returns factorization of n """
    if n == 1: return []
    if n%2==0: return [2] + brentRho(n//2)
    if baillie_psw(n): return [n]
    y,c,m = randint(2,n-2),randint(1,n-1),randint(1,n-1)
    g = lambda x: (pow(x,2,n)+c)%n
    d,r,q,i = 1,1,1,0
    while d==1: 
        x = y
        for _ in range(r):
            y = g(y)
        k = 0
        while (k<r and d==1):
            ys = y
            for _ in range(min(m,r-k)):
                y = g(y)
                q = (q*abs(x-y))%n
            d = gcd(q,n)
            k += m
        r <<= 1
        if maxIter:
            i += 1
            if i == maxIter:
                print("max iterations reached while factoring ",n)
                return [n]
    if baillie_psw(d):
        return [d] + brentRho(n//d)
    else:
        if d==n:
            g = lambda x: (pow(x,2,n)+randint(1,n-1))%n
            while True:
                ys = g(ys)
                d = gcd(abs(x-ys),n)
                if d>1: break
        return brentRho(d)+brentRho(n//d)

def isPerfectPower(n):
    """ returns x,p with smallest x such that x**p == n """
    for p in primes(n.bit_length()):
        x = integers.iroot(n,p)
        if pow(x, p) == n: return x,p
    return n,1
    
def lucasPP(n):
    """ lucas strong probable prime test, returns True/False """
    if n%2==0 or n<3: return n==2
    if integers.iroot(n)**2 == n: return False
    dAbs, sign, d = 5, 1, 5
    while True:
        if 1 < gcd(d, n) < n: return False
        if integers.jacobiSymbol(d, n) == -1: break
        dAbs, sign = dAbs + 2, sign * -1
        d = dAbs * sign
    p, q, t = 1, (1-d)//4, (n+1)//2
    u, u2, v, v2, q, q2 = 0, 1, 2, p, q, 2*q
    for i in range(t.bit_length()):
        u2 = (u2 * v2) % n
        v2 = (v2 * v2 - q2) % n
        if t & (1 << i):
            u, v = u2 * v + u * v2, (v2 * v) + (u2 * u * d)
            if u%2==1: u += n
            u = (u >> 1) % n
            if v%2==1: v += n
            v = (v >> 1) % n
        if i < t.bit_length() - 1:
            q = pow(q,2,n)
            q2 = q + q
    return u == 0

def baillie_psw(n):
    """ baillie PSW prime test, definite for inputs < 2^64 """
    return millerRabin(n,[2]) and lucasPP(n)

def nextPrime(n):
    """ outputs next prime strictly greater than n """
    if n < 2: return 2
    n = (int(n)+1) | 1 #next odd int
    while True:
        if baillie_psw(n): return n
        n += 2

@lru_cache
def mobius(n):
    """ outputs: 
        0 if n divides a prime squared
        1 if n has an even number of distinct prime factors
        -1 if n has an odd number of distinct prime factors
    """
    count = 0
    for p in primeslist.expect(int(n**0.5)+1):
        if p*p > n: break
        if n%p==0:
            n //= p
            if n%p==0: return 0
            count += 1
    if n > 1: count += 1
    if count%2:
        return -1
    return 1

if __name__ == "__main__":
    #primeslist = dynamicPrimes(10**8)
    #print(len(primeslist.primes),analytics.lap(),analytics.maxMem())
    rsa896 = 412023436986659543855531365332575948179811699844327982845455626433876445565248426198098870423161841879261420247188869492560931776375033421130982397485150944909106910269861031862704114880866970564902903653658867433731720813104105190864254793282601391257624033946373269391
    bigPrime = 64135289477071580278790190170577389084825014742943447208116859632024532344630238623598752668347708737661925585694639798853367
    print(baillie_psw(rsa896),": expect False")
    print(baillie_psw(bigPrime),": expect True")
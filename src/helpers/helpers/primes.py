from itertools import compress
from functools import lru_cache
from math import log, gcd
from random import randint
from bisect import bisect

def initialize(limit):
    """ Initialize prime list from other modules """
    global primeslist
    primeslist = dynamicPrimes(int(limit**0.5)+1)
    return primeslist

def primes(n):
    """ Returns  a list of primes < n for n > 2 """
    sieve = bytearray([True]) * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = bytearray((n-i*i-1)//(2*i)+1)
    return [2,*compress(range(3,n,2), sieve[1:])]

def primesInRange(a,b):
    a = a-1+a%2
    if a < 2: return primes(b)
    sieve = bytearray([True]) * (b//2)
    for i in range(3,int(b**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = bytearray((b-i*i-1)//(2*i)+1)
    return [*compress(range(a,b,2), sieve[a//2:])]

def millerExtend(a,b):
    a = a+1-a%2
    return list(filter(millerRabin,range(a,b,2)))

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
            self.primes += millerExtend(self.n,n)
            self.n = n
            return self.primes
        return self.primes
        #return self.primes[:bisect(self.primes,n)]

primeslist = dynamicPrimes()

def isPrime(n):
    """ Test if single number is prime """
    if n < 2:
        return False
    for p in primeslist.expect(int(n**0.5)):
        if p*p > n:
            return True
        if n % p == 0:
            return False
    raise Exception("didn't generate enough primes to verify primality of ",n)

def factorization(n):
    """ Returns a list of the prime factorization of n """
    pf = []
    for p in primeslist.expect(int(n**0.5)):
      if p*p > n : break
      count = 0
      while not n % p:
        n //= p
        count += 1
      if count > 0: pf.append((p, count))
    if n > 1: pf.append((n, 1))
    return pf

def divisors(n,power=1):
    """ Returns an unsorted list of the divisors of n**power """
    divs = [1]
    for p, e in factorization(n):
        divs += [x*p**k for k in range(1,power*e+1) for x in divs]
    return divs

def totients(n):
    phi = list(range(n+1))
    for p in range(2, n+1, 2):
        phi[p] >>= 1
    for p in range(3, n+1, 2):
        if phi[p] != p:
            continue
        phi[p] -= 1
        for j in range(2*p, n+1, p):
            phi[j] -= phi[j] // p
    return phi

def partition(n,I=1):
    """ Returns partitions of the integer n """
    yield (n,)
    for i in range(I, n//2+1):
        for p in partition(n-i,i):
            yield (i,) + p

def partitionCount(n):
    ways = [1] + [0] * n
    nums = [c for c in range(1,n)]
    for num in nums:
        for i in range(num,n+1):
            ways[i] += ways[i-num]
    return ways[n] + 1

def millerRabin(n):
    if n%2==0 or n<3: return n==2
    r,d = 0,n-1
    while d%2==0:
        d >>= 1
        r += 1 
    for a in testSet(n):
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

def iroot(k, n): # assume n > 0
    u, s, k1 = n, n+1, k-1
    while u < s:
        s = u
        u = (k1 * u + n // u ** k1) // k
    return s

def ilog(b, n): # max e where b**e <= n
    lo, blo, hi, bhi = 0, 1, 1, b
    while bhi < n:
        lo, blo, hi, bhi = hi, bhi, hi+hi, bhi*bhi
    while 1 < (hi - lo):
        mid = (lo + hi) // 2
        bmid = blo * pow(b, (mid - lo))
        if n < bmid: hi, bhi = mid, bmid
        elif bmid < n: lo, blo = mid, bmid
        else: return mid
    if bhi == n: return hi
    return lo

def isPerfectPower(n):
    for p in primes(ilog(2,n)):
        x = iroot(p, n)
        if pow(x, p) == n: return x,p
    return n,1

def pollardRho(n,x=2): #finds a factor d of n
    g = lambda x: (pow(x,2,n)+1)%n
    r = 1
    while True:
        y = x
        for _ in range(r):
            x = g(x)
            d = gcd(x-y, n)
            if d > 1:
                return d
        r <<= 1

def brentRho(n): # returns factorization of n
    if n == 1: return []
    if n%2==0: return [2] + brentRho(n//2)
    g = lambda x: (pow(x,2,n)+1)%n
    y,c,m = randint(2,n-3),randint(1,n-3),randint(1,n-3)
    print(y,c,m)
    d,r,q = 1,1,1
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
    if d==n:
        g = lambda x: (pow(x,2,n)+c)%n
        while True:
            ys = g(ys)
            d = gcd(abs(x-ys),n)
            if d>1: break         
    return [d] + brentRho(n//d)

"""
n=2000
for i in range(1+2**n,2**(n+1),2):
    if millerRabin(i):
        print(i)

a0 = 114813069527425452423283320117768198402231770208869520047764273682576626139237031385665948631650626991844596463898746277344711896086305533142593135616665318539129989145312280000688779148240044871428926990063486244781615463646388363947317026040466353970904996558162398808944629605623311649536164221970332681344168908984458505602379484807914058900934776500429002716706625830522008132236281291761267883317206598995396418127021779858404042159853183251540889433902091920554957783589672039160081957216630582755380425583726015528348786419432054508915275783882625175435528800822842770817965453762184851149030217
"""
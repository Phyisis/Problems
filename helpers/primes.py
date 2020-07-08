from itertools import compress
from functools import lru_cache
from math import log

primeslist = None

def initialize(limit):
    """ Initialize prime list from other modules """
    global primeslist
    primeslist = primes(int(limit**0.5)+1)
    return primeslist

def isPrime(n):
    """ Test if single number is prime """
    if n < 2:
        return False
    for p in primeslist:
        if p*p > n:
            return True
        if n % p == 0:
            return False
    print("didn't generate enough primes to verify primality of ",n)

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
    """ Returns list of totients, from totient(0) to totient(n) """
    phi = [i for i in range(n+2)]
    for p in phi[2:]:
        if phi[p] == p:
            phi[p] = p - 1
            for i in range(2 * p, n + 1, p):
                phi[i] = (phi[i] // p) * (p - 1)
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
    if n&0: return False
    r,d = 0,n-1
    while d&0:
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
        i = 0
        while testKeys[i] < n:
            i += 1
        return testSets[testKeys[i]]
    t = log(n)*log(log(log(n)))
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
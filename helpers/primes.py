from itertools import compress
from functools import lru_cache

def initialize(limit):
    """ Initialize prime list from other modules """
    global primeslist
    primeslist = primes(int(limit**0.5)+1)

def isPrime(n):
    """ Test if single number is prime """
    if n <= 1:
        return False
    sqrt = int(n**0.5)
    for i in range(2, sqrt + 1):
        if n % i == 0:
            return False
    return True

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

def divisors(n):
    """ Returns an unsorted list of the divisors of n """
    divs = [1]
    for p, e in factorization(n):
        divs += [x*p**k for k in range(1,e+1) for x in divs]
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

primeslist = None
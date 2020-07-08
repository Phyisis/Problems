"""
(a+1)^n == an+1 (mod a^2)
(a-1)^n == an-1 or 1-an (mod a^2) depending whether n is odd or even; 
the sum is therefore either 2an or 2.

When a is odd, this is always maximised at a^2-a (as in the example with a=7), achieved for example when n=(a-1)/2; 
when a is even, it is maximised at a^2-2a for a>2, achieved for example when n=(a-2)/2.
"""
from Problems.helpers import analytics, primes
analytics.monitor()

primesList = primes.primes(10**8)

def main():
    n = 1
    while 2*primesList[n-1]*n < 10**10:
        n += 1
    if ((primesList[n-1]+1)**n+(primesList[n-1]-1)**n)%primesList[n-1]**2 == 2:
        return n+1
    return n

print(main(), analytics.lap(), analytics.maxMem())
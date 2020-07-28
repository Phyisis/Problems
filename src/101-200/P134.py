from helpers import analytics, primes, integers
analytics.monitor()
from math import ceil,log10,floor

limit = int(1e6)+4
primesList = primes.primes(limit)

def solve(a,b):
    m = 10**ceil(log10(a))
    g,x,y = integers.egcd(b,m) #base solution: x*a,m*a: b*sx + m*sy = a
    k = ceil(-x*a/m)
    return b*(x*a+k*m)

def solve2(a,b):
    d = 10**(ceil(log10(a)))
    dinv = pow(d, b - 2, b)
    k = ((b - a) * dinv) % b
    return a + d * k

def main():
    total = 0
    for i in range(2,len(primesList)-1):
        total += solve(primesList[i],primesList[i+1])
    return total

print(main(), analytics.lap(), analytics.maxMem())
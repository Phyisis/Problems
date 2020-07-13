"""
37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

1, 3,5,7,9, 13,17,21,25, 31,37,43,49
4n^2+6n+1, 4n^2+6n+5
"""
from helpers import analytics, primes
analytics.monitor()

def poly(n):
    return [4*n**2-2*n+1,4*n**2-4*n+1,4*n**2+2*n+1,4*n**2+1]

def main():
    s = 1
    primeCount = 0
    for n in range(1,20000):
        for m in poly(n):
            if primes.isPrime(m):
                primeCount += 1
        s += 4
        if primeCount/s < 0.1:
            return 2*n+1, primeCount/s
    return primeCount/s

print(main(), analytics.lap(), analytics.maxMem())

# 26241
# time: 9.41
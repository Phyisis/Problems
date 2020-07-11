import repackage; repackage.up()
from helpers import analytics, primes
analytics.monitor()

primes.initialize(10**6)
ns = list(range(1,10000))

def isCube(n):
    return round(n**(1/3))**3 == n

def isSquare(n):
    return round(n**0.5)**2 == n

def main(limit):
    count = 0
    for c in range(1,limit):
        cube = c**3
        for s in primes.divisors(c**3):
            if not isSquare(s): continue
            k = cube//s - round(s**0.5)
            if k < 2: break
            if k < limit and k == int(k) and primes.millerRabin(int(k)):
                count += 1
    return count

print(main(10**2), analytics.lap(), analytics.maxMem())

"""
n**3 + p * n**2 == x**3
p == (x**3-n**3)/(n**2)
p + n == (x**3)/n**2
"""
import repackage; repackage.up()
from helpers import analytics,primes
analytics.monitor()
from math import gcd

limit = int(1e12) # 1e12:? , 1e5:124657
primes.initialize(limit)

def isProgressive(n):
    cuberoot,sqrt = int(n**(1/3)),int(n**0.5)
    for d in range(cuberoot,sqrt):
        if d*d == (n%d)*(n//d):
            return True
    return False

def divisors(n,power=1):
    """ Returns an unsorted list of the divisors of n """
    divs = [1]
    for p, e in primes.factorization(n):
        divs += [x*p**k for k in range(1,power*e+1) for x in divs]
    #print(n,sorted(list(filter(lambda x: x<n,divs))))
    return list(filter(lambda x: x<n,divs))

def main(limit):
    total = 0
    for d in range(2,int(limit**0.5)):
        for r in divisors(d,3):
            n = (d**3)/r+r
            if int(n**0.5)**2==n and n < limit and d*d == (n%d)*(n//d):
                total += n
    return int(total)

print(main(limit), analytics.lap(), analytics.maxMem())
# 878454337159, ~180 seconds
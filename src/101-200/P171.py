from helpers import analytics,primes
analytics.monitor()
from itertools import combinations_with_replacement,groupby,permutations
from math import factorial,prod

digitSqr = list(map(lambda x: x**2,range(1,10)))
#sqr = list(map(lambda x: x**2,range(1,40)))

def f(n):
    return sum(map(lambda x: int(x)**2,str(n)))

def isSqr(n):
    return int(n**0.5)**2 == n

def uniquePerms(p):
    g = (len(list(i)) for _,i in groupby(p))
    return factorial(len(p))//prod(map(factorial,g))

def main():
    total = 0
    for k in range(1,20):
        for c in combinations_with_replacement(digitSqr,k):
            if isSqr(sum(c)):
                total += uniquePerms(c)
    return total

print(main(), analytics.lap(), analytics.maxMem())
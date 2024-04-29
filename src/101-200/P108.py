from helpers import analytics,primes
analytics.monitor()
from fractions import Fraction
from math import prod

"""
1/x+1/y=1/n 
(x+y)/(x*y) = 1/n
x*y/n = (x+y)
x/n-1 = x/y
y = (x*n)/(x-n)
so (x-n) is a divisor of either x or n

(x-n)*(y-n)=n**2
find pairs of divisors x1,y1 := x1*y1 == n**2 with x = x1+n, y = y1+n
"""

limit = int(1e7)
primes.initialize(limit)

def main():
    n = 1
    solutions = 0
    while solutions < 1000:
        solutions = solve(n)
        n += 1
    return n-1

def solve(n):
    return (prod((2*i+1) for _,i in primes.factorization(n).items())+1)//2


print(main(), analytics.lap(), analytics.maxMem())
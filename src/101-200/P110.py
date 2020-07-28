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

limit = int(1e6)
primes.initialize(limit)
#  2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59

def main():
    f = 2*3*5*7*11*13*17*19*23*29*31
    for i in range(limit):
        if solve(i*f) >= 4000000:
            return i*f

def solve(n):
    return (prod((2*i+1) for _,i in primes.factorization(n).items())+1)//2

print(main(), analytics.lap(), analytics.maxMem())
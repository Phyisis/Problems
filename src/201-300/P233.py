"""
Let f(N) be the number of points with integer coordinates that are 
on a circle passing through (0,0), (N,0),(0,N), and (N,N).
It can be shown that f(10000) = 36.
What is the sum of all positive integers N ≤ 10^11 such that f(N) = 420 ?

Center = (N/2,N/2)
(x-N/2)^2 + (y-N/2)^2 = (N^2)/2

y = N/2 +/- sqrt((1/2)N^2-(x-N/2)^2)
y
N*y - y^2 = (N^2)/2 + N*x - x^2
x^2-y^2 = N*(N/2 + x - y)
x^2-y^2-N*x+N*y = N^2/2

Let M = N/2:
(x-M)^2 + (y-M)^2 = 2*M^2
x^2-2Mx+M^2+y^2-2My+M^2 = 2*M^2
x^2+y^2=2M*(x+y)
(x^2+y^2)/(x+y) = N
(x^2+y^2)=N*(x+y)
x^2-N*x = N*y-y^2
x*(x-N)=y*(N-y)

r = N/sqrt(2)
"""
from helpers import analytics,primes
analytics.monitor()
from math import ceil,prod
from itertools import permutations

limit = int(1e11)+1
primesList = primes.initialize(int(1e14))
pm1 = list(filter(lambda x: x%4==1,primesList))

def f(n): #doesn't check for odd powers of 4k+3 primes, since we are squaring n
    while n%4==0:
        n//=4
    if n==1:
        return 4
    c = 1
    for p,k in primes.factorization(n).items():
        if p%4 == 1:
            c *= (2*k+1)
    return ceil(c/2)*8-4
    
def main2(limit):
    total = 0
    for n in range(359125,limit+1):
        if f(n) == 420:
            total += n
    return total

# ceil(c/2)=53
# c/2 = 53 or c/2 = 52.5
# c = 106 or c = 105 it's always 105, since 106 is even

"""
print(primes.divisors(105)) [1,3,5,7,15,21,35,105]
2k+1 in  [3,5,7,15,21,35,105]
possible combinations of exponents of 4k+1 prime factors of n
3*35 # k = 1,17 # not possible under 1e11
5*21 # k = 2,10
7*15 # k = 3,7
3*5*7 # k = 1,2,3
105 # k = 52 # not possible under 1e11
k = 1,2,3,7,10,17,52
"""

def baseSolutions(limit):
    e2 = ((2,10),(3,7))
    e3 = ((1,2,3),)
    P = []
    for e in e2:
        for s in permutations(e):
            P += search2(s,limit)
    for e in e3:
        for s in permutations(e):
            P += search3(s,limit)
    return sorted(P)

def search2(s,limit):
    P = []
    for i1 in range(len(pm1)-1):
        a = pm1[i1]**s[0]
        for i2 in range(i1+1,len(pm1)):
            c = a * pm1[i2]**s[1]
            if c < limit:
                P.append(c)
            else:
                if i1+1 == i2:
                    return P 
                break
    return P

def search3(s,limit):
    P = []
    for i1 in range(len(pm1)-2):
        a = pm1[i1]**s[0]
        for i2 in range(i1+1,len(pm1)-1):
            b = a*pm1[i2]**s[1]
            for i3 in range(i2+1,len(pm1)):
                c = b*pm1[i3]**s[2]
                if c < limit:
                    P.append(c)
                else:
                    if i1+2 == i3:
                        return P 
                    break
    return P

def main(limit):
    base = baseSolutions(limit)
    total = 0
    M = list(filter(lambda n: all(map(lambda x: x%4!=1 or x == 2, primes.factorization(n))),range(1,limit//base[0]+1)))
    for b in base:
        for n in M:
            t = b*n
            if t > limit: break
            total += t
    return total
            
print(main(limit), analytics.lap(), analytics.maxMem())
# 271204031455541309
from helpers import analytics, primes
analytics.monitor()
from functools import reduce
from math import gcd

"""
a<=b<=c, a+b+c <= 10**8
base of subtriangle: c_b = b*c/(a+b)
h = sqrt(-(a-b-c)(a+b-c)(a-b+c)(a+b+c))/(2(a+c))
area of subtriangle: A_s = c_b*h/2
"""
primesList = primes.primes(10**4)

def isIntegerRatio(a,b,c): # a*(a+b+c) % b*c == 0
    return ((a+b)*(a+c)) % (b*c) == 0

def valid(a,b,c,N):
    return c == int(c) and isIntegerRatio(a,b,c) and b < c < min(N-a-b,a+b)

def divisors(n,power=1,facs = []):
    """ Returns an unsorted list of the divisors of n**power """
    divs = [1]
    pf = primes.factorization(n)
    for p in facs:
        if p in pf:
            pf[p] += 1 
        else:
            pf[p] = 1
    for p in pf:
        divs += [x*p**k for k in range(1,power*pf[p]+1) for x in divs]
    return divs

def g(a,N): # count triangles with condition for small side a. 
    count = 0
    for d in divisors(a,2,[2]): #2*a < b <= (1+sqt(2))*a , c = a*(b+a)/(b-a)
        b = d+a
        if b <= 2*a or b > 2.42*a: continue
        c = a*(b+a)/d
        if valid(a,b,c,N):
            count += 1
    for d in divisors(a,2,[3]): #a < b <= (1+sqt(3)//2)*a , c = a*(b+a)/(2*b-a)
        if (d+a)%2: continue
        b = (d+a)//2
        if b <= a or b > 1.37*a: continue
        c = a*(b+a)/d
        if valid(a,b,c,N):
            count += 1
    return count

def main(N):
    count = N//3
    for a in range(1,N//3+1):
        count += g(a,N)
    return count

"""
(a+b)*(a+c)=n*b*c (n<=4)
this equation only has solutions if there is a rational number r=p/q such that
a+b=n/r*c and a+c=r*b
The range of r is constraint by the inequalities a<=b, b<=c and a+b>c.
Thus, for co-prime p,q we get solutions of the form
a/c=(n-1)*q/(p+q) , b/c=(n*q*q+p*q)/p/(p+q)
"""

def main2(nmax):
    cc = nmax // 3
    for q in range(1, int(nmax**0.5) + 1):
        for p in range(q + 1, int(q * 2**0.5) + 1):
            if gcd(p, q) == 1:
                d = 2 if p % 2 == 0 else 1
                r = (p + q) * (p + 2 * q) // d
                cc += nmax // r
        for p in range(q + 1, int(q * 3**0.5) + 1):
            if gcd(p, q) == 1:
                d = (3 if p % 3 == 0 else 1) * (2 if (p + q) % 2 == 0 else 1)
                r = (p + q) * (p + 3 * q) // d
                cc += nmax // r
    return cc


print(main(10**4), analytics.lap(), analytics.maxMem())
# 139012411
# incorrect:
# 139012408
# time: 8730.1334721

"""
for a < b < 2a: c = a*(a+b)/(2b-a)
for 2a < b <= N//2: c = a*(a+b)/(b-a)

when is a*(a+b)/(b-a) an integer?
let x = (b-a), then b = x+a, a*(2a+x)/x = (2a**2)/x + 1

when is a*(a+b)/(2*b-a) an integer?
let x = (2*b-a), then b = x/2+a/2, a*(3a/2+x/2)/x => 3a**2/x

loop through divisors d of a, or a+b
d+a = b, or (d+a)//2 = b 

"""
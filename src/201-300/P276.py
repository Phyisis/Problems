from helpers import analytics, primes
analytics.monitor()
from math import gcd
from functools import reduce

"""
Consider the triangles with integer sides a, b and c with a ≤ b ≤ c.
An integer sided triangle (a,b,c) is called primitive if gcd(a,b,c)=1.
How many primitive integer sided triangles exist with a perimeter not exceeding 10 000 000?
"""

def farey(N): # all coprime pairs a,b with a < b <= N
    a,b,c,d = 1,N,1,N-1
    yield a,b
    while not (c == 1 and d == 1):
        yield c,d
        k = (N + b)//d
        e = k * c - a
        f = k * d - b
        a,b,c,d = c,d,e,f
    return

def main(limit):
    count = 0
    for b,c in farey(limit):
        if 1+b+c > limit or b < 2 or b+b-1 < c: continue
        lo,hi = max(1,c-b+1), min(b,limit-b-c+1)
        if hi > lo: count += (hi-lo)
    return count

print(main(10**3), analytics.lap(), analytics.maxMem())
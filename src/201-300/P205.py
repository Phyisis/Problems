from helpers import analytics
analytics.monitor()
from math import comb

def ways(r,n,s): #to roll r with n, s-sided dice
    m = int((r-n)/s)
    w = 0
    for k in range(0,m+1):
        w += ((-1)**k)*comb(n,k)*comb(r-s*k-1,n-1)
    return w

def P(r,n,s):
    m = int((r-n)/s)
    w = 0
    for k in range(0,m+1):
        w += ((-1)**k)*comb(n,k)*comb(r-s*k-1,n-1)
    return w/s**n

def populate(table,n,s):
    for i in range(0,n*s+1):
        table.append(ways(i,n,s))

def main():
    p,c = [],[]
    populate(p,9,4)
    populate(c,6,6)
    w = 0
    t = (4**9) * (6**6)
    for C in range(0, 37):
        for P in range (C+1, 37):
            w += p[P]*c[C]
    return round(w/t,7)

print(main(), analytics.lap(), analytics.maxMem())
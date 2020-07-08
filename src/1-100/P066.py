import repackage; repackage.up()
from helpers import analytics
analytics.monitor()
from fractions import Fraction

limit = int(1e3)

def contFrac(n):
    m = int(n**0.5)
    p,q = m,1
    h0,k0,h1,k1 = 1,0,m,1
    yield h1,k1
    while True:
        q = Fraction(n-p**2,q)
        d = int(Fraction(p+m,q))
        p = d*q-p        
        h0,k0,h1,k1 = h1,k1,d*h1+h0,d*k1+k0
        yield h1,k1

def pellSolve(D):
    for x,y in contFrac(D):
        if x**2-D*y**2 == 1:
            return x,y
    return 1,0

def main(limit):
    x_min = []
    for D in range(2,limit+1):
        if int(D**0.5)**2==D: continue
        x_min.append([D,pellSolve(D)[0]])
    return max(x_min,key = lambda x: x[1])

print(main(limit), analytics.lap(), analytics.maxMem())
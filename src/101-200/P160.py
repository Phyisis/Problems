from helpers import analytics
analytics.monitor()
from math import factorial

mod = 10**5

def P(n,p): #exponent of prime p, in n!
    a,i,x = 0,0,n
    while x > 0:
        a += x
        i += 1
        x = n//p**i
    return a

def main(n):
    a,b = P(n,2),P(n,5)
    print(pow(2,a-b,mod))
    m = min(a,b)
    t = 1
    for i in range(2,n+1):
        while i%10==0:
            i //= 10
        while i%5==0:
            i //= 5
            t //= 2
        t = (t*i)%mod
    return t%mod

#f(10**6) == 22464
print(main(10**12), analytics.lap(), analytics.maxMem())
# 16576
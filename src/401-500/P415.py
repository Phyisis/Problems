import repackage; repackage.up()
from helpers import analytics
analytics.monitor()
from math import gcd

mod = 10**8
size = 10**5

def T(n,k):
    sum = 0
    max0 = n//(k-1)
    max1 = n//(k)
    max2 = n//(k+1)
    min0 = -(n/(k-1))
    x = max0
    y = max0
    while x >= 0:
        while y >= 1:
            if gcd(x,y) == 1:
                if (x > max1 or y > max1):
                    #print("f1")
                    sum += (n - (k-1)*x)*(n - (k-1)*y) % mod
                elif (x > max2 or y > max2):
                    #print("f2")
                    sum -= 2 * (n - k*x)*(n - k*y) % mod
                    sum += (n - (k-1)*x)*(n - (k-1)*y) % mod
                else:
                    #print("f3")
                    sum += (n - (k+1)*x)*(n - (k+1)*y) % mod
                    sum -= 2 * (n - k*x)*(n - k*y) % mod
                    sum += (n - (k-1)*x)*(n - (k-1)*y) % mod
            y -= 1
        x -= 1
        y = max0
    return 2*sum % mod

def Titanic(N):
    G = (2**((N+1)**2)-1-(N+1)*(N+1)) % mod
    S = 0
    for K in range(3,N+2):
        Z = int(pow(2,K,mod) - 1 - (K)*(K+1)//2) % mod
        M = T(N+1,K)
        S = (S + M*Z) % mod
    R = (G-S) % mod
    return R

def main():
    return Titanic(size)%mod

print(main(), analytics.lap(), analytics.maxMem())

'''
f2(q)=1/3(−2q**3+3(2**(q+1)−1)q**2−(3(2**(q+2))+1)q+18(2**q−1))
f1(q)=−3(N+1)(2**(q+1)−q−2)(q−1)f1(q)=−3(N+1)(2q+1−q−2)(q−1)
f0(q)=4(N+1)2(2**q−q−1)
'''
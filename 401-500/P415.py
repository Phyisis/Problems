import numpy as np
from fractions import gcd
import collections
import functools
import math
from time import clock
time1 = clock()

mod = 10**8
size = 111

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
            #print(str(x) + "," + str(y))
            if gcd(x,y) == 1:
                #print(str(x) + "," + str(y))
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
    #print(G)
    S = 0
    for K in range(3,N+2):
        Z = math.floor(pow(2,K,mod) - 1 - (K)*(K+1)//2) % mod
        M = T(N+1,K)
        #print(M)
        S = (S + M*Z) % mod
    #print(S)
    R = (G-S) % mod
    return R

print(Titanic(size))

time2 = clock()
print("runtime: " + str(time2 - time1))

'''
f2(q)=1/3(−2q**3+3(2**(q+1)−1)q**2−(3(2**(q+2))+1)q+18(2**q−1))
f1(q)=−3(N+1)(2**(q+1)−q−2)(q−1)f1(q)=−3(N+1)(2q+1−q−2)(q−1)
f0(q)=4(N+1)2(2**q−q−1)
'''






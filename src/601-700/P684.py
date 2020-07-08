import repackage; repackage.up()
import math
from functools import lru_cache
from helpers import analytics
analytics.monitor()

mod = 1000000007

def s(n):
    q,r = n//9, n%9 
    return (r+1)*pow(10,q,mod)-1

def S(n):
    n += 1
    q,r = n//9,n%9
    total = 5 * (pow(10,q,mod)-1) 
    for i in range(1,r+1):
        total += s(n-i) % mod
    return total - n + r

def F(n):
    A = [0,1]
    for _ in range(n):
        A.append(A[-2]+A[-1])
    return A

def main(): #from 2 to 90, mod 1000000007
    return sum(S(n) % mod for n in F(90)[2:91]) % mod

print(main(), analytics.lap(), analytics.maxMem())
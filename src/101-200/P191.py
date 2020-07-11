import repackage; repackage.up()
from helpers import analytics
analytics.monitor()
from functools import lru_cache

# 0,1,2 = O, A < 3 consecutive, L < 2
@lru_cache
def T(r,n):
    if n==r: return 2**n - 1
    if n < r: return 2**n
    return sum(T(r,n-i) for i in range(1,r+1))

def main(limit):
    return T(3,limit) + sum(T(3,i)*T(3,limit-(i+1)) for i in range(limit))

print(main(30), analytics.lap(), analytics.maxMem())
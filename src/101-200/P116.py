from helpers import analytics
analytics.monitor()
from functools import lru_cache

@lru_cache
def T(m,i,c=0): #blocksize m, remaining squares i, current block size c
    if i == 0:
        return 1
    s = 0
    if m-c%m <= i : #is it possible to add a red square?
        s += T(m,i-1,c+1)
    if c % m == 0: # is it possible to add a grey square?
        s += T(m,i-1,0)
    return s

def main(n):
    return sum(T(m,n) for m in [2,3,4])-3

print(main(50), analytics.lap(), analytics.maxMem())

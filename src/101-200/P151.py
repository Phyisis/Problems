from helpers import analytics
analytics.monitor()
from functools import lru_cache

@lru_cache
def F(s):
    d = sum(s)
    n = 0   
    if d == 0: return 0
    if d == 1: n += 1    
    for i in range(5):
        if s[i] == 0: continue
        k = tuple(s[x]+1 if x < i 
            else s[x]-1 if x == i  
            else s[x] 
            for x in range(5))
        n += (k[i]+1) * F(k) / d
    return n

def main():
    return round(F((0,0,0,0,1))-2,6)

print(main(), analytics.lap(), analytics.maxMem())
# 0.464399

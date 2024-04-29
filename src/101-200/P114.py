from helpers import analytics
analytics.monitor()
from functools import lru_cache

@lru_cache
def T(m,i,c=0): #minimum blocksize m, remaining squares i, current block size c
    if i == 0:
        return 1
    s = 0
    if c+i >= m: #is it possible to add a red square?
        s += T(m,i-1,c+1)
    if c == 0 or c >= m: # is it possible to add a grey square?
        s += T(m,i-1,0)
    return s

def main():
    return T(3,50)

print(main(), analytics.lap(), analytics.maxMem())

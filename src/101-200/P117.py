from helpers import analytics
analytics.monitor()
from functools import lru_cache

@lru_cache
def T(i): #remaining squares i, current block size c
    if i == 0:
        return 1
    s = T(i-1)
    if i >= 2 : #is it possible to add a red square?
        s += T(i-2)
    if i >= 3 : #is it possible to add a green square?
        s += T(i-3)
    if i >= 4 : #is it possible to add a blue square?
        s += T(i-4)
    return s

def main(n):
    return T(n)

print(main(50), analytics.lap(), analytics.maxMem())

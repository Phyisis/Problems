import repackage; repackage.up()
from helpers import analytics
analytics.monitor()
from functools import lru_cache

t = 10**25

@lru_cache
def count(n):
    if n == (n ^ ( n & (n-1))):
        return n.bit_length()
    r = (n ^ ( n & (n-1))).bit_length() #rightmost bit
    return (r-1)*count((n>>r))+count((n>>r)<<(r-1))

def main():
    return count(t)

print(main(), analytics.lap(), analytics.maxMem())
# 178653872807
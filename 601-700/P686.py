from Problems.helpers import analytics
analytics.monitor()
import math

def lead(n,p):
    d = 1 + int(n*math.log10(2))
    return int(10**(n*math.log10(2)-d+p))

def main(L,n):
    p = len(str(L))
    i = 0
    count = 0
    while count < n:
        i += 1
        if lead(i,p) == L:
            count += 1
    return i

print(main(123,678910), analytics.lap(), analytics.maxMem())

# 193060223
# time: 200.9682563
import operator as op
from functools import reduce

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer / denom

result = 0
for n in range(1,101):
    for r in range(n+1):
        if ncr(n,r) > 1000000:
            result += 1

print(result)
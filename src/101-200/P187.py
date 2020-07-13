from helpers import analytics, primes
analytics.monitor()

limit = int(1e8)
primesList = primes.primes(limit//2)

def binarySearch(A,n,m = 1):
    lo = 0
    hi = len(A)
    i = lo
    while True:
        if lo + 1 == hi:
            if A[i]*m > n:
                return i-1
            return i
        if A[i]*m == n:
            return i
        elif A[i]*m < n:
            lo = i
        elif A[i]*m > n:
            hi = i
        i = (lo+hi)//2

rootIndex = binarySearch(primesList,int(limit**0.5))
pRoot = primesList[rootIndex]

def main():
    total = ((rootIndex+1)*(rootIndex+2))//2 + rootIndex + 1
    for p in primesList[:rootIndex+1]:
        total += binarySearch(primesList[rootIndex+1:],limit,p)
    return total

print(main(), analytics.lap(), analytics.maxMem())

# 17427258
# time: 53.1897325
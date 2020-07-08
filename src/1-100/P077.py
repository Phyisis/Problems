import repackage; repackage.up()
from helpers import analytics, primes
analytics.monitor()

limit = int(1e5)

def primePartitionCount(n):
    ways = [1] + [0] * n
    nums = primes.primes(n)
    for num in nums:
        for i in range(num,n+1):
            ways[i] += ways[i-num]
    return ways

def main(limit):
    w = primePartitionCount(limit)
    for n in range(len(w)):
        if w[n] > 4998:
            return n
    return None

print(main(limit), analytics.lap(), analytics.maxMem())
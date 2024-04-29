from helpers import analytics
analytics.monitor()
import math

primes = [2]

def CheckPrime(num):
    rootn = math.floor(num**(.5))
    for i in primes:
        if i > rootn:
            return True
        if num % i == 0:
            return False
    return True

def main(limit):
    n=3
    while (len(primes) < limit):
        if CheckPrime(n):
            primes.append(n)
        n += 2
    return primes[-1]

print(main(10001), analytics.lap(), analytics.maxMem())
"""
104743 
time: 0.06683887600000002 
max memory: 9.1MB
"""






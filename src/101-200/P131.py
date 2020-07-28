from helpers import analytics, primes
analytics.monitor()

primes.initialize(10**6)

def main(limit):
    a3,b3,i = 0,1,2
    count = 0
    while True:
        x = b3-a3
        if x > limit: break
        if primes.isPrime(x):
            count += 1
        a3,b3,i = b3,i**3,i+1
    return count

print(main(10**6), analytics.lap(), analytics.maxMem())

"""
n**3 + p * n**2 == x**3 and p < 10**6
n**3 * (p/n + 1) == x**3
n**3 * (p+n)/n == x**3
n * cuberoot(p+n)/cuberoot(n) = x
let a**3 = (p+n), b**3 = n
then p = a**3-b**3
p = (a-b)*(a**2+a*b+b**2)
if (a-b) is a factor of p, and p is prime, then a-b == 1
a**3-b**3 < 10**6
"""
import repackage; repackage.up()
from helpers import analytics, primes
analytics.monitor()

limit = int(64e6)
primes.initialize(limit)

def main(limit):
    total = 0
    for i in range(1,limit):
        divs = primes.divisors(i)
        s = sum(map(lambda x: x**2, divs))**0.5
        if s == int(s):
            total += i
    return total

print(main(limit), analytics.lap(), analytics.maxMem())

# 1922364685
# time: 2572.2456758999997
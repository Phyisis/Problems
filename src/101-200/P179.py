import repackage; repackage.up()
from helpers import analytics, primes
analytics.monitor()

limit = int(1e7)
primes.initialize(limit)

def main(limit):
    total = 0
    last = 1
    for i in range(2,limit):
        divs = len(primes.divisors(i))
        if divs == last:
            total += 1
        last = divs
    return total

print(main(limit), analytics.lap(), analytics.maxMem())
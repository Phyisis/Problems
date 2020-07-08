import repackage; repackage.up()
from helpers import analytics, primes
analytics.monitor()

limit = 100

def main(limit):
    return primes.partitionCount(limit) - 1

print(main(limit), analytics.lap(), analytics.maxMem())
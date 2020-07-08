import repackage; repackage.up()
from helpers import analytics,primes
analytics.monitor()

primesList = primes.primes(int(1e8))
primesHash = set(primesList)

def main():
    results = []
    for p in primesList[4:]:
        if len(results) == 11:
            return sum(results), results
        if truncatableLeft(p) and truncatableRight(p):
            results.append(p)
    return sum(results), results
    
def truncatableLeft(p):
    for i in range(1,len(str(p))):
        if int(str(p)[:i]) not in primesHash:
            return False
    return True

def truncatableRight(p):
    for i in range(1,len(str(p))):
        if int(str(p)[len(str(p))-i:len(str(p))]) not in primesHash:
            return False
    return True

print(main(), analytics.lap(), analytics.maxMem())
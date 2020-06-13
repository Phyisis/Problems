from helpers import analytics,primes
analytics.monitor()
from itertools import combinations

primesList = primes.primes(int(1e4)) 

def main():
    perms = {}
    for p in primesList:
        ps = str(sorted(str(p)))
        if ps in perms:
            perms[ps].append(p)
        else:
            perms[ps] = [p]
    results = []
    for p in perms.keys():
        s = sorted(perms[p])
        for c in combinations(s,3):
            if c[1]-c[0] == c[2]-c[1]:
                results.append(c)
    return results

print(main(), analytics.lap(), analytics.maxMem())
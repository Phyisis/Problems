import repackage; repackage.up()
from itertools import combinations
from helpers import analytics,primes
analytics.monitor()

primesList = list(map(str,primes.primes(int(1e6))))
digits = list(map(str,range(10)))

def countkeys(c):
    x = {}
    for p in primesList:
        for d in digits:
            if d in p:
                for k in stringPermutations(d,p):
                    if k in x:
                        x[k] += 1
                        if x[k] == c:
                            return lowestPrime(k)
                    else:
                        x[k] = 1
    return False

def stringPermutations(d,p):
    perms = []
    indices = [i for i in range(len(p)) if p[i]==d]
    for i in range(len(indices)+1):
        for c in combinations(indices,i):
            s = list(p)
            for j in c:
                s[j]="*"
            perms.append(''.join(s))
    return perms

def lowestPrime(k):
    for d in digits:
        if k.replace("*",d) in primesList:
            return k.replace("*",d)

def main():
    return countkeys(8)

print(main(), analytics.lap(), analytics.maxMem())
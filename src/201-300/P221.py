from helpers import analytics, primes
analytics.monitor()

#The numbers are of the form p(p+d)(p+(p^2+1)/d), 
# where d runs over divisors of p^2+1 and p runs over all positive integers.
primesList = primes.initialize(10**12+10)

def main():
    A = set()
    for p in range(10**5):
        q = p**2 + 1
        for d in primes.divisors(q):
            if d*d > q: continue
            x = p*(p+d)*(p+q//d)
            #print(x)
            A.add(x)
    return sorted(list(A))[150000]

print(main(), analytics.lap(), analytics.maxMem())
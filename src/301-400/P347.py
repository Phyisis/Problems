from helpers import analytics, primes
analytics.monitor()

limit = 10**7
primesList = primes.primes(int(limit**0.5)+1)          

def sf(n):
    pcount,pf = 0,[]
    for p in primesList:
        if p*p > n: break
        count = 0
        while n%p==0:
            n //= p
            count += 1
        if count > 0: 
            pf.append(p)
            pcount += 1
        if pcount == 2 and n > 1: return []
    if n > 1:
        pf.append(n)
        pcount += 1
        if pcount > 2: return []
    return tuple(pf)   

def main(limit):
    pairs = {}
    for n in range(1,limit+1):
        pf = sf(n)
        if len(pf) == 2:
            pairs[pf] = n
    return sum(pairs.values())

# S(100) = 2262
# S(10**7) = ?
print(main(limit), analytics.lap(), analytics.maxMem())
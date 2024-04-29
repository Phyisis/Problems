from helpers import analytics, primes
analytics.monitor()

pl = primes.primes(int(1e6))
primesHash = set(pl)

def main():
    longest = 0
    result = None
    for i in range(1,len(pl)):
        pl[i] += pl[i-1]
    for i in range(3):
        for j in range(i+1+longest,len(pl)):
            if j > len(pl):
                return result, longest
            q = pl[j]-pl[i]
            if q in primesHash:
                if j-i > longest:
                    longest = j-i
                    result = q
    return result, longest

print(main(), analytics.lap(), analytics.maxMem())
"""
(997651, 543) 
time: 0.18962122399999998 
max memory: 18.8MB
"""
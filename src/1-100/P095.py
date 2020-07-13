from helpers import analytics, primes
analytics.monitor()

limit = int(1e6)
primes.initialize(limit)

def sumOfDivs(n):
    divs = primes.divisors(n)
    return sum(divs) - n

def main():
    longest = (0,None,None)
    seen = set([1])
    for n in range(2,limit+1):
        chain = [n]
        while n < limit:
            if n in seen:
                break
            n = sumOfDivs(n)
            if n in chain:
                s = chain.index(n)
                if len(chain) - s > longest[0]:
                    longest = (len(chain) - s,min(chain[s:]),chain)
                    print(longest)
                break
            chain.append(n)
        seen.update(chain)
    return longest

print(main(), analytics.lap(), analytics.maxMem())
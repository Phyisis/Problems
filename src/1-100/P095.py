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
"""
(1, 6, [6])
(2, 220, [220, 284])
(28, 14316, [5916, 9204, 14316, 19116, 31704, 47616, 83328, 177792, 295488, 629072, 589786, 294896, 358336, 418904, 366556, 274924, 275444, 243760, 376736, 381028, 285778, 152990, 122410, 97946, 48976, 45946, 22976, 22744, 19916, 17716])
(28, 14316, [5916, 9204, 14316, 19116, 31704, 47616, 83328, 177792, 295488, 629072, 589786, 294896, 358336, 418904, 366556, 274924, 275444, 243760, 376736, 381028, 285778, 152990, 122410, 97946, 48976, 45946, 22976, 22744, 19916, 17716]) 
time: 16.503591836000002 
max memory: 73.8MB
"""
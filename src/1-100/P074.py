from helpers import analytics
analytics.monitor()
from math import factorial

limit = int(1e6)

def sumOfFac(n):
    return sum(factorial(int(d)) for d in str(n))

def main():
    count = 0
    seen = set([1])
    for n in range(2,limit+1):
        chain = [n]
        while True:
            n = sumOfFac(n)
            if n in chain:
                if len(chain) == 60:
                    count += 1
                break
            chain.append(n)
        seen.update(chain)
    return count

print(main(), analytics.lap(), analytics.maxMem())
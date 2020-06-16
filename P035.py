from helpers import analytics,primes
analytics.monitor()

limit = int(1e6)
pu = set(primes.primes(limit))

def circular(p):
    rs = [int(str(p)[-r:]+str(p)[:-r]) for r in range(len(str(p)))]
    for n in rs:
        if n not in pu:
            return False
    return True

def main():
    return len(list(filter(circular, pu)))

print(main(), analytics.lap(), analytics.maxMem())
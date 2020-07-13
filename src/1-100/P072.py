from helpers import analytics, primes
analytics.monitor()

limit = int(1e6)+1

def main():
    return sum(primes.totients(limit)[2:-2])

print(main(), analytics.lap(), analytics.maxMem())
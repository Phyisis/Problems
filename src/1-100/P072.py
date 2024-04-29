from helpers import analytics, primes
analytics.monitor()

limit = int(1e6)+1

def main():
    return sum(primes.totients(limit)[2:-2])

print(main(), analytics.lap(), analytics.maxMem())
"""
303963152391 
time: 0.9575981140000001 
max memory: 25.3MB
"""
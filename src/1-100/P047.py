from helpers import analytics, primes
analytics.monitor()
primes.initialize()

def main(target):
    i = 1
    run = 0
    first = 1
    while True:
        i += 1
        pf = primes.factorization(i)
        if len(pf) == target:
            run += 1
            if run == 1:
                first = i
            if run == target:
                return first
        else:
            run = 0

print(main(4), analytics.lap(), analytics.maxMem())
"""
134043 
time: 0.536603128 
max memory: 9.6MB
"""

from helpers import analytics, primes
analytics.monitor()

limit = int(1e7)
phi = primes.totients(limit)

def main(limit):
    n_min = 2
    for i in range(2, limit + 1):
        if i / phi[i] < n_min / phi[n_min]:
            if sorted(str(i)) == sorted(str(phi[i])):
                n_min = i
    return n_min

print(main(limit), analytics.lap(), analytics.maxMem())
"""
8319823 
time: 15.986644459 
max memory: 395.9MB
"""
from helpers import analytics, primes
analytics.monitor()

limit = int(1e6)

def main(limit):
    phi = primes.totients(limit)
    return max(range(1,len(phi)), key=lambda i:i/phi[i])

print(main(limit), analytics.lap(), analytics.maxMem())
"""
510510 
time: 1.2458872669999999 
max memory: 17.6MB
"""
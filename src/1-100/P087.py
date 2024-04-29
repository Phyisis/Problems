import math, itertools
from helpers import analytics, primes
analytics.monitor()

def main():
    counted = set()
    limit = int(5e7)
    pu = primes.primes(int(limit**(1/2)+100)) #((7069,i:907),(367,i:72),(83,i:22))
    for i in range(22+1):
        for j in range(72+1):
            for k in range(907+1):
                n = pu[k]**2 + pu[j]**3 + pu[i]**4
                if n < limit:
                    if n not in counted:
                        counted.add(n)
                else: break
    return len(counted)
    
print(main(), analytics.lap(), analytics.maxMem())
"""
1097343 
time: 3.28581918 
max memory: 72.4MB
"""
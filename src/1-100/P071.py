from helpers import analytics
analytics.monitor()
from fractions import Fraction

def main():
    target = Fraction(3,7)
    d_max = int(1e6)+1
    n,d = 0,1
    distance = 1
    closest = None
    while d < d_max:
        f = Fraction(n,d)
        if f < target:
            if target-Fraction(n,d)<distance:
                closest = (n,d)
                distance = target-Fraction(n,d)
            n += 1
        else:
            d += 1
    return Fraction(*closest)

print(main(), analytics.lap(), analytics.maxMem())
"""
428570/999997 
time: 6.63748115 
max memory: 9.1MB
"""
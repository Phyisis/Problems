import repackage; repackage.up()
from functools import lru_cache
from helpers import analytics
analytics.monitor()
from fractions import Fraction

@lru_cache
def contFrac(i):
    if i == 0:
        return Fraction(1,2)
    return Fraction(1,2+contFrac(i-1))

def main():
    total = 0 
    for i in range(1000):
        f = 1 + contFrac(i)
        if len(str(f.numerator)) > len(str(f.denominator)):
            total += 1
    return total

print(main(), analytics.lap(), analytics.maxMem())
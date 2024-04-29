from helpers import analytics
analytics.monitor()
from fractions import Fraction

def oplus(a,b):
    return Fraction(1,Fraction(1,a)+Fraction(1,b))

def main():
    seen = {1}
    for _ in range(1,18):
        for s in list(seen):
            seen.update([oplus(1,s),1+s])
    return len(seen)

print(main(), analytics.lap(), analytics.maxMem())
# 3857447
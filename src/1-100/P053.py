from math import comb
from helpers import analytics
analytics.monitor()

def main():
    result = 0
    for n in range(1,101):
        for r in range(n+1):
            if comb(n,r) > 1000000:
                result += 1
    return result

print(main(), analytics.lap(), analytics.maxMem())
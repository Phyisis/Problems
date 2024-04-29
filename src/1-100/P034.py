from helpers import analytics
analytics.monitor()
from math import factorial

def main():
    total = 0
    for i in range(3, int(5e4)):
        if sum([factorial(int(n)) for n in str(i)]) == i:
            total += i
    return total

print(main(), analytics.lap(), analytics.maxMem())
"""
40730 
time: 0.153595637 
max memory: 8.8MB
"""
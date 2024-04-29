from itertools import permutations
from helpers import analytics
analytics.monitor()

primesList = (2, 3, 5, 7, 11, 13, 17)

def valid(s):
    for i in range(1, 8):
        if int(s[i:i+3]) % primesList[i-1]:
            return False
    return True

def main():
    total = 0
    for c in permutations(range(10)):
        s = ''.join(map(str,c))
        if valid(s):
            total += int(s)
    return total

print(main(), analytics.lap(), analytics.maxMem())
"""
16695334890 
time: 12.013062833000001 
max memory: 8.8MB
"""
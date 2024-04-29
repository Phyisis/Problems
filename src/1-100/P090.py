from itertools import combinations
from helpers import analytics
analytics.monitor()

digits = [0,1,2,3,4,5,6,7,8,6]
dice = list(combinations(digits,6))
pairs = ((0,1),(1,8),(0,6),(1,6),(3,6),(4,6),(0,4),(2,5))

def valid(a,b):
    return all(x in a and y in b or x in b and y in a for x,y in pairs)

def main():
    total = 0
    for a in range(len(dice)):
        for b in range(a,len(dice)):
            if valid(dice[a],dice[b]):
                total += 1
    return total

print(main(), analytics.lap(), analytics.maxMem())
"""
1217 
time: 0.052157204 
max memory: 8.9MB
"""
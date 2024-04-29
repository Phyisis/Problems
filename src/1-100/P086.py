from helpers import analytics
from math import isqrt,gcd
analytics.monitor()
"""
def minPath(a,b,c):
    return (c**2+(a+b)**2)

def main():
    total = 0
    limit = 1
    while total < 1000000:
        for i in range(1,limit+1):
            for j in range(i,limit+1):
                m = minPath(i,j,limit)
                if m == isqrt(m)**2:
                    total += 1
        limit += 1
    return total,limit-1

print(main(), analytics.lap(), analytics.maxMem())
"""
"""
(1000457, 1818) 
time: 1362.1862480690002 
max memory: 8.8MB
"""

def main(limit):
    count = 0
    longest_side = 0
    while count <= limit:
        longest_side += 1
        for sum_of_short_sides in range(1, 2*longest_side + 1): 
            sqrt = (longest_side**2 + sum_of_short_sides**2)**0.5
            if sqrt == int(sqrt):
                if sum_of_short_sides <= longest_side:
                    count += sum_of_short_sides // 2
                else:
                    count += 1 + (longest_side - (sum_of_short_sides+1)//2)
    return longest_side

print(main(1000000), analytics.lap(), analytics.maxMem())
"""
1818 
time: 3.568579828 
max memory: 8.8MB
"""
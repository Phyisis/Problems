#using Pell's equation
from helpers import analytics
analytics.monitor()

def main():  
    limit = int(1e9)
    offset = [-1,1]
    x = 2
    y = 1  
    result = 0
    while True:
        for b in offset:
            p = 2 * x + b
            areaX3 = y * (x + 2*b)
            if (p > limit): 
                return result        
            if (p > 0 and areaX3 > 0 and p % 3 == 0 and areaX3 % 3 == 0):
                result += p + b        
        x,y = (2 * x + y * 3, y * 2 + x)

print(main(), analytics.lap(), analytics.maxMem())
"""
518408346 
time: 0.0001453100000000096 
max memory: 8.8MB
"""
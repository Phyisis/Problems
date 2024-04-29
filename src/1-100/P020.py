import math
from helpers import analytics
analytics.monitor()

def main():
    return sum(map(int,str(math.factorial(100))))

print(main(), analytics.lap(), analytics.maxMem())
"""
648 
time: 0.00023186999999999514 
max memory: 8.8MB
"""








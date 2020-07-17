import math
from helpers import analytics
analytics.monitor()

def main():
    return sum(map(int,str(math.factorial(100))))

print(main(), analytics.lap(), analytics.maxMem())








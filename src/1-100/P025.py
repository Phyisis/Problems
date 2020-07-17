from helpers import analytics
analytics.monitor()
from math import log10, ceil

limit = 1000

def main(limit):  
    n0,n1 = 0,1
    count = 1        
    while (ceil(log10(n1)) < limit):
        n0,n1 = n1,n0+n1
        count += 1
    return count

print(main(limit), analytics.lap(), analytics.maxMem())









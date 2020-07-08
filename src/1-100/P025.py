import repackage; repackage.up()
from helpers import analytics
analytics.monitor()
from math import log10, ceil

limit = 1000

def GetNext(n0,n1):
    return n1,n0+n1

def main(limit):  
    n0 = 0
    n1 = 1
    FibSeq = [n0,n1]        
    while (ceil(log10(FibSeq[len(FibSeq)-1])) < limit):
        n0,n1 = GetNext(n0,n1)
        FibSeq.append(n1)
    return len(FibSeq)-1

print(main(limit), analytics.lap(), analytics.maxMem())









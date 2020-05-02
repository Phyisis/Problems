import numpy as np
import random
from fractions import gcd
from functools import reduce
import math

max = 1000
n0 = 0
n1 = 1
FibSeq = [n0,n1]

def GetNext(n0,n1):
    n2 = n0 + n1
    return n1,n2
    
while (math.ceil(math.log(FibSeq[len(FibSeq)-1],10)) < max):
    n0,n1 = GetNext(n0,n1)
    FibSeq.append(n1)

print(len(FibSeq)-1)









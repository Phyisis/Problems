import numpy as np
import random
from fractions import gcd
from functools import reduce
import math

min = 2
max = 10000
sum = 0

def GetDivisorsSum(num):
    dsum = 0
    half = math.floor(num/2.0)
    for i in range(1,half+1):
        if (num % i == 0):
            dsum += i
    return dsum

for i in range(min,max+1):
    idiv = GetDivisorsSum(i)
    if (i == GetDivisorsSum(idiv) and i != idiv):
        print(i,idiv)
        sum += i

print(sum)









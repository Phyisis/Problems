import numpy as np
import random
from fractions import gcd
from functools import reduce
import math

def GetDivisorsSum(num):
    i = 2
    dsum = 1
    limit = int(num**0.5)
    while i <= limit:
        if (num % i == 0):
            if i != num/i:
                dsum += i + num//i
            else:
                dsum += i
                break
        i+=1
    return dsum


abundants = []

for i in range(12,28140):
    if GetDivisorsSum(i) > i:
        abundants.append(i)

print("abundants:",len(abundants))

def isPair(A,num):
    B = {abundants[i]:i for i in range(len(abundants))}
    for i in range(len(A)):
        if (num-A[i]) in B:
            return True
        B[A[i]] = i
    return False

total = 0
for i in range(1,28130):
    if not isPair(abundants,i):
        total += i

print("total:",total)

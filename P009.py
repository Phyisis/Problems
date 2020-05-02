import numpy as np
import random
from fractions import gcd
from functools import reduce
import math

n = 1000
max = math.floor(n**(.5))

def GetTriple(u,v):
    a = u**2 - v**2
    b = 2*u*v
    c = u**2 + v**2
    return [a,b,c]

for i in range(1,max):
    for j in range(1,max):
        trip = GetTriple(i,j)
        if ((trip[0] + trip[1] + trip[2]) == 1000):
            print(trip[0])
            print(trip[1])
            print(trip[2])
            print(trip[0] * trip[1] * trip[2])
        









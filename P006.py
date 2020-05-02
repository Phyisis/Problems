import numpy as np
import random
from fractions import gcd
from functools import reduce
import math


min = 1
max = 100
sum = 0
sumsqr = 0
sqrsum = 0
dif = 0

for i in range(min,max+1):
    sumsqr += i**2
    sum += i
   
sqrsum = sum**2
dif = sqrsum - sumsqr

print(dif)





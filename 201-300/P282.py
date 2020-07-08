import numpy as np
import random
from fractions import gcd
from functools import reduce
import math
import _Utility_ as U

mod = 14**8

def A(m,n):
    if (m==0): return n+1
    if (m>0 and n==0): return A(m-1,1)
    if (m>0 and n>0): return A(m-1,A(m,n-1))
    

test = A(3,3)
print(test)

m = 5
n = 5

data = np.zeros((m,n))

for m in range(0,m):
    for n in range(0,n):
        data[n,m] = A(m,n)

print(data)

#print(U.format_matrix(['0','1','2','3','4'],data,'{:^{}}', '{:<{}}', '{:>{}.3f}', '\n', ' | '))

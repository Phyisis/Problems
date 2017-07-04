import numpy as np
import random
from fractions import gcd

min = 0
max = 4000000
sum = 0

n1 = 1
n2 = 2

while (n2 < max):
        if n2 % 2 == 0:
                sum += n2
        temp = n1 + n2
        n1 = n2
        n2 = temp


                
print(sum)

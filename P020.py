import numpy as np
import random
from fractions import gcd
from functools import reduce
import math

result = math.factorial(100)
sum = 0

for i in range(0,len(str(result))):
    sum += int(str(result)[i])

print(sum)









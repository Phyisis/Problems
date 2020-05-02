import numpy as np
import random
from fractions import gcd

min = 0
max = 1000
sum = 0

def MultipleOfThree(n):
        r = 0
        while n:
                r, n = r + n % 10, n // 10
        if (r % 3 == 0):
                return True
        else:
                return False

def MultipleOfFive(n):
        if (n % 10 == 0) or (n % 10 == 5):
                return True
        else:
                return False


for i in range(min,max):
        if MultipleOfThree(i) or MultipleOfFive(i):
                sum += i
                
print(sum)

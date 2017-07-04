import numpy as np
import random
from fractions import gcd
import math


min = 900
max = 999

def Palindrome(n):
        temp = str(n)
        for i in range(0,len(temp)-1):
                if temp[i] != temp[len(temp)-1-i]:
                        return False
        return True

for i in range(max,min,-1):
        for j in range(max,min,-1):
                if Palindrome(i*j):
                        print(i*j)




import numpy as np
import random
from fractions import gcd
from functools import reduce
import math
import string

def getScore(name):
    score = len(name) 
    for letter in name:
        score += string.ascii_uppercase.index(letter)
    return score

namesFile = open("p022_names.txt", "r")
names = []

for line in namesFile:
    names += [name.strip('"') for name in line.split(",")]

names.sort()
total = 0

for i in range(len(names)):
    total += getScore(names[i])*(i+1)   

print(total) 


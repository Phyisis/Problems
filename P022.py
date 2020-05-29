import numpy as np
import random, math, string, os
from fractions import gcd
from functools import reduce

def getScore(name):
    score = len(name) 
    for letter in name:
        score += string.ascii_uppercase.index(letter)
    return score

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "bin", "p022_names.txt")
namesFile = open(filename, "r")
names = []

for line in namesFile:
    names += [name.strip('"') for name in line.split(",")]

names.sort()
total = 0

for i in range(len(names)):
    total += getScore(names[i])*(i+1)   

print(total) 


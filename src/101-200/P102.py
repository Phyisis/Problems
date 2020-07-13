from helpers import analytics
analytics.monitor()
import os
from math import acos,pi

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "Problems/bin", "p102_triangles.txt")
triangleFile = open(filename, "r")
triangles = []

for line in triangleFile:
    t = list(map(int,line.split(",")))
    triangles.append(((t[0],t[1]),(t[2],t[3]),(t[4],t[5])))

def dot(a,b):
    return sum(a[i]*b[i] for i in range(len(a)))

def magnitude(a):
    return sum(x**2 for x in a)**0.5

def angleBetween(a,b):
    return acos(dot(a,b)/(magnitude(a)*magnitude(b)))

def main():
    total = 0
    for t in triangles:
        angleSum = sum(angleBetween(t[i],t[i+1]) for i in range(-1,2))
        if abs(angleSum-2*pi) < 0.00001:
            total += 1
    return total

print(main(), analytics.lap(), analytics.maxMem())
import math, os
from helpers import analytics
analytics.monitor()

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "bin", "p099_base_exp.txt")
baseExpPairsFile = open(filename, "r")

pairs = [[int(n) for n in line.split(",")] for line in baseExpPairsFile]

def main():    
    largest = 0
    line = 0
    for i in range(len(pairs)):
        a,b = pairs[i]
        if b*math.log(a) > largest:
            largest = b*math.log(a)
            line = i+1
    return line

print(main(), analytics.lap(), analytics.maxMem())
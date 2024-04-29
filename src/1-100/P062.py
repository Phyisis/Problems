#Find the smallest cube for which exactly five permutations of its digits are cube.
from helpers import analytics
analytics.monitor()

cubes = {"1":[1,1]}

def search():
    i = 2
    while True:
        nextCube = ''.join(sorted(str(i**3)))
        if nextCube in cubes:
            cubes[nextCube][0] += 1
            cubes[nextCube].append(i)
            if cubes[nextCube][0] == 5:
                return cubes[nextCube]
        else:
            cubes[nextCube] = [1,i]
        i += 1

def main():
    return search()[1]**3

print(main(), analytics.lap(), analytics.maxMem())
"""
127035954683 
time: 0.019725740000000005 
max memory: 10.5MB
"""
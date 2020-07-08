from functools import reduce
from math import gcd
n = 2

def M(num):
    t = [0,0,0]
    sets = []
    while (t != [num,num,num]):
        if (t[2] < num):
            t[2] += 1
            if CheckGcd(t):
                sets.append(t[:])
            continue
        if (t[2] == num):
            t[2] = 0
            if (t[1] < num):
                t[1] += 1
                if CheckGcd(t):
                    sets.append(t[:])
                continue
        if (t[1] == num):
            t[2] = 0
            t[1] = 0
            t[0] += 1
            if CheckGcd(t):
                sets.append(t[:])
            continue
    return sets

def CheckGcd(s):
    if (reduce(gcd,(s[0],s[1],s[2])) == 1):
        return True
    return False

def ChooseNext(num,prev):
    for i in range(len(prev)-1,-1,-1):
        if (i == 0 and prev[i] == (num - len(prev)) and prev[i] != 0):
            for k in range(len(prev)):
                prev[k] = k
            prev.append(len(prev))
            return prev
        if (prev[i] == num-1):
            continue
        if (i+1 < len(prev) and prev[i]+1 == prev[i+1]):
            continue
        prev[i] += 1
        j = i
        while (j < len(prev)-1):
             prev[j+1] = prev[j] + 1
             j += 1
        return prev

def IsTrivial(i):
    if (i[0] == i[1] == i[2]):
        return True
    return False

def HasSolution(matrix):
    x = False
    y = False
    z = False
    for i in matrix:        
        if i[0] >= i[1] and i[0] >= i[2]:
            x = True
            continue
        if i[1] >= i[0] and i[1] >= i[2]:
            y = True
            continue
        if i[2] >= i[0] and i[2] >= i[1]:
            z = True
            continue
        if (x and y and z): return True
    return False


def E(num):
    #number of subsets which have linear solutions through 1,1,1
    sets = M(num)
    print(sets)
    subset = [0]
    numValid = 0
    for i in range(2**len(sets)-1):
        valid = False
        toMix = []
        for j in subset:
            if IsTrivial(sets[j]):
                numValid += 1
                continue
            toMix.append(sets[j])
        if HasSolution(toMix):
            valid = True
        if valid: numValid += 1
        subset = ChooseNext(len(sets),subset)
    return numValid

solutions = E(n)
print(solutions)

      

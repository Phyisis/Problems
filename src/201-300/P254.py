from helpers import analytics
analytics.monitor()
from math import factorial

fac = {i:factorial(i) for i in range(10)}
print(fac)

def f(n): # sum of factorials of digits
    return sum(fac[i] for i in map(int,str(n)))

def sf(n): # sum of digits of f(n)
    return sum(map(int,str(f(n))))

def g(n): #minimum i such that sf((i)) == n
    i = 1
    while sf(i) != n:
        i += 1
    return i 

def sg(n): # sum of digits of g(n)
    return sum(map(int,str(g(n))))

def main(limit):
    for n in range(1,limit):
        print(n,f(n),sf(n),g(n),sg(n))
    #return sum(sg((n)) for n in range(1,limit+1))

print(main(20), analytics.lap(), analytics.maxMem())

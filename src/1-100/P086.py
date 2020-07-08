import repackage; repackage.up()
from helpers import analytics
analytics.monitor()

squares = set([x**2 for x in range(1,int(1e5))])

def minPath(a,b,c):
    return (c**2+(a+b)**2)

def main():
    total = 0
    limit = 1
    while total < 1000000:
        for i in range(1,limit+1):
            for j in range(i,limit+1):
                if minPath(i,j,limit) in squares:
                    total += 1
        limit += 1
    return total,limit-1

print(main(), analytics.lap(), analytics.maxMem())
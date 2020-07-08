import repackage; repackage.up()
from helpers import analytics
analytics.monitor()

limit = 12000

def main():
    a,b,c,d = 1,3,4000,11999
    r = 0
    while not (c == 1 and d == 2):
        k = (limit + b)//d
        e = k * c - a
        f = k * d - b
        a,b,c,d = c,d,e,f
        r += 1
    return r

print(main(), analytics.lap(), analytics.maxMem())
import repackage; repackage.up()
from helpers import analytics
analytics.monitor()
from math import log10,ceil

phi = (1 + 5**.5)/2

def fDigits(n):
    a,b = log10((1 + 5**.5)/2),log10(5)/2
    return ceil(n*a-b) 

def isPandigital(n):
    return sorted(list(str(n)[:9])) == ["1","2","3","4","5","6","7","8","9"]

def firstN(num,n):
    return int(str(num)[:n])

def lastN(num,n):
    return num % 10**n

def main():
    n = 2
    f1,f2, l1,l2, dc1,dc2 = 1,1, 1,1, 1,1
    while True:
        if isPandigital(f2) and isPandigital(l2):
            return n
        m = 1
        if dc2 > 18:
            m = 10**(dc2-dc1)
        n += 1
        f1,f2, l1,l2, dc1,dc2 = f2,firstN(f1+f2*m,18), l2,lastN(l1+l2,9), dc2,fDigits(n)

print(main(), analytics.lap(), analytics.maxMem())
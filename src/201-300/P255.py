import repackage; repackage.up()
from helpers import analytics
analytics.monitor()
from math import floor,ceil
from random import randint

def roundedSqrt(n):
    d,steps = len(str(n)),0
    x1,x2 = 0,0
    if d%2==0:
        x2 = 7*10**((d-2)//2)
    else:
        x2 = 2*10**((d-1)//2)
    while x2 != x1:
        x1,x2 = x2, floor((x2+ceil(n/x2))/2)
        steps += 1
    return steps

def main(limit):
    count,a1,a2 = 1,0,roundedSqrt(limit//10)
    for n in range(limit//10+1,limit):
        count += 1
        q = roundedSqrt(n)
        print(n,q)
        a1,a2 = a2, a2 + (q-a2)/count
    return round(a2,10)

# 10**5 expect: 3.2102888889
# 10**14:
print(main(10**5), analytics.lap(), analytics.maxMem())

# 144463/45000
# 1504433/450000
# 16245001/4500000
# 1444463 1504433 16245001

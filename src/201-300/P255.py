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
    count,a = 1,roundedSqrt(limit//10)
    for n in range(limit//10+1,limit):
        count += 1
        q = roundedSqrt(n)
        a = a + (q-a)/count
    return round(a,10)

# 10**5 expect: 3.2102888889
# 10**14: ~15.27
print(main(10**2), analytics.lap(), analytics.maxMem())

# 10**2: 93/45 
# 10**3: 1181/450
# 10**4: 1703/600
# 10**5: 144463/45000 in 0.617 sec
# 10**6: 1504433/450000 in 2.88 sec
# 10**7: 16245001/4500000 in 31.35 sec

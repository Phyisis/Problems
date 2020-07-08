import repackage; repackage.up()
from decimal import Decimal,getcontext
import math
from helpers import analytics
analytics.monitor()

getcontext().prec = 110

def digitSum(n):
    digits = str(Decimal(n).sqrt()).replace('.','')
    return sum(int(x) for x in digits[:100])

def isirrational(n):
    sqrt = math.sqrt(n)
    return sqrt != int(sqrt)

def main():
    return sum(map(digitSum,filter(isirrational,range(1,101))))

print(main(), analytics.lap(), analytics.maxMem())

# 40886 time: 0.00285
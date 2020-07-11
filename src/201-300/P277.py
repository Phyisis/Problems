import repackage; repackage.up()
from helpers import analytics
analytics.monitor()
#UDDDUdddDDUDDddDdDddDDUDDdUUDd
#100012220010022020220010021102 f
#201120010022020220010022210001 finv

#0,1,2 = D,U,d
f = [lambda x: x//3, lambda x: (4*x+2)//3, lambda x: (2*x-1)//3]
finv = [lambda x: 3*x, lambda x: (x*3-2)//4, lambda x: (x*3+1)//2]

def up(n):
    k = map(int,"201120010022020220010022210001")
    for i in k:
        n = finv[i](n)
    return n

def main():
    i = 1
    while up(i) < 10**15:
        i += 1
    return i

print(main(), analytics.lap(), analytics.maxMem())
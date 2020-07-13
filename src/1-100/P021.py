from helpers import analytics
analytics.monitor()

def GetDivisorsSum(num):
    dsum = 0
    half = int(num/2.0)
    for i in range(1,half+1):
        if (num % i == 0):
            dsum += i
    return dsum

def main(limit):
    total = 0
    for i in range(2,limit+1):
        idiv = GetDivisorsSum(i)
        if (i == GetDivisorsSum(idiv) and i != idiv):
            #print(i,idiv)
            total += i
    return total
    
print(main(10000), analytics.lap(), analytics.maxMem())









from helpers import analytics
analytics.monitor()

def GetNumDivisors(num):
    divisors = 0
    rootn = int(num**(.5))
    for i in range(2,rootn):
        if (num % i == 0):
            divisors += 2
        if rootn**2 == num:
            divisors -= 1
    return divisors

def main(limit):
    nt = 1
    tnum = 0
    while (GetNumDivisors(tnum) < limit):
        tnum += nt
        nt += 1
    return tnum

print(main(500), analytics.lap(), analytics.maxMem())
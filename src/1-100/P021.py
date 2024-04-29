from helpers import analytics,primes
analytics.monitor()
primes.initialize(1000)

def d0(num): #original d(n)
    dsum = 1
    for i in range(2,num//2+1):
        if (num % i == 0):
            dsum += i
    return dsum

def d(n):
    return sum(primes.divisors(n))-n

def main(limit):
    total = 0
    for i in range(2,limit+1):
        idiv = d(i)
        if (i == d(idiv) and i != idiv):
            #print(i,idiv)
            total += i
    return total

print(main(10000), analytics.lap(), analytics.maxMem())
"""
31626 
time: 0.31672321200000003 
max memory: 9.6MB
"""









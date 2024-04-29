from helpers import analytics
analytics.monitor()

n = 3
primes = {2:0}

def isPrime(num):
    if num in primes: return True
    if num < 2: return False
    rootn = int(num**(.5))
    for i in primes:
        if i > rootn:
            return True
        if num % i == 0:
            return False
    return True

def extendPrimes(num):
    global n
    if num < 2: return False
    while n < int(num**(.5)):
        if isPrime(n):
            primes[n]=0
        n += 2
    return isPrime(num)

def main():
    longest = (0,0,0,0)
    for a in range(-999,1000):
        for b in range(-1000,1001):
            x = 0
            while extendPrimes(x**2+a*x+b):
                x+=1
            x-=1
            if x > longest[0]:
                longest = (x,a,b,a*b)
    return longest[-1]

print(main(), analytics.lap(), analytics.maxMem())  
"""
-59231 
time: 4.362433255999999 
max memory: 8.8MB
"""        
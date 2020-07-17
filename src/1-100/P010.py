from helpers import analytics
analytics.monitor()

primes = [2]

def CheckPrime(num):
    rootn = int(num**(.5))
    for i in primes:
        if i > rootn:
            return True
        if num % i == 0:
            return False
    return True

def main(limit):
    total = 2
    n = 3
    while (n < limit):
        if CheckPrime(n):
            primes.append(n)
            total += n
        n += 2
    return total

print(main(2000000), analytics.lap(), analytics.maxMem())






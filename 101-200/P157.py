from Problems.helpers import analytics,primes
analytics.monitor()
from math import gcd
"""
1/a+1/b==p/10**n, a <= b
2**n * 5**n == p* a*b/(a+b)
10**n/a+10**n/b == p
lcm(a,b) % 10**n == 0 or 10**n % lcm(a,b) == 0
1/a terminates iff a == 2**k1 * 5**k2, with decimal of length lcm(k1,k2)
"""
def lcm(a,b):
    return (a*b)/gcd(a,b)

a = 2**4 * 5**6
print(1/a,lcm(4,6))

def main():
    return 

print(main(), analytics.lap(), analytics.maxMem())
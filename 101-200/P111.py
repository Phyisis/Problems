from Problems.helpers import analytics,primes,iterators
analytics.monitor()
from itertools import permutations, combinations_with_replacement, product

def S(n,d): #check n digit numbers for repeated digit d
    r = list(map(str,filter(lambda x: x != d,range(10))))
    psum = 0
    for k in range(n-1,0,-1): # how many d's
        if psum > 0:
            return psum
        for p in product(r,repeat = n-k):
            for a in iterators.nSetkBits(n,k):
                q = list(p)
                number = int(''.join([d if a[i] else q.pop() for i in range(n)]))
                if len(str(number)) == n and primes.millerRabin(number):
                    psum += number
    return psum

def main():
    return sum(S(10,d) for d in map(str,range(10)))

print(main(), analytics.lap(), analytics.maxMem())
# 612407567715
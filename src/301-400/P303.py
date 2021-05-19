from helpers import analytics
analytics.monitor()
from itertools import product

def f(n):
    i = 1
    while True:
        stop = True
        for d in str(n*i):
            if d not in {'0','1','2'}:
                stop = False
                break
        if stop:
            print(n,i,n*i) 
            return i
        i += 1

def main(N):
    total = 0
    k = 0
    digits = ('0','1','2')
    nums = set(range(1,N+1))
    while len(nums) > 20:
        for d in {'1','2'}:
            for c in product(digits,repeat = k):
                s = int(d + ''.join(c))
                remove = set()
                for n in nums:
                    if s%n == 0:
                        total += s//n
                        remove.add(n)
                nums.difference_update(remove)
        k += 1
    print(k,nums)
    for n in nums:
        total += f(n)
    return total
    
print(main(10**4), analytics.lap(), analytics.maxMem())
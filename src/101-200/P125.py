import repackage; repackage.up()
from helpers import analytics
analytics.monitor()

limit = int(1e8)

def palindrome(n):
    n_str = str(n)
    return n_str == n_str[::-1]

def main():
    nums = set([])
    i = 1
    while i**2 < limit:
        j = i+1
        p = i**2 + j**2
        while p < limit:
            if palindrome(p):
                nums.add(p)
            j += 1
            p += j**2
        i += 1
    return sum(nums)

print(main(), analytics.lap(), analytics.maxMem())
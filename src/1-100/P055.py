from helpers import analytics
analytics.monitor()

limit = int(1e4)

def isPalindrome(n):
    if str(n)==str(n)[::-1]:
        return True
    return False

def isLychrel(n):
    for i in range(50):
        revn = int(str(n)[::-1])
        n += revn
        if isPalindrome(n):
            return False
    return True

def main(limit):
    total = 0
    for i in range(1,limit):
        if isLychrel(i):
            total += 1
    return total

print(main(limit), analytics.lap(), analytics.maxMem())
"""
249 
time: 0.07476907499999999 
max memory: 8.8MB
"""
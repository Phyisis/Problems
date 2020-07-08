import repackage; repackage.up()
from helpers import analytics
analytics.monitor()

limit = int(1e9)

def main(limit):
    total = 0
    for n in range(1,limit):
        if n % 10 != 0 and reversible(n):
            total += 1
    return total

def reversible(n):
    s = n + int(str(n)[::-1])
    for d in str(s):
        if int(d) % 2 == 0:
            return False
    return True

print(main(limit), analytics.lap(), analytics.maxMem())
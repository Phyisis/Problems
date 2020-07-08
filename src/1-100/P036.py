import repackage; repackage.up()
from helpers import analytics
analytics.monitor()

limit = int(1e6)

def main(limit):
    total = 0
    for i in range(1,limit):
        if str(i) == str(i)[::-1] and bin(i)[2:] == bin(i)[:1:-1]:
            total += i
    return total

print(main(limit), analytics.lap(), analytics.maxMem())
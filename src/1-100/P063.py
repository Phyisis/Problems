from helpers import analytics
analytics.monitor()
import math

#int(b*log10(a)) == b
limit = int(1e2)

def main(limit):
    count = 0
    for a in range(1,limit):
        for b in range(1,limit):
            if int(b*math.log10(a))+1 == b:
                count += 1
    return count

print(main(limit), analytics.lap(), analytics.maxMem())
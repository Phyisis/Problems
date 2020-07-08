import repackage; repackage.up()
import math
from helpers import analytics
analytics.monitor()

# t total discs
# b blue discs
# find values such that t > 1e12, 0 < b < t and (b/t)*((b-1)/(t-1)) = 0.5 exactly
# (b**2-b) = (t**2-t)/2
# sqrt(2)/2 = 0.7071067811865

limit = int(1e12)

def main():
    p = 1
    t = 1
    while True: # search values of t
        t2 = (t**2-t)
        lo = 0
        hi = t
        b = lo
        while True: # search values of b
            b2 = 2*(b**2-b)
            if b2 == t2:
                if t > limit:
                    return b
                #print((b,t))
                t,p = math.ceil((t*t)/p),t
                break
            elif b2 < t2:
                lo = b
                b = (lo+hi)//2
            elif b2 > t2:
                hi = b
                b = (lo+hi)//2
            if lo + 1 == hi:
                break
        t += 1

print(main(), analytics.lap(), analytics.maxMem())
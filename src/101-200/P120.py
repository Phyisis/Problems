"""
(a+1)^n == an+1 (mod a^2)
(a-1)^n == an-1 or 1-an (mod a^2) depending whether n is odd or even; 
the sum is therefore either 2an or 2.

When a is odd, this is always maximised at a^2-a (as in the example with a=7), achieved for example when n=(a-1)/2; 
when a is even, it is maximised at a^2-2a for a>2, achieved for example when n=(a-2)/2.
"""
from helpers import analytics
analytics.monitor()

def main():
    total = 0
    for a in range(3,1001,2):
        total += a*(a-1)
    for a in range(4,1001,2):
        total += a*(a-2)
    return total

print(main(), analytics.lap(), analytics.maxMem())
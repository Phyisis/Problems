from helpers import analytics,primes, iterators
analytics.monitor()
import guppy

"""
For a positive integer k, define d(k) as the sum of the digits of k in its usual decimal representation. 
Thus d(42) = 4+2 = 6.

For a positive integer n, define S(n) as the number of positive integers k < 10^n with the following properties :
    k is divisible by 23 and
    d(k) = 23.
You are given that S(9) = 263626 and S(42) = 6377168878570056.
Find S(11^12) and give your answer mod 109.
"""

p23 = [k for k in iterators.partition(23) if max(k) < 10]
#ways to split 10^(11^12) into k=1->24 groups: comb(10^n,k)
#primes.initialize(10**8)

def main(N):
    return

print(main(9), analytics.lap(), analytics.maxMem())
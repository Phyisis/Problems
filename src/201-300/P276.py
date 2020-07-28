from helpers import analytics, primes
analytics.monitor()

"""
Consider the triangles with integer sides a, b and c with a ≤ b ≤ c.
An integer sided triangle (a,b,c) is called primitive if gcd(a,b,c)=1.
How many primitive integer sided triangles exist with a perimeter not exceeding 10 000 000?
"""

def main(n):
    T = [0] * (n+1)
    for i in range(1,n+1):
        x = i
        if (i%2 == 1): x += 3
        x = (x*x + 24) // 48
        T[i] = T[i-1] + x
    r = 0
    primes.initialize(n)
    for i in range(1,n+1):
        m = primes.mobius(i)
        if m == 0: continue
        r += m*T[n//i]
    return r

print(main(10**7), analytics.lap(), analytics.maxMem())
# 5777137137739632912 in 162 seconds
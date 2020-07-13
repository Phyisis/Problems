from helpers import analytics, primes
analytics.monitor()
from itertools import accumulate

#Find G(10^11). Give your answer modulo 998244353
limit = 10**11
mod = 998244353

def a(x): #equivalent to main, but slow
    phi = primes.totients(limit)
    return sum(phi[k]*(x//k)*(x//k+1) for k in range(1,x+1))//2 % mod

def T(n):
    return n*(n+1)//2

def main(n):
    L = int(n**0.62)
    phi = primes.totients(L)
    Phi1 = list(accumulate(phi))    # Phi1[i] = Phi(i)
    Phi2 = [0] * (n//L+1)           # Phi2[i] = Phi(n//i)
    for j in range(n//L, 0, -1):
        k = n//j
        kr = int(k**0.5)
        s = 0
        for i in range(kr, 1, -1):
            kdivi = k//i
            if kdivi > L:
                s -= Phi2[n//kdivi]
            else:
                s -= Phi1[kdivi]
            s -= (kdivi - k//(i+1)) * Phi1[i]
        s -= (k - k//2) * Phi1[1]
        if k//kr == kr:
            s += Phi1[kr]
        Phi2[j] = s + T(k)
    nr = int(n**0.5)
    result = 0
    Tnr = T(nr)
    for i in range(1, nr+1):
        ndivi = n//i
        if ndivi <= L:
            result += i * Phi1[ndivi]
        else:
            result += i * Phi2[i]
        result += (T(ndivi) - Tnr) * phi[i]
    return result % mod

print(main(limit), analytics.lap(), analytics.maxMem())
# 551614306
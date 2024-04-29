from math import gcd

def legendre1(a, p): #legendre symbol of (a/p)
    return pow(a, (p - 1) // 2, p)

def legendre(a, p): 
    return ((pow(a, (p-1) >> 1, p) + 1) % p) - 1

def jacobiSymbol(n, k): # k > 0, k%2==1
    n,t = n%k, 1
    while n != 0:
        while n % 2 == 0:
            n >>= 1
            r = k%8
            if r == 3 or r == 5:
                t = -t
        n, k = k, n
        if n % 4 == 3 and k % 4 == 3:
            t = -t
        n %= k
    if k == 1: return t
    return 0

def tonelli(n, p):
    q,s,i,z = p-1,0,1,2
    while q % 2 == 0:
        q //= 2
        s += 1
    if s == 1:
        return pow(n, (p + 1) // 4, p)
    while z < p and p - 1 != legendre(z, p):
        z += 1
    c = pow(z, q, p)
    r = pow(n, (q + 1) // 2, p)
    t = pow(n, q, p)
    m = s
    t2 = 0
    while (t - 1) % p != 0:
        t2 = (t * t) % p
        i = 1
        while i < m:
            if (t2 - 1) % p == 0:
                break
            t2 = (t2 * t2) % p
            i += 1
        b = pow(c, 1 << (m - i - 1), p)
        r = (r * b) % p
        c = (b * b) % p
        t = (t * c) % p
        m = i
    return r

def egcd(p,q):
    if p == 0:
        return (q,0,1)
    else:
        gcd,x,y = egcd(q%p,p)
        return (gcd,y-(q//p)*x,x)

def mod_inv(a, m):
    g,x,y = egcd(a,m) 
    if (g == 1): 
        return (x%m + m) % m
    return 1

def isqrt(n):
    if n == 0: return 0
    x, y = n, (n + 1) // 2
    while y < x: x, y = y, (y + n//y) // 2
    return x

def iroot(n, k=2): # assume n > 0
    u, s, k1 = n, n+1, k-1
    while u < s:
        s = u
        u = (k1 * u + n // u ** k1) // k
    return s

def ilog(x, b): # greatest integer l such that b**l <= x.
    l = 0
    while x >= b:
        x /= b
        l += 1
    return l


# modular sqrt(n) mod p
# p must be prime
def mod_sqrt(n, p):
    a = n%p
    if p%4 == 3: return pow(a, (p+1) >> 2, p)
    elif p%8 == 5:
        v = pow(a << 1, (p-5) >> 3, p)
        i = ((a*v*v << 1) % p) - 1
        return (a*v*i)%p
    elif p%8 == 1: # Shank's method
        q, e = p-1, 0
        while q&1 == 0:
            e += 1
            q >>= 1
        n = 2
        while legendre(n, p) != -1: n += 1
        w, x, y, r = pow(a, q, p), pow(a, (q+1) >> 1, p), pow(n, q, p), e
        while True:
            if w == 1: return x
            v, k = w, 0
            while v != 1 and k+1 < r:
                v = (v*v)%p
                k += 1
            if k == 0: return x
            d = pow(y, 1 << (r-k-1), p)
            x, y = (x*d)%p, (d*d)%p
            w, r = (w*y)%p, k
    else: return a # p == 2
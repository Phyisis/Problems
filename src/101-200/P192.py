from helpers import analytics
analytics.monitor()

def farey(x, N):
    xsqrt = x**0.5
    isqrt = int(xsqrt)
    if isqrt == xsqrt: return 0
    x = xsqrt-isqrt
    a,b,c,d = 0,1,1,N
    while c/d < x:
        k = (N + b)//d
        e = k * c - a
        f = k * d - b
        a,b,c,d = c,d,e,f
    if abs(a/b-x)<abs(c/d-x):
        return b
    else: 
        return d

print(farey(10**5,10**4))

def main():
    return sum(farey(n,10**12) for n in range(2,10**5+1))

#print(main(), analytics.lap(), analytics.maxMem())

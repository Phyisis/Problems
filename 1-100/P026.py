from helpers import analytics
analytics.monitor()

def getDecimalLength(a,b):
    k = 0
    u = a % b
    v = u
    while u!=v:
        u=S(u,b)
        v=S(S(v,b),b)
        k+=1
    v = a % b
    q = 0
    while u!=v:
        u = S(u,b)
        v = S(v,b)
        q += 1
    p = 0
    v = S(v,b)
    p+=1
    while u!=v:
        v = S(v,b)
        p += 1
    return (p,q)

def S(r,b):
    return (10*r) % b

def main():
    num = 0
    longest = 0
    for i in range(7,1000):
        while i % 2 == 0:
            i /= 2
        while i % 5 == 0:
            i /= 5
        if i == 1: continue
        p,q = getDecimalLength(1,i)
        if p > longest:
            #print("1/"+str(i)+":",(p,q))
            longest = p
            num = i
    return num

print(main(), analytics.lap(), analytics.maxMem())

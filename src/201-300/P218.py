from helpers import analytics
analytics.monitor()

def perfectTriplets(limit):
    count,count2 = 0,0
    c, m = 0, 2
    while c < limit:
        for n in range(m%2+1,m,2): 
            x,y,z = m**2 - n**2, 2*m*n, m**2+n**2
            a,b,c = x**2 - y**2, 2*x*y, z**2
            A = x*y*(x**2-y**2)
            if A % 84 != 0:
                count += 1
            else:
                count2 += 1
        m += 1
    return count,count2

def main():
    limit = int(1e16)
    return perfectTriplets(limit+1)

print(main(), analytics.lap(), analytics.maxMem())
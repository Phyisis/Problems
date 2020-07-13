from helpers import analytics, primes
analytics.monitor()

def main():
    p = [1,1]
    n = 2
    while True:
        pt = 0
        k,d,m = 1,1,1
        while d <= n:
            pt += m*p[n-d]
            d += k
            if d > n:
                break
            pt += m*p[n-d]
            d += k + k + 1
            k = k+1
            m = -m
        p.append(pt%1000000)
        if pt % 1000000 == 0:
            return n
        n += 1

print(main(), analytics.lap(), analytics.maxMem())
from helpers import analytics
analytics.monitor()

def main():
    n_min = 1
    n_max = 100
    total = 0
    sumsqr = 0
    sqrsum = 0
    dif = 0

    for i in range(n_min,n_max+1):
        sumsqr += i**2
        total += i
    
    sqrsum = total**2
    return sqrsum - sumsqr

print(main(), analytics.lap(), analytics.maxMem())




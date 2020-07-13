from helpers import analytics
analytics.monitor()

a = 1504170715041707
b = 4503599627370517

def main():
    total,lo,hi = a,a,a
    while lo > 1:
        n = lo + hi
        n %= b
        if n > hi:
            hi = n
        if n < lo:
            lo = n
            total += n
    return total

print(main(), analytics.lap(), analytics.maxMem())
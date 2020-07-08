from helpers import analytics
analytics.monitor()
from fractions import Fraction

def main():
    result = 1
    results = []
    for n in range(11,100):
        for d in range(50,100):
            if Fraction(n,d) in Cancel(n,d):
                result *= Fraction(n,d)
                results.append((n,d))
    print(results)
    return result

def Cancel(n,d):
    ns,ds = str(n),str(d)
    results = []
    for i in range(len(ns)):
        for j in range(len(ds)):
            if int(ns[1-i]) == int(ds[1-j]) and int(ns[1-i]) != 0 and int(ds[j]) != 0 and int(ns[i]) != int(ds[j]):
                results.append(Fraction(int(ns[i]),int(ds[j])))
    return results

print(main(), analytics.lap(), analytics.maxMem())
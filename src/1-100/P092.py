import repackage; repackage.up()
from helpers import analytics
analytics.monitor()

def getNext(n):
    return sum(int(d)**2 for d in str(n))

pool = set(range(1,int(1e7)))
term89 = set([89])
term1 = set([1])

def main():
    while pool:
        n = pool.pop()
        seen = [n]
        while True:
            if n in term89:
                for i in seen:
                    term89.add(i)
                    if i in pool:
                        pool.remove(i)
                break
            if n in term1:
                for i in seen:
                    term1.add(i)
                    if i in pool:
                        pool.remove(i)
                break
            n = getNext(n)
            seen.append(n)
    return len(term89)

print(main(), analytics.lap(), analytics.maxMem())
from Problems.helpers import analytics
analytics.monitor()

def isBouncy(n):
    n = list(map(int,str(n)))
    c = None
    for i in range(len(n)-1):
        if n[i+1] == n[i]: continue
        k = -1 if n[i+1]-n[i] < 0 else 1
        if k != c and c != None:
            return True
        c = k
    return False

def main():
    n = 1
    b = 0
    while b/n < 0.99:
        n += 1
        if isBouncy(n):
            b += 1
    return n

print(main(), analytics.lap(), analytics.maxMem())
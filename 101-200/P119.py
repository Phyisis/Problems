from Problems.helpers import analytics
analytics.monitor()

def main():
    count,d = 0,2
    a = []
    while count < 50:
        for k in range(2,15):
            n = d**k
            if n > 9 and sum(map(int,str(n)))==d:
                count += 1
                a.append(n)
        d += 1
    return sorted(a)[29]

print(main(), analytics.lap(), analytics.maxMem())
# 248155780267521
from helpers import analytics
analytics.monitor()

def main():
    n = 1
    while True:
        ns = sorted(str(n))
        for m in range(2,7):
            if sorted(str(n*m)) != ns:
                break
            if m == 6:
                return n
        n += 1

print(main(), analytics.lap(), analytics.maxMem())
"""
142857 
time: 0.246918633 
max memory: 8.8MB
"""
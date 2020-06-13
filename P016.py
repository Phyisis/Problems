from helpers import analytics
analytics.monitor()

def main():
    b = 2
    p = 1000
    return sum(int(d) for d in str(b**p))

print(main(), analytics.lap(), analytics.maxMem())







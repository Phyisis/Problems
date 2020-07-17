from helpers import analytics
analytics.monitor()

def main():
    b,p = 2,1000
    return sum(map(int,str(b**p)))

print(main(), analytics.lap(), analytics.maxMem())







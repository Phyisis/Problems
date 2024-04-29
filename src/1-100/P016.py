from helpers import analytics
analytics.monitor()

def main():
    b,p = 2,1000
    return sum(map(int,str(b**p)))

print(main(), analytics.lap(), analytics.maxMem())
"""
1366 
time: 0.0001460350000000027 
max memory: 8.8MB
"""







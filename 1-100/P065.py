from helpers import analytics
analytics.monitor()

def main(limit):    
    n0, n1 = 1, 2
    for i in range(2, limit+1): 
        n0, n1 = n1, n0 + n1 * (1 if i%3 else 2 * i//3)
    return sum(map(int,str(n1)))

print(main(100), analytics.lap(), analytics.maxMem())
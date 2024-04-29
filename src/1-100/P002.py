from helpers import analytics
analytics.monitor()

def main():
    limit = 4000000
    total = 0
    n1 = 1
    n2 = 2
    while (n2 < limit):
            if n2 % 2 == 0:
                    total += n2
            temp = n1 + n2
            n1 = n2
            n2 = temp
    return total
                
print(main(), analytics.lap(), analytics.maxMem())
"""
4613732 
time: 0.00013337100000000712 
max memory: 8.8MB
"""

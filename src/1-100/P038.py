from helpers import analytics
analytics.monitor()

limit = int(1e4)
digits = set(str(i) for i in range(1,10))

def main(limit):
    largest = 0
    for n in range(1,limit):
        r = str(n)
        m = 2
        while int(r) < int(1e9):
            if int(r) > int(1e8):
                if set(list(r)) == digits:
                    if int(r) > largest:
                        largest = int(r)
            r += str(m*n)
            m += 1
    return largest
                    
print(main(limit), analytics.lap(), analytics.maxMem())
"""
932718654 
time: 0.029425167999999995 
max memory: 8.9MB
"""
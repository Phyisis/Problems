import repackage; repackage.up()
from helpers import analytics
analytics.monitor()

def main():
    total = 0
    for i in range(1000):
            if i%3 == 0 or i%5==0:
                    total += i
    return total
                
print(main(), analytics.lap(), analytics.maxMem())
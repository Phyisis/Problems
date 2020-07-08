import repackage; repackage.up()
from helpers import analytics
analytics.monitor()

def main():
    return sum(i**i for i in range(1,1001))%int(1e10)
    
print(main(), analytics.lap(), analytics.maxMem())
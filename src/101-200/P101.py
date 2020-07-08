import repackage; repackage.up()
from helpers import analytics
analytics.monitor()
import numpy as np

seq = [sum((-x)**k for k in range(11)) for x in range(1,11)]

def main():
    total = 0
    for i in range(10):
        x,y = list(range(1,i+2)),seq[:i+1]
        fit = np.poly1d(np.polyfit(x,y,i))
        total += round(fit(i+2))
    return int(total)

print(main(), analytics.lap(), analytics.maxMem())
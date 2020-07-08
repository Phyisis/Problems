import repackage; repackage.up()
import math
from helpers import analytics
analytics.monitor()


def main():
    return sum(int(d) for d in str(math.factorial(100)))

print(main(), analytics.lap(), analytics.maxMem())








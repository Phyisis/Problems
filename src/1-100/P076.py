from helpers import analytics, iterators
analytics.monitor()

limit = 100

def main(limit):
    return iterators.partitionCount(limit) - 1

print(main(limit), analytics.lap(), analytics.maxMem())
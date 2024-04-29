from helpers import analytics, iterators
analytics.monitor()

limit = 100

def main(limit):
    return iterators.partitionCount(limit) - 1

print(main(limit), analytics.lap(), analytics.maxMem())
"""
190569291 
time: 0.0041035669999999955 
max memory: 9.2MB
"""
import repackage; repackage.up()
from helpers import analytics
analytics.monitor()
from math import log10

"""
log10((n*x-n//10)/n%10) == int(log10(n))
"""

def divRotate(n):
    print(n)
    print((n%10*10**int(log10(n))+n//10))
    return (n%10*10**int(log10(n))+n//10)%n == 0

print(divRotate(142857))

def main():
    return 

print(main(), analytics.lap(), analytics.maxMem())
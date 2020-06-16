# find last 10 digits of 28433*(2**7830457)+1
from helpers import analytics
analytics.monitor()

def main():
    return (28433*(2**7830457)+1) % int(1e10)

print(main(), analytics.lap(), analytics.maxMem())
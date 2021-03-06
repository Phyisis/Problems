from helpers import analytics
analytics.monitor()

def isDigitPowerSum(num):
    if sum([int(d)**5 for d in str(num)]) == num:
        return True
    return False

def main():
    results = []
    for i in range(10,200000):
        if isDigitPowerSum(i):
            results.append(i)
    return sum(results)

print(main(), analytics.lap(), analytics.maxMem())
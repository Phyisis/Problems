from helpers import analytics
analytics.monitor()

def main():
    results = []
    for a in range(2,101):
        for b in range(2,101):
            num = a**b
            if num not in results:
                results.append(num)
    return len(results)

print(main(), analytics.lap(), analytics.maxMem())
"""
9183 
time: 1.16509071 
max memory: 9.4MB
"""
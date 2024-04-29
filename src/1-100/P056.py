from helpers import analytics
analytics.monitor()

def main():
    largest = 0
    for a in range(1,101):
        for b in range(1,101):
            n = sum(int(d) for d in str(a**b))
            if n > largest:
                largest = n
    return largest

print(main(), analytics.lap(), analytics.maxMem())
"""
972 
time: 0.27028901299999997 
max memory: 8.8MB
"""
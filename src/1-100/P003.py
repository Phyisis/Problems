from helpers import analytics
analytics.monitor()

def main(n):
    pf = set([])
    while n%2==0:
        pf.add(2)
        n //= 2
    for i in range(3,int(n**(.5)),2):
        while n % i == 0:
            pf.add(i)
            n //= i
    if n > 1:
        pf.add(n)
    return sorted(list(pf))

num = 600851475143
print(main(num), analytics.lap(), analytics.maxMem())
"""
[71, 839, 1471, 6857] 
time: 0.018820619999999996 
max memory: 8.8MB
"""

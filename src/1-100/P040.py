from helpers import analytics
analytics.monitor()
from math import prod

def main():
    s = "".join(str(i) for i in range(int(1e6)))
    return prod([int(s[int(x)]) for x in [1e0, 1e2, 1e3, 1e4, 1e5, 1e6]])

print(main(), analytics.lap(), analytics.maxMem())
"""
210 
time: 0.353004087 
max memory: 18.3MB
"""
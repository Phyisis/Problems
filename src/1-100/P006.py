from helpers import analytics
analytics.monitor()

def main(N):
    sumsqr = (N * (N + 1) * (2*N + 1)) // 6
    sqrsum = (N*(N+1)//2)**2
    return sqrsum - sumsqr

print(main(100), analytics.lap(), analytics.maxMem())
"""
25164150 
time: 9.246000000000254e-05 
max memory: 8.8MB
"""



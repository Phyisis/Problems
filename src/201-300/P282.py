from helpers import analytics,primes
analytics.monitor()

"""
0,0: 1
1,1: 2+4 - 3 = 3
2,2: 2*5 - 3 = 7
3,3: 2^6 - 3 = 61
4,4: 2^^7 - 3
    2^^7 % 14^8 == 2^2^2^65536 / 2^(2^3) % 7^8
5,5: 2^^^8 - 3
6,6: 2^^^^9 - 3
"""

mod = 14**8

def A(m,n):
    if m == 0: return n+1
    if n == 0: return A(m-1,1)
    return A(m-1,A(m,n-1))

def main():
    for i in range(7):
        print(A(i,i))

print(main(), analytics.lap(), analytics.maxMem())
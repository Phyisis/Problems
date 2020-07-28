from helpers import analytics,primes
analytics.monitor()

mod = 14**8

def A(m,n):
    if m == 0: return n+1
    if n == 0: return A(m-1,1)
    return A(m-1,A(m,n-1))

def main():
    for i in range(7):
        print(A(i,i))

print(main(), analytics.lap(), analytics.maxMem())
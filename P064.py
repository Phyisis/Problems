from helpers import analytics
analytics.monitor()

limit = int(1e4)

def contFracCount(n):
    r = int(n**0.5)
    f = r
    if r**2 == n: return 0
    k, period = 1, 0
    while k != 1 or period == 0:
        k = (n - r * r) // k
        r = (f + r) // k * k - r
        period += 1
    return period

def main():
    count = 0
    for n in range(2,limit+1):
        if contFracCount(n)%2 == 1: #repeated part is odd
            count += 1
    return count

print(main(), analytics.lap(), analytics.maxMem())


"""
def contFrac(n):
    sqrt = n**0.5
    if sqrt == int(sqrt):
        return 0
    f = 2*int(sqrt)
    X = [sqrt]
    A = [int(sqrt)]
    while f != A[-1]:
        #x_n+1 = 1/(x_n-a_n)
        X.append(1/(X[-1]-A[-1]))
        A.append(int(X[-1]))
    return 
"""
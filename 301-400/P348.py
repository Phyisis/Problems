from Problems.helpers import analytics,primes
analytics.monitor()

def isPalindrome(n):
    n_str = str(n)
    return n_str==n_str[::-1]

def main():
    P = {}
    for i in range(30000):
        for j in range(1000):
            n = i**2 + j**3
            if isPalindrome(n):
                if n in P:
                    P[n] += 1
                else:
                    P[n] = 1
    s = []
    keys = sorted(P.keys())
    for k in keys:
        if P[k] == 4:
            s.append(k)
    return len(s),sum(s[:5])

print(main(), analytics.lap(), analytics.maxMem())
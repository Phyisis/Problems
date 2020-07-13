from helpers import analytics,primes
analytics.monitor()

primes.initialize(10**8)

def pascal(A=[1]):
    return [1] + [A[i] + A[i+1] for i in range(len(A)-1)] + [1]

def squareFree(n):
    return all(map(lambda x: x[1] == 1,primes.factorization(n)))

def main():
    total = 1
    seen = {1}
    A = [1]
    for _ in range(51):
        for i in range(1,len(A)//2+1):
            n = A[i]
            if n not in seen and squareFree(n):
                total += n
                seen.add(n)
        seen.update(A)
        A = pascal(A)
    return total

print(main(), analytics.lap(), analytics.maxMem())
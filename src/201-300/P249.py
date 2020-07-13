from helpers import analytics,primes
analytics.monitor()

limit = 5000 #5000
primesList = primes.primes(limit)
maxSum = sum(primesList)
primesHash = set(primes.primes(maxSum))

def total_subsets_matching_sum(numbers, t):
    array = [1] + [0] * t
    for current_number in numbers:
        for num in range(t - current_number, -1, -1):
            if array[num]:
                array[num + current_number] += array[num]
    return array

def main():
    total = 0
    A = total_subsets_matching_sum(primesList,maxSum)
    for i in range(len(A)):
        if i in primesHash:
            total += A[i]
    return total % int(1e16)

print(main(), analytics.lap(), analytics.maxMem())
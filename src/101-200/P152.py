import repackage; repackage.up()
from helpers import analytics,primes
analytics.monitor()
from fractions import Fraction

"""
for sum of inverse squares to equal 1/2,
sum(1/k**2 for k in s) = 1/2
"""

limit = 35
invSqrs = [Fraction(1,i**2) for i in range(2,limit+1)]

def total_subsets_matching_sum(numbers, t):
    A = {0:1, t:0}
    maxSum = sum(numbers)
    for current_number in numbers:
        print(current_number, len(A), A[t])
        B = {}
        for num in A:
            if num < t-current_number and num + maxSum >= t:
                if num + current_number in B:
                    B[num + current_number] += A[num]
                else:
                    B[num + current_number] = 1
        for n in B:
            if n in A:
                A[n] += B[n]
            else:
                A[n] = B[n]
        maxSum -= current_number
        keys = list(A.keys())
        for n in keys:
            if n+maxSum < t:
                del A[n]
    return A

def displaySubsetsThatSumTo(target, numbers):
    wheel = [0]
    resultsCount = 0
    s = 0
    while True:
        s = incrementWheel(0, s, numbers, wheel)
        if s == None:
            break
        if s == target:
            resultsCount += 1
    return resultsCount

def incrementWheel(position, s, numbers, wheel):
    if (position == len(numbers) or s == None):
        return None
    wheel[position] += 1
    if (wheel[position] == 2):
        wheel[position] = 0
        s -= numbers[position]
        if (len(wheel) < position + 2):
            wheel.append(0)
        s = incrementWheel(position + 1, s, numbers, wheel)
    else:
        s += numbers[position]
    return s

def main():
    return displaySubsetsThatSumTo(sum(invSqrs)-Fraction(1,2),invSqrs)

print(main(), analytics.lap(), analytics.maxMem())
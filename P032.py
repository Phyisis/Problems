from itertools import combinations,permutations

def isPandigital(a,b,c):
    if sorted(str(a)+str(b)+str(c))==sorted("123456789"):
        return True
    return False

digits = [1,2,3,4,5,6,7,8,9]
fourDigits = [int(''.join(map(str, s))) for s in permutations(digits,4)]
fiveDigits = [int(''.join(map(str, s))) for s in permutations(digits,5)]
numbers = fourDigits + fiveDigits

results = []

for a in numbers:
    for b in range(1,1000):
        if a % b == 0 and isPandigital(a,b,a//b) and a not in results:
            results.append(a)


print(results)
print(sum(results))
import math

def main():
    total = 0
    for i in range(3, int(5e4)):
        if sum([math.factorial(int(n)) for n in str(i)]) == i:
            total += i
    return total

print(main())
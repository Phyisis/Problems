from math import sqrt; from itertools import count, islice, permutations

def is_prime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

def main():
    for n in reversed(range(1,10)):
        for x in reversed(list(permutations(range(1,n+1)))):
            xs = int("".join([str(a) for a in x]))
            if is_prime(xs):
                return xs

print(main())

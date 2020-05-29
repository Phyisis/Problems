import primes

def main(target):
    i = 1
    run = 0
    first = 1
    while True:
        i += 1
        pf = len(primes.factorization(i))
        if pf == target:
            run += 1
            if run == 1:
                first = i
            if run == target:
                return first
        else:
            run = 0

print(main(4))

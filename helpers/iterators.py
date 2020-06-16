from itertools import combinations

def nSetkBits(n, k):
    for bits in combinations(range(n), k):
        s = [False] * n
        for bit in bits:
            s[bit] = True
        yield s
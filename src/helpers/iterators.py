from itertools import combinations

def nSetkBits(n, k):
    for bits in combinations(range(n), k):
        s = [False] * n
        for bit in bits:
            s[bit] = True
        yield s

def set_partitions(iterable, k=None):
    L = list(iterable)
    def set_partitions_helper(L, k):
        if k == 1:
            yield [L]
        elif len(L) == k:
            yield [[s] for s in L]
        else:
            e, *M = L
            for p in set_partitions_helper(M, k - 1):
                yield [[e], *p]
            for p in set_partitions_helper(M, k):
                for i in range(len(p)):
                    yield p[:i] + [[e] + p[i]] + p[i + 1 :]
    if k is None:
        for k in range(1, len(L) + 1):
            yield from set_partitions_helper(L, k)
    else:
        yield from set_partitions_helper(L, k)
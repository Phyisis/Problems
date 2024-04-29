from itertools import combinations
from functools import lru_cache

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

@lru_cache
def partition(number):
    answer = set()
    answer.add((number, ))
    for x in range(1, number):
        for y in partition(number - x):
            answer.add(tuple(sorted((x, ) + y)))
    return answer

def partitionCount(n):
    ways = [1] + [0] * n
    nums = [c for c in range(1,n)]
    for num in nums:
        for i in range(num,n+1):
            ways[i] += ways[i-num]
    return ways[n] + 1

def farey(N): # all coprime pairs a,b with a < b <= N
    a,b,c,d = 1,N,1,N-1
    yield a,b
    while not (c == 1 and d == 1):
        yield c,d
        k = (N + b)//d
        a, b, c, d = c, d, k*c-a, k*d-b
    return
"""
Triangle	 	P3,n=n(n+1)/2	 	1, 3, 6, 10, 15, ...
Square	 	    P4,n=n**2	 	    1, 4, 9, 16, 25, ...
Pentagonal	 	P5,n=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
Hexagonal	 	P6,n=n(2n−1)	 	1, 6, 15, 28, 45, ...
Heptagonal	 	P7,n=n(5n−3)/2	 	1, 7, 18, 34, 55, ...
Octagonal	 	P8,n=n(3n−2)	    1, 8, 21, 40, 65, ...
"""
from math import comb
from itertools import permutations
from helpers import analytics
analytics.monitor()

def P(r,n):
    return (r-2)*(n*(n-1)//2)+n

def genNumbers():
    A = []
    for r in range(3,9):
        nums = []
        n = 1
        t = P(r,n)
        while t < int(1e3):
            n += 1
            t = P(r,n)
        while t < int(1e4):
            nums.append((t//100,t%100))
            n += 1
            t = P(r,n)
        A.append(nums)
    return list(reversed(A))

def main():
    N = genNumbers()
    for A in permutations(N):
        for s0 in A[0]:
            for s1 in A[1]:
                if s0[1] == s1[0]:
                    for s2 in A[2]:
                        if s1[1] == s2[0]:
                            for s3 in A[3]:
                                if s2[1] == s3[0]:
                                    for s4 in A[4]:
                                        if s3[1] == s4[0]:
                                            for s5 in A[5]:
                                                if s4[1] == s5[0] and s5[1] == s0[0]:
                                                    r = (s0,s1,s2,s3,s4,s5)
                                                    return r, sum(100*x[0]+x[1] for x in r) 




print(main(), analytics.lap(), analytics.maxMem())

"""
1287 (8)

"""
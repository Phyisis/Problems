"""
43 44 45 46 47 48 49
42 21 22 23 24 25 26
41 20  7  8  9 10 27
40 19  6  1  2 11 28
39 18  5  4  3 12 29
38 17 16 15 14 13 30
37 36 35 34 33 32 31
"""

def box(n):
    return 4*(4*n**2+n+1)

def sumOfDiagonals(n):
    total = 1
    for i in range(1,n+1):
        total += box(i)
    return total

print(sumOfDiagonals(500))
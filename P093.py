# ugly, reports incorrect length of maximum sequence, but still gives right answer

from helpers import analytics
analytics.monitor()
from fractions import Fraction
from itertools import combinations

def op2(s):
    a,b = s
    r = set([a+b,a*b,a-b,b-a])
    if a != 0:
        r.add(Fraction(b,a))
    if b != 0:
        r.add(Fraction(a,b))
    return r

def main():
    s = None
    n_max = 0
    for a in range(1,7):
        for b in range(2,8):
            for c in range(3,9):
                for d in range(4,10):
                    currentDigits = [a,b,c,d]
                    obtainable = set([])
                    for c0 in combinations(currentDigits,2):
                        c0 = list(c0)
                        nums0 = op2(c0)
                        rem0 = [i for i in currentDigits if not i in c0 or c0.remove(i)]
                        for n0 in nums0:
                            for c1 in combinations(rem0+[n0],2):
                                c1 = list(c1)
                                nums1 = op2(c1)
                                rem1 = [i for i in rem0+[n0] if not i in c1 or c1.remove(i)]
                                for n1 in nums1:
                                    obtainable.update(op2(rem1+[n1]))
                    obtainable = sorted(list(filter(lambda x: x == int(x) and x>0,obtainable)))
                    for o in range(1,len(obtainable)):
                        if obtainable[o] != obtainable[o-1] + 1:
                            if obtainable[o-1] > n_max:
                                n_max = obtainable[o-1]
                                s = str(a) + str(b) + str(c) + str(d)
                            break
    return s, n_max

print(main(), analytics.lap(), analytics.maxMem())
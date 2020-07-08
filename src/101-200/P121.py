import repackage; repackage.up()
from helpers import analytics, iterators
analytics.monitor()
from fractions import Fraction
from math import prod

def main(turns):
    r,b = 0,1
    turn = []
    for _ in range(turns):
        r += 1
        turn.append(Fraction(b,r+b))
    prob = 0
    for bits in range(turns//2+1,turns+1):
        for A in iterators.nSetkBits(turns,bits):
            p = 1
            for t in range(len(A)):
                if A[t]:
                    p *= turn[t]
                else:
                    p*= 1-turn[t]
            prob += p
    return prob, int(prob.denominator/prob.numerator)

print(main(15), analytics.lap(), analytics.maxMem())
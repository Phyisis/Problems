from helpers import analytics
analytics.monitor()
import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "bin", "p054_poker.txt")
handsFile = open(filename, "rb")

T=(([1],[3,1.5]),([3,1.7],[5]))
def rank(H, v=dict(zip(b'23456789TJQKA', range(13)))):
    C,V,S = zip(*reversed(sorted([(H.count(c), v[c], s) for c, s in H.split()])))
    return ([C[0], C[C[0]]] if C[0]>1 else T[len(set(S))==1][V[0]-V[4]==4]), V

def main():
    return sum([rank(s[:14]) > rank(s[15:]) for s in handsFile])

print(main(), analytics.lap(), analytics.maxMem())
from helpers import analytics
analytics.monitor()
import os, itertools

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "bin", "p098_words.txt")
wordsFile = open(filename, "r")

def getWords():
    words = []
    for line in wordsFile:
        words += [word.strip('"') for word in line.split(",") if len(word)>6]
    return words

def getWordDict():
    anagram = {}
    words = getWords()
    for word in words:
        key = ''.join(sorted(list(word)))
        if key not in anagram:
            anagram[key] = [word]
        else:
            anagram[key].append(word)
    delete = [key for key in anagram if len(anagram[key])==1]
    for key in delete:
        del anagram[key]
    return anagram

def applyMap(n,p,m):
    x = int(''.join(p[m[i]] for i in n))
    if int(x**0.5)**2 == x:
        return x
    return False

def main():
    anagram = getWordDict()
    max_sq = 0
    for a,b in anagram.values():
        m = {n:l for l,n in enumerate(set(a))}
        for p in itertools.permutations('123456789', len(m)):
            a_sq, b_sq = applyMap(a,p,m), applyMap(b,p,m)
            if a_sq and b_sq:
                max_sq = max(a_sq, b_sq, max_sq)
    return max_sq

print(main(), analytics.lap(), analytics.maxMem())
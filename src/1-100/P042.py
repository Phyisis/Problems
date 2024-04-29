from helpers import analytics
analytics.monitor()
import os, string

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "bin", "p042_words.txt")
wordsFile = open(filename, "r")

words = []
for line in wordsFile:
    words += [word.strip('"') for word in line.split(",")]

tNums = set([int(n*(n+1)/2) for n in range(100)])

def getScore(word):
    score = 0 
    for letter in word:
        score += string.ascii_uppercase.index(letter)+1
    return score

def main():
    total = 0
    for word in words:
        if getScore(word) in tNums:
            total += 1
    return total

print(main(), analytics.lap(), analytics.maxMem())
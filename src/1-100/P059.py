import repackage; repackage.up()
from helpers import analytics
analytics.monitor()
import os
from string import ascii_lowercase

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "bin", "englishtop1000.txt")
wordsFile = open(filename, "r")
words = []

for line in wordsFile:
    if len(words) > 99:
        break
    words += [line.strip()]

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "bin", "p059_cipher.txt")
cipherFile = open(filename, "r")

message = []

for line in cipherFile:
    message += [int(b) for b in line.split(",")]

def read(m):
    return ''.join(map(chr,m))

def XOR(m,c):
    return [ord(c[i%len(c)])^m[i] for i in range(len(m))]

def main():
    best = None
    topCount = 0
    for i in ascii_lowercase:
        for j in ascii_lowercase:
            for k in ascii_lowercase:
                c = i+j+k
                count = 0
                tm = read(XOR(message,c))
                for word in words:
                    if tm.find(word) > 0:
                        count += 1
                if count > topCount:
                    topCount = count
                    best = c
    return sum(XOR(message, best))

print(main(), analytics.lap(), analytics.maxMem())
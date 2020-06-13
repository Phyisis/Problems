from helpers import analytics
analytics.monitor()
from random import randint,shuffle

limit = int(1e7)
games = 1
lastChance = 0
chanceStack = list(range(16))
lastCC = 0
ccStack = list(range(16))

def resetDecks():    
    shuffle(chanceStack)
    shuffle(ccStack)

def chance(pos):
    global lastChance, chanceStack
    card = chanceStack[lastChance]
    lastChance = (lastChance + 1) % 16
    if card > 9:
        return pos
    if card == 0:
        return 0
    if card == 1:
        return 10
    if card == 2:
        return 11
    if card == 3:
        return 24
    if card == 4:
        return 39
    if card == 5:
        return 5
    if card == 6:
        card = 7
    if card == 7:
        if pos < 5 or pos > 35:
            return 5
        if pos < 15 and pos > 5:
            return 15
        if pos < 25 and pos > 15:
            return 25
        if pos < 35 and pos > 25:
            return 35
    if card == 8:
        if pos < 12 or pos > 28:
            return 12
        if pos < 28 and pos > 12:
            return 28
    if card == 9:
        return (pos - 3)%40
    return pos

def CC(pos):  
    global lastCC, ccStack 
    card = ccStack[lastCC]
    lastCC = (lastCC + 1) % 16
    if card == 0:
        return 0
    if card == 1:
        return 10
    return pos

def roll(d):
    return (randint(1,d),randint(1,d))

def main():
    squares = [0] * 40
    for g in range(games):
        resetDecks()
        pos = 0
        doubles = 0
        for _ in range(limit):
            r = roll(4)
            if r[0] == r[1]:
                doubles += 1
            else:
                doubles = 0
            if doubles == 3:
                pos = 10
                doubles = 0
            pos = (pos + sum(r)) % 40
            if pos == 30:
                pos = 10
            if pos == 7 or pos == 22 or pos == 36:
                pos = chance(pos)
            if pos == 2 or pos == 17 or pos == 33:
                pos = CC(pos)
            squares[pos] += 1
    return sorted([(b,squares[b]/(limit*games)) for b in range(len(squares))], key=lambda x: x[1]) #largest(squares)

def largest(A):
    n = (0,0,0)
    k = (0,0,0)
    for i in range(len(A)):
        if A[i] >= k[0]:
            n = (i,n[0],n[1])
            k = (A[i],k[0],k[1])
    return n, [b/(limit*games) for b in k]
    
print(main(), analytics.lap(), analytics.maxMem())
from helpers import analytics
analytics.monitor()

n = 1
min = 1901
max = 2000
NLY = 365
LY = 366
firstsNLY = [1,32,60,91,121,152,182,213,244,274,305,335]
firstsLY = [1,32,61,92,122,153,183,214,245,275,306,336]
sundays = 0

def IsLY(yr):
    if (yr % 400 == 0): return True
    if (yr % 100 == 0): return False
    if (yr % 4 == 0): return True
    return False

for y in range(min,max+1):
    if IsLY(y):
        for d in range(1,LY+2):
            if ((n == 0) and (d in firstsLY)):
                sundays += 1
            n = (n + 1) % 7
    if not IsLY(y):
        for d in range(1,NLY+2):
            if ((n == 0) and (d in firstsNLY)):
                sundays += 1
            n = (n + 1) % 7

print(sundays, analytics.lap(), analytics.maxMem())
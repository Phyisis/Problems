import repackage; repackage.up()
from helpers import analytics
analytics.monitor()

def f(x):
    return {
        '0' : 0,
        '1' : len('one'),
        '2' : len('two'),
        '3' : len('three'),
        '4' : len('four'),
        '5' : len('five'),
        '6' : len('six'),
        '7' : len('seven'),
        '8' : len('eight'),
        '9' : len('nine'),
        '10' : len('ten'),
        '11' : len('eleven'),
        '12' : len('twelve'),
        '13' : len('thirteen'),
        '14' : len('fourteen'),
        '15' : len('fifteen'),
        '16' : len('sixteen'),
        '17' : len('seventeen'),
        '18' : len('eighteen'),
        '19' : len('nineteen'),
        '20' : len('twenty'),
        '30' : len('thirty'),
        '40' : len('forty'),
        '50' : len('fifty'),
        '60' : len('sixty'),
        '70' : len('seventy'),
        '80' : len('eighty'),
        '90' : len('ninety'),
    }[x]

def GetLetters(num):
    letters = 0
    if (num >= 1000):
        letters += len('onethousand')
    if (num >= 100 and num < 1000):
        letters += f(str(num//100))
        letters += len('hundred')
    if (num >= 100 and num % 100 != 0 and num < 1000):
        letters += len('and')
    if (num % 100 > 10 and num % 100 < 20):
        letters += f(str(num % 100))
    else:
        letters += f(str((num % 100) - (num % 10)))
        letters += f(str(num % 10))
    return letters
    
def main(limit):
    total = 0
    for i in range(1,limit+1):
        total += GetLetters(i)
    return total

print(main(1000), analytics.lap(), analytics.maxMem())





import repackage; repackage.up()
from helpers import analytics
analytics.monitor()
import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "bin", "p089_roman.txt")
numFile = open(filename, "r")
numerals = [line.strip() for line in numFile]

rom_val = {
    'I':1,
    'V':5,
    'X':10,
    'L':50,
    'C':100,
    'D':500,
    'M':1000
}

def toModern(s):
    int_val = 0
    for i in range(len(s)):
        if i > 0 and rom_val[s[i]] > rom_val[s[i-1]]:
            int_val += rom_val[s[i]] - 2 * rom_val[s[i-1]]
        else:
            int_val += rom_val[s[i]]
    return int_val

def toRoman(int_val):
    ints = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
    nums = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
    result = []
    for i in range(len(ints)):
        count = int(int_val / ints[i])
        result.append(nums[i] * count)
        int_val -= ints[i] * count
    return ''.join(result)

def charSaved(rn):
    return len(rn) - len(toRoman(toModern(rn)))

def main():
    total = 0
    for rn in numerals:
        total += charSaved(rn)
    return total

print(main(), analytics.lap(), analytics.maxMem())
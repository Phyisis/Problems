from itertools import permutations
from helpers import analytics
analytics.monitor()

def main():
    digits = "0123456789"
    perms = ["".join(s) for s in permutations(digits)]
    perms.sort()
    return perms[999999]

print(main(), analytics.lap(), analytics.maxMem())
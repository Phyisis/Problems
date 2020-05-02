from itertools import permutations

digits = "0123456789"

perms = ["".join(s) for s in permutations(digits)]

perms.sort()
print(perms[0])
print(perms[999999])
import math
baseExpPairsFile = open("p099_base_exp.txt", "r")

pairs = [[int(n) for n in line.split(",")] for line in baseExpPairsFile]
largest = 0
line = 0

for i in range(len(pairs)):
    a,b = pairs[i]
    if b*math.log(a) > largest:
        largest = b*math.log(a)
        line = i+1

print(largest)
print(line)
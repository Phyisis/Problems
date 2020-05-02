def isDigitPowerSum(num):
    if sum([int(d)**5 for d in str(num)]) == num:
        return True
    return False

results = []

for i in range(10,200000):
    if isDigitPowerSum(i):
        results.append(i)

print(results)
print("sum:",sum(results))
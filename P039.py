def pythagoreanTriplets(limit):
    triplets = {}
    c, m = 0, 2
    while c < limit: 
        for n in range(1, m): 
            a = m**2 - n**2 
            b = 2 * m * n 
            c = m**2 + n**2 
            p = a+b+c
            i = 1
            while i*p < limit + 1:
                triplets[(i*a,i*b,i*c)]=i*p
                i += 1
        m += 1
    return triplets

triplets = pythagoreanTriplets(int(1e3))
solution = [0,0]
for i in range(1,1001):
    num = 0
    for p in triplets.values():
        if i==p:
            num += 1
    if num > solution[1]:
        solution[1] = num
        solution[0] = i
print(solution)


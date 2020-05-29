import math

def rectCount(a,b):
    return math.comb(a+1,2)*math.comb(b+1,2)

target = int(2e6)
closest = {"area":0, "distance":float("inf"), "point":(0,0)}
for a in range(2000):
    for b in range(2000):
        d = rectCount(a,b)
        if abs(d-target) < closest["distance"]:
            closest["area"] = a*b
            closest["distance"] = abs(d-target) 
            closest["point"] = (a,b)

print(closest)
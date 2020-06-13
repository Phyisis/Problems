from helpers import analytics
analytics.monitor()

def GetTriple(u,v):
    a = u**2 - v**2
    b = 2*u*v
    c = u**2 + v**2
    return [a,b,c]

def main(n):
    rootn = int(n**0.5)
    for i in range(1,rootn):
        for j in range(1,rootn):
            trip = GetTriple(i,j)
            if ((trip[0] + trip[1] + trip[2]) == 1000):
                print(trip[0])
                print(trip[1])
                print(trip[2])
                print(trip[0] * trip[1] * trip[2])

print(main(1000), analytics.lap(), analytics.maxMem())







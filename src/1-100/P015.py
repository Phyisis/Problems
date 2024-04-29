from helpers import analytics
analytics.monitor()

w, h = 20, 20
paths = 0

grid = [[0 for x in range(w+1)] for y in range(h+1)]

def GetPaths(x,y):
    if (grid[x][y] != 0): return grid[x][y]
    if (x == 1):
        grid[x][y] = (y + 1)
        return (y + 1)
    if (y == 1):
        grid[x][y] = (x + 1)
        return (x + 1)
    a = GetPaths(x-1,y)
    b = GetPaths(x,y-1)
    grid[x][y] = a + b
    return a + b

print(GetPaths(w,h), analytics.lap(), analytics.maxMem())
"""
137846528820 
time: 0.0003527029999999959 
max memory: 8.8MB
"""
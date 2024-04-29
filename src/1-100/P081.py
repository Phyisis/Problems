from helpers import analytics
analytics.monitor()
import os
from itertools import product

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "bin", "p081_matrix.txt")
matrixFile = open(filename, "r")
matrix = [[int(name) for name in line.split(",")] for line in matrixFile]
width,height = len(matrix[0]),len(matrix)

def getAdjacent(pos):
    i,j = pos
    adj = []
    if i+1 < width:
        adj.append((i+1,j))
    if j+1 < height:
        adj.append((i,j+1))
    return adj

def getBack(pos):
    i,j = pos
    adj = []
    if i-1 >= 0:
        adj.append((i-1,j))
    if j-1 >= 0:
        adj.append((i,j-1))
    return adj

def tileCost(tile):
    return matrix[tile[1]][tile[0]]

def floodFill(start,end):
    clu = {}
    for i,j in product(range(width),range(height)):
        clu[(i,j)] = float('inf')
    clu[start] = tileCost(start)
    frontier = set(getAdjacent(start))
    while clu[end] == float('inf'):
        newFrontier = set([])
        for tile in frontier:
            m = float('inf')
            t = None
            for k in getBack(tile):
                if clu[k] < m:
                    m = clu[k]
                    t = k
            clu[tile] = tileCost(tile) + clu[t]
        for tile in frontier:
            for k in getAdjacent(tile):
                if clu[k] == float('inf') and k not in newFrontier:
                    newFrontier.add(k)
        frontier = newFrontier
    return clu[end]
    
def main():
    return floodFill((0,0),(width-1,height-1))

print(main(), analytics.lap(), analytics.maxMem())
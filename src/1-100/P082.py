import repackage; repackage.up()
from helpers import analytics
analytics.monitor()
import os
from itertools import product

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "bin", "p081_matrix.txt")
matrixFile = open(filename, "r")
matrix = [[int(name) for name in line.split(",")] for line in matrixFile]
width,height = len(matrix[0]),len(matrix)
    
def main():
    cost = [matrix[i][-1] for i in range(height)]
    for i in range(width-2, -1, -1):
        cost[0] += matrix[0][i]
        for j in range(1, height):
            cost[j] = min(cost[j], cost[j-1]) + matrix[j][i]
        for j in range(width-2, -1, -1):
            cost[j] = min(cost[j], cost[j+1] + matrix[j][i])
    return min(cost)

print(main(), analytics.lap(), analytics.maxMem())
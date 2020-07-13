from helpers import analytics
analytics.monitor()
import networkx, os
graph = networkx.DiGraph()

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "bin", "p081_matrix.txt")
matrixFile = open(filename, "r")
matrix = [[int(name) for name in line.split(",")] for line in matrixFile]
width,height = len(matrix[0]),len(matrix)
directions = ((-1,0), (0,-1), (1,0), (0,1))

def main():
    for i in range(height):
        for j in range(width):
            neighbors = [(i+x, j+y) for x, y in directions if 0 <= i+x < height and 0 <= j+y < width]
            for ni, nj in neighbors:
                graph.add_edge((i, j), (ni, nj), weight = matrix[ni][nj])
    path_length = networkx.dijkstra_path_length(graph, source=(0,0), target=(height-1,width-1))
    return path_length + matrix[0][0]

print(main(), analytics.lap(), analytics.maxMem())
"""This module will build a graph of the cost matrix follwoing PD rules"""
# build the graph
def build_graph(matrix):
    graph = {}
    rows = len(matrix)
    cols = len(matrix[0])
    
    for i in range(rows):
        for j in range(cols):
            node = (i, j)
            neighbors = []
            if matrix[i][j] == 0:
                for x, y in [(i-1, j), (i, j+1), (i+1, j), (i, j-1)]:
                    if 0 <= x < rows and 0 <= y < cols and matrix[x][y] != 0:
                        neighbors.append((x, y))
            elif matrix[i][j] != 0:
                for x, y in [(i-1, j), (i, j+1), (i+1, j), (i, j-1)]:
                    if 0 <= x < rows and 0 <= y < cols:
                        neighbors.append((x, y))

            if neighbors:  # Only add nodes with neighbors
                graph[node] = neighbors
                
    return graph

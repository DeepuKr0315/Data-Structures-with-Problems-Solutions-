"""Time Complexity:

Breadth-first search (BFS) has a time complexity of O(V^2) when it is implemented with an 
adjacency matrix, where V is the number of vertices (or nodes) in the graph. This is because 
we need to traverse the entire row for each vertex to check for its neighbours in the adjacency
matrix. As there are V vertices and each row has V elements, this results in O(V^2) time complexity.

Space Complexity:

The space complexity is O(V) because in the worst-case scenario, all the vertices/nodes might end
up in the queue at the same time.
"""

vertices = ['A', 'B', 'C', 'D', 'E', 'F']
vertex_indices = { 'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5 }
 
# The adjacency matrix
adjacency_matrix = [
    [0, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 1],
    [0, 1, 0, 1, 1, 0],
    [0, 0, 1, 0, 1, 0],
    [0, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 1, 0]
]
def travelBFS(graph, start):
    queue = [start]
    output = []
    visited = {}
    visited[start] = True
    while len(queue) > 0:
        current = queue.pop()
        output.append(current)
        current_idx = vertex_indices[current]
        neighbours = graph(current_idx)
        for i in range(len(neighbours)):
            if neighbours[i] == 1 and vertices[i] not in visited:
                queue.append(vertices[i])
                visited[vertices[i]] = True
    return output

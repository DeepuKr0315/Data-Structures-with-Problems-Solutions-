adjacency_list = {
    'A': ['B', 'F'],
    'B': ['A', 'C'],
    'C': ['B', 'E', 'D'],
    'D': ['C', 'E'],
    'E': ['D', 'C', 'F'],
    'F': ['A', 'E']
}

def traverseRecursiveDFS(graph, vertex, output, visited):
    output.append(vertex)
    visited[vertex] = True
    neighbours = graph[vertex]
    for neighbour in neighbours:
        if neighbour not in visited:
            traverseRecursiveDFS(graph, neighbour, output, visited)
    return output
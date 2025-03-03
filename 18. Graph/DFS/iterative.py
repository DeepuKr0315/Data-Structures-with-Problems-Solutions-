adjacency_list = {
    'A': ['B', 'F'],
    'B': ['A', 'C'],
    'C': ['B', 'E', 'D'],
    'D': ['C', 'E'],
    'E': ['D', 'C', 'F'],
    'F': ['A', 'E']
}

def traverseIterativeDFS(graph, start):
    output = []
    visited = {}
    stack = [start]
    visited[start] = True
    while stack:
        current = stack.pop()
        output.append(current)
        neighbours = graph(current)
        for neighbour in neighbours:
            if neighbour not in visited:
                stack.append(neighbour)
                visited[neighbour] = True
    return output
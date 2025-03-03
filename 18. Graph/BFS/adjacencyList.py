def traversalBFS(graph, start):
    visited = {}
    queue = [start]
    output = []
    visited[start] = True
    while len(queue):
        current = queue.pop()
        output.append(current)
        neighbours = graph[current]
        for neighbour in neighbours:
            if neighbour not in visited:
                queue.append(neighbour)
                visited[neighbour] = True
    return output
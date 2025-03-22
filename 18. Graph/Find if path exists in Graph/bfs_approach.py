# problem link =  https://leetcode.com/problems/find-if-path-exists-in-graph/description/
# 1971. Find if Path Exists in Graph


from collections import deque

def validPath(n, edges, source, destination):
    graph = {i : [] for i in range(n)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    queue = deque([source])
    visited = set([source])
    while queue:
        node = queue.popleft()
        if node == destination:
            return True    
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return False

print(validPath(n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2))
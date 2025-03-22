# problem link =  https://leetcode.com/problems/find-if-path-exists-in-graph/description/
# 1971. Find if Path Exists in Graph

from collections import deque

def validPath(n, edges, source, destination):
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    stack = deque([source])
    visited = set()
    while stack:
        current = stack.pop()
        if current == destination:
            return True
        if current not in visited:
            visited.add(current)
            for neighbor in graph[current]:
                stack.append(neighbor)
    return False

print(validPath(n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2))
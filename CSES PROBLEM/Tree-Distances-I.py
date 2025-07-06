# Problem link = https://cses.fi/problemset/task/1132

"""
You are given a tree consisting of n nodes.
Your task is to determine for each node the maximum distance to another node.
Input
The first input line contains an integer n: the number of nodes. The nodes are numbered 1,2,\ldots,n.
Then there are n-1 lines describing the edges. Each line contains two integers a and b: there is an edge between nodes a and b.
Output
Print n integers: for each node 1,2,\ldots,n, the maximum distance to another node.
Constraints

1 <= n <= 2 * 10^5
1 <= a, b <= n
"""

from collections import deque

def bfs(start, graph, n):
    dist = [-1] * (n + 1)
    q = deque()
    q.append(start)
    dist[start] = 0
    farthest_node = start

    while q:
        node = q.popleft()
        for neighbor in graph[node]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[node] + 1
                q.append(neighbor)
                if dist[neighbor] > dist[farthest_node]:
                    farthest_node = neighbor

    return farthest_node, dist

def tree_distances(n, edges):
    graph = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # 1st BFS to find one endpoint of the diameter
    node_a, _ = bfs(1, graph, n)

    # 2nd BFS from node_a to get distances and find node_b
    node_b, dist_from_a = bfs(node_a, graph, n)

    # 3rd BFS from node_b to get distances
    _, dist_from_b = bfs(node_b, graph, n)

    # Result: max of distance from node_a and node_b
    result = []
    for i in range(1, n + 1):
        result.append(max(dist_from_a[i], dist_from_b[i]))

    return result

# Input reading
n = int(input())
edges = []
for _ in range(n - 1):
    u, v = map(int, input().split())
    edges.append((u, v))

# Output
res = tree_distances(n, edges)
print(' '.join(map(str, res)))
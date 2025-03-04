"""
Number of connected components

You are given a graph with n vertices. To indicate the connections in the graph you are given 
an array edges whose each element is an array of the form [u,v]. [u,v] indicates that there is 
an edge between u and v where u and v denote two vertices or nodes. Write a function that takes 
in ‘n’ and the ‘edges’ array and returns the number of connected components in the graph.

"""


def buildAdjacencyList(n, edges):
    adjacency_list = [[] for _ in range(n)]
    for edge in edges:
        node1 = edge[0]
        node2 = edge[1]
        adjacency_list[node1].append(node2)
        adjacency_list[node2].append(node1)
    return adjacency_list

def dfs(graph, vertex, visited):
    visited[vertex] = True
    neighbours = graph[vertex]
    for neighbour in neighbours:
        if neighbour not in visited:
            dfs(graph, neighbour, visited)

def count_components(n, edges):
    graph = buildAdjacencyList(n, edges)
    visited = {}
    count = 0
    for vertex in range(n):
        if vertex not in visited:
            count += 1
            dfs(graph, vertex, visited)
    return count

n = 7
edges = [[0,1],[1,2],[3,4],[5,6]]
print(count_components(n, edges))
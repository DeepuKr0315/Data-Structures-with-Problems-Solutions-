# problem link = https://leetcode.com/problems/course-schedule/description/
# 207. Course Schedule

from collections import deque

def buildAdjList(n, prerecs):
    adjList = [[] for _ in range(n)]
    for prerec in prerecs:
        toTake, firstTake = prerecs
        adjList[firstTake].append(toTake)
    return adjList

def checkCycleBFS(vertex, graph):
    queue = deque()
    visited = {}
    for i in range(len(graph[vertex])):
        queue.append(graph[vertex][i])
    while queue:
        curr = queue.popleft()
        visited[curr] = True
        if curr == vertex:
            return True
        neighbours = graph[vertex]
        for neighbour in neighbours:
            if neighbour not in visited:
                queue.append(neighbour)
                visited[neighbour] = True
    return False

def canFinish(numCourses, prerequisites):
    adjList =  buildAdjList(numCourses, prerequisites)
    hasCycle = False
    for vertex in range(numCourses):
        hasCycle = checkCycleBFS(vertex, adjList)
        if hasCycle:
            return False
    return True
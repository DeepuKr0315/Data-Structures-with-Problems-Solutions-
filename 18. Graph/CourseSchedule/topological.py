
# problem link = https://leetcode.com/problems/course-schedule/description/
# 207. Course Schedule

def buildAdjList(n, prerecs):
    adjList = [[] for _ in range(n)]
    inDegree = [0 for _ in range(n)]
    for prerec in prerecs:
        toTake, firstTake = prerec
        adjList[firstTake].append(toTake)
        inDegree[toTake] += 1
    return adjList, inDegree

def canFinish(n, prerecs):
    stack = []
    adjList, inDegree = buildAdjList(n, prerecs)
    for i in range(n):
        if inDegree[i] == 0:
            stack.append(i)
    count = 0
    while stack:
        current = stack.pop()
        count += 1
        neighbours = adjList[current]
        for i in range(len(neighbours)):
            neighbour = neighbours[i]
            inDegree[neighbour] -= 1
            if inDegree[neighbour] == 0:
                stack.append(neighbour)
    return count == n
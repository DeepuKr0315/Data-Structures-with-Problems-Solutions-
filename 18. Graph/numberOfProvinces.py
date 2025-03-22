# Problem Link = https://leetcode.com/problems/number-of-provinces/description/
# 547. Number of Provinces

def findCircleNum(isConnected):
    def dfs(city):
        for neighbor, is_connected in enumerate(isConnected[city]):
            if is_connected and neighbor not in visited:
                visited.add(neighbor)
                dfs(neighbor)

    visited = set()
    n = len(isConnected)
    provinces = 0
    for city in range(n):
        if city not in visited:
            dfs(city)
            provinces += 1
    return provinces

isConnected = [[1,0,0],[0,1,0],[0,0,1]]
print(findCircleNum(isConnected))
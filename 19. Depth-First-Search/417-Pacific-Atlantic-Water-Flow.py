# Problem link = https://leetcode.com/problems/pacific-atlantic-water-flow/description/?envType=daily-question&envId=2025-10-05

from collections import deque
def pacificAtlantic(heights):
    if not heights or not heights[0]:
        return []

    m, n = len(heights), len(heights[0])
    res = []

    def bfs(i, j):
        q = deque([(i, j)])
        visited = [[False] * n for _ in range(m)]
        visited[i][j] = True
        pacific = atlantic = False

        while q:
            x, y = q.popleft()

            if x == 0 or y == 0:
                pacific = True
            if x == m - 1 or y == n - 1:
                atlantic = True

            if pacific and atlantic:
                return True

            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and heights[nx][ny] <= heights[x][y]:
                    visited[nx][ny] = True
                    q.append((nx, ny))

        return False

    for i in range(m):
        for j in range(n):
            if bfs(i, j):
                res.append([i, j])

    return res

heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
print(pacificAtlantic(heights))
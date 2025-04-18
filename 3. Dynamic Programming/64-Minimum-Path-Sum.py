# 64. Minimum Path Sum
# Problem link = https://leetcode.com/problems/minimum-path-sum/description/

def minPathSum(grid):
    row = len(grid)
    col = len(grid[0])
    dp = [[0] * col for _ in range(row)]
    dp[0][0] = grid[0][0]
    for i in range(row):
        for j in range(col):
            if i == 0 and j == 0:
                continue
            elif i == 0:
                dp[i][j] = dp[i][j - 1] + grid[i][j]
            elif j == 0:
                dp[i][j] = dp[i - 1][j] + grid[i][j]
            else:
                dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])
    return dp[row - 1][col - 1]

print(minPathSum(grid = [[1,3,1],[1,5,1],[4,2,1]]))
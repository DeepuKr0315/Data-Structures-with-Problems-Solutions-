# 64. Minimum Path Sum
# Problem link = https://leetcode.com/problems/minimum-path-sum/description/

def minPathSum(grid):
    def helper(i, j):
        if i == 0 and j == 0:
            return grid[0][0]
        elif i < 0 or j < 0:
            return float('inf')
        return grid[i][j] + min(helper(i - 1, j), helper(i, j - 1))

    return helper(len(grid) - 1, len(grid[0]) - 1)

print(minPathSum(grid = [[1,3,1],[1,5,1],[4,2,1]]))
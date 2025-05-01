# https://leetcode.com/problems/maximal-square/description/
# Maximal Square

def maximalSquare(matrix):
    rows, cols = len(matrix), len(matrix[0])
    cache = {}
    def helper(row, col):
        if row >= rows or col >= cols:
            return 0
        if (row, col) not in cache:
            down = helper(row + 1, col)
            right = helper(row, col + 1)
            diagonal = helper(row + 1, col + 1)
            cache[(row, col)] = 0
            if(matrix[row][col] == "1"):
                cache[(row, col)] = 1 + min(down, right, diagonal)
        return cache[(row, col)]
    helper(0, 0)
    return max(cache.values()) ** 2

def maximalSquare2(matrix):
    dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
    out = 0
    for i in range(len(matrix)):
        dp[i][0] = int(matrix[i][0])
        if dp[i][0] == 1:
            out = 1
    for j in range(len(matrix[0])):
        dp[0][j] = int(matrix[0][j])
        if dp[0][j] == 1:
            out = 1
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if matrix[i][j] == "1":
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1])
            out = max(out, dp[i][j])
    return out ** 2

matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(maximalSquare(matrix))
print(maximalSquare2(matrix))
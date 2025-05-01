# problem link = https://leetcode.com/problems/minimum-falling-path-sum/description/
# Minimum Falling Path Sum

def minFallin(matrix):
    N = len(matrix)
    for i in range(1, N):
        for j in range(N):
            middle = matrix[i - 1][j]
            left = matrix[i - 1][j - 1] if j > 0 else float('inf')
            right = matrix[i - 1][j + 1] if j < N - 1 else float('inf')
            matrix[i][j] = matrix[i][j] + min(middle, left, right)
    return min(matrix[-1])

matrix = [[-19,57],[-40,-5]]
print(minFallin(matrix))
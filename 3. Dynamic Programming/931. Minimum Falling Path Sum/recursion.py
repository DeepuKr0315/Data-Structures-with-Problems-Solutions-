# problem link = https://leetcode.com/problems/minimum-falling-path-sum/description/
# Minimum Falling Path Sum

def minFalling(matrix):
    N = len(matrix)
    def helper(row, col):
        if(row == N):
            return 0
        if(col == N or col < 0):
            return float('inf')
        result = matrix[row][col] + min(helper(row + 1, col - 1), helper(row + 1, col), helper(row + 1, col + 1))
        return result
    result = float('inf')
    for col in range(N):
        result = min(result, helper(0, col))
    return result

matrix = [[2,1,3],[6,5,4],[7,8,9]]
print(minFalling(matrix))
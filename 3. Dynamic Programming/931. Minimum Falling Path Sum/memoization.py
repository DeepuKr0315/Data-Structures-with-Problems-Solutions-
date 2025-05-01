# problem link = https://leetcode.com/problems/minimum-falling-path-sum/description/
# Minimum Falling Path Sum

def minFalling(matrix):
    N = len(matrix)
    check = {}
    def helper(row, col):
        if(row == N):
            return 0
        if(col == N or col < 0):
            return float('inf')
        if (row, col) in check:
            return check[(row, col)]
        result = matrix[row][col] + min(helper(row + 1, col - 1), helper(row + 1, col), helper(row + 1, col + 1))
        check[(row, col)] = result
        return result
    result = float('inf')
    for col in range(N):
        result = min(result, helper(0, col))
    return result

matrix = [[2,1,3],[6,5,4],[7,8,9]]
print(minFalling(matrix))
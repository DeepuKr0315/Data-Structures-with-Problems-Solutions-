# problem link = https://leetcode.com/problems/search-a-2d-matrix-ii/
def searchIn2D(matrix, target):
    row, col = len(matrix), len(matrix[0])
    top = 0
    bottom = row - 1
    while top <= bottom:
        middle = (top + bottom) // 2
        if matrix[middle][0] > target:
            bottom = middle - 1
        elif target > matrix[middle][col-1]:
            top = middle + 1
        else:
            break
    if top > bottom:
        return False
    left = 0
    right = col - 1
    while left <= right:
        mid = (left + right) // 2
        if matrix[middle][mid] == target:
            return True
        elif matrix[middle][mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return False

print(searchIn2D(matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20))
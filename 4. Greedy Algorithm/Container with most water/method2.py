# problem link = https://leetcode.com/problems/container-with-most-water/description/
# Two shifting pointers method

def maxArea(array):
    left, right = 0, len(array)-1
    max_Area = 0
    while left < right:
        area = min(array[left], array[right]) * (right - left)
        max_Area = max(max_Area, area)
        if array[left] < array[right]:
            left += 1
        else:
            right -= 1
    return max_Area

height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))
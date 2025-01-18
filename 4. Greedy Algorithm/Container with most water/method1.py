# problem link = https://leetcode.com/problems/container-with-most-water/description/

def maxArea(height):
    max_Area = 0
    n = len(height)
    for i in range(n - 1):
        for j in range(i + 1, n):
            area = min(height[i], height[j]) * (j - i)
            max_Area = max(area, max_Area)
    return max_Area

height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))
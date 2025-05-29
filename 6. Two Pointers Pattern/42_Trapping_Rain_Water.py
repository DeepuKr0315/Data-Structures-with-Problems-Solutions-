# Problem link = https://leetcode.com/problems/trapping-rain-water/description/

def trap(height):
    left = 0
    right = len(height) - 1
    leftMax = height[left]
    rightMax = height[right]
    res = 0
    while (left < right):
        if height[left] < height[right]:
            left += 1
            leftMax = max(height[left], leftMax)
            res += leftMax - height[left]
        else:
            right -= 1
            rightMax = max(height[right], rightMax)
            res += rightMax - height[right]
    return res

height = [4,2,0,3,2,5]
print(trap(height))
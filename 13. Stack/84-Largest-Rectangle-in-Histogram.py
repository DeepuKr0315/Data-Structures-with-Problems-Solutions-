# Problem link = https://leetcode.com/problems/largest-rectangle-in-histogram/description/

def largestRectangleArea(heights):
    stack = []
    n = len(heights)
    max_area = 0
    for i, h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h:
            index, height = stack.pop()
            max_area = max(max_area, height * (i - index))
            start = index
        stack.append((start, h))
    for index, height in stack:
        max_area = max(max_area, height * (n - index))
    return max_area

heights = [2,1,5,6,2,3]
print(largestRectangleArea(heights))
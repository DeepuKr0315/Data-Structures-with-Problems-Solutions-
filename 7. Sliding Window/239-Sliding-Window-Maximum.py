
# problem link = https://leetcode.com/problems/sliding-window-maximum/description/

from collections import deque
def maxSlidingWindow(nums, k):
    output = []
    dq = deque()
    for i in range(k):
        while dq and nums[i] >= nums[dq[-1]]:
            dq.pop()
        dq.append(i)
    output.append(nums[dq[0]])
    for i in range(k, len(nums)):
        if dq and dq[0] == i - k:
            dq.popleft()
        while dq and nums[i] >= nums[dq[-1]]:
            dq.pop()
        dq.append(i)
        output.append(nums[dq[0]])
    return output

print(maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3))
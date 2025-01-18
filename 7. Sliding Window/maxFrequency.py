
# problem link = https://leetcode.com/problems/frequency-of-the-most-frequent-element/description/

def freqElement(nums, k):
    nums.sort()
    left = 0
    total = 0
    res = 0
    for right in range(len(nums)):
        total += nums[right]
        # invalid window
        while total + k < nums[right] * (right-left+1):
            total -= nums[left]
            left += 1
        # valid window
        res = max(res, right - left + 1)
    return res
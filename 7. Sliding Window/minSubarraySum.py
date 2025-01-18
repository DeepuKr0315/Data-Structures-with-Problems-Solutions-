
# problem link = https://leetcode.com/problems/minimum-size-subarray-sum/description/

def minSubarraySum(target, nums):
    left = 0
    currentSum = 0
    length = float('inf')
    for right in range(len(nums)):
        currentSum += nums[right]
        while currentSum >= target:
            newLen = right - left + 1
            if newLen < length:
                length = newLen
            currentSum -= nums[left]
            left += 1
    return length if length != float('inf') else 0

target = 7
nums = [2,3,1,2,4,3]
print(minSubarraySum(target, nums))
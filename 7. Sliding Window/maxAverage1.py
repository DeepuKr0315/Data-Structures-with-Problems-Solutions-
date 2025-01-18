
# problem link = https://leetcode.com/problems/maximum-average-subarray-i/description/

def maxAverage(nums, k):
    currSum = sum(nums[:k])
    maxSum = currSum
    for i in range(k, len(nums)):
        currSum += nums[i] - nums[i-k]
        maxSum = max(maxSum, currSum)
    return maxSum / float(k)

print(maxAverage([1, 13, -6, -3, 40, 2], k = 4))
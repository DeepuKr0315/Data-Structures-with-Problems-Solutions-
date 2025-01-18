# problem link = https://leetcode.com/problems/partition-equal-subset-sum/

def canPartition(self, nums):
    if sum(nums)%2 != 0:
        return False
        memo = {}
    total_sum = sum(nums)//2
    def helper(index, rem_sum):
        if rem_sum == 0:
            return True
        if index >= len(nums) or rem_sum < 0:
            return False
        if (index, rem_sum) in memo:
            return memo[(index,rem_sum)]
        include = helper(index+1, rem_sum-nums[index])
        exclude = helper(index+1, rem_sum)

        memo[(index, rem_sum)] = include or exclude
        return memo[(index, rem_sum)]
    return helper(0, total_sum)
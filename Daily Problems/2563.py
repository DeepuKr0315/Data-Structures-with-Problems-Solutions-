# 2563. Count the Number of Fair Pairs
# problem link = https://leetcode.com/problems/count-the-number-of-fair-pairs/description/

def countFairPairs(nums, upper, lower):
    nums.sort()
    def helper(target):
        count = 0
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] <= target:
                count += right - left
                left += 1
            else:
                right -= 1
        return count
    upper_limit = helper(upper)
    lower_limit = helper(lower - 1)
    return upper_limit - lower_limit

print(countFairPairs(nums = [0,1,7,4,4,5], lower = 3, upper = 6))
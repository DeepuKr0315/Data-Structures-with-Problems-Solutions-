# problem link = https://leetcode.com/problems/two-sum/description/

def twoSum(nums, target):
    num_available = {}
    for i in range(len(nums)):
        need_val = target - nums[i]
        if need_val in num_available:
            return [num_available[need_val], i]
        else:
            num_available[nums[i]] = i
    return []

nums = [2, 15, 11, 7]
target = 9
print(twoSum(nums, target))
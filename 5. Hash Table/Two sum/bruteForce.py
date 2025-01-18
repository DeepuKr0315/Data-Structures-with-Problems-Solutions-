# problem link = https://leetcode.com/problems/two-sum/description/

def twoSum(nums, target):
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[j] + nums[i] == target:
                return [i, j]
    return [-1, -1]

nums = [2, 15, 11, 7]
target = 9
print(twoSum(nums, target))